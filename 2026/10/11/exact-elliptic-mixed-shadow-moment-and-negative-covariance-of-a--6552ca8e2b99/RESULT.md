# Exact elliptic mixed shadow moment and negative covariance of a regular tetrahedron

## Finding
For a regular tetrahedron \(T\subset\mathbb R^3\) of unit edge length, choose \(U\) uniformly on the unit sphere and let \(A(U)\) and \(P(U)\) be the area and perimeter of the orthogonal planar projection of \(T\) onto \(U^\perp\). Set \(\theta=\arctan\sqrt2\). Then
\[
\mathbb E[A(U)P(U)] = \frac{4\sqrt3}{3\pi}+\frac{\sqrt2}{\pi}\left(2E(\theta\mid-1/2)-F(\theta\mid-1/2)\right)=1.24063482223759\ldots,
\]
where \(F\) and \(E\) are the standard incomplete elliptic integrals. Moreover \(\mathbb EA=\sqrt3/4\), \(\mathbb EP=3\theta\), and the area–perimeter covariance is strictly negative:
\[
-0.0004<\operatorname{Cov}(A,P)<-0.0003.
\]
The explicit special-function evaluation and rigorously certified sign refine the previously reported numerical mixed moment; the numerical value and a negative numerical correlation are not claimed as new.

## Assumptions and scope
The tetrahedron has all six edge lengths equal to one. The direction \(U\) has rotation-invariant probability measure \(d\sigma/(4\pi)\) on \(S^2\). Projection silhouettes may degenerate on a measure-zero set, which does not affect the moments. Area is two-dimensional Lebesgue area and perimeter is Euclidean polygonal perimeter. For \(0\le\phi<\pi/2\), define
\[
F(\phi\mid m)=\int_0^\phi\frac{dt}{\sqrt{1-m\sin^2t}},\qquad E(\phi\mid m)=\int_0^\phi\sqrt{1-m\sin^2t}\,dt.
\]
The theorem concerns this two-variable mixed moment, not the full joint distribution or higher moments. Uniform rescaling of edge lengths by \(\ell>0\) multiplies the mixed moment and covariance by \(\ell^3\).

## Proof
Write \(c=1/\sqrt3\), \(s=\sqrt{2/3}\), and let the four unit outward face normals be
\[
n_1=(c,s,0),\quad n_2=(c,-s,0),\quad n_3=(-c,0,s),\quad n_4=(-c,0,-s).
\]
Their pairwise scalar products are \(-1/3\). The points \(v_i=-(\sqrt6/4)n_i\) form a regular tetrahedron of unit edge length. Each face has area \(\sqrt3/4\). Cauchy's projection formula for the facets therefore gives
\[
A(u)=\frac{\sqrt3}{8}\sum_{i=1}^4|u\cdot n_i|.
\tag{1}
\]
For an edge adjacent to the faces with outward normals \(n_i,n_j\), put \(e_{ij}=(n_i\times n_j)/\|n_i\times n_j\|\). That edge belongs to the projected silhouette exactly when \((u\cdot n_i)(u\cdot n_j)<0\), outside a measure-zero set. Its projected length is \(\sqrt{1-(u\cdot e_{ij})^2}\). Thus
\[
P(u)=\sum_{1\le i<j\le4}{\bf1}_{\{(u\cdot n_i)(u\cdot n_j)<0\}}\sqrt{1-(u\cdot e_{ij})^2}.
\tag{2}
\]
All six edge terms have equal integrals when multiplied by \(A(u)\), by tetrahedral symmetry. For the pair \((1,2)\), the edge direction is parallel to the third coordinate axis. Parameterize the unit sphere by
\[
u=(\sin\varphi\cos t,\sin\varphi\sin t,\cos\varphi),\qquad 0\le\varphi\le\pi,\quad 0\le t<2\pi.
\]
Put \(\alpha=\arctan(1/\sqrt2)=\pi/2-\theta\). The sign condition in (2) is \(|\tan t|>1/\sqrt2\); by fourfold absolute-value symmetry it suffices to integrate \(\alpha\le t\le\pi/2\) and multiply by four. There the four absolute face-normal products sum to
\[
2s\sin\varphi\sin t+2\max(c\sin\varphi\cos t,s|\cos\varphi|).
\]
Splitting the second integral at \(\varphi_0=\arctan(\sqrt2/\cos t)\) and using \(\int_0^\pi\sin^3\varphi\,d\varphi=4/3\) gives, by elementary antiderivatives,
\[
\int_0^\pi\sin^2\varphi\sum_{i=1}^4|u\cdot n_i|\,d\varphi
=\frac83\left(s\sin t+c\frac{1+\cos^2t}{\sqrt{2+\cos^2t}}\right).
\tag{3}
\]
The additional factor \(\sin\varphi\) in the projected edge length and the spherical area element \(\sin\varphi\,d\varphi dt\) explain the square of \(\sin\varphi\) in (3). Combining the six edges, the four symmetric angular sectors, (1), and (3) yields
\[
\mathbb E[AP]=\frac{2\sqrt3}{\pi}\int_\alpha^{\pi/2}\left(s\sin t+c\frac{1+\cos^2t}{\sqrt{2+\cos^2t}}\right)dt
=\frac{4\sqrt3}{3\pi}+\frac2\pi J,
\tag{4}
\]
where
\[
J=\int_0^\theta\frac{1+\sin^2t}{\sqrt{2+\sin^2t}}\,dt.
\]
The elementary identity \((1+z)/\sqrt{2+z}=\sqrt{2+z}-(2+z)^{-1/2}\) gives
\[
J=\frac{2E(\theta\mid-1/2)-F(\theta\mid-1/2)}{\sqrt2},
\]
which proves the closed form. Since a uniformly oriented face has expected absolute normal component \(1/2\), (1) gives \(\mathbb EA=\sqrt3/4\). The expected contribution of one unit edge to (2) is \(\theta/2\): integrating \(\sin^2\varphi\) over the angular sectors of total width \(4\theta\), divided by \(4\pi\), gives \(\theta/2\). Hence \(\mathbb EP=3\theta\).

It remains to prove the strict covariance sign without relying on floating-point approximations. Define \(S_n=\int_0^\theta\sin^{2n}t\,dt\). Direct integration by parts and \(\sin^2\theta=2/3\), \(\sin\theta\cos\theta=\sqrt2/3\) yield
\[
S_0=\theta,\qquad S_n=\frac{2n-1}{2n}S_{n-1}-\frac{\sqrt2}{6n}(2/3)^{n-1}\quad(n\ge1).
\tag{5}
\]
Expanding \((1+z)^{-1/2}\) with \(z=\sin^2t/2\in[0,1/3]\), its alternating remainder after order \(14\) has magnitude at most \(z^{15}\). Thus
\[
\left|J-\frac1{\sqrt2}\sum_{n=0}^{14}\frac{(-1)^n}{8^n}{2n\choose n}(S_n+S_{n+1})\right|\le\frac5{3^{16}}.
\tag{6}
\]
The accompanying `verify.py` computes *outward rational interval* bounds for the quantities in (5)–(6): rational square-root enclosures via integer square roots, \(\pi=16\arctan(1/5)-4\arctan(1/239)\) by alternating Taylor sums, and \(\theta=\pi/4+\arctan(3-2\sqrt2)\) by the same method. It proves the stronger exact inequalities
\[
-0.0004<\frac{4\sqrt3}{3\pi}+\frac{2J}{\pi}-\frac{3\sqrt3\theta}{4}<-0.0003.
\]
Every interval operation is on exact rational endpoints. Numerical decimal output merely displays approximations to those rational certificates. This completes the sign proof.

## Verification
Run `python3 verify.py` using Python 3's standard library. The executable certificate implements (5)–(6) using `fractions.Fraction` and asserts strict rational bounds for the covariance. Separately it projects the four vertices onto 400 independent test planes, forms a planar convex hull, and compares its area and perimeter with (1)–(2); observed maximal discrepancies are below \(3\times10^{-16}\) and \(5\times10^{-15}\), respectively. A 200,000-point midpoint quadrature independently checks (4), but is not used to certify an exact identity or the covariance sign.

## Relationship to prior work
Finch, *Planar Projections and Second Intrinsic Volume* (arXiv:1203.2464v1, first publicly submitted 2012-03-12), §2.1, reports the same mixed moment numerically near \(1.2406348222\) and a negative numerical correlation, and explicitly notes the absence of a closed form for the mixed area–perimeter moment. This theorem supplies an incomplete-elliptic-integral evaluation and a rationally certified negative covariance; it does **not** claim discovery of the numerical value or negativity as an empirical observation. Dirksen, *Sections of the Regular Simplex—Volume Formulas and Estimates* (arXiv:1509.06408), studies linear sections and section volumes rather than this random projection's mixed area–perimeter moment. Searches for mixed tetrahedral shadow moments, equivalent elliptic forms, and stronger coverage found no known formula implying the displayed identity. This is evidence of a specific gap, not a proof that no earlier equivalent expression exists.

## Limitations
The elliptic expression is not an elementary closed form, and no exact closed form for the entire joint distribution or for higher mixed moments is established. Originality may be limited by earlier equivalent integrals hidden under other projection or stochastic-geometry terminology. The deterministic proof uses tetrahedral symmetry and does not extend automatically to arbitrary simplices. The rational sign enclosure proves only the stated strict bounds; the longer displayed decimal is numerical, not an exact rational evaluation. Independent external audit has not been performed.

## References
1. S. R. Finch, “Planar Projections and Second Intrinsic Volume,” arXiv:1203.2464v1 (2012), §2.1 and §5; https://arxiv.org/abs/1203.2464.
2. H. Dirksen, “Sections of the Regular Simplex—Volume Formulas and Estimates,” arXiv:1509.06408 (2015); https://arxiv.org/abs/1509.06408.
