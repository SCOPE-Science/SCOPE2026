# Finite-mixture cooperative bistability: a weight-polytope criterion and quadratic onset law

## Finding
Let an infinite well-mixed population play a finite mixture of geometric-return public-goods games. Interaction class \(j\) has group size \(n_j\geq2\), synergy/discount parameter \(\delta_j>0\), and probability \(w_j\geq0\), with \(\sum_jw_j=1\). Define
\[
 H_w(x)=\sum_{j=1}^m\frac{w_j}{n_j}\bigl(1+(\delta_j-1)x\bigr)^{n_j-1},\qquad
 \dot x=x(1-x)\bigl(rH_w(x)-1\bigr),\quad r>0.
\]
For every finite number of classes, this system has at most two *isolated* interior fixed points. Let
\[
 A(w)=\sum_j w_j\frac{n_j-1}{n_j}(\delta_j-1),\qquad
 B(w)=\sum_j w_j\frac{n_j-1}{n_j}(\delta_j-1)\delta_j^{n_j-2}.
\]
There exist two distinct interior fixed points for some \(r\) **if and only if** \(A(w)<0<B(w)\). Equivalently, the weights admitting the phenomenon form exactly the intersection of the probability simplex with these two strict linear halfspaces. When this occurs, let \(z\in(0,1)\) be the unique solution of \(H_w'(z)=0\). The exact open benefit-to-cost interval is
\[
 \frac1{\min\{H_w(0),H_w(1)\}}<r<\frac1{H_w(z)}.
\]
Throughout this interval, the lower interior fixed point and full cooperation are stable, while the upper interior fixed point and full defection are unstable. A weight vector with \(A<0<B\) exists precisely when there is a discounting class (\(\delta<1\)), a synergistic class (\(\delta>1\)), and at least one of those two classes has \(n\ge3\). Zero weights are allowed; if strictly positive weights for every class are required, the same existence characterization holds by sufficiently small perturbation.

There is also a universal *quadratic birth law* for this bistability interval. Suppose the weights follow an admissible affine path \(w(t)=w^0+tv\) for \(t\ge0\) sufficiently small, and \(H_t=H_{w(t)}\) satisfies
\[
 H_0'(0)=0,\quad c=H_0''(0)>0,\quad
 \kappa=-\left.\frac{d}{dt}H_t'(0)\right|_{t=0}>0.
\]
Then the stable interior branch first appears at \(z(t)=\kappa t/c+O(t^2)\), and the exact width of the interval of \(r\) giving two interior fixed points obeys
\[
 \Delta r(t)=\frac{\kappa^2}{2cH_0(0)^2}t^2+O(t^3).
\]
The right-endpoint counterpart replaces \(H_0'(0)=0\) by \(H_0'(1)=0\), requires \(H_0''(1)>0\) and \(\left.\frac{d}{dt}H_t'(1)\right|_0>0\), and replaces \(H_0(0)\) by \(H_0(1)\).

A concrete three-order family has \((n_j,\delta_j)=(2,1/2),(3,2),(4,1/2)\), and weights
\[
 \bigl(w_1,w_2,w_3\bigr)=\left(\frac58-\theta,\theta,\frac38\right),\qquad
 \theta=\frac{57}{176}-t.
\]
For sufficiently small positive \(t\), this exhibits full-cooperation/active-state bistability, with sharp exact onset coefficient
\[
 \Delta r(t)=\frac{20614528}{2170899}t^2+O(t^3).
\]

## Assumptions and scope
The number of interaction classes is finite; all \(n_j\) are integers at least two, all \(\delta_j\) are strictly positive, and class probabilities are independent of strategy frequencies. The population is well mixed, updates follow the deterministic one-dimensional replicator equation stated above, and a cooperator in a game pays the same unit cost irrespective of class. The ratio \(r\) is shared across classes. The characterization counts distinct *interior* roots; boundary equilibria always exist and coincident roots at bifurcation thresholds are not counted twice. Stability refers to the phase line within \([0,1]\), not to structured populations, finite stochastic populations, or arbitrary update rules.

## Proof
**1. Convexity and the root ceiling.** Since \(\delta_j>0\), each factor \(1+(\delta_j-1)x\) is positive on \([0,1]\). Differentiation gives
\[
 H_w''(x)=\sum_j\frac{w_j(n_j-1)(n_j-2)}{n_j}
 (\delta_j-1)^2\bigl(1+(\delta_j-1)x\bigr)^{n_j-3}\ge0.
\]
If some positively weighted class has \(n_j\ge3\) and \(\delta_j\ne1\), this second derivative is strictly positive on the entire interval. Strict convexity precludes more than two distinct intersections with any horizontal line: three such intersections would contradict the strict monotonicity of secant slopes. Otherwise \(H_w\) is affine (indeed, constant if all nonlinear contributions vanish), so it has at most one isolated horizontal-line intersection. In the exceptional constant case where \(rH_w=1\), every interior point is stationary, explaining the qualification 'isolated'.

**2. Exact existence and stability.** For two distinct interior intersections with \(H_w(x)=1/r\), strict convexity is necessary. By Rolle's theorem and strictly increasing derivative, the unique minimizer \(z\) lies between the intersections. Its derivative must be negative at \(0\) and positive at \(1\), which is exactly \(A(w)<0<B(w)\). Conversely, these two slope inequalities imply a unique \(z\in(0,1)\), and strict convexity gives \(H_w(z)<\min\{H_w(0),H_w(1)\}\). The horizontal line lies strictly above the minimum and strictly below both endpoint values exactly for the claimed interval of \(r\). The sign pattern of \(rH_w-1\) is \(+,-,+\), reading left to right, so the first interior root attracts and the second repels; the signs near \(0\) and \(1\) imply the stated boundary stability. Equality at either limit is a degenerate collision or a boundary root, not two distinct interior roots.

**3. Feasibility in weight space.** The functions \(A(w)\) and \(B(w)\) are linear. Without both discounting and synergistic classes, their signs cannot straddle zero as required. If all discounting and synergistic classes are pairwise (\(n=2\)), the remaining classes contribute zero slope and \(A=B\), so feasibility is impossible. Conversely choose one discounting class \(d\) and one synergistic class \(s\), with at least one group size at least three. Write \(p=(n_d-1)(1-\delta_d)/n_d>0\) and \(q=(n_s-1)(\delta_s-1)/n_s>0\). Set \(u=\delta_d^{n_d-2}\le1\) and \(v=\delta_s^{n_s-2}\ge1\), with \(u<v\). Assign positive weights in a ratio satisfying \(u/v<qw_s/(pw_d)<1\). Then \(A=-pw_d+qw_s<0\) but \(B=-puw_d+qvw_s>0\). Normalization leaves both inequalities unchanged. Other weights can be made small and positive if desired, without losing strictness.

**4. Quadratic opening at an endpoint.** At \(t=0\), strict positivity of \(H_0''(0)\), nonnegative \(H_0''\) everywhere and the finite-mixture formula imply \(H_0'(x)>0\) for \(0<x\le1\). Therefore \(H_0(0)<H_0(1)\). The implicit function theorem applied to \(H_t'(z(t))=0\) yields \(z(t)=\kappa t/c+O(t^2)\), and \(A(t)<0<B(t)\) for all sufficiently small positive \(t\). Taylor expansion with the affine dependence of the weights gives
\[
 H_t(0)-H_t(z(t))=\frac{\kappa^2}{2c}t^2+O(t^3).
\]
Here the smaller endpoint remains \(H_t(0)\). Thus
\[
 \Delta r(t)=\frac1{H_t(z(t))}-\frac1{H_t(0)}
 =\frac{H_t(0)-H_t(z(t))}{H_t(z(t))H_t(0)}
 =\frac{\kappa^2}{2cH_0(0)^2}t^2+O(t^3).
\]
The proof at the right endpoint is identical after substituting \(y=1-x\). Both leading coefficients are strictly positive, making the quadratic exponent sharp.

**5. Exact three-order witness.** Direct expansion of the example gives
\[
 H_t(x)=\frac{31}{88}+\frac t6-\frac{11t}{12}x+
 \left(\frac{251}{1408}-\frac t3\right)x^2-\frac3{256}x^3.
\]
Hence \(\kappa=11/12\), \(c=251/704\), \(H_0(0)=31/88\), and \(H_0'(1)=905/2816>0\). The coefficient in step 4 evaluates exactly to \(20614528/2170899\). All three weights are positive for sufficiently small positive \(t\), so the example is admissible.

## Verification
The accompanying Python standard-library file `verify.py` independently constructs the finite-mixture payoff polynomial in exact rational arithmetic. Running `python3 verify.py` checks the three-order polynomial identity, both endpoint slopes, the curvature and quadratic coefficient, a separate strict two-root witness, and a rational parameter grid of mixed games. The checker reports **1,555 exact-rational assertions passed**. These finite checks corroborate the algebra and examples; the proof above establishes the assertions for arbitrary finite numbers of interaction classes and all admissible continuous parameters.

## Relationship to prior work
Llabrés, Sadekar, Malizia, and Battiston (2026) derive the class-specific geometric-return payoff difference and analyze mixtures of **two** interaction orders, proving an at-most-two-interior-root property in that setting and an explicit pairwise/triplewise phase diagram. The present result concerns arbitrary finite mixtures, including multiple nonlinear response strengths, and adds an exact polyhedral criterion for the mixing weights and a sharp local quadratic width law at the onset boundary. These claims do not follow merely by repeating the two-order numerical phase diagram: the generalization requires the all-class curvature argument, and the onset coefficient requires a separate minimizer expansion.

Peña (2012) studies random group sizes and Jensen comparisons, notably with a shared synergy/discount rule across group sizes. Zhu et al. (2024) consider probabilistic synergy versus discounting with a fixed group size. Archetti (2018) explains general Bernstein-polynomial techniques. These supply important context and tools, but the inspected treatments do not state the combined finite-mixture endpoint-polytope characterization or its quadratic onset coefficient. Convexity and the implicit-function/Taylor tools themselves are standard; the claimed contribution is the explicit classification in this specific heterogeneous-interaction model, not a new abstract convexity theorem.

## Limitations
This is a deterministic, well-mixed, two-strategy result for finite, exogenous mixtures with a common benefit/cost ratio. It does not establish behavior on correlated hypergraphs or for strategy-dependent mixing. At \(A=0\), \(B=0\), or the two boundaries in \(r\), local linear stability can fail and the two-interior-root statement must not be applied. An all-affine constant-payoff instance can have a continuum of equilibria at one special ratio. Publication priority remains uncertain: an equivalent specialized classification in unindexed literature cannot be excluded. The computational checks are finite and do not replace the analytic arguments.

## References
1. J. Llabrés, O. Sadekar, F. Malizia, and F. Battiston, “Emergence of cooperation in nonlinear higher-order public goods games,” arXiv:2604.07228, first public preprint 8 April 2026; *Physical Review E* **114**, 034316 (2026). https://arxiv.org/html/2604.07228v2
2. J. Peña, “Group-size diversity in public goods games,” *Evolution* **66**, 623–636 (2012), first online 4 November 2011. https://doi.org/10.1111/j.1558-5646.2011.01504.x
3. W. Zhu et al., “Evolutionary dynamics in stochastic nonlinear public goods games,” *Communications Physics* **7**, 377 (2024). https://doi.org/10.1038/s42005-024-01865-6
4. M. Archetti, “How to Analyze Models of Nonlinear Public Goods,” *Games* **9**, 17 (2018). https://doi.org/10.3390/g9020017
