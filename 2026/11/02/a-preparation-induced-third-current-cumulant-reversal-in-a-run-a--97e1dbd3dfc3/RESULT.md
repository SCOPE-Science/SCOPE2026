# A preparation-induced third-current-cumulant reversal in a run-and-tumble gas

## Finding

For a one-dimensional gas of independent run-and-tumble particles initially distributed with macroscopic density \(\rho>0\) on the negative half-line, speed \(v>0\), direction-flip rate \(\gamma>0\), and independent equally likely initial orientations, there is a qualitative distinction between two standard quenched-density preparations.

Let \(\kappa_{3,qq}(t)\) denote the disorder-averaged third cumulant when **both** the initial positions and orientations are held fixed before averaging the particle dynamics (quenched density, quenched magnetization). Let \(\kappa_{3,qa}(t)\) denote the corresponding quenched-density third cumulant when initial orientations are first averaged independently (annealed magnetization). Then, **for every \(t>0\)**,

\[
\boxed{\kappa_{3,qq}(t)<\kappa_{3,qa}(t),\qquad \kappa_{3,qa}(t)>0.}
\]

At short times,
\[
\boxed{\begin{aligned}
\kappa_{3,qq}(t)&=-\frac{\rho v\gamma}{4}t^2+O(\rho v\gamma^2t^3),\\
\kappa_{3,qa}(t)&=\frac{\rho v\gamma}{8}t^2+O(\rho v\gamma^2t^3).
\end{aligned}}
\]

Writing \(D=v^2/(2\gamma)\), both quantities have the same *strictly positive* long-time leading behavior,
\[
\boxed{\kappa_{3,qq}(t)\sim\kappa_{3,qa}(t)\sim2\rho\sqrt{Dt}\,C_3,\quad
C_3=\frac1{\sqrt\pi}\left[\frac{3\sqrt2}{2\pi}\arctan\left(\frac1{\sqrt2}\right)-\frac14\right]>0.}
\]

In particular, \(\kappa_{3,qq}\) is negative for all sufficiently small positive times, positive for all sufficiently large times, and continuous: **at least one finite-time sign reversal occurs**. No uniqueness of its zero is claimed. Annealing the initial magnetization eliminates this negative-skewness regime altogether.

## Assumptions and scope

A particle initially at \(-z\), for \(z\ge0\), follows \(X_t=-z+v\int_0^t S_u\,du\). The continuous-time two-state Markov chain \(S_u\in\{-1,+1\}\) flips sign at independent rate \(\gamma>0\). Particles move independently. First take \(N\) iid initial positions uniformly distributed on \([-L,0]\), independent initial signs with probabilities \(1/2,1/2\), and independent trajectories; then take \(L,N\to\infty\) with \(N/L\to\rho>0\). The integrated net origin current \(Q_t\) equals the number of particles lying to the right at time \(t\). This limit is the standard step-density thermodynamic limit.

Write \(U_\pm(z,t)=\mathbb P(\int_0^t v S_u\,du>z\mid S_0=\pm1)\) and \(m=(U_++U_-)/2\). The *quenched* cumulants are defined via third derivatives at \(s=0\) of the disorder-averaged conditional log moment-generating functions, not as unconditional cumulants after mixing quenched disorder:
\[
K_{qq}(s,t)=\rho\int_0^\infty\frac{\log[1+U_+(z,t)(e^s-1)]+\log[1+U_-(z,t)(e^s-1)]}{2}\,dz,
\]
\[
K_{qa}(s,t)=\rho\int_0^\infty\log[1+m(z,t)(e^s-1)]\,dz,
\qquad \kappa_{3,ij}=\partial_s^3 K_{ij}(0,t).
\]

Both integrals vanish beyond \(z=vt\). The quenched orientation convention is the disorder-average of conditional log generating functions, as in Jose--Rosso--Ramola; reversing the order of averaging and taking a logarithm describes a different preparation.

## Proof

**1. Third cumulants and the all-time ordering.** For a Bernoulli success probability \(p\), its third cumulant is \(b_3(p)=p(1-p)(1-2p)=p-3p^2+2p^3\). Differentiating the exact log-generating functions gives
\[
\kappa_{3,qq}(t)=\frac\rho2\int_0^\infty[b_3(U_+)+b_3(U_-)]\,dz,
\qquad \kappa_{3,qa}(t)=\rho\int_0^\infty b_3(m)\,dz.
\]

The unbiased initial sign makes the displacement law symmetric, so for every \(0<z<vt\), \(0<m(z,t)<1/2\), and hence \(b_3(m)>0\). Writing \(d=(U_+-U_-)/2\), the polynomial identity
\[
\frac{b_3(m+d)+b_3(m-d)}2-b_3(m)=3(2m-1)d^2
\]
shows that
\[
\boxed{\kappa_{3,qa}-\kappa_{3,qq}=\frac{3\rho}{4}\int_0^{vt}(1-2m)(U_+-U_-)^2\,dz>0.}
\]

The strictness follows because the no-flip atom of weight \(e^{-\gamma t}\) in the \(+\)-oriented displacement lies at \(+vt\), while the \(-\)-oriented displacement has its no-flip atom at \(-vt\). Thus the two crossing probabilities differ on a nonempty interval just below \(z=vt\). The continuous component from at least one flip makes \(m<1/2\) on \(0<z<vt\).

**2. Short time.** Put \(z=vty\), \(0<y<1\). A single direction flip, conditioned on its time, yields uniformly in \(0\le y<1\) (with endpoint values understood by one-sided limits)
\[
U_+(vty,t)=1-\frac{\gamma t}{2}(1+y)+O((\gamma t)^2),\qquad
U_-(vty,t)=\frac{\gamma t}{2}(1-y)+O((\gamma t)^2).
\]

These follow from the zero-flip probabilities and the crossing conditions for one flip; two or more flips have total probability \(O((\gamma t)^2)\), uniformly in \(y\). Consequently,
\[
b_3(U_+)=-\frac{\gamma t}{2}(1+y)+O((\gamma t)^2),\quad
b_3(U_-)=\frac{\gamma t}{2}(1-y)+O((\gamma t)^2).
\]

Their averaged integral gives \(\kappa_{3,qq}=-\rho v\gamma t^2/4+O(\rho v\gamma^2t^3)\). Also \(m(vty,t)=1/2-\gamma ty/2+O((\gamma t)^2)\) and \(b_3(m)=\gamma ty/4+O((\gamma t)^2)\), giving \(\kappa_{3,qa}=\rho v\gamma t^2/8+O(\rho v\gamma^2t^3)\).

**3. Long time.** Let \(M_t=S_t-S_0+2\gamma\int_0^t S_u\,du\). This is a bounded-jump martingale whose predictable quadratic variation is \(4\gamma t\). Its martingale central limit theorem, since jumps are bounded, gives for *either* fixed initial sign
\[
\frac{v\int_0^tS_u\,du}{\sqrt{2Dt}}\Longrightarrow N(0,1),\quad D=\frac{v^2}{2\gamma}.
\]

A standard bounded-jump martingale fourth-moment inequality gives \(\mathbb E|M_t|^4=O(1+t^2)\). Because \(S_t-S_0\) is bounded, the scaled positive displacements are uniformly integrable, with uniformly small integrated tails. Hence for \(z=2\sqrt{Dt}\,y\), the crossing probabilities converge for almost every fixed \(y>0\) to \(p(y)=\operatorname{erfc}(y)/2\). Since \(|b_3(p)|\le p\) for \(p\in[0,1]\), uniform integrability permits the spatial integral limit:
\[
\lim_{t\to\infty}\frac{\kappa_{3,qq}(t)}{2\rho\sqrt{Dt}}
=\lim_{t\to\infty}\frac{\kappa_{3,qa}(t)}{2\rho\sqrt{Dt}}
=\int_0^\infty p(y)(1-p(y))(1-2p(y))\,dy=:C_3>0.
\]

For exact evaluation, define \(I_k=\int_0^\infty\operatorname{erfc}(y)^k\,dy\). Integration by parts and \(\int_0^\infty e^{-ay^2}\operatorname{erf}(by)\,dy=\arctan(b/\sqrt a)/(\sqrt{\pi a})\) give
\[
I_1=\frac1{\sqrt\pi},\quad I_2=\frac2{\sqrt\pi}(1-2^{-1/2}),\quad
I_3=\frac{3-3\sqrt2+(6\sqrt2/\pi)\arctan(1/\sqrt2)}{\sqrt\pi}.
\]

Substitution into \(C_3=I_1/2-3I_2/4+I_3/4\) proves the displayed constant. Positivity also follows directly from the integral because \(0<p(y)<1/2\) for \(y>0\). Continuity in \(t>0\) follows from the jump-process transition kernel and bounded spatial support on compact time intervals, completing the existence-of-sign-reversal conclusion.

## Verification

The standalone program `verify.py` computes crossing probabilities in two independent ways: conditioning on the Poisson flip count gives beta-distributed orientation occupation fractions, while integrating the explicit Bessel-function telegraph propagator gives a separate representation. It also integrates the Bernoulli third-cumulant polynomials and tests the all-time algebraic identity, the two short-time coefficients, and the evaluated Gaussian asymptotic constant. Run with `python verify.py` using Python 3, NumPy and SciPy. The numerical sign crossing near \(\gamma t\approx0.6703493\) is **illustrative only**; uniqueness and an exact zero location are neither proved nor claimed.

## Relationship to prior work

Banerjee--Majumdar--Rosso--Schehr [1] derived the current statistics for noninteracting run-and-tumble gases with annealed and quenched **position** disorder. Jose--Rosso--Ramola [2] introduced the four density/magnetization annealing choices and provided their generating functions and **second-cumulant** formulas for initially unbiased orientations. Their extended paper [3] treats arbitrary initial orientation bias and likewise focuses on the **variance**. All underlying particle propagators, cumulant generating functions and second-cumulant results are prior work. The distinct evaluated result here is a third-cumulant sign reversal *under simultaneous density/magnetization quenching*, an all-time strict preparation-ordering identity, and their sharp short-/long-time coefficients. Existing complete generating functions determine these quantities in principle; this theorem extracts new qualitative consequences rather than claiming a new generating function.

## Limitations

The result applies to independent constant-speed Markov velocity reversals with unbiased initial magnetization in the infinite-volume step-density limit and to the stated disorder-averaged conditional cumulants. It is not a statement about the unconditional current cumulant after mixing initial conditions; it does not prove a unique crossing, give the precise crossing time, treat interactions or finite populations, or provide a finite-sample inference guarantee. Definitive priority relative to all existing literature has not been independently determined.

## References

[1] T. Banerjee, S. N. Majumdar, A. Rosso and G. Schehr, *Current fluctuations in non-interacting run-and-tumble particles in one-dimension*, arXiv:2001.01923 (first public 2020-01-07); Phys. Rev. E 101, 052101 (2020). https://arxiv.org/abs/2001.01923

[2] S. Jose, A. Rosso and K. Ramola, *Generalized disorder averages and current fluctuations in run and tumble particles*, arXiv:2306.13613 (first public 2023-06-23); Phys. Rev. E 108, L052601 (2023). https://arxiv.org/abs/2306.13613

[3] S. Jose, A. Rosso and K. Ramola, *Effect of initial conditions on current fluctuations in non-interacting active particles*, arXiv:2310.16811 (first public 2023-10-25); J. Phys. A 57, 285002 (2024). https://arxiv.org/abs/2310.16811
