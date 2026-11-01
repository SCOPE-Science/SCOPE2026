# Research review

## Correctness — PASS
The theorem concerns the intrinsic centered inradius of the central section, not the projected octahedron. The section/projection polarity identity is exact; the radius is the reciprocal of the largest projected cube-vertex norm. Sorting the three absolute normal coordinates gives the deterministic statistic \(R=(3-(a-b-c)^2)^{-1/2}\), with correct support \([1/\sqrt3,1/\sqrt2]\). The positive spherical tail is derived by explicit polar-coordinate integration, while the negative tail is the spherical area of eight identical curvilinear triangles evaluated by Gauss–Bonnet with correct geodesic curvature. The tangent-plane limit at the collapsing triangle yields the exact \(C^1\)/non-\(C^2\) interior transition and second-derivative jump. The accompanying checker reconstructs actual section polygons without using the dual formula and independently tests 500 plane orientations; direct quadrature, boundary values, and a 150,000-normal simulation yield 533 further overall diagnostics. Computations are supporting checks, not infinite proofs. Residual correctness risk concerns unrecognized degeneracies in the spherical derivation, despite verified boundary and random tests.

## Originality — PASS, with historical-priority uncertainty
The complete public results on the *inradius of an octahedron projection* and the *diameter of an octahedron section* were read, not merely their abstracts. The first is reciprocal to the circumradius of a **cube section**; the present object is reciprocal to the circumradius of a **cube projection**. They are not equivalent: at normal \((1,1,1)/\sqrt3\), the former inradius is \(1/\sqrt2\) and the present section inradius is \(\sqrt{3/8}\). The diameter law concerns the ratio of the smallest and largest ordered normal coordinates, while the present law depends on all three; distinct normals with the same diameter can have different inradii. A complete octahedral width law gives another different statistic. Brazitikos–Pandis analyze extreme *section volumes* rather than this probability distribution. A 2026 paper on negative moments and random-projection inradius bounds was available at abstract level only, not read in full; its stated estimates do not imply the displayed exact law. Searches for stereological and cube-projection-circumradius aliases did not identify covering results, but such absence is not novelty proof. An older nonindexed result or complete inaccessible source remains a priority risk.

## Value — PASS
The inradius is a natural measure of the largest disk contained in an arbitrary central cross-section. A complete elementary distribution for the smallest regular three-dimensional crosspolytope gives an exact benchmark where neighboring literature treats volumes, diameters, widths, or inradii of projections. The interior differentiability transition comes from a genuine change in spherical-region topology (the disappearance of the negative-sum chamber) and is not a routine endpoint or normalization calculation. The theorem is a finite-dimensional exact special-case evaluation; its value does not depend on any unproved asymptotic extension.

## Checked literature and limitations
- S. Brazitikos and C. Pandis, *Restricted Hyperplane Sections of the Cross-Polytope and the Simplex*, arXiv:2606.07163v1, full arXiv text inspected.
- *Exact inradius law for random planar projections of the regular octahedron*, public result of 11 October 2026, full RESULT.md inspected.
- *Exact Haar diameter law for central sections of the regular octahedron*, public result of 11 October 2026, full RESULT.md inspected.
- *Exact width distribution of the unit-edge regular octahedron*, public result of 11 October 2026, full RESULT.md inspected.
- A. Hmadi and D.-M. Liakopoulos, *Negative moments of the support function and applications to isotropic convex bodies*, arXiv:2609.27757v1, abstract only. An inaccessible full manuscript is a residual originality risk, not a substitute for inspection.

No assertion of independent mathematical certification or peer review is made.

Self-review: passed. Independent audit: not yet performed.
