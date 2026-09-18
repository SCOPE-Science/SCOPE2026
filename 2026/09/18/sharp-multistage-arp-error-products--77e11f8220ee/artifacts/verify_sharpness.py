import math
import numpy as np


def initial_state(k1):
    z = np.full(k1 + 1, 1.0 / math.sqrt(k1 + 1))
    p = z * z
    return z, p


def extend_state(z, p, k, eps):
    a = math.sqrt(1.0 - k * eps * eps)
    z_new = np.concatenate([a * z, np.full(k, eps)])
    p_new = np.zeros_like(z_new)
    old_n = len(z)
    for j, pj in enumerate(p):
        den = a * a * z[j] * z[j] + k * eps * eps
        p_new[j] += pj * (a * a * z[j] * z[j]) / den
        for ell in range(k):
            p_new[old_n + ell] += pj * eps * eps / den
    assert abs(np.sum(p_new) - 1.0) < 1e-12
    assert abs(np.dot(z_new, z_new) - 1.0) < 1e-12
    return z_new, p_new


def staged_state(stage_sizes, epsilons):
    z, p = initial_state(stage_sizes[0])
    for k, eps in zip(stage_sizes[1:], epsilons):
        z, p = extend_state(z, p, k, eps)
    return z, p


def oblique_ratio(z, p):
    return float(np.sum(p / (z * z)))


def css_ratio(z, p, delta):
    den = z * z + delta * delta * (1.0 - z * z)
    return float(np.sum(p / den))


def one_shot_css_ratio(z, delta):
    den = z * z + delta * delta * (1.0 - z * z)
    return float(np.sum((z * z) / den))


def nested_basis(stage_sizes, epsilons):
    k1 = stage_sizes[0]
    z = np.full(k1 + 1, 1.0 / math.sqrt(k1 + 1))
    # Deterministic orthonormal basis of z^perp.
    cols = []
    for i in range(k1 + 1):
        v = np.eye(k1 + 1)[:, i].copy()
        v -= z * np.dot(z, v)
        for q in cols:
            v -= q * np.dot(q, v)
        nrm = np.linalg.norm(v)
        if nrm > 1e-12 and len(cols) < k1:
            cols.append(v / nrm)
    V = np.column_stack(cols)
    block_ends = [k1]
    for k, eps in zip(stage_sizes[1:], epsilons):
        a = math.sqrt(1.0 - k * eps * eps)
        z_new = np.concatenate([a * z, np.full(k, eps)])
        V_old = np.vstack([V, np.zeros((k, V.shape[1]))])
        cols_new = [V_old[:, j].copy() for j in range(V_old.shape[1])]
        for i in range(len(z_new)):
            v = np.eye(len(z_new))[:, i].copy()
            v -= z_new * np.dot(z_new, v)
            for q in cols_new:
                v -= q * np.dot(q, v)
            nrm = np.linalg.norm(v)
            if nrm > 1e-12 and len(cols_new) < len(z_new) - 1:
                cols_new.append(v / nrm)
        V = np.column_stack(cols_new)
        z = z_new
        block_ends.append(V.shape[1])
    return V, z, block_ends


def check_two_stage_formula(k, p, eps):
    z, probs = staged_state([k, p], [eps])
    observed = oblique_ratio(z, probs)
    formula = (k + 1) * (p + 1) / (1.0 + k * p * eps * eps)
    bad_prob = p * (k + 1) * eps * eps / (1.0 + k * p * eps * eps)
    # In this symmetric family, all tail omissions have ratio eps^{-2}.
    second_tail = bad_prob / (eps ** 4)
    return observed, formula, bad_prob, second_tail


if __name__ == "__main__":
    print("Two-stage exact formula checks")
    for k, p, eps in [(1, 1, 0.1), (2, 1, 0.1), (2, 2, 0.08), (3, 2, 0.05)]:
        obs, formula, bad, tail_second = check_two_stage_formula(k, p, eps)
        print(f"k={k}, p={p}, eps={eps:.3g}: mean={obs:.12f}, formula={formula:.12f}, "
              f"bad_prob={bad:.8f}, tail_second_moment={tail_second:.6f}")
        assert abs(obs - formula) < 1e-11

    print("\nMultistage sharpness checks")
    cases = [
        ([1, 1, 1], [0.05, 0.001]),
        ([2, 1, 2], [0.05, 0.001]),
        ([1, 1, 1, 1], [0.04, 0.002, 0.0001]),
    ]
    delta = 1e-11
    for ks, eps in cases:
        z, probs = staged_state(ks, eps)
        staged_obl = oblique_ratio(z, probs)
        product_bound = float(np.prod([k + 1 for k in ks]))
        d = sum(ks)
        one_obl = d + 1.0
        staged_css = css_ratio(z, probs, delta)
        one_css = one_shot_css_ratio(z, delta)
        print(f"stages={ks}: staged_oblique={staged_obl:.12f}, product={product_bound:.12f}, "
              f"one_shot_oblique={one_obl:.12f}, staged_css={staged_css:.12f}, "
              f"one_shot_css={one_css:.12f}")
        assert staged_obl <= product_bound + 1e-10
        assert abs(staged_css - staged_obl) < 1e-6
        assert abs(one_css - one_obl) < 1e-6

        V, z_basis, _ = nested_basis(ks, eps)
        ortho = np.linalg.norm(V.T @ V - np.eye(V.shape[1]), ord=np.inf)
        nullres = np.linalg.norm(V.T @ z_basis, ord=np.inf)
        zmatch = min(np.linalg.norm(z - z_basis), np.linalg.norm(z + z_basis))
        print(f"  basis residuals: orthogonality={ortho:.3e}, null={nullres:.3e}, zmatch={zmatch:.3e}")
        assert ortho < 1e-10 and nullres < 1e-10 and zmatch < 1e-10
