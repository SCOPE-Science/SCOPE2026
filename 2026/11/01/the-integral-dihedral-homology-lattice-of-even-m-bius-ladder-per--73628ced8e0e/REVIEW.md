# Scientific review

## Correctness — PASS
The all-parameter proof constructs the independent-set parametrization of perfect matchings, a strictly equivariant homotopy equivalence to a cycle-tile model, and a contractible spoke-star core leaving exactly two relative cells. The integral relative long exact sequence proves that these cells supply a genuine \(\mathbb Z\)-basis. Rotation and reflection induce the claimed signed permutations of that basis. The eigensublattice index follows from a determinant of absolute value two. The finite independent enumeration in `verify_pm_dihedral.py` confirms the matching parametrization and all tile orientations through fourteen spokes, but is explicitly not used as an infinite proof. Boundary cases \(n=4\), both congruence classes, and the distinction between integral and rational representations are addressed.

## Originality — PASS with residual risk
Agarwal–Basak (2026, v2 Section 5.1, Theorem 21) proves only the underlying wedge-of-two-spheres type for even widths. The directly inspected published rotation result establishes the rational character and the square of the rotation, explicitly excluding an integral lattice classification. The inspected antipodal half-turn result proves the central involution acts trivially but leaves the requested eigensublattice index undetermined. The inspected odd-width dihedral result is inapplicable to even widths. A rational trace-zero involution has at least two integral realization types, split versus exchange, so none of the earlier conclusions implies the new index-two statement. Both full generator matrices and the explicit integer basis are additional. Unindexed or implicit formulations remain a residual priority risk, and nonappearance in database searches is not itself a proof of novelty.

## Value — PASS
The first natural integrality problem left by known rational rotation characters is whether the two eigenspaces split the integer homology lattice. The theorem proves a uniform, persistent index-two obstruction for infinitely many widths, supplies the complete integral dihedral module and a canonical structural explanation from two exceptional tilings, and independently rederives the underlying sphere wedge. This is not merely another Betti number, a rational restatement, or an unmotivated small instance.

## Limitations
No claim is made about odd widths, incidental extra automorphisms, equivariant homotopy equivalence, or independent verification. The historical literature comparison is bounded, not an absolute uniqueness certification.

Self-review: passed. Independent audit: not yet performed.
