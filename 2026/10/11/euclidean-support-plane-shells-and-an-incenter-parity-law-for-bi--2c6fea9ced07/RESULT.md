# Euclidean support-plane shells and an incenter parity law for bipartite-cycle root polytopes

## Finding
For every integer \(k\ge2\), the edge-root polytope of the alternatingly oriented cycle with \(2k\) vertices has \(k^2\) facets with an exact Euclidean support-hyperplane distance profile. The largest intrinsic Euclidean inscribed ball has radius
\[
r_k=\begin{cases}
\sqrt{\frac{2}{k(k^2-2)}}&k\text{ even},\\
\sqrt{\frac{2}{k(k^2-1)}}&k\text{ odd}.
\end{cases}
\]
The ball centered at the vertex barycenter contacts exactly \(2k\) facets for even \(k\), and exactly \(k\) for odd \(k\). The affine hull of *all* optimal-ball centers has dimension \(0\) for even \(k\) and \(k-1\) for odd \(k\). Thus the center is unique precisely in the even case.

## Assumptions and scope
Index two sets of coordinate vectors by \(A_i\) and \(B_i\), with \(i\in\mathbb Z/k\mathbb Z\). Equip \(\mathbb R^{2k}\) with its ordinary Euclidean inner product. Set
\[
P_k=\operatorname{conv}\{u_i=e_{A_i}-e_{B_i},\ v_i=e_{A_{i+1}}-e_{B_i}:0\le i<k\}.
\]
This is the root polytope of the bipartite cycle with edges \(A_iB_i\) and \(A_{i+1}B_i\), directed from the \(B\)-part to the \(A\)-part. Its affine span has dimension \(2k-2\), barycenter \(c=(\mathbf1_A/k,-\mathbf1_B/k)\), and translation space
\[
H=\{(x,y)\in\mathbb R^k\oplus\mathbb R^k:\textstyle\sum_i x_i=\sum_i y_i=0\}.
\]
All radii, normals, and center dimensions use the induced Euclidean metric on \(c+H\); these are not affine-invariant quantities.

## Proof
**Step 1 (the complete facet family).** Put \(p_i=u_i-c\) and \(q_i=v_i-c\). Both sets \(\{p_i\}\) and \(\{q_i\}\) sum to zero. Each individually spans a \((k-1)\)-dimensional simplex with the origin in its relative interior: the only linear relation among its \(k\) vectors is their sum. Together the \(2k\) vectors span \(H\) and have only these two independent relations. Indeed, a linear dependence among the original edge differences forces equal coefficients along the connected cycle, while the centered sums of the two perfect matchings account for both relations. Thus the two simplex spans are complementary and \(P_k-c\) is their free sum.

A proper facet of a free sum of two simplices containing the origin internally must be the convex hull of one facet from each simplex. Every such facet consequently contains all \(p_h\) except one \(p_i\), and all \(q_h\) except one \(q_j\). We denote it by \(F_{i,j}\). These \(k^2\) facets are distinct, exhaustive, and have dimension \(2k-3\). In particular, their affine supporting hyperplanes have unique normalized outward normals \(n_{i,j}\in H\) with support value \(1\).

**Step 2 (exact support normals).** Their scalar products with the vertex vectors must be
\[
\langle n_{i,j},p_h\rangle=1-k\mathbf1_{h=i},\qquad
\langle n_{i,j},q_h\rangle=1-k\mathbf1_{h=j}.
\]
To see the omitted values, note that each of the two vertex sets sums to zero, and the other \(k-1\) scalar products equal \(1\). Write \(n_{i,j}=(x,y)\), with both coordinate sums zero, and put \(d=(j-i)\bmod k\in\{0,\ldots,k-1\}\). Then the equations become
\[
x_h-y_h=1-k\mathbf1_{h=i},\qquad x_{h+1}-y_h=1-k\mathbf1_{h=j},
\]
so \(x_{h+1}-x_h=k(\mathbf1_{h=i}-\mathbf1_{h=j})\). Solving the cyclic recurrence with zero mean gives the explicit integer normal
\[
x_h=-d+k\mathbf1_{\{1,\ldots,d\}}((h-i)\bmod k),\qquad
y_h=x_h-1+k\mathbf1_{h=i}.
\]
The indicator of an empty interval is zero when \(d=0\). These coordinates make the support inequalities strict at \(p_i,q_j\), since those two support values are \(1-k<1\).

Counting the entries of these two coordinate blocks, or expanding their centered squares, yields
\[
\boxed{\ \|n_{i,j}\|^2=k\bigl[k-1+2d(k-1-d)\bigr].\ }
\]
Therefore the Euclidean distance from \(c\) to the **supporting hyperplane** of \(F_{i,j}\) is precisely
\[
\delta_{i,j}=\bigl(k[k-1+2d(k-1-d)]\bigr)^{-1/2}.
\]
This is a statement about supporting *planes*; for a noncontact facet, the closest point on its plane need not lie in that facet.

**Step 3 (sharp inradius and contacting facets).** All cyclic shifts \(i\mapsto i+1\) act on \(P_k\) by Euclidean isometries, and their unique common fixed point in \(c+H\) is \(c\). For any radius for which a translated Euclidean ball is contained in \(P_k\), averaging the center over the cyclic group preserves feasibility (because the set of centers is convex). Hence a maximum-radius ball exists with center \(c\), and its radius is the minimum of the support-plane distances above.

The product \(d(k-1-d)\) attains its maximum at the middle integers. If \(k\) is odd, its unique maximizing offset is \(d=(k-1)/2\); if \(k\) is even, both offsets \(d=k/2-1\) and \(d=k/2\) maximize it. The maximal squared normal norm is \(k(k^2-1)/2\) in the odd case and \(k(k^2-2)/2\) in the even case. Taking reciprocal square roots gives the stated radius. Each fixed offset contributes \(k\) facets, giving the contacting counts \(k\) and \(2k\), respectively. The supporting ball touches each of these facets, since its plane-contact point belongs to the ball and the ball is contained in the polytope.

**Step 4 (all optimal centers and parity).** Let \(r_k\) be the optimal radius and write an arbitrary candidate center as \(c+t\), with \(t\in H\). The ball is contained in the polytope exactly when
\[
\langle n_{i,j},t\rangle\le 1-r_k\|n_{i,j}\|\quad\text{for all }i,j.
\]
The right side is zero exactly for contacting facets and strictly positive otherwise. For each contacting offset, its \(k\) cyclic normals sum to zero (each individual normal has zero total in each color class). Summing the corresponding nonpositive inequalities forces equality in every contact inequality. Conversely, any vector orthogonal to all contact normals, if sufficiently small, satisfies every remaining strict inequality. Thus \(\mathcal C_k\) has affine hull \(c+W_k^\perp\), where \(W_k\subseteq H\) is the span of the contact normals.

The coordinate-difference map \(\pi:H\to\mathbb R^k_0\), defined by \(\pi(x,y)=x-y\), sends any normal \(n_{i,j}\) to \(\mathbf1-k e_i\). As \(i\) varies these span the \((k-1)\)-dimensional zero-sum subspace. When \(k\) is odd, there are exactly \(k\) contact normals, their sum is zero, and their images under \(\pi\) span dimension \(k-1\). Hence \(\dim W_k=k-1\) and \(\dim\operatorname{aff}(\mathcal C_k)=(2k-2)-(k-1)=k-1\).

When \(k=2m\) is even, subtract the contact normal with offset \(m-1\) from the contact normal with offset \(m\), keeping its first omitted index \(i\) fixed. The explicit formula gives
\[
n_{i,i+m}-n_{i,i+m-1}=(k e_{i+m}-\mathbf1,\ k e_{i+m}-\mathbf1).
\]
These \(k\) differences span the diagonal subspace \(\{(z,z):\sum_h z_h=0\}\), of dimension \(k-1\), which is exactly the kernel of \(\pi\). Since the projected contact normals also span its \((k-1)\)-dimensional image, \(W_k=H\). Therefore \(\mathcal C_k=\{c\}\) when \(k\) is even. This establishes the complete assertion for every integer \(k\ge2\).

## Verification
The accompanying standalone source file `verify.py` uses exact rational arithmetic to construct all candidate support normals, compare every incidence scalar product, check the closed squared-norm formula, count active facets, and compute the exact contact span for \(2\le k\le14\). Independently of the displayed normal formula, the script solves the support systems directly for \(2\le k\le7\). With `python3 verify.py --hull` and optional NumPy/SciPy, it also builds ambient affine convex hulls independently for \(2\le k\le6\) and checks their complete facet planes and distance multisets. These checks passed. Finite checks do not replace the all-parameter argument above.

## Relationship to prior work
Kálmán and Postnikov's root-polytope treatment of bipartite graphs supplies general combinatorial facet techniques, but it does not give this Euclidean support-plane norm profile or the parity classification of optimal-ball centers [2]. Kálmán and Tóthmérész study geometric root polytopes of directed graphs, spanning-tree dissections, and lattice information [1,3], without the metric result proved here. A related published exact result on root polytopes of oriented cycles determines Ehrhart information, not these Euclidean invariants [4]. Thus known combinatorial equivalences (including edge polytopes obtained by changing signs in one color class) do not alone imply the metric conclusion without the explicit support-normal optimization and contact-span argument.

## Limitations
The result is for the alternating bipartite orientation, unweighted coordinate-root realization, and intrinsic ordinary Euclidean metric; it is not an invariant of all affinely equivalent realizations and makes no assertion for nonalternating orientations. Support-plane distances should not be confused with nearest-point distances to arbitrary noncontact faces. Other presentations under edge-polytope, polar, or free-sum terminology might contain equivalent results that were not found. No independent mathematical audit has been performed.

## References
[1] T. Kálmán and L. Tóthmérész, *Root polytopes and Jaeger-type dissections for directed graphs*, first public arXiv version 2021-05-03, https://arxiv.org/abs/2105.00960 (primary geometric setting, MSC 52B20).

[2] T. Kálmán and A. Postnikov, *Root polytopes, Tutte polynomials, and a duality theorem for bipartite graphs*, https://arxiv.org/abs/1602.04449 (root-polytope facet and combinatorial methods).

[3] T. Kálmán and L. Tóthmérész, *h*-vectors of graph polytopes using activities of dissecting spanning trees*, https://arxiv.org/abs/2203.17127 (related lattice geometry, not Euclidean inballs).

[4] *Exact Ehrhart polynomials of oriented cycle root polytopes*, published published-finding corpus record https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-ehrhart-polynomials-of-oriented-cycle-root-polytopes--e32575b66377 (indexed title and synopsis inspected, not full text).
