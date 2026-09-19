import math
import numpy as np


def nested_residuals(blocks, eps):
    """Return nested supports and unit normals e_r for the sharpness family."""
    k1 = blocks[0]
    n = sum(blocks) + 1
    levels = []
    e = np.zeros(n)
    e[: k1 + 1] = 1.0 / math.sqrt(k1 + 1)
    end = k1 + 1
    levels.append((end, e.copy()))
    for r, kr in enumerate(blocks[1:], start=2):
        theta = eps ** (2 ** (r - 2))
        w = np.zeros(n)
        w[end : end + kr] = 1.0 / math.sqrt(kr)
        e = math.cos(theta) * e + math.sin(theta) * w
        end += kr
        levels.append((end, e.copy()))
    return levels


def msarp_hole_distribution(blocks, eps):
    levels = nested_residuals(blocks, eps)
    k1 = blocks[0]
    n = sum(blocks) + 1
    # First projection DPP: omit one point from the first simplex block.
    probs = np.zeros(n)
    probs[: k1 + 1] = 1.0 / (k1 + 1)
    prev_end = k1 + 1
    for (r, kr) in enumerate(blocks[1:], start=2):
        end, e = levels[r - 1]
        new_probs = np.zeros(n)
        new_idx = list(range(prev_end, end))
        for h in range(prev_end):
            if probs[h] == 0:
                continue
            candidates = [h] + new_idx
            weights = np.array([e[j] ** 2 for j in candidates])
            weights /= weights.sum()
            for j, w in zip(candidates, weights):
                new_probs[j] += probs[h] * w
        probs = new_probs
        prev_end = end
    return probs, levels[-1][1]


def projection_ratio_per_omission(e, sigma):
    x = e * e
    return 1.0 / (sigma * sigma * (1.0 - x) + x)


def oblique_expected_ratio(blocks, eps):
    probs, e = msarp_hole_distribution(blocks, eps)
    return float(np.sum(probs / (e * e)))


def orthogonal_expected_ratio(blocks, eps):
    probs, e = msarp_hole_distribution(blocks, eps)
    theta_last = eps ** (2 ** (len(blocks) - 2)) if len(blocks) > 1 else eps
    sigma = math.sin(theta_last) ** 2 if len(blocks) > 1 else eps * eps
    ratios = projection_ratio_per_omission(e, sigma)
    staged = float(probs @ ratios)
    one_shot = float((e * e) @ ratios)
    return staged, one_shot, sigma, e


def null_basis(e):
    # Orthonormal basis for e^perp.
    _, _, vh = np.linalg.svd(e.reshape(1, -1), full_matrices=True)
    return vh[1:, :].T


def direct_projection_ratios(e, sigma):
    V = null_basis(e)
    O = np.column_stack([V, e])
    D = np.diag([1.0] * (len(e) - 1) + [sigma])
    A = D @ O.T
    out = []
    for j in range(len(e)):
        U = [i for i in range(len(e)) if i != j]
        C = A[:, U]
        Q, _ = np.linalg.qr(C, mode="reduced")
        err2 = np.linalg.norm(A - Q @ (Q.T @ A), "fro") ** 2
        out.append(err2 / (sigma * sigma))
    return np.array(out)


def check_two_stage_closed_form(k, p, theta):
    blocks = [k, p]
    # For two stages eps=theta exactly.
    probs, e = msarp_hole_distribution(blocks, theta)
    s2 = math.sin(theta) ** 2
    predicted_oblique = (k + 1) * (p + 1) / (1.0 + k * s2)
    actual_oblique = float(np.sum(probs / (e * e)))
    return actual_oblique, predicted_oblique


if __name__ == "__main__":
    print("Two-stage exact identity (k=2, p=3):")
    for theta in (0.30, 0.15, 0.07):
        actual, predicted = check_two_stage_closed_form(2, 3, theta)
        print(f"theta={theta:.3f}  enumerated={actual:.12f}  formula={predicted:.12f}  diff={actual-predicted:+.3e}")

    print("\nThree-stage family blocks=(2,2,1):")
    blocks = [2, 2, 1]
    product = math.prod(k + 1 for k in blocks)
    dplus1 = sum(blocks) + 1
    print(f"product bound={product}, one-shot bound={dplus1}")
    for eps in (0.30, 0.20, 0.12, 0.08):
        obl = oblique_expected_ratio(blocks, eps)
        ort, one, sigma, e = orthogonal_expected_ratio(blocks, eps)
        print(
            f"eps={eps:.3f} sigma={sigma:.3e}  oblique={obl:.9f}  "
            f"orthogonal={ort:.9f}  one-shot={one:.9f}  min|e|={np.min(np.abs(e)):.3e}"
        )

    print("\nDirect matrix check at eps=0.20:")
    eps = 0.20
    probs, e = msarp_hole_distribution(blocks, eps)
    theta_last = eps ** 2
    sigma = math.sin(theta_last) ** 2
    formula = projection_ratio_per_omission(e, sigma)
    direct = direct_projection_ratios(e, sigma)
    print(f"max per-omission discrepancy={np.max(np.abs(formula-direct)):.3e}")
    print(f"staged formula={probs @ formula:.12f}")
    print(f"staged direct ={probs @ direct:.12f}")

    print("\nSingleton stages blocks=(1,1,1,1):")
    blocks = [1, 1, 1, 1]
    product = 2 ** len(blocks)
    dplus1 = sum(blocks) + 1
    print(f"product bound={product}, one-shot bound={dplus1}")
    for eps in (0.35, 0.25, 0.18):
        obl = oblique_expected_ratio(blocks, eps)
        ort, one, sigma, e = orthogonal_expected_ratio(blocks, eps)
        print(
            f"eps={eps:.3f} sigma={sigma:.3e}  oblique={obl:.9f}  "
            f"orthogonal={ort:.9f}  one-shot={one:.9f}"
        )
