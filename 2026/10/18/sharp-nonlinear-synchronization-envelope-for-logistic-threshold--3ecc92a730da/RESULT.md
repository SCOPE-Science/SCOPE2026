# Sharp nonlinear synchronization envelope for logistic threshold networks

## Finding

For every nonnegative row-stochastic matrix \(W\) of size \(N\geq 2\), every constant feedback strength \(\beta\geq0\), and every shared, locally measurable forcing \(H(t)\), consider the logistic activation dynamics
\[
\dot x_i(t)=-x_i(t)+\sigma\bigl(H(t)+\beta(Wx(t))_i\bigr),\qquad
\sigma(s)=(1+e^{-s})^{-1},\quad x(0)\in[0,1]^N.
\]
Define the state diameter and the row overlap coefficient
\[
R(t)=\max_i x_i(t)-\min_i x_i(t),\qquad
\delta(W)=\frac12\max_{i,j}\sum_{k=1}^N|W_{ik}-W_{jk}|,
\]
and set \(q=\beta\delta(W)\). If \(r(t)\) solves
\[
\dot r=-r+\tanh(qr/4),\qquad r(0)=R(0),
\]
then the **exact, sharp universal comparison** is \(0\le R(t)\le r(t)\) for every \(t\ge0\). For each fixed \(q\ge0\) and \(0\le R(0)\le1\), a two-node threshold network realizes equality for all time.

The resulting sharp regimes are:

1. If \(q<4\), then \(R(t)\le R(0)e^{-(1-q/4)t}\). The exponent is the best universal exponential rate.
2. If \(q=4\), then all trajectories synchronize and
   \[
   \limsup_{t\to\infty}\sqrt t\,R(t)\le\sqrt{\frac32}.
   \]
   The power and coefficient are both attained in the two-node example for any positive initial diameter.
3. If \(q>4\), then the two-node example has two symmetry-related unequal-activity equilibria with state diameters \(r_*(q)>0\), where \(r_*(q)\) is the unique positive solution of \(r_*=\tanh(qr_*/4)\). Thus no universal all-initial-condition synchronization statement extends beyond the threshold.

In particular, sufficiently overlapping rows enforce synchronization even when the individual feedback strength \(\beta\) exceeds the scalar logistic bistability threshold \(4\); the conclusion is pathwise for arbitrary shared forcing.

## Assumptions and scope

The size \(N\) is any integer at least two. All entries of \(W\) are nonnegative and each row sums to one; \(W\) and \(\beta\) do not depend on time. The common forcing \(H:[0,\infty)\to\mathbb R\) is measurable and finite almost everywhere, with no boundedness or regularity beyond measurability needed: the vector field is uniformly bounded in its forcing-dependent portion and globally Lipschitz in the state. The initial state is in the closed unit cube; no irreducibility, symmetry, connectedness, or autonomous forcing is required. The claim is about **differences between coordinates within one solution**, not convergence of the entire state to a single steady vector under time-varying forcing.

## Proof

**1. Well-posedness and invariance.** At a boundary face \(x_i=0\), its derivative is nonnegative; at \(x_i=1\), its derivative is nonpositive. The logistic map has bounded derivative \(0\le\sigma'(s)\le1/4\). Because \(W\) is row stochastic, the right-hand side is globally Lipschitz in \(x\) uniformly over all values of the measurable forcing. Carathéodory existence and uniqueness, the invariant unit cube, and global forward continuation follow.

**2. Sharp row-difference control.** For any two rows \(i,j\), their difference has zero total sum. Split its positive and negative entries and subtract the minimum of \(x\) to obtain
\[
|(Wx)_i-(Wx)_j|\le\frac12\sum_k|W_{ik}-W_{jk}|\,R\le\delta(W)R.
\]
This is the standard Dobrushin diameter estimate; the row coefficient itself is not claimed to be new.

**3. Sharp logistic secant control.** For any reals \(u\ge v\), writing \(m=(u+v)/2\) and \(a=(u-v)/2\ge0\), direct hyperbolic algebra yields
\[
\sigma(u)-\sigma(v)=\frac{\sinh a}{\cosh m+\cosh a}
\le\frac{\sinh a}{1+\cosh a}=\tanh\bigl((u-v)/4\bigr).
\]
If \(u<v\), the sigmoid difference is nonpositive and obeys the same nonnegative upper bound after replacing \(u-v\) by \(|u-v|\). For almost every \(t\), the upper right Dini derivative of the finite maximum-minus-minimum satisfies
\[
D^+R(t)\le -R(t)+\tanh\bigl(qR(t)/4\bigr).
\]
Indeed, at an active maximum index \(i\) and active minimum index \(j\), the derivative difference of the state equations is \(-R\) plus a logistic difference. The Dini derivative selects the largest such active derivative difference; each obeys the bound. The scalar right-hand side is locally Lipschitz, so scalar comparison proves \(R(t)\le r(t)\) for all time, including instants with tied maxima/minima.

**4. Exact optimality construction.** For any \(q\ge0\), select \(\delta\in(0,1]\) and \(\beta=q/\delta\), and take
\[
W_\delta=\begin{pmatrix}(1+\delta)/2&(1-\delta)/2\\(1-\delta)/2&(1+\delta)/2\end{pmatrix},
\qquad H(t)\equiv-\beta/2.
\]
The plane \(x_1+x_2=1\) is invariant: on it the two sigmoid inputs are opposites and their outputs sum to one. With \(x_1(0)=(1+r_0)/2\) and \(x_2(0)=(1-r_0)/2\), where \(0\le r_0\le1\), the signed difference obeys
\[
\dot r=-r+\sigma(qr/2)-\sigma(-qr/2)=-r+\tanh(qr/4).
\]
The signed difference remains nonnegative by uniqueness, so it equals the diameter. This attains the full comparison trajectory for every \(q\), every permitted initial diameter, and every time.

**5. Subcritical and critical regimes.** If \(q<4\), \(\tanh z\le z\) for nonnegative \(z\) gives the stated exponential estimate. In the equality example the linearization at \(r=0\) has eigenvalue \(-1+q/4\), so no strictly faster universal exponential decay exponent works uniformly for positive sufficiently small initial diameter. At \(q=4\), the scalar equation is \(r'=-r+\tanh r\). Every solution with \(r_0>0\) decreases to zero and remains positive, since \(\tanh r<r\) for \(r>0\). Furthermore,
\[
\frac{d}{dt}\frac1{r(t)^2}=\frac{2(r(t)-\tanh r(t))}{r(t)^3}\longrightarrow\frac23,
\]
because \(r-\tanh r=r^3/3+O(r^5)\). Integrating, or applying the Stolz/Cesàro argument, yields \(t r(t)^2\to3/2\). When \(r_0=0\) the diameter is identically zero. Comparison then gives the global critical bound and the construction gives sharpness.

**6. Above threshold.** Let \(q>4\) and put \(a=q/4>1\). The function \(f(r)=-r+\tanh(ar)\) has \(f(0)=0\), \(f'(0)>0\), \(f(1)<0\), and \(f''(r)=-2a^2\operatorname{sech}^2(ar)\tanh(ar)<0\) for all \(r>0\). Therefore there is exactly one root \(r_*(q)\in(0,1)\). In the two-node invariant plane, the states \(((1+r_*)/2,(1-r_*)/2)\) and its reversal are genuine fixed points. They exhibit a persistent nonzero diameter. This does not assert their attraction in the full \(N\)-dimensional phase space.

## Verification

The accompanying standalone Python 3 file `threshold_diameter_checker.py` uses only the standard library. It tests 4,000 random row-stochastic networks for the pointwise Dini inequality and 1,500 exact two-node-saturation instances; it also checks the scalar critical inverse-square asymptotic numerically at three initial amplitudes and four supercritical roots. Execute `python3 threshold_diameter_checker.py`. Finite diagnostics do not certify the all-time comparison or the limiting laws, which are established by the preceding proof.

## Relationship to prior work

Boudourides, *Collective Hysteresis and Multistability in Threshold Networks* (arXiv:2609.10580v1, publicly posted September 5, 2026), introduces the same row-stochastic threshold-response network, proves a global infinity-norm contraction and unique equilibrium when \(\beta\sup\sigma'<1\), and studies equitable quotients and heterogeneous cusp bifurcations. Here the subject is instead **within-trajectory, topology-sensitive synchronization**: it can persist at \(\beta>4\) despite multiple homogeneous equilibria; the forcing may vary arbitrarily in time; and the nonlinear envelope, critical \(t^{-1/2}\) coefficient, and counterexample are exact. The complete accessible HTML primary text, especially Sections 2–7, was inspected for these claims.

Gaubert and Qu, *Dobrushin's ergodicity coefficient for Markov operators on cones, and beyond* (arXiv:1302.5226; *Integral Equations and Operator Theory*, 2015), establish the classical row-stochastic diameter coefficient and a framework for nonlinear consensus on cones. Their Section 4 identifies the linear diameter contraction coefficient; Section 6 studies translation-invariant nonlinear consensus flows. Neither inspected statement directly gives the logistic activation-minus-decay envelope with external shared forcing or the sharp critical and supercritical formulas here. The underlying Dobrushin inequality and the scalar expansion of \(\tanh\) are prior standard tools.

## Limitations

The assertion concerns coordinate consensus, not convergence to a unique constant under forcing or uniqueness of equilibria. It requires a common external field, logistic threshold distribution, nonnegative row-stochastic coupling, and time-independent \(W\) and \(\beta\). Row-wise heterogeneous forcing can prevent exact synchronization. The upper bound is universally optimal over networks, not necessarily attained by every fixed network. No assertion is made about full-space stability of the two nonhomogeneous fixed points. Classical consensus inequalities and scalar normal-form techniques may yield related special cases; independent bibliographic and mathematical assessment has not been performed.

## References

1. M. Boudourides, *Collective Hysteresis and Multistability in Threshold Networks*, arXiv:2609.10580v1 (first made public September 5, 2026), https://arxiv.org/abs/2609.10580.
2. S. Gaubert and Z. Qu, *Dobrushin's ergodicity coefficient for Markov operators on cones, and beyond*, arXiv:1302.5226, https://arxiv.org/abs/1302.5226; *Integral Equations and Operator Theory* (2015).
