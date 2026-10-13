"""Independent finite-dimensional checks for a weighted local-reset channel theorem.

Dependencies: NumPy. Run: python verify.py
"""
import itertools
import math
import numpy as np

rng = np.random.default_rng(250402651)
plus = np.array([1.0, 1.0], dtype=complex) / math.sqrt(2)
minus = np.array([1.0, -1.0], dtype=complex) / math.sqrt(2)


def tensor(*factors):
    v = np.array([1.0 + 0j])
    for a in factors:
        v = np.kron(v, a)
    return v


def kraus(n, site, bit):
    factors = [np.eye(2, dtype=complex) for _ in range(n)]
    basis = np.eye(2, dtype=complex)[bit]
    factors[site] = np.outer(plus, basis)
    k = factors[0]
    for f in factors[1:]:
        k = np.kron(k, f)
    return k


def single_site_reset(n, site, rho):
    return sum((k := kraus(n, site, b)) @ rho @ k.conj().T for b in (0, 1))


def weighted_channel(n, weights, rho):
    return sum(w * single_site_reset(n, i, rho) for i, w in enumerate(weights))


def mask_probabilities(n, weights, steps):
    v = np.zeros(1 << n)
    v[0] = 1.0
    for _ in range(steps):
        nxt = np.zeros_like(v)
        for mask, p in enumerate(v):
            for i, w in enumerate(weights):
                nxt[mask | (1 << i)] += w * p
        v = nxt
    return v


def inclusion_exclusion(weights, steps):
    n = len(weights)
    out = 0.0
    for mask in range(1, 1 << n):
        missing_weight = sum(weights[i] for i in range(n) if mask & (1 << i))
        term = (1.0 - missing_weight)**steps
        out += (1.0 if mask.bit_count() % 2 else -1.0) * term
    return out


def trace_norm_hermitian(a):
    return float(np.sum(np.abs(np.linalg.eigvalsh((a + a.conj().T) / 2))))


def random_density(d):
    z = rng.standard_normal(d) + 1j * rng.standard_normal(d)
    z /= np.linalg.norm(z)
    return np.outer(z, z.conj())


def test(n, weights, steps):
    d = 1 << n
    rho = random_density(d)
    probs = mask_probabilities(n, weights, steps)
    assert abs(probs.sum() - 1.0) < 5e-13
    tail = 1.0 - probs[-1]
    assert abs(tail - inclusion_exclusion(weights, steps)) < 4e-12
    output = rho.copy()
    for _ in range(steps):
        output = weighted_channel(n, weights, output)
    mixture = np.zeros((d, d), dtype=complex)
    for mask, p in enumerate(probs):
        x = rho.copy()
        for i in range(n):
            if mask & (1 << i):
                x = single_site_reset(n, i, x)
        mixture += p*x
    assert np.linalg.norm(output - mixture) < 3e-12
    pvec = tensor(*([plus] * n))
    stationary = np.outer(pvec, pvec.conj())
    assert trace_norm_hermitian(output - stationary) <= 2 * tail + 4e-12
    mvec = tensor(*([minus] * n))
    minus_input = np.outer(mvec, mvec.conj())
    output_w = minus_input.copy()
    for _ in range(steps):
        output_w = weighted_channel(n, weights, output_w)
    assert abs(trace_norm_hermitian(output_w - stationary) / 2 - tail) < 3e-12

    if n < 4:
        rdim = 2
        joint = random_density(d * rdim)
        transformed = joint.copy()
        for _ in range(steps):
            updated = np.zeros_like(transformed)
            for i, w in enumerate(weights):
                for b in (0, 1):
                    k = np.kron(kraus(n, i, b), np.eye(rdim))
                    updated += w * k @ transformed @ k.conj().T
            transformed = updated
        reduced_reference = np.trace(joint.reshape(d, rdim, d, rdim), axis1=0, axis2=2)
        target = np.kron(stationary, reduced_reference)
        assert trace_norm_hermitian(transformed - target) <= 2 * tail + 4e-12


def uniform_cover_prob(n, steps):
    probs = [0.0] * (n + 1)
    probs[0] = 1.0
    for _ in range(steps):
        nxt = [0.0] * (n + 1)
        for k in range(n + 1):
            if probs[k]:
                nxt[k] += probs[k] * k / n
                if k < n:
                    nxt[k + 1] += probs[k] * (n - k) / n
        probs = nxt
    return 1 - probs[n]


checks = 0
for n in range(1, 4):
    for _ in range(5):
        w = rng.uniform(0.15, 1.2, n)
        w = w / w.sum()
        for m in range(7):
            test(n, w, m)
            checks += 1

def arbitrary_dimension_check(dims, local_probabilities, weights, steps):
    """Verify a product nonuniform qsample and its grand-coupling Kraus map."""
    n = len(dims)
    d = math.prod(dims)
    local_phi = [np.sqrt(p).astype(complex) for p in local_probabilities]
    target_v = tensor(*local_phi)
    target = np.outer(target_v, target_v.conj())
    orth = []
    for phi in local_phi:
        v = np.zeros(len(phi), dtype=complex)
        v[0] = -phi[1]
        v[1] = phi[0]
        v /= np.linalg.norm(v)
        orth.append(v)
    v = tensor(*orth)
    state = np.outer(v, v.conj())
    mats = []
    for i, w in enumerate(weights):
        for b in range(dims[i]):
            factors = [np.eye(di, dtype=complex) for di in dims]
            factors[i] = np.outer(local_phi[i], np.eye(dims[i], dtype=complex)[b])
            k = factors[0]
            for other in factors[1:]:
                k = np.kron(k, other)
            mats.append(math.sqrt(w) * k)
    completeness = sum(k.conj().T @ k for k in mats)
    assert np.linalg.norm(completeness - np.eye(d)) < 1e-12
    output = state.copy()
    for _ in range(steps):
        output = sum(k @ output @ k.conj().T for k in mats)
    tail = inclusion_exclusion(weights, steps)
    assert abs(trace_norm_hermitian(output - target)/2 - tail) < 3e-12


for m in range(8):
    arbitrary_dimension_check((2, 3), ([0.2, 0.8], [0.1, 0.35, 0.55]),
                              (0.3, 0.7), m)
    checks += 1

for n in (100, 250, 500):
    for c in (-1.0, 0.0, 1.0):
        t = math.floor(n * math.log(n) + c*n)
        computed = uniform_cover_prob(n, t)
        limit = 1 - math.exp(-math.exp(-c))
        assert abs(computed - limit) < 0.05, (n, c, computed, limit)
        checks += 1

print('VERIFY_OK', checks, 'independent Kraus, reference, masks, inclusion-exclusion and Gumbel tests')
