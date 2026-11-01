# Weighted four-cycle symmetric edge polytopes: exact Minkowski-decomposition strata

## Finding
For the four-cycle \(C_4\), assign positive weights \(w_1,w_2,w_3,w_4\) to its cyclically ordered edges. Define the weighted symmetric edge polytope, in the three-dimensional zero-sum subspace of \(\mathbb R^4\), by
\[
P(w)=\operatorname{conv}\{\pm w_i(e_i-e_{i+1}):1\le i\le4\},\qquad e_5=e_1.
\]
Then \(P(w)\) admits a nontrivial Minkowski decomposition if and only if its four edge weights can be partitioned into two equal pairs: there exists a partition \(\{1,2,3,4\}=\{i,j\}\sqcup\{k,l\}\) with \(w_i=w_j\) and \(w_k=w_l\). This criterion includes the all-equal case.

If there are exactly two distinct weights, each occurring twice, the cone of Minkowski summands of \(P(w)\), modulo translations, has exactly two extremal rays. Its indecomposable factors are a three-dimensional cross-polytope and a line segment. If all four weights coincide, the polytope is a parallelotope, and its summand cone has three extremal segment rays. At every other positive weight vector, \(P(w)\) is Minkowski indecomposable.

Thus the decomposable positive-weight locus is exactly the union of three pair-equality planes, rather than the full region where one or more quadrilateral facets occur.

## Assumptions and scope
A convex polytope \(P\) is Minkowski indecomposable if every Minkowski decomposition \(P=Q+R\) is trivial: apart from point summands, the summands must be homothetic to \(P\); otherwise \(P\) is decomposable. Summands are identified up to translation. All weights are strictly positive; no integer or rational restriction is imposed. Positive affine transformations preserve Minkowski summand structure.

Take the first three edge vectors as a linear basis. Their cyclic sum relation sends the fourth edge vector, after a harmless sign change, to \((a,b,c)\), where
\[
a=w_4/w_1,\qquad b=w_4/w_2,\qquad c=w_4/w_3.
\]
It suffices to analyze
\[
P(a,b,c)=\operatorname{conv}\{\pm e_1,\pm e_2,\pm e_3,\pm(a,b,c)\},\qquad a,b,c>0.
\]
The statement concerns Minkowski decomposition, not the distinct operation of Blaschke addition. It does not classify weighted symmetric edge polytopes of other graphs.

## Proof
**1. The number of vertices.** The point \((a,b,c)\) belongs to the cross-polytope \(\operatorname{conv}\{\pm e_1,\pm e_2,\pm e_3\}\) precisely when \(a+b+c\le1\). The point \(e_1\) lies in \(\operatorname{conv}\{\pm e_2,\pm e_3,\pm(a,b,c)\}\) precisely when \(a\ge1+b+c\), by expanding \(e_1\) in the latter three independent vectors and taking the sum of absolute coefficients. The other two coordinates have analogous tests. At most one of these four inequalities can hold. In each such case \(P\) has exactly six vertices, comprising three linearly independent antipodal pairs; hence it is a simplicial three-dimensional cross-polytope and is Minkowski indecomposable. In the remaining case all eight generating points are vertices, characterized by
\[
a+b+c>1,\quad a<1+b+c,\quad b<1+a+c,\quad c<1+a+b.
\]

**2. Quadrilateral faces.** Every proper face contains at most one point of each antipodal pair, since the origin is interior. Thus every facet has either three or four vertices. A four-vertex facet is supported by a linear functional attaining \(1\) at a signed selection of \(e_1,e_2,e_3,(a,b,c)\), and exists precisely when
\[
\sigma_1a+\sigma_2b+\sigma_3c=\sigma_4,\qquad\sigma_i\in\{-1,1\}.
\]
Under the strict eight-vertex inequalities, these sign conditions reduce, up to reversing all signs, to the three equations
\[
a+b-c=1,\qquad a-b+c=1,\qquad -a+b+c=1.\tag{1}
\]
Each satisfied equation gives one pair of opposite quadrilateral facets. No other quadrilateral facets occur. If \(k\) equations hold, there are \(2k\) quadrilateral facets and \(12-4k\) triangular facets, by Euler's relation and double-counting facet-edge incidences.

**3. Zero or one equation.** If none of (1) holds, every facet is triangular. If exactly one holds, the only nontriangular facets are an opposite pair. In the latter case the dual graph of a three-dimensional polytope is three-vertex-connected, so after removing these two facet-vertices the remaining triangular facets are connected by shared edges; every quadrilateral facet touches this triangular family. In either case McMullen's strongly-connected-indecomposable-faces criterion (triangles are indecomposable) proves that \(P\) is Minkowski indecomposable.

**4. Exactly two equations.** Solving any pair of (1), and permuting the three coordinates, gives
\[
a=1,\qquad b=c=t>0,\qquad t\ne1.
\]
Put \(d=(1,t,t)\), \(h=(0,\tfrac12,\tfrac12)\), \(p=(1,\tfrac t2,\tfrac t2)\), \(q=(0,\tfrac12,-\tfrac12)\), and \(m=\min\{1,t\}\). The eight vertices of \(P(1,t,t)\) form four segments: the two centered at \(\pm p\) of half-length \(t h\), and the two centered at \(\pm q\) of half-length \(h\). The elementary identity \(\operatorname{conv}(\bigcup_i(A_i+S))=\operatorname{conv}(\bigcup_i A_i)+S\), for a common convex set \(S\), gives the exact decomposition
\[
\begin{aligned}
P(1,t,t)&=Q_t+[-mh,mh],\\
Q_t&=\operatorname{conv}\{\pm p\pm(t-m)h,\ \pm q\pm(1-m)h\}.
\end{aligned}\tag{2}
\]
Here the independent signs in each brace generate the stated point pairs. When \(t<1\), the \(\pm p\) segments in \(Q_t\) collapse, whereas when \(t>1\), the \(\pm q\) segments collapse. In either case \(Q_t\) has exactly three linearly independent antipodal vertex pairs, so is a three-dimensional cross-polytope and is indecomposable. The other factor is a nonzero segment. This proves decomposability.

To prove **completeness of its summand cone**, label the vertices \(v_1=e_1,v_2=e_2,v_3=e_3,v_4=d,v_5=-e_1,v_6=-e_2,v_7=-e_3,v_8=-d\). For \(0<t<1\), the four triangular facets have vertex triples \((1,6,7),(6,7,8),(2,3,4),(2,3,5)\); for \(t>1\), they are \((1,6,8),(1,7,8),(2,4,5),(3,4,5)\). The four quadrilateral facets, in both cases, are \((1,2,4,7),(1,3,4,6),(2,5,7,8),(3,5,6,8)\). These are verified directly by evaluating supporting linear forms; each vertex belongs to the displayed facets.

Let \(H\) be any Minkowski summand of \(P\). Each triangular facet of \(P\) is homothetically indecomposable, and the two triangular facets on either side of an internal common edge force the same edge-scaling factor in \(H\). Thus the summand vertices indexed by \(A=\{1,6,7,8\}\) have the form \(\lambda_Av_i+u_A\), while those indexed by \(B=\{2,3,4,5\}\) have the form \(\lambda_Bv_i+u_B\). The two opposite edges \((1,4)\) and \((5,8)\) are both parallel to \(h\) and have constant first coordinate, forcing \(\lambda_A=\lambda_B\) and \((u_B-u_A)_1=0\). Every edge between \(A\) and \(B\) is parallel to \(h\); in particular \((1,4)\) forces \(u_B-u_A\) to be parallel to \(h\). Hence, modulo translation, every summand depends on at most two scalars: a global homothety and one displacement along \(h\). Since the nonhomothetic indecomposable factors in (2) give two independent summand directions, the cone is exactly two-dimensional, with those two factors as its extremal rays. This also proves uniqueness of the two indecomposable Minkowski factors up to scaling and translation.

**5. Three equations.** All three equations (1) hold precisely when \(a=b=c=1\). The eight vertices are the vertices of the parallelotope
\[
P(1,1,1)=[-u,u]+[-v,v]+[-z,z],\quad u=(e_1+e_2)/2,\ v=(e_1+e_3)/2,\ z=(e_2+e_3)/2.
\]
Its three independent segment factors generate the complete summand cone.

Finally, the condition that two of (1) hold says, equivalently, that the four original positive edge weights split into two equal pairs. The three-equation case is the all-equal subcase. Combining all cases proves the classification.

## Verification
A standalone exact-rational checker enumerates supporting facets from all triples of generating points, independently computes edges from their facet incidences, and determines the dimension of the permitted edge-parallel vertex deformation space. The computed dimensions (including translations) are \(4\) in sample indecomposable eight-vertex cases, \(5\) for both \(t=1/2\) and \(t=2\), and \(6\) for the uniform parallelotope. It separately checks the four/four facet classification in the two-equality regimes and confirms the explicit triangular-facet table. Those finite computations corroborate, but do not replace, the all-positive-weight analytic argument.

## Relationship to prior work
Higashitani and Mori (2026, arXiv:2608.02445, Sections 1, 3, 5 and 6) classify **unweighted** symmetric edge polytopes that are Minkowski decomposable, including the square graph \(K_{2,2}=C_4\); they explicitly provide its unweighted Minkowski decomposition. They also present McMullen's triangular-face criterion. The present result evaluates a different, four-parameter positive edge-weight family on that same graph: generic positive deformations are indecomposable, and exactly three pair-equality loci survive, with a complete decomposition-cone description. It is not a direct implication of the graph-only classification, whose hypotheses fix all edge-vector lengths to one.

General polyhedral deformation-cone and edge-dependency methods are known and may offer alternative proofs. A prior formulation under the language of antipodal eight-vertex polytopes or circuits could overlap this specific weight-stratum classification; no claim of exhaustive historical priority is made.

## Limitations
The result applies only to a four-cycle with strictly positive edge weights and its affine-equivalent four-pair circuit model. It does not extend the graph classification to arbitrary weighted graphs, nor determine Euclidean metric invariants, lattice properties, or Ehrhart data. The self-contained proofs establish the universal classification, while the bundled finite tests inspect selected rational inputs only. Independent mathematical audit and exhaustive historical-priority verification are not performed.

## References
1. A. Higashitani and A. Mori, *Minkowski decomposability of symmetric edge polytopes*, arXiv:2608.02445v1, first public 3 August 2026, especially Sections 1, 3, 5, and 6.
2. P. McMullen, *Indecomposable convex polytopes*, Israel Journal of Mathematics 58 (1987), 321–323 (the criterion quoted in Reference 1, Section 3).
3. A. Higashitani, A. Padrol, and R. Sanyal, *Indecomposability of 0/1-polytopes*, arXiv:2605.22594v1 (21 May 2026), for distinct unweighted 0/1-polytope decomposition theory.
