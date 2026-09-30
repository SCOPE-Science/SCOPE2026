# Independent Audit — No exponential Riesz bases on bounded strictly convex bodies without boundary regularity

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `8ccf7ce87498b479eb4fab94e0f83db3fc01fe1b`  
**Audited current source tree:** `8ccf7ce87498b479eb4fab94e0f83db3fc01fe1b`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record tree exactly matches the assigned source-tree SHA. GitHub was used read-only as evidence; this file is a guarded publication-plan payload and is not claimed to be already present in the repository.

## Correctness — PASSED

PASS. Ortega-Cerdà's current v2 Remark 6.4 gives exactly the needed analytic criterion: boundary Lebesgue measure zero, a finite nonzero boundary measure with zero overlap under every nontrivial translate, and two-sided positive-measure neighborhoods. For a compact strictly convex body, after rotating a translation to ae_n, every positive-width vertical fiber has boundary only at its lower and upper endpoints, and the width w=u-l is strictly concave. Hence E_a={w=a} lies in the boundary of the convex superlevel set {w>=a} and is (n-1)-dimensional Lebesgue-null in the base. Because E_a is compactly inside the projection interior and the endpoint graph is locally Lipschitz there, the translated-boundary intersection has zero surface measure. Standard convex-body facts supply the remaining criterion hypotheses.

## Originality — PASSED

PASS. Ortega-Cerdà's September 2026 paper proves balls, triangles, and all bounded convex open sets with C^2 boundary; even its September 27 v2 still states that regularity-based convex-domain result and the general boundary criterion, not the arbitrary strictly convex theorem. Wan's simultaneous paper advertises a different class including disks and triangles. Targeted searches for exponential Riesz bases on arbitrary nonsmooth strictly convex bodies did not locate a result subsuming the submitted theorem. Novelty is confined to the translate-overlap lemma for strict convexity and its application to Ortega-Cerdà's criterion.

## Scientific value — PASSED

PASS. The result removes all boundary differentiability from a newly established nonexistence theorem on a natural large class and identifies strict convexity itself as sufficient geometric input. It is a meaningful strengthening because strictly convex bodies may have very rough boundaries and no positive-curvature patch to which the source's C^2 proof applies.

## Independent checks

- Read Ortega-Cerdà v2 in lawful open arXiv HTML, including Remark 6.4 and Corollary 8.1; the general criterion and the C^2 scope match the submitted use.
- Re-derived the singleton-fiber claim above the boundary of the projection using a lifted supporting hyperplane and strict convexity.
- Re-derived strict convexity of the lower endpoint, strict concavity of the upper endpoint, and strict concavity of the width function.
- Checked E_a subset boundary{w>=a}, nullity of that convex boundary, and local-Lipschitz lifting to surface-measure nullity.
- Checked that every boundary neighborhood of a convex body with nonempty interior meets both the interior and strict exterior in positive-measure open sets.
- Compared against Wan's contemporaneous arXiv:2609.16674 scope and found no arbitrary-strictly-convex statement.
- Verified the assigned record path is unchanged from the dispatcher source-check commit to current main and that both dated independent-audit marker files are absent.

## Limitations

- The theorem applies to strictly convex bodies only; convex bodies with flat faces can have positive-measure translated boundary overlap.
- The analytic obstruction itself is Ortega-Cerdà's prior work; the audit credits only the rough strict-convexity geometric verification.
- Both motivating Riesz-basis preprints are extremely recent, leaving a residual simultaneous-work risk.

## Evidence and references

- https://arxiv.org/abs/2609.18426
- https://arxiv.org/html/2609.18426v2
- https://arxiv.org/abs/2609.16674
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/18/strict-convexity-riesz-basis-obstruction--f3a7cf0b8ac6

This change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
