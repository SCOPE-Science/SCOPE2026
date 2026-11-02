# Sharp randomized-to-deterministic ordering transition for two-component quadratic reshuffling

## Finding

For the two scalar component losses \(f_1(x)=ax^2/2+\delta x\) and \(f_2(x)=bx^2/2-\delta x\), suppose \(a,b>0\), \(\delta\ne0\), and use the exact component-gradient step \(0<h<1/\max\{a,b\}\). In each independent two-update epoch, apply component \(1\) then \(2\) with probability \(p\in[0,1]\), or component \(2\) then \(1\) otherwise. The average objective has the unique minimizer \(x_*=0\). Denote \(t=(1-ha)(1-hb)\in(0,1)\).

The resulting epoch-boundary chain has a unique stationary law. Its stationary mean-squared distance to \(x_*\) is
\[
\mathcal E(p)=\frac{h^4\delta^2((a+b)p-a)^2}{(1-t)^2}+\frac{h^4\delta^2(a+b)^2p(1-p)}{1-t^2}.
\]
The unique global optimum over all independent, identically distributed per-epoch order probabilities is
\[
p_{\rm opt}=\operatorname{clip}_{[0,1]}\!\left(\frac{a}{a+b}+\frac{(a-b)(1-t)}{4t(a+b)}\right).
\]
If \(a\ne b\), set \(\tau=|a-b|/(\max\{a,b\}+3\min\{a,b\})\). Exactly when \(t>\tau\), the optimal per-epoch policy randomizes both orders with strictly positive probabilities. For \(t\le\tau\), the optimal policy is deterministic: \(p_{\rm opt}=1\) for \(a>b\), and \(p_{\rm opt}=0\) for \(b>a\). There is one crossover step size
\[
h_c=\frac{a+b-\sqrt{(a-b)^2+4ab\tau}}{2ab},
\]
so that nondegenerate randomization is optimal for \(0<h<h_c\) and deterministic ordering for \(h_c\le h<1/\max\{a,b\}\). When \(a=b\), the unique optimum is \(p_{\rm opt}=1/2\) throughout the specified step interval.

For fixed unequal curvatures, ordinary uniform reshuffling \(p=1/2\) has
\[
\mathcal E(1/2)=\frac{\delta^2(a-b)^2}{4(a+b)^2}h^2+O(h^3),
\]
whereas optimal biased reshuffling has
\[
\mathcal E(p_{\rm opt})=\frac{\delta^2ab}{2(a+b)}h^3+O(h^4).
\]
Their risk ratio therefore diverges as \(h\downarrow0\):
\[
\frac{\mathcal E(1/2)}{\mathcal E(p_{\rm opt})}
\sim\frac{(a-b)^2}{2ab(a+b)}\frac1h.
\]
The prefix-gradient-discrepancy squared for either ordering is identical in this two-component model: at the only nontrivial prefix, the two possible gradient deviations are negatives of one another. Thus this specific order-insensitive discrepancy cannot distinguish the stationary-risk-optimal sampling probabilities.

## Assumptions and scope

The component gradient is computed at the latest within-epoch iterate, not at the epoch start. Each epoch contains both component updates exactly once; the order choices are independent across epochs with the same probability \(p\). The step \(h\) is fixed and positive, and \(0<h<1/\max\{a,b\}\) ensures both individual linear factors are positive. The error is measured only at epoch boundaries by limiting mean squared distance to \(x_*\). All arithmetic is exact. No distributional assumption is placed on the deterministic initial iterate.

Here \(\operatorname{clip}_{[0,1]}(z)=\min\{1,\max\{0,z\}\}\). The stationary distribution exists even when the optimal probability is an endpoint, in which case the chain is deterministic and its invariant law is a Dirac mass.

## Proof

**Epoch map.** Let \(T_1(x)=(1-ha)x-h\delta\) and \(T_2(x)=(1-hb)x+h\delta\). Direct composition gives
\[
T_2(T_1(x))=tx+h^2b\delta,\qquad
T_1(T_2(x))=tx-h^2a\delta.
\]
Consequently the epoch-end iterate obeys \(X_{k+1}=tX_k+h^2\delta U_{k+1}\), where the \(U_k\) are independent, taking value \(b\) with probability \(p\) and value \(-a\) with probability \(1-p\). Because \(0<t<1\) and \(U\) is bounded, the absolutely convergent random series \(h^2\delta\sum_{j=0}^{\infty}t^jU_{-j}\) gives the unique invariant law. Two chains sharing the same order sequence contract by the factor \(t^k\), proving convergence from any deterministic initial point in distribution and in mean square.

**Moments and optimal probability.** Exactly \(\mathbb E U=(a+b)p-a\) and \(\operatorname{Var}U=(a+b)^2p(1-p)\). Summing the stationary series gives
\[
\mathbb EX=\frac{h^2\delta((a+b)p-a)}{1-t},\qquad
\operatorname{Var}X=\frac{h^4\delta^2(a+b)^2p(1-p)}{1-t^2}.
\]
Adding the squared mean yields \(\mathcal E(p)\). Its strictly positive second derivative is
\[
\mathcal E''(p)=\frac{4h^4\delta^2t(a+b)^2}{(1-t)^2(1+t)}>0.
\]
The unique unconstrained minimizer obtained by differentiation is \(a/(a+b)+(a-b)(1-t)/(4t(a+b))\). Projecting this value onto \([0,1]\) gives the constrained optimizer.

**Sharp phase boundary.** When \(a>b\), the unconstrained optimizer is greater than \(a/(a+b)\), so it can meet only the upper endpoint. The equality \(p_{\rm free}=1\) is equivalent to \(t=(a-b)/(a+3b)\). When \(b>a\), symmetry exchanges the two order labels and the corresponding lower-endpoint condition is \(t=(b-a)/(b+3a)\). Thus in both cases the sharp criterion is \(t=\tau\). On the step interval, \(t(h)=(1-ha)(1-hb)\) decreases strictly from \(1\) to \(0\), since its derivative is \(-(a+b)+2abh<0\). Solving \(t(h)=\tau\) for the smaller positive quadratic root yields the displayed \(h_c\). For equal curvatures differentiation gives the permanent optimum \(p=1/2\).

**Small-step separation.** The expansions \(t=1-(a+b)h+abh^2\) and \(1-t^2=2(a+b)h+O(h^2)\) imply the displayed leading order for uniform \(p=1/2\). At the interior optimizer, \(p_{\rm opt}=a/(a+b)+O(h)\); its mean is \(O(h^2)\), so its squared mean is \(O(h^4)\), while its leading variance is \(h^3\delta^2ab/[2(a+b)]\). Since \(a\ne b\), the ratio has the stated divergent asymptotic. The order-discrepancy assertion follows because, at any iterate \(x\), the two gradients differ from their mean by \(\pm(\nabla f_1(x)-\nabla f_2(x))/2\), whose squares coincide.

**Exact example.** At \(a=3\), \(b=1\), \(h=1/4\), \(\delta=1\), one has \(t=3/16<\tau=1/3\). The unique optimal choice is \(p=1\), with \(\mathcal E(1)=1/169\), compared with \(\mathcal E(1/2)=71/3211\). The unique crossover is \(h_c=(2-\sqrt2)/3\).

## Verification

The independent symbolic/exact-rational checks are provided in `verify.py` and can be run with `python verify.py` after installing the declared dependency from `requirements.txt`. The checker reconstructs the exact first and second stationary moments, proves the derivative and endpoint identities symbolically, checks both leading small-step constants, verifies the rational example and exhaustively enumerates all \(2^k\) order histories for each \(1\le k\le9\) in six independent rational parameter sets, comparing their exact finite-time first two moments against the derived recurrence. The checker is a corroboration, not a replacement for the all-parameter analytic proof above.

## Relationship to prior work

Rajput, Lee and Papailiopoulos examine whether random permutations are optimal and establish function-dependent gaps and useful nonrandom orders. Their results motivate the importance of order but do not provide this exact stationary risk minimizer over iid biased two-permutation laws or its curvature-dependent transition. Mohtashami, Stich and Jaggi develop gradient-prefix discrepancy and sequence-sensitive convergence bounds; in this two-sample model the squared prefix discrepancy is identical for the two orderings despite the strict stationary risk preference. Domingo-Enrich analyzes the noise spectrum of reshuffling via a common-Hessian linearized model and uniform random permutations. Its common-Hessian approximation does not give the exact unequal-curvature epoch map used here, and its uniform law does not optimize the permutation probability.

This finding uses classical random affine recursions and elementary quadratic minimization; neither technique is presented as new in isolation. No claim of precedence over every specialized treatment of nonuniform permutation sampling is made.

## Limitations

The classification is for a scalar two-component strongly convex quadratic family, independent identically distributed order choices across epochs, fixed positive step below the reciprocal maximum curvature, and epoch-end stationary mean squared error. It does not compare arbitrary deterministic time-varying schedules such as alternating order, adaptive sampling, stepsize tuning, other error metrics, a larger dataset or multidimensional problems. The optimal sampling probability depends on knowing \(a\), \(b\) and \(h\). Computational checks are finite and do not constitute a general proof of the formulas; the algebraic proof above establishes the general statements. Specialized literature may affect publication priority. Independent external validation has not been conducted.

## References

- Rajput, S., Lee, K., and Papailiopoulos, D., *Permutation-Based SGD: Is Random Optimal?*, arXiv:2102.09718, first public February 19, 2021. https://arxiv.org/abs/2102.09718
- Mohtashami, A., Stich, S., and Jaggi, M., *Characterizing & Finding Good Data Orderings for Fast Convergence of Sequential Gradient Methods*, arXiv:2202.01838, first public February 3, 2022. https://arxiv.org/abs/2202.01838
- Domingo-Enrich, C., *Computing the Variance of Shuffling Stochastic Gradient Algorithms via Power Spectral Density Analysis*, arXiv:2206.00632, first public June 1, 2022. https://arxiv.org/abs/2206.00632
