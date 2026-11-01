# Scientific review: simplex-frustum John ellipsoids

## Correctness — PASS
The uniqueness of the global maximal-volume inscribed ellipsoid implies full permutation symmetry. Exact halfspace support bounds reduce the unrestricted ellipsoid problem to maximizing a strictly unimodal function of one positive axial radius. The resulting two exact analytic regimes, all facet-contact assertions and volume-ratio ordering follow algebraically; finite numerical checks merely corroborate these proofs.

## Originality — PASS, with a historical-priority limitation
Ivanov–Naszódi (arXiv:2212.11781) supply broad John theory rather than the explicit frustum solution. Eydelzon (arXiv:2609.08045) concerns the untruncated simplex, covered by the first regime. Horwitz (arXiv:math/0312403) covers planar inscribed ellipses, not dimensions at least three. An indexed same-frustum result calculates Godbersen mixed-volume profiles, which do not give the stated maximizing ellipsoid or its contact phase. Its complete text was unavailable; older unindexed literature remains a priority risk. Search non-detection was not treated as proof of novelty.

## Mathematical value — PASS
The exact contact transition determines when a cutting facet first constrains a classical extremal ellipsoid. The strict increase of the affine-invariant relative ellipsoid volume gives a global, dimension-uniform geometric ordering and a sharp limiting constant, making this a natural complete invariant calculation rather than an arbitrary parameter slice.

## Scope and verification
Only one-vertex parallel truncations of simplices in dimensions at least three are proved. The boundary parameter one is a degenerate body and is taken as a limit. A reproducibility script tested finite dimensions and parameter grids, but the proof is analytic and independent of those finite tests.

Self-review: passed. Independent audit: not yet performed.
