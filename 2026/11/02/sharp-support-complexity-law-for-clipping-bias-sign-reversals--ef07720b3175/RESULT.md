# Sharp support-complexity law for clipping-bias sign reversals

## Finding

**Theorem (sharp support complexity and realizable mean-drift reversals).** Let \(Z\) be a finitely supported, real, mean-zero random variable, and let \(m\ge2\) be the number of distinct *nonzero absolute magnitudes* in its support. For every clipping cap \(c>0\), define
\[
T_c(t)=\max\{-c,\min\{t,c\}\},\quad b(c)=\mathbb E[T_c(Z)],\quad F_c(x)=\mathbb E[T_c(x+Z)].
\]
As \(c\) increases, the sign of the mean clipping bias \(b(c)\) can reverse at most \(m-2\) times. A reversal means a transition between intervals on which the continuous function is strictly positive and strictly negative; intervals where it vanishes identically do not themselves count as reversals.

The bound is **sharp simultaneously for every integer \(m\ge3\)**. There is a mean-zero distribution on exactly \(m\) nonzero magnitudes, with strictly positive rational atom probabilities, for which the bias has exactly \(m-2\) alternating sign reversals, at the caps
\[
c=\frac32,\frac52,\ldots,m-\frac32.
\]
For each distribution in this explicit family, \(F_c\) has a unique zero \(x_c\) for every \(c>0\). It satisfies \(\operatorname{sgn}(x_c)=-\operatorname{sgn}(b(c))\), so the unique mean-drift equilibrium crosses the *true* stochastic-quadratic minimizer exactly \(m-2\) times as the cap is increased. Furthermore, for each fixed cap \(c>0\) and every \(0<\eta<2\), deterministic population clipped-gradient descent
\[
x_{k+1}=x_k-\eta F_c(x_k)
\]
converges to \(x_c\) from every real initialization.

Thus three distinct gradient-noise magnitudes are necessary and sufficient for one clipping-threshold reversal, while any prescribed number of reversals can be realized with a correspondingly small, finite, bounded-noise quadratic model.

## Assumptions and scope

The underlying component objectives are \(f_z(x)=\tfrac12(x+z)^2\) for \(x\in\mathbb R\). Because \(\mathbb E Z=0\), their population objective is \(f(x)=\tfrac12 x^2+\tfrac12\mathbb E Z^2\), with its unique minimizer at zero. Clipping is the ordinary scalar Euclidean-norm clipping operator, not clipping of objective values. There is no assumption of equal atom probabilities, equal spacing, or symmetry in the upper bound; the sharp construction uses integer-spaced magnitudes. The variable \(c\) is a deterministic threshold and the gradient noise \(Z\) does not change with \(c\) or \(x\).

The theorem concerns expected clipped gradients and deterministic iterations that use that expectation. It does **not** assert almost-sure convergence of constant-step stochastic SGD driven by a fresh sampled gradient at each step.

## Proof

### Universal upper bound

List the distinct nonzero absolute values of \(Z\) as \(0<a_1<\cdots<a_m\). Define their *signed masses*
\[
w_i=\mathbb P(Z=a_i)-\mathbb P(Z=-a_i),\qquad 1\le i\le m.
\]
Mass at zero, if any, contributes nothing to \(b\). Consequently
\[
b(c)=\sum_{i=1}^m w_i\min\{a_i,c\},\qquad \sum_{i=1}^m a_iw_i=\mathbb E Z=0.
\]
The function \(b\) is continuous and affine on each interval between successive magnitudes. Moreover \(b(0)=0\) and \(b(c)=0\) for all \(c\ge a_m\). Every connected interval on which \(b\) is strictly nonzero and maintains one sign contains at least one knot \(a_i\) with \(1\le i\le m-1\) and \(b(a_i)\ne0\): an affine function vanishing at both endpoints of a knot interval is identically zero there. Distinct sign-components use distinct knots. Thus at most \(m-1\) nonzero sign-components can alternate, and there are at most \(m-2\) reversals. This remains true when signed masses vanish or there are zero intervals. In particular, the two-magnitude case permits no reversals.

### A family attaining every bound

Fix \(m\ge3\), and set \(v_0=v_m=0\) and \(v_i=(-1)^{i-1}\) for \(1\le i\le m-1\). Define
\[
s_i=v_{i+1}-v_i\quad(0\le i<m),\qquad s_m=0,\qquad w_i=s_{i-1}-s_i\quad(1\le i\le m).
\]
Every \(w_i\ne0\); direct differences give \(\sum_{i=1}^m|w_i|=W=4m-5\), an odd positive integer. Put
\[
\mathbb P\bigl(Z=i\operatorname{sgn}(w_i)\bigr)=\frac{|w_i|}{W},\qquad 1\le i\le m.
\]
These are strictly positive probabilities adding to one. Since the telescoping slopes sum to \(v_m-v_0=0\),
\[
\mathbb E Z=\frac1W\sum_{i=1}^m iw_i=\frac1W\sum_{i=0}^{m-1}s_i=0.
\]
On the interval \(j<c<j+1\), where \(0\le j<m\),
\[
b'(c)=\frac1W\sum_{i=j+1}^m w_i=\frac{s_j}{W}.
\]
As \(b(0)=0\), this proves \(b(i)=v_i/W\) for all integer knots \(0\le i\le m\). Adjacent nonzero knot values alternate between \(1/W\) and \(-1/W\). Affine interpolation gives a unique simple zero in each interval \((i,i+1)\), \(1\le i\le m-2\), at \(c=i+1/2\). There are no other strict sign reversals. This proves sharpness for every \(m\).

For illustration, the minimal three-atom law is
\[
\mathbb P(Z=1)=\frac37,\quad\mathbb P(Z=-2)=\frac37,\quad\mathbb P(Z=3)=\frac17.
\]
It has zero mean, and its clipped mean is
\[
b(c)=\frac17\begin{cases}
c,&0<c\le1,\\
3-2c,&1\le c\le2,\\
c-3,&2\le c\le3,\\
0,&c\ge3.
\end{cases}
\]
The mean clipped gradient at the true minimizer is positive for \(0<c<3/2\), negative for \(3/2<c<3\), and zero for \(c=3/2\) and for all \(c\ge3\).

### Unique equilibria and globally convergent population iteration

For every \(c>0\), \(F_c(x)\) is continuous, nondecreasing and \(1\)-Lipschitz, and tends to \(-c\) and \(c\) as \(x\to-\infty\) and \(x\to+\infty\), respectively. Thus it has at least one zero. If it vanished at two distinct points, monotonicity of each positively weighted clipped term would force *all* terms to remain constant throughout the connecting interval. Their sum would then be \(c\) times the difference of probabilities of two complementary subsets of the atoms; its vanishing would require one subset to have probability exactly \(1/2\). All probabilities have integer numerators over the odd denominator \(W=4m-5\), so this is impossible. Hence \(x_c\) is unique and its sign is opposite to that of \(F_c(0)=b(c)\), with zero equilibrium exactly when \(b(c)=0\).

Finally, for \(x_*:=x_c\), monotonicity and the \(1\)-Lipschitz property imply \((x-x_*)F_c(x)\ge F_c(x)^2\). For any \(0<\eta<2\),
\[
|x-\eta F_c(x)-x_*|^2\le|x-x_*|^2-\eta(2-\eta)F_c(x)^2.
\]
The distance is nonincreasing and the squared residuals are summable. Boundedness, continuity, and uniqueness of the zero imply that the full deterministic population sequence converges to \(x_*\).

## Verification

A standalone standard-library Python verifier is supplied as `verify.py`. Running `python verify.py` verifies exact rational identities, all knot values and half-integer crossings for every \(3\le m\le80\), elementary root-direction diagnostics, the complete three-atom example, and independent numerical monotonicity/Lipschitz checks. Its output is `VERIFY_OK exact_family_m=3..80; all_midpoint_zeros; signs; unique_root_diagnostics; random_monotone_lipschitz=2000`. These finite checks are consistency tests; the arbitrary-\(m\) theorem is proved analytically above.

## Relationship to prior work

Classical Huber location M-estimation uses the same clipped-score equation, and the equivalence is explicitly acknowledged. Prior stochastic-gradient clipping research established biased equilibria and general convergence-neighborhood bounds, including explicit fixed-threshold two-point examples. The result here instead counts, sharply in the number of noise magnitudes, how often *the same* centered gradient law can reverse the direction of its clipping-induced mean drift as the cap varies. It provides distributions realizing every allowed count, with a unique globally attractive population fixed point at every cap. Such a count is not established in the specifically inspected primary sources. A specialized statement in classical Huber-path literature remains a publication-priority risk.

## Limitations

The theorem is scalar and applies to a fixed finite noise law on quadratic component losses. For noise laws with infinitely many distinct magnitudes no finite crossing bound is asserted. The global convergence assertion is for deterministic expected-gradient iteration, not for individual constant-step stochastic trajectories. The finding does not provide a privacy guarantee, finite-sample risk comparison, or advice that any particular clipping threshold is optimal. Although the algebraic Huber-score interpretation is classical, no independent publication-priority assessment has been performed.

## References

1. A. Koloskova, H. Hendrikx, and S. U. Stich, *Revisiting Gradient Clipping: Stochastic bias and tight convergence guarantees*, Proceedings of Machine Learning Research **202** (2023), 17343–17363; public preprint arXiv:2305.01588, first posted 2023-05-02. https://proceedings.mlr.press/v202/koloskova23a.html
2. X. Chen, Z. S. Wu, and M. Hong, *Understanding Gradient Clipping in Private SGD: A Geometric Perspective*, arXiv:2006.15429 (2020). https://arxiv.org/abs/2006.15429
3. J. Qian, Y. Wu, B. Zhuang, S. Wang, and J. Xiao, *Understanding Gradient Clipping In Incremental Gradient Methods*, Proceedings of Machine Learning Research **130** (2021), 1504–1512. https://proceedings.mlr.press/v130/qian21a.html
4. P. J. Huber, *Robust Estimation of a Location Parameter*, The Annals of Mathematical Statistics **35** (1964), 73–101. General clipped-score/Huber M-estimator background only; the primary full text was not inspected for priority.
