# Two distinct optimal-coupling transitions for stochastic extragradient on a bilinear game

## Finding

Fix two samplewise bilinear saddle operators \(F_u(z)=uJz\) on \(\mathbb R^2\), where \(u\in\{1,2\}\) and \(J=\begin{psmallmatrix}0&1\\-1&0\end{psmallmatrix}\). Each of two stochastic oracle calls has uniform marginal distribution over \(\{1,2\}\). Let the two calls within one extragradient step have *any coupling* of those marginals; successive pairs are independent and identically distributed. With common positive stepsize \(\eta\), write \(x=\eta^2\) and \(q=\Pr\{U=V\}\in[0,1]\).

For every nonzero initial point \(z_0\), every integer \(n\ge1\), and every \(x>0\),
\[
\mathbb E\|z_n\|^2=\|z_0\|^2R(q,x)^n,
\quad
R(q,x)=q\left(1-\tfrac52x+\tfrac{17}{2}x^2\right)
+(1-q)\left(1-\tfrac32x+4x^2\right).
\]
The unique mean-square-optimal coupling (apart from a tie) is \(q=1\) for \(0<x<2/9\), and \(q=0\) for \(x>2/9\). At \(x=2/9\), every feasible coupling ties. Thus the optimizer changes from shared samples to complementary samples. The optimal expected squared error decreases geometrically for every nonzero initial state if and only if \(0<x<3/8\), with sharp boundary \(3/8\). By comparison, the common-sample and independent-sample schemes have mean-square stability intervals \(0<x<5/17\) and \(0<x<8/25\), respectively.

The almost-sure optimal coupling has a different transition. Define the sample-path squared-norm exponent
\[
\Lambda(q,x)=\lim_{n\to\infty}\frac1n\log\frac{\|z_n\|^2}{\|z_0\|^2},
\]
which exists almost surely and is deterministic. Throughout the complete mean-square-stabilizable region \(0<x<3/8\), it is uniquely minimized by \(q=1\) for \(x<x_{\rm typ}\), by \(q=0\) for \(x>x_{\rm typ}\), and by every coupling at equality, where
\[
x_{\rm typ}=\frac{13-\sqrt{105}}{16}=0.1720655771\ldots
< x_{\rm ms}=\frac29.
\]
Consequently, on the entire open interval \(x_{\rm typ}<x<2/9\), a shared sample minimizes expected squared error at every finite horizon, but complementary sampling has the better almost-sure exponential decay rate. At \(x=1/5\), the two mean-square factors are \(21/25\) (shared) and \(43/50\) (complementary), while the corresponding almost-sure squared-norm exponents are \(\log(21/25)\) and \(\tfrac12\log(406/625)\); the latter is more negative.

## Assumptions and scope

The underlying convex-concave game is \(\min_s\max_t\,\mathbb E[U]st=(3/2)st\), with unique saddle at the origin and samplewise operators \(F_u(s,t)=(ut,-us)\). All sampling pairs \((U_k,V_k)\) are independent across iterations. Each call separately has \(\Pr\{U_k=1\}=\Pr\{U_k=2\}=\Pr\{V_k=1\}=\Pr\{V_k=2\}=1/2\); correlations within a pair are unrestricted. Every step takes the same \(\eta>0\) in its prediction and correction calls:
\[
z_{k+1/2}=z_k-\eta F_{U_k}(z_k),\qquad z_{k+1}=z_k-\eta F_{V_k}(z_{k+1/2}).
\]
No momentum, averaging, adaptive sampling, regularization, stochastic intercept, or projection is included. The error criterion is the distance from the origin, not an arbitrary duality gap. The two oracle evaluations have the same fixed count for all couplings. The full exact finite-horizon identity holds for all \(\eta>0\); the comparison of almost-sure optimal policies is asserted on \(0<\eta^2<3/8\).

## Proof

**Joint-law reduction.** Every coupling of two uniform \(\{1,2\}\) marginals is uniquely specified by \(q\in[0,1]\):
\[
\Pr(1,1)=\Pr(2,2)=q/2,\qquad
\Pr(1,2)=\Pr(2,1)=(1-q)/2.
\]
No independence between the two within-step calls is assumed. The cases \(q=1\), \(q=0\), and \(q=1/2\) correspond to shared, complementary, and independent calls.

**Pathwise gain.** Using \(J^\top=-J\) and \(J^2=-I\), the update matrix conditioned on \((U,V)=(u,v)\) is
\[
M_{uv}=(1-\eta^2uv)I-\eta vJ,
\quad M_{uv}^\top M_{uv}=g_{uv}(x)I,
\quad g_{uv}(x)=(1-xuv)^2+xv^2>0.
\]
Therefore the squared norm multiplies by \(g_{uv}(x)\) **for every current direction**. The four polynomials are
\[
\begin{aligned}
g_{11}&=1-x+x^2, &g_{22}&=1-4x+16x^2,\\
g_{12}&=1+4x^2, &g_{21}&=1-3x+4x^2.
\end{aligned}
\]
Independence of pairs across steps now gives the displayed finite-horizon mean-square identity, with \(R(q,x)=\mathbb E[g_{UV}(x)]\). In particular, \(R\) is strictly positive.

**Mean-square policy and stability.** Put \(R_{\rm sh}=(g_{11}+g_{22})/2\) and \(R_{\rm co}=(g_{12}+g_{21})/2\). The difference factors as
\[
R_{\rm sh}-R_{\rm co}=\frac{x(9x-2)}2.
\]
Because \(R(q,x)=qR_{\rm sh}+(1-q)R_{\rm co}\), minimizing at every positive finite horizon selects exactly the stated endpoints and tie. Direct factoring gives
\[
R_{\rm sh}-1=\frac{x(17x-5)}2,\qquad
R_{\rm co}-1=\frac{x(8x-3)}2.
\]
As \(0<2/9<5/17<3/8\), the minimum over all couplings is strictly below one exactly for \(0<x<3/8\). For independent samples \(q=1/2\), its factor is \(1-2x+25x^2/4\), which is below one exactly for \(0<x<8/25\). At or above each boundary, mean-square geometric convergence does not hold for the specified policy.

**Almost-sure policy and strict disagreement.** The gains are strictly positive, so the strong law of large numbers for the independent, finite-valued sequence \(\log g_{U_kV_k}(x)\) gives
\[
\Lambda(q,x)=\frac q2\log(g_{11}g_{22})+
\frac{1-q}{2}\log(g_{12}g_{21}).
\]
The sign of the slope in \(q\) is the sign of the difference of products; exact expansion yields
\[
g_{11}g_{22}-g_{12}g_{21}=-x(8x^2-13x+2).
\]
The two positive roots of the quadratic are \(x_\pm=(13\pm\sqrt{105})/16\). Since \(0<x_-<2/9<3/8<x_+\), the affine expression in \(q\) selects shared sampling below \(x_-\), complementary sampling above \(x_-\), and all couplings at the tie, throughout \(0<x<3/8\). To check \(x_-<2/9\) without relying on decimals, the inequality reduces to \(85<9\sqrt{105}\), whose square is \(7225<8505\). For \(x=1/5\), substitution gives the exact factors and products claimed above: \(g_{11}g_{22}=441/625\) and \(g_{12}g_{21}=406/625\). Thus the mean-square and typical-path preferences strictly disagree there.

## Verification

Execute `python verify.py` in an environment with the dependency in `requirements.txt`. The checker recomputes all four update matrices, the scalar norm gains, factorization identities, exact endpoint/stability values, and the finite-horizon norm expectation by independent exact-rational enumeration through four steps at several step sizes and coupling values. The checker contains 84 exact symbolic and rational assertions. These finite checks corroborate the displayed algebra; the full-horizon and almost-sure statements follow from the explicit proof, not from enumeration.

## Relationship to prior work

Li et al. (2021 preprint; AISTATS 2022) analyze same-sample stochastic extragradient on bilinear games and prove convergence estimates with averaging and restarting, including the interpolation regime. Their sampled-matrix formulation is close, but the inspected algorithm, principal theorems and appendix locations do not compare all fixed-marginal predictor/corrector couplings or optimize both the arithmetic and logarithmic norm rates. Gorbunov et al. (2021 preprint; AISTATS 2022) provide a unified same-sample/independent-sample theory and arbitrary sampling **within** same-sample SEG; the inspected relevant sections and appendix table of contents frame arbitrary sampling as sampling probabilities or minibatches, not a two-oracle coupling optimization. The 2026 Yoon–Loizou abstract compares same- and independent-sample variants under different convergence hypotheses; only its abstract was accessible in this review, so possible specialized overlap in its full text remains unresolved.

The proof uses elementary special algebra of two-dimensional rotations and the classical strong law, which are not claimed as new. The claimed contribution is the exact optimal-coupling classification and separation of two mathematically different long-run risk objectives under a fixed two-call, fixed-marginal constraint.

## Limitations

This is an exact minimal bilinear finite-sum benchmark, not a general guarantee for arbitrary stochastic variational inequalities, asymmetric step sizes, noncommuting sample matrices, or dependent draws across iterations. Almost-sure superiority does not imply smaller expected squared error, and vice versa. The result does not compare against deterministic full-gradient extragradient, other oracle budgets, adaptive couplings, or time-varying distributions. A targeted literature and mathematical-record search cannot establish publication priority; a separate independent review is not claimed. The cited 2026 preprint was accessible only at abstract level.

## References

1. C. J. Li, Y. Yu, N. Loizou, G. Gidel, Y. Ma, N. Le Roux, and M. I. Jordan, *On the Convergence of Stochastic Extragradient for Bilinear Games using Restarted Iteration Averaging*, arXiv:2107.00464, first posted June 30, 2021; AISTATS/PMLR 151 (2022). https://arxiv.org/abs/2107.00464 ; https://proceedings.mlr.press/v151/junchi-li22a/junchi-li22a.pdf
2. E. Gorbunov, H. Berard, G. Gidel, and N. Loizou, *Stochastic Extragradient: General Analysis and Improved Rates*, arXiv:2111.08611, first posted November 16, 2021; AISTATS/PMLR 151 (2022). https://arxiv.org/abs/2111.08611 ; https://proceedings.mlr.press/v151/gorbunov22b/gorbunov22b.pdf
3. T. Yoon and N. Loizou, *On Same-Sample and Independent-Sample Stochastic Extragradient for Monotone Variational Inequalities*, arXiv:2608.06182 (2026). Abstract-only comparison. https://arxiv.org/abs/2608.06182
