"""Finite numerical and exact checks of the weighted wheel average-mixing spectrum.

Uses direct symmetric diagonalization for the left-hand side and cyclic
Fourier projectors for the right-hand side.  Only finite tests are performed;
the theorem for all rim orders and positive couplings requires its proof.
"""
import math
import numpy as np


def weighted_wheel(n, g):
    assert isinstance(n, int) and n >= 3 and g > 0
    a = np.zeros((n + 1, n + 1))
    for j in range(n):
        a[0, 1 + j] = g
        a[1 + j, 0] = g
        a[1 + j, 1 + (j + 1) % n] = 1.
        a[1 + (j + 1) % n, 1 + j] = 1.
    return a


def direct_average(a):
    values, vectors = np.linalg.eigh(a)
    groups = []
    for j, v in enumerate(values):
        if not groups or abs(v - values[groups[-1][0]]) > 1.e-8:
            groups.append([j])
        else:
            groups[-1].append(j)
    ans = np.zeros_like(a)
    for inds in groups:
        e = vectors[:, inds] @ vectors[:, inds].T
        ans += e * e
    return ans, len(groups)


def collision_indices(n):
    return [k for k in range(1, n // 2 + 1)
            if k < n / 2 + 1.e-12 and 2 * math.cos(2 * math.pi * k / n) < -1.e-12]


def collision_coupling(n, k):
    theta = 2. * math.cos(2 * math.pi * k / n)
    assert theta < 0.
    return math.sqrt(theta * (theta - 2.) / n)


def cyclic_projector(n, k):
    indices = np.arange(n)
    diffs = indices[:, None] - indices[None, :]
    if n % 2 == 0 and k == n // 2:
        return ((-1.) ** diffs) / n
    return (2. / n) * np.cos(2. * math.pi * k * diffs / n)


def closed_average(n, g, resonance_index=None):
    sigma = math.sqrt(1. + n * g * g)
    bplus = (1. + 1. / sigma) / 2.
    bminus = (1. - 1. / sigma) / 2.
    result = np.zeros((n + 1, n + 1))
    result[0, 0] = (1. + 1. / sigma**2) / 2.
    result[0, 1:] = result[1:, 0] = g * g / (2. * sigma**2)
    block = ((bplus**2 + bminus**2) / (n*n)) * np.ones((n, n))
    for k in range(1, (n // 2) + 1):
        if 2 * k == n or 2 * k < n:
            q = cyclic_projector(n, k)
            block += q * q
    if resonance_index is not None:
        block += ((1. - 1. / sigma) / n) * cyclic_projector(n, resonance_index)
    result[1:, 1:] = block
    return result


def closed_spectrum(n, g, resonance_index=None):
    beta = (2. + (n - 1.) * g*g) / (2. * (1. + n*g*g))
    alpha = (1. - 1. / math.sqrt(1. + n*g*g)) / n
    values = [1., beta]
    for freq in range(1, n):
        base = 1. / n if n % 2 else (2. / n if freq % 2 == 0 else 0.)
        if resonance_index is not None and (freq == resonance_index or
                                             freq == n - resonance_index):
            base += alpha
        values.append(base)
    return np.sort(values)


def rank_theorem(n, k=None):
    if n % 2:
        return n + 1
    base = n // 2 + 1
    if k is None or k % 2 == 0:
        return base
    return base + (1 if k == n // 2 else 2)


def numerical_tests():
    tested = 0
    resonant = 0
    maxmatrix = 0.
    maxspectral = 0.
    maxstochastic = 0.
    maxker = 0.
    for n in range(3, 29):
        cases = [(g, next((k for k in collision_indices(n)
                            if abs(g-collision_coupling(n,k)) < 1.e-12), None))
                 for g in (0.19, 0.5, 0.9, 1.7, 2.31)]
        for k in collision_indices(n):
            gc = collision_coupling(n, k)
            cases.extend([(gc, k), (gc * 0.999, None), (gc * 1.001, None)])
        for g, k in cases:
            a = weighted_wheel(n, g)
            actual, groups = direct_average(a)
            expected = closed_average(n, g, k)
            spec = np.linalg.eigvalsh(actual)
            analytic = closed_spectrum(n, g, k)
            maxmatrix = max(maxmatrix, np.max(abs(actual - expected)))
            maxspectral = max(maxspectral, np.max(abs(spec - analytic)))
            maxstochastic = max(maxstochastic, np.max(abs(actual.sum(axis=1) - 1)))
            r_actual = int(np.count_nonzero(spec > 1.e-7))
            r_exp = rank_theorem(n, k)
            assert r_actual == r_exp, ('rank', n, g, k, r_actual, r_exp)
            if n % 2 == 0:
                for f in range(1, n, 2):
                    if k is not None and (f == k or f == n - k):
                        continue
                    w = np.r_[0., np.exp(2j*np.pi*f*np.arange(n)/n)]
                    maxker = max(maxker, float(np.linalg.norm(actual @ w)))
            tested += 1
            resonant += int(k is not None)
    assert maxmatrix < 3e-12, maxmatrix
    assert maxspectral < 3e-12, maxspectral
    assert maxstochastic < 3e-12, maxstochastic
    assert maxker < 3e-12, maxker
    return tested, resonant, maxmatrix, maxspectral, maxker


def exact_tests():
    import sympy as s
    passed = 0
    # All matrix identities in this test are over Q(sqrt(3)); no floating point.
    for n, g, k in [(6, 2 / s.sqrt(3), 3), (6, 1 / s.sqrt(2), 2),
                     (8, s.Integer(1), 4)]:
        sig = s.sqrt(1 + n*g*g)
        am = s.zeros(n+1)
        for j in range(n):
            am[0,j+1]=g; am[j+1,0]=g
            am[j+1,(j+1)%n+1]=1; am[(j+1)%n+1,j+1]=1
        u=s.ones(n,1)/s.sqrt(n)
        outer=u*u.T
        projs=[]
        for sign in [+1,-1]:
            ah=(1-sign/sig)/2
            br=(1+sign/sig)/2
            off=sign*g/(2*sig)
            ee=s.zeros(n+1)
            ee[0,0]=ah
            for i in range(n):
                ee[0,i+1]=off;ee[i+1,0]=off
                for j in range(n):ee[i+1,j+1]=br/n
            projs.append(ee)
        for r in range(1,n//2+1):
            qr=s.Matrix(n,n,lambda i,j: (s.Integer(-1)**(i-j))/n
              if 2*r==n else 2*s.cos(2*s.pi*r*(i-j)/n)/n)
            er=s.zeros(n+1)
            for i in range(n):
                for j in range(n):er[i+1,j+1]=qr[i,j]
            projs.append(er)
        # Merge precisely the unique resonant projectors.
        fused=projs[1]+projs[1+k]
        parts=[projs[0],fused]+[projs[1+r] for r in range(1,n//2+1) if r!=k]
        assert all(s.simplify((p*p-p)).is_zero_matrix for p in parts)
        assert s.simplify(sum(parts,s.zeros(n+1))-s.eye(n+1)).is_zero_matrix
        exact_m=s.zeros(n+1)
        for p in parts:exact_m+=p.multiply_elementwise(p)
        pred=s.zeros(n+1)
        a=(1+1/sig**2)/2
        b=g*g/(2*sig**2)
        bplus=(1+1/sig)/2
        bminus=(1-1/sig)/2
        pred[0,0]=a
        for i in range(n):
            pred[0,i+1]=b;pred[i+1,0]=b
        for i in range(n):
            for j in range(n):
                vij=(bplus*bplus+bminus*bminus)/n**2
                for r in range(1,n//2+1):
                    q=(s.Integer(-1)**(i-j)/n if 2*r==n else
                        2*s.cos(2*s.pi*r*(i-j)/n)/n)
                    vij+=q*q
                    if r==k:vij+=(1-1/sig)*q/n
                pred[i+1,j+1]=vij
        assert s.simplify(pred-exact_m).is_zero_matrix
        expected_nonzero=rank_theorem(n,k)
        assert pred.rank() == expected_nonzero
        passed+=1
    return passed


if __name__=='__main__':
    count, reson, diff, spec, ker=numerical_tests()
    exact=exact_tests()
    print(f'VERIFY_OK numerical_cases={count} exact_symbolic_cases={exact} '
          f'exact_matrix_identities={exact} resonances={reson} '
          f'worst_matrix_error={diff:.3g} worst_spectrum_error={spec:.3g} '
          f'worst_kernel_residual={ker:.3g} '
          f'n6_k3_rank={rank_theorem(6,3)}/7 '
          f'n8_k3_rank={rank_theorem(8,3)}/9')
