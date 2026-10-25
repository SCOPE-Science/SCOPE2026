# Exact non-Gaussian isoperimetric deficit of random equilateral zonogons

## Finding

For each integer \(n\ge2\), take independent angles \(\Theta_1,\ldots,\Theta_n\) uniformly distributed on \([0,\pi)\), and let \(u_j=(\cos\Theta_j,\sin\Theta_j)\). Form the centered equilateral zonogon
\[
Z_n=\sum_{j=1}^n[-u_j/2,u_j/2],\qquad A_n=\operatorname{Area}(Z_n).
\]
Its perimeter is deterministically \(P(Z_n)=2n\). The circle of that perimeter has area \(n^2/\pi\). Thus the normalized isoperimetric deficit
\[
D_n=\frac{P(Z_n)^2/(4\pi)-A_n}{n}=\frac{n^2/\pi-A_n}{n}
\]
is nonnegative. The following statements hold.

1. **Exact spectral identity, for every configuration of angles:** writing \(S_{n,k}=\sum_{j=1}^ne^{2ik\Theta_j}\),
\[
\boxed{D_n=\frac{2}{\pi n}\sum_{k=1}^{\infty}\frac{|S_{n,k}|^2}{4k^2-1}.}
\]
The series converges absolutely. This is a deterministic, nonnegative sum-of-squares certificate for the isoperimetric deficit of every unit-segment planar zonogon.

2. **Exact finite-sample moments:**
\[
\boxed{\mathbb E D_n=\frac1\pi,\qquad
\operatorname{Var}(D_n)=\frac{n-1}{2n}\left(\frac12-\frac4{\pi^2}\right).}
\]
Equivalently, \(\mathbb EA_n=n(n-1)/\pi\) and \(\operatorname{Var}(A_n)=\binom n2(1/2-4/\pi^2)\).

3. **Non-Gaussian fluctuation law:** if \(E_1,E_2,\ldots\) are independent exponential random variables of rate one, then
\[
\boxed{D_n\ \Longrightarrow\ T=\frac2\pi\sum_{k=1}^{\infty}\frac{E_k}{4k^2-1}.}
\]
The limit exists almost surely, is nondegenerate, and has \(\mathbb ET=1/\pi\) and \(\operatorname{Var}(T)=1/4-2/\pi^2\). Its complete Laplace transform, for real \(s\ge0\), is
\[
\boxed{
\mathbb E e^{-sT}=
\begin{cases}
\displaystyle\frac{\sqrt{1-2s/\pi}}{\sin((\pi/2)\sqrt{1-2s/\pi})},&0\le s<\pi/2,\\[8pt]
2/\pi,&s=\pi/2,\\[5pt]
\displaystyle\frac{\sqrt{2s/\pi-1}}{\sinh((\pi/2)\sqrt{2s/\pi-1})},&s>\pi/2.
\end{cases}}
\]
The upper tail is exponentially sharp, including its explicit prefactor:
\[
\boxed{\mathbb P(T>t)\sim\frac{16}{3\pi}e^{-3\pi t/2}\quad(t\to\infty).}
\]
In particular, the deficit from the perimeter-matched disk has nonvanishing, **non-Gaussian** fluctuations at order \(n\), although the area itself is of order \(n^2\).

## Assumptions and scope

Areas use two-dimensional Lebesgue measure. Minkowski sums and Euclidean perimeters have their ordinary definitions. Directions are independent and uniformly distributed modulo \(\pi\), and every generating segment has length exactly one. The deterministic identity holds even when some angles coincide; probabilistic claims use the independent uniform-angle law. The result concerns the fixed-dimensional planar limit \(n\to\infty\), not higher-dimensional random zonotopes, nonuniform directions, or random segment lengths. The limiting law is asserted in distribution; no coupling-dependent \(L^2\) convergence is asserted.

## Proof

**Step 1: area, perimeter, and the Fourier certificate.** The standard two-dimensional zonotope determinant formula gives
\[
A_n=\sum_{1\le i<j\le n}|\det(u_i,u_j)|=\sum_{i<j}|\sin(\Theta_i-\Theta_j)|.
\]
Planar perimeter is additive under Minkowski addition, so the sum of \(n\) unit segments has perimeter \(2n\) whenever the sum is two-dimensional (almost surely under the angle law). The same perimeter identity follows by the support-function/Cauchy formula for arbitrary configurations, interpreted as a limit if a sum is degenerate. The uniformly absolutely convergent trigonometric series
\[
|\sin t|=\frac2\pi-\frac4\pi\sum_{k=1}^{\infty}\frac{\cos(2kt)}{4k^2-1}
\]
and the elementary identity
\[
2\sum_{i<j}\cos(2k(\Theta_i-\Theta_j))=|S_{n,k}|^2-n
\]
imply, using \(\sum_{k\ge1}(4k^2-1)^{-1}=1/2\),
\[
A_n=\frac{n^2}{\pi}-\frac2\pi\sum_{k\ge1}\frac{|S_{n,k}|^2}{4k^2-1}.
\]
Every summand is nonnegative and bounded by \(n^2/(4k^2-1)\); hence the series is absolutely convergent and the first claim follows.

**Step 2: finite-sample mean and variance.** For independent uniform angles, \(\mathbb E|\sin(\Theta_i-\Theta_j)|=2/\pi\) and \(\mathbb E|\sin(\Theta_i-\Theta_j)|^2=1/2\). Pair terms with disjoint indices are independent. For distinct \(i,j,k\), conditional on \(\Theta_i\), both \(|\sin(\Theta_i-\Theta_j)|\) and \(|\sin(\Theta_i-\Theta_k)|\) are independent with the *constant* conditional mean \(2/\pi\); hence their covariance is zero. Counting pairs proves the exact area moments. Dividing the area variance by \(n^2\) proves the deficit variance; its mean is \(1/\pi\).

**Step 3: distributional limit and control of infinitely many modes.** For any fixed positive integer \(K\), the vector
\[
\left(n^{-1/2}S_{n,1},\ldots,n^{-1/2}S_{n,K}\right)
\]
converges by the multivariate real central limit theorem to \(K\) independent standard complex normal variables (real and imaginary components each have variance \(1/2\)). Indeed, the real Fourier modes at distinct positive frequencies are mutually orthogonal and their pseudo-covariances vanish under the uniform angle law. Squared moduli of these normals are independent rate-one exponentials. Thus the first \(K\) summands of the spectral certificate converge jointly to the corresponding truncated exponential series.

Moreover, for every \(n\) and \(k\ge1\), \(\mathbb E|S_{n,k}|^2=n\). Uniformly in \(n\), the expected positive Fourier tail is therefore exactly
\[
\mathbb E\left[\frac2{\pi n}\sum_{k>K}\frac{|S_{n,k}|^2}{4k^2-1}\right]
=\frac2\pi\sum_{k>K}\frac1{4k^2-1}\longrightarrow0.
\]
The same summable bound controls the exponential-series tail. The converging-together argument proves the stated convergence in distribution. By the finite-sample variance formula and the explicit limit variance, second moments also converge; this is *moment convergence*, not an unqualified assertion of \(L^2\) convergence on a shared probability space.

**Step 4: exact Laplace transform.** Set \(c_k=2/[\pi(4k^2-1)]\). Independence yields
\[
\mathbb E e^{-sT}=\prod_{k\ge1}(1+sc_k)^{-1}.
\]
Euler's product \(\sin(\pi z)/(\pi z)=\prod_{k\ge1}(1-z^2/k^2)\), with \(z^2=(1-2s/\pi)/4\), evaluates this product. When \(s>\pi/2\), the sine becomes an imaginary hyperbolic sine; continuity gives the middle value \(2/\pi\). Differentiation at zero or summation of \(c_k\) and \(c_k^2\) proves the stated moments. Explicitly, \(\sum_{k\ge1}(4k^2-1)^{-2}=(\pi^2-8)/16\).

**Step 5: sharp positive tail.** Write \(T=c_1E_1+R\), where \(c_1=2/(3\pi)\) and \(R=\sum_{k\ge2}c_kE_k\) is independent of \(E_1\). Since \(c_2<c_1\), there exists \(\varepsilon>0\) with \(\mathbb E\exp((c_1^{-1}+\varepsilon)R)<\infty\). Conditioning on \(R\) and applying dominated convergence give
\[
\lim_{t\to\infty}e^{t/c_1}\mathbb P(T>t)=\mathbb E e^{R/c_1}
=\prod_{k=2}^\infty\left(1-\frac3{4k^2-1}\right)^{-1}.
\]
The product telescopes by
\[
\prod_{k=2}^\infty\left(1-\frac3{4k^2-1}\right)
=\frac{\prod_{k=2}^\infty(1-k^{-2})}{\prod_{k=2}^\infty(1-(2k)^{-2})}
=\frac{1/2}{8/(3\pi)}=\frac{3\pi}{16}.
\]
Hence the tail prefactor is \(16/(3\pi)\), completing the proof.

## Verification

Run `python3 verify.py` from this directory. The standalone standard-library checker tests the geometric area formula against the exact Fourier identity at several explicit and seeded random angular configurations, checks the rigorous tail error bound for truncated Fourier series, checks the Euler-product Laplace formula on both sides of its removable branch point, checks the tail-prefactor product, and compares sampled finite-sample moments with their derived formulas. Printed finite tests are corroboration; the proof above establishes all dimensions and the infinite limit.

## Relationship to prior work

Joós and Lángi, *Isoperimetric problems for zonotopes* (first public preprint 7 June 2022, arXiv:2206.03204), provide the geometric framework, determinant/intrinsic-volume formulas, and deterministic extremal isoperimetric questions for zonotopes. These are premises, not new contributions here. Their full text addresses extremal and asymptotic deterministic inequalities, not the distribution of the deficit under independent unit-direction sampling.

Schneider, *Random zonotopes and valuations* (arXiv:2202.06774, 2022), studies expectations of intrinsic volumes of sums of i.i.d. random segments and a Gaussian central limit theorem under a positive first Hoeffding projection. For the present fixed-length uniform-angle model that projection is identically constant: \(\mathbb E[|\sin(\theta-\Theta)|]=2/\pi\) for every \(\theta\). Consequently the assumptions of Schneider's nondegenerate Gaussian theorem do not hold here; the explicitly computed second-order non-Gaussian law fills a distinct regime. Classical degenerate \(U\)-statistic theory supplies general second-chaos limits, but not without further spectral calculation the concrete geometric distribution, elementary Laplace formula, or sharp tail prefactor.

Buffière and Marchal, *Fluctuations of lattice zonotopes and polygons* (arXiv:2303.18045, 2023), analyze a different **lattice-constrained** random-zonotope ensemble and Gaussian boundary-point fluctuations. Rahmani, Pinoli, and Debayle, *Description of the symmetric convex random closed sets as zonotopes from their Feret diameters* (2017), study random convex-set descriptions with fixed chosen directions rather than i.i.d. uniform directions of unit segments. Published-result comparisons did not identify an exact implication covering this claim, but absence from searchable material does not establish uniqueness.

## Limitations

The random-segment directions must be independent and Haar-uniform modulo \(\pi\), and generator lengths must be exactly one. Random-radius models generally have nonzero first-order projections and different fluctuation scales. The limiting exponential series is not claimed to be the law for finite \(n\). The finite-sample numerical checker cannot establish an infinite-series identity or the weak limit by itself; those assertions rely on the stated analytic arguments. The bibliographic comparison is necessarily incomplete, especially for older or less-indexed treatments of degenerate circular \(U\)-statistics, and independent external mathematical validation has not been performed.

## References

1. A. Joós and Z. Lángi, *Isoperimetric problems for zonotopes*, arXiv:2206.03204v1 (public 2022-06-07); complete accessible version arXiv:2206.03204v2 (2023). https://arxiv.org/abs/2206.03204 ; https://arxiv.org/html/2206.03204v2 .
2. R. Schneider, *Random zonotopes and valuations*, arXiv:2202.06774v1 (2022). https://arxiv.org/abs/2202.06774 .
3. T. Buffière and P. Marchal, *Fluctuations of lattice zonotopes and polygons*, arXiv:2303.18045v1 (2023). https://arxiv.org/html/2303.18045v1 .
4. S. Rahmani, J.-C. Pinoli, and J. Debayle, *Description of the symmetric convex random closed sets as zonotopes from their Feret diameters*, Modern Stochastics: Theory and Applications 3 (2016), 325–364; online 2017-01-03. https://www.vmsta.org/journal/VMSTA/article/78/text .
5. Standard Fourier series for absolute sine, Euler sine product, multivariate central limit theorem, and classical degenerate \(U\)-statistic convergence; all special-case computations used in the theorem are displayed above.
