# Apex distance tails reconstruct every right regular pyramid

## Finding
Let \(S\) be the complete boundary, including the base, of a right regular Euclidean \(n\)-gonal pyramid with integer \(n\geq3\), base apothem \(a>0\), and positive height \(h>0\). Let \(v\) be its apex and \(X\) be uniformly distributed by surface area on \(S\). Set \(D=d_S(v,X)\), where \(d_S\) is intrinsic shortest-path distance. Write
\[
\alpha=\pi/n,\quad b=a\tan\alpha,\quad L=\sqrt{a^2+h^2},\quad C=a+L.
\]
Then \(D\) has maximum possible value \(C\), attained at exactly one surface point: the base center. As \(\varepsilon\downarrow0\),
\[
\Pr(D>C-\varepsilon)=\frac{\varepsilon^2}{aC}+
\frac{\tan^2(\pi/n)}{3aC^2}\varepsilon^3+O_{n,a,h}(\varepsilon^4).
\]
In particular, the leading coefficient is independent of the base's number of sides at fixed \(a,L\), whereas the next coefficient recovers that number. The endpoint \(C\) together with these two coefficients *uniquely determines* \(n,a,h\), and hence the pyramid up to Euclidean congruence. The exact second moment is
\[
\mathbb E D^2=\frac{L(L+a)}2+\frac{a^2\sec^2(\pi/n)}6.
\]
The full law is also specified below by one-dimensional elementary quadratures, not only by its tail.

## Assumptions and scope
The base is a regular convex \(n\)-gon centered at the vertical projection of the apex; every lateral face is an isosceles triangle. All distances are intrinsic to the *closed* surface, not Euclidean through the solid and not shortest paths restricted to the lateral surface alone. Surface area is the standard two-dimensional Hausdorff measure normalized to probability. The height is strictly positive; no planar-degeneration statement is asserted. Parameters \(n,a,h\) are unrestricted otherwise.

For the base plane, use origin at the center and outward unit edge normals \(\nu_j=(\cos(2\pi j/n),\sin(2\pi j/n))\), \(0\le j<n\). The base polygon is \(K=\{x:\langle x,\nu_j\rangle\le a\ \forall j\}\). Its circumradius is \(R=\sqrt{a^2+b^2}\), its area is \(nab\), and the total lateral area is \(nbL\), giving total area \(nbC\).

## Proof
**Exact apex distance field.** Define \(F\) on each lateral triangular face by ordinary straight-line distance from the apex in that face. On the base put
\[
F(x)=\min_{0\le j<n}|x-C\nu_j|.
\]
For \(x\) on edge \(j\) of the base, write \(x=a\nu_j+t\tau_j\) with \(|t|\le b\) and \(\tau_j\perp\nu_j\). Edge \(j\)'s virtual apex has distance \(\sqrt{L^2+t^2}\), which equals the length of the corresponding segment in its lateral face. By regular-polygon nearest-normal geometry, that virtual apex is a closest one at every point of its edge. Therefore the definitions of \(F\) match across every lateral/base seam; the lateral definitions also match along lateral edges. Each face restriction is 1-Lipschitz, so \(F\) is globally 1-Lipschitz for the intrinsic length metric. Since \(F(v)=0\), it follows that \(F(x)\le d_S(v,x)\) everywhere.

Conversely, each lateral point is joined to the apex by its straight face segment, attaining \(F\). For a base point \(x\ne0\), rotate coordinates so that its closest normal is \((1,0)\), and write \(x=(r\cos\theta,r\sin\theta)\), with \(|\theta|\le\alpha\) and \(0\le r\le a\sec\theta\). The segment from the unfolded virtual apex \((C,0)\) to \(x\) crosses the relevant edge's supporting line at tangential coordinate
\[
t_* =\frac{Lr\sin\theta}{C-r\cos\theta}.
\]
It meets the actual edge, because \(|t_*|\le a|\tan\theta|\le b\): indeed \(u=r\cos\theta\le a\) implies \(Lu/(C-u)\le a\). Folding this straight segment across the edge produces a surface path from the apex to \(x\) with length \(|x-C\nu_j|=F(x)\). The assertion also holds by continuity for the center and sector boundaries. Consequently \(d_S(v,x)=F(x)\) everywhere. On the base the formula becomes
\[
d_S(v,x)^2=C^2+r^2-2Cr\cos\theta
\quad\bigl(|\theta|\le\alpha,\ 0\le r\le a\sec\theta\bigr).
\]
The nonunique shortest paths within the base occur on its radial segments from the center to the vertices (the ordinary Euclidean Voronoi boundaries of the virtual apices); this explicitly identifies the nontrivial base portion of the cut locus.

**Unique farthest point.** On every lateral face, the maximum apex distance is the lateral-edge length \(S=\sqrt{L^2+b^2}\), attained at base vertices. The square of the base distance is convex as a function of \(r\) along every ray \(\theta\), so its maximum on that ray is at \(r=0\) or \(r=a\sec\theta\). On the latter boundary it is at most \(S\), whereas at the base center it equals \(C\). Since
\[
C^2-S^2=2aL+a^2-b^2\ge2a(L-a)>0,
\]
using \(\tan^2(\pi/n)\le3\) and \(L>a\), the unique maximum is the base center, of value \(C\).

**Upper-tail expansion.** For sufficiently small \(\varepsilon>0\), the superlevel set \(\{d_S(v,\cdot)>C-\varepsilon\}\) lies strictly inside the base near its center. In each angular sector its radial boundary is the smaller root
\[
\rho_\varepsilon(\theta)=C\cos\theta-
\sqrt{C^2\cos^2\theta-2C\varepsilon+\varepsilon^2}.
\]
Uniformly for \(|\theta|\le\alpha\),
\[
\rho_\varepsilon(\theta)=\varepsilon\sec\theta+
\frac{\varepsilon^2}{2C}(\sec^3\theta-\sec\theta)+O(\varepsilon^3).
\]
Integrating polar area across all \(n\) sectors yields
\[
\operatorname{Area}\{d_S(v,\cdot)>C-\varepsilon\}=
\frac n2\int_{-\alpha}^{\alpha}\rho_\varepsilon(\theta)^2\,d\theta
=n\tan\alpha\,\varepsilon^2+
\frac{n\tan^3\alpha}{3C}\varepsilon^3+O(\varepsilon^4).
\]
Division by the total surface area \(nbC=naC\tan\alpha\) proves the stated probability expansion.

**Inverse recovery.** Write \(k\) and \(q\) for the respective coefficients of \(\varepsilon^2\) and \(\varepsilon^3\) in this upper-tail expansion. From the *distribution alone*, its right endpoint gives \(C\), and then
\[
a=\frac1{kC},\qquad L=C-a,\qquad
n=\frac{\pi}{\arctan\sqrt{3aC^2q}},\qquad
h=\sqrt{L^2-a^2}.
\]
The square root and inverse tangent are taken nonnegative and principal, respectively. All parameters are therefore identified uniquely; there is no scale ambiguity when the distance distribution retains its physical units.

**Exact second moment.** In one lateral triangle, the mean squared apex distance is \(L^2/2+b^2/6\) by uniform barycentric-coordinate moments. In the base, \(\mathbb E|X|^2=a^2/2+b^2/6\) and \(\mathbb E\max_j\langle X,\nu_j\rangle=2a/3\), both from sector integration. Hence the base's mean squared apex distance is \(C^2+a^2/2+b^2/6-4aC/3\). Averaging these two conditional expectations with respective surface-area weights \(L/C\) and \(a/C\), then simplifying, gives \(L(L+a)/2+(a^2+b^2)/6\) as claimed.

**Complete distribution by one-dimensional quadrature.** Put \(\phi=\arctan(b/L)\). For \(t\ge0\), the area on a single lateral face lying within apex distance \(t\) is
\[
J(t)=\frac12\int_{-\phi}^{\phi}\min\{t^2,L^2\sec^2 u\}\,du.
\]
For each \(|\theta|\le\alpha\), if \(t<C|\sin\theta|\), set \(G(t,\theta)=0\). Otherwise let
\[
r_\pm(t,\theta)=C\cos\theta\pm\sqrt{t^2-C^2\sin^2\theta},
\]
\[
G(t,\theta)=\frac12\Bigl[\max\{0,\min(a\sec\theta,r_+)^2-
\max(0,r_-)^2\}\Bigr].
\]
Then the complete cumulative distribution is
\[
\Pr(D\le t)=\frac{J(t)+\displaystyle\int_{-\alpha}^{\alpha}G(t,\theta)\,d\theta}{bC}.
\]
This formula applies to all \(t\ge0\), including transition thresholds, and equals one for \(t\ge C\). It expresses a finite, exact real integral, not a claim that every branch admits a uniform elementary antiderivative.

## Verification
The standalone `check.py` independently integrates squared distances in the lateral and base sectors by high-order Gauss--Legendre quadrature for six side counts and four positive heights. It compares with the exact moment formula at absolute error below \(2\times10^{-12}\). A second set of 24 high-threshold quadratures checks the two-term tail expansion; 50,000 sector tests check nearest-image and edge-crossing geometric identities. All executed tests passed. They are numerical corroboration only; the infinite-parameter statements follow from the analytic proof above.

To reproduce from a directory containing `check.py`, execute `python check.py` with Python 3 and NumPy installed.

## Relationship to prior work
Miller and Pak's 2003 arXiv preprint develops the general source-image and Voronoi characterization of polyhedral cut loci (notably Theorem 2.9) and constructive unfolding algorithms. This supplies the established conceptual setting; it is not claimed as a new source-image principle. The present result derives a specific regular-pyramid virtual-source reduction, exact uniform-surface moment, a two-term maximal-distance tail, and an inverse-recovery formula for the entire regular-pyramid family. These quantitative consequences were not located in the inspected sections of the cited preprint. The 1987 discrete-geodesic algorithms of Mitchell, Mount and Papadimitriou are also older general background, not claimed as new.

## Limitations
The theorem excludes zero height, nonregular bases, off-axis apices, non-area-uniform sampling, and point sources other than the apex. The inverse formula uses the exact distribution and mathematically exact tail coefficients; no finite-sample statistical stability guarantee is claimed. A general source-unfolding algorithm does not by itself settle whether an earlier specialist author independently evaluated the identical pyramid-specific distribution or inverse tail. No independent scientific audit has been performed.

## References
1. E. Miller and I. Pak, *Metric combinatorics of convex polyhedra: cut loci and nonoverlapping unfoldings*, arXiv:math/0312253v1, publicly submitted 12 December 2003. https://arxiv.org/abs/math/0312253 . See especially Section 2 and Theorem 2.9.
2. J. S. B. Mitchell, D. M. Mount, and C. H. Papadimitriou, *The Discrete Geodesic Problem*, SIAM Journal on Computing 16 (1987), 647–668, DOI 10.1137/0216045. Cited as general algorithmic background; the full paper was not inspected in this assessment.
