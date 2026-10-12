# Exact coupling-invariant Euclidean risk and state-dependent batch-optimal objective in four-coordinate descent

## Finding

For fixed-size two-coordinate random batches with balanced inclusion marginals, the expected Euclidean squared error of simultaneous coordinate-gradient descent on the natural pair-coupled four-dimensional quadratic is **independent of joint sampling**. In contrast, its expected objective value depends on a single joint-inclusion parameter, with an optimal endpoint determined by initial alignment and an unbounded gap between endpoint samplings for one initial mode.

Write \(B_\rho=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix}\), \(H=\operatorname{diag}(B_\rho,B_\rho)\), \(r=(1+\rho^2)/2\), \(u_0=\|x_0\|_2^2\), and \(z_0=x_{0,1}x_{0,2}+x_{0,3}x_{0,4}\). Let \(\alpha\) be the sum of the probabilities of choosing either coupled pair \(\{1,2\}\) or \(\{3,4\}\). Then for **every** integer \(k\ge0\),

\[
\mathbb E\|x_k\|_2^2=r^k u_0,
\qquad
\mathbb E f(x_k)=r^k\left[\frac{1-\rho^2}{2(1+\rho^2)}u_0+
\alpha^k\left(\rho z_0+\frac{\rho^2}{1+\rho^2}u_0\right)\right].
\]

Here \(\alpha^0=1\), including \(\alpha=0\). For every positive horizon, the optimal \(\alpha\) equals zero when \(C=\rho z_0+\rho^2u_0/(1+\rho^2)>0\), one when \(C<0\), and any feasible value when \(C=0\). For \(x_0=(1,1,1,1)\), the objective ratio \(\mathbb E_{\alpha=1}f(x_k)/\mathbb E_{\alpha=0}f(x_k)=(1+\rho^2)/(1-\rho)\) for every \(k\ge1\). For \(x_0=(1,-1,1,-1)\), the preference is reversed.

## Assumptions and scope

Fix any real \(\rho\in(0,1)\). Optimize \(f(x)=\tfrac12x^\top Hx\) over \(x\in\mathbb R^4\), where \(H\) is the block-diagonal symmetric positive-definite matrix above and the exact minimizer is the origin. Start from an arbitrary deterministic \(x_0\in\mathbb R^4\). At each time, independently of earlier batch choices, sample **exactly** two distinct indices \(S_k\) from a fixed probability distribution on the six two-subsets of \(\{1,2,3,4\}\). Each coordinate has inclusion marginal \(\Pr(i\in S_k)=1/2\). For selected coordinates use *simultaneous, pre-update* gradients and unit diagonal scaling:

\[
x_{k+1,i}=\begin{cases}x_{k,i}-(Hx_k)_i,&i\in S_k,\\x_{k,i},&i\notin S_k.\end{cases}
\]

Thus a selected first coordinate of a pair becomes negative \(\rho\) times the *old* other coordinate. This is **not** an exact solve on a two-coordinate sampled block and **not** serial coordinate Gauss–Seidel. Expectations are over all batch histories. There is no observation noise or gradient approximation.

The inclusion constraints imply that there exist \(\alpha,\beta,\gamma\ge0\), \(\alpha+\beta+\gamma=1\), such that
\[
\Pr(\{1,2\})=\Pr(\{3,4\})=\alpha/2,
\quad \Pr(\{1,3\})=\Pr(\{2,4\})=\beta/2,
\quad \Pr(\{1,4\})=\Pr(\{2,3\})=\gamma/2.
\]
All \(\alpha\in[0,1]\) are feasible, and the formulas below depend on neither \(\beta\) nor \(\gamma\).

## Proof

**Admissible sampling laws.** Label the six pair probabilities by their indices. The four equal marginal equations, together with total probability one, give opposing-pair equalities \(p_{12}=p_{34}\), \(p_{13}=p_{24}\), \(p_{14}=p_{23}\). Hence the asserted three-parameter representation is both necessary and sufficient.

**Two closed second moments.** For any currently coupled pair \((a,b)\), the next pair equals \((a,b)\) if neither is selected, \((-\rho b,-\rho a)\) if both are selected, \((-\rho b,b)\) if only its first is selected, and \((a,-\rho a)\) if only its second is selected. The probabilities of these four cases are respectively \(\alpha/2,\alpha/2,(1-\alpha)/2,(1-\alpha)/2\). Define
\[
u_k=\mathbb E\|x_k\|_2^2,
\qquad z_k=\mathbb E(x_{k,1}x_{k,2}+x_{k,3}x_{k,4}).
\]
Directly summing the four outcomes proves, for all \(k\ge0\),
\[
u_{k+1}=r u_k,
\qquad z_{k+1}=\alpha r z_k-\frac{(1-\alpha)\rho}{2}u_k,
\qquad r=\frac{1+\rho^2}{2}.
\]
The full two-pair process may have correlated coordinates across the two blocks, but these equations use only the **marginal** four cases for each block, and so are exact without pair independence.

**Explicit solution.** Inductively \(u_k=r^k u_0\). The linear forced recurrence for \(z_k\) gives
\[
z_k=r^k\left[\alpha^k z_0-
\frac{\rho u_0}{1+\rho^2}(1-\alpha^k)\right].
\]
Since \(f(x)=\tfrac12\|x\|_2^2+\rho(x_1x_2+x_3x_4)\), substitution yields the two boxed formulas in the finding for every nonnegative integer \(k\), including the boundary samplings \(\alpha=0\) and \(\alpha=1\).

**Exact optimization and reversal.** For any \(k\ge1\), \(\alpha^k\) is strictly increasing on \([0,1]\); its coefficient is \(C\), establishing the optimal endpoint or indifference. With \(x_0=(1,1,1,1)\), \(u_0=4\), \(z_0=2\), so \(C>0\) and \(\alpha=0\) minimizes expected objective. With \(x_0=(1,-1,1,-1)\), \(u_0=4\), \(z_0=-2\), and
\[
C=-\frac{2\rho(1-\rho)^2}{1+\rho^2}<0,
\]
so \(\alpha=1\) is optimal. For the first initial vector, \(\alpha=1\) gives \(\mathbb Ef(x_k)=2(1+\rho)r^k\), whereas \(\alpha=0\) gives \(\mathbb Ef(x_k)=2(1-\rho^2)r^k/(1+\rho^2)\); their ratio is exactly \((1+\rho^2)/(1-\rho)\), tending to infinity as \(\rho\uparrow1\). At every \(\rho<1\), \(r<1\), so all expected squared Euclidean errors and objectives still converge geometrically to zero.

## Verification

The standalone `verify.py` uses only the Python 3 standard library, exact `fractions.Fraction` arithmetic, and all six legal batches. Running `python3 verify.py` prints `PASS: 1024 exact rational objective/norm/optimality identities, horizons through 5 and 8`. It explicitly propagates full state-probability dictionaries for multiple values of \(\rho\), \(\alpha\), the cross-match splitting and four starting vectors through five steps. Separate exact checks verify the endpoint-optimality inequalities and gap identity through eight steps. The infinite-horizon assertion follows from the displayed exact conditional-moment recurrence and its analytical solution, **not** from finite enumeration.

## Relationship to prior work

Hanzely and Richtárik (2018), the motivating primary source, analyze arbitrary minibatch inclusion laws in accelerated coordinate descent and nonaccelerated variants through joint-inclusion matrices and expected-separable-overapproximation bounds. The simultaneously updated gradient-coordinate primitive and arbitrary sampling are directly related. Their inspected algorithm, theorem and appendix sections give sufficient rate bounds, but not the present exact two-moment identity, invariance of expected Euclidean error under **all** balanced joint laws, nor the state-dependent sharp objective-ratio comparison. Qu and Richtárik (2014) develop the joint-inclusion and ESO formalism; their inspected statements are upper bounds rather than the exact coupled-moment recurrence. Xie and Yang (2026) study randomized **exact block solves**, which do not implement the simultaneous per-coordinate step here.

In related published results, the inverse-positive SPD sampling theorem addresses an **iid single-coordinate** law and a worst-case **one-step** energy contraction objective, not a fixed-size-two joint law or initial-state-dependent finite-horizon objective. The weighted-Jacobi Euclidean-safety result concerns **deterministic all-coordinate** relaxation, not the present balanced random batch sampling. Other serial Gauss–Seidel and volume-sampled block-minimization results have different updates. These differences are statement-level comparisons, not conclusions drawn solely from titles. Cross-literature priority risk remains, especially from finite-state random matrix, simultaneous randomized Jacobi and balanced-design sampling treatments not indexed in the inspected sources.

## Limitations

Only the specified two coupled positive-definite coordinate pairs, exact simultaneous unit-step updates, a fixed independent-in-time two-subset law with marginals one half, and exact arithmetic are covered. The claim establishes a **fixed-horizon and all-horizon expected-objective** sampler comparison for a prescribed initial state; it does **not** establish a universal sampler for unknown initial data, arbitrary Hessians, noisy gradients, nonlinear objectives, stronger norm guarantees, or an improved exponential rate. The unbounded ratio concerns asymptotic prefactors at fixed positive time as the Hessian approaches singularity, not divergence at fixed \(\rho<1\). The full uniqueness of individual distributions at \(\alpha=0\) is not asserted: only the parameter \(\alpha\) is uniquely optimal when \(C\ne0\).

## References

1. Filip Hanzely and Peter Richtárik, *Accelerated Coordinate Descent with Arbitrary Sampling and Best Rates for Minibatches*, arXiv:1809.09354v1 (first posted September 25, 2018), https://arxiv.org/abs/1809.09354v1.
2. Zheng Qu and Peter Richtárik, *Coordinate Descent with Arbitrary Sampling II: Expected Separable Overapproximation*, arXiv:1412.8063v1 (first posted December 27, 2014), https://arxiv.org/abs/1412.8063v1.
3. Dong-Yue Xie and Xi Yang, *On randomized batch-sampling coordinate descent methods for solving linear least-squares problems*, arXiv:2610.04685v1 (2026), https://arxiv.org/abs/2610.04685v1; uses exact sampled-block solves rather than the simultaneous coordinate steps considered here.
4. *Closed-form optimal coordinate sampling for inverse-positive SPD quadratics*, published research result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-inverse-positive-optimal-coordinate-sampling--82c9d23eb995; addresses one-coordinate fixed iid sampling.
5. *Sharp Euclidean damping frontier for weighted Jacobi on 2×2 SPD systems*, published research result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-weighted-jacobi-euclidean-damping-frontier--457b47fc383f; addresses deterministic whole-vector Jacobi.
