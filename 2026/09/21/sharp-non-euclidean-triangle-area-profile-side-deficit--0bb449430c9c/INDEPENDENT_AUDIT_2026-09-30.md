# Independent audit — 2026-09-30 UTC

Record: `2026/09/21/sharp-non-euclidean-triangle-area-profile-side-deficit--0bb449430c9c`  
Assigned and audited source tree: `33abb06251f006fb9b47c7a021f3d005b38befd5`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `3fea56ef5fb1825b8f105d38db8c2f9b78d5e260`  
Disposition: **passed**

## Correctness

**independently_supported**. The fixed-(p,Q) optimization is sound. With slacks x=s-a,y=s-b,z=s-c, fixed perimeter fixes x+y+z and Q equals three times their squared deviation from the mean. Spherical and hyperbolic L'Huilier formulas make area monotone in the product tau(s)tau(x)tau(y)tau(z). For g=log tau, g' is csc or csch and is strictly convex, so the two moment constraints force every interior extremum to have at most two slack values. The two isosceles branches in the record are the resulting solutions. Independent numerical evaluation of the comparison derivative was strictly positive on representative spherical and hyperbolic domains. The lower branch reaches a zero slack exactly at u=1/2, i.e. Q/p^2=1/8, after which the area infimum is zero at the degenerate boundary; continuity gives the full interval.

## Originality

**qualified_supported**. Svrtan--Veljan 2012 gives non-Euclidean Finsler--Hadwiger inequalities, while Bogosel 2025 gives the sharp Euclidean Blaschke--Santaló diagram for the same perimeter/area/side-deficit triple. Those are substantial prior inputs and the Euclidean case is correctly excluded. Searches for spherical or hyperbolic fixed-perimeter fixed-Q area profiles did not locate the two-sided formulas, the universal 1/8 transition, or the interval-realization theorem. The claim is therefore supported for the constant-curvature non-Euclidean profile, with residual risk from older triangle-inequality literature expressed in different variables.

## Scientific value

**meaningful_sharp_profile**. The theorem replaces one-sided non-Euclidean inequalities by a complete vertical profile with both extremizers, a sharp curvature-independent degeneracy threshold, and all intermediate values. It gives a natural non-Euclidean analogue of the recent Euclidean optimal diagram.

## Independent checks

- Re-derived the slack/moment identity and the two isosceles solutions from the constraints.
- Checked strict convexity of csc and csch derivatives and the Lagrange two-value reduction.
- Numerically sampled the branch-comparison derivative on admissible spherical and hyperbolic ranges and found it strictly positive.
- Verified algebraically that u=1/2 is equivalent to Q/p^2=1/8 and to the lower branch touching a coordinate plane.

## Literature and evidence checked

- https://www.croris.hr/crosbi/publikacija/prilog-casopis/151282
- https://arxiv.org/abs/2508.06285
- https://doi.org/10.1007/s00025-025-02405-6
- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/21/sharp-non-euclidean-triangle-area-profile-side-deficit--0bb449430c9c

## Limitations

- The spherical theorem is restricted to minor-arc triangles with perimeter below 2pi.
- The hyperbolic normalization is curvature -1; other curvatures require scaling.
- Only the Euclidean quadratic side dispersion Q is profiled.
- The Euclidean exact profile is prior work and not part of the novelty claim.
