# Velocity-reversal universality under preferential position resetting

## Finding

Consider a one-dimensional active particle of speed \(v>0\), intrinsic tumbling rate \(\gamma>0\), and Poisson relocation rate \(r>0\). At each relocation time \(t\), its position is replaced by the position visited at an independently uniformly sampled time in \([0,t]\). Independently, the velocity sign is reversed with probability \(\eta\in[0,1]\); it is **never** copied from the sampled past time. Start at \(X_0=0\) with an independent fair initial velocity sign.

For every reversal probability \(\eta\in[0,1]\), the mixed position–orientation moment and mean-square position obey
\[
\lim_{t\to\infty}\mathbb E[X_t\sigma_t]
 =\frac{v}{2\gamma+r},\qquad
\mathbb E[X_t^2]
 =\frac{2v^2}{r(2\gamma+r)}\log(rt)+C_\eta+O(t^{-1}).
\]
Here \(C_\eta\) is a finite constant that can depend on the reversal protocol. **The coefficient of logarithmic spreading is independent of the velocity-reversal probability**, although the transient variance does depend on it:
\[
\mathbb E[X_t^2]
 =v^2t^2-v^2\left(\frac{2\gamma}{3}+\frac{7r}{18}+\frac{\eta r}{3}\right)t^3+O(t^4)
 \quad(t\downarrow0).
\]

These three exact population-level observables identify the three kinetic parameters when \(v\) is known. Set
\[
 m=\lim_{t\to\infty}\mathbb E[X_t\sigma_t],\quad
 L=\lim_{t\to\infty}\bigl(\mathbb E[X_{e t}^2]-\mathbb E[X_t^2]\bigr),\quad
 b=\lim_{t\downarrow0}\frac{v^2t^2-\mathbb E[X_t^2]}{v^2t^3}.
\]
The logarithmic-increment definition of \(L\) uses only observable moments and no unknown rate inside a logarithm. Then
\[
 r=\frac{2vm}{L},\qquad
 \gamma=\frac12\left(\frac vm-r\right),\qquad
 \eta=\frac3r\left(b-\frac{2\gamma}{3}-\frac{7r}{18}\right).
\]

For comparison, when each preferential relocation copies **both** the past position and past sign (the different model of Boyer and Majumdar), its established logarithmic mean-square coefficient is \(v^2/(\gamma r)\). At matched \(v,\gamma,r\), the present coefficient is smaller by the strict factor \(2\gamma/(2\gamma+r)\). Therefore the large-reset-rate behaviors are respectively of order \(r^{-2}\) and \(r^{-1}\).

## Assumptions and scope

Time is continuous, and all random event clocks, Bernoulli marks, and sampled historical times are independent except for the stated sharing of the relocation clock between position and sign updates. The intrinsic sign flips \(\sigma_t\in\{-1,+1\}\) at rate \(\gamma\). On intervals without instantaneous events, \(\dot X_t=v\sigma_t\). At a Poisson relocation event at time \(t>0\), first choose \(U_t\sim\operatorname{Unif}[0,t]\) independently of the past; set \(X_t=X_{U_t}\); then replace \(\sigma_t\) by \(-\sigma_{t-}\) with probability \(\eta\), otherwise leave it unchanged. Simultaneous events have probability zero. In particular, the reset sign is **not** \(\sigma_{U_t}\). The process exists pathwise because only finitely many events occur on bounded intervals. Its position satisfies \(|X_t|\le vt\) pathwise. Expectations are over both initial sign and all subsequent randomness. The symbols \(O(t^{-1})\) and \(O(t^4)\) have parameter-dependent constants, with parameters fixed throughout the relevant limit. The large-time limit is taken before any limit in \(r\), \(\gamma\), or \(\eta\).

## Proof

**1. An orientation correlation identity.** The sign process flips at the union of its intrinsic Poisson flip clock of rate \(\gamma\) and the thinned relocation marks that reverse it, of rate \(\eta r\). Its future increments are independent of the past filtration. Thus for \(0\le s\le t\),
\[
 \mathbb E[\sigma_t\mid\mathcal F_s]
 =e^{-\beta(t-s)}\sigma_s,\qquad \beta=2(\gamma+\eta r)>0.
\]
Global reflection of the initial sign and every ensuing sign gives \(\mathbb E[X_t]=0\) for every \(t\).

**2. A closed equation for the position–orientation moment.** Put \(M(t)=\mathbb E[X_t\sigma_t]\), \(J(t)=\int_0^t e^{-\beta(t-s)}M(s)\,ds\), and \(a=2\gamma+r\). Ordinary motion contributes \(v\) to \(M'\), intrinsic tumbling contributes \(-2\gamma M\), and a relocation replaces \(X_t\sigma_t\) in conditional expectation by
\[
 \frac{1-2\eta}{t}\int_0^t X_s\sigma_{t-}\,ds.
\]
By the preceding conditional-correlation identity, its expected value equals \((1-2\eta)J(t)/t\). Consequently, for \(t>0\),
\[
 M'=v-aM+\frac{r(1-2\eta)}tJ,\qquad
 J'=M-\beta J,\qquad M(0)=J(0)=0.
\]
The integral representation defines the apparent \(t=0\) singularity continuously.

To bound \(M\), use \(|1-2\eta|\le1\) and \(|J(t)|/t\le \sup_{s\le t}|M(s)|\). A first-crossing comparison at either boundary \(\pm v/(2\gamma)\) shows that \(|M(t)|\le v/(2\gamma)\) for every \(t\ge0\): at the upper boundary the right derivative is at most \(v-(2\gamma+r)v/(2\gamma)+rv/(2\gamma)=0\), whereas at the lower boundary it is strictly positive. Therefore \(|J(t)|\le v/(2\gamma\beta)\). With \(m=v/a\), variation of constants gives
\[
 M(t)-m=e^{-at}(M(0)-m)
 +r(1-2\eta)\int_0^t e^{-a(t-s)}\frac{J(s)}s\,ds.
\]
Here \(J(s)=O(s^2)\) as \(s\downarrow0\), and \(J\) is bounded globally; splitting the integral at \(t/2\) yields \(M(t)=m+O(t^{-1})\).

**3. Exact second-moment quadrature and logarithmic asymptotic.** Write \(V(t)=\mathbb E[X_t^2]\) and \(H(t)=\int_0^tV(s)\,ds\). The velocity-reversal mark does not change the new position, so the moment equation is
\[
 V'=2vM-rV+\frac r t H,\qquad H'=V,\qquad V(0)=H(0)=0.
\]
Define \(F(t)=2vM(t)\) and \(Y(t)=H(t)/t\). Since \(V=Y+tY'\), the last display is equivalent to
\[
 tY''+(2+rt)Y'=F(t),\qquad
 Y'(t)=\frac{e^{-rt}}{t^2}\int_0^t s e^{rs}F(s)\,ds.
\]
This is an exact finite-time quadrature, not an asymptotic approximation. Step 2 implies \(F(t)=F_\infty+O(t^{-1})\), with \(F_\infty=2v^2/(2\gamma+r)\). Integration by parts, or splitting the integral into its constant and \(O(s^{-1})\) terms, gives
\[
 Y'(t)=\frac{F_\infty}{rt}+O(t^{-2}),\quad
 Y(t)=\frac{F_\infty}{r}\log(rt)+C'+O(t^{-1}).
\]
Because \(V=Y+tY'\), the first asserted large-time law follows, with a finite \(C_\eta=C'+F_\infty/r\).

**4. Independent small-time event count.** The probability of two or more Poisson events up to time \(t\) is \(O(t^2)\), and the bound \(|X_t|\le vt\) makes their contribution \(O(t^4)\) to \(V\). With no event, \(X_t^2=v^2t^2\). With one intrinsic tumble at time \(s\), \(X_t=v\sigma_0(2s-t)\), producing the cubic change \(-2\gamma v^2t^3/3\). With one relocation at time \(s\) and recalled time \(U\) uniform on \([0,s]\), the final displacement is \(v\sigma_0(U+t-s)\) without a marked reversal, and \(v\sigma_0(U-t+s)\) with reversal. Integrating the squared-position difference from the no-event path over \(0<s<t\) and \(0<U<s\) gives respectively \(-7rv^2t^3/18\) and \(-13rv^2t^3/18\). Bernoulli averaging yields the displayed cubic coefficient \(2\gamma/3+7r/18+\eta r/3\).

**5. Identification and comparison.** The inversion formulas follow algebraically from the strictly positive \(m\) and \(L\) and the linear dependence of \(b\) on \(\eta\). In the history-copying model of Boyer and Majumdar, both the recalled position and sign are used at relocation, so its jump operator differs from Step 2; its known mean-square asymptotic is \(v^2\log(rt)/(\gamma r)\). The ratio of coefficients is exactly \(2\gamma/(2\gamma+r)\), strictly between zero and one. No claim about the other model's finite-time moments is needed.

## Verification

A standalone \(\texttt{CHECK.py}\) accompanies this result. It checks the independent one-event path integrals using exact rational arithmetic; numerically solves the closed four-dimensional moment system for five reversal probabilities; verifies the exactly soluble \(\eta=1/2\) mixed-moment formula; compares late logarithmic increments and the early cubic expansion; and uses seeded event-by-event path simulation to check the moment equations independently. The packaged checker passes **78 assertions**. These finite checks are supporting tests; the global quantifiers and asymptotic limits are proved in Steps 1–5.

## Relationship to prior work

Evans and Majumdar (arXiv:1808.06450, first posted 2018-08-20) introduced arbitrary probability of reversing the velocity during resetting of a run-and-tumble particle, but the position always returns to a **fixed site**, yielding a stationary spatial law. Boyer and Majumdar (arXiv:2312.13439, first posted 2023-12-20) replaced fixed-site resetting with uniform-time historical relocation and derived the Fourier law and logarithmic variance when **both position and velocity are copied from the sampled past state**. The present model instead uses historical **position-only** relocation and a local Bernoulli velocity reversal, for which neither prior jump operator gives the displayed mixed-moment equation or logarithmic coefficient by parameter substitution. Mailler and Uribe Bravo (arXiv:1810.02735) proved broad preferential-relocation limit theorems for complete state relocation followed by a Markov run, but their model does not directly implement the partial state update studied here. These works motivate the comparison but are not re-presented as new results.

## Limitations

The result concerns exact population moments for fixed \(v,\gamma,r>0\), initial position zero and an independent fair initial sign. It does not establish a full position-density limit theorem, a long-time central limit theorem, first-passage formulas, or statistical guarantees for finite observations. The initial cubic observation needed to identify \(\eta\) presupposes access to an ideal short-time expansion. The logarithmic coefficient cannot distinguish the reversal probabilities by itself. The priority comparison is limited to the specified literature and searches; equivalent formulations elsewhere remain possible, and no independent scientific audit has been performed.

## References

1. M. R. Evans and S. N. Majumdar, *Run and tumble particle under resetting: a renewal approach*, arXiv:1808.06450 (initial public version 2018-08-20), Journal of Physics A 51, 475003 (2018). https://arxiv.org/abs/1808.06450
2. D. Boyer and S. N. Majumdar, *Active particle in one dimension subjected to resetting with memory*, arXiv:2312.13439 (initial public version 2023-12-20), Physical Review E 109, 054105 (2024). https://arxiv.org/abs/2312.13439
3. C. Mailler and G. Uribe Bravo, *Random walks with preferential relocations and fading memory: a study through random recursive trees*, arXiv:1810.02735 (initial public version 2018-10-05). https://arxiv.org/abs/1810.02735
