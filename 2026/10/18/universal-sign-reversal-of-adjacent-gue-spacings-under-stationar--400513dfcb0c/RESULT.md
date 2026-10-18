# Universal sign reversal of adjacent GUE spacings under stationary renewal resetting

## Finding
Let \(H_t\) be the drift-free \(3\times3\) Hermitian matrix Brownian motion started at the zero matrix and normalized by \(H_t\overset{d}=\sqrt t\,H_1\), where \(H_1\) has matrix density proportional to \(\exp[-\operatorname{tr}(H^2)/2]\). Let independent simultaneous resets return the entire matrix to zero after successive strictly positive i.i.d. durations \(W\), with \(0<\mathbb EW<\infty\) and \(\mathbb EW^2<\infty\). Observe the stationary-renewal version at a time chosen independently of the motion and the resetting environment. For its ordered eigenvalues let \(G_1=\lambda_2-\lambda_1\) and \(G_2=\lambda_3-\lambda_2\).

Set
\[
m=\frac{27}{8\sqrt\pi},\quad h=\frac{27\sqrt3}{2\pi}-4,\quad c_*=\frac{108\sqrt3-81-32\pi}{8\pi}>0.
\]
Writing \(A\) for the stationary time elapsed since the last reset, the exact identity and sharp bound are
\[
\operatorname{Cov}(G_1,G_2)=h\,\mathbb EA-m^2(\mathbb E\sqrt A)^2\ \ge\ c_*\,\mathbb EA>0.
\]
Equality holds if and only if the reset interval \(W\) is deterministic. In particular, if the resets are Poisson with rate \(r>0\), then
\[
\operatorname{Cov}(G_1,G_2)=\frac1r\left(\frac{27\sqrt3}{2\pi}-\frac{1753}{256}\right)>0.
\]
In contrast, for a reset-free snapshot at a fixed age \(t>0\),
\[
\operatorname{Cov}(G_1(t),G_2(t))=t\left(\frac{27\sqrt3}{2\pi}-4-\frac{729}{64\pi}\right)<0.
\]
Thus the fixed-age anticorrelation of the two neighboring GUE spacings reverses sign under **every** stationary-renewal reset protocol with the stated moments, and deterministic-period resetting minimizes the stationary covariance after normalization by mean age.

## Assumptions and scope
Matrix entries are independently restarted at each reset, with an entirely fresh Hermitian Brownian path. The stationary renewal clock is independent of these paths. The inter-reset times have any law supported in \((0,\infty)\), including discrete distributions; a stationary observation for deterministic periods uses a uniformly randomized phase. Finite \(\mathbb EW^2\) ensures the stationary-age mean is finite. The matrix normalization gives ordered eigenvalue density proportional to \(\exp[-(\lambda_1^2+\lambda_2^2+\lambda_3^2)/(2t)]\prod_{i<j}(\lambda_j-\lambda_i)^2\) at each \(t>0\). Multiplying the matrix Brownian variance by \(\sigma^2>0\) multiplies all covariance formulas by \(\sigma^2\).

## Proof
**1. Exact fixed-age two-gap moments.** At time \(t=1\) put \(a=\lambda_2-\lambda_1>0\), \(b=\lambda_3-\lambda_2>0\), and integrate out the mean eigenvalue. The resulting density is
\[
 f(a,b)=\frac{a^2b^2(a+b)^2}{I_{00}}\exp\!\left[-\frac{a^2+ab+b^2}{3}\right],\qquad a,b>0.
\]
For integers \(k,l\ge0\), define
\[
 I_{kl}=\int_0^\infty\!\int_0^\infty a^{k+2}b^{l+2}(a+b)^2\exp\!\left[-\frac{a^2+ab+b^2}{3}\right]da\,db.
\]
The substitutions \(s=a+b\), \(u=a/(a+b)\) give the absolutely convergent one-variable integral
\[
 I_{kl}=\frac{3^{(8+k+l)/2}}2\,\Gamma\!\left(\frac{8+k+l}2\right)\int_0^1\frac{u^{k+2}(1-u)^{l+2}}{(u^2-u+1)^{(8+k+l)/2}}du.
\]
Elementary trigonometric substitution \(2u-1=\sqrt3\tan\phi\), \(-\pi/6<\phi<\pi/6\), and integration of the resulting polynomial-trigonometric functions yield
\[
 I_{00}=4\pi\sqrt3,\qquad I_{10}=I_{01}=\frac{27}2\sqrt{3\pi},\qquad I_{11}=162-16\pi\sqrt3.
\]
Hence \(\mathbb E a=\mathbb E b=I_{10}/I_{00}=m\) and \(\mathbb E(ab)=I_{11}/I_{00}=h\). At age \(t\), Brownian self-similarity implies \((G_1(t),G_2(t))\overset d=\sqrt t\,(a,b)\); therefore their fixed-age covariance is \(t(h-m^2)\).

**2. Exact equilibrium-age mixture.** For renewal periods \(W\) of finite positive mean, the equilibrium age has density in the measure sense
\[
 \mathbb P(A\in da)=\frac{\mathbb P(W>a)}{\mathbb EW}\,da\quad(a\ge0).
\]
Equivalently, \(A=U W^*\), where \(U\) is independent uniform on \((0,1)\) and \(W^*\) has length-biased law \(\mathbb P(W^*\in dw)=w\,\mathbb P(W\in dw)/(\mathbb EW)\). Consequently,
\[
 \mathbb EA=\frac{\mathbb EW^2}{2\mathbb EW},\qquad \mathbb E\sqrt A=\frac{2\,\mathbb EW^{3/2}}{3\mathbb EW}.
\]
Conditional on age, the two gaps have the reset-free law at that age; hence \(\mathbb EG_1=\mathbb EG_2=m\mathbb E\sqrt A\) and \(\mathbb E(G_1G_2)=h\mathbb EA\), proving the covariance identity.

**3. Sharp, strictly positive lower bound.** Cauchy–Schwarz yields
\[
 (\mathbb EW^{3/2})^2\le(\mathbb EW)(\mathbb EW^2),\quad
 \frac{(\mathbb E\sqrt A)^2}{\mathbb EA}\le\frac89.
\]
Equality in Cauchy–Schwarz requires \(W\) constant almost surely, and any constant \(W\) indeed attains equality. Substitution gives the claimed sharp bound. To establish its strict numerical sign without a plot, use the rational inequalities \(\sqrt3>19/11\) and \(\pi<22/7\), which give \(108\sqrt3-81-32\pi>108(19/11)-81-32(22/7)>0\). Conversely, \(\sqrt3<7/4\) and \(\pi>25/8\) imply \(864\sqrt3-256\pi-729<1512-800-729<0\); this last expression is \(64\pi(h-m^2)\), proving the fixed-age sign.

**4. Poisson specialization.** With exponential reset intervals of rate \(r\), the equilibrium age is also exponential of rate \(r\), with \(\mathbb EA=1/r\) and \((\mathbb E\sqrt A)^2=\pi/(4r)\). Substituting the exact fixed-age moments proves the stated Poisson coefficient.

## Verification
Run `python3 check.py` using only the Python standard library. It implements independently the one-variable quadrature for \(I_{00},I_{10},I_{11}\), compares the stated exact evaluations, and evaluates 234 assertions including the signed covariance formulas, deterministic sharpness, general two-point renewal durations, and the Poisson identity. This computation is corroboration, not the proof for arbitrary times, matrices, or renewal laws; those statements follow from Steps 1–4. The coefficient values are approximately \(h-m^2=-0.182808459118\), \(c_*=0.220052490583\), and the rate-one Poisson covariance \(0.595283838194\).

## Relationship to prior work
Biroli–Majumdar–Schehr (2025) introduced simultaneously Poisson-reset Dyson Brownian motion and derived the stationary joint eigenvalue law; they explicitly analyze an individual spacing through the \(N=2\) surmise and large-\(N\) spacing behavior. Their full finite-\(N\) density is an essential premise, not a claimed contribution. Akemann–Majumdar–Päßler (2026) constructs arbitrary-index tridiagonal resetting matrix models and recovers the Poisson stationary joint law. Shir–Martinez-Azcona–Chenu (2025) analyzes individual \(k\)-nearest-neighbor spacing distributions, not the covariance of **two different** adjacent spacings in stationary-renewal environments. The present narrow contribution is the evaluated \(3\times3\) joint-gap moment, renewal-universal positive covariance and sharp lower coefficient, juxtaposed with fixed-age negative covariance. General equilibrium-age identities and elementary Cauchy–Schwarz are standard; their statements are not claimed as new. Other random-matrix joint-gap calculations may independently yield parts of the fixed-age moment, and implicit coverage remains a literature risk.

## Limitations
The universal sign theorem holds for \(3\times3\) GUE-type matrix diffusion started and reset at zero, with no confining potential, complete simultaneous renewal resetting, and finite second moment of reset periods. It does not establish the same sign in other matrix sizes, other Dyson indices, nonzero reset matrices, independent entry resets, traps, or nonequilibrium observation times. A fixed deterministic observation age is **not** a stationary renewal observation. Numerical checks do not substitute for the derived exact integrals or renewal argument. Independent external validation has not been performed.

## References
1. M. Biroli, S. N. Majumdar, G. Schehr, *Resetting Dyson Brownian motion*, arXiv:2503.14733v1 (first public 2025-03-18); *Phys. Rev. E* **112**, 014101 (2025), DOI: 10.1103/d29k-kmcs.
2. G. Akemann, S. N. Majumdar, P. Päßler, *A tridiagonal matrix-valued process with stochastic resetting for arbitrary Dyson index*, arXiv:2605.26945v1 (2026).
3. R. Shir, P. Martinez-Azcona, A. Chenu, *Surmise for random matrices’ level spacing distributions beyond nearest-neighbors*, arXiv:2504.20134v1 (2025).
4. American Mathematical Society, MSC2020 code 82C31, stochastic methods applied to time-dependent statistical mechanics.
