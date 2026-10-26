# Exact negative-memory bands in a cyclic run–rest particle under harmonic confinement

## Finding

A stationary, overdamped active particle with exponentially distributed runs and rests can have *infinitely many alternating positive and negative position-autocorrelation intervals*, despite having neither inertia nor a deterministic oscillator. The complete sign classification below identifies a strict onset, counts every negative interval before the infinite-band transition, and gives its sharp divergence law.

Write \(h=\kappa/r\), \(u=r|t|\), and \(C(t)=\operatorname{Cov}(X_t,X_0)\). Then
\[
C(t)=\frac{v^2}{2r^2(h^4+4)}\left[\frac{2-h^2}{h}e^{-hu}+e^{-u}(h^2\cos u+2\sin u)\right].
\]
For \(0<h<1\), set
\[
\delta=1-h,\quad A=\frac{2-h^2}{h},\quad B=\sqrt{h^4+4},\quad
\phi=\arctan(2/h^2),\quad
u_0=\phi+\pi-\arctan\delta,
\]
\[
M=\frac{B}{\sqrt{1+\delta^2}}e^{-\delta u_0}.
\]
There is a unique \(h_*\in(0,1)\) solving \(A=M\), with \(h_*=0.8914223658803029\ldots\). For \(h<h_*\), \(C(t)>0\) at every finite \(t\). At \(h=h_*\), \(C(t)\ge0\) with exactly one positive-lag zero, at \(t=u_0/r\). For \(h_*<h<1\), the number of connected negative-lag intervals on \(t>0\) is exactly
\[
N(h)=\left\lceil\frac{\log(M/A)}{2\pi(1-h)}\right\rceil.
\]
For \(h\ge1\), there are infinitely many alternating positive and negative intervals, and
\[
N(h)\sim\frac{\log5}{4\pi(1-h)}\qquad(h\uparrow1,\;h<1).
\]
The count is zero at \(h=h_*\) and throughout \((0,h_*)\); the displayed ceiling is asserted only for \(h_*<h<1\).

## Assumptions and scope

Let \(J_t\) be the irreducible, continuous-time, four-state Markov chain with directed cycle \(R_+\to T_+\to R_-\to T_-\to R_+\), each arrow traversed at the same exponential rate \(r>0\). The active velocity function \(q\) is respectively \(+1,0,-1,0\) on these four states. Thus every positive or negative run is followed by a finite random rest and the next run *reverses sign deterministically*; this is not independent random reorientation at the next run. Let the confined coordinate evolve as
\[
\dot X_t=-\kappa X_t+vq(J_t),\qquad \kappa>0,\;v>0,
\]
with no translational thermal diffusion. Take the unique stationary joint law, obtained by taking the Markov chain stationary and filtering its entire past. The result concerns two-time *coordinate autocovariance*, not merely the unconfined motility autocorrelation or stationary position density. All negative-lag intervals refer to positive time lags; by stationarity the covariance is even.

## Proof

**Stationary motility and filtering.** The cycle is uniform in stationarity, and the generator on its first Fourier harmonic has eigenvalues \(-r\pm ir\). Consequently, the mean motility vanishes and
\[
R_q(t)=\mathbb E[q(J_t)q(J_0)]=\frac12e^{-r|t|}\cos(rt).
\]
The contracting linear equation has exactly one stationary solution
\[
X_t=v\int_{-\infty}^t e^{-\kappa(t-s)}q(J_s)\,ds,
\]
whose mean is zero. Its covariance is the convolution of \(v^2R_q\) with \(G_\kappa(t)=e^{-\kappa|t|}/(2\kappa)\). Equivalently, distributionally,
\[
(-\partial_t^2+\kappa^2)C(t)=v^2R_q(t),
\]
with \(C\) even and vanishing as \(|t|\to\infty\). For \(t>0\), solving the forced constant-coefficient ODE and imposing \(C'(0)=0\) gives exactly the displayed closed formula; the solution is continuous at the resonance \(h=1\), so no exceptional parameter is omitted.

**Counting finite negative intervals.** For \(0<h<1\), divide \(C(t)\) by the strictly positive factor \(v^2e^{-hu}/[2r^2(h^4+4)]\). The remaining sign is that of
\[
F_h(u)=A+B e^{-\delta u}\cos(u-\phi).
\]
Here \(A,B,\delta>0\). Whenever \(\cos(u-\phi)\ge0\) the sign is positive. On each negative-cosine half-period there is a unique minimum of the damped cosine (equivalently, a unique maximum of its negative), at \(u_k=u_0+2\pi k\), for \(k\ge0\), because its derivative vanishes exactly when \(\tan(u-\phi)=-\delta\). There are no negative-cosine sectors before the first such sector on \(u\ge0\), since \(0<\phi-\arctan\delta<\pi/2\). The trough values of the sign function are
\[
F_h(u_k)=A-Me^{-2\pi\delta k}.
\]
Each sector therefore contributes exactly one connected interval with negative covariance if and only if \(Me^{-2\pi\delta k}>A\). Counting the nonnegative integers \(k\) satisfying this strict inequality gives the ceiling formula, including the exact-integer boundary case. Equality creates a tangential zero, not a negative interval.

**Uniqueness of the onset.** Normalize the correlation by a positive scalar and let \(f(u)=e^{-|u|}\cos u\). The filter has Fourier multiplier \(h^2/(h^2+\omega^2)\), corresponding to convolution with the probability density \(k_h(u)=(h/2)e^{-h|u|}\). For any \(0<h_1<h_2\), writing \(p=(h_1/h_2)^2\), the exact Fourier identity yields
\[
k_{h_1}*f=\big[p\,\delta_0+(1-p)k_{h_1}\big]*(k_{h_2}*f).
\]
If the higher-rate filtered correlation is everywhere nonnegative, the lower-rate one is everywhere *strictly* positive, because the second kernel has an everywhere-positive density and the higher-rate correlation is positive around zero. For sufficiently small \(h\), \(A>B\), giving strict positivity; at \(h=1\), the bracket is \(1+\cos u+2\sin u\), which takes negative values. By continuity, a finite-lag zero first occurs at some \(h_*\in(0,1)\). The convolution strictness makes this threshold unique and proves that the unique first trough touches zero there, equivalently \(A=M\). Numerical evaluation of this *uniquely specified* root gives the stated approximate value.

**Infinite-band edge and asymptotic law.** At \(h=1\), \(e^{-u}(1+\cos u+2\sin u)\) has infinitely many positive and negative intervals because its sinusoidal amplitude is \(\sqrt5>1\). At \(h>1\), the nonzero oscillatory \(e^{-u}\) term dominates the \(e^{-hu}\) term, giving infinitely many sign changes. Finally, as \(h\uparrow1\), \(A\to1\), \(M\to\sqrt5\), so the ceiling count divided by \(1/(1-h)\) tends to \(\log\sqrt5/(2\pi)=\log5/(4\pi)\), completing the claimed divergence.

## Verification

The accompanying standalone `verify_covariance.py` recomputes the two-time covariance by independently evolving all four mixed moments \(\mathbb E[X_t\mathbf1_{J_t=j}X_0]\) through the Markov forward equations, rather than using the scalar convolution solution. Its parameterized matrix-exponential comparison uses 26 logarithmically spaced confinement ratios and 30 lags each (780 independent comparisons); the largest absolute difference observed was \(1.34\times10^{-15}\) with double precision and normalized \(r=v=1\). The script also brackets and solves the onset equation, computes exact lobe counts for representative parameters, checks expected signs at their minima, and checks the divergence trend. These finite checks corroborate but do not replace the preceding proof.

## Relationship to prior work

Sun, Ye and Podgornik study finite-duration rests in a harmonic trap, but their run orientation is independently redrawn after each rest, so the sign-memory process and covariance sign laws here do not follow from their model without altering its transition kernel. Datta, Beta and Großmann treat intermittent active motion with general renewal laws and orientational memory, primarily deriving *unconfined* transport and displacement statistics; their general motility-correlation approach motivates the present Markov forcing calculation but does not state the harmonic-filtered negative-band count or its critical divergence. Basu and collaborators study a three-velocity harmonic-trap model with different jump transitions and stationary position density. Smith and collaborators study harmonic confinement with equally likely clockwise and counterclockwise quarter-turns, rather than the strictly directed cycle here. Standard linear-filter identities are used as established techniques, not claimed as discoveries. The contribution assessed here is the *complete sign-set classification* for the specific directed run–rest cycle, including the unique onset and infinite-band asymptotic law, not the elementary fact that linear filtering transforms spectra.

## Limitations

Only the precisely defined directed cyclic chain, equal transition rates, one-dimensional harmonic confinement and stationary preparation are covered. The theorem does not claim the same onset for unequal run/rest rates, independently redrawn orientations, thermal translational noise, or nonlinear traps. The argument does not prove publication priority; a broad previously published linear-filter positivity theorem may imply portions of the sign classification. Numerical onset digits are approximations, not a computer-assisted proof of uniqueness. An independent audit has not been performed.

## References

1. A. Sun, F. Ye, and R. Podgornik, *Exact moments for a run and tumble particle in a harmonic trap with a finite tumble time*, arXiv:2409.00578, first posted 2024-09-01. https://arxiv.org/abs/2409.00578
2. A. Datta, C. Beta, and R. Großmann, *The random walk of intermittently self-propelled particles*, arXiv:2406.15277, first posted 2024-06-21. https://arxiv.org/abs/2406.15277
3. U. Basu, S. N. Majumdar, A. Rosso, S. Sabhapandit, and G. Schehr, *Exact stationary state of a run-and-tumble particle with three internal states in a harmonic trap*, arXiv:1910.10083. https://arxiv.org/abs/1910.10083
4. N. R. Smith, P. Le Doussal, S. N. Majumdar, and G. Schehr, *Exact position distribution of a harmonically-confined run-and-tumble particle in two dimensions*, arXiv:2207.10445. https://arxiv.org/abs/2207.10445
