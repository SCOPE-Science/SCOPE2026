# Sharp Euclidean rounding of cube–cross-polytope intersections

## Finding

For every integer \(d\ge 2\), consider the natural signed-permutation-invariant interpolation
\[
K_{d,t}=[-1,1]^d\cap\{x\in\mathbb R^d:\|x\|_1\le t\},\qquad t>0.
\]
Let \(d_{\mathrm{BM}}\) denote the Banach–Mazur distance between origin-symmetric convex bodies and let \(B_2^d\) be the Euclidean unit ball. For \(1\le t\le d\), set \(k=\lfloor t\rfloor\). Then
\[
\boxed{d_{\mathrm{BM}}(K_{d,t},B_2^d)
=\frac{\sqrt{k+(t-k)^2}}{\min\{1,t/\sqrt d\}}.}
\]
The infimum over **all** invertible linear transformations is attained by an unrotated, uniformly scaled Euclidean ball. Moreover, **every** centered ellipsoid realizing this distance is a Euclidean ball up to homothety; non-spherical shears or tilts cannot improve or tie it.

On the entire interpolation \(t>0\), the exact sharp optimization is
\[
\boxed{\arg\min_{t>0}d_{\mathrm{BM}}(K_{d,t},B_2^d)=\{\sqrt d\}.}
\]
Writing \(m=\lfloor\sqrt d\rfloor\), its minimum value is
\[
\boxed{D_d=\sqrt{m+(\sqrt d-m)^2}
=\sqrt{\sqrt d-\{\sqrt d\}(1-\{\sqrt d\})}.}
\]
In particular, as \(d\to\infty\),
\[
D_d=d^{1/4}\left(1-\frac{\{\sqrt d\}(1-\{\sqrt d\})}{2\sqrt d}
+O(d^{-1})\right).
\]
The minimum has an exact **arithmetic regularity transition**. If \(d\) is not a square, put \(q=\sqrt d\), \(m=\lfloor q\rfloor\), and \(a=q-m\in(0,1)\). The one-sided derivatives of the **squared** distance at its minimizer are
\[
(D(t)^2)'_{t=q^-}=-\frac{2m(1-a)}q<0,\qquad
(D(t)^2)'_{t=q^+}=2a>0.
\]
Thus a nonsquare dimension has a genuine linear cusp. If \(d=m^2\) with \(m\ge2\), the minimum is instead differentiable, with unequal quadratic coefficients:
\[
D(m+\delta)^2=
\begin{cases}
m+\frac{m-1}{m}\delta^2+O(|\delta|^3),&\delta\uparrow0,\\
m+\delta^2,&\delta\downarrow0.
\end{cases}
\]

For \(d=2\), the unique best member is the regular octagon, and its distance is \(\sqrt{4-2\sqrt2}=\sec(\pi/8)\). For \(d=3\), the best parameter is \(\sqrt3\), rather than the regular truncated-octahedron parameter \(3/2\).

## Assumptions and scope

We work in standard Euclidean coordinates. The parameter is real and positive, the dimension \(d\) is an arbitrary integer at least two, and all convex bodies have nonempty interior and are centrally symmetric. We use the standard Banach–Mazur distance of their induced real normed spaces; the usual arbitrary translations may be omitted for origin-symmetric unit balls. The statement of uniqueness concerns the quadratic shape matrix of an optimal centered ellipsoid, not the irrelevant scalar or orthogonal freedom in its presentation.

For \(0<t\le1\), the body is exactly \(tB_1^d\); for \(t\ge d\), it is \(B_\infty^d\). Both exterior regimes have distance \(\sqrt d\), and no exterior parameter minimizes when \(d\ge2\).

## Proof

**1. Exact Euclidean radii.** On \(K_{d,t}\) with \(1\le t\le d\), maximize \(\sum_i x_i^2\) subject to \(0\le |x_i|\le1\) and \(\sum_i|x_i|\le t\). At a maximizer all available \(\ell_1\) budget is used. If two unsaturated absolute coordinates were positive, moving mass from the smaller to the larger one would strictly increase the squared norm. Thus a maximizer has \(k=\lfloor t\rfloor\) coordinates of magnitude one, at most one coordinate of magnitude \(t-k\), and zeros elsewhere. The squared maximal radius is exactly
\[
R^2=k+(t-k)^2.
\]
The inradius follows directly from the defining supporting halfspaces: \(|x_i|\le1\) have Euclidean facet distance one, while every signed halfspace \(\sum_i\sigma_i x_i\le t\) has distance \(t/\sqrt d\) from the origin. Hence
\[
r=\min\{1,t/\sqrt d\}.
\]
These are true maximal inscribed and minimal circumscribed concentric ball radii: any strictly larger centered ball violates at least one defining halfspace, and any strictly smaller centered circumball misses a maximizing vertex. Central symmetry gives the same optimal centers even if translations are initially allowed.

**2. All-ellipsoid optimality (not merely spherical radii).** Write \(K=K_{d,t}\) and let \(K^\circ\) be its polar. Standard polarity gives
\[
K^\circ=\operatorname{conv}\big(B_1^d\cup t^{-1}B_\infty^d\big).
\]
Let \(v\in K\) be any contact with the outer sphere of radius \(R\), and let \(w\in K^\circ\) be a contact with the outer sphere of radius \(1/r\). Such contacts exist by compactness and the radii calculation. The full group \(G\) of signed coordinate permutations acts orthogonally on both bodies. For its uniform orbit average, sign symmetry kills off-diagonal entries and coordinate transitivity equalizes the diagonals, giving the **exact matrix identities**
\[
\frac1{|G|}\sum_{g\in G}(gv)(gv)^{\mathsf T}=\frac{R^2}{d}I_d,
\qquad
\frac1{|G|}\sum_{g\in G}(gw)(gw)^{\mathsf T}=\frac{1}{dr^2}I_d.
\]
Take an arbitrary symmetric positive definite matrix \(A\). Define
\[
M(A)=\max_{x\in K}x^{\mathsf T}Ax,\qquad
N(A)=\max_{y\in K^\circ}y^{\mathsf T}A^{-1}y.
\]
The best containment ratio associated with the quadratic metric \(A\) has square \(M(A)N(A)\). The above orbit identities yield
\[
M(A)\ge\frac{R^2}{d}\operatorname{tr}A,
\qquad N(A)\ge\frac{1}{dr^2}\operatorname{tr}A^{-1}.
\]
Writing \(\lambda_1,\ldots,\lambda_d>0\) for the eigenvalues of \(A\), Cauchy–Schwarz implies
\[
M(A)N(A)\ge\frac{R^2}{r^2}
\frac{(\sum_i\lambda_i)(\sum_i\lambda_i^{-1})}{d^2}
\ge \frac{R^2}{r^2}.
\]
In fact, the exact eigenvalue identity provides a quantitative stability bound for *any* such ellipsoidal metric:
\[
M(A)N(A)\ge\frac{R^2}{r^2}
\left(1+\frac1{d^2}\sum_{i<j}\frac{(\lambda_i-\lambda_j)^2}{\lambda_i\lambda_j}\right).
\]
Here, by definition, \(N(A)\) includes the inverse metric \(A^{-1}\). At \(A=I_d\), equality holds. Equality in the second inequality forces all eigenvalues equal. Therefore \(R/r\) is the **global** Banach–Mazur distance and the optimal positive-definite quadratic shape is unique up to scalar. The reduction to positive-definite \(A\) is exact because every linear image of the Euclidean ball is an origin-centered ellipsoid, and all such ellipsoids arise from such a metric.

**3. Unique optimal cutoff.** On every open subinterval \(k<t<k+1\) lying below \(\sqrt d\), the squared distance is
\[
D(t)^2=\frac{d\,[k+(t-k)^2]}{t^2},\qquad
\frac{d}{dt}D(t)^2=\frac{2dk(t-k-1)}{t^3}<0
\]
(where \(k\ge1\)). Above \(\sqrt d\), the squared distance is \(k+(t-k)^2\), strictly increasing on every nontrivial interval between integers. Continuity across integer breakpoints therefore makes the distance strictly decreasing on \([1,\sqrt d]\), strictly increasing on \([\sqrt d,d]\), and constant at the larger endpoint value \(\sqrt d\) outside \([1,d]\). Thus the global minimizer is uniquely \(t=\sqrt d\). Substitution and the binomial series give the formulas above. Direct one-sided differentiation gives the stated cusp in nonsquare dimensions; substituting \(d=m^2\) and expanding at the integer breakpoint gives the two quadratic coefficients in square dimensions.

## Verification

The accompanying standalone `CHECK.py` uses exact rational arithmetic to enumerate the outer contacts and polar contact orbits for sample rational cutoffs in dimensions two through seven. It independently checks both isotropic covariance identities and the trace-based lower bound for explicit nonscalar positive-definite metrics and their exact inverses. Finite numerical checks of the piecewise monotonicity were run through dimension 119, and the planar regular-octagon benchmark was compared with \(\sec(\pi/8)\). The checker returns `VERIFY_OK`. The universal theorem and uniqueness rely on the proof above, not on finite enumeration or samples.

## Relationship to prior work

Grundbacher and Kobos (2026, arXiv:2603.18268) determine exact distances for direct sums of independent normed-space blocks and related cone constructions. The present overlapping pair of constraints defining \(K_{d,t}\) is neither an \(\ell_p\)-direct sum nor one of those cones. Grundbacher and Kobos (2026, arXiv:2602.14847) give an abstract contact-point characterization of optimal Euclidean Banach–Mazur positions. Our orbit-average argument is consistent with that general framework, but the sharp cutoff \(\sqrt d\), the complete parameter profile, the contact radii, and the dimension-dependent minimum do not follow without the explicit family calculation. The familiar cube and cross-polytope endpoint distance \(\sqrt d\), as well as the planar regular-octagon benchmark, are prior background, not new claims.

## Limitations

This is an exact optimization within a single symmetric convex-body family, not a comparison over all centrally symmetric convex bodies, all convex interpolations, or non-Euclidean target spaces. The uniqueness statement is for optimal ellipsoidal quadratic shape; the minimizing cutoff is unique inside this specifically normalized intersection family. The distance is not asserted to determine the body's combinatorial type. Published priority of an equivalent computation in inaccessible or unindexed literature is not independently certified.

## References

1. F. Grundbacher and T. Kobos, *Exact Banach–Mazur distances of certain \(\ell_p\)-sums and cones*, arXiv:2603.18268 (initial public posting March 18, 2026), https://arxiv.org/abs/2603.18268.
2. F. Grundbacher and T. Kobos, *John-type decompositions for affinely-optimal positions of convex bodies*, arXiv:2602.14847 (initial public posting February 16, 2026), https://arxiv.org/abs/2602.14847.
3. F. Grundbacher and T. Kobos, *On certain extremal Banach–Mazur distances and Ader's characterization of distance ellipsoids*, arXiv:2407.08829 (initial public posting July 11, 2024), https://arxiv.org/abs/2407.08829.
