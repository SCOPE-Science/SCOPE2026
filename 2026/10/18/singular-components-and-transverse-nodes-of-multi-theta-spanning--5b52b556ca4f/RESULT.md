# Singular components and transverse nodes of multi-theta spanning-tree hypersurfaces

## Finding
Let \(k\) be an algebraically closed field of characteristic zero and let \(m\ge4\). Give the \(2m\) edges of the complete bipartite graph \(K_{2,m}\) coordinates \(a_i,b_i\), one pair for each of its \(m\) intermediate vertices. Its **spanning-tree polynomial** (products over edges *in* each spanning tree, not complements) is
\[
F_m=\sum_{i=1}^m a_ib_i\prod_{j\ne i}(a_j+b_j).
\]
Write \(X_m=V(F_m)\subset\mathbb P^{2m-1}_k\), \(u_i=a_i+b_i\), and \(v_i=a_ib_i\). For each \(i\), let
\[
C_i=V\left(a_i,b_i,F_{m-1}^{(i)}\right),\qquad
F_{m-1}^{(i)}=\sum_{j\ne i}v_j\prod_{\ell\notin\{i,j\}}u_\ell.
\]
For each three-element subset \(I\subset\{1,\ldots,m\}\), let \(L_I=V(u_i:i\in I)\).

**Theorem.** \(X_m\) is geometrically integral and normal. Its complete reduced singular locus has the irredundant irreducible-component decomposition
\[
\operatorname{Sing}(X_m)_{\mathrm{red}}
=\bigcup_{i=1}^m C_i\ \cup\!\!\bigcup_{|I|=3} L_I.
\]
Each component has dimension \(2m-4\) and codimension three in \(\mathbb P^{2m-1}\). Every \(C_i\) is integral of degree \(m\); every \(L_I\cong\mathbb P^{2m-4}\) has degree one. Hence
\[
\#\operatorname{Irr}\operatorname{Sing}(X_m)_{\mathrm{red}}
=m+\binom m3,\qquad
\deg\operatorname{Sing}(X_m)_{\mathrm{red}}=m^2+\binom m3.
\]
The generic transverse analytic singularity along *every* component is an ordinary quadratic double point in three transverse parameters, analytically of the form \(xy-z^2=0\) over \(k\). The reduced singular locus is equidimensional of codimension two inside \(X_m\).

For \(m=4\), these are four degree-four integral hypersurface components and four linear components; the singular locus has eight components and degree twenty. The \(m=3\) decomposition into four components is explicitly present in the previously published prism-matroid example of Denham, Schulze, and Walther; the new assertion is the uniform classification for \(m\ge4\), its degree formula, and its transverse singularity profile.

## Assumptions and scope
The base field is algebraically closed of characteristic zero. All equalities of singular loci and component unions concern reduced closed subschemes, not the potentially nonreduced Jacobian ideal. Each projective space and degree is with respect to the natural homogeneous edge-coordinate embedding. The graph is simple \(K_{2,m}\); the hypersurface uses the spanning-tree convention, which differs from the complementary-edge Symanzik convention used in parts of the physics literature. The asserted local analytic type is generic on each component, not at component intersections.

## Proof
**1. Polynomial and integrality.** Every spanning tree of \(K_{2,m}\) uses both edges at exactly one intermediate vertex and exactly one edge at each other intermediate vertex; this proves the displayed expression for \(F_m\). For \(s\ge2\), write
\[
F_s=a_s\bigl(b_sU+F_{s-1}\bigr)+b_sF_{s-1},\quad U=\prod_{j<s}(a_j+b_j).
\]
In \(k[a_1,b_1,\ldots,a_{s-1},b_{s-1}]\), the polynomials \(U\) and \(F_{s-1}\) are coprime: modulo any factor \(a_j+b_j\) of \(U\), the only surviving summand of \(F_{s-1}\) is \(a_jb_j\prod_{\ell\ne j,s}(a_\ell+b_\ell)\), which is not identically zero. For \(s=2\) the same statement uses \(F_1=a_1b_1\). Thus the displayed coefficients of the linear polynomial in \(a_s\) are coprime in the ring with \(b_s\) adjoined. Gauss's lemma proves irreducibility of \(F_s\) for every \(s\ge2\), hence of \(F_m\) and every \(F_{m-1}^{(i)}\).

**2. Exhaustive singular-point classification.** Partition points by the number \(r\) of vanishing \(u_i\)'s. When \(r=0\), on the open torus of \(u\)'s write
\[
F_m=\left(\prod_j u_j\right)G,
\quad G=\sum_i\frac{a_ib_i}{a_i+b_i}.
\]
At points of \(X_m\) in this open set, vanishing of the gradient of \(F_m\) is equivalent to that of \(G\). But
\[\frac{\partial G}{\partial a_i}=\frac{b_i^2}{u_i^2},\qquad
\frac{\partial G}{\partial b_i}=\frac{a_i^2}{u_i^2},\]
so the gradient cannot vanish when every \(u_i\ne0\).

If exactly one \(u_i\) vanishes, the hypersurface equation reduces to \(v_i\prod_{j\ne i}u_j=0\), forcing \(v_i=0\) and thus \(a_i=b_i=0\). The only possibly nonzero partial derivatives are then the two derivatives with respect to \(a_i,b_i\); both equal \(F_{m-1}^{(i)}\). Thus such a point is singular exactly when it belongs to \(C_i\).

If exactly two distinct \(u_i,u_j\) vanish, the hypersurface equation holds automatically. The derivatives with respect to \(a_i,b_i\) equal \(v_j\prod_{\ell\notin\{i,j\}}u_\ell\), and the corresponding derivatives for \(j\) equal \(v_i\prod_{\ell\notin\{i,j\}}u_\ell\); all other derivatives vanish. Singularity forces \(v_i=v_j=0\), hence both coordinate pairs vanish. Such points belong to \(C_i\cap C_j\). If three or more \(u_i\)'s vanish, every term of every derivative retains at least one of the vanishing \(u\)'s. Such points are precisely covered by the union of all \(L_I\). Conversely, the original derivative formulas show that the points of every \(C_i\) and \(L_I\) are singular, including their nongeneric intersections. This proves the set equality over every algebraically closed field, hence equality of reduced subschemes.

**3. Irredundancy, degree, dimension.** Since \(F_{m-1}^{(i)}\) is irreducible of degree \(m\), \(C_i\) is an integral hypersurface of degree \(m\) in the linear \(\mathbb P^{2m-3}\) defined by \(a_i=b_i=0\). It has dimension \(2m-4\). Each \(L_I\) is a linear \(\mathbb P^{2m-4}\), because its three displayed independent equations use disjoint variable pairs. Every \(C_i\) has a dense open set with all \(u_j\ne0\) for \(j\ne i\), so it lies in no \(L_I\) and in no \(C_j\) for \(j\ne i\). Similarly, the generic point of \(L_I\) has all its three pairs nonzero individually, so it belongs to no \(C_j\); distinct three-element index sets define distinct linear spaces. The components are therefore distinct and irredundant. Their common dimension proves purity, and the projective degree of the reduced pure-dimensional union is the sum of component degrees, giving both formulas.

**4. Generic transverse double points.** At a general point of \(C_i\), all other \(u_j\ne0\), \(F_{m-1}^{(i)}=0\), and \(dF_{m-1}^{(i)}\ne0\) by the derivative calculation on the open set where all remaining \(u\)'s are nonzero. With transverse parameters \(s=a_i,t=b_i,w=F_{m-1}^{(i)}\), the full local equation is exactly
\[
F_m=s t U+(s+t)w,\qquad U=\prod_{j\ne i}u_j\ne0.
\]
Its quadratic initial form has nonzero determinant (for instance its Hessian determinant is \(2U\) up to a nonzero sign and coordinate scaling). At a general point of \(L_{\{i,j,k\}}\), the coordinates \(u_i,u_j,u_k\) are transverse parameters and \(v_iv_jv_k\prod_{\ell\notin\{i,j,k\}}u_\ell\ne0\). The quadratic initial form is a nonzero scalar times
\[
v_i u_ju_k+v_j u_iu_k+v_k u_iu_j,
\]
whose Hessian determinant equals \(2v_iv_jv_k\) up to nonzero factors. In characteristic zero these are nondegenerate quadratic forms in three variables. The formal Morse lemma (and hence completion of the local analytic ring over \(\mathbb C\)) identifies each generic transverse germ with an ordinary quadratic double point. At a generic point this is understood over an algebraic closure of the component function field.

**5. Normality.** \(X_m\) is an integral hypersurface, hence Cohen–Macaulay and satisfies Serre's condition \(S_2\). By the above complete classification its singular locus has codimension two in \(X_m\), so \(X_m\) is regular in codimension one (\(R_1\)). Serre's criterion proves normality.

## Verification
Run the standalone file `verify.py` using Python 3. It exhaustively compares the projective Jacobian criterion with the proposed component membership for every projective point of \(\mathbb P^5(\mathbb F_5)\), \(\mathbb P^7(\mathbb F_3)\), and \(\mathbb P^9(\mathbb F_2)\), corresponding respectively to \(m=3,4,5\). It also verifies homogeneous Euler identities at many exact integer sample points reduced modulo 101 and checks representative transverse Hessian determinants. The expected final line is `VERIFY_OK`. These finite checks are corroborative only; the proof above supplies the unbounded classification.

## Relationship to prior work
Patterson established that graph-hypersurface singular supports are determinantal degeneracy supports; this does not compute the irreducible components or degrees for the present family. Denham, Schulze, and Walther proved general reduced/degeneracy properties of configuration hypersurfaces and, in their Example 5.1, explicitly give the quartic \(m=3\) instance, including its four generic singular components. That finite instance is acknowledged as previously known. The present theorem extends to every \(m\ge4\), with exact component and degree formulas and transverse singularity models. The polynomial convention is given explicitly to prevent confusion with complementary-edge graph polynomials. No result that merely identifies the singular locus as a determinantal rank locus is asserted to establish the detailed decomposition proved here.

## Limitations
Only reduced singular support and generic transverse germs are classified. The full nonreduced Jacobian scheme, singularities where components intersect, and characteristic-dependent schemes in positive characteristic are not classified. The theorem is a direct computation for the particular spanning-tree family, not a universal statement about general graph hypersurfaces. Potential equivalent coverage in other graph-configuration literature remains an originality risk. No independent audit has occurred.

## References
1. E. Patterson, *On the Singular Structure of Graph Hypersurfaces*, arXiv:1004.5166 (first version publicly submitted 2010-04-29), in particular Theorem 4.13. https://arxiv.org/abs/1004.5166
2. G. Denham, M. Schulze, and U. Walther, *Matroid connectivity and singularities of configuration hypersurfaces*, Letters in Mathematical Physics 111 (2021), article 8; DOI:10.1007/s11005-020-01352-3, especially Example 3.17, Main Theorem, and Example 5.1. https://link.springer.com/article/10.1007/s11005-020-01352-3
