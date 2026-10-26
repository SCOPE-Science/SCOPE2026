# Phase-resolved critical extinction under staggered ecological pulses

## Finding

A two-population competitive Lotka–Volterra system may have an exactly zero invasion exponent after periodic density-independent pulses. In the weak-competition regime, that equality is nevertheless a **global extinction threshold**. The vanishing population has a universal inverse-time law with an explicitly computable **phase-dependent envelope**. In particular, changing when species receive their pulses can change the leading extinction amplitude without changing either species' per-period pulse product or the zero-invasion condition.

Precisely, with the definitions below, every strictly positive trajectory satisfies
\[
\lim_{t\to\infty}x(t)=0,\qquad
\lim_{t\to\infty}\bigl(y(t)-y_*(t)\bigr)=0,\qquad
\lim_{t\to\infty}\left[t\,x(t)-\frac{P(t)}{\kappa\overline P}\right]=0.
\]
The limits use post-pulse, right-continuous values. There is no positive periodic coexistence orbit under the hypotheses.

## Assumptions and scope

Fix \(T>0\), coefficients \(b,c,e,f>0\), and bounded piecewise-continuous \(T\)-periodic functions \(a,d:\mathbb R\to\mathbb R\). In each period fix phases \(0<\theta_1<\cdots<\theta_m<T\), \(m\ge0\), and pulse multipliers \(\alpha_j,\beta_j>0\). Solutions are positive and right-continuous, starting at \(x(0),y(0)>0\), evolving between pulses by
\[
\dot x=x\bigl(a(t)-b x-c y\bigr),\qquad
\dot y=y\bigl(d(t)-e x-f y\bigr),
\]
with \((x^+,y^+)=(\alpha_j x^-,\beta_j y^-)\) at \(\theta_j+kT\), for every integer \(k\ge0\). Multipliers equal to one permit species-specific staggered interventions. Identical pulses at one phase are represented by one pair.

Set
\[
q=\frac{c}{f}>0,\qquad
\kappa=b-qe=\frac{bf-ce}{f}>0,
\]
\[
\Gamma_y=\int_0^T d(s)\,ds+\sum_{j=1}^m\log\beta_j>0,\qquad
\Gamma_x=\int_0^T a(s)\,ds+\sum_{j=1}^m\log\alpha_j=q\Gamma_y.
\]
The strict inequality \(\kappa>0\) is a weak-competition condition. No sign restriction is imposed on the instantaneous intrinsic rates \(a(t)\) and \(d(t)\); only their boundedness and the specified average conditions are needed.

Define \(\Phi(0)=1\) by \(\dot\Phi=(a-qd)\Phi\) between pulses and \(\Phi(\theta_j^+)=(\alpha_j/\beta_j^q)\Phi(\theta_j^-)\). Because \(\Gamma_x-q\Gamma_y=0\), its period multiplier equals one, so \(\Phi\) is a positive, bounded, bounded-away-from-zero, \(T\)-periodic right-continuous function.

Let \(y_*(t)>0\) be the unique periodic solution of the scalar resident equation \(\dot y_*=y_*(d(t)-f y_*)\) with pulses \(y_*^+=\beta_j y_*^-\), and define
\[
P(t)=\Phi(t)y_*(t)^q,\qquad
\overline P=\frac1T\int_0^T P(s)\,ds>0.
\]
The theorem states that the displayed three limits hold for **every** pair \(x(0),y(0)>0\), without a small-invader hypothesis. Equivalently, for each phase \(s\in[0,T)\),
\[
\lim_{k\to\infty}k\,x(kT+s)=\frac{P(s)}{\kappa\int_0^T P(u)\,du}.
\]

## Proof

**1. Global boundedness and the resident cycle.** Comparison with scalar self-limited impulsive logistic equations gives global positive solutions and bounds uniform in forward time. To see the bound explicitly, replace \(a(t)\) by its finite supremum and drop the nonpositive cross term from the first equation (and similarly for \(y\)); the reciprocal of each upper comparison solution evolves affinely and positively over every period. Its positive forcing term gives a uniform positive lower bound on reciprocal states after a finite number of periods, even when pulses amplify rather than diminish densities.

For the resident equation, \(u=1/y_*\) solves \(u'=-d(t)u+f\) between pulses and \(u^+=u^-/\beta_j\). Its positive one-period affine return map is \(u(T)=e^{-\Gamma_y}u(0)+J\) with \(J>0\). Since \(0<e^{-\Gamma_y}<1\), there is a unique positive fixed point and every positive resident trajectory converges to it at corresponding phases. The same construction works with \(d\) replaced by \(d-\varepsilon\) when \(0<\varepsilon<\Gamma_y/T\), and those periodic fixed points converge to \(y_*\) as \(\varepsilon\downarrow0\).

**2. An exact normalization, including every pulse.** Define \(R=x/y^q\). Between pulses,
\[
\frac{d}{dt}\log R=a(t)-q d(t)-(b-qe)x=a(t)-q d(t)-\kappa x.
\]
At each pulse, \(R^+/R^-=\alpha_j/\beta_j^q\), exactly the jump of \(\Phi\). Thus \(Z=R/\Phi\) is continuous across all pulses and \(Z'=-\kappa\Phi y^q Z^2\) between them. Integration yields the **global exact identity**
\[
\boxed{\displaystyle
\frac{x(t)}{y(t)^q}=\frac{\Phi(t)}{R(0)^{-1}+\kappa\int_0^t\Phi(s)y(s)^q\,ds}.}
\]
Set \(I(t)=\int_0^t\Phi(s)y(s)^q\,ds\). The formula and positivity imply \(0<R(t)\le R(0)\sup\Phi\) uniformly for all time.

**3. The denominator diverges.** Suppose \(I(\infty)<\infty\). Since periodic \(\Phi\) is bounded below, \(\int_0^\infty y(t)^qdt<\infty\). On every interval of length \(T\), the bounded densities and growth functions and the finitely many fixed positive pulse multipliers give a uniform bound on the absolute logarithmic change of \(y\). Consequently the maximum and minimum values of \(y\) in one period are uniformly comparable by a fixed factor. The vanishing integral over successive periods forces \(y(t)\to0\), uniformly in each period. Since \(x=R y^q\) and \(R\) is bounded, also \(x(t)\to0\). However the exact log-growth balance for the resident is
\[
\log\frac{y((k+1)T)}{y(kT)}
=\Gamma_y-\int_{kT}^{(k+1)T}(e x(t)+f y(t))\,dt.
\]
The integral tends to zero, so the right side is eventually greater than \(\Gamma_y/2>0\). Then \(y(kT)\) grows geometrically, contradicting the established decay and boundedness. Hence \(I(t)\to\infty\) and the exact identity gives \(R(t)\to0\). As \(y\) is bounded, \(x(t)\to0\).

**4. Resident convergence.** For every sufficiently small \(\varepsilon>0\), eventually \(0\le e x(t)<\varepsilon\), so the second equation lies between the scalar pulsed logistic flows with intrinsic rates \(d-\varepsilon\) and \(d\). Scalar order comparison survives the identical \(\beta_j\) pulses; their unique attracting positive cycles squeeze the lower and upper long-time limits of \(y(t)\). By continuity of the reciprocal fixed point as \(\varepsilon\downarrow0\), this implies \(y(t)-y_*(t)\to0\), uniformly over a full period, including right-continuous pulse phases.

**5. Exact critical amplitude.** The convergence in Step 4 implies \(\Phi(t)y(t)^q-P(t)\to0\). Since \(P\) is periodic and integrable,
\[
\lim_{t\to\infty}\frac{I(t)}t=\frac1T\int_0^T P(s)\,ds=\overline P>0.
\]
Multiplying the identity in Step 2 by \(t y(t)^q\) proves \(t x(t)-P(t)/(\kappa\overline P)\to0\). If a strictly positive coexistence cycle existed, \(Z^{-1}\) would increase by \(\kappa\int_0^T\Phi y^q>0\) every period despite \(Z\) being periodic, a contradiction. This establishes all statements.

## Verification

A standalone Python standard-library program, `verify_pulse_critical.py`, reproduces a two-phase explicit example, checks the reciprocal-logistic resident solution, numerically confirms the exact normalized-ratio identity, and compares the predicted asymptotic amplitudes with fourth-order Runge–Kutta trajectories over 3,000 periods. The program was executed successfully and its output showed the analytic phase-separated predictions to within one percent. These finite numerical tests are **not** used as proofs of the all-parameter assertion.

Here is an exact example with \(T=1\), constant \(a=d=1\), \((b,c,e,f)=(2,1,1,1)\), and a single resident pulse \(\beta=1/2\) at phase \(1/4\). Species \(x\) has the same pulse factor \(\alpha=1/2\), either also at \(1/4\) or instead at \(3/4\). Then \(q=\kappa=1\), \(\Gamma_x=\Gamma_y=1-\log2>0\), and
\[
y_*(0)=\left(1+\frac{e^{-3/4}}{1-2e^{-1}}\right)^{-1}=0.358727078574\ldots.
\]
The resident period integral is \(A=\int_0^1 y_*(s)\,ds=1-\log2\). Let \(B=\int_{1/4}^{3/4}y_*(s)\,ds=0.127152604678\ldots>0\). Coincident pulses give \(\Phi\equiv1\), hence
\[
\lim_{k\to\infty}k x(k)=\frac{y_*(0)}{A}=1.169052574549\ldots.
\]
Staggering the \(x\) pulse to \(3/4\) instead gives \(\Phi=2\) on \((1/4,3/4)\) and \(\Phi=1\) otherwise, hence
\[
\lim_{k\to\infty}k x(k)=\frac{y_*(0)}{A+B}=0.826549758689\ldots.
\]
The pulse products and critical invasion exponent are identical, yet the leading critical abundance differs. All numerical constants follow from elementary exponential/logarithmic logistic-flow formulas.

## Relationship to prior work

Courcelle, MacDonald, and Patel (arXiv:2609.09343, first posted 8 September 2026) establish permanence criteria for periodically pulsed Lotka–Volterra populations and analyze two-species competition under strict invasion inequalities. Their treated comparisons do not state the global inverse-time decay law **at equality**, its explicit periodic envelope, or the pulse-offset contrast. Schreiber (arXiv:2507.02157) develops invasion-rate methods for general flow-kick systems and obtains permanence and extinction conclusions under sign and structural hypotheses, without an explicit globally attracting critical \(t^{-1}\) amplitude in this model. The earlier impulsive competition paper by Jin, Han, and Li (DOI below) was identifiable through its abstract, but its complete text was not accessible for a conclusive full-document exclusion of overlap. The present theorem addresses the degenerate invasion-exponent boundary rather than permanence under strict positivity.

## Limitations

The theorem requires exactly two positive populations, constant interaction coefficients with \(bf>ce\), a viable resident cycle, a finite repeatable schedule of positive density-independent pulses, and exact zero invasion exponent. It does not establish behavior for \(bf\le ce\), nonlinear or state-triggered kicks, nonperiodic environments, or stochastic disturbances. The inaccessible complete text of a relevant older impulsive-competition article leaves residual publication-priority uncertainty. The numerical program checks one concrete family and does not independently certify the infinite-time argument.

## References

1. E. Courcelle, J. S. MacDonald, and S. Patel. *Persistence of n-Species Lotka–Volterra Models with Periodic Pulses*. arXiv:2609.09343 (first public version 8 September 2026), especially the permanence results and two-species examples.
2. S. J. Schreiber. *Coexistence and Extinction in Flow-Kick Systems: An Invasion Growth Rate Approach*. arXiv:2507.02157 (first public version 2 July 2025), sections on Lotka–Volterra disturbances, invasion growth rates, permanence, and extinction.
3. Z. Jin, M. Han, and G. Li. *The persistence in a Lotka–Volterra competition systems with impulsive*. *Chaos, Solitons & Fractals*, DOI:10.1016/j.chaos.2004.09.065 (abstract available; complete text not inspected).
