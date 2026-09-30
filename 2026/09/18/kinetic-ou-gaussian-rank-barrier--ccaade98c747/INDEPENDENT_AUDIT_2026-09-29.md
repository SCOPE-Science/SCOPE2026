# Independent audit — A sharp Gaussian-rank barrier for kinetic Ornstein--Uhlenbeck innovations

**Audit date:** 2026-09-29 (UTC)
**Source path:** `2026/09/18/kinetic-ou-gaussian-rank-barrier--ccaade98c747`
**Audited tree:** `be6facda096a4474217427a00d37f40028433882`

## Disposition

**PASSED.** The record survives independent review on correctness, originality, and scientific value without a substantive research-file change.

## Correctness

The covariance, rank obstruction, sharp rank-d Bures--Wasserstein error, and small-step constant are correct. Variation of constants and Ito isometry give the displayed 2-by-2 covariance block. Its determinant factorization is positive for every h>0, hence the exact joint (X,V) innovation has rank 2d. Any affine image of one d-dimensional standard normal has covariance rank at most d, whereas two d-dimensional normals suffice by Cholesky. The Gaussian W2 problem reduces to rank-d Bures approximation, whose minimum discards the d copies of the smaller eigenvalue, giving d lambda_-(h); series expansion gives lambda_-(h)=gamma alpha h^3/6+O(h^4).

### Independent checks

- Re-derived A_h, B_h, and C_h directly from the two stochastic convolution kernels by Ito isometry.
- Verified the determinant reduction to q(x)=e^x(x-2)+x+2 with q(0)=q'(0)=0 and q''(x)=x e^x>0, proving strict positive definiteness for h>0.
- Checked that rank(LL^T)<=d for a 2d-by-d affine Gaussian map and that a 2-by-2 Cholesky factor tensored with I_d realizes the exact covariance with two d-normal draws.
- Applied the Gaussian Bures formula and Eckart--Young to the square-root matrices; the spectral rank-d truncation attains squared error d lambda_-(h).
- Independently expanded the covariance entries and eigenvalue: det(A,B,C)=h^4/12+O(h^5) and lambda_-(h)=gamma alpha h^3/6+O(h^4).

## Originality

PASS with a deliberately narrow resource-model claim. The first 12 pages of Lyu--Wang--Yang's September 2026 ULMC preprint were independently retrieved and inspected: they explicitly formulate low-cost methods using two correlated Gaussian random vectors per iteration and compare this count with one- and three-Gaussian methods, but they do not state a necessity theorem for the exact free kinetic-OU conditional innovation. Exact OU transitions, the Gaussian Bures--Wasserstein formula, and rank-constrained Bures covariance approximation are established prior art; Bréchet et al. already characterize rank-bounded Bures minimizers. The currently searchable literature did not reveal the combined theorem identifying two d-normal draws as necessary and sufficient for exact affine-Gaussian conditional simulation together with the exact one-draw defect and h^(3/2) constant.

### Literature checked

- https://arxiv.org/abs/2609.20713 — Lyu--Wang--Yang, A Unified Framework for Wasserstein Convergence of ULMC Methods beyond Log-Concavity, arXiv:2609.20713v1. Pages 1--12 independently inspected; they count two correlated Gaussians per iteration for the new low-cost schemes but do not give the audited exact-transition lower bound.
- https://proceedings.mlr.press/v202/brechet23a.html — Bréchet--Papagiannouli--An--Montúfar, ICML 2023; characterizes minimizers for Bures--Wasserstein approximation over rank-bounded covariance matrices, so that optimization ingredient is prior art.

## Scientific value

The result gives a sharp interpretation of a concrete computational resource used by current underdamped Langevin integrators: it separates what two Gaussian draws are intrinsically needed for at the exact free-OU transition level from stronger claims about weak, invariant-measure, or long-time accuracy. The exact one-draw defect supplies a quantitative local benchmark rather than just a rank impossibility.

## Limitations

- The lower bound applies to affine-Gaussian conditional innovations, not arbitrary measurable transformations of a lower-dimensional random source.
- It is a one-step Euclidean-W2 transition statement and does not imply that two Gaussians are necessary for weak accuracy, invariant-measure accuracy, or a global sampling guarantee.
- The theorem is stated for scalar friction and isotropic noise; general friction matrices are outside the audited claim.

## Publication guard

The current source tree on `main` matched the assignment tree exactly during this audit. This guarded change-set adds only the independent-audit evidence pair and updates the independent-audit channel in `VERIFICATION.md`; the Lean and expert-attestation channels are preserved unchanged.
