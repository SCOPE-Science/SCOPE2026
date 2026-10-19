# Sharp global contraction and outlier breakdown for commuting Gaussian semi-unbalanced barycenters

## Finding

The Gaussian semi-unbalanced Wasserstein barycenter's alternating-relaxation iteration has a **sharp global contraction constant without a compact-covariance assumption** whenever the input covariance matrices and the initialized barycenter commute. The same exact scalar reduction establishes a finite response to an arbitrarily large single covariance outlier, a sharp inverse-square approach to that response, and a square-root divergence as the clean mass vanishes.

Fix an integer \(d\ge 1\), a number of inputs \(n\ge1\), positive weights \(w_i\) with \(\sum_i w_i=1\), and \(\tau>0\). Consider the centered input Gaussians
\[
\alpha_i=\mathcal N\bigl(0,\operatorname{diag}(a_{i1}^2,\ldots,a_{id}^2)\bigr),\qquad a_{ij}>0.
\]
For \(a,b>0\), define the relaxed scalar standard deviation
\[
s_a(b)=\frac{b+\sqrt{b^2+\tau(2+\tau/a^2)}}{2+\tau/a^2}.
\]
The exact hybrid iteration, starting with arbitrary positive \(b_{0j}\), is
\[
b_{k+1,j}=T_j(b_{kj}):=\sum_{i=1}^n w_i s_{a_{ij}}(b_{kj}).
\]
Put
\[
q_j=\sum_{i=1}^n\frac{2w_i}{2+\tau/a_{ij}^2},\qquad q=\max_{1\le j\le d}q_j<1.
\]
Then the map is a strict global contraction in the \(2\)-Wasserstein metric between centered diagonal Gaussians, with **exact** (not merely bounded) Lipschitz constant \(q\). It has a unique positive fixed point \(b_*\), and
\[
\|b_k-b_*\|_2\le q^k\|b_0-b_*\|_2\quad\text{for every integer }k\ge0.
\]
It is also gradient descent with stepsize \(1/2\) on the exact reduced objective in standard-deviation coordinates. That objective is globally strongly convex, with **sharp** Euclidean strong-convexity modulus \(2(1-q)\).

For a sharper robustness statement, specialize to one dimension and two inputs with standard deviations \(a>0\) and \(M>0\), of respective weights \(1-w\) and \(w\), where \(0<w<1\). Let \(b_M\) be the unique semi-unbalanced barycenter standard deviation. As \(M\to\infty\), it increases to a **finite** value \(B_w\), the unique positive solution of
\[
B_w=(1-w)s_a(B_w)+w s_\infty(B_w),\qquad
s_\infty(b)=\frac{b+\sqrt{b^2+2\tau}}2.
\]
In fact,
\[
B_w-b_M=\frac{K_w}{M^2}+O_{a,\tau,w}(M^{-4}),
\]
where, writing \(R_w=\sqrt{B_w^2+2\tau}\) and \(T_\infty(b)=(1-w)s_a(b)+w s_\infty(b)\),
\[
K_w=\frac{w\tau\,s_\infty(B_w)^2}{2R_w\,[1-T_\infty'(B_w)]}>0.
\]
As the clean fraction tends to zero, the finite ceiling itself has the sharp breakdown law
\[
\lim_{w\uparrow1}\sqrt{1-w}\,B_w=\sqrt{a^2+\tau/2}.
\]
In contrast, the ordinary \(2\)-Wasserstein Gaussian barycenter has standard deviation \((1-w)a+wM\) and diverges linearly with \(M\). All asymptotics above keep \(a\) and \(\tau\) fixed and take the limits in the indicated order.

## Assumptions and scope

The semi-unbalanced cost used here is exactly
\[
\mathcal S_\tau(\alpha,\beta)=\inf_{\pi:\,\pi_y=\beta}
\left\{\int\|x-y\|_2^2\,d\pi(x,y)+\tau D_{\mathrm{KL}}(\pi_x\|\alpha)\right\},
\]
with probability marginals, the ordinary probability-relative entropy, no additional entropic coupling penalty, and fixed second marginal \(\beta\). The barycenter problem minimizes \(\sum_i w_i\mathcal S_\tau(\alpha_i,\beta)\) over centered Gaussian \(\beta\) with positive diagonal covariance in the common eigenbasis. The hybrid step first minimizes each marginal relaxation at a fixed barycenter and then computes the exact \(2\)-Wasserstein barycenter of those relaxed Gaussian marginals. No numerical error, approximate inner minimization, unequal regularization parameters, or noncommuting covariance is included. A fixed common orthogonal change of basis changes none of the conclusions.

For diagonal covariances, \(W_2\) distance between the centered input/output Gaussian distributions equals the Euclidean distance between their positive standard-deviation vectors. The scalar infinity subscript in \(s_\infty\) denotes only a limit as the input standard deviation tends to infinity; it is not itself a legitimate finite-variance Gaussian input.

## Proof

**1. Reduction is exact, not a Gaussian ansatz.** Fix one coordinate, with target \(Y\sim\mathcal N(0,b^2)\), source reference \(\mathcal N(0,a^2)\), and arbitrary admissible source marginal \(\eta\) having mean \(m\) and standard deviation \(s>0\). Cauchy–Schwarz gives
\[
\inf_{\pi:\pi_x=\eta,\,\pi_y=\beta}\mathbb E_\pi(X-Y)^2
\ge m^2+(s-b)^2.
\]
The maximum-entropy property of the Gaussian gives
\[
D_{\mathrm{KL}}(\eta\|\mathcal N(0,a^2))\ge
\tfrac12\bigl((m^2+s^2)/a^2-1-2\log(s/a)\bigr).
\]
Both bounds are equalities for \(\eta=\mathcal N(m,s^2)\) and the affine monotone Gaussian coupling, so the unrestricted marginal optimization reduces exactly to minimizing
\[
m^2\bigl(1+\tau/(2a^2)\bigr)
+(s-b)^2+\tfrac\tau2\bigl(s^2/a^2-1-2\log(s/a)\bigr).
\]
The optimal mean is zero. In \(d\) dimensions, squared transport cost separates across coordinates, and the relative-entropy chain rule implies
\[
D_{\mathrm{KL}}(\eta\|\mathop{\otimes}_{j=1}^d\alpha_j)
\ge\sum_{j=1}^dD_{\mathrm{KL}}(\eta_j\|\alpha_j).
\]
Product Gaussian marginals and product optimal couplings attain equality, proving exact coordinatewise tensorization without assuming that a nonproduct source marginal is Gaussian.

**2. Strictly convex inner minimization.** For \(s>0\) the scalar objective is
\[
h_a(s;b)=(s-b)^2+\tfrac\tau2\left(s^2/a^2-1-2\log(s/a)\right).
\]
Its second derivative is \(2+\tau/a^2+\tau/s^2>0\). Its stationarity equation is
\[
(2+\tau/a^2)s^2-2bs-\tau=0.
\]
The unique positive root is exactly \(s_a(b)\), with first derivative
\[
s_a'(b)=\frac{1+b/\sqrt{b^2+\tau(2+\tau/a^2)}}{2+\tau/a^2}.
\]
For every \(b>0\), this derivative is positive and strictly smaller than \(2/(2+\tau/a^2)<1\), and it increases to that upper bound as \(b\to\infty\).

**3. Global contraction and sharp strong convexity.** At each coordinate, the outer barycenter of the relaxed Gaussian laws has standard deviation equal to their weighted arithmetic average; this gives \(T_j\). The mean-value theorem and the preceding derivative formula imply
\[
|T_j(b)-T_j(c)|\le q_j|b-c|,
\quad\|T(b)-T(c)\|_2\le q\|b-c\|_2.
\]
The positive orthant is complete only after adjoining its boundary, but \(T\) extends continuously there and sends every boundary point to a strictly positive vector. Banach's theorem on the closed nonnegative orthant therefore gives a unique interior fixed point and convergence from all nonnegative starts, including the stipulated strictly positive ones. Sharpness follows by varying the coordinate attaining \(q\) while sending both its arguments to infinity: the difference quotient tends to \(q_j\).

Writing
\[
F(b)=\sum_{j=1}^d\sum_{i=1}^n w_i\min_{s>0}h_{a_{ij}}(s;b_j),
\]
the envelope theorem, or differentiation of the explicit optimizer, gives \(\partial_jF(b)=2[b_j-T_j(b_j)]\). Thus \(T(b)=b-\tfrac12\nabla F(b)\). Its Hessian is diagonal with entries \(2[1-T_j'(b_j)]\), each strictly positive, with infimum \(2(1-q_j)\) as \(b_j\to\infty\). Hence the exact global strong-convexity modulus is \(2(1-q)\), and the fixed point is the unique diagonal-Gaussian minimizer.

**4. Finite outlier ceiling and its sharp correction.** Implicit differentiation of the inner stationarity equation gives
\[
\frac{\partial s_a(b)}{\partial a}=
\frac{2\tau s_a(b)}{a^3(2+\tau/a^2+\tau/s_a(b)^2)}>0.
\]
Therefore the two-input map and its fixed point increase with \(M\). For any finite \(M\), its contraction factor is bounded above by \((1-w)2/(2+\tau/a^2)+w<1\), uniformly in \(M\). The pointwise limit map \(T_\infty\) has the same strict uniform contraction bound, so the increasing fixed points converge to its unique finite fixed point \(B_w\). To obtain the correction, set \(\delta=\tau/M^2\) in the exact formula for \(s_M(b)\). Differentiating its quadratic equation at \(\delta=0\) gives
\[
\left.\frac{\partial s_M(b)}{\partial\delta}\right|_{\delta=0}
=-\frac{s_\infty(b)^2}{2\sqrt{b^2+2\tau}}.
\]
The fixed-point equation is analytic in \(\delta\) near zero and its derivative in \(b\) equals \(1-T_\infty'(B_w)>0\). The ordinary implicit-function theorem now yields the positive constant \(K_w\) in the statement and a remainder of order \(M^{-4}\).

**5. Exact near-total-contamination exponent.** With \(c_a=2+\tau/a^2\), the expansions as \(b\to\infty\) are
\[
s_a(b)=\frac{2b}{c_a}+\frac\tau{2b}+O(b^{-3}),
\qquad s_\infty(b)=b+\frac\tau{2b}+O(b^{-3}).
\]
For any fixed finite \(b\), \(s_\infty(b)>b\); hence the fixed point \(B_w\) cannot remain bounded as \(w\uparrow1\). Insert the expansions in its fixed-point equation and multiply by \(B_w\). This yields
\[
(1-w)\left(1-\frac{2}{c_a}\right)B_w^2
=\frac\tau2+O(B_w^{-2}).
\]
Because \(1-2/c_a=\tau/(2a^2+\tau)\), the displayed limit \(\sqrt{1-w}\,B_w\to\sqrt{a^2+\tau/2}\) follows. The ordinary Wasserstein barycenter formula follows directly by minimizing \((1-w)(b-a)^2+w(b-M)^2\).

## Verification

Run the accompanying standalone `verify.py` with Python 3.9 or later; it uses only the standard library. Its deterministic tests cover the positive quadratic root, stationarity, analytic derivatives, the exact Lipschitz bound in multiple commuting dimensions, the gradient-descent identity, finite-outlier convergence, the inverse-square coefficient, and the square-root breakdown exponent. Its completed execution passed 7,366 assertions. The universal statements are established by the mathematical arguments above; these finite computational checks are supplementary and do not constitute exhaustive verification.

For a reproducible scalar reference point, at \(a=1\), \(\tau=2\), and \(w=1/2\), the global sharp factor in the infinite-outlier limit is \(q=3/4\). The finite contamination ceiling and coefficient are
\[
B_{1/2}=1.7156269037800918\ldots,\qquad
K_{1/2}=2.2594588405703605\ldots.
\]
The local derivative at the limiting fixed point is \(0.60259837637538\ldots\), not the worst-case global constant.

## Relationship to prior work

Nguyen, Le, Nguyen, Pham and Ho introduce the semi-unbalanced Gaussian barycenter and an alternating hybrid method, show Gaussian reduction, and prove convergence subject to bounded-spectrum assumptions; their experiments include contaminated Gaussian data. Those ingredients, the construction of the hybrid iteration, and qualitative robustness are prior work, not claimed here. This result identifies the exact dimension-free global contraction modulus and strong-convexity constant on the commuting covariance submanifold **without an a priori spectral strip**, and gives a finite-outlier ceiling together with two sharp asymptotics.

Chewi, Maunu, Rigollet and Stromme establish convergence theory for ordinary Bures-Wasserstein barycenter algorithms; their objective does not contain this KL relaxation. Altschuler, Chewi, Gerber and Stromme give dimension-free guarantees for ordinary and other regularized barycenter schemes, but that should not be conflated with the specific one-sided KL relaxation and its exact hybrid map. Janati, Muzellec, Peyré and Cuturi study entropically regularized (including unbalanced) Gaussian transport; their entropic coupling penalty and associated fixed-point equations differ from the unregularized-coupling semi-unbalanced objective used here.

## Limitations

The exact global factor applies to commuting diagonal covariance inputs and an iteration remaining in their common eigenbasis; it does not establish the same factor or global contraction for noncommuting covariance matrices or arbitrary distributions. The ceiling concerns divergence of **one covariance standard deviation** with a nonzero fixed clean weight and fixed positive regularization. It is not a general adversarial-contamination or location-outlier robustness guarantee. The square-root breakdown law takes the outlier-magnitude limit first, then the clean-weight limit. Full originality relative to all unindexed or inaccessible literature has not been independently certified.

## References

- N.-H. Nguyen, D. Le, H.-P. Nguyen, T. Pham, and N. Ho, *On Barycenter Computation: Semi-Unbalanced Optimal Transport-based Method on Gaussians*, arXiv:2410.08117, first publicly submitted 2024-10-10. https://arxiv.org/abs/2410.08117
- S. Chewi, T. Maunu, P. Rigollet, and A. J. Stromme, *Gradient descent algorithms for Bures-Wasserstein barycenters*, COLT/PMLR 125 (2020), pp. 1276–1304. https://proceedings.mlr.press/v125/chewi20a.html
- J. M. Altschuler, S. Chewi, P. Gerber, and A. J. Stromme, *Averaging on the Bures-Wasserstein manifold: dimension-free convergence of gradient descent*, arXiv:2106.08502. https://arxiv.org/abs/2106.08502
- H. Janati, B. Muzellec, G. Peyré, and M. Cuturi, *Entropic Optimal Transport between Unbalanced Gaussian Measures has a Closed Form*, arXiv:2006.02572. https://arxiv.org/abs/2006.02572
