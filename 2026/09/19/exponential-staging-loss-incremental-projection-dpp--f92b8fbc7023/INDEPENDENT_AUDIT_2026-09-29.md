# Independent Audit — Exponential staging loss for incremental projection-DPP column selection

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `fc1ba46bd5f6b998a3e811d187cf69218a3f9ea8`  
**Audited current source tree:** `fc1ba46bd5f6b998a3e811d187cf69218a3f9ea8`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record tree exactly matches the assigned source-tree SHA. GitHub was used read-only as evidence, and the dated independent-audit files were absent when this guarded plan was prepared.

## Correctness — PASS

PASS. In the nested Givens construction, the first s columns stabilize after G_s and on the active s+1 coordinates their projection kernel is I-z^(s)z^(s)^T. A rank-s projection DPP therefore omits j with probability |z_j^(s)|^2. Conditioning on the previous s-1 selected indices leaves exactly two possible omissions—the old omitted index and the new index—with the submitted two-weight update. The doubly exponential hierarchy c_s=epsilon^{2^{s-2}} makes the newly introduced weight negligible relative to every old weight, so each one-column stage asymptotically doubles E(1/a_J), giving 2^d. For the final near-rank-d matrix, the exact leave-one-column orthogonal residual is 1/(G^{-1})_{jj}; after normalization by sigma_epsilon^2 it converges uniformly to 1/a_j, while one-shot projection-DPP omission has probability a_j and therefore tends to d+1. An independent numerical reimplementation for d=2,...,6 and epsilon=.03 approaches 2^d for staged selection and d+1 for one-shot selection.

## Originality — PASS

PASS. Grigori--Xue's complete open v1 proves the multistage upper bound prod_i(1+k_i), notes the extreme one-column factor 2^t, and proves only a single conditional step can attain equality (Theorem 3.2). It does not construct one nested family making the factors compound, nor an exponential lower bound for the actual orthogonal column-subset residual, nor the 2^d versus d+1 staged/one-shot separation. The submitted construction therefore answers a genuine sharpness question left open by the source rather than repeating its product bound.

## Scientific value — PASS

PASS. The result shows the source's multiplicative multistage guarantee can be exponentially sharp in a single coherent instance—even for the optimal orthogonal CSS residual—while one-shot sampling on the same limiting family remains only linear in d. This gives a concrete worst-case counterpoint to the source's empirical observation that MSARP and one-shot ARP often behave comparably.

## Independent checks

- Read the lawful-open full HTML of Grigori--Xue v1; Theorem 3.2 proves only one-step tightness and Theorem 3.3/its induction gives the multistage product upper bound.
- Re-derived the active projection kernel and the conditional two-omission DPP recursion.
- Rechecked the weight hierarchy and the stagewise doubling limit.
- Independently reimplemented the Givens family, staged omission law, exact orthogonal residual denominator, and one-shot law; for epsilon=.03 and d=2..6 the staged ratios were approximately 3.996,7.989,15.978,31.957,63.914 while one-shot ratios were approximately 3,4,5,6,7.
- Checked that distinct leading singular values make the ordered dominant right-singular basis unique up to signs, so the staged schedule is not an SVD-basis artifact.
- Targeted searches found no contemporaneous follow-up giving a simultaneous exponential tightness construction.
- Verified the assigned record tree is unchanged from the dispatcher source-check commit to current main and that the dated audit markers are absent.

## Limitations

- The construction is asymptotic in epsilon→0 for each fixed d and does not claim a uniform joint d,epsilon rate.
- The lower bound is for this staged projection-DPP/ARP setting and does not imply all incremental CSS algorithms suffer exponential loss.
- The source paper is extremely recent, so simultaneous unindexed sharpness work remains a residual priority risk.

## Evidence and references

- https://arxiv.org/abs/2609.20556
- https://arxiv.org/html/2609.20556v1
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/19/exponential-staging-loss-incremental-projection-dpp--f92b8fbc7023

This change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
