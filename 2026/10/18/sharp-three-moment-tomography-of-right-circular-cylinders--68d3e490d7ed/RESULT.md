# Sharp three-moment tomography of right circular cylinders

## Finding
Let \(C_{d,h}\subset\mathbb R^3\) be a solid right circular cylinder of base diameter \(d>0\), height \(h>0\), and arbitrary position and axis orientation. For \(U\) uniform on \(S^2\), let \(W=w_{C_{d,h}}(U)\) be its (unoriented) projected length in direction \(U\), and put \(m_k=\mathbb E[W^k]\).

**Sharp moment cutoff.** The three real numbers \((m_1,m_2,m_3)\) uniquely determine the ordered geometric parameters \((d,h)\), for every \(d,h>0\); the first two moments do not determine them, even locally on a nonempty open family of aspect ratios. Reconstruction uses one quadratic equation followed by a strict third-moment selection rule. The inverse map is Lipschitz on every compact positive parameter rectangle. Thus the minimal universal number of initial scalar width moments for this family is exactly three.

## Assumptions and scope
The cylinder is the Minkowski sum of a radius-\(d/2\) Euclidean disk in a plane orthogonal to its axis and a segment of length \(h\) parallel to its axis. Its surface need not be smooth at the two rim circles. No directional labels, repeated samples, volume, or prior normalization are required: only exact expectations with respect to uniform orientation. The conclusion reconstructs height and diameter, not spatial position or axis orientation, which width laws cannot distinguish.

## Proof
Write \(T=|U\cdot e|\), where \(e\) is a unit cylinder-axis vector. Spherical uniformity gives \(T\sim\mathrm{Unif}[0,1]\), and Minkowski additivity of support functions yields
\[
W=d\sqrt{1-T^2}+hT.
\]
Consequently direct integration gives
\[
\begin{aligned}
m_1&=\frac\pi4d+\frac12h,\\
m_2&=\frac13(2d^2+2dh+h^2),\\
m_3&=\frac{3\pi}{16}d^3+\frac34d^2h+\frac{3\pi}{16}dh^2+\frac14h^3.
\end{aligned}
\]

Fix \(m=m_1>0\). Then \(h=2m-\pi d/2\) and
\[
m_2=\frac{\pi^2-4\pi+8}{12}d^2+\frac{4-2\pi}{3}md+\frac43m^2.
\]
Thus there are at most two possible values of \(d\). If distinct, their sum is
\[
P=\frac{8m(\pi-2)}{\pi^2-4\pi+8},
\]
so the second candidate is \(P-d\). Let \(G_m(x)\) denote the cubic expression for \(m_3\) after replacing \(h\) by \(2m-\pi x/2\). Polynomial division gives
\[
\frac{G_m(x)-G_m(P-x)}{2x-P}=c_2x^2+c_1x+c_0,
\]
where
\[
\begin{aligned}
c_2&=\frac{\pi(\pi^2-12)}{64},\\
c_1&=-\frac{m\pi(\pi-2)(\pi^2-12)}{8(\pi^2-4\pi+8)},\\
c_0&=\frac{m^2(\pi^5+8\pi^4-80\pi^3+96\pi^2+384\pi-768)}{4(\pi^2-4\pi+8)^2}.
\end{aligned}
\]
The discriminant of the quadratic on the right is
\[
\Delta=-\frac{3m^2\pi(\pi^2-12)}{16(\pi^2-4\pi+8)^2}\,Q(\pi),
\quad Q(z)=z^4-6z^3+4z^2+36z-64.
\]
Indeed, \(Q''(z)=12z(z-3)+8>0\) for \(z\ge3\), while \(Q'(3)=6>0\); therefore \(Q\) is strictly increasing there. The classical rational bounds \(3<\pi<22/7\) and the exact identity \(Q(22/7)=-104/2401\) imply \(Q(\pi)<0\). They also give \(\pi^2<12\). Hence \(c_2<0\) and \(\Delta<0\), so the quotient quadratic is strictly negative for every real \(x\) and \(m>0\). Distinct candidates for \(d\) consequently have distinct third moments. This proves reconstruction by \((m_1,m_2,m_3)\).

To show optimality, set \(\lambda=h/d>0\). Eliminating overall scale produces
\[
R(\lambda)=\frac{m_2}{m_1^2}=\frac{16(\lambda^2+2\lambda+2)}{3(\pi+2\lambda)^2},
\quad
R'(\lambda)=\frac{32((\pi-2)\lambda+\pi-4)}{3(\pi+2\lambda)^3}.
\]
This ratio decreases strictly until \(\lambda_*=(4-\pi)/(\pi-2)>0\), then increases strictly. Moreover \(\lim_{\lambda\to\infty}R(\lambda)=4/3>32/(3\pi^2)=R(0)\). Every value in \((R(\lambda_*),R(0))\) therefore has two distinct positive aspect-ratio preimages. Scaling both cylinders to a common first moment gives equal first and second moments. Thus no two-moment universal reconstruction theorem is possible.

For stability, the analytic parameter map \((d,h)\mapsto(m_1,m_2,m_3)\) is injective. It is an immersion: on a constant-\(m_1\) line, the derivative of \(m_2\) vanishes only at \(d=P/2\), while there the derivative of \(m_3\) equals the strictly negative quotient quadratic evaluated at \(P/2\). An injective \(C^1\) immersion on a compact positive parameter rectangle has a Lipschitz inverse onto its image, by the uniform local derivative bound and compact separation of non-neighboring pairs.

## Verification
The standalone `verify.py` re-derives the quadratic root sum, third-moment divided-difference coefficients, negative-discriminant factorization, and rational sign certificate symbolically. It independently compares the first three formulas with high-precision numerical quadrature for 25 positive cylinders, and exhibits a positive two-moment collision with distinct third moments. Run `python verify.py` with Python 3, SymPy and mpmath. Symbolic identity checks are supplementary: the preceding algebra, sign estimates and inverse-function argument are the proof for all positive cylinders.

## Relationship to prior work
Abas, *Width Laws and Spectral Geometry* (2026), Section 7.4, Proposition 7.4, derives the full random-direction width density of every right circular cylinder and proves identification from the entire width distribution. Its finite moment reconstruction theorem concerns orthotopes, not the sharp cylinder moment cutoff. The present result uses the established cylinder width representation but adds exact three-moment sufficiency, two-moment nonuniqueness, and stability of this finite-data inverse. The later study *Random Width and Brightness: Polyhedral Density Theory, Reconstruction, and Gaussian Identifiability* (2026) develops related distributional and labelled-moment reconstruction, chiefly for polytopes and finite direction systems. No claim is made that the cylinder width representation, its full density, or general spherical moment integration is new.

## Limitations
Reconstruction assumes exact raw orientation-averaged moments and a priori membership in the two-parameter right circular-cylinder family. It does not give a noise-independent uniform inverse bound as \(d\to0\), \(h\to0\), or the parameters become unbounded. A complete historical priority check of the full later 2026 manuscript was unavailable; equivalently phrased earlier finite-moment results may exist. The exact stability constants on compact parameter domains are not optimized.

## References
1. Omri Abas, *Width Laws and Spectral Geometry: Universality, Geometric Memory, and Reconstruction*, arXiv:2608.06348 (first public August 6, 2026), especially Proposition 7.4 and Theorem 3.5. https://arxiv.org/pdf/2608.06348
2. Omri Abas, *Random Width and Brightness: Polyhedral Density Theory, Reconstruction, and Gaussian Identifiability*, arXiv:2609.26202 (initial posting August 10, 2026), abstract and accessible public bibliographic record. https://arxiv.org/abs/2609.26202
