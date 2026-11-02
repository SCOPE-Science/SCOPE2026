# A sharp two-scale bifurcation in random-step implicit-midpoint damping

## Finding

Consider scalar pseudo-time relaxation \(u'(t)=-\lambda u(t)\), where \(\lambda>0\), advanced with the implicit-midpoint rule. Independently at each iteration, choose the positive step length \(H=h e^a\) or \(H=h e^{-a}\), each with probability \(1/2\), where \(a\ge0\) is a fixed logarithmic half-spread and the overall scale \(h>0\) is free. We optimize **expected squared residual per numerical step**, not accuracy at a prescribed physical time. Let \(x=\log(\lambda h/2)\), \(c=\cosh a\), and write \(q_a(x)=\mathbb E[(u_{k+1}/u_k)^2]\) for nonzero \(u_k\). Then

\[
q_a(x)=1-\frac{2(1+c\cosh x)}{(c+\cosh x)^2},\qquad
\mathbb E|u_N|^2=|u_0|^2q_a(x)^N\quad(N\in\mathbb N_0).
\]

There is a sharp symmetry-breaking threshold

\[
a_c=\operatorname{arcosh}2=\log(2+\sqrt3),\qquad
\frac{h_+}{h_-}=e^{2a_c}=7+4\sqrt3.
\]

For \(0\le a\le a_c\) the **unique** minimizing scale is \(h=2/\lambda\). For \(a>a_c\) there are **exactly two** minimizing scales

\[
h_{\star,\pm}=\frac{2}{\lambda}\exp(\pm x_\star),\qquad
x_\star=\operatorname{arcosh}\!\left(c-\frac2c\right)>0.
\]

These scales have product \(4/\lambda^2\). The sharp minimum is

\[
\min_{h>0}q_a\!\left(\log\frac{\lambda h}{2}\right)=
\begin{cases}
\dfrac{c-1}{c+1},&1\le c\le2,\\[3pt]
\dfrac{c^2-2}{2(c^2-1)},&c\ge2.
\end{cases}
\]

The two branches agree at \(c=2\), where the minimum equals \(1/3\) and is quartically flat:
\[
q_{a_c}(x)=\frac13+\frac{x^4}{54}+O(x^6)\quad(x\to0).
\]

From above the threshold, the two optimizing log-scales separate with the sharp law
\[
x_\star=\sqrt{3\sqrt3}\,\sqrt{a-a_c}+O((a-a_c)^{3/2}).
\]

For every \(a>0\), the mean-square optimal scales are strictly different from the two scales that make one of the random midpoint multipliers identically zero. At either of those nonoptimal scales, nevertheless, the exact residual becomes zero after a geometric number of iterations with success parameter \(1/2\). Thus minimization of expected squared residual and attainment of *finite-step almost-sure extinction* select different step scales.

## Assumptions and scope

All parameters are real, with \(\lambda>0\), \(a\ge0\), \(h>0\), and deterministic \(u_0\ne0\). At each iteration, the choice of \(H\in\{he^{-a},he^a\}\) is fresh, independent of previous choices and equiprobable. The midpoint equation is solved exactly; the algebra is in exact arithmetic. The optimization holds \(a\) and \(\lambda\) fixed and varies the positive overall geometric-mean step scale \(h\), so the ratio of step lengths stays fixed. When \(a=0\), the distribution is deterministic and the single midpoint step \(h=2/\lambda\) annihilates the mode.

The objective is one-step or fixed-step-count mean-square decay; physical elapsed time is random and changes when \(h\) changes. No optimality per unit physical time or at a fixed final time is asserted. All scalar initial values scale the squared error by \(|u_0|^2\).

## Proof

**Midpoint multiplier and independence.** The implicit-midpoint relation for \(u'=-\lambda u\) is \(u_{k+1}=u_k-\lambda H(u_k+u_{k+1})/2\), hence the multiplier is
\[
R(H)=\frac{1-\lambda H/2}{1+\lambda H/2}.
\]
For any finite positive \(H\), \(|R(H)|<1\). Substitution \(\lambda H/2=e^{x\pm a}\) gives \(R(H)=-\tanh((x\pm a)/2)\), and therefore
\[
q_a(x)=\frac12\left[\tanh^2\frac{x+a}{2}+\tanh^2\frac{x-a}{2}\right].
\]
The factors at successive iterations are independent, so multiplying their second moments proves the stated exact \(N\)-step formula for every integer \(N\ge0\).

**Rational reduction.** Since \(\tanh^2(z/2)=1-2/(1+\cosh z)\), let \(y=\cosh x\ge1\), \(c=\cosh a\ge1\). The identity
\[
(1+\cosh(x+a))(1+\cosh(x-a))=(y+c)^2
\]
follows from the addition formulas and \(\cosh^2-\sinh^2=1\). Summing the two reciprocal factors gives
\[
q_a(x)=Q_c(y):=1-\frac{2(1+cy)}{(y+c)^2},\qquad
\frac{dQ_c}{dy}=\frac{2(cy+2-c^2)}{(y+c)^3}.
\]
There are no hidden stationary points, as \(y\) ranges over the whole half-line \([1,\infty)\).

**All global optimizers and values.** If \(1\le c\le2\), then \(cy+2-c^2\ge c+2-c^2\ge0\) for \(y\ge1\), with strict positivity away from the endpoint, including at \(c=2\). Thus \(Q_c\) is strictly increasing on \((1,\infty)\); \(y=1\), equivalently \(x=0\), is the unique minimizer. Substitution gives \(Q_c(1)=(c-1)/(c+1)\). If \(c>2\), the derivative is negative for \(1\le y<c-2/c\) and positive thereafter, so the sole minimizing \(y\) is \(y_\star=c-2/c>1\). Exactly the two \(x=\pm\operatorname{arcosh}(y_\star)\) achieve it; substitution gives \(Q_c(y_\star)=(c^2-2)/(2(c^2-1))\). The endpoint limits as \(y\to\infty\) equal \(1\), so no minimizers are missing. The threshold is \(c=2\), equivalent to the stated \(a_c\) and length ratio. Symmetry of \(x\mapsto-x\) gives the reciprocal-scale product.

**Degeneracy and splitting.** At \(c=2\), Taylor expansion of the exact rational function with \(y=\cosh x=1+x^2/2+O(x^4)\) gives \(Q_2(\cosh x)=1/3+x^4/54+O(x^6)\). When \(a=a_c+\delta\) with \(\delta\downarrow0\), \(c=2+\sqrt3\,\delta+O(\delta^2)\) and
\[
y_\star-1=\left(c-\frac2c\right)-1=\frac{3\sqrt3}{2}\delta+O(\delta^2).
\]
Inverting \(\cosh x_\star-1=x_\star^2/2+O(x_\star^4)\) yields the stated square-root law with remainder \(O(\delta^{3/2})\).

**Mean-square versus almost-sure design.** A midpoint multiplier is zero exactly when \(\lambda H/2=1\), which for the two atoms means \(x=+a\) or \(x=-a\). For \(a>0\), the mean-square optimizer always satisfies \(|x|<a\): this is immediate for \(c\le2\), and for \(c>2\) follows from \(1<c-2/c<c=\cosh a\). Hence neither optimal atom is zero. At either zero-atom scale, independent iterations extinguish any nonzero scalar state at the first occurrence of the matching atom, with \(\Pr(T=n)=2^{-n}\) for \(n=1,2,\ldots\), whereas under a mean-square-optimal scale a product of nonzero factors never vanishes at finite \(n\). The zero-atom scale is strictly mean-square suboptimal: for \(1<c\le2\), direct subtraction gives
\[
\frac{\tanh^2a}{2}-\frac{c-1}{c+1}
=\frac{(c-1)(1+2c-c^2)}{2c^2(c+1)}>0,
\]
and for \(c>2\), subtraction gives \(1/[2c^2(c^2-1)]>0\). This proves the distinct objectives without conflating almost-sure extinction with mean-square optimality.

## Verification

A standalone Python verifier in `verify.py` checks the rational identity, derivative and minimum formulas symbolically; verifies the critical quartic coefficient; tests exact-rational evaluations; compares direct midpoint products to the closed formula across sample values; compares global candidates to 6,171 grid evaluations; verifies exact finite-horizon binomial expansions; and probes the near-critical splitting law. Run `python verify.py` after installing the dependency in `requirements.txt`. The verifier passed 6,847 check groups. The analytic argument above, not finite testing, establishes the all-parameter claims.

For orientation, at \(a=1.5\), the length ratio is approximately \(20.08554\). The two optimal log-scales are \(x\approx\pm0.96440445\), with one-step squared contraction \(q_{\min}\approx0.389718\). The central scale gives approximately \(0.403414\); the almost-sure-killing scale gives approximately \(0.409647\).

## Relationship to prior work

Abdulle and Garegnani [1] introduced and analyzed random-time-step numerical integration, explicitly including implicit midpoint as a geometrically preserving integrator. Their work proves accuracy and conservation statements for probabilistic solvers, not the fixed-spread, cost-per-iteration global damping optimization or its symmetry-breaking threshold. Lie, Stahn and Sullivan [2] derive broad error bounds for randomized operator evolution on possibly nonuniform time grids, primarily through additive random perturbations, not this two-atom midpoint scale-design classification. The classical midpoint stability function and its lack of stiff decay at arbitrarily large steps are established numerical-analysis background [3]. These existing facts are used, not claimed as novel.

A related exact scalar analysis of randomized implicit-stage weights, distinct from randomizing the physical step length, optimizes a distribution over stage parameters at fixed mean. It does not imply the present optimization over geometric-mean time-step scale with fixed two-point log-spread. No exhaustive priority claim is made beyond the inspected literature and available research records.

## Limitations

The model is scalar, uses equiprobable independent two-point step choices and exact arithmetic, and optimizes the residual after a prescribed number of iterations. The result does not determine optimality for nonuniform step probabilities, general spectra, nonlinear ODEs, prescribed physical terminal times, variable solve costs, finite-precision arithmetic, or solver accuracy. The finite-termination corollary relies on exact parameter matching and exact zero arithmetic. A mathematically equivalent phase diagram could exist in older analyses of rational stability functions or random multiplicative recursions; the searched literature does not establish definitive publication priority.

## References

[1] A. Abdulle and G. Garegnani, *Random time step probabilistic methods for uncertainty quantification in chaotic and geometric numerical integration*, arXiv:1801.01340, first posted 2018-01-04; *Statistics and Computing* 30 (2020), 907–932. https://arxiv.org/abs/1801.01340

[2] H. C. Lie, M. Stahn and T. J. Sullivan, *Randomised one-step time integration methods for deterministic operator differential equations*, arXiv:2103.16506, first posted 2021-03-30; *Calcolo* 59 (2022), article 13. https://arxiv.org/abs/2103.16506

[3] E. Hairer, C. Lubich and G. Wanner, *Geometric Numerical Integration*, second edition, Springer, 2006. https://doi.org/10.1007/3-540-30666-8
