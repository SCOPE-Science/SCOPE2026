# Scientific review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The proof was checked separately at the atomic, nonatomic, duality and operator-ideal steps.

On the atomic part, each fiber over an atom is one copy of a finite-dimensional Euclidean space, and the multiplication operator is an lp-direct sum of the matrices A_j. Retaining fewer than n singular-vector modes gives a rank-<n approximant whose error is the largest omitted singular value. Conversely, any n selected singular modes give an n-dimensional subspace on which the operator is bounded below by their minimum singular value. This single witness simultaneously forces the lower bounds for approximation, Bernstein and Gelfand numbers.

On the nonatomic part, whenever t is below the essential supremum of ||A(omega)||, a countable dense set of unit vectors yields one fixed fiber vector v and a positive-measure nonatomic set E on which ||A(omega)v||>t. The subspace {phi v: phi in Lp(E)} is infinite dimensional and the multiplier is bounded below by t there. This supplies the continuous floor at every finite s-number index.

For Kolmogorov numbers, with p' conjugate to p, the adjoint of M_{A*} on L_{p'} is M_A under standard finite-dimensional Bochner duality. The general identity d_n(S')=c_n(S) therefore gives the same formula because A_j and A_j* have identical singular values and identical operator norms.

For the ideal-distance statement, every threshold above the limiting tail leaves only finitely many atomic singular modes and hence a finite-rank truncation. Every threshold below the tail produces an infinite-dimensional subspace on which M_A is bounded below. A strictly singular perturbation cannot remain bounded below on that subspace, forcing the matching lower bound. The inclusions K subset FSS subset SS then give equality of all three distances.

No hidden complementability assumption is used: the lower-bound arguments require only finite-dimensional intersection for Gelfand numbers and failure of bounded-below behavior for strictly singular restrictions.

## Originality

**PASS, to the best of our knowledge.** The result was compared with the main nearby classical and modern lines:

- Plichko--Shevchik (1999) gives the scalar atomless rigidity that a multiplication operator in their rearrangement-invariant setting is strictly singular exactly in the zero case; this is treated as prior art.
- Hutton--Morrell--Retherford (1976) is classical prior art on scalar diagonal operators, approximation numbers and Kolmogorov diameters.
- Gupta--Acharya (2011) develops approximation-number estimates for matrix transformations on vector-valued sequence spaces and proves an approximability criterion for diagonal block operators; the bare atomic compactness criterion is therefore not claimed as new.
- Duru--Kitover--Orhon (2013) characterizes scalar multiplication operators on vector-valued Köthe-Bochner spaces.
- Heymann (2015) develops multiplication operators on Bochner spaces and Banach fibre spaces; Budde--Heymann (2022) studies operator-valued multiplication operators on Bochner Lp-spaces in connection with extrapolation spaces.
- Standard s-number literature supplies the definitions, inequalities and adjoint duality used in the proof.

The contribution claimed here is narrower and more specific: one exact formula, valid simultaneously for approximation, Bernstein, Gelfand and Kolmogorov numbers, for finite matrix-valued multiplication operators over a mixed sigma-finite base, plus the exact common norm distance to K, FSS and SS. No matching statement was identified in the inspected literature.

The principal residual originality risk is older diagonal/direct-integral literature. In particular, the full 1976 Hutton--Morrell--Retherford paper, Pietsch's operator-ideal monographs, and Heymann's 2015 thesis were not exhaustively inspected, and a Hilbert-space or differently phrased special case may be present there. The p=2 decomposable-operator case is therefore not claimed separately as novel.

## Value

**PASS.** The theorem gives a complete finite-dimensional approximation profile and a sharp singularity classification from one transparent invariant: the nonatomic norm floor together with the decreasing rearrangement of atomic fiber singular values. It shows that the profile is independent of p throughout 1<p<infinity despite the ambient spaces being non-Hilbert for p not equal to 2, and it quantitatively unifies the atomless and discrete extremes in a single formula.

## Scientific limitations

The finite-dimensional fiber hypothesis is essential to the stated invariant. Infinite-dimensional fibers can themselves carry nontrivial compact and strictly singular behavior. The endpoints p=1 and p=infinity are not included because the Kolmogorov-number proof uses reflexive Bochner duality. The literature comparison is strongest for the explicitly cited multiplication, diagonal and s-number sources; older direct-integral terminology remains the main source of residual uncertainty.
