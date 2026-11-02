# A sharp oscillatory-memory boundary for a run–pause particle in a harmonic trap

## Finding

An overdamped particle in a harmonic trap can exhibit indefinitely alternating signs in its stationary *position autocovariance*, without inertia, provided that its pauses retain a direction label and bias subsequent runs toward reversal. The onset has a sharp, two-parameter classification.

Let \(b,\gamma,v>0\) and \(-1\leq\eta<1\). A four-state continuous-time chain has states \(R_+,T_+,R_-,T_-\), with rate \(\gamma\) for each \(R_s\to T_s\), rate \(\gamma(1+\eta)/2\) for \(T_s\to R_s\), and rate \(\gamma(1-\eta)/2\) for \(T_s\to R_{-s}\), for \(s\in\{+1,-1\}\). The position solves \(\dot X_t=-bX_t+v q_R(J_t)\), where \(q_R(R_s)=s\) and \(q_R(T_s)=0\). The label is retained during the pause; \(\eta=0\) means independent choice of the next run direction and \(\eta<0\) favors a reversal.

Write \(C(t)=\mathbb E[X_0X_t]\) under the unique joint stationary law. Then

\[
\boxed{\ C(t)\text{ has infinitely many strict positive and negative lag intervals}\quad\Longleftrightarrow\quad \eta<0\ \text{and}\ b\geq\gamma.\ }
\]

For \(\eta\geq0\), the autocovariance is strictly positive at every lag. For \(\eta<0\) and \(b<\gamma\), it is strictly positive at all sufficiently large lags, although this assertion does not exclude finite negative intervals. On the sharp boundary \(b=\gamma\), set \(\omega=\gamma\sqrt{-\eta}\). The exact profile is

\[
\boxed{\ \frac{C(t)}{C(0)}=e^{-\gamma t}\left(\frac{1+\cos(\omega t)}2+\frac{\gamma}{\omega}\sin(\omega t)\right),\quad t\geq0.\ }
\]

Its first positive-lag zero occurs exactly at \(\pi/\omega\), and its first strictly negative interval is

\[
\left(\frac\pi\omega,\ \frac{2\pi-2\arctan(\omega/(2\gamma))}{\omega}\right).
\]

The profile repeats its sign pattern with angular period \(2\pi\), while its envelope decays. The delay to the first sign reversal diverges as \(\pi/(\gamma\sqrt{-\eta})\) when reversal bias tends to zero. These statements concern stationary two-time statistics, not oscillatory sample paths.

## Assumptions and scope

All rates and trap strength are time-independent. There is no translational thermal noise, resetting, interaction with other particles, or inertia. The internal chain is irreducible even at \(\eta=-1\), and is not assumed reversible. The endpoint \(\eta=1\) is excluded, since it creates two disconnected persistent-sign classes. The unique stationary position is the bounded past-history filter

\[
X_t=v\int_{-\infty}^t e^{-b(t-u)}q_R(J_u)\,du,
\qquad |X_t|\leq v/b.
\]

In particular \(\mathbb E X_t=0\) and \(C\) is continuous. The claim concerns all \(t\geq0\), all \(-1\leq\eta<1\), and all \(b,\gamma,v>0\), with *infinitely many* strict alternating-sign intervals as the classification property; it does not claim a classification of whether *any single* negative lag occurs for \(b<\gamma\).

## Proof

**1. Internal stationarity and the closed odd sector.** The stationary probabilities of \(R_+,T_+,R_-,T_-\) are all \(1/4\): each run and pause has the same total exit rate and incoming balance. The finite-state generator \(L\), acting on \(q_R\) and on \(q_T(R_s)=0,\ q_T(T_s)=s\), satisfies

\[
Lq_R=-\gamma q_R+\gamma\eta q_T,
\qquad Lq_T=\gamma q_R-\gamma q_T.
\]

Thus the odd sector has the matrix \(\gamma\begin{pmatrix}-1&\eta\\1&-1\end{pmatrix}\). Its two eigenvalues are \(-\gamma\pm\gamma\sqrt\eta\), with the principal imaginary square root when \(\eta<0\).

**2. Stationary mixed moments.** Let \(k_R=\mathbb E[Xq_R]\) and \(k_T=\mathbb E[Xq_T]\). Since \(\mathbb E[q_R^2]=1/2\), applying the joint generator to \(Xq_R\) and \(Xq_T\) gives

\[
0=-(b+\gamma)k_R+\gamma\eta k_T+v/2,
\qquad 0=\gamma k_R-(b+\gamma)k_T.
\]

With \(D=(b+\gamma)^2-\gamma^2\eta>0\), the unique solution and the stationary second-moment identity are

\[
k_R=\frac{v(b+\gamma)}{2D},\qquad
k_T=\frac\gamma{b+\gamma}k_R,\qquad
C(0)=\mathbb E[X^2]=\frac{v k_R}{b}>0.
\]

**3. Covariance evolution.** For \(t\geq0\), put \(h_R(t)=\mathbb E[X_0q_R(J_t)]\), and define \(h_T\) similarly. Generator evolution gives

\[
\binom{h_R}{h_T}'=\gamma
\begin{pmatrix}-1&\eta\\1&-1\end{pmatrix}
\binom{h_R}{h_T},\qquad
C'(t)=-bC(t)+v h_R(t),
\]

with initial data \((h_R(0),h_T(0),C(0))=(k_R,k_T,v k_R/b)\). For \(\eta<0\), write \(\omega=\gamma\sqrt{-\eta}\). Direct matrix exponentiation yields

\[
h_R(t)=k_Re^{-\gamma t}
\left(\cos(\omega t)-\frac\omega{b+\gamma}\sin(\omega t)\right).
\]

Define \(R=(1+i\omega/(b+\gamma))/(b-\gamma+i\omega)\), whose numerator and denominator are nonzero. Solving the scalar equation for \(C\) gives the exact real-valued formula

\[
\boxed{\ C(t)=v k_R\left[\frac{e^{-bt}}b+
\operatorname{Re}\left\{R\big(e^{(-\gamma+i\omega)t}-e^{-bt}\big)\right\}\right].\ }
\]

This formula holds at \(b=\gamma\), too, without a removable-singularity convention because \(\omega>0\).

**4. Sign classification for reversal bias.** If \(b>\gamma\), the nonzero complex coefficient \(R\) produces an oscillatory leading term \(v k_R e^{-\gamma t}\operatorname{Re}(Re^{i\omega t})\); the remaining term is \(O(e^{-bt})\). Hence alternating open positive and negative lag intervals persist arbitrarily far out. If \(b<\gamma\), the leading \(e^{-bt}\) coefficient in \(C/(v k_R)\) is

\[
A=\frac1b-\operatorname{Re}R
=\frac{\gamma(\gamma^2+\omega^2-b^2)}{b(b+\gamma)((b-\gamma)^2+\omega^2)}>0.
\]

Thus \(C(t)=v k_R A e^{-bt}+O(e^{-\gamma t})>0\) for all sufficiently large \(t\). At \(b=\gamma\), simplifying \(R\) gives the normalized critical profile above. Its trigonometric bracket factors as

\[
\cos(\omega t/2)
\left[\cos(\omega t/2)+\frac{2\gamma}{\omega}\sin(\omega t/2)\right].
\]

The factorization gives the first zero \(\pi/\omega\), the stated negative interval, and periodically recurring sign changes at arbitrarily large lags.

**5. No sign reversal without reversal bias.** For \(\eta\geq0\), the stationary active-force covariance is

\[
\mathbb E[vq_R(J_0)\,vq_R(J_t)]
=\frac{v^2}{2}e^{-\gamma|t|}\cosh(\gamma\sqrt\eta\,|t|)>0.
\]

The stationary position is the stable linear filter of this active force. Its covariance is the positive-kernel convolution

\[
C(t)=\frac1{2b}\int_{-\infty}^{\infty}e^{-b|t-u|}
\mathbb E[vq_R(J_0)\,vq_R(J_u)]\,du>0.
\]

Together, the three cases prove the biconditional and all boundary statements.

## Verification

The included standalone `verify.py` uses only Python's standard library. It builds the four-state generator explicitly and checks exact-rational stationary balance, generator action on the odd sector, mixed-moment equations, and the stationary variance. Independently it solves the closed covariance ODE by numerical Taylor matrix propagation and compares against the spectral expression on a parameter grid including both sides of the critical boundary, \(b=\gamma\), and \(\eta=0\). Further checks cover strict signs at the critical boundary, the nonzero oscillatory residue above the boundary, and positivity of the real-pole coefficient below it. Run `python verify.py` next to this document. The observed replay reported 2,970 passing assertions; finite computation supports, but does not establish, the universal proof.

## Relationship to prior work

Sun, Ye and Chen (first publicly submitted 2026-10-18) derive conditional stationary distributions and a stochastic moment framework for harmonically trapped run-and-tumble particles with finite tumble times; their tumble phase independently reselects the next run direction. Sun, Ye and Podgornik (2024) develop the related finite-tumble positional statistics. Basu and collaborators (2019) solve the harmonic trap's three-velocity stationary distribution. Those models do not retain a hidden sign during pauses with an adjustable next-run reversal bias; the unbiased case here, \(\eta=0\), overlaps their orientation-renewing mechanism and is not claimed as novel. Britton and collaborators (2026) study nonuniform post-tumble orientations, notably spatial statistics in a different setting; full-text overlap with the finite-pause trapped model was not resolved. Classical covariance filtering and eigenvalue methods are standard tools, not independent contributions. The contribution asserted here is the complete sharp sign-oscillation classification for the direction-retaining four-state trapped process and the exceptional critical-lag law, not the general method of computing finite-state correlations.

## Limitations

This theorem does not determine the full stationary position density, the sign of every finite-lag covariance when \(\eta<0\) and \(b<\gamma\), mixing rates in stronger norms, or the effect of added thermal noise. The stationary correlations may have exponentially small amplitude at their first sign reversal when \(\eta\) is only weakly negative, so experimental detectability is not implied. Broader work on persistent velocity-jump filters might imply aspects of the result; the precise literature novelty is a best-knowledge assessment pending independent priority examination. No independent mathematical audit has been performed.

## References

1. A. Sun, F. Ye, J. Z. Y. Chen, *Run-and-tumble particles in a harmonic external field: constructing the solution of the Fokker-Planck equation from the equations of motion*, arXiv:2610.24961 (first submitted 2026-10-18), https://arxiv.org/abs/2610.24961.
2. A. Sun, F. Ye, R. Podgornik, *Exact moments for a run and tumble particle with a finite tumble time in a harmonic trap* (related finite-tumble analysis), arXiv:2409.00578, https://arxiv.org/abs/2409.00578.
3. U. Basu, S. N. Majumdar, A. Rosso, S. Sabhapandit, G. Schehr, *Exact stationary state of a run-and-tumble particle with three internal states in a harmonic trap*, arXiv:1910.10083, https://arxiv.org/abs/1910.10083.
4. C. Britton, Z. Zhang, S. Han, T. Bertrand, *Run-and-tumble particles with preferred reorientation*, arXiv:2608.23519, https://arxiv.org/abs/2608.23519.
5. M. Baldovin, A. Manacorda, *Control protocols for harmonically confined run-and-tumble particles*, Phys. Rev. E 114, 014112 (2026), https://doi.org/10.1103/rspp-2334.
