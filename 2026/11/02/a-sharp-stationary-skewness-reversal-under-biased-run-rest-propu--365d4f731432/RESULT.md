# A sharp stationary skewness reversal under biased run–rest propulsion

## Finding

An active particle may have a strictly positive mean position relative to the center of a harmonic trap, while its stationary distribution is skewed in the *opposite* direction. For a three-state run–rest particle, there is exactly one rest-to-run rate at which the stationary third centered moment changes sign; this transition occurs **strictly before** equality of the mean run and rest durations. The location of this threshold is an explicit algebraic function of trap relaxation, run termination and the bias of the freshly selected direction.

Let the rate of termination of a run be \(\alpha>0\), the rate of completion of a resting/tumbling phase be \(\beta>0\), the harmonic relaxation rate be \(\kappa>0\), and the probability of choosing the positive direction at the next run be \(p\in(1/2,1)\). Set
\[
a=\alpha/\kappa,\qquad b=\beta/\kappa,\qquad w=2p-1\in(0,1).
\]
Define
\[
\mathcal P(a,b,w)=a(a+1)(a+2)(a-b)
-(1-w^2)b^2\bigl[7a^2+12a+4+(7a+6)b+2b^2\bigr].
\]
For the unique stationary position \(X\), including any independent thermal diffusivity \(D\ge0\), the exact third centered moment is
\[
\boxed{\displaystyle
\mathbb E[(X-\mathbb EX)^3]
=\left(\frac v\kappa\right)^3
\frac{2bw\,\mathcal P(a,b,w)}
{(a+1)(a+2)(a+b)^3(a+b+1)(a+b+2)}.}
\]
For every fixed \(a>0\) and \(w\in(0,1)\), a **unique** \(b_*(a,w)\in(0,a)\) solves \(\mathcal P(a,b_*,w)=0\). The stationary skewness is positive for \(0<b<b_*\), zero precisely at \(b=b_*\), and negative for \(b>b_*\). Its sign changes even though \(\mathbb EX=v\beta w/[\kappa(\alpha+\beta)]>0\) throughout. The root is strictly increasing in \(w\), and \(b_*(a,w)\to a\) as \(w\uparrow1\). At \(w=1\), interpreted as always selecting the positive run, the exact threshold is \(b_*=a\). At \(w=0\), reflection symmetry makes the third centered moment identically zero, so no skewness-sign threshold is asserted.

## Assumptions and scope

Let \(S_t\in\{-1,0,+1\}\) be the continuous-time Markov chain with rates \(+1\to0\) and \(-1\to0\) equal to \(\alpha\), and \(0\to+1\), \(0\to-1\) equal to \(\beta p\), \(\beta(1-p)\). At each departure from rest, the run direction is freshly sampled; there is no direct switch between the two running states. Let \(B_t\) be standard Brownian motion independent of \(S\). The position evolves as
\[
dX_t=(-\kappa X_t+vS_t)\,dt+\sqrt{2D}\,dB_t,
\qquad v,\kappa,\alpha,\beta>0,\quad D\ge0.
\]
All distributions and moments are stationary; \(\mathbb EX\) denotes the stationary expectation. The *standardized* skewness is \(\mathbb E[(X-\mathbb EX)^3]/\operatorname{Var}(X)^{3/2}\); its sign equals the sign of the displayed third centered moment because the stationary variance is strictly positive. The claim does not assert a change of modal shape or a change of the sign of the mean.

## Proof

**Existence, normalization and the thermal factor.** The internal chain is irreducible for \(0<p<1\); its stationary probabilities, ordered as \((+1,0,-1)\), are
\[
\pi=\left(\frac{b(1+w)}{2(a+b)},\frac{a}{a+b},\frac{b(1-w)}{2(a+b)}\right).
\]
The unique stationary solution exists as a pullback integral,
\[
X_t=v\int_{-\infty}^t e^{-\kappa(t-s)}S_s\,ds
+\sqrt{2D}\int_{-\infty}^t e^{-\kappa(t-s)}\,dB_s.
\]
The first summand is bounded in absolute value by \(v/\kappa\); the second is an independent centered Gaussian of variance \(D/\kappa\). Hence the third cumulant of the sum is precisely the third cumulant of the first summand, at every \(D\ge0\).

**Stationary moment equations.** Rescale the active position by \(Y=\kappa X^{\mathrm{act}}/v\) and time by \(\tau=\kappa t\); then \(dY/d\tau=-Y+S\). Define the three-component column \(m_n\) by \((m_n)_s=\mathbb E[Y^n\mathbf1_{\{S=s\}}]\) in state order \((+1,0,-1)\). Write
\[
Q=\begin{pmatrix}-a&a&0\\b(1+w)/2&-b&b(1-w)/2\\0&a&-a\end{pmatrix},\qquad
V=\operatorname{diag}(1,0,-1).
\]
Stationarity of the joint generator, applied to each \(Y^n\mathbf1_{\{S=s\}}\), gives the exact finite-dimensional recurrence
\[
m_0=\pi^\top,\qquad (nI-Q^\top)m_n=nVm_{n-1}\quad(n=1,2,3).
\]
Each matrix is invertible: the eigenvalues of \(Q\) have nonpositive real part, while \(n\ge1\). Consequently this recurrence determines all moments used below without closure approximation. Summing components yields
\[
M_1=\frac{bw}{a+b},\qquad
M_2=\frac{b(abw^2+a+b+1)}{(a+1)(a+b)(a+b+1)},
\]
\[
M_3=\frac{bw\,[a^2b^2w^2+3a^2b+2a^2+3ab^2+9ab+6a+2b^2+6b+4]}
{(a+1)(a+2)(a+b)(a+b+1)(a+b+2)}.
\]
The central third moment \(M_3-3M_1M_2+2M_1^3\) simplifies exactly to
\[
\frac{2bw\mathcal P(a,b,w)}{(a+1)(a+2)(a+b)^3(a+b+1)(a+b+2)}.
\]
Restoring the scale \((v/\kappa)^3\) and using Gaussian cumulant additivity proves the formula for \(X\). The variance is positive because \(S\) is a nonconstant stationary process and a nonzero exponentially filtered copy cannot be deterministic (and the added Gaussian variance is nonnegative).

**The sharp reversal threshold.** Put \(c=1-w^2\in(0,1)\). For \(0<b<a\), the first term of \(\mathcal P\) is strictly decreasing in \(b\) and the strictly positive quantity
\[
c b^2\,[7a^2+12a+4+(7a+6)b+2b^2]
\]
is strictly increasing. Moreover \(\mathcal P(a,0,w)=a^2(a+1)(a+2)>0\), while \(\mathcal P(a,a,w)<0\). There is exactly one root in \((0,a)\). For \(b\ge a\), both terms have nonpositive sign and the second is strictly negative, so there are no additional roots. Every other factor of the stationary third cumulant is positive, proving the complete sign classification. At any \(b>0\), increasing \(w\in(0,1)\) strictly increases \(\mathcal P\); the unique crossing therefore shifts strictly upward in \(b\). As \(w\uparrow1\), \(\mathcal P(a,b,w)\) tends to \(a(a+1)(a+2)(a-b)\), whose unique nonnegative zero is \(b=a\). This proves the claimed limiting threshold and the one-sided endpoint extension.

## Verification

The standalone program `verification/check_skewness.py` evaluates moments by independently solving the finite-state generator equations and compares the resulting centered third moments with the polynomial formula on 60 parameter triples. It also checks 60 additive-Gaussian invariance cases, the unique root and strict sign transitions for nine parameter pairs. Run using `python verification/check_skewness.py`; the program uses NumPy and SciPy. A second executable, `verification/symbolic_check.py`, independently reproduces the rational identities using SymPy. All provided checks were run successfully. The finite computations corroborate, rather than replace, the exact generator and monotonicity proof.

For example, at \(a=1\) and \(w=1/2\), the transition is \(b_*=0.407081392\ldots\); at \(b=0.2\) the third centered moment of the normalized active position is positive, while at \(b=1\) it is negative. These signs hold unchanged after adding independent thermal diffusion.

## Relationship to prior work

Sun, Ye, and Podgornik [1] give an exact moment construction and stationary distribution for finite-duration tumbling with *unbiased* run orientations. Their conclusion specifically mentions biased run orientations as a prospective extension. Basu and collaborators [2] solve the symmetric three-state harmonic-trap model with equal switching rates; their stationary law is reflection-symmetric and has zero third cumulant. Santra, Olsen, and Gupta [3] evaluate skewness for biased intermittent active processes *without a harmonic confining potential*; their Fourier–Laplace framework explicitly assumes translation-invariant dynamics in each phase. None of those evaluated results identifies the biased *confined* stationary skewness-reversal phase boundary established here.

The finite-state generator moment recursion is standard. The claim of novelty is restricted to the evaluated centered-third-moment factorization, the unique polarization-dependent reversal threshold strictly below equal run/rest rates, and its invariance under additive independent thermal diffusion. No novelty is claimed for the Markov generator method or for the symmetric three-state stationary law.

## Limitations

The theorem requires exponential run and rest durations, independent resampling of run direction, a harmonic trap with linear relaxation, and (for the strict threshold) \(0<w<1\). It does not cover correlated reorientation, position-dependent switching rates, nonlinear confinement, arbitrary renewal run/rest distributions, or estimation efficiency for finite trajectory data. A general matrix-analytic theorem for Markov-modulated linear filters could subsume portions of the explicit moment calculation, but the cited literature does not give the evaluated sign-reversal phase diagram. Publication priority beyond the inspected literature is not independently established.

## References

[1] A. Sun, F. Ye, R. Podgornik, *Exact moments for a run and tumble particle in a harmonic trap with a finite tumble time*, arXiv:2409.00578 (first posted 2024-09-01; inspected 2025 revision), https://arxiv.org/abs/2409.00578.

[2] U. Basu, S. N. Majumdar, A. Rosso, S. Sabhapandit, G. Schehr, *Exact stationary state of a run-and-tumble particle with three internal states in a harmonic trap*, arXiv:1910.10083 (2019), https://arxiv.org/abs/1910.10083.

[3] I. Santra, K. S. Olsen, D. Gupta, *Dynamics of switching processes: general results and applications to intermittent active motion*, arXiv:2408.16643 (first posted 2024-08-29; inspected 2024 revision), https://arxiv.org/abs/2408.16643.
