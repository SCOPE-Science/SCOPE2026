# Joint color and pentagon symmetry of graph-coloring manifolds

## Finding
For every integer \(n\geq4\), let \(X_n=|\operatorname{Hom}(C_5,K_n)|\) be the geometric realization of the standard graph-multimorphism prodsimplicial complex. The dihedral group \(D_5\) acts by permuting pentagon positions, and the color group \(S_n\) acts by relabeling the complete graph. The actions commute. Write \(\varepsilon\) for the one-dimensional character of \(D_5\) which equals \(-1\) on reflections and \(+1\) on rotations, and write \(\operatorname{sgn}\) for the sign character of \(S_n\). All representations below are over \(\mathbb Q\).

When \(n\) is even, the only nonzero reduced homology is
\[
\widetilde H_{2n-5}(X_n;\mathbb Q)\cong\mathbf1\boxtimes\mathbf1.
\]
When \(n\) is odd, precisely three reduced groups are nonzero:
\[
\begin{aligned}
\widetilde H_{n-3}(X_n;\mathbb Q)&\cong\varepsilon\boxtimes\operatorname{sgn},\\
\widetilde H_{n-2}(X_n;\mathbb Q)&\cong\mathbf1\boxtimes\operatorname{sgn},\\
\widetilde H_{2n-5}(X_n;\mathbb Q)&\cong\varepsilon\boxtimes\mathbf1.
\end{aligned}
\]
Each displayed group is one-dimensional. In particular, the quotient by both position symmetries and color relabeling has the parity dichotomy
\[
\widetilde H_i\bigl(X_n/(D_5\times S_n);\mathbb Q\bigr)\cong
\begin{cases}
\mathbb Q,& n\text{ even and }i=2n-5,\\
0,&\text{otherwise}.
\end{cases}
\]
Thus for odd \(n\) this quotient is rationally acyclic, whereas for even \(n\) it has the rational homology of a sphere. No claim of contractibility or a manifold structure for the quotient is made.

## Assumptions and scope
A cell of \(\operatorname{Hom}(C_5,K_n)\) is a five-tuple \((A_0,\ldots,A_4)\) of nonempty color subsets with \(A_i\cap A_{i+1}=\varnothing\), indices modulo five; it is the product \(\prod_i\Delta^{A_i}\) and has dimension \(\sum_i(|A_i|-1)\). Source and target permutations act by permuting factors and by relabeling the simplex vertices, respectively. Homology and quotients mean ordinary singular homology of geometric realizations, with rational coefficients. The character \(\varepsilon\) refers to reflections in the full order-ten dihedral group, not merely one selected involution.

## Proof
**Step 1 (known topology and source reflection).** Schultz's 2005 Stiefel-manifold theorem identifies \(X_n\) with the unit tangent sphere bundle of \(S^{n-2}\), namely \(V_{n-1,2}\), of dimension \(2n-5\). For the sphere bundle \(S^{n-3}\to V_{n-1,2}\to S^{n-2}\), the rational Euler class vanishes if \(n\) is odd and is nonzero if \(n\) is even. Its rational Gysin sequence therefore gives exactly the stated one-dimensional homology degrees, forgetting actions. The 2005 equivariant homotopy model, independently strengthened to a one-reflection-equivariant homeomorphism in the 2014 paper *Stiefel manifolds and coloring the pentagon*, identifies a pentagon reflection with the Stiefel involution \((u,v)\mapsto(u,-v)\). This involution fixes the base, has degree \((-1)^{n-2}\) on the fiber, and hence induces \(+1\) on degree \(n-2\) and \((-1)^{n-2}\) on both degree \(n-3\) and top degree whenever those groups exist. Every rotation has order five and therefore acts trivially on one-dimensional rational homology. Hence the full \(D_5\)-characters are determined, without claiming a \(D_5\)-equivariant Stiefel homeomorphism.

**Step 2 (color-permutation orientation).** The manifold \(X_n\) is connected and orientable for all \(n\ge4\) by the Stiefel description. Let \(\tau\in S_n\) transpose colors zero and one. Consider the maximal-dimensional cell in which these two colors occur in pentagon positions \(\{0,2\}\), color two occurs in \(\{1,3\}\), color three occurs in \(\{1,4\}\), and every further color occurs in \(\{0,2\}\). Every assigned set is independent in the pentagon, and all five position factors are nonempty. The cell has dimension \(2n-5\). The transposition fixes it, reversing orientation once in the simplex of position zero and once in the simplex of position two, hence preserving the product orientation. The local orientation sign of a manifold homeomorphism is constant; therefore \(\tau\) preserves the global fundamental class. Transpositions generate \(S_n\), so the entire color group acts trivially on top rational homology.

**Step 3 (color sign on middle homology).** Let \(p_3:X_n\to\partial\Delta^{n-1}\) be the coordinate projection sending a multicoloring to its nonempty proper color set at pentagon position three (indices here may be cyclically shifted). It is \(S_n\)-equivariant. The action on top cohomology of the simplex boundary is \(\operatorname{sgn}\). To establish that its pullback is nonzero, use the small model \(\operatorname{Hom}_{\{2,4\}}(C_5,K_n)\) in Schultz's 2005 proof (Section 5): its face-poset description embeds it as the boundary of a regular neighborhood \(N\) of the diagonal in \(\partial\Delta^{n-1}\times\partial\Delta^{n-1}\), with the first factor given by the complement of the retained coordinate-three color set. This identification is natural under relabeling colors. The first-factor projection \(N\to\partial\Delta^{n-1}\) is a homotopy equivalence because \(N\) retracts to the diagonal. When \(n\) is odd, the rational Euler class of the tangent sphere bundle is zero, so the boundary inclusion \(\partial N\hookrightarrow N\) induces an isomorphism in degree \(n-2\) cohomology. Consequently \(p_3^*\) is nonzero (indeed an isomorphism) in degree \(n-2\). Thus \(S_n\) acts by \(\operatorname{sgn}\) on that one-dimensional cohomology group and its dual homology group. The complement involution of the simplex boundary commutes with color relabeling, so it does not change this character.

**Step 4 (Poincaré duality and quotients).** Since every color permutation preserves the orientation by Step 2, rational Poincaré duality gives the same sign character on the complementary degree \(n-3\) group when \(n\) is odd. Combining the independently determined commuting source and target actions yields the displayed external tensor products. For any finite group acting cellularly on a finite CW complex, rational homology of the topological quotient is the invariant part of rational homology. Taking \(D_5\times S_n\) invariants gives the parity statement; \(n\) odd has no positive-degree invariant line, while \(n\) even retains its top line. There are no further nonzero reduced degrees by Step 1.

## Verification
The accompanying `verify.py` enumerates every cell by assigning to each color an independent subset of the pentagon and discarding assignments omitting a pentagon vertex. For group elements acting on source and color positions, it computes the exact signed cellular Lefschetz number, including signs from permuting product factors and from reordering colors inside simplex factors. It exhaustively verifies the five classes of test elements (identity, source rotation, source reflection, color transposition, and simultaneous reflection/transposition) for \(n=4,5,6\); all fifteen Lefschetz values agree with the claimed characters. In particular, the combined reflection/color transposition has Lefschetz number \(4\) when \(n=5\), distinguishing the middle-degree sign action from the trivial one. The script also checks the explicit fixed top cell and its transposition orientation for each tested size. These finite checks are tests of the all-\(n\) proof, not substitutes for the published Stiefel and Gysin inputs.

## Relationship to prior work
Kozlov (2005) calculated the ordinary integral cohomology groups of cycle-coloring spaces, and Schultz (2005, Section 5) proved the Stiefel homeomorphism and established equivariant homotopy behavior for one source reflection. The 2014 paper *Stiefel manifolds and coloring the pentagon* strengthened the one-reflection model to an equivariant homeomorphism, while explicitly raising the separate full-dihedral equivariant-homeomorphism question. These known homotopy, nonequivariant cohomology, and one-involution facts are hypotheses, not new assertions. The new assertion is the complete **joint** rational \(D_5\times S_n\) character for all \(n\ge4\) and the resulting simultaneous symmetry-quotient parity dichotomy. The proof adds the fixed-top-cell orientation argument and the naturally color-equivariant projection to the boundary of the simplex, rather than presuming the known homeomorphism is fully \(D_5\times S_n\)-equivariant. Calculations for fixed four- and five-color *dihedral-only quotients* do not supply the whole joint action or the uniform both-group quotient theorem.

## Limitations
No integral representation lattice or torsion in the simultaneous quotient is calculated. In particular, rational acyclicity does not imply contractibility. The result does not settle whether the Stiefel homeomorphism can be made fully \(D_5\)-equivariant. The source evidence is the earliest public 2005 version rather than a later journal revision. Publication priority beyond the inspected sources and searchable records cannot be guaranteed.

## References
1. D. N. Kozlov, *Cohomology of colorings of cycles*, arXiv:math/0507117 (first public 2005-07-06), https://arxiv.org/abs/math/0507117 .
2. C. Schultz, *Small models of graph colouring manifolds and the Stiefel manifolds \(\operatorname{Hom}(C_5,K_n)\)*, arXiv:math/0510535 (first public 2005-10-25), https://arxiv.org/abs/math/0510535 ; in particular Sections 3 and 5.
3. *Stiefel manifolds and coloring the pentagon*, Journal of Combinatorial Theory, Series A 121 (2014), 74–88, DOI:10.1016/j.jcta.2013.09.006; particularly the main theorem and Question 5.6, https://doi.org/10.1016/j.jcta.2013.09.006 .
4. P. Csorba and F. H. Lutz, *Graph coloring manifolds*, arXiv:math/0510177 (first public 2005-10-09), https://arxiv.org/abs/math/0510177 .
