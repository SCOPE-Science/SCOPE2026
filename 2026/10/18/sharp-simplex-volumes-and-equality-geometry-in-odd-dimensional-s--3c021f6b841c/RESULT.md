# Sharp simplex volumes and equality geometry in odd-dimensional spherical slabs

## Finding

For every odd integer \(d=2k+1\ge 3\) and every \(0<t\le 1\), put
\[
K_{d,t}=\{(x,z)\in\mathbb R^{d-1}\times\mathbb R:\ \|x\|_2^2+z^2\le 1,\ |z|\le t\}.
\]
Let \(M_d(t)\) denote the largest \(d\)-dimensional volume of any simplex contained in \(K_{d,t}\), with no restriction that its vertices belong to a prescribed finite set. Then
\[
\boxed{M_d(t)=\begin{cases}
\dfrac{(d+1)^{(d+1)/2}}{d!(d-1)^{(d-1)/2}}\,t(1-t^2)^{(d-1)/2},&0<t\le 1/\sqrt d,\\[5pt]
\dfrac{(d+1)^{(d+1)/2}}{d!d^{d/2}},&1/\sqrt d\le t\le 1.
\end{cases}}
\]
For \(0<t\le 1/\sqrt d\), every maximizing simplex consists of two centroid-centered regular \(k\)-simplices, with \(k+1\) vertices each, in orthogonal horizontal \(k\)-planes of radius \(\sqrt{1-t^2}\), one on \(z=t\) and one on \(z=-t\). Conversely every such configuration is maximizing. For \(1/\sqrt d<t\le1\), the maximizers are exactly the regular \(d\)-simplices inscribed in the unit sphere whose vertices satisfy \(|z|\le t\).

The occupied-volume fraction \(M_d(t)/\operatorname{vol}_d(K_{d,t})\) decreases strictly throughout \(0<t\le1\). The critical slab half-width \(1/\sqrt d\) is sharp and marks saturation at the unrestricted ball-simplex maximum.

## Assumptions and scope

Volume means ordinary Euclidean \(d\)-volume. A simplex is the convex hull of \(d+1\) affinely independent points; the maximum is attained by compactness. The parameter \(t\) is dimensionless because the ambient ball has radius one. The limit \(t\downarrow0\) is not a full-dimensional containing body and is deliberately excluded. The odd-dimension hypothesis is essential for the displayed sharpness construction; no exact claim is made for even \(d\). Rotation about the distinguished \(z\)-axis, interchange of the two horizontal layers, and permutations of simplex vertices do not change the geometric extremizers.

A regular \(k\)-simplex on a horizontal sphere of radius \(r\) is a collection of \(k+1\) points of norm \(r\) with pairwise inner product \(-r^2/k\) and centroid zero. Two such simplices are orthogonal when their linear spans are orthogonal.

## Proof

**1. Ball simplex lemma and equality.** For arbitrary \(p_0,\dots,p_d\in\overline B^d\), write \(\mu=(d+1)^{-1}\sum p_i\) and
\[
C=\sum_{i=0}^{d}(p_i-\mu)(p_i-\mu)^T.
\]
The elementary Gram-determinant identity is
\[
(d!)^2\operatorname{vol}_d(\operatorname{conv}\{p_i\})^2=(d+1)\det C.
\]
Indeed, for the edge matrix \(E=[p_1-p_0\ \cdots\ p_d-p_0]\), we have \(C=E(I_d-\mathbf1\mathbf1^T/(d+1))E^T\), and the rank-one determinant identity gives \(\det(I_d-\mathbf1\mathbf1^T/(d+1))=1/(d+1)\). Moreover,
\[
\operatorname{tr} C=\sum_i\|p_i\|^2-(d+1)\|\mu\|^2\le d+1.
\]
Arithmetic–geometric mean for the nonnegative eigenvalues yields \(\det C\le((d+1)/d)^d\). Hence
\[
\operatorname{vol}_d(\operatorname{conv}\{p_i\})\le
c_d:=\frac{(d+1)^{(d+1)/2}}{d!d^{d/2}}.
\]
Equality requires \(\mu=0\), all \(\|p_i\|=1\), and \(C=(d+1)I_d/d\). The matrix of the \(d+1\) points therefore has Gram matrix \((d+1)I_{d+1}/d-\mathbf1\mathbf1^T/d\), so its distinct columns have inner product \(-1/d\). These conditions are also sufficient: the equality configurations are exactly centered regular simplices on the unit sphere.

**2. An exact enclosing ellipsoid.** Assume \(0<t\le 1/\sqrt d\), and define the positive numbers
\[
A=\frac d{d-1}(1-t^2),\qquad B=d\,t^2,
\]
and the ellipsoid \(E=\{(x,z):\|x\|^2/A+z^2/B\le1\}\). For every \(|z|\le t\), direct expansion gives
\[
A\bigl(1-z^2/B\bigr)-(1-z^2)
=\frac{1-dt^2}{d-1}\left(1-\frac{z^2}{t^2}\right)\ge0.
\]
Consequently \(K_{d,t}\subseteq E\). Applying the ball simplex lemma to the linear image \((x,z)\mapsto(x/\sqrt A,z/\sqrt B)\) gives, for every contained simplex,
\[
\operatorname{vol}_d(\Delta)\le c_d A^{(d-1)/2}\sqrt B
=\frac{(d+1)^{(d+1)/2}}{d!(d-1)^{(d-1)/2}}t(1-t^2)^{(d-1)/2}.
\]
For \(t\ge1/\sqrt d\), inclusion \(K_{d,t}\subseteq\overline B^d\) instead gives \(M_d(t)\le c_d\).

**3. Sharpness in every odd dimension.** Set \(d=2k+1\) and decompose the horizontal space as \(\mathbb R^{2k}=U\oplus V\), with \(\dim U=\dim V=k\) and \(U\perp V\). Let \(r=\sqrt{1-t^2}\). In \(U\) select a centered regular \(k\)-simplex \(\{u_0,\ldots,u_k\}\) of circumradius \(r\), and in \(V\) a second one \(\{v_0,\ldots,v_k\}\). The \(d+1=2(k+1)\) points
\[
(u_0,t),\ldots,(u_k,t),\quad(v_0,-t),\ldots,(v_k,-t)
\]
belong to \(K_{d,t}\). Under the linear normalization from step 2, every transformed point has norm one; inner products of two distinct points are \(-1/d\), since
\[
\frac{r^2}{A}=\frac{d-1}{d},\qquad \frac{t^2}{B}=\frac1d,\qquad
\langle u_i,u_j\rangle=\langle v_i,v_j\rangle=-\frac{r^2}{k}\ \ (i\ne j),\qquad\langle u_i,v_j\rangle=0.
\]
Thus the transformed points form a regular \(d\)-simplex, attaining the ellipsoid upper bound. At \(t_0=1/\sqrt d\), the defining ellipsoid is the unit ball, and the same construction is a regular ball-inscribed simplex. This fixed simplex remains feasible for every \(t\ge t_0\), giving \(M_d(t)=c_d\) on the second branch.

**4. All equality configurations.** Suppose first \(0<t<t_0\). Equality in the ellipsoid simplex bound forces the transformed vertices to be those of a centered regular unit-sphere simplex. In the strict enclosure identity from step 2, equality at a boundary point of \(K_{d,t}\) and \(E\) is possible only when \(|z|=t\) and \(\|x\|=r\). The transformed vertical coordinates are therefore \(\pm1/\sqrt d\). Their sum is zero, so exactly \((d+1)/2=k+1\) vertices occur at each sign. For distinct vertices in the same layer, the required inner product \(-1/d\) implies horizontal inner product \(-r^2/k\); for opposite layers it implies horizontal orthogonality. This is precisely the pair of orthogonal centered regular \(k\)-simplices claimed above, and the converse was proved in step 3.

At \(t=t_0\), every maximizing simplex is a unit-sphere regular simplex. Its vertical coordinates \(z_i\) satisfy \(\sum_i z_i^2=(d+1)/d\), while each \(|z_i|\le1/\sqrt d\). Thus every \(|z_i|=1/\sqrt d\), and the same two-layer classification follows. For \(t>t_0\), equality in the full-ball bound gives precisely the feasible centered regular ball-inscribed simplices.

**5. Strict occupied-volume decay.** Let \(\kappa_{d-1}\) be the volume of the unit ball of \(\mathbb R^{d-1}\), and put \(g(s)=(1-s^2)^k\). Cross-sectional integration gives
\[
\operatorname{vol}_d(K_{d,t})=2\kappa_{d-1}\int_0^t g(s)\,ds.
\]
For \(t\le t_0\), the occupied fraction is a positive dimension-dependent constant times
\[
\frac{t g(t)}{\int_0^t g(s)\,ds}
=\left[\int_0^1\left(\frac{1-t^2u^2}{1-t^2}\right)^kdu\right]^{-1}.
\]
For each \(0\le u<1\) the integrand on the right strictly increases as \(t\) increases in \((0,1)\), proving strict decrease of this ratio. For \(t\ge t_0\), the numerator \(M_d(t)=c_d\) is constant and the body's volume increases strictly up to \(t=1\). The two formulas agree at the transition, so strict decrease holds throughout.

## Verification

The accompanying `verify.py` uses only Python's standard library and exact rational arithmetic. It constructs the Gram matrix of the explicit odd-dimensional witnesses and verifies the squared-volume formula in dimensions \(3,5,7,9\) at twelve rational slab widths. It also checks six transition identities, four monotonicity sample sequences, and the orthogonality and inner-product identities. Run with `python3 verify.py` from the directory containing this file and `RESULT.md`. The expected terminal line is `VERIFY_OK exact_odd_dimension_cases=12 transition_identities=6 monotonicity_samples=4`.

Those finite checks test formulas and examples; the uniform theorem, all equality cases, and monotonicity are proved above. No external or independent mathematical audit has been carried out.

## Relationship to prior work

Horváth and Lángi (2014), particularly their Corollary 1, characterize maximum-volume simplices inscribed in the full unit sphere; that special full-ball bound is used in step 1. They study fixed numbers of sphere-vertex polytopes, not the varying-width intersection of a ball with a symmetric slab, its odd-dimensional contact geometry, or its occupied-volume monotonicity.

Lassak (2010) gives width identities and necessary geometric constraints for maximum-volume simplices in normed-space unit balls. Lassak (2011) gives a universal barycentric-dilation bound for simplices inscribed in arbitrary convex bodies. Neither yields the sharp spherical-slab profile by the stated conclusions. These comparisons distinguish the present all-width formula from general necessary conditions and universal bounds; they do not establish absolute historical priority. McKinney (1974) studies maxima in centrally symmetric convex bodies. Only its published extract could be inspected; its inaccessible full text is a separately identified priority risk, and no claim of noncoverage is drawn from the extract alone.

## Limitations

The formula and complete classification are asserted only in odd dimensions \(d\ge3\). In even dimensions, the low-width ellipsoid bound cannot attain equality through the present two-layer method: a centered regular simplex would require an equal number of plus and minus signs among the odd number \(d+1\) of vertices. This observation is not an even-dimensional optimality theorem. The three cited sources and targeted literature searches do not exclude a previously published equivalent formula under another description of spherical slices, caps, or truncated balls. The result is a mathematical proof with limited computational corroboration, not an independently certified statement.

## References

1. Á. G. Horváth and Z. Lángi, *Maximum volume polytopes inscribed in the unit sphere*, arXiv:1402.6496, first publicly submitted 2014-02-26, https://arxiv.org/abs/1402.6496 ; full text https://arxiv.org/html/1402.6496v3 .
2. M. Lassak, *Simplices of maximum volume contained in the unit ball of a normed space*, Publicationes Mathematicae Debrecen 77 (2010), 79–86, https://publi.math.unideb.hu/paper/1476/download/ .
3. M. Lassak, *Approximation of convex bodies by inscribed simplices of maximum volume*, Contributions to Algebra and Geometry 52 (2011), 389–394, https://doi.org/10.1007/s13366-011-0026-x .
4. J. R. McKinney, *On maximal simplices inscribed in a central convex set*, Mathematika 21 (1974), 38–44, https://doi.org/10.1112/S0025579300005763 (public extract inspected; complete text unavailable).
