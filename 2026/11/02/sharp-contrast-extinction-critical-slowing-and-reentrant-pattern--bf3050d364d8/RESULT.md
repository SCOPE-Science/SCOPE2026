# Sharp contrast extinction, critical slowing, and reentrant pattern stability in logistic threshold networks

## Finding

Consider, for every integer \(N\geq2\), the autonomous activation network
\[
\dot x_i=-x_i+\ell\bigl(\theta+\beta (Wx)_i\bigr),\qquad
\ell(z)=\frac{1}{1+e^{-z}},\quad x(0)\in[0,1]^N,
\]
with arbitrary real \(\theta\), \(\beta\geq0\), and a nonnegative row-stochastic matrix \(W\). Put
\[
\delta(W)=\frac12\max_{i,j}\sum_{r=1}^N|w_{ir}-w_{jr}|,\qquad
D(x)=\max_i x_i-\min_i x_i,\qquad k=\frac{\beta\delta(W)}4.
\]
Then the following sharp network-versus-pattern classification holds.

1. Every solution satisfies the *nonlinear contrast inequality*
\[
D^+D(t)\leq-D(t)+\tanh\bigl(kD(t)\bigr).
\]
If \(k<1\), then \(D(t)\leq D(0)e^{-(1-k)t}\). If \(k=1\), then \(D(t)\to0\) and
\[
\limsup_{t\to\infty}tD(t)^2\leq\frac32.
\]
In both cases every solution converges to a single spatially homogeneous equilibrium \(s\mathbf1\), where \(s\in(0,1)\) solves \(s=\ell(\theta+\beta s)\). This statement permits several different homogeneous equilibria for the same parameters; no uniqueness of the terminal scalar state is asserted.

2. The boundary \(\beta\delta(W)=4\) and the critical constant \(3/2\) are sharp *uniformly over network sizes and weights*. For every \(\delta\in(0,1]\), let
\[
W_\delta=\frac12\begin{pmatrix}1+\delta&1-\delta\\1-\delta&1+\delta\end{pmatrix},\qquad \theta=-\frac\beta2.
\]
The invariant line \(x_1+x_2=1\), with contrast \(v=x_1-x_2\), carries the exact equation
\[
\dot v=-v+\tanh\left(\frac{\beta\delta}{4}v\right).
\]
At \(\beta\delta=4\), any trajectory with \(0<v(0)<1\) obeys \(\lim_{t\to\infty}t v(t)^2=3/2\). At \(\beta\delta>4\), there are two nonhomogeneous equilibria
\[
\left(\frac{1+v_*}{2},\frac{1-v_*}{2}\right),\qquad
\left(\frac{1-v_*}{2},\frac{1+v_*}{2}\right),
\]
where \(v_*\in(0,1)\) is the unique positive root of \(v_*=\tanh(kv_*)\). Their contrast opens as \(v_*\sim\sqrt{3(k-1)}\) as \(k\downarrow1\).

3. The two-node *pattern-attraction threshold* is distinct from the pattern-existence threshold whenever \(0<\delta<1\). Define
\[
H(v)=\frac{(1-v^2)\operatorname{artanh}v}{v},\qquad
H(v_s)=\delta,\qquad
\beta_s(\delta)=\frac4{1-v_s^2}.
\]
There is exactly one \(v_s\in(0,1)\), and \(\beta_s(\delta)>4/\delta\). For \(4/\delta<\beta<\beta_s(\delta)\), the two nonhomogeneous equilibria are hyperbolic saddles; for \(\beta>\beta_s(\delta)\), both are hyperbolic sinks. At equality one eigenvalue is zero (no nonlinear-stability assertion). For \(\delta=1\), the two nonhomogeneous equilibria are hyperbolic sinks for every \(\beta>4\).

This gives a sharp global *suppression of spatially heterogeneous asymptotic states* even in the scalar-bistable regime \(\beta>4\), together with the exact two-node pattern birth and later stabilization.

For example, with \(W=W_{1/4}\), \(\beta=8\), and \(\theta=-4\), the homogeneous scalar equation has three distinct equilibria (two attracting), but \(\beta\delta(W)=2<4\), so every trajectory nevertheless loses all node-to-node contrast exponentially and converges to one of those homogeneous equilibria. With \(\delta=1/2\), the distinct pattern thresholds are \(\beta_{\mathrm{birth}}=8\) and \(\beta_s\approx10.9359659465\).

## Assumptions and scope

A fixed, finite network is considered. No symmetry, connectivity, irreducibility, diagonal positivity, or equitable partition of \(W\) is required for the all-network result. The logistic function is the common response at every node; the common field \(\theta\) is constant in time. The open interior \((0,1)^N\) is forward entered from its cube boundary for each positive time. In the sharpness construction the two-node matrix is symmetric, with \(0<\delta\leq1\) and \(\beta>0\). The Dobrushin coefficient of \(W_\delta\) is exactly \(\delta\). The primary classification concerns autonomous ordinary differential equations, not discrete updates or random switching.

## Proof

**The exact logistic chord bound.** For any \(a,b\in\mathbb R\), the identity \(\ell(z)=(1+\tanh(z/2))/2\) and the monotonicity of \(\tanh\) give
\[
|\ell(a)-\ell(b)|\leq\tanh\left(\frac{|a-b|}{4}\right).
\]
Indeed, for a fixed separation the difference is largest when the arguments are centered at zero; equality then holds. For any row indices \(i,j\), because the row difference has coefficient sum zero, separating positive from negative coefficients proves
\[
|(Wx)_i-(Wx)_j|\leq\frac12\sum_{r=1}^N|w_{ir}-w_{jr}|D(x)\leq\delta(W)D(x).
\]
The first inequality is the classical Dobrushin diameter estimate, not an independent novelty claim.

**Global diameter dynamics.** The cube is forward invariant since its inward-pointing vector field has \(\dot x_i>0\) at \(x_i=0\) and \(\dot x_i<0\) at \(x_i=1\). For every active maximizer \(i\) and minimizer \(j\), subtract the corresponding equations; the two preceding bounds give
\[
\dot x_i-\dot x_j\leq-D+\tanh(kD).
\]
The maximum-of-finitely-many Dini derivative rule establishes the claimed inequality even when extrema tie. The scalar comparison solution \(z'=-z+\tanh(kz)\), \(z(0)=D(0)\), bounds \(0\leq D(t)\leq z(t)\). For \(k<1\), \(\tanh(kz)\leq kz\) proves exponential decay. For \(k=1\), \(-z+\tanh z<0\) for every \(z>0\), and the Taylor law \(z'=-z^3/3+O(z^5)\) gives \((z^{-2})'=2/3+O(z^2)\). Since \(z(t)\to0\), integration or Cesàro averaging yields \(z(t)^2t\to3/2\). The critical upper bound follows.

**Full convergence, not just narrowing.** Let \(p=N^{-1}\sum_i x_i\). Since every coordinate of \(Wx\) and \(p\) is between the current extreme states, the ordinary logistic Lipschitz bound gives
\[
p'=-p+\ell(\theta+\beta p)+r(t),\qquad |r(t)|\leq\frac\beta4D(t)\longrightarrow0.
\]
The scalar analytic function \(f(p)=-p+\ell(\theta+\beta p)\) has finitely many zeros in \([0,1]\): it extends analytically across that compact set and satisfies \(f(0)>0>f(1)\), hence cannot be identically zero. To see that a bounded solution of \(p'=f(p)+r(t)\), \(r(t)\to0\), approaches one of those zeros, suppose its \(\liminf\) and \(\limsup\) differ. Every point strictly between them is crossed in both directions arbitrarily late. On any subinterval where \(f\) has a fixed nonzero sign, sufficiently late crossings are forced in only one direction, a contradiction. Thus \(p(t)\to s\) with \(f(s)=0\), and \(D(t)\to0\) gives \(x_i(t)\to s\) for all \(i\). The case of a singleton limit not solving \(f(s)=0\) is excluded by the derivative having a fixed nonzero sign in its neighborhood.

**Sharpness and the two stability thresholds.** On the two-node invariant line, substitution gives the exact odd scalar equation stated above. For \(k=1\), every \(v(0)\in(0,1)\) decreases toward zero and the preceding cubic asymptotics attain \(3/2\). If \(k>1\), \(\tanh(kv)-v\) is strictly concave on \((0,1)\), with derivative \(k-1>0\) at zero and a negative value at one. It therefore has exactly one positive zero \(v_*\); oddness gives the reflected state. Expansion at \(k=1\) yields \(v_*^2=3(k-1)+o(k-1)\).

At either nonhomogeneous equilibrium both logistic derivatives equal \((1-v_*^2)/4\); hence the full two-dimensional Jacobian equals \(-I+[\beta(1-v_*^2)/4]W_\delta\), with eigenvalues
\[
\lambda_{\mathrm{mean}}=-1+\frac\beta4(1-v_*^2),\qquad
\lambda_{\mathrm{contrast}}=-1+\frac{\beta\delta}4(1-v_*^2).
\]
The equilibrium identity implies \(k=\operatorname{artanh}(v_*)/v_*\), so these eigenvalues are \(-1+H(v_*)/\delta\) and \(-1+H(v_*)\). Since
\[
H'(v)=\frac{v-(1+v^2)\operatorname{artanh}v}{v^2}<0,\quad H(0+)=1,\quad H(1-)=0,
\]
the contrast eigenvalue is always negative for \(v_*>0\). For \(0<\delta<1\), the mean eigenvalue crosses zero exactly once, when \(H(v_s)=\delta\), giving \(\beta_s=4/(1-v_s^2)\); it changes from positive to negative. For \(\delta=1\) both eigenvalues are strictly negative for all \(\beta>4\). All claims follow.

## Verification

Run `python verify.py` with Python 3 and installed `numpy`, `scipy`, and `sympy`. It checks the exact logistic symmetry and cubic Taylor coefficient using symbolic mathematics; performs 400 randomized network/field tests of the Dobrushin-logistic diameter inequality; verifies two-node equilibrium and Jacobian spectra over 20 parameter combinations; checks the unique two-stage threshold numerically at four coupling contrasts; and integrates the exact critical contrast equation to test the constant \(3/2\). The executable diagnostics confirm the formulas on sampled inputs but **do not replace the analytical arguments over arbitrary network dimension, parameters, or infinite time**.

## Relationship to prior work

Boudourides introduces this row-stochastic threshold-response network and establishes contraction when \(\beta\sup\ell'<1\), the stability ordering of homogeneous modes, persistence of weakly coupled mixed equilibria, and local heterogeneous cusps. That contraction condition is \(\beta<4\), whereas the global contrast theorem uses the possibly much smaller product \(\beta\delta(W)\), applying also to \(\beta>4\) and leaving scalar bistability intact. Its globally valid critical \(t^{-1/2}\) envelope and sharp mixed-pattern stability thresholds are not stated in the inspected sections of the motivating work.

The Dobrushin coefficient and the linear diameter contraction inequality are classical (Gaubert–Qu and the earlier Markov-consensus literature), and are used here as prior tools rather than claimed discoveries. Duncan and collaborators study equilibria of steep sigmoidal regulatory networks by combinatorial switching limits, not this uniform finite-slope, all-weight logistic contrast boundary. Kaye studies scalar collective hysteresis and a spatial extension; the publicly inspected summary does not assert the present finite-network threshold. Priority beyond inspected literature is not independently certified.

## Limitations

The sharpness of the **uniform guarantee** does not assert that every particular matrix with \(\beta\delta(W)>4\) possesses heterogeneous equilibria. The pattern-attraction classification applies only to the explicitly specified symmetric two-node family and its common-field choice. At the secondary stability threshold no nonlinear center-manifold type is established. The critical \(3/2\) bound is a limsup and need not be attained in every network; attainment is proved for the constructed invariant contrast line. No global basin partition, robustness to differing node thresholds, or extension to time-varying/nonstochastic weights is claimed. Historical priority remains provisional pending broader expert inspection.

## References

- Moses Boudourides, *Collective Hysteresis and Multistability in Threshold Networks*, arXiv:2609.10580, first posted 2026-09-05, https://arxiv.org/abs/2609.10580 .
- Stéphane Gaubert and Zheng Qu, *Dobrushin's ergodicity coefficient for Markov operators on cones*, arXiv:1307.4649, https://arxiv.org/abs/1307.4649 .
- William Duncan, Tomas Gedeon, Hiroshi Kokubu, Konstantin Mischaikow, and Hiroe Oka, *Equilibria and their Stability in Networks with Steep Sigmoidal Nonlinearities*, arXiv:2103.17184, https://arxiv.org/abs/2103.17184 .
- Alexander R. Kaye, *From individual thresholds to collective hysteresis: a mechanistic model of the dawn chorus*, Journal of the Royal Society Interface 23 (2026), article 20260267, https://doi.org/10.1098/rsif.2026.0267 .
