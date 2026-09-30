# Independent audit — Exact identifiability threshold for equal-weight binomial mixtures with known anchors

**Audit date:** 2026-09-29 (UTC) (UTC)  
**Source path:** `2026/09/20/equal-weight-binomial-mixture-identifiability--0e59e4914c83`  
**Assigned and audited tree:** `2aaae96b56112e0959d31a26a109b6d7cde61d3a`  
**Repository snapshot:** `SCOPE-Science/SCOPE2026` at inventory commit `e9ed144c13b7834896a844cc4f9cac3c25a168a6`

## Disposition

**PASSED.** The record survives independent review.

## Correctness

PASS. The Bin(N,p) mixture law determines and is determined by raw mixing moments through degree N via factorial moments. With equal weights and r exact support anchors, subtracting the anchors exposes the first N power sums of the M=K-r unknown atoms. Newton identities recover all M elementary symmetric polynomials, hence the support polynomial, once N>=M. The lower-bound construction is valid: a sufficiently small constant-term perturbation Q_epsilon=Q+epsilon preserves M distinct real roots inside an anchor-free interval while leaving e_1,...,e_{M-1}, and therefore the first M-1 power sums, unchanged. The explicit K=4, r=1 example was independently recomputed and the two mixtures agree for N=2 but separate at N=3.

## Originality

PASS with a substantial classical-moment caveat. The mechanism is elementary Newton-identity/finite-moment theory, and unrestricted binomial-mixture identifiability at the 2K-1 scale is classical. Targeted searches did not locate a prior statement of the exact global N>=K threshold for the equal-weight submodel together with the anchored N>=K-r extension and a matching global construction below threshold. No earlier SCOPE record with this theorem was found. An equivalent theorem may exist under equal-weight quadrature or finite-moment terminology, so the priority conclusion is literature-bounded rather than absolute.

## Scientific value

PASS. Even though the proof is short, the exact threshold changes the sample/trial requirement for a standard mixture family from the unrestricted 2K-1 scale to K, and quantifies exactly how known support anchors reduce the threshold one-for-one. The sharp global counterexample below threshold makes the statement more than parameter counting or a local identifiability observation.

## Independent checks

- Verified the moment equivalence between the binomial law and moments through degree N.
- Checked the Newton-identity reconstruction and the constant-term perturbation argument, including the M=1 edge case.
- Recomputed the published K=4 anchored example: both N=2 laws are (0.3075, 0.335, 0.3575), while the N=3 laws differ.
- Searched September 17–19 SCOPE directory names for binomial/equal-weight/moment-identifiability overlaps and found no matching prior record.

## Literature and evidence

- https://doi.org/10.1080/01621459.1964.10482176 — Blischke (1964), classical binomial-mixture parameter estimation/identifiability context with unrestricted weights.
- https://doi.org/10.1214/AOMS/1177703862 — Teicher (1963), foundational finite-mixture identifiability context.
- https://arxiv.org/abs/2007.08101 — Gordon et al. (2020), sparse Hausdorff moment recovery with unknown weights.
- https://proceedings.mlr.press/v195/fan23b.html — Fan and Li (2023), sparse moment recovery/stability with unknown weights.

## Limitations

- Exact equal weights, the exact number K of distinct components, and exact anchor locations are essential assumptions.
- The theorem is about exact identifiability, not stable numerical recovery; nearly colliding support points can make root recovery badly conditioned.
- Because the proof reduces to classical Newton identities, older equivalent formulations outside mixture-model terminology remain a meaningful originality risk.

## Repository guard

The current `main` record tree was checked against the assignment and is unchanged at `2aaae96b56112e0959d31a26a109b6d7cde61d3a`. The publication plan changes only independent-audit materials and `VERIFICATION.md`; the Lean and expert-attestation channels are preserved exactly as `unknown` with null evidence.
