# A sharp angular threshold and reentrant moment instability for randomly tested heat steps

## Finding
For a two-mode positive heat generator, consider a one-dimensional trial space and a one-dimensional residual-test space whose direction is independently resampled at every backward-Euler step from two equal-probability orientations. The following classification is exact.

Let \(0<m\le L\), \(A=\operatorname{diag}(m,L)\), \(\kappa=L/m\), and let \(v=(\cos\phi,\sin\phi)\), \(v_\perp=(-\sin\phi,\cos\phi)\). Fix a test rotation \(0<\theta<\pi/2\). The test vector at step \(n\) is \(w_{\sigma_n}=\cos\theta\,v+\sigma_n\sin\theta\,v_\perp\), with independent equiprobable signs \(\sigma_n\in\{-1,+1\}\). Write
\[
a=v^\mathsf TAv>0,\qquad b=\tan\theta\,v_\perp^\mathsf TAv.\]
At every step for which the test-dependent minimizer is unique, the computed scalar coefficient obeys
\[
\alpha_{n+1}=\frac{\alpha_n}{1+\tau(a+\sigma_nb)},\qquad \tau>0.
\]
Here \(x_n=\alpha_nv\), and the minimized finite-test residual is **exactly zero**, even when the computed trajectory is unstable.

If \(|b|\le a\), the method converges geometrically in mean square for **every** positive timestep: \(\mathbb E|\alpha_n|^2\to0\). If \(|b|>a\), set \(q=a+|b|\), \(d=|b|-a\), and
\[
H(\tau)=\frac12\left(\frac1{(1+q\tau)^2}+\frac1{(1-d\tau)^2}\right).
\]
There exist **exactly two** positive solutions \(\tau_-<1/d<\tau_+\) to \(H(\tau)=1\) (excluding the pole). Mean-square convergence holds precisely for
\[
\tau\in(0,\tau_-)\cup(\tau_+,\infty),
\]
while the second moment grows geometrically for \(\tau\in(\tau_-,1/d)\cup(1/d,\tau_+)\). At \(\tau=\tau_\pm\) the nonzero second moment stays constant; at \(\tau=1/d\) one of the two discrete minimizers is not unique, so this update rule is not defined without a tie-breaker.

This reentrant instability can occur for some trial line if and only if
\[
\theta>\theta_c:=2\arctan\sqrt{m/L}
\]
when \(m<L\); for \(m=L\), there is no such angle below \(\pi/2\). In particular, the **inclusive** angular safety condition \(\theta\le\theta_c\) guarantees strict mean-square decay for every trial line and every positive timestep, with \(\theta_c\sim2/\sqrt\kappa\) as \(\kappa\to\infty\).

For every configuration with \(|b|>a\), there is additionally an open interval of timesteps with **almost-sure exponential decay despite exponential growth of the second moment**. An exact rational example is \(A=\operatorname{diag}(1,9)\), \(v=(3,1)/\sqrt{10}\), \(\theta=\pi/4\), and \(\tau=14/5\). Its two multipliers are \(25/319\) and \(-25/17\). Their mean squared magnitude is \(31890625/29408929>1\), whereas the absolute product is \(625/5423<1\). Thus almost every realization decays, but the mean squared error diverges.

## Assumptions and scope
The continuous reference is the homogeneous finite-dimensional heat equation \(\dot x=-Ax\), with \(A\) positive definite. The trial class at every time level is the fixed line \(\operatorname{span}\{v\}\). The update is the **finite-test** minimum-residual backward-Euler step, not the full-dual-norm minimizer. At time level \(n+1\), choose \(\alpha_{n+1}\) to minimize
\[
\left|\left\langle (\alpha_{n+1}-\alpha_n)v+\tau\alpha_{n+1}Av,\,w_{\sigma_n}\right\rangle\right|^2/(\tau\|w_{\sigma_n}\|_A^2),
\]
where \(\|w\|_A^2=w^\mathsf TAw>0\). This is the restriction of a steady-energy-test dual residual to a one-dimensional test space. The sign choices are independently re-drawn with probability one half each; the timestep is fixed, and the initial coefficient is deterministic and nonzero. There is no forcing, parameter noise, or adaptively changed trial direction. This is an explicitly defined randomized-test specialization motivated by finite-test residual measurement, **not** an assertion that the motivating paper implements random test rotations.

## Proof
**Step 1 (exact optimizer).** Since \(w_\sigma^\mathsf Tv=\cos\theta>0\) and \(w_\sigma^\mathsf TAv=\cos\theta\,a+\sigma\sin\theta\,v_\perp^\mathsf TAv\), the measured residual is a positive weight times
\[
\left((1+\tau(a+\sigma b))\alpha_{n+1}-\alpha_n\right)^2.
\]
Unless \(1+\tau(a+\sigma b)=0\), its unique minimizer has zero measured residual and the multiplier stated above. When the factor vanishes, the loss does not depend on \(\alpha_{n+1}\), hence no unique minimizer exists.

**Step 2 (second moments).** Independence and the fixed trial line give the exact recursion
\[
\mathbb E|\alpha_n|^2=|\alpha_0|^2 H(\tau)^n,\quad
H(\tau)=\tfrac12\big[(1+\tau(a+b))^{-2}+(1+\tau(a-b))^{-2}\big].
\]
If \(|b|\le a\), both effective stiffnesses are nonnegative and at least one strictly positive, so \(0<H(\tau)<1\) at every positive timestep. If \(|b|>a\), relabel the signs so they give \(q=a+|b|>0\) and \(-d=a-|b|<0\), with \(q>d>0\). On \((0,1/d)\), \(H(0)=1\), \(H'(0)=d-q=-2a<0\), \(H''(\tau)=3q^2/(1+q\tau)^4+3d^2/(1-d\tau)^4>0\), and \(H(\tau)\to\infty\) as \(\tau\uparrow1/d\). Strict convexity forces exactly one positive return crossing \(\tau_-\). On \((1/d,\infty)\), both terms of \(H'(\tau)=-q/(1+q\tau)^3+d/(1-d\tau)^3\) are negative, and \(H\) decreases from infinity to zero. Hence precisely one further crossing \(\tau_+\). The stated phase diagram follows.

**Step 3 (sharp angular threshold).** For \(v=(\cos\phi,\sin\phi)\),
\[
\frac{|v_\perp^\mathsf TAv|}{v^\mathsf TAv}
=\frac{(L-m)|\tan\phi|}{m+L\tan^2\phi}.
\]
Its maximum over trial lines is \((L-m)/(2\sqrt{mL})\), attained when \(|\tan\phi|=\sqrt{m/L}\). Thus \(|b|\le a\) for all trial lines exactly when \(\tan\theta\,(L-m)/(2\sqrt{mL})\le1\). For \(m<L\) this is equivalent to \(\theta\le2\arctan\sqrt{m/L}\). Equality produces a zero-stiffness test with probability one half but still strict mean-square contraction because the other test has positive stiffness. Above equality choose an attaining trial line to obtain \(|b|>a\). The asymptotic angular law follows from the Taylor expansion of \(\arctan\).

**Step 4 (sample paths).** Outside the pole, the strong law of large numbers applied to the two logarithmic multipliers yields almost surely
\[
\lim_{n\to\infty}\frac1n\log\left|\frac{\alpha_n}{\alpha_0}\right|=-\frac12\log\left|[1+\tau(a+b)][1+\tau(a-b)]\right|.
\]
At either second-moment boundary, the two squared multipliers are unequal positive values with arithmetic mean one. Strict concavity of the logarithm gives the average log strictly below zero, so sample paths already decay exponentially at those boundaries. By continuity, a neighboring open interval on the moment-unstable side also has negative logarithmic growth. This proves existence of the almost-sure/second-moment gap for every \(|b|>a\).

**Step 5 (exact witness).** For \(A=\operatorname{diag}(1,9)\), \(v=(3,1)/\sqrt{10}\), and \(\theta=\pi/4\), direct inner products give \(a=9/5\) and \(b=12/5\). At \(\tau=14/5\) the two multipliers are \(25/319\), \(-25/17\). Their squared arithmetic mean and absolute product are the exact fractions above, proving the simultaneous statements without numerical approximation.

## Verification
Run `python3 verification.py` from a directory containing the packaged checker. The script uses exact rational arithmetic for the witness and 14,000 seeded reconstruction/angle cases plus 500 reentrant phase-diagram tests. The algebraic proof, not the finite tests, establishes the universal claims. No numerical experiment can certify a universal stability boundary by itself.

## Relationship to prior work
Muñoz-Matute and Rojas (2026) develop a time-stepping finite-test minimum-residual framework for parabolic problems and explicitly require complementary residual information to recover fully discrete reliability. Their results motivate the finite-test question; they do not, in the material inspected, give the balanced random one-test two-eigenmode classification above. This specialization deliberately changes test selection at every step and does not challenge the published reliability bounds, which include residual components that a finite test space misses.

Classical Petrov–Galerkin discrete inf–sup principles describe why test/trial compatibility matters. Operator-turning-angle and Kantorovich inequalities provide a known tool for the sharp angle optimization in Step 3; this fact alone is **not** presented as new. Classical independent-product stability results supply the moment and logarithmic criteria in Steps 2 and 4. The contribution assessed here is their exact combination for this randomly resampled finite-test backward-Euler update: inclusive angular safety, two disjoint stable timestep ranges beyond it, the singular loss boundary, and a universal pathwise-versus-moment gap.

## Limitations
Only two real positive eigenmodes, a fixed one-dimensional trial line, equiprobable independent two-angle test resampling, exact residual minimization, and fixed timestep are treated. These conclusions are not assertions about the full test-space dual norm, arbitrary neural-network optimization, higher-dimensional randomly rotated spaces, or independently perturbed forcing. When a test denominator vanishes, uniqueness fails rather than numerical divergence being assigned by convention. Mean-square instability does not imply that a typical sample path diverges. The earliest source inspection was limited to the public abstract, introduction, and initial formulation; the complete motivating manuscript could not be reopened for an appendix-level comparison, leaving a specialized-coverage risk.

## References
1. J. Muñoz-Matute and S. Rojas, *Stable time-stepping via residual minimization: finite-element and neural-network approximations for transient parabolic problems*, arXiv:2609.27548v1, 23 September 2026. https://arxiv.org/abs/2609.27548.
2. T. Führer, N. Heuer, and J. Sen Gupta, *A time-stepping DPG scheme for the heat equation*, arXiv:1607.00301, 2016. https://arxiv.org/abs/1607.00301.
3. C. Mollet, *Stability of Petrov–Galerkin Discretizations: Application to the Space-Time Weak Formulation for Parabolic Evolution Problems*, Comput. Methods Appl. Math. 14(2), 231–255 (2014). https://doi.org/10.1515/cmam-2014-0001.
4. K. Gustafson, *Operator trigonometry of preconditioning, domain decomposition, sparse approximate inverses, successive overrelaxation, minimum residual schemes*, Numer. Linear Algebra Appl. 10 (2003), 291–315. https://doi.org/10.1002/nla.289.
5. D. J. Higham, X. Mao, and C. Yuan, *Almost sure and moment exponential stability in the numerical simulation of stochastic differential equations*, SIAM J. Numer. Anal. 45 (2007), 592–609. https://doi.org/10.1137/060658138.
