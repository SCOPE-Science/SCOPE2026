# Singular linear strata of diagonal-free Segre projections

## Finding
Let \(k\) be an algebraically closed field of arbitrary characteristic and \(n\ge3\). Write \(z_{ij}\), \(1\le i,j\le n\), \(i\ne j\), for homogeneous coordinates on \(\mathbb P^{n(n-1)-1}\). Let \(X_n\) be the projective toric variety parametrized on its dense torus by \(z_{ij}=u_i v_j\) for all \(i\ne j\). Equivalently, it is the projective edge toric variety of the crown graph \(K_{n,n}\) with a perfect matching removed, or the diagonal-free coordinate projection of a Segre embedding.

Put
\[
R_i=\mathbb P\bigl(\operatorname{span}\{z_{ij}:j\ne i\}\bigr),\quad
C_i=\mathbb P\bigl(\operatorname{span}\{z_{ji}:j\ne i\}\bigr),\quad
L_{ij}=\mathbb P\bigl(\operatorname{span}\{z_{ij},z_{ji}\}\bigr)\ (i<j).
\]
Here \(\mathbb P(\operatorname{span}\{\cdots\})\) denotes the indicated coordinate linear subspace, not a span of coordinate functions in the dual vector space. Then \(X_n\) is geometrically integral, normal, and of dimension \(2n-2\), and its **complete reduced singular locus** is the irredundant union
\[
\boxed{\operatorname{Sing}(X_n)_{\mathrm{red}}=\bigcup_{i=1}^{n}(R_i\cup C_i)\ \cup\ \bigcup_{1\le i<j\le n}L_{ij}.}
\]
Thus there are exactly \(2n+\binom n2\) irreducible singular components. Every \(R_i,C_i\cong\mathbb P^{n-2}\) has codimension \(n\) in \(X_n\); every \(L_{ij}\cong\mathbb P^1\) has codimension \(2n-3\). The singular locus is equidimensional for \(n=3\) (nine lines) and non-equidimensional for every \(n\ge4\).

At a general point of \(R_i\) or \(C_i\), the transverse affine germ is the rank-at-most-one cone of \(2\times(n-1)\) matrices, i.e. the affine cone over \(\mathbb P^1\times\mathbb P^{n-2}\). At a general point of \(L_{ij}\), it is the rank-at-most-one cone of \(2\times(2n-4)\) matrices, i.e. the cone over \(\mathbb P^1\times\mathbb P^{2n-5}\). The respective generic transverse Hilbert--Samuel multiplicities are \(n-1\) and \(2n-4\).

Two distinct row components are disjoint, as are two column components and two distinct \(L\)-components. One has \(R_i\cap C_j=\{[z_{ij}]\}\) if \(i\ne j\), and \(R_i\cap C_i=\varnothing\). The line \(L_{ij}\) meets exactly \(R_i,C_j\) at \([z_{ij}]\), and exactly \(R_j,C_i\) at \([z_{ji}]\), and is disjoint from all other row and column components. Hence every nonempty intersection of distinct components is a coordinate point. In the first cube-graph instance \(n=4\), this gives eight singular planes, six extra singular lines, and two distinct generic transverse Segre multiplicities \(3\) and \(4\).

## Assumptions and scope
All assertions are geometric over an algebraically closed field \(k\), with no restriction on characteristic. The subscript \(\mathrm{red}\) is essential: no description of embedded or nonreduced singular-scheme structure is claimed. The local models hold on dense torus orbits of the indicated components, not at their intersections. The closure of the monomial image, rather than the naive set of rank-one matrices with diagonal entries suppressed, is the object under study. Its homogeneous ring is \(k[u_i v_j:i\ne j]\) with degree-one edge monomials.

## Proof
**1. Facets and normality.** Denote the row and column vertex weights in the exponent polytope by \((x_1,\ldots,x_n)\) and \((y_1,\ldots,y_n)\). The crown edge polytope is
\[
P_n=\operatorname{conv}\{(e_i,e_j):i\ne j\}
=\{(x,y):x_i,y_i\ge0,\ \sum x_i=\sum y_i=1,\ x_i+y_i\le1\ (1\le i\le n)\}.
\]
Indeed, an edge convex combination is a nonnegative transportation table supported outside the diagonal. Fractional max-flow/min-cut requires only the singleton inequalities \(x_i\le1-y_i\): any set containing two or more rows has every column as a neighbor because \(n\ge3\). Conversely those inequalities ensure a feasible table. All \(3n\) indicated inequalities are facets: coordinate facets have the required dimension because their allowed-edge support graphs are connected; the face \(x_i+y_i=1\) has precisely the \(2(n-1)\) affinely independent vertices incident to the index \(i\), giving dimension \(2n-3\). The affine lattice of \(P_n\) is the full integer lattice in \(\sum x_i=\sum y_i=1\), by connectivity and total unimodularity of bipartite incidence matrices. Integral max-flow gives an integer table for every integer margin point in every integral dilate of \(P_n\). The edge semigroup is therefore saturated, giving projective normality. Connectedness of the crown graph gives dimension \(2n-2\).

**2. Exhaustive face classification by active diagonal facets.** Write \(h_i=1-x_i-y_i\). Every face is the intersection of its active facets among \(x_i=0,y_i=0,h_i=0\). At a vertex \((e_r,e_s)\) with \(r\ne s\), \(h_i=0\) holds exactly for \(i=r\) or \(i=s\). Therefore a nonempty face has at most two distinct active \(h\)-facets.

If none is active, the active primitive inward normals are a subset of the coordinate-facet normals of \(\Delta_{n-1}\times\Delta_{n-1}\). Their cone is a smooth coordinate cone in the full lattice. If precisely \(h_p=0\) is active, the face's vertices lie on two arms: \((e_p,e_j)\) with \(j\ne p\), and \((e_i,e_p)\) with \(i\ne p\). If both arms occur, some other row and some other column have positive weights in the relative interior. The active coordinate normals, together with the primitive normal of \(h_p\), form part of an integral basis: modulo the active coordinate normals, \(h_p\) has coefficient \(\pm1\) on a freely varying row coordinate (redistribute mass between row \(p\) and a positive other row). Thus the normal cone is smooth. If only one arm occurs, the face lies in the full row-star face \(F_{R_p}\) or column-star face \(F_{C_p}\). If both \(h_p=h_q=0\) are active, with \(p\ne q\), all vertices must be \((e_p,e_q)\) or \((e_q,e_p)\), so the face lies in their joining segment \(F_{L_{pq}}\). There are no other cases.

**3. These faces are singular and maximal.** On \(F_{R_p}\), exactly the \(n-1\) facets \(x_i=0\) for \(i\ne p\), the facet \(y_p=0\), and \(h_p=0\) are active. They give \(n+1\) distinct extremal rays of a normal cone of dimension \(n\); its unique primitive ray dependence has the form
\[
\textstyle\sum_{i\ne p}x_i=h_p+y_p
\]
for the inward linear forms. Thus the cone is nonsimplicial. The same applies to \(F_{C_p}\). On \(F_{L_{pq}}\), the active facets are the \(2n-4\) coordinate facets \(x_i=y_i=0\) for \(i\notin\{p,q\}\), together with \(h_p=h_q=0\). Their \(2n-2\) distinct extremal primitive inward normals span a cone of dimension \(2n-3\) with dependence
\[
\textstyle\sum_{i\notin\{p,q\}}(x_i+y_i)=h_p+h_q.
\]
It is nonsimplicial. By the toric orbit--face correspondence, every subface of these singular faces has singular orbit, whereas every face not contained in one of them has a smooth normal cone by Step 2. The displayed face families are pairwise incomparable for \(n\ge3\), so they give precisely the maximal singular orbit closures and establish the full reduced singular-locus formula.

**4. Explicit transverse cones and multiplicities.** At a relative-interior point of \(F_{R_p}\), quotient the tangent lattice by directions along this face. Put \(u_i=x_i\) for \(i\ne p\) and \(v=y_p\). The transverse tangent cone is
\[
\{(u,v)\in\mathbb R^n:u_i\ge0,\ 0\le v\le\sum_{i\ne p}u_i\}.
\]
Its primitive semigroup generators are \((e_i,0)\) and \((e_i,1)\) for \(i\ne p\); every integral point decomposes into these generators by distributing \(v\) integer units among the nonnegative integer \(u_i\). Their sole relations are the \(2\times2\) minors of a \(2\times(n-1)\) matrix. Hence the local affine transverse ring is the normal rank-one determinantal cone claimed above. The column case is symmetric.

For \(F_{L_{pq}}\), use \(w=(x_i,y_i)_{i\notin\{p,q\}}\) and \(v=h_p\) in the quotient lattice. The identity \(h_p+h_q=\sum w_i\) identifies its transverse cone with
\[
\{(w,v):w_i\ge0,\ 0\le v\le\sum_i w_i\},\quad\text{with }2n-4\text{ coordinates in }w.
\]
All its integer lattice points are attained: once \(w\) and \(h_p,h_q\) are integral, one free integral row/column transfer along \(F_{L_{pq}}\) reconstructs the original affine lattice point. The same semigroup argument gives the rank-one \(2\times(2n-4)\) determinantal cone. A rank-one \(2\times m\) cone has multiplicity \(\deg(\mathbb P^1\times\mathbb P^{m-1})=m\), proving both numbers.

**5. Linear geometry and intersections.** Each listed face is a unimodular simplex or segment, and its toric orbit closure is exactly the coordinate linear subspace with the stated edge-vertex support. Two such coordinate spaces intersect precisely when their coordinate supports overlap. Distinct row stars and distinct column stars have disjoint supports; row \(i\) and column \(j\) share exactly \(z_{ij}\) if \(i\ne j\). The reverse-edge segment shares its two endpoints with the four indicated stars and shares no coordinates with any other reverse-edge segment. This proves all the incidence statements. Linear-subspace dimensions give the component codimensions, and the first cube-graph case follows by setting \(n=4\).

## Verification
Run `python3 verification/check_crown.py` from the package root with SymPy installed. It independently enumerates all nonempty intersections of the \(3n\) proposed facets, computes each face's exact dimension from its bipartite incidence graph, determines active normal vectors, and applies the Smith normal form to detect lattice-index singularities in simplicial cones. For \(n=3,4,5,6\), the respective total face counts are \(49,349,1911,9327\), and the exact singular-face counts are \(15,50,140,357\). The maximal singular-face counts are \(9,14,20,27\), with precisely the predicted row stars, column stars, and reverse-edge segments. The script checks the full singular-face set against the downward closure of these components, not merely their numbers, and reports `VERIFY_OK`. These finite cases are checks on the uniform proof; they do not prove the statement for larger \(n\).

## Relationship to prior work
Ohsugi and Hibi, *Simple polytopes arising from finite graphs* (arXiv:0804.4287, first posted 2008-04-27), classify when graph-edge polytopes are simple, including the smoothness of complete-bipartite edge polytopes. Their Theorems 1.8 and 2.1 concern graph-wide simplicity and Gröbner properties, not the full singular orbit stratification after deleting a matching. Coons and Sullivant, *Quasi-independence models with rational maximum likelihood estimator* (arXiv:2006.06832, 2020), study exactly the surrounding class of structural-zero monomial statistical models but classify rational maximum-likelihood estimators, not these singular orbit components. A previously available computation of Hilbert series for matching-deleted Segre coordinate projections concerns the same monomial family and supplies normalization and degree information; the present claim is instead the complete reduced singular support, its component incidence, and local transverse determinantal models. General toric orbit/smoothness criteria are used, not claimed as new.

## Limitations
The proof classifies the **reduced** singular locus and the transverse local rings at dense generic orbits. It does not compute the global nonreduced Jacobian singular scheme, its embedded components, or the singular local rings at component intersections. The claim is a complete geometric classification for this specified graph family, not a new algorithm for arbitrary toric varieties. A full independent mathematical audit has not been performed, and equivalent coverage in less searchable mathematical literature remains an originality risk.

## References
- H. Ohsugi and T. Hibi, *Simple polytopes arising from finite graphs*, arXiv:0804.4287 (2008), especially Theorem 1.8 and Sections 1--3. https://arxiv.org/abs/0804.4287
- J. I. Coons and S. Sullivant, *Quasi-independence models with rational maximum likelihood estimator*, arXiv:2006.06832 (2020), especially Definitions 1.1--1.2 and Theorems 1.3 and 5.4. https://arxiv.org/html/2006.06832v2
