# Complete face polynomial for the Minkowski sum of two coordinate cross-polytopes

## Finding
Let \(A\) and \(B\) be two nonempty subsets of a finite coordinate set \(U=A\cup B\), and take \(a,b>0\). The face polynomial of the Minkowski sum of their coordinate cross-polytopes depends **only** on the three cardinalities \(p=|A\setminus B|\), \(q=|B\setminus A|\), \(r=|A\cap B|\), and not on the positive coefficients \(a,b\). Define the finite polynomials
\[
U_m(z)=\frac{(1+2z)^m-1}{z}=\sum_{j=1}^m2^j\binom mj z^{j-1},\qquad U_0(z)=0.
\]
With the full-dimensional polytope itself counted once, its complete face polynomial is
\[
\boxed{F_{p,q,r}(z)=U_p(z)U_{q+r}(z)+U_{p+r}(z)U_q(z)-U_p(z)U_q(z)
+\frac{(1+2z)^{p+q}\bigl((1+2z)^r-1\bigr)}{z}
+z^{p+r}U_q(z)+z^{q+r}U_p(z)+z^{p+q+r}.}
\]
In particular,
\[
\boxed{f_0=4(pq+pr+qr)+2r,\qquad
 f_{n-1}=2^n\mathbf 1_{r>0}+2^p\mathbf1_{p>0}+2^q\mathbf1_{q>0},\qquad n=p+q+r.}
\]
The following absolute-value inequalities are an irredundant geometric facet description, with an inequality omitted when its subscripted cardinality vanishes:
\[
\sum_{i\in A\setminus B}|x_i|\le a,\qquad
\sum_{j\in B\setminus A}|x_j|\le b,\qquad
\sum_{i\in U}|x_i|\le a+b\quad(r>0).
\]
Each absolute-value inequality is shorthand for all its sign-linearizations. The final family consists of \(2^n\) facets if \(r>0\).

## Assumptions and scope
Work in \(\mathbb R^U\) with standard basis vectors \(e_i\). For nonempty \(T\subseteq U\), write \(C_T=\operatorname{conv}\{e_i,-e_i:i\in T\}\). Write \(P=A\setminus B\), \(S=B\setminus A\), \(R=A\cap B\), of sizes \(p,q,r\), and \(n=p+q+r\ge1\). Require \(p+r\ge1\), \(q+r\ge1\), and \(a,b>0\). The sum \(K=aC_A+bC_B\) is \(n\)-dimensional because every coordinate axis in \(U\) appears in one of the summands. The coefficient of \(z^k\) in \(F\) is the number of \(k\)-dimensional nonempty faces for \(0\le k\le n\), including \(f_n=1\), but excluding the empty face. The formula permits \(p=0\), \(q=0\), or \(r=0\), and also \(n=1\).

## Proof
**Supporting faces.** For a normal \(u\in\mathbb R^U\), put \(t_A=\max_{i\in A}|u_i|\), \(t_B=\max_{j\in B}|u_j|\). If \(t_A>0\), the exposed face \(C_A^u\) is the simplex spanned by all \(\operatorname{sgn}(u_i)e_i\) with \(|u_i|=t_A\), \(i\in A\); if \(t_A=0\), it is the whole \(C_A\). The analogous statement holds for \(B\). The exposed face of a Minkowski sum is exactly \(K^u=aC_A^u+bC_B^u\), with the pair of summand faces intrinsic to \(K^u\). Indeed if two normals expose the same sum face, their midpoint exposes the intersection of the two summand faces; a proper subset of either summand face cannot have the same Minkowski sum with a fixed compact convex second summand (as follows by strict support inequality in a distinguishing direction). Thus counting distinct pairs of exposed summand faces counts the faces without duplication.

**Both maxima positive, no common maximizing coordinate.** Write \(J_A\subseteq A\) and \(J_B\subseteq B\) for the nonempty selected indices (with an independent sign at each selected index). They are disjoint precisely when one of the following holds: \(J_A\subseteq P\) or \(J_B\subseteq S\). To see necessity, a selected overlapping coordinate forces its normal value to be the maximum in both sets, thereby also selecting it in both. For sufficiency, choose \(t_A>t_B>0\) in the first case, or the reverse in the second, except if an overlapping coordinate is selected in the lower-maximum set, when the same choice still works. All other coordinates can be placed strictly below their permitted maxima. As the signed selected sets have disjoint supports, the exposed face is the product, up to translation and scaling, of two simplices, of dimension \(|J_A|+|J_B|-2\). Using \(U_m(z)=\sum_{j\ge1}2^j\binom mj z^{j-1}\), inclusion–exclusion yields
\[
U_pU_{q+r}+U_{p+r}U_q-U_pU_q.
\]

**Both maxima positive, common maximizing coordinates.** Set \(J=J_A\cap J_B\ne\varnothing\). Necessarily \(J\subseteq R\) and \(t_A=t_B\); signs of common coordinates agree. All selected coordinates are obtained by choosing a nonempty signed subset of \(R\) and arbitrary signed subsets of \(P,S\). The resulting face has dimension \(|J_A\cup J_B|-1\): its affine-direction space consists of vectors supported on those selected coordinates whose coordinate sum is zero, since a common selected coordinate couples the two simplex directions. Every such signed pattern is exposed by assigning a common largest absolute normal value to its selected coordinates, strictly smaller values elsewhere. Therefore the generating contribution is
\[
\frac{(1+2z)^{p+q}\big((1+2z)^r-1\big)}{z}.
\]

**One maximum zero.** If \(t_A=0<t_B\), the first face is the entire \(p+r\)-dimensional \(C_A\) and the second is a signed simplex on a nonempty subset of \(S\). Its affine span uses disjoint coordinates, so the face dimension is \(p+r+|J_B|-1\), contributing \(z^{p+r}U_q\). The symmetric case gives \(z^{q+r}U_p\). If both maxima vanish, \(u=0\) and the exposed face is the whole \(n\)-dimensional \(K\), contributing \(z^n\). All cases are disjoint and exhaustive. This proves the polynomial.

**Dimension and weight independence.** Every face is determined by one of the four combinatorial cases, depending only on the supports and signs of \(u\) and on the equality or strict ordering of the two normal maxima. Those data do not involve the positive scalar coefficients. The face correspondences respect inclusion, hence the face lattice is fixed as the coefficients vary.

**Facet inequalities.** The support function is \(h_K(u)=a\max_{i\in A}|u_i|+b\max_{j\in B}|u_j|\). Its unit polar is \(K^\circ=\{u:a t_A+b t_B\le1\}\). Let \(H=(a+b)^{-1}[-1,1]^U\), let \(D_P=a^{-1}[-1,1]^P\) embedded by zeros outside \(P\), and \(D_S=b^{-1}[-1,1]^S\) embedded analogously. If \(t_A\ge t_B\), write \(u=(a+b)t_B h+a(t_A-t_B)d\), where \(h\in H\), \(d\in D_P\), with unused convex weight assigned to the origin; the decomposition chooses \(h\) on all coordinates at or below \(t_B\) and allocates the excess only to exclusive \(P\)-coordinates. If \(t_B\ge t_A\), use \(D_S\) symmetrically. Thus \(K^\circ=\operatorname{conv}(H\cup D_P\cup D_S)\) for \(a,b>0\), with all claimed points as needed. Vertices of \(D_P\) (if \(p>0\)) and \(D_S\) (if \(q>0\)) are extreme; those of \(H\) are extreme precisely when \(r>0\). One can expose each such vertex by putting sufficiently large normal weight on one distinguished coordinate in the appropriate support, with small nonzero weights on the other coordinates to distinguish signs. The polar vertex list yields exactly the displayed irredundant facet families. The coefficient of \(z^{n-1}\) agrees with their total number, and extracting the constant term of \(F\) gives the vertex count.

## Verification
The included standalone `CHECK_FVECTOR.py` uses only Python's standard library. It computes coefficients from the formula, and independently enumerates face pairs exposed by all normals in \(\{-2,-1,0,1,2\}^n\) for every valid \((p,q,r)\) with \(1\le n\le5\). It derives each face dimension by exact rational row reduction of its summand edge directions. All 45 parameter triples passed; representative face vectors (in increasing dimension order, including the full face) are \((14,24,12,1)\) for \((1,1,1)\), \((24,68,64,20,1)\) for \((1,1,2)\), and \((34,128,192,136,40,1)\) for \((2,2,1)\). The finite check is an error detector, not an infinite-dimensional proof. The formula and irredundance for arbitrary positive weights rest on the preceding argument.

## Relationship to prior work
Wang–Hou–Thawinrak–Liu–Dai study lattice-point enumeration for arbitrary Minkowski sums of cross-polytopes and explicitly pose the determination of face posets and face numbers as an open direction (arXiv:2608.16037, §5, Problem 5.4). The present statement completely resolves the **two-summand coordinate-support** subfamily, not the general many-summand problem. Eur–Fink–Larson–Spink develop the broader signed-permutohedral framework, including Minkowski decompositions and volume/Ehrhart results (arXiv:2209.06752); those results do not directly specify this exact overlap-dependent face polynomial. Agnarsson studies the flag polynomial for Minkowski sums of simplices (arXiv:1006.5928), a different class without centrally symmetric cross-polytope summands.

## Limitations
The theorem assumes exactly two summands that are positively scaled standard **coordinate cross-polytopes**; it does not count faces of arbitrary rotations, arbitrary polytopes, or sums of three or more such bodies. The complete face polynomial does not by itself give a complete flag-enumerator for chains of faces. Historical priority is provisional: an equivalent two-summand result could be encoded in older signed-permutohedral or polyhedral normal-fan literature. The certificate enumerates a finite set of low-dimensional sign patterns only. No independent scientific audit has been performed.

## References
1. H. Wang, Q. Hou, W. Thawinrak, Z. Liu, Z. Dai, *Counting Lattice Points in Minkowski Sums of Cross Polytopes*, arXiv:2608.16037, first public 2026-08-17, https://arxiv.org/abs/2608.16037.
2. C. Eur, A. Fink, M. Larson, H. Spink, *Signed permutohedra, delta-matroids, and beyond*, arXiv:2209.06752, https://arxiv.org/abs/2209.06752.
3. G. Agnarsson, *The flag polynomial of the Minkowski sum of simplices*, arXiv:1006.5928, https://arxiv.org/abs/1006.5928.
