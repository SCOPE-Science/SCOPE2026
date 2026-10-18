# Memoryless Sadam: a sharp softplus flip boundary and its exceptional terminating orbits

## Finding

Consider the scalar positive quadratic \(f(x)=\lambda x^2/2\) with \(\lambda>0\), positive fixed base step \(\eta\), and the Sadam recurrence of Tong, Liang, and Bi with its explicitly admissible memoryless parameters \(\beta_1=\beta_2=0\) and positive calibration parameter \(\beta\). Set
\[
L(u)=\log(1+e^u),\qquad a=\eta\beta\lambda,\qquad u_t=\beta\lambda|x_t|.
\]
The exact iterate is
\[
\boxed{x_{t+1}=x_t\bigl(1-a/L(u_t)\bigr).}\tag{1}
\]

**Global convergence and its two exceptional cases.** For \(0<a\le2\log2\), **every** initial value converges to zero. An orbit started at \(x_0\ne0\) can reach zero in finitely many steps precisely when a nonzero iterate has magnitude
\[
\boxed{\beta\lambda|x_t|=u_{\rm hit}:=\log(e^a-1),}\tag{2}
\]
which is possible only if \(a>\log2\). Once this happens, the orbit is identically zero thereafter. Thus any asymptotic *quotient* or *nonzero decay constant* below is asserted only for initial conditions whose orbits do **not** terminate in finite time.

For \(0<a<2\log2\), every nonterminating orbit satisfies
\[
\boxed{\lim_{t\to\infty}\frac{x_{t+1}}{x_t}=1-\frac{a}{\log2}.}\tag{3}
\]
At the internal resonance \(a=\log2\), every orbit started away from zero is nonterminating and converges locally quadratically, with
\[
\boxed{\lim_{t\to\infty}\frac{|x_{t+1}|}{|x_t|^2}=\frac{\beta\lambda}{2\log2}.}\tag{4}
\]
At \(a=2\log2\), a nonterminating orbit eventually alternates sign and obeys
\[
\boxed{\lim_{t\to\infty}t|x_t|=\frac{\log2}{\beta\lambda},\qquad
\lim_{t\to\infty}t^2f(x_t)=\frac{(\log2)^2}{2\beta^2\lambda}.}\tag{5}
\]
A terminating orbit at this critical parameter instead has both limits zero and no eventual alternating signs; consequently the nonzero constants in (5) cannot be asserted for *every* nonzero initial condition.

For \(a>2\log2\), the minimizer is linearly unstable, and there is exactly one nonzero symmetric two-cycle \(\{x_*,-x_*\}\), where
\[
\boxed{\beta\lambda|x_*|=\log(e^{a/2}-1).}\tag{6}
\]
That two-cycle is locally attracting. No global basin assertion is made.

The threshold \(\eta\beta\lambda=2\log2\) therefore separates global convergence to the optimizer from linear instability in the memoryless scalar model. The distinct internal value \(\eta\beta\lambda=\log2\) cancels the linear term. The exact finite-termination qualification is essential at both subcritical and critical parameters.

## Assumptions and scope

Equation (1) is the uncorrected-for-bias memoryless specialization of the source's Sadam algorithm: with \(\beta_1=\beta_2=0\), one has \(m_t=g_t=\lambda x_t\) and \(v_t=g_t^2\), and the source replaces \(\sqrt{v_t}\) by \(\beta^{-1}\log(1+e^{\beta\sqrt{v_t}})\). The source permits \(0\le\beta_1,\beta_2<1\). The result concerns a deterministic scalar quadratic and a fixed positive step; it does not establish a corresponding threshold for nonzero memory, stochastic gradients, multidimensional coupling, bias-corrected variants, or real-world training.

An orbit is **terminating** if some iterate equals zero exactly; it is **nonterminating** otherwise. Starting at \(x_0=0\) always yields the zero orbit. For a nonzero starting point, (2) characterizes the first possible zero hit; its nonzero right-hand side exists exactly for \(a>\log2\). Since the scalar map can map a nonzero state to zero, finite-time termination must not be tacitly excluded from statements about all initial values.

## Proof

With the stated specialization, \(g_t=\lambda x_t\), \(m_t=g_t\), and \(\sqrt{v_t}=|g_t|\); substitution into the Sadam softplus denominator immediately gives (1). The function \(L\) is strictly increasing on \([0,\infty)\), with \(L(0)=\log2\) and range \([\log2,\infty)\).

**Global convergence.** For \(0<a\le2\log2\) and any \(u>0\),
\[
0<\frac a{L(u)}<2,
\]
so \(|x_{t+1}|<|x_t|\) for nonzero \(x_t\). Magnitudes decrease to a limit \(\ell\ge0\). If \(\ell>0\), continuity makes the strict contraction multiplier uniformly smaller than one near \(\ell\), contradicting convergence to a positive limit. Thus \(x_t\to0\). Zero is fixed, so the conclusion holds also for terminating or initially zero orbits.

**Exact zero-hit criterion.** For \(x_t\ne0\), equation (1) yields \(x_{t+1}=0\) if and only if \(L(u_t)=a\). The range and strict monotonicity of \(L\) show that there is a *positive* solution if and only if \(a>\log2\), uniquely given by \(u_{\rm hit}=\log(e^a-1)\). This proves (2). In particular at \(a=2\log2\), choosing \(\beta\lambda|x_0|=\log3\) makes \(L(u_0)=\log4=2\log2\), so \(x_1=0\). Likewise \(a=\log3\) and \(\beta\lambda|x_0|=\log2\) give \(x_1=0\) in the strict subcritical regime. These are exact counterexamples to unqualified nonzero asymptotic laws; no continuity convention can define the quotient \(x_{t+1}/x_t\) once both numerator and denominator vanish.

**Ordinary and resonant asymptotics.** For a nonterminating orbit, \(x_t\ne0\) at every time and \(u_t\to0\). Taking the limit of its multiplier in (1) gives (3). The expansion
\[
L(u)=\log2+u/2+u^2/8+O(u^3)
\]
implies at \(a=\log2\) that \(1-a/L(u)=u/(2\log2)+O(u^2)\). Substituting \(u=\beta\lambda|x|\) proves (4). At this value of \(a\), the zero-hit criterion excludes finite termination for every nonzero initial state.

**Critical behavior.** Put \(a=2\log2\) and restrict to a nonterminating orbit. Since \(u_t\to0\), its signed multiplier is eventually strictly negative, and signs alternate. Its magnitude satisfies
\[
u_{t+1}=u_t\bigl(2\log2/L(u_t)-1\bigr)
=u_t-u_t^2/\log2+O(u_t^3).
\]
The expression in parentheses is positive for all sufficiently small \(u_t>0\); thus the reciprocal difference is
\[
\frac1{u_{t+1}}-\frac1{u_t}=\frac1{\log2}+O(u_t).
\]
Summing these increments and dividing by \(t\) gives \(1/(tu_t)\to1/\log2\) by Cesàro convergence, hence \(t u_t\to\log2\). Replacing \(u_t\) by \(\beta\lambda|x_t|\) and substituting into \(f\) proves both limits in (5).

**Supercritical two-cycle and attraction.** When \(a>2\log2\), the derivative of the map (1) at zero is \(1-a/\log2<-1\), proving local linear instability. A nonzero symmetric two-cycle is characterized by the multiplier \(-1\), or \(L(u_*)=a/2\). Since \(a/2>\log2\), this has exactly one positive solution, (6). With \(q=a/2\), \(p=1-e^{-q}\), and \(u_*=\log(e^q-1)=q+\log(1-e^{-q})\), the derivative of the signed map at either cycle point is
\[
d=-1+\frac{4u_*p}{a}.
\]
Here \(0<u_*<q=a/2\) and \(0<p<1\), so \(0<4u_*p/a<2\). Thus \(|d|<1\), and the two-step multiplier \(d^2<1\) proves local attraction. The proof does not attempt to describe all supercritical initial conditions.

## Verification and boundaries

The derivation of (1), monotone convergence, expansion, and multiplier estimate are analytical for the complete stated parameter ranges, not extrapolations from simulation. The exact substitutions \(a=2\log2,\ u_0=\log3\) and \(a=\log3,\ u_0=\log2\) exhibit the exceptional zero-hit orbits and explain the necessary correction of the universal asymptotic language. For nonterminating critical orbits, numerical evaluation can check the coefficient \(tu_t\to\log2\), but the all-time limit follows from the reciprocal-increment proof. The original included `verify.py` is a finite analytical/iteration guard; its successful execution alone is not a substitute for the quantified exception.

## Relationship to prior work and limitations

Tong, Liang, and Bi introduce Sadam through a softplus calibration of Adam's second-moment denominator and discuss parameter-dependent effective learning rates, convergence results and practical optimization. Those definitions and results are prior work. The precise memoryless scalar flip threshold, second-order cancellation, critical inverse-time law for nonterminating orbits, and explicit locally attracting symmetric two-cycle are not asserted to follow from the source's general convergence estimates. The relevant structural mechanism is the source's calibration parameter controlling a real change in discrete optimizer dynamics. Standard one-dimensional fixed-point and flip calculations are used as tools, not claimed as new general dynamical-systems theorems. It remains possible that a different account of normalized-gradient or softplus recurrences contains an equivalent scalar map, and the narrow memoryless model is not a prediction for arbitrary implementation settings.

## References

1. Q. Tong, G. Liang, and J. Bi, *Calibrating the Adaptive Learning Rate to Improve Convergence of ADAM*, arXiv:1908.00700 (2019).
2. Q. Tong, G. Liang, and J. Bi, *Calibrating the adaptive learning rate to improve convergence of ADAM*, Neurocomputing 481 (2022), 333–356, DOI:10.1016/j.neucom.2022.01.014.
