# Independent Audit — Gaussian-boundary hypergeometric laws: sharp Hellinger rate and root-n noncontiguity

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned/current source tree:** `4f8a0054e93d70e8ec7ba7118164a5889f0d1bef`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The inventory-snapshot and current-main directory entries match exactly by child Git blob/tree SHA, so the assigned source-tree SHA remains the current tree audited. GitHub was used read-only as evidence.

## Correctness — PASSED

PASS. The beta-precision representation gives the stated tail mechanism. At x^2=2L+d log L with d>1, the small-precision change of variables yields P_a(|X|>x)=a/x^2(1+o(1)), while the Gaussian component is o(a/L). The cutoffs s_a^2=2L+2 log L and r_a^2=2L+6 log L therefore place a/(2L)(1+o(1)) of P_a-mass beyond r_a and only o(a/L) mass in the transition band. The exact density-ratio representation gives a central Hellinger contribution O(a^2)+O(aL^{-5/2})=o(a/L); Cauchy–Schwarz makes the outer affinity negligible. Hence H^2(P_a,P_0)~a/(2L). Affinity tensorization then gives the exp(-gamma/4) product limit and the (log n)/n detection scale. The critical maximum law follows from n P_{a_n}(|X|>sqrt(2y log n))->kappa/(2y) for y>=1 and Gaussian domination for y<1. The root-n noncontiguity witness is likewise valid because nP_{tau/sqrt(n)}(|X|>sqrt(2(1+eps)log n))->infinity while the Gaussian exceedance probability vanishes. The triangular empirical-CDF argument under sqrt(n)a_n->0 is consistent with the source's bounded derivative/curvature setup, so the stated first-order blindness of the fixed-scale minimum-distance statistic does not require contiguity.

## Originality — PASSED

PASS, narrowly scoped. Lawford's September 2026 paper introduces this Gaussian-nested hypergeometric family, its beta-precision representation, algebraic tail, and nonstandard minimum-distance boundary inference, but the accessible source statement does not give the sharp Hellinger expansion H^2~a/[2 log(1/a)], the induced iid information boundary, or the explicit experiment-versus-CDF locality separation. General sparse-mixture detection and heavy-impurity extreme-value theory supply the mechanism and are prior art; they are not credited as new. Targeted searches did not locate the displayed path-specific constant or product-Hellinger consequence in prior work.

## Scientific value — PASSED

PASS. The result quantifies the source paper's non-DQM Gaussian boundary in an experiment-level metric, identifies a detection scale much finer than the root-n CDF scale, and gives a concrete regime where the full iid experiments are asymptotically separated while the minimum-distance statistic retains its null first-order law. That is a substantive correction of locality interpretation, not merely another tail calculation.

## Independent checks

- Re-derived the uniform logarithmic-window tail asymptotic from the beta-precision mixture.
- Rechecked the central Hellinger bound, transition-band mass, and outer-affinity estimate giving the exact 1/2 constant.
- Rechecked affinity tensorization, the critical maximum limit, and the root-n maximum-event noncontiguity witness.
- Compared the claim with Lawford arXiv:2609.20393 and general sparse-mixture/heavy-impurity literature without crediting those general mechanisms as new.
- Verified inventory-snapshot and current-main record entries are byte-identical by child Git blob/tree SHA, so the assigned tree SHA remains the audited current tree.

## Limitations

- The validated sharp Hellinger result is for the standardized one-parameter path with fixed location and scale.
- No full likelihood-ratio limit experiment or finite-sample error bound is established at the critical scale.
- The originality finding is path-specific; sparse-mixture detection and heavy-tail maximum mechanisms are established prior art.
- The source paper is extremely recent, leaving residual risk from contemporaneous unindexed work.

## Evidence and references

- https://arxiv.org/abs/2609.20393
- https://doi.org/10.1109/TIT.2014.2304295
- https://doi.org/10.3390/math9182208
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/18/hypergeometric-gaussian-hellinger-noncontiguity--40af82dd69ac

This staged audit changes only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
