# Scientific review

## Correctness — PASS
The ambient signed chain ranks and integral Smith form are reconstructed from 11, 55, 110 and 55 canonically ordered simplices. Exhaustive checks over all 462 five-subsets identify exactly 55 induced two-sphere carriers, and the affine orbit and local triangular-bipyramid shape are checked independently. The key nonstandard step is the integer Smith form of the 110-by-110 concatenated boundary-and-cycle matrix: 65 nonzero invariant factors, all equal to one. Combined with rank 45 for the second boundary this proves genuine integral generation, not only rational spanning. The all-tetrahedra half-boundary is integral, nontrivial, of order two and invariant. The standalone `verify.py` checks these facts using exact arithmetic.

## Originality — PASS
The previously known Moore-space decomposition is credited to Govc (arXiv:2006.05333, Proposition 3.4), not claimed. Masulli–Villa (arXiv:1510.00660) establishes the directed clique construction but not these particular minimal support cycles or their integral spanning. The comparison with published tournament work and accessible indexed related findings, including different Paley tournaments, found no statement covering the 55-support orbit together with the primitive integral-lattice certificate. This is a best-knowledge conclusion, not a proof of absolute priority. Specialized unpublished calculations remain a risk.

## Mathematical value — PASS
This is a naturally motivated local-to-global question for the smallest doubly regular tournament with known second-homology torsion. It identifies the shortest induced sphere carriers and proves the striking stronger fact that small free spherical cycles together span even the global order-two torsion. The canonical signed all-tetrahedra torsion representative supplies a structural explanation independent of the published abstract Betti and homotopy classifications. Neither a routine corollary of the Moore-space type nor a mere numerical rank calculation provides the integral lattice-generation statement.

## Limits
Only the 11-vertex quadratic-residue tournament and five-vertex minimal support layer are classified. No larger-family formula or uniqueness among all chain representatives is asserted. The computational proof uses deterministic integer arithmetic and has not undergone independent review.

Self-review: passed. Independent audit: not yet performed.
