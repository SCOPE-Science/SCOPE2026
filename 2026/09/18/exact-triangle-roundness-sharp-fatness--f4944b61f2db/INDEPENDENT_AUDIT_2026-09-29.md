# Independent Audit — Exact triangle formula for Pach–Tardos roundness and sharp fatness calibration

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `7277930f9e4203da78cc9af89b662a58f9334b01`  
**Audited current source tree:** `7277930f9e4203da78cc9af89b662a58f9334b01`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record tree exactly matches the assignment tree SHA. GitHub was used only as read-only evidence; this audit plan does not assert that any staged audit text is already published.

## Correctness — PASS

PASS. After normalizing p=(-1,0), q=(1,0), support lines at the bisector-chord endpoints give h_+≥|a| and h_-≥|b|. The smaller angle between those two triangle side lines is at least the minimum angle α, while it is at most |atan a|+|atan b|; convexity of tan therefore yields C(T,p,q)≥tan(α/2). Taking a minimum-angle vertex and its internal angle-bisector endpoint attains equality. For the fatness bounds, the obtuse/right branch has smallest enclosing radius equal to half the longest side and gives rho=2tu/(t+u); the acute branch gives rho=4tu(1-tu)/((1+t²)(1+u²)). Monotonicity in u over the admissible angle range produces exactly the stated piecewise lower envelope and upper envelope, with the two isosceles equality families and the sharp linear constants.

## Originality — PASS

PASS. Pach–Tardos introduced the roundness invariant in September 2026 and prove general convex-body comparisons, but their source does not evaluate C(S) on arbitrary triangles or give the submitted sharp triangle-specific r/R conversion. The classical triangle identities and minimum-angle mesh-quality notions are prior art; the new content is the exact evaluation of this newly defined invariant and its sharp calibration on the triangle class.

## Scientific value — PASS

PASS. The theorem makes a newly introduced abstract roundness invariant completely explicit on the fundamental class of triangles and determines its exact relationship to the standard smallest-angle and inradius/enclosing-radius quality measures. The sharp equality families make the comparison structurally informative rather than a routine bound.

## Independent checks

- rechecked the supporting-line lower-bound argument, including the obtuse-vertex supplement case
- recomputed the angle-bisector equality configuration
- independently derived the obtuse/right and acute enclosing-radius formulas in half-angle variables
- differentiated the u-dependent acute factor and checked the breakpoint t=√2-1 and both sharp envelopes
- compared the claim with Pach–Tardos's general convex-body roundness results and scope
- verified the current main directory tree exactly equals the assigned tree SHA

## Limitations

- The theorem is triangle-specific and does not improve the general convex-body constants of Pach–Tardos.
- The circumradius in the comparison is the smallest-containing-disk radius, not always the three-point circumcircle radius.
- Because the underlying invariant was introduced only days before this record, contemporaneous unindexed work remains a residual priority risk.

## Evidence and references

- https://arxiv.org/abs/2609.20702
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/18/exact-triangle-roundness-sharp-fatness--f4944b61f2db

This change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
