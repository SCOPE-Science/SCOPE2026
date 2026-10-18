# Two antipodal vertices determine the Euclidean outer sphere of every generic cross-polytope monotone-path polytope
## Finding
For every integer \(n\ge3\) and strictly increasing positive real numbers \(0<a_1<\cdots<a_n\), put
\[
D_n=\operatorname{conv}\{\pm e_1,\ldots,\pm e_n\}\subset\mathbb R^n,
\qquad \ell(x)=\sum_{i=1}^{n}a_i x_i.
\]
Let \(P_n(a)=\operatorname{MPP}_{\ell}(D_n)\) be the monotone-path (fiber) polytope with the **normalized** vertex realization obtained by averaging path sections over \([-a_n,a_n]\); equip its affine hull \(\ker\ell\) with the Euclidean metric induced from \(\mathbb R^n\). Then its unique smallest enclosing Euclidean ball has center \(0\) and radius
\[
\boxed{R(P_n(a))=\frac12\sqrt{1+\left(\frac{a_{n-1}}{a_n}\right)^2}.}
\tag{1}
\]
Of its \(3^{n-1}-1\) vertices, precisely two touch this sphere:
\[
\boxed{v_\pm=\pm\frac12\left(e_{n-1}-\frac{a_{n-1}}{a_n}e_n\right).}
\tag{2}
\]
They are obtained from the two coherent monotone paths \(-e_n\to\pm e_{n-1}\to e_n\). They form the unique diametral pair, so
\[
\boxed{\operatorname{diam}_2 P_n(a)=\sqrt{1+(a_{n-1}/a_n)^2}.}
\tag{3}
\]
Every vertex corresponding to a coherent path with at least two intermediate vertices has the **uniform strict squared-radius clearance**
\[
R(P_n(a))^2-\|v\|_2^2\ge\frac{(a_n-a_{n-1})^2}{8a_n^2}>0.
\tag{4}
\]
Thus the entire outer Euclidean sphere and all its contact vertices depend only on the largest two positive projection coefficients, even though all coefficients change the realization.

## Assumptions and scope
The cross-polytope is the standard unit-coordinate cross-polytope, not a general affine image. The projection is generic with positive strictly ordered coefficients; coordinate permutation and sign changes reduce any generic orientation to this case via Euclidean isometries. The metric is the standard ambient Euclidean metric restricted to the actual fiber-polytope subspace \(\ker\ell\), *not* a metric transported by a combinatorial or arbitrary affine equivalence.

The normalized monotone-path vertex of a coherent path \(p_0,\ldots,p_{k+1}\), with \(p_0=-e_n\), \(p_{k+1}=e_n\), and strictly increasing heights \(t_j=\ell(p_j)\), is defined by the height-average trapezoid formula
\[
v(p_0,\ldots,p_{k+1})=\frac1{4a_n}\sum_{j=0}^{k}(t_{j+1}-t_j)(p_j+p_{j+1}).
\tag{5}
\]
This fixes the scale in (1)--(4). By Black and De Loera's characterization, the coherent paths are exactly those using one or more signed vertices \(\sigma_j e_{i_j}\), \(i_j<n\), with no repeated absolute index, ordered by height; all such paths give distinct vertices. There is no coherent direct antipodal edge \(-e_n\to e_n\) with zero intermediate vertices.

## Proof
Set \(A=a_n\) and \(B=a_{n-1}\), so \(0<B<A\). For any coherent path write the intermediate heights
\[
-B\le t_1<\cdots<t_k\le B,\qquad 1\le k\le n-1,
\]
where \(t_j=\sigma_j a_{i_j}\), \(p_j=\sigma_j e_{i_j}\), \(t_0=-A\), and \(t_{k+1}=A\). Formula (5) telescopes coordinatewise to
\[
v_{i_j}=\frac{\sigma_j}{4A}(t_{j+1}-t_{j-1}),
\qquad v_n=-\frac{t_1+t_k}{4A},
\tag{6}
\]
all other coordinates being zero. Therefore
\[
16A^2\|v\|_2^2=F_k(t_1,\ldots,t_k)
=\sum_{j=1}^{k}(t_{j+1}-t_{j-1})^2+(t_1+t_k)^2.
\tag{7}
\]
For \(k=1\), \(F_1=4(A^2+t_1^2)\), whence
\[
\|v\|_2^2=\frac14\left(1+\frac{a_{i_1}^2}{A^2}\right)
\le\frac14\left(1+\frac{B^2}{A^2}\right).
\]
Equality is possible exactly for \(i_1=n-1\), with either sign, producing (2).

For \(k\ge2\), extend the domain of (7) from the discrete intermediate heights to the closed ordered simplex
\[
\mathcal T_k=\{(t_1,\ldots,t_k):-B\le t_1\le\cdots\le t_k\le B\}.
\]
Each term of \(F_k\) is a square of an affine function, so \(F_k\) is convex. Its maximum over this simplex is therefore reached at a vertex, which must have the form
\[
t_1=\cdots=t_r=-B,\qquad
 t_{r+1}=\cdots=t_k=B,\qquad 0\le r\le k.
\tag{8}
\]
For \(k=2\), the mixed vertex \(r=1\) gives \(F_2=2(A+B)^2\), while either constant vertex gives \(F_2=2A^2+6B^2\). For \(k\ge3\), the constant vertices and the two endpoint switches \(r=1,k-1\) yield \(F_k=2A^2+6B^2\). When \(k\ge4\), an interior switch \(2\le r\le k-2\) yields \(F_k=2(A-B)^2+8B^2\). These exhaust the simplex vertices.

Both expressions for \(k\ge3\) are at most \(2(A+B)^2\), because
\[
2(A+B)^2-(2A^2+6B^2)=4B(A-B)>0,
\]
and
\[
2(A+B)^2-\bigl(2(A-B)^2+8B^2\bigr)=8B(A-B)>0.
\]
Consequently every coherent path with \(k\ge2\) has
\[
16A^2\|v\|_2^2\le2(A+B)^2
=4(A^2+B^2)-2(A-B)^2
<4(A^2+B^2),
\tag{9}
\]
which establishes (4) and excludes all such paths from outer contact. Combined with the \(k=1\) case, this shows every generating vertex belongs to the origin-centered ball of radius (1), with equality precisely at the pair (2). The convex hull belongs to the ball by convexity.

Since \(v_-=-v_+\), any enclosing ball has radius at least \(\|v_+\|_2=R\). If an enclosing ball with this radius had center \(c\), the identity
\[
\frac{\|v_+-c\|_2^2+\|v_--c\|_2^2}{2}
=R^2+\|c\|_2^2
\]
forces \(c=0\); hence the optimal ball and its center are unique. Strict convexity of squared Euclidean norm implies that a convex combination of the vertices can lie on this optimal sphere only if all participating vertices are the same contact vertex. Therefore (2) lists **all** outer contacts, not just contacting generators. Any diametral pair must lie at opposite ends of a diameter of the enclosing ball, proving uniqueness and (3). \(\square\)

## Verification
The symbolic argument handles all real coefficients satisfying the stated inequalities, with no rationality assumption. To corroborate the path integration and the convex-simplex inequality independently, `verify_signohedron.py` computes (5) directly segment by segment with exact rational arithmetic, enumerates coherent sign patterns, checks \(\ell(v)=0\), the predicted radius, exactly two contacts, and the multi-intermediate clearance (4). It passed 597 strictly ordered positive rational coefficient profiles in dimensions 2--9, covering 198,294 coherent path vertices, including 193,860 with multiple intermediate vertices. Dimension two is included only as an additional diagnostic and is not needed by the theorem. The finite checks do not establish the universal statement independently of the proof.

## Relationship to prior work
Black and De Loera, *Monotone Paths on Cross-Polytopes* (arXiv:2102.01237), prove the exact coherent-path indexing, signed-path vertex description, and facet and face data used as starting points here. Their diameter \(2(n-1)\) is **one-skeleton graph diameter in number of flips**; it is not the Euclidean diameter (3). The present argument adds an optimization over the actual normalized geometric coordinates and proves a global Euclidean minimum-enclosing ball and complete outer contacts.

A published result on the canonical polar representative \(([-1,1]^d+\operatorname{conv}\{\pm e_i\})^\circ\) computes its own Euclidean radius \(1/2\) and its \(2d\) contacting vertices. That realization is merely **combinatorially equivalent** to a generic monotone-path polytope; its Euclidean metric and radial coordinates are not the orientation-dependent realization (5). In particular, formula (1) varies continuously with \(B/A\) and exceeds \(1/2\), so the polar-representative theorem does not imply (1)--(4). Another published coherent-path result establishes flip-distance enumeration on the sign-vector graph, which concerns combinatorial rather than Euclidean distance. These comparisons were performed against the materially inspected full statements, not titles alone.

## Limitations
The theorem is realization-sensitive and does not claim the same radius under arbitrary affine transformations of a signohedron or for nongeneric projections with equal-height ties. It determines the circumradius, Euclidean diameter, and outer contacts but not inradius, John/Löwner ellipsoids, volume, or the full vertex norm distribution. The gap (4) applies only to paths with at least two intermediate vertices; shorter noncontacting paths have a separate positive coefficient gap. Accessible primary mathematical records have been compared, but an unindexed equivalent assertion under other terminology cannot be categorically excluded. Independent validation has not been performed.

## References
1. Alexander E. Black and Jesús A. De Loera, *Monotone Paths on Cross-Polytopes*, arXiv:2102.01237, first posted 2021-02-02, revised 2021-04-15, primary MSC 52B05; Theorem 1.1 and the restatement of Billera--Sturmfels Theorem 5.3. https://arxiv.org/html/2102.01237v2
2. L. J. Billera and B. Sturmfels, *Fiber Polytopes*, *Annals of Mathematics* 135 (1992), 527--549, cited through the explicit monotone-path vertex formula reproduced in reference 1.
3. *Canonical signohedra are tangential with exact radial shells*, published geometrical result on the polar of a cube plus crosspolytope, consulted via its complete public theorem and proof; distinct Euclidean realization.
4. *Exact flip-distance enumerator of cross-polytope coherent monotone paths*, published combinatorial graph-distance result, consulted via its complete public theorem and proof; different metric.
