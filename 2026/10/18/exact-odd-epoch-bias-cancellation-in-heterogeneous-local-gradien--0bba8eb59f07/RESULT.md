# Exact odd-epoch bias cancellation in heterogeneous local gradient descent

## Finding

Full averaging after several local gradient steps can converge to the *true* minimum of a heterogeneous quadratic objective without bias correction, but this center-independent exactness occurs at nontrivial fixed stepsizes only for **odd** local epoch counts and exactly two sufficiently close curvature values. The following theorem gives the complete scalar classification and its sharp large-epoch boundary layer.

**Theorem (full-averaging local-gradient exactness and its parity frontier).** Let \(N\ge2\), let \(h_i>0\) be scalar curvatures, and let the centers \(c_i\in\mathbb R\) be arbitrary. Set
\[
f_i(x)=\tfrac12h_i(x-c_i)^2,\qquad f(x)=N^{-1}\sum_{i=1}^N f_i(x),\qquad x_*=\frac{\sum_i h_ic_i}{\sum_i h_i}.
\]
For an integer \(E\ge1\), run \(E\) exact gradient steps of common length \(\alpha\) on each \(f_i\), starting from a common synchronized value, and then average all local iterates equally. Repeat, with
\[
0<\alpha<\frac{2}{\max_i h_i}.
\]
The synchronized values always converge geometrically to a unique limit. This limit equals \(x_*\) **for every choice of centers** precisely in the following cases:

1. \(E=1\), with arbitrary admissible \(\alpha\).
2. \(E\ge2\) even, when and only when all \(h_i\) are equal.
3. \(E\ge3\) odd, either when all \(h_i\) are equal, or when the distinct curvatures are exactly \(\{a,b\}\), where \(0<a<b<2a\), and \(\alpha=\alpha_E(a,b)\) is the **unique** root in \((1/a,2/b)\) of
\[
F_E(\alpha a)=F_E(\alpha b),\qquad F_E(z)=\frac{1-(1-z)^E}{z}.
\]

For \(E=3\), the exceptional step has the particularly simple form
\[
\alpha_3(a,b)=\frac{3}{a+b}.
\]
For fixed \(1<b/a<2\), the exceptional steps satisfy the sharp odd-epoch asymptotic
\[
\lim_{\substack{E\to\infty\\ E\ \mathrm{odd}}} E\bigl(2-\alpha_E(a,b)b\bigr)=-\log\bigl(b/a-1\bigr).
\]
If a fraction \(q\in(0,1)\) of agents has curvature \(b\) (the remainder has curvature \(a\)), the synchronized contraction multiplier at the exceptional step tends to \(-q(b/a-1)\) along odd \(E\to\infty\).

In particular, a nontrivial exactness step can occur only in the *oscillatory but individually stable* gradient range; it cannot occur when all local one-step multipliers are nonnegative.

## Assumptions and scope

The scheme is the full-averaging specialization of the multiple-local-updates/single-combination inexact gradient construction: the mixing matrix is \(W=\mathbf1\mathbf1^{\mathsf T}/N\). The averaging is performed **after** all \(E\) local gradient steps. Every communication-round output is therefore synchronized, but within-round local states generally disagree. There is no gradient tracking, correction, stochastic noise, inertia, or diminishing step length.

The result is deterministic, scalar, finite-client, fixed-step and exact-arithmetic. “Exactness” means the communication-round limit agrees with the minimizer of the *original* sum **uniformly over all assignments of the centers**. It does not assert exactness at every intermediate local iterate, at every timestep, for partially mixing graphs, or for arbitrary vector quadratics. Equality for a particular special choice of centers can also occur outside this classification through cancellation; such accidental equality is not the statement classified here.

The upper bound on \(\alpha\) is open and ensures every individual local-gradient multiplier lies strictly between \(-1\) and \(1\). At the boundary and beyond, the theorem makes no convergence assertion.

## Proof

**1. Exact communication-round map.** Starting at a common real number \(z_k\), local gradient descent on the \(i\)-th quadratic satisfies
\[
x_i^{(j+1)}=c_i+(1-\alpha h_i)(x_i^{(j)}-c_i),\qquad x_i^{(0)}=z_k.
\]
Induction yields
\[
x_i^{(E)}=r_i z_k+(1-r_i)c_i,\qquad r_i=(1-\alpha h_i)^E.
\]
Consequently the full averaging map is
\[
z_{k+1}=\bar r\,z_k+\frac1N\sum_{i=1}^N(1-r_i)c_i,\qquad\bar r=\frac1N\sum_i r_i.
\]
The strict stepsize bound gives \(|1-\alpha h_i|<1\), hence \(|r_i|<1\) and \(|\bar r|<1\). Thus the map is an affine contraction with unique fixed point
\[
z_\infty=\frac{\sum_i(1-r_i)c_i}{\sum_i(1-r_i)},\qquad z_k-z_\infty=\bar r^k(z_0-z_\infty).
\]
Each \(1-r_i\) is positive, including when the one-step multiplier is negative. The convergence statement follows without invoking an external convergence estimate.

**2. Uniform exactness is equality of dimensionless curvature distortions.** Write
\[
1-r_i=\alpha h_i F_E(\alpha h_i),\qquad F_E(z)=\sum_{j=0}^{E-1}(1-z)^j.
\]
The two fixed-point formulas are linear combinations of the arbitrary centers. They agree for every \((c_1,\ldots,c_N)\) if and only if their normalized coefficients agree individually:
\[
\frac{1-r_i}{\sum_j(1-r_j)}=\frac{h_i}{\sum_j h_j}\qquad(1\le i\le N).
\]
Since every \(h_i>0\), this is equivalent to a common value of \(F_E(\alpha h_i)\) for all agents. This coefficientwise equivalence—not agreement for one selected center vector—is the classification criterion.

**3. Even epochs are rigid.** For \(E=1\), \(F_1\equiv1\). For even \(E\ge2\), put \(u=1-z\in(-1,1)\). Since
\[
F_E(z)=\frac{1-u^E}{1-u},\qquad
\frac{\mathrm d}{\mathrm d u}\frac{1-u^E}{1-u}
=\frac{1-Eu^{E-1}+(E-1)u^E}{(1-u)^2},
\]
the derivative with respect to \(u\) is strictly positive. For \(-1<u<0\), the numerator is \(1+E|u|^{E-1}+(E-1)|u|^E>0\). For \(0\le u<1\), positivity follows directly from the finite sum \(\sum_{j=1}^{E-1}ju^{j-1}>0\). Because \(u=1-z\) decreases as \(z\) increases, \(F_E\) is strictly decreasing on \((0,2)\). All distortions are equal if and only if the curvatures are equal.

**4. Odd epochs have exactly one fold.** Let \(E\ge3\) be odd. On \(0<z<1\), \(F_E(z)=1+u+\cdots+u^{E-1}>1\) with \(u=1-z\in(0,1)\), and \(F_E\) is strictly decreasing in \(z\). At \(z=1\), \(F_E(1)=1\). For \(1<z<2\), write \(z=1+t\), \(0<t<1\), obtaining
\[
F_E(1+t)=g_E(t):=\frac{1+t^E}{1+t}<1.
\]
Its derivative has the sign of
\[
H_E(t)=Et^{E-1}+(E-1)t^E-1,
\]
which increases strictly from \(-1\) to \(2E-2\) on \((0,1)\). Hence \(g_E\) decreases to a single strict minimum and then increases. A horizontal level of \(F_E\) in \((0,2)\) contains at most two distinct points, and any two distinct points sharing a level lie strictly in \((1,2)\) on opposite sides of that minimum. Therefore three distinct curvature values can never have equal distortions. Furthermore, for two different curvatures \(a<b\), equality forces \(\alpha a>1\) and \(\alpha b<2\), possible only if \(b<2a\).

Conversely, take \(0<a<b<2a\). On the nonempty interval \(\alpha\in(1/a,2/b)\), define \(D(\alpha)=F_E(\alpha a)-F_E(\alpha b)\). At its left endpoint, the smaller argument is \(1\), and the larger lies in \((1,2)\), so \(D(1/a)>0\). At its right endpoint, the larger argument is \(2\), where \(F_E(2)=1\) for odd \(E\), while the smaller lies in \((1,2)\); hence \(D(2/b)<0\). Continuity gives at least one root.

At any root, the two arguments straddle the unique minimizer of \(g_E\), so
\[
D'(\alpha)=aF_E'(\alpha a)-bF_E'(\alpha b)<0.
\]
Every zero is thus a strict crossing from positive to negative. Two distinct zeros would require at least one intervening zero that does not cross this way (by continuity and the intermediate value theorem), a contradiction. The root is unique. The positivity of the distortion weights and the affine contraction from step 1 then prove convergence to the exact original minimizer for all centers. Finally, \(F_3(z)=3-3z+z^2\), so equality for distinct curvatures reduces to \(\alpha=3/(a+b)\), and \(b<2a\) is exactly the condition making this value admissible in \((1/a,2/b)\).

**5. Odd-epoch near-boundary limit.** Fix \(\kappa=b/a\in(1,2)\), and let \(\alpha_E\) denote the unique exceptional step for odd \(E\ge3\). It belongs to the compact closure \([1/a,2/b]\). Any convergent subsequence staying away from \(2/b\) would satisfy \(\alpha_E a\to z_a\in[1,2/\kappa)\) and \(\alpha_E b\to z_b\in[\kappa,2)\). On compact subsets of \((0,2)\), the geometric identity gives \(F_E(z)\to1/z\) as \(E\to\infty\); this applies also at \(z=1\). The limiting equality would give \(1/z_a=1/z_b\), impossible because \(b>a\). Thus
\[
\alpha_E b\longrightarrow2.
\]
Let \(t_{a,E}=\alpha_Ea-1\) and \(t_{b,E}=\alpha_Eb-1\). Both belong to \((0,1)\), with \(t_{a,E}\to2/\kappa-1<1\) and \(t_{b,E}\to1\). The defining equality of \(F_E\) is equivalent to
\[
1+t_{b,E}^E=\kappa(1+t_{a,E}^E),\qquad
 t_{b,E}^E\longrightarrow\kappa-1\in(0,1).
\]
Writing \(\delta_E=2-\alpha_Eb=1-t_{b,E}\to0\), logarithms give
\[
E\log(1-\delta_E)\to\log(\kappa-1),\qquad
E\delta_E\to-\log(\kappa-1),
\]
using \(\log(1-\delta)/(-\delta)\to1\). If \(qN\) agents have curvature \(b\), the communication-round factor is \(\bar r_E=-(1-q)t_{a,E}^E-qt_{b,E}^E\to-q(\kappa-1)\), as asserted.

**6. Exact rational witness.** Take two agents with
\[
h_1=1,\quad h_2=\tfrac32,\quad c_1=0,\quad c_2=1,\quad
\alpha=\tfrac65.
\]
The global minimizer is \(x_*=3/5\). For \(E=3\), the local round multipliers are \(r_1=-1/125\) and \(r_2=-64/125\). The common synchronized fixed point is exactly \(3/5\), and its error follows
\[
z_{k+1}-\tfrac35=-\tfrac{13}{50}(z_k-\tfrac35).
\]
With the *same* inputs and step length but \(E=2\), the round multipliers become \(1/25\) and \(16/25\), so \(z_\infty=3/11\ne3/5\). This verifies that the parity distinction is observable within strictly stable local gradient steps.

## Verification

The standalone file `verify.py` uses only standard-library exact rational arithmetic and high-precision decimal arithmetic. It performs direct local-gradient steps and compares them with the derived affine round map over multiple center and curvature configurations. It checks the cubic tuning rule and rational bias/no-bias witnesses exactly. It separately brackets exceptional odd-epoch steps and checks the predicted large-epoch scaling for selected values. Running `python verify.py` prints a check count and the exact witness values. These computations are *illustrations and finite consistency checks*; the claims for all epoch counts, all curvatures and the infinite-epoch limit are supported by the analytic proof above, not by numeric enumeration.

## Relationship to prior work

Wu, Liao, Ding and Xiao [1] introduced the inexact MUSIC method (their update equations (7)–(9)) and analyzed its neighborhood convergence with a sufficient small-step condition. This theorem specializes its full-averaging communication matrix to scalar heterogeneous quadratics and supplies a distinct exactness question, including an exceptional oscillatory stepsize outside those sufficient bounds. It does **not** assert that the original general error-bound theorem fails.

Charles and Konečný [2, Theorem 1 and equations (6)–(8)] had already derived the exact surrogate Hessian distortion of deterministic federated local updates: the polynomial \(F_E\), up to normalization, is the scalar version of their distortion operator. Thus the affine map, the surrogate-weight viewpoint and the possibility of objective misalignment are **prior methods**, not separate novelty claims. The new statement is the complete **parity-dependent level-set classification** of that polynomial within the full individually stable range, the sharp factor-of-two curvature obstruction, the unique odd-epoch equality step, and its boundary-layer law.

Wang and collaborators [3] introduced average drift at the optimum and showed that data heterogeneity need not force an optimization bias in general. Their statistical cancellation mechanism and convergence estimates do not state this all-centers deterministic two-curvature classification. Charles and Rush [4] established conservatism of iterated gradient fields, which includes quadratics, but did not classify exact empirical-minimizer preservation by local update parity. Khaled, Mishchenko and Richtárik [5, 6] obtained broad small-step analyses, rather than the sharp oscillatory-stepsize exactness window considered here.

## Limitations

The theorem concerns a special, exactly solvable class: scalar positive-curvature quadratics, one shared stable step length, equal full averaging every fixed number of local steps, and synchronization-time outputs. In particular, local iterates before averaging generally approach an \(E\)-periodic within-round profile and need not converge to the global optimizer. Curvature heterogeneity with three or more levels cannot be repaired by this *one-parameter* cancellation mechanism, but this says nothing about other algorithms with more tunable parameters. Robustness to perturbations of the step length, noisy gradients, partial network mixing or matrix-valued Hessians is not quantified. The near-boundary odd-epoch tuning can be sensitive in finite precision. Independent external validation and exhaustive priority certification are not claimed.

## References

[1] M. Wu, H. Liao, Z. Ding, Y. Xiao, “MUSIC: Accelerated Convergence for Distributed Optimization With Inexact and Exact Methods,” arXiv:2403.02589v1 (first posted 2024-03-05), https://arxiv.org/abs/2403.02589.

[2] Z. Charles, J. Konečný, “Convergence and Accuracy Trade-Offs in Federated Learning and Meta-Learning,” AISTATS/PMLR 130 (2021), pp. 2575–2583, https://proceedings.mlr.press/v130/charles21a.html.

[3] J. Wang, R. Das, G. Joshi, S. Kale, Z. Xu, T. Zhang, “On the Unreasonable Effectiveness of Federated Averaging with Heterogeneous Data,” arXiv:2206.04723v1 (2022), https://arxiv.org/abs/2206.04723.

[4] Z. Charles, K. Rush, “Iterated Vector Fields and Conservatism, with Applications to Federated Learning,” ALT/PMLR 167 (2022), pp. 130–147, https://proceedings.mlr.press/v167/charles22a.html.

[5] A. Khaled, K. Mishchenko, P. Richtárik, “First Analysis of Local GD on Heterogeneous Data,” arXiv:1909.04715 (2019), https://arxiv.org/abs/1909.04715.

[6] A. Khaled, K. Mishchenko, P. Richtárik, “Tighter Theory for Local SGD on Identical and Heterogeneous Data,” arXiv:1909.04746 (2019), https://arxiv.org/abs/1909.04746.
