# Independent scientific audit — SCOPE-20260920-47dbba32618f

Audited at: 2026-10-01T20:13:40.771389Z

Disposition: **passed**

## Correctness — PASS

Dividing the exact split-skew recurrence by \(1+i\gamma\tau\) gives the stated quadratic. The two Schur-Cohn inequalities simplify to the displayed factorization; for \(\theta>1/2\) the second inequality is exactly the finite threshold when \(0\le\gamma<2\theta+1\) and is positive for every finite \(\tau\) when \(\gamma\ge2\theta+1\). The first Schur inequality is weaker on the finite-threshold region. Differentiating the exact threshold function gives the two competing minima; at \(\theta=(1+\sqrt3)/4\) they tie at \(\gamma=0\) and \(\gamma=1/2\), and the one-sided test functions prove global max-min optimality. The committed root checker independently verifies boundary moduli, representative phase points, the \(\theta=1\) reduction, and the numerical constant.

### Correctness sources

- assigned RESULT.md
- assigned artifacts/verify_split_skew_reflection.py
- https://arxiv.org/abs/2609.15936
- https://arxiv.org/abs/2609.18373

### Correctness risks

- The theorem is exact only for the planar split-skew family; it is not a universal convergence theorem for arbitrary monotone inclusions.

## Originality — PASS

The directly relevant constant-reflection paper has now been read in full: it proves the admissible coefficient range \(\theta>1/2\), a general sufficient step bound, and the sharp pure-forward rotation slice, but it does not analyze the nonzero split-skew resolvent family or optimize the worst split-skew ceiling over \(\theta\). Shehu gives the exact split-skew threshold only at standard reflection \(\theta=1\). The closest published record located for the same skew family optimizes convergence rate at \(\theta=1\), a different objective.

### Equivalent formulations

No located equivalent formulation contains the joint \((\theta,\gamma)\) phase diagram or the equioscillating max-min constant.

### Broader coverage

These sources dominate individual slices but neither implies the all-reflection split-skew threshold or its global tuning optimum.

### Exact database or table

No existing exact table or published finding located contains the audited optimizer.

### Claim versus prior implication

The final claim requires solving the full Schur-Cohn inequalities with both parameters free and then performing a nontrivial global minimax calculation.

### Sources inspected

- An Adaptive Linesearch-free Method for Monotone Variational Inequalities under Local Lipschitz Continuity — https://arxiv.org/abs/2609.15936. NOT_COVERING: It covers the coefficient range and \(\gamma=0\) slice but not the nonzero split-skew phase diagram or max-min tuning.
- The sharp step-size constant for one-call reflection splittings on monotone inclusions — https://arxiv.org/abs/2609.18373. COVERING_SLICE: It gives the \(\theta=1\) threshold recovered by the audited formula, not the reflection-parameter optimization.

### Checked sources

- https://arxiv.org/abs/2609.15936
- https://arxiv.org/abs/2609.18373
- https://arxiv.org/abs/1908.05699
- https://arxiv.org/abs/2509.02005
- published record 2026/09/19/rate-optimal-frb-skew-rotations--689d5e743c56

### Residual risks

- Very recent parallel work could exist, but the most direct constant-reflection and split-skew primary sources were inspected in full.

## Value — PASS

The result identifies the exact obstruction surface for a canonical two-parameter monotone-inclusion test family and shows that standard reflection is not robustly optimal even within that family. The explicit equioscillating optimizer raises the exact split-skew ceiling by about 15.17%, giving a mathematically motivated target for sharper general convergence or obstruction results.

### Value sources

- https://arxiv.org/abs/2609.15936
- https://arxiv.org/abs/2609.18373

### Value risks

- The value is as an exact obstruction/tuning theorem; no universal convergence improvement is proved.

## Limitations

- The theorem is exact for \(A=\gamma L J\) and \(B=LJ\) in the plane.
- It gives necessary obstruction ceilings for universal theorems, not a universal sufficient step-size theorem.
- Finite-precision numerical behavior is not part of the claim.
