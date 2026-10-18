# A single parallel pair creates disjoint singular lines and isolated Segre cones in rank-two matroid toric varieties

## Finding
For any integer \(n\ge5\) and any algebraically closed field \(k\), let \(M_n\) be the rank-two matroid on \([n]\) whose only dependent two-subset is \(\{1,2\}\). Let \(P_n\) be its base polytope and \(X_n\) the normal projective toric variety determined by the normal fan of \(P_n\).

**Theorem.** The reduced singular locus of \(X_n\) consists of exactly \(n-2\) pairwise disjoint projective lines and \(\binom{n-2}{2}\) isolated torus-fixed points. The lines are the orbit closures associated with the edges joining \(e_1+e_j\) and \(e_2+e_j\) for \(3\le j\le n\). Their generic transverse singularity is the affine rank-one locus of \(2\times(n-3)\) matrices, of Hilbert–Samuel multiplicity \(n-3\). Every isolated singularity is the affine rank-one locus of \(2\times(n-2)\) matrices, of multiplicity \(n-2\). Moreover, the support of the non-\(\mathbb Q\)-factorial locus equals the singular locus. In particular, the reduced singular locus is not pure-dimensional.

For \(n=5\), there are three disjoint singular lines, each with generic transverse threefold ordinary-double-point type, and three isolated singular points of multiplicity three.

## Assumptions and scope
All geometric statements are over an algebraically closed field \(k\), with no characteristic restriction. The lattice is \(L=\{z\in\mathbb Z^n:\sum_i z_i=0\}\); the polytope is
\[
P_n=\operatorname{conv}\{e_i+e_j:1\le i<j\le n,\ \{i,j\}\ne\{1,2\}\}\subset\{\sum_i x_i=2\}.
\]
Here \(e_i\) are standard unit vectors. For integers \(a,b\ge2\), write \(D_{a,b}\) for the affine variety cut out by all \(2\times2\) minors of a generic \(a\times b\) matrix (the rank-at-most-one determinantal cone). Its dimension is \(a+b-1\), its singular locus is the apex, and its multiplicity there is \(\binom{a+b-2}{a-1}\). Normality and singularities refer to the normal toric variety associated with the polytope's normal fan, rather than the possibly differently presented affine cone over its projective embedding.

## Proof
**1. Polytope vertices and affine charts.** For each allowed pair \(B=\{i,j\}\), the indicator vector \(v_B=e_i+e_j\) is a vertex, as the linear functional \(x_i+x_j\) uniquely maximizes there; no further vertices exist. The projective variety is covered by its torus-fixed-point charts
\[
U_B=\operatorname{Spec} k[S_B],\qquad S_B=\mathbb N\{v_C-v_B:C\text{ is an allowed basis}\}\subset L.
\]
At a vertex \(B\), every difference \(v_C-v_B\) decomposes as a sum of at most two **allowed single exchanges** \(e_t-e_s\) obtained from an adjacent basis. Indeed, if \(B\cap C\) has size one there is one exchange; if the two bases are disjoint then a bijection from \(B\) to \(C\) with both intermediate bases allowed exists. To see the exceptional case, the only forbidden pair is \(\{1,2\}\): if an intermediate pair is forbidden, exchange the two target elements in the opposite order; at most one intermediate can be forbidden because all targets and both bases are themselves allowed. Thus the edge-exchange characters generate \(S_B\).

**2. Ordinary charts.** If \(B\subset\{3,\ldots,n\}\), both ways of swapping one of the two elements of \(B\) for any of the other \(n-2\) elements are allowed. Arrange the resulting \(2(n-2)\) characters in a two-row matrix. Their only semigroup relations are the \(2\times2\) minor relations, so
\[
U_B\simeq D_{2,n-2}.
\]
To prove the relation assertion, write a monomial product as a nonnegative integral flow on the complete bipartite graph whose two row vertices are the deleted elements of \(B\) and whose columns are their replacements. Two monomials have the same character precisely when they have the same row and column totals. Their difference is a balanced integral flow, decomposable into alternating bipartite cycles; chords reduce any cycle of length greater than four to four-cycles, yielding precisely the minor binomials. The underlying affine semigroup is saturated: for an integral lattice point in its cone, the negative coordinates at the two removed basis elements prescribe integral row supplies and the nonnegative coordinates at the replacement elements prescribe integral column demands; equality of their totals ensures an integer nonnegative transportation matrix. Hence no extra normalization monomials arise. This argument is integral and characteristic-free.

**3. Special charts.** For \(B=\{1,j\}\), with \(3\le j\le n\), there is one distinguished exchange \(e_2-e_1\), while the remaining exchanges are \(e_t-e_1\) and \(e_t-e_j\) for \(t\in\{3,\ldots,n\}\setminus\{j\}\). The latter form the complete bipartite \(2\times(n-3)\) system. The distinguished exchange has nonzero second coordinate, whereas all other generators have zero second coordinate; its coefficient can therefore be recovered uniquely from any semigroup equality, proving a free semigroup factor. Hence
\[
U_{\{1,j\}}\simeq D_{2,n-3}\times\mathbb A^1.
\]
The same computation with indices \(1,2\) interchanged applies to \(B=\{2,j\}\). These exhaust all vertices.

**4. Singular components and gluing.** Each \(D_{2,q}\) with \(q\ge2\) is the affine cone over the Segre embedding \(\mathbb P^1\times\mathbb P^{q-1}\). It is smooth away from its vertex, and has singularity only at that vertex (for example, use the rank-one parameterization locally where a matrix entry is invertible and the Jacobian at the zero matrix). By Steps 2–3 the only singular points on any ordinary chart are its closed torus-fixed points; on every special chart the singular locus is exactly \(\{0\}\times\mathbb A^1\).

The free-factor direction corresponds to the segment \(E_j=[v_{\{1,j\}},v_{\{2,j\}}]\). It is genuinely a polytope edge: the linear weight assigning \(10\) to element \(j\), \(1\) to elements \(1,2\), and \(0\) elsewhere exposes exactly its two endpoints. Consequently the two special-chart singular axes glue to the invariant curve \(V(E_j)\simeq\mathbb P^1\). Two distinct such curves have no common vertex, so their torus-orbit closures are disjoint. They contain every special fixed point and none of the ordinary ones. Hence there are exactly \(n-2\) such one-dimensional components and exactly \(\binom{n-2}{2}\) isolated components indexed by ordinary bases, and no other singular components since these charts cover \(X_n\).

**5. Multiplicities and \(\mathbb Q\)-factoriality.** The projectivization of the affine cone \(D_{2,q}\) is \(\mathbb P^1\times\mathbb P^{q-1}\) embedded by \(\mathcal O(1,1)\). The degree of this Segre variety, hence the cone multiplicity, is \(q\). At a generic point of \(V(E_j)\), the affine-line factor becomes a smooth curve parameter; thus the transverse multiplicity is \(n-3\), while at each ordinary isolated point it is \(n-2\). The cone \(D_{2,q}\) has \(2q\) distinct extremal rays in dimension \(q+1\), so for \(q\ge2\) it is nonsimplicial and not \(\mathbb Q\)-factorial at the apex. Away from these apices the charts are smooth and hence \(\mathbb Q\)-factorial. Therefore the non-\(\mathbb Q\)-factorial support equals the reduced singular support.

## Verification
Run `python3 parallel_pair_check.py` with the Python standard library. It checks each basis chart's proposed primitive exchanges, integral rational rank, decomposition of all remaining basis differences into at most two exchanges, all four-cycle binomials, and explicit exposed special edges for \(4\le n\le9\). Successful completion prints `VERIFY_OK`. These finite tests are corroboration; Steps 1–5 provide the all-parameter proof.

## Relationship to prior work
Feichtner–Sturmfels [1] develop the matroid-polytope and normal-fan framework (including the basis-exchange characterization) and its Bergman subfans. Lam–Postnikov [2] study triangulations, Gröbner bases, and normality for matroid-related alcoved polytopes. Neither inspected discussion provides these special affine toric charts, the mixed-dimensional singular-locus decomposition, or its local multiplicities. The general rank-one determinantal geometry used in the proof is classical and not asserted as new; the contribution is the exact gluing and component classification for this minimal parallel-pair matroid degeneration.

## Limitations
This classifies the **reduced** singular support and generic local analytic types, not the full scheme-theoretic singular locus or a resolution. A finite checker does not independently prove all ranks. An equivalent computation in differently indexed matroid or toric literature cannot be ruled out. The restriction \(n\ge5\) is essential for the positive-dimensional singular components: at \(n=4\), the special charts are smooth.

## References
1. E. M. Feichtner and B. Sturmfels, *Matroid polytopes, nested sets and Bergman fans*, arXiv:math/0411260 (first posted 2004-11-11), especially Section 2. https://arxiv.org/abs/math/0411260.
2. T. Lam and A. Postnikov, *Alcoved Polytopes I*, arXiv:math/0501246 (first posted 2005-01-16), especially Sections 4 and 7. https://arxiv.org/abs/math/0501246.
