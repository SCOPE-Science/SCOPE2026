# Scientific review

## Correctness — PASS

For every integer \(k\ge2\), the clique classification is exhaustive: a distance-\(k\) clique in the \(3k\)-cycle either lies in a circular interval of \(k+1\) vertices or is one of exactly \(k\) equilateral triangles. The interval core is the nerve of a good cover of the circle, hence is homotopy equivalent to \(S^1\). The explicit radial map has degree one on the embedded cycle, making its integral first-homology normalization primitive. Each exceptional triangle attaches along that primitive positive circle generator, so the relative integral boundary is the row \((1,\ldots,1)\). Reflection changes the triangle orientation and circle orientation together; rotation permutes the oriented triangles without sign. Equivariance of the integral boundary gives precisely the signed augmentation kernel, not just its rational character. The relative long exact sequence and one degree-one attachment also prove vanishing of the remaining reduced homology and the previously known sphere-wedge type.

The separate standalone checker reconstructs all faces for \(2\le k\le8\), compares with exhaustive direct clique enumeration when \(2\le k\le4\), checks the exceptional face boundaries, and verifies complete signed Lefschetz traces of every dihedral element. These computations test rather than replace the infinite-parameter proof. All required calculations use exact integers.

## Originality — PASS, with residual risks

Adamaszek, *Clique complexes and graph powers* (arXiv:1104.0433, Corollary 6.7), proves the same **nonequivariant** homotopy type. Consequently that sphere-wedge statement is a prior premise and is not asserted to be new. It does not determine integral rotation/reflection matrices, an integral signed lattice, or reflection character values.

Adamaszek, Adams, Frick, Peterson, and Previte-Johnson, *Nerve complexes of circular arcs* (arXiv:1410.4336), Proposition 7.2, gives an equivariant result for the circular-arc **nerve** complexes. Its Section 8 identifies cycle-power **clique** complexes with different-order nerves up to nonequivariant homotopy. The change in vertex count prevents direct transport of an action of the same full dihedral group, and the source's stated theorems do not settle the present integral action. The circle Rips paper arXiv:1503.03669 concerns homotopy transitions without this integral reflection action.

Searches for alternate descriptions (cyclic graph powers, inclusive graph-metric Rips, rational/dihedral homology, integral augmentation lattices) found no stronger indexed theorem with the same group and integral statement. An earlier calculation of the **ordinary cyclic orbit space** determines a quotient homotopy type, not the full reflection-sensitive integral homology module. Search-index incompleteness and a possibly unindexed equivalent equivariant treatment remain risks; novelty has not been independently confirmed.

## Value — PASS

The first singular winding ratio \(1/3\) is the natural threshold where the circle-like Rips complex gains the equilateral triangles and its second homology becomes nontrivial. The signed augmentation lattice is intrinsic to these missing circular-arc faces. It determines the complete integral action for an unbounded family, including reflection parity and fixed-submodule ranks, which the previously known sphere multiplicity cannot recover. This is a structural equivariant refinement with applications to invariant homology and coefficient reductions; no unproved broader consequences are asserted.

## Scope and limitations

Only the first singular ratio and ordinary integral homology representation are classified, not arbitrary critical ratios, equivariant homotopy type, ordinary orbit-space homology, or adjacent-scale persistence. Finite verification is not a substitute for the all-parameter proof. Publication priority remains uncertain without independent bibliographic and mathematical validation.

Self-review: passed. Independent audit: not yet performed.
