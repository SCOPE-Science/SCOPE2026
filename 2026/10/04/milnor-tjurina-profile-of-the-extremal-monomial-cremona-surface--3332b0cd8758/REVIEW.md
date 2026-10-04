# Review: Milnor–Tjurina profile of the extremal monomial Cremona surface

## Correctness
**PASS.** The claim is quantified for every integer \(d\ge3\) over \(\mathbb C\), with \(n=d-1\). The unique singular point follows immediately from the triangular projective Jacobian equations. The Milnor formula follows from additivity of local intersection multiplicity after factoring \(g_x=x^{n-1}L\), and both component intersections are computed explicitly. The Tjurina formula follows from an explicit Gröbner basis and a complete count of standard monomials. The isolated-singularity hypothesis needed for the Milnor number and Saito criterion is proved. The finite checker independently replays the Euler identity, Buchberger reductions, and standard-monomial count for \(2\le n\le10\).

Risk: the verifier is finite and therefore is not evidence for the universal quantifier by itself; the universal conclusion depends on the symbolic proof written in RESULT.md.

## Originality
**PASS.** The closest source, Fassarella–Medeiros arXiv:2206.04847, defines exactly the same family, states its unique singular point, and proves that the associated map is the unique equality case for inverse degree up to coordinate and variable permutations. The inspected Example 3.2 computes only the Milnor sum of a smooth general linear section and does not state the local Milnor number, Tjurina number, their defect, or the quasihomogeneity transition of the surface singularity. Johnson's earlier extremal example supplies the map and inverse degree but not the inspected local invariant package. Broader toric-polar characteristic-class work does not imply the exact local formulas in the material inspected. published-finding corpus and direct text searches for the family combined with Milnor/Tjurina terminology did not locate an equivalent or stronger statement.

Residual risk: a computation in literature not indexed by the searched services could duplicate the formulas.

## Value
**PASS.** This is not an arbitrary parameter slice: the family is singled out by the sharp inverse-degree theorem. The formulas measure the exact local complexity of its unique surface singularity and reveal a qualitative boundary at \(d=3\): the Milnor–Tjurina defect grows exactly as \((d-2)(d-3)\), so all higher members are non-quasihomogeneous. This connects the extremal birational construction to a natural deformation-theoretic invariant of the associated hypersurface.

Risk: no downstream classification theorem is claimed; the value is the exact invariant profile and structural transition for a distinguished infinite family.

## Closest literature and limitations
The primary comparison is Fassarella–Medeiros, arXiv:2206.04847, Example 3.2 and Theorem 3.3. Johnson, arXiv:1105.1188, is the earlier source of the extremal family. Fassarella–Medeiros–Salomão, arXiv:2205.03957, is a broader toric-polar comparison. The claim is deliberately limited to the local surface germ and does not re-claim the map, the inverse-degree bound, or uniqueness of the equality case.

Same-model review: passed. Independent audit: not yet performed.
