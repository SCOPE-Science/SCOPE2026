# Exact signed linear-Laplace covariance interval on the geodesic circle

## Finding
Let \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\) have shortest-arc distance \(\vartheta(x,y)\in[0,\pi]\). For every \(a>0\) and real \(b\), the continuous kernel
\[
K_{a,b}(x,y)=e^{-a\vartheta(x,y)}\bigl(1+b\vartheta(x,y)\bigr)
\]
is positive semidefinite on every finite set of circle sites if and only if
\[
\boxed{-\frac{a(1-e^{-\pi a})}{1-(1+\pi a)e^{-\pi a}}\ \le b\le\ \frac{a(1-e^{-\pi a})}{1-(1-\pi a)e^{-\pi a}}.}
\]
Both denominators are strictly positive. Every kernel in this closed interval is *strictly* positive definite on each finite set of distinct sites. At the lower boundary the constant Fourier coefficient is zero and all nonconstant coefficients are positive; at the upper boundary every Fourier coefficient is positive, with an enhanced fourth-order decay along even modes. Below the lower boundary the constant mode is negative, while above the upper boundary all sufficiently high even Fourier modes are negative.

In particular the geodesic-distance Matérn-\(3/2\)-shaped kernel \(e^{-a\vartheta}(1+a\vartheta)\) fails positive definiteness for every finite \(a>0\). Its sharp admissible linear coefficient deficit is
\[
a-b_+(a)=\frac{\pi a^2e^{-\pi a}}{1-(1-\pi a)e^{-\pi a}}\sim\pi a^2e^{-\pi a}\quad(a\to\infty).
\]
The opposite boundary has \(b_-(a)\to-2/\pi\), whereas \(b_+(a)\sim a/2\), as \(a\downarrow0\).

## Assumptions and scope
All angles use radians and the circle circumference is \(2\pi\). The only parameter assumptions are \(a>0\) and \(b\in\mathbb R\). Positive semidefinite means every finite Hermitian Gram matrix of \(K_{a,b}\) is positive semidefinite, including repeated sites. Strict positive definiteness means positive quadratic form for every nonzero coefficient vector at pairwise distinct sites. The statement concerns the intrinsic shortest-arc metric, **not** the Euclidean chordal metric and not the periodization of the Euclidean Matérn function. No claim is made for higher-dimensional spheres.

## Proof
**1. Exact Fourier coefficients.** Put \(E=e^{-\pi a}\), let \(n\in\mathbb Z_{\ge0}\), and set \(s_n=(-1)^n\). For the real even profile \(k_{a,b}(t)=e^{-a|t|}(1+b|t|)\) on \([ -\pi,\pi]\), its complex Fourier coefficient is
\[
\widehat k_{a,b}(n)=\frac1\pi\int_0^\pi e^{-at}(1+bt)\cos(nt)\,dt.
\]
Elementary integration gives
\[
F_n(a)=\int_0^\pi e^{-at}\cos(nt)\,dt
=\frac{a(1-s_nE)}{a^2+n^2}>0.
\]
Differentiation under the integral sign, justified on the bounded interval, yields
\[
\widehat k_{a,b}(n)=\frac{F_n(a)-bF_n'(a)}\pi
=\frac{F_n(a)}\pi[1-bR_n(a)],
\quad
R_n(a)=\frac1a+\frac{s_n\pi E}{1-s_nE}-\frac{2a}{a^2+n^2}.
\]
The same coefficient occurs for the negative index. By Fourier positivity on compact abelian groups, \(K_{a,b}\) is positive semidefinite if and only if \(1-bR_n(a)\ge0\) for every \(n\ge0\).

**2. Exact extremal logarithmic derivatives.** For even indices, \(R_{2j}\) increases strictly with \(j\) and has limit
\[
R_+(a)=\frac1a+\frac{\pi E}{1-E}>0.
\]
For odd indices, \(R_{2j+1}\) likewise increases to \(1/a-\pi E/(1+E)\), which is strictly less than \(R_+(a)\). The least even value is \(R_0=-1/a+\pi E/(1-E)<0\), because \(e^{\pi a}>1+\pi a\). The least odd value exceeds \(R_0\), since
\[
R_1-R_0=\frac{2}{a(a^2+1)}-\frac{\pi}{\sinh(\pi a)}>0.
\]
Indeed, writing \(t=\pi a\), the elementary bound \(\sinh t\ge t+t^3/6\) gives
\[
2\sinh t-t(1+a^2)\ge t+t^3(1/3-1/\pi^2)>0.
\]
Consequently
\[
\inf_{n\ge0}R_n=R_0<0,\qquad
\sup_{n\ge0}R_n=R_+>0,
\]
where the supremum is not attained at a finite index. These two extrema turn all Fourier inequalities into
\[
\frac1{R_0}\le b\le\frac1{R_+}.
\]
Substitution yields exactly the interval in the Finding. The positive lower denominator follows from \(e^t>1+t\) for \(t>0\).

**3. Sharpness, boundary behavior and strictness.** When \(b<1/R_0\), the zero mode is strictly negative; when \(b>1/R_+\), the even-mode subsequence becomes negative for all sufficiently large even indices. At \(b=1/R_+\) the even Fourier coefficients have the explicit positive form
\[
\widehat k_{a,b}(2j)=\frac{2a^2b(1-E)}{\pi(a^2+4j^2)^2}>0
\]
for \(j\ge0\), while the odd coefficients are positive by the strict bound \(R_n<R_+\). At \(b=1/R_0\), exactly the zero mode vanishes; all other coefficients are positive by \(R_n>R_0\).

If all Fourier coefficients are strictly positive, a nonzero finitely supported signed measure gives a strictly positive Gram quadratic form by Fourier uniqueness. At the lower endpoint, a finite atomic measure annihilated by all nonzero modes would be proportional to Haar measure, which is impossible unless it is zero. Hence strict positive definiteness holds even there. Finally, the stated deficit and small-\(a\) limits follow by direct algebra and Taylor expansion.

## Verification
The companion `checker.py` uses Python's standard library. Run `python3 checker.py` next to this file. It independently approximates 120 Fourier integrals by composite Simpson quadrature, compares them with the analytic formula (observed maximum discrepancy \(5\times10^{-15}\)), checks boundary positivity for the first 100 modes, and detects negative finite circulant-Gram eigenvalues outside each boundary. Its finite checks are corroborative only: the infinite-mode statement is established by the inequalities in the proof. At \(a=1\), it obtains \(b_-\approx-1.165354814545474\) and \(b_+\approx0.875739371737745\).

## Relationship to prior work
The Fourier-coefficient characterization is classical. Gneiting's *Strictly and non-strictly positive definite functions on spheres* (arXiv:1111.7077, Theorem 1 and Example 2) gives the circle's Fourier criterion and the known failure of the standard geodesic Matérn family for smoothness above \(1/2\). It does not give these two sharp signed correction bounds or their different endpoint mechanisms. Feragen, Lauze and Hauberg (arXiv:1411.0296) discuss metric negative type and the uncorrected geodesic Laplacian, not the affine correction. Huang and Li (arXiv:2201.12856) instead develop a periodic spectral/SPDE circular Matérn covariance, a different kernel. This result explicitly solves the admissibility problem for the intrinsic affine-Laplace family, including the sharp near-Matérn deficit and both endpoints. A broader unindexed parametrization remains a novelty risk.

## Limitations
The classification applies to the one-dimensional unit circle and the specific affine correction only. It does not establish admissibility for higher-order polynomial corrections, for the ordinary higher-dimensional sphere, or for the periodically wrapped Euclidean Matérn kernel. The originality assessment is limited to the primary literature and research records inspected; it is not a proof of global uniqueness. Numerical testing does not certify infinite-frequency inequalities, which are addressed separately in the analytic proof.

## References
1. Tilmann Gneiting, *Strictly and non-strictly positive definite functions on spheres*, first arXiv version 2011-11-30, arXiv:1111.7077, https://arxiv.org/abs/1111.7077 (Theorem 1, Example 2).
2. Aasa Feragen, François Lauze, Søren Hauberg, *Geodesic Exponential Kernels: When Curvature and Linearity Conflict*, arXiv:1411.0296, first submitted 2014-11-02, https://arxiv.org/abs/1411.0296 (Theorem 4 and related discussion).
3. Chunfeng Huang and Ao Li, *The Circular Matérn Covariance Function and its Link to Markov Random Fields on the Circle*, arXiv:2201.12856, first submitted 2022-01-30, https://arxiv.org/abs/2201.12856 (Section 2).
4. I. J. Schoenberg, *Positive definite functions on spheres*, Duke Mathematical Journal **9** (1942), 96–108; underlying Fourier characterization is recalled in Reference 1.
