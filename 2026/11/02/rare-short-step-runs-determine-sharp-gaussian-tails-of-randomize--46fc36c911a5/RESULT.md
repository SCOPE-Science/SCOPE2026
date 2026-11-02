# Rare short-step runs determine sharp Gaussian tails of randomized backward Euler–Maruyama

## Finding

Consider the Ornstein–Uhlenbeck equation
\[
 dX_t=-\lambda X_t\,dt+\sigma\,dW_t,
 \qquad \lambda>0,\quad\sigma>0,
\]
and the backward Euler–Maruyama recursion with independent random positive step lengths
\[
 X_{n+1}=\frac{X_n+\sigma\sqrt{H_n}\,Z_{n+1}}{1+\lambda H_n},
 \qquad
 \Pr(H_n=a)=\rho,\quad\Pr(H_n=b)=1-\rho,
\]
where \(0<a<b\), \(0<\rho<1\), and the \(Z_n\) are independent standard normals, independent of the steps. The recursion has a unique stationary update-index law \(\pi\). Define
\[
 v_h=\frac{\sigma^2}{\lambda(2+\lambda h)},
 \qquad
 \alpha=(1+\lambda a)^{-2},
 \qquad
 \kappa=\frac{\log(1/\rho)}{\log(1/\alpha)}.
\]
Then \(\alpha\in(0,1)\), \(\kappa>0\), and the **two-sided sharp tail law** is
\[
 \boxed{\displaystyle
  \Pr_{\pi}(X>t)=\Pr_{\pi}(X<-t)
  \asymp t^{-(1+2\kappa)}
  \exp\!\left(-\frac{t^2}{2v_a}\right)
  \qquad(t\to\infty).}
\]
Here \(F(t)\asymp G(t)\) means that their ratio lies between two strictly positive finite constants for all sufficiently large \(t\); **no convergent multiplicative constant is claimed**. Consequently the coefficient of \(t^2\) in the logarithmic upper-tail rate is \(-1/(2v_a)\), and the coefficient of \(\log t\) after subtracting that quadratic term is exactly \(-(1+2\kappa)\). These constants depend on the shortest step and its probability, rather than just the mean step or stationary mean square.

In particular, two completely explicit step laws with \(\lambda=\sigma=1\) have **identical** mean step \(2\) and **identical** stationary mean-squared error \(7/27\), yet sharply different extreme-event probabilities:

| Step law | Distribution | Stationary right tail |
| --- | --- | --- |
| A | \(H=1,3\), each with probability \(1/2\) | \(\Theta(t^{-2}e^{-3t^2/2})\) |
| B | \(H=3/2\) with probability \(4/5\), or \(H=4\) with probability \(1/5\) | \(\Theta(t^{-1-2\log(5/4)/\log(25/4)}e^{-7t^2/4})\) |

In fact, if \(T_A(t)\) and \(T_B(t)\) denote the respective stationary right tails, then
\[
 \boxed{\displaystyle
 \lim_{t\to\infty}\frac{1}{t^2}
 \log\!\left(\frac{T_A(t)}{T_B(t)}\right)=\frac14.}
\]
Hence the two rare-event probabilities differ by an exponentially growing factor even though both first-step means and stationary quadratic errors agree.

## Assumptions and scope

All parameters satisfy \(\lambda,\sigma>0\), \(0<a<b<\infty\), \(0<\rho<1\). Steps are sampled independently at each update and independently of the Gaussian increments. The invariant law is observed **per numerical update** rather than at a physical-time-uniform sample. The result assumes exact real arithmetic and Gaussian increments with variance exactly \(H_n\) before implicit scaling. The finite initial value may be any deterministic real number or any independent square-integrable law.

For reference, the continuous-time Ornstein–Uhlenbeck invariant variance is \(\sigma^2/(2\lambda)\); the variance of the numerical invariant law is generally different and the law is not in general Gaussian.

## Proof

**1. Invariant Gaussian scale mixture.** Set
\[
 q_h=(1+\lambda h)^{-2},\qquad
 s_h=\sigma^2h(1+\lambda h)^{-2},\qquad
 v_h=\frac{s_h}{1-q_h}.
\]
The last equality simplifies to the stated formula for \(v_h\). Both possible one-step state multipliers are strictly less than one in absolute value. Backward iteration in independent Gaussian innovations therefore converges in \(L^2\) to a unique stationary state. Conditional on the complete step sequence, this state is centered Gaussian with a random variance \(V\) satisfying
\[
 V\ \stackrel d=\ q_H V'+s_H
   =q_H V'+(1-q_H)v_H,
\]
where \(V'\) is an independent copy and \(H\in\{a,b\}\) has the indicated probabilities. Since every update of this variance recursion is a convex combination of the previous variance and one of \(v_a,v_b\), its stationary solution satisfies
\[
 0<v_b\le V\le v_a<\infty\quad\text{almost surely}.
\]
Uniqueness follows from deterministic contraction by \(\max\{q_a,q_b\}<1\). The unconditional invariant variance is therefore
\[
 \overline v=\mathbb E_{\pi}X^2=\mathbb EV
 =\frac{\rho s_a+(1-\rho)s_b}
 {1-\rho q_a-(1-\rho)q_b}.
\]

**2. Exact endpoint small-deviation exponent.** Put
\[
 D=v_a-V,\qquad \Delta=v_a-v_b>0,\qquad
 \alpha=q_a,\qquad\beta=q_b,\qquad B=(1-\beta)\Delta>0.
\]
Because \(0<\beta<\alpha<1\), the distributional recursion becomes the following two affine maps:
\[
 D\ \stackrel d=\
 \begin{cases}
 \alpha D',&\text{with probability }\rho,\\
 \beta D'+B,&\text{with probability }1-\rho.
 \end{cases}
\]
Let \(N\) be the number of consecutive short-step maps before the first long-step map when reading the independent backward recursion. Then \(\Pr(N\ge n)=\rho^n\), and
\[
 D\ \stackrel d=\ \alpha^N(\beta D'+B),
 \qquad B\le\beta D'+B\le\Delta.
\]
It follows for sufficiently small \(\varepsilon>0\) that
\[
 \Pr\bigl(\alpha^N\Delta\le\varepsilon\bigr)
 \le\Pr(D\le\varepsilon)
 \le\Pr\bigl(\alpha^N B\le\varepsilon\bigr).
\]
For each fixed \(C>0\), the outer probability is
\[
 \rho^{\left\lceil\log(C/\varepsilon)/\log(1/\alpha)\right\rceil}
 \quad\text{when }\varepsilon<C.
\]
Since \(\kappa=\log(1/\rho)/\log(1/\alpha)\), there are constants \(0<c<C<\infty\) such that
\[
 c\varepsilon^{\kappa}\le\Pr(D\le\varepsilon)
 \le C\varepsilon^{\kappa}
 \qquad(\varepsilon\downarrow0).
\]
This both proves that \(v_a\) is the exact upper endpoint of the mixing-variance support and determines its sharp small-ball exponent. An exact multiplicative small-ball limit is not needed.

**3. Gaussian-mixture tail transfer.** Conditional Gaussianity gives
\[
 \Pr_{\pi}(X>t)=
 \mathbb E\!\left[\overline\Phi\left(t/\sqrt{v_a-D}\right)\right],
\]
where \(\overline\Phi\) is the standard normal right tail. Uniform Mills bounds on the compact interval \([v_b,v_a]\) compare this quantity, up to constants, with
\[
 \frac{e^{-t^2/(2v_a)}}{t}
 \mathbb E\exp\!\left[-\frac{t^2D}{2v_a(v_a-D)}\right].
\]
As \(D\in[0,\Delta]\), the exponential inside the expectation is bounded above by \(e^{-t^2D/(2v_a^2)}\). The small-ball bound in part 2 and integration by parts imply
\[
 \mathbb E[e^{-sD}]=O(s^{-\kappa})\qquad(s\to\infty).
\]
For the matching lower estimate, restrict the expectation to \(D\le t^{-2}\). On that event the Gaussian exponential loss relative to variance \(v_a\) is uniformly bounded; Mills' lower bound and the small-ball lower estimate imply
\[
 \Pr_{\pi}(X>t)
 \ge c' t^{-1-2\kappa}e^{-t^2/(2v_a)}.
\]
Combining upper and lower bounds proves the asserted \(\Theta\)-law. Symmetry follows from conditional centered Gaussianity.

**4. Exact matched-variance comparison.** With \(\lambda=\sigma=1\), direct rational calculation gives for law A
\[
 \mathbb E H=2,\qquad
 \mathbb E q_H=\frac5{32},\qquad
 \mathbb E s_H=\frac7{32},\qquad
 \overline v=\frac{7/32}{1-5/32}=\frac7{27}.
\]
For law B the corresponding quantities are
\[
 \mathbb E H=2,\qquad
 \mathbb E q_H=\frac{17}{125},\qquad
 \mathbb E s_H=\frac{28}{125},\qquad
 \overline v=\frac{28/125}{1-17/125}=\frac7{27}.
\]
The shortest-step conditional equilibrium variances are \(v_a=1/3\) and \(v_a=2/7\), respectively. The short-step squared multipliers are \(1/4\) and \(4/25\), and their probabilities are \(1/2\) and \(4/5\). Substitution into the proven tail theorem yields the two displayed \(\Theta\)-laws, whose logarithmic ratio has coefficient \(7/4-3/2=1/4\). This completes the proof.

## Verification

Run the included standard-library-only verifier with `python verify.py`. It checks exact rational noise and contraction coefficients, the stationary moment recursion, affine endpoint-deficit maps, the probability-support inequalities for many finite backward strings, and both matched-variance witnesses. It reports **50,315 passed checks**. These are diagnostics of the algebraic steps; the infinite small-deviation and tail statements follow from the proof above, not from finite computation.

## Relationship to prior work

The backward Euler–Maruyama invariant-measure theory of Liu, Mao and Wu (first public preprint June 20, 2022) proves existence and convergence of numerical invariant laws for much broader drift and diffusion classes with fixed step size. Liu and Wang's 2023 infinite-horizon analysis likewise addresses strong convergence and stationary approximation, not the stationary Gaussian extreme-tail prefactor for independently random step lengths. Existing random-step stochastic-theta moment formulas identify the Gaussian-mixture representation and moment criteria; the present result uses these ingredients but establishes a different quantitative endpoint: a sharp rare-run exponent and two explicit laws agreeing in mean step and invariant quadratic error while differing exponentially in the tails. Classical Gaussian Mills bounds and geometric-run arguments are used as standard tools rather than claimed as new results.

## Limitations

This is a scalar, additive-Gaussian-noise, two-positive-step, iid-step theorem at **update-index stationarity**. There is no claim about physical-time-weighted sampling, adaptive state-dependent steps, infinite-support step distributions, higher-dimensional nonnormal drifts, or finite-precision effects. The two-sided tail estimate determines the exact exponential and power exponents but not a limiting prefactor; possible multiplicative lattice oscillations are unresolved. No independent audit or exhaustive publication-priority certification has been performed.

## References

1. W. Liu, X. Mao, Y. Wu, *The backward Euler–Maruyama method for invariant measures of stochastic differential equations with super-linear coefficients*, arXiv:2206.09970 (first public June 20, 2022); *Applied Numerical Mathematics* **184** (2023), 137–150. https://arxiv.org/abs/2206.09970
2. W. Liu, Y. Wang, *Strong convergence in the infinite horizon of numerical methods for stochastic differential equations*, arXiv:2307.05039 (July 11, 2023). https://arxiv.org/abs/2307.05039
3. K. Cui, *Semiparametric Gaussian variance-mean mixtures for heavy-tailed and skewed data*, *International Scholarly Research Notices* (2012), article 345784. Section 2.2 discusses general Gaussian mixture tail transfers for unbounded mixing scales, rather than the bounded upper-endpoint mechanism used here. https://doi.org/10.5402/2012/345784
