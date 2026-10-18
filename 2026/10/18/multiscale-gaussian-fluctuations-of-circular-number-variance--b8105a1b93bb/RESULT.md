# Multiscale Gaussian fluctuations of circular number variance

## Finding
Let \(U_1,\dots,U_N\) be independent uniform points on the unit circle. For a window of length \(s\in[0,1]\), write
\[
C_N(x,s)=\sum_{i=1}^N\mathbf1_{\{U_i\in(x,x+s]\bmod1\}},\qquad
V_N(s)=\int_0^1(C_N(x,s)-Ns)^2\,dx.
\]
The mean is exactly \(\mathbb E V_N(s)=Ns(1-s)\). For any \(s,t\in[0,1]\), put \(a=\min\{s,1-s\}\), \(b=\min\{t,1-t\}\), \(u=\min\{a,b\}\), and \(v=\max\{a,b\}\). The **finite-sample joint covariance**, valid for every integer \(N\ge1\), is
\[
\boxed{\operatorname{Cov}(V_N(s),V_N(t))=\frac{2N(N-1)}{3}u^2[3v(1-v)-u].}
\tag{1}
\]

Moreover, let \(\delta_N\downarrow0\) satisfy \(\delta_N\sqrt N/\log N\to\infty\). For each fixed \(R>0\), define the continuous fluctuation process on \([0,R]\)
\[
Y_N(r)=\frac{V_N(r\delta_N)-Nr\delta_N(1-r\delta_N)}{N\delta_N^{3/2}}.
\]
Then, as \(N\to\infty\),
\[
\boxed{Y_N\Longrightarrow\left(2\int_0^r W_z\,dz\right)_{0\le r\le R}\quad\text{in }C([0,R]),}
\tag{2}
\]
where \(W\) is standard Brownian motion. In particular, for \(0\le r\le t\), the limiting covariance is
\[
\boxed{\operatorname{Cov}(Y(r),Y(t))=\frac23r^2(3t-r).}
\tag{3}
\]
Thus a **single** uniform sample produces a correlated process over all shrinking window lengths, and its mesoscopic limit is twice integrated Brownian motion (not a collection of independent Gaussian variables).

## Assumptions and scope
The points are iid Haar-uniform on the circle; the number variance integrates over all circular translates of a window. Formula (1) is exact at every finite sample size and every pair of lengths, including \(N=1\), \(s=0\), \(s=1\), and lengths exceeding one half. The functional limit holds for a deterministic sequence \(\delta_N>0\) approaching zero, provided \(\delta_N\sqrt N/\log N\to\infty\); the convergence is weak in the uniform topology of \(C([0,R])\) for each fixed \(R\). No claim is made at scales below this sufficient coupling range, for dependent sample points, or for a growing range \(R\).

## Proof
**1. Finite-sample covariance.** For \(s\in[0,1]\), define the centered periodic overlap kernel
\[
h_s(d)=(s-d)_+ +(s-(1-d))_+-s^2,\qquad 0\le d<1,
\]
where \(x_+=\max(x,0)\). Expanding the squared count and integrating gives the deterministic identity
\[
V_N(s)=Ns(1-s)+2\sum_{1\le i<j\le N}h_s((U_i-U_j)\bmod1).
\tag{4}
\]
For a uniform \(U_j\), the conditional mean of the kernel given \(U_i\) is zero; hence covariances of distinct pair summands vanish even when those pairs share one sample index. Their Fourier coefficients at nonzero integer frequency \(k\) are
\[
\widehat h_s(k)=\frac{\sin^2(\pi ks)}{\pi^2k^2},\qquad \widehat h_s(0)=0.
\]
Writing \(\lambda_k(s)=2\sin^2(\pi ks)/(\pi^2k^2)\), Parseval and (4) therefore yield
\[
\operatorname{Cov}(V_N(s),V_N(t))=N(N-1)\sum_{k=1}^{\infty}\lambda_k(s)\lambda_k(t).
\tag{5}
\]
The expression is unchanged by replacing a length with its complement. For \(0\le s\le t\le1/2\), use \(\sin^2z=(1-\cos2z)/2\) and the Fourier--Bernoulli identity
\[
\sum_{k=1}^{\infty}\frac{\cos(2\pi kx)}{k^4}=-\frac{\pi^4}{3}B_4(\{x\}),\qquad B_4(x)=x^4-2x^3+x^2-\frac1{30}.
\]
The right side of (5), divided by \(N(N-1)\), becomes
\[
\frac1{90}+\frac{B_4(s)+B_4(t)}3-\frac{B_4(t-s)+B_4(s+t)}6
=\frac23s^2[3t(1-t)-s].
\]
This proves (1), including the boundary cases by continuity.

**2. One Brownian bridge for all scales.** Let \(B\) be a standard Brownian bridge, extended periodically. Set
\[
H_s=\int_0^1(B(\{x+s\})-B(x))^2\,dx.
\]
The nonzero complex Fourier coefficients of the bridge, after multiplication by \(2\pi ik\), are independent circular standard complex Gaussian variables for positive \(k\): this follows by integration by parts applied to \(B(x)=W(x)-xW(1)\) and orthogonality of the integer Fourier modes of Brownian white noise. Parseval therefore gives the **simultaneous** process representation
\[
H_s=\sum_{k=1}^{\infty}\lambda_k(s)E_k,\qquad 0\le s\le1,
\tag{6}
\]
with a common iid sequence \(E_k\sim\operatorname{Exp}(1)\) at every scale. The series converges uniformly in \(s\) almost surely, since \(\lambda_k(s)\le 2/(\pi^2k^2)\). In particular \(\mathbb EH_s=s(1-s)\), and the joint covariance is the kernel in (5) without its finite-sample factor.

**3. Shrinking-scale bridge limit.** For \(\delta\downarrow0\) and \(r\in[0,R]\), define
\[
Z_\delta(r)=\delta^{-3/2}[H_{\delta r}-\delta r(1-\delta r)]
=\sum_{k=1}^{\infty}\frac{\lambda_k(\delta r)}{\delta^{3/2}}(E_k-1).
\]
For \(0\le r\le t\le R\) and small enough \(\delta\), (1) gives the exact identity
\[
\operatorname{Cov}(Z_\delta(r),Z_\delta(t))
=\frac23r^2(3t-r)-2\delta r^2t^2.
\tag{7}
\]
At any finite collection of \(r\)'s, every fixed linear combination is a triangular array sum of independent centered exponentials. The maximum absolute coefficient is bounded by \(2R^2\sqrt\delta\) times the sum of absolute linear-combination weights, while the squared-coefficient sum stays bounded by (7). Its third absolute-moment sum is thus \(O(\sqrt\delta)\). Lyapunov's theorem and Cramér--Wold give jointly Gaussian finite-dimensional limits with the covariance in (3), including degenerate combinations by the second-moment bound.

For \(0\le r\le t\le R\), (7) further gives
\[
\operatorname{Var}(Z_\delta(t)-Z_\delta(r))
=4r(t-r)^2+\frac43(t-r)^3-2\delta(t^2-r^2)^2
\le\frac{16R}{3}|t-r|^2.
\]
A centered exponential variable has variance \(1\) and fourth moment \(9\); consequently a linear combination of independent centered exponentials has fourth moment at most nine times the square of its variance. The uniform bound \(\mathbb E|Z_\delta(t)-Z_\delta(r)|^4\le 9(16R/3)^2|t-r|^4\) implies tightness in \(C([0,R])\) (every process vanishes at \(r=0\)). Its Gaussian limit has covariance (3), which equals \(4\int_0^r\int_0^t\min(z,w)\,dw\,dz\); hence the limit is twice integrated Brownian motion.

**4. Return to empirical counts.** Apply the Komlós--Major--Tusnády strong approximation, in the form used in the source paper, coupling the centered empirical distribution \(G_N(x)=\sqrt N(F_N(x)-x)\) to a standard Brownian bridge \(B_N(x)\) so that \(\eta_N=\|G_N-B_N\|_\infty=O_{\mathbb P}(\log N/\sqrt N)\). Circular increments of \(G_N\) yield exactly \(V_N(s)/N\). Therefore Cauchy--Schwarz gives, simultaneously for \(0\le s\le R\delta_N\),
\[
\left|\frac{V_N(s)}N-H_{N,s}\right|
\le4\eta_N\sqrt{H_{N,s}}+4\eta_N^2.
\tag{8}
\]
From (6) and \(\lambda_k(s)\le\min\{2R^2\delta_N^2,2/(\pi^2k^2)\}\),
\[
\mathbb E\sup_{0\le s\le R\delta_N}H_{N,s}
\le\sum_{k\ge1}\min\{2R^2\delta_N^2,2/(\pi^2k^2)\}=O_R(\delta_N).
\]
Thus (8), divided by \(\delta_N^{3/2}\), is
\[
O_{\mathbb P}\left(\frac{\log N}{\sqrt N\delta_N}
+\frac{(\log N)^2}{N\delta_N^{3/2}}\right)=o_{\mathbb P}(1)
\]
under the stated hypothesis. The centered coupled bridge fluctuations are distributed as \(Z_{\delta_N}\), so functional Slutsky yields (2).

## Verification
The standalone file `verify.py` uses only Python's standard library. Running `python verify.py` checks the exact pairwise count identity against direct piecewise integration for \(450\) deterministic pseudorandom configurations, the Fourier covariance against the closed polynomial in \(120\) scale pairs, the exact scaled covariance in \(100\) cases, and the Gaussian increment-covariance identity in \(100\) cases (\(770\) checks total). These are finite diagnostics; the all-sample and asymptotic conclusions rely on the four analytical steps above.

## Relationship to prior work
Aistleitner, Hörmann, and Manskova (arXiv:2610.11687v1, October 8, 2026) established the exact single-window expected number variance, its Brownian-bridge exponential-series approximation and fixed-window variance, together with almost-sure Poissonian-window thresholds. Their Theorem 1 and Sections 2--4 use a fixed window length; their Lemma 4 gives the diagonal asymptotic variance \(\frac43s^3-2s^4\), agreeing with (1) after removing the finite factor. The new statement treats arbitrary pairs of lengths at finite \(N\) and the entire process over shrinking lengths, including the identified integrated-Brownian Gaussian limit.

Andreanov and Grebenkov (arXiv:1205.2100v1, 2012) analyze the scalar time-averaged mean-square displacement of an ordinary Brownian trajectory, a related quadratic increment functional. Their averaging is nonperiodic and their results are single-lag distributional formulas and cumulants, not joint finite-sample covariance or a functional shrinking-window theorem for circular empirical point counts. The Gaussian-process techniques themselves are classical; no claim of novelty is made for the KMT approximation, Fourier diagonalization, or Gaussian triangular-array CLT in isolation.

## Limitations
The condition \(\delta_N\sqrt N/\log N\to\infty\) is **sufficient**, not asserted optimal. The limiting theorem concerns weak convergence in the fixed compact window-index range, not strong approximation at the normalized fluctuation scale, not extreme windows below the stated coupling regime, and not dependent or nonuniform samples. The displayed finite exact covariance does not determine the finite-dimensional finite-sample distribution. Prior research on Brownian time-averaged quadratic increments may imply analogous Gaussian limits in related settings; no priority claim is made for those generic fluctuation techniques. No independent validation has been performed.

## References
1. C. Aistleitner, S. Hörmann, and M. Manskova, *On the asymptotic behavior of the number variance of random points on the unit torus*, arXiv:2610.11687v1 (first publicly available October 8, 2026), https://arxiv.org/abs/2610.11687 .
2. A. Andreanov and D. S. Grebenkov, *Time-averaged MSD of Brownian motion*, arXiv:1205.2100v1 (May 9, 2012), https://arxiv.org/abs/1205.2100 .
3. J. Komlós, P. Major, and G. Tusnády, *An approximation of partial sums of independent RV's and the sample DF. I*, Zeitschrift für Wahrscheinlichkeitstheorie und Verwandte Gebiete 32 (1975), 111–131; classical empirical-process coupling cited in Reference 1.
