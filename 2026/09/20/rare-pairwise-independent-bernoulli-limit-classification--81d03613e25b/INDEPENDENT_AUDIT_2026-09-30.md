# Independent audit — 2026-09-30

**Record:** `2026/09/20/rare-pairwise-independent-bernoulli-limit-classification--81d03613e25b`  
**Audited source tree:** `b42609b3afa5ff274ea2f7e1419f890fbda79e2d`  
**Disposition:** passed

## Correctness — PASS

PASS. Pairwise independence gives E S_n=lambda_n and Var(S_n)=lambda_n-sum p_{n,i}^2 -> lambda; bounded second moments imply uniform integrability of S_n, so any weak limit has mean lambda, while lower semicontinuity of x^2 yields Var(Y)<=lambda. For the converse, the exchangeable conditional-uniform-subset construction has marginal lambda/n and pairwise independence exactly when E K_n=lambda and E[K_n(K_n-1)]=(1-1/n)lambda^2. For finite-support targets with variance below lambda, the filed transfer of O(1/n) mass from a positive atom j to 0 and n preserves the mean and raises the factorial moment by exactly the deficit. On the variance=lambda boundary, mixing by eta_n=lambda^2/[n(lambda-v_Z)] with the adjacent-integer minimum-variance law lowers the factorial moment by exactly lambda^2/n. Mean-preserving tail compression and a diagonal choice then handle arbitrary targets. The explicit lambda=1 construction has E K_n=1 and E K_n(K_n-1)=(n-1)/n exactly and converges in probability to 1.

## Originality — PASS

PASS, with an explicit literature-access limitation. Finite-n first-two-binomial-moment probability bounds under pairwise independence are prior art, and Gupta--Hu--Kehne--Levin give an explicit symmetric marginal-1/n example converging to (delta_0+delta_2)/2; therefore the mere failure of Poisson convergence is not new. The inspected 2023 Ramachandra--Natarajan paper is about tight finite-n probability bounds and does not state the weak-limit classification. A full-text request for the 1989 Boros--Prékopa article, after open-access routes failed, reached publisher human verification and could not be completed noninteractively; I do not claim to have read inaccessible pages. Its abstract and the detailed 2023 discussion characterize it as a finite moment/probability-bound result. No inspected source states that the weak limits are exactly all nonnegative-integer laws with mean lambda and variance at most lambda, realized by exchangeable equal-marginal rows.

## Scientific value — PASS

PASS. The result is a complete scalar weak-limit classification rather than another counterexample: it identifies precisely what survives from the law of small numbers under pairwise independence and proves that nothing else does. The equal-marginal exchangeable converse rules out heterogeneity as the mechanism and the variance-loss construction clearly explains how second moment escapes to vanishing tail mass.

## Independent checks

- Re-derived the necessity using L^2 boundedness, first-moment uniform integrability, and lower semicontinuity of the second moment.
- Verified the mass-transfer and boundary-mixture factorial-moment algebra.
- Checked the lambda=1 example exactly: E K_n=1, E[K_n(K_n-1)]=(n-1)/n, and E K_n^2=2-1/n.
- Compared with the 2023 tight-bounds paper and the 2025/2026 contention-resolution construction; attempted authorized retrieval of Boros--Prékopa after OA failure but publisher human verification blocked completion.

## Literature evidence

- https://doi.org/10.1137/21M1408294 — Ramachandra and Natarajan (2023), tight finite-n probability bounds under pairwise independence, including identical marginals.
- https://doi.org/10.1007/s10107-025-02253-w — Gupta, Hu, Kehne and Levin (2025/2026), explicit symmetric pairwise-independent marginal-1/n construction with a non-Poisson two-point count limit.
- https://doi.org/10.1287/moor.14.2.317 — Boros and Prékopa (1989), first-two-binomial-moment probability bounds. Full text could not be inspected in this run because publisher human verification blocked the authorized retrieval after OA routes failed.

## Limitations

- The theorem classifies scalar counts, not point-process limits or locations of rare events.
- Higher k-wise independence imposes additional factorial-moment constraints and is outside scope.
- The construction is existential and is not optimized for support size or sampling entropy.
- The inaccessible full Boros--Prékopa text leaves a residual originality risk, although available metadata and later detailed descriptions frame it as finite-n probability bounds rather than this asymptotic classification.

No GitHub write was performed by the audit chat. This file is staged by the guarded `scope-audit-change-set-v1` plan only.
