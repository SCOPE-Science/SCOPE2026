# Sharp finite-moment tomography of ellipsoids from invariant random chords

## Finding

Fix an integer \(d\ge2\). Let \(E\subset\mathbb R^d\) be any nondegenerate Euclidean ellipsoid with positive semiaxis lengths \(a_1,\ldots,a_d\). Choose an **unoriented affine line** according to Euclidean-motion-invariant line measure, conditioned on its intersecting \(E\) (equivalently, choose its direction uniformly on the sphere and its orthogonal offset by Lebesgue measure, then condition on intersection). Let \(L\) be the length of its intersection with \(E\).

**Theorem.** The following exactly \(d\) unlabelled chord-length moments determine the entire multiset of semiaxis lengths, including its absolute scale:
\[
\mathbb E L^{d+1},\quad \mathbb E L^{d+3},\quad\ldots,\quad \mathbb E L^{3d-1}.
\]
A constructive inversion consists of recovering the first \(d-1\) elementary symmetric functions of the squared semiaxes by a truncated power-series inverse, determining their product from one strictly monotone scalar integral, and taking roots of the resulting polynomial. No equal-axis or genericity assumption is required. The number \(d\) is minimal for any **continuous** real-valued measurement scheme that identifies every ellipsoid's \(d\) unordered positive semiaxes, because distinct ordered axes form an open \(d\)-dimensional parameter domain.

## Assumptions and scope

The sampling measure is the invariant measure on affine **lines**, not the law of chords joining two independent boundary points and not the law obtained by conditioning a uniformly sampled interior point. Translating or rotating the ellipsoid does not change the distribution; accordingly, only the unordered semiaxes can be recovered. For a spherical ellipsoid all formulas remain valid. Every moment above exists because \(L\) is bounded. The result makes no claim of recovery of the spatial center or orientation from direction-unlabelled data, of statistical optimality under noisy finite sampling, or of a smaller-order moment cutoff within restricted families.

Set \(b_i=a_i^2>0\), \(B=\operatorname{diag}(b_1,\ldots,b_d)\), \(Q=B^{-1}\), and \(A(u)=u^TQu\) for \(u\in S^{d-1}\). Denote normalized surface average by \(\langle\cdot\rangle\). For real \(s\ge0\), put
\[
 c_{d,s}=2^s\frac{\Gamma((d+1)/2)\Gamma(1+s/2)}{\Gamma((d+1+s)/2)},\qquad
 T_k=\frac{\mathbb E L^{d+1+2k}}{c_{d,d+1+2k}}\quad(0\le k\le d-1).
\]

## Proof

**1. Conditional line geometry.** For fixed unit direction \(u\), write the line as \(p+\mathbb Ru\) with \(p\in u^\perp\). Completing the square in \((p+tu)^TQ(p+tu)\) gives
\[
 L(p,u)=\frac2{\sqrt{A(u)}}\sqrt{1-p^T\Bigl(Q-\frac{Quu^TQ}{A(u)}\Bigr)p}.
\]
The expression under the last square root is nonnegative precisely for offsets in the projection of \(E\) onto \(u^\perp\). This projection has \((d-1)\)-volume
\[
 \kappa_{d-1}\Bigl(\prod_i a_i\Bigr)\sqrt{A(u)}.
\]
(For instance, the restriction of the Schur complement displayed above has determinant \((\det Q)/A(u)\).) Thus, after conditioning on intersection, the direction density is proportional to \(\sqrt{A(u)}\). For that direction, a uniform projected offset becomes a uniform \(q\) in the unit \((d-1)\)-ball after an invertible linear map, and
\[
 L=\frac2{\sqrt{A(u)}}\sqrt{1-\|q\|^2}.
\]
Beta integration over this ball yields, for all \(s\ge0\),
\[
 \boxed{\mathbb E L^s=c_{d,s}\frac{\langle A^{(1-s)/2}\rangle}{\langle A^{1/2}\rangle}.}\tag{1}
\]
The projected-offset and angular normalizations cancel in this ratio, so no unstated line-measure constant remains.

**2. Recover all but the final symmetric coefficient.** Gaussian integration in polar coordinates proves, for every positive definite \(M\),
\[
 \langle(u^TMu)^{-d/2}\rangle=(\det M)^{-1/2}.
\]
Apply this to \(M=Q-tI\) for \(0\le t<\min_i b_i^{-1}\), and use (1). With \(x=\prod_i b_i\),
\[
 \langle(A-t)^{-d/2}\rangle
 =\sqrt{x}\prod_{i=1}^d(1-b_it)^{-1/2}.
\]
The coefficient of \(t^k\) on the left is \((d/2)_k\langle A^{-d/2-k}\rangle/k!\). Consequently, if \(H(t)=\sum_{k\ge0}h_kt^k\), then
\[
 h_k=\frac{(d/2)_k}{k!}\frac{T_k}{T_0},\qquad
 H(t)=\prod_{i=1}^d(1-b_it)^{-1/2}.
\]
Only the measured \(T_0,\ldots,T_{d-1}\) are needed to obtain \(H\) modulo \(t^d\). Formally invert its square:
\[
 \biggl(1+\sum_{k=1}^{d-1}h_kt^k\biggr)^{-2}
 \equiv1-e_1t+e_2t^2-\cdots+(-1)^{d-1}e_{d-1}t^{d-1}\pmod{t^d}.
\]
Here \(e_j\) is the \(j\)th elementary symmetric polynomial in \(b_1,\ldots,b_d\). The only missing coefficient is \(x=e_d\).

**3. The last coefficient is strictly identifiable.** Define the known polynomial
\[
 P_0(y)=y^d+e_1y^{d-1}+\cdots+e_{d-1}y,
\]
so \(\prod_i(y+b_i)=P_0(y)+x\). Put \(R=\langle A^{1/2}\rangle\) and \(c_d=\mathbb E\|Z\|=\sqrt2\Gamma((d+1)/2)/\Gamma(d/2)\) for \(Z\) a standard Gaussian vector in \(\mathbb R^d\). The Gaussian radial decomposition and the elementary Laplace representation of the square root give
\[
 \frac{R}{\sqrt{x}}
 =\frac{1}{\sqrt{2\pi}\,c_d}\int_0^\infty
 \left(x^{-1/2}-(x+P_0(y))^{-1/2}\right)y^{-3/2}\,dy.
\]
Integration by parts (both endpoint terms vanish) transforms this into
\[
 \boxed{\frac{R}{\sqrt{x}}=
 \frac{1}{\sqrt{2\pi}\,c_d}\,J(x),\quad
 J(x)=\int_0^\infty\frac{P_0'(y)}{\sqrt{y}\,[x+P_0(y)]^{3/2}}\,dy.}\tag{2}
\]
Every \(e_j>0\); hence \(P_0(y)>0\) and \(P_0'(y)>0\) for \(y>0\). The integral converges at zero because its integrand is \(O(y^{-1/2})\), and at infinity because it is \(O(y^{-(d+3)/2})\). Differentiation under the integral sign gives
\[
 J'(x)=-\frac32\int_0^\infty
 \frac{P_0'(y)}{\sqrt y\,[x+P_0(y)]^{5/2}}\,dy<0
 \qquad(x>0).
\]
By step 2 and (1), \(T_0=\langle A^{-d/2}\rangle/R=\sqrt{x}/R\). Hence
\[
 \boxed{T_0=\frac{\sqrt{2\pi}\,c_d}{J(x)}}.\tag{3}
\]
For the already recovered coefficients \(e_1,\ldots,e_{d-1}\), (3) determines exactly one positive \(x\); it is strictly increasing as a function of \(x\). Existence is guaranteed by the observed ellipsoid. The squared semiaxes now are the positive roots, with multiplicity, of
\[
 z^d-e_1z^{d-1}+e_2z^{d-2}-\cdots+(-1)^d x=0.
\]
Taking positive square roots completes constructive identification.

**4. Minimal measurement count.** The region \(a_1>\cdots>a_d>0\) is open in \(\mathbb R^d\). A map from it into \(\mathbb R^m\) consisting of \(m<d\) continuously varying real statistics cannot be injective: otherwise compose it with the coordinate embedding into \(\mathbb R^d\); invariance of domain would force its image to have nonempty interior although it lies in a lower-dimensional coordinate subspace. Every fixed finite chord moment is continuous in the axes by (1) and compactness on positive-parameter neighborhoods. Therefore \(d\) is a globally minimal number of such continuous scalar measurements. \(\square\)

## Verification

The bundled standalone \(verify.py\) uses exact rational arithmetic to recover the truncated polynomial in dimensions \(2\), \(3\), and \(4\), including repeated semiaxes. It evaluates the monotone integral independently by transformed Simpson quadrature and bisection and performs an independent \(64\)-node Gauss–Legendre by \(192\)-angle quadrature of the original spherical moment integrals in dimension \(3\). For squared axes \((1,4,9)\), the predicted coefficients are \((1,-14,49)\), and the independent angular ratios agree to less than \(3\times10^{-14}\) relative error. This numerical verification is not a substitute for the general proof. Run \(\texttt{python verify.py}\) with Python \(3.10\) or later; only the standard library is used.

## Relationship to prior work

Invariant-line chord length laws and their different randomization conventions have a substantial classical literature. N. Suwa (1977) considers test-line sampling of ellipsoidal particle populations. A. M. Kellerer (1984), particularly its discussion of isotropic-uniform randomness and its spheroid formulas, derives forward chord distributions for prolate and oblate spheroids; their full distributions determine moment sequences when the semiaxes are already specified. The present theorem addresses the opposite **finite-data inverse problem**, including every high-dimensional triaxial ellipsoid and repeated axes. It proves global injectivity of a specified set of exactly \(d\) line-chord moments by recovering all but one symmetric coefficient and strictly resolving the last through (2).

Related results on inverse moments of **central hyperplane-section volumes** reconstruct ellipsoid axes from a different sampling statistic. Their symmetric-polynomial technique has a structural resemblance to step 2, but does not provide the line-chord normalization, the strict last-coefficient inversion, or the present finite-moment statement. A separate earlier forward law for long random ellipsoid chords determines tail behavior, not the finite inverse identification here.

## Limitations

The result proves identifiability from exact population moments, not a noise-robust estimation method. Inverting polynomial roots near repeated semiaxes can be ill-conditioned, and the selected moment orders increase with dimension. Historical priority has not been independently audited: in particular, other stereological inversion literature or complete text of adjacent prior results may contain an equivalent finite-moment statement. No mathematical claim of uniqueness is made for arbitrary convex bodies, and no directional labels are recovered.

## References

1. N. Suwa, “Estimation of the Distribution of Ellipsoids with Random Test Lines,” *Tohoku Journal of Experimental Medicine* **121** (1977), 365–370. DOI: 10.1620/tjem.121.365. Publicly available at https://www.jstage.jst.go.jp/article/tjem1920/121/4/121_4_365/_pdf/-char/en (J-STAGE availability dated November 28, 2008).
2. A. M. Kellerer, “Chord-Length Distributions and Related Quantities for Spheroids,” *Radiation Research* **98** (1984), 425–437. DOI: 10.2307/3576477. Lawfully hosted copy: https://epub.ub.uni-muenchen.de/8751/1/8751.pdf.
3. R. Schneider and W. Weil, *Stochastic and Integral Geometry*, Springer, 2008, DOI: 10.1007/978-3-540-78859-1 (general invariant line geometry).
