# Sharp high-signal budget split for variance-aware stochastic gradient descent

## Finding

A single pooled minibatch is strictly worse in expected squared error than any prescribed division of the same independent gradient samples into at least two successive, **reoptimized oracle steps** on an isotropic quadratic with Gaussian additive gradient noise. The comparison holds at every finite, nonzero initial error, with no change in sample count. More generally, the non-strict comparison holds for arbitrary zero-mean independent noise with finite positive second moment.

For two successive minibatches of sizes \(b_1,b_2\in\mathbb N\) in dimension \(d\ge1\), set \(t=b_1/b_2\). As the initial squared error tends to infinity with \(d,b_1,b_2\) fixed, the exact ratio of two-step to pooled mean-squared error is
\[
R_d(t)=(1+t)\mathbb E\!\left[\frac{Q_d}{Q_d+t}\right],\qquad Q_d=\frac{\chi_d^2}{d}.
\]
For each \(d\), this ratio is strictly below one for every \(t>0\), tends to one at both endpoints, and has exactly one minimizer \(t_d>0\). Its optimized minimum increases strictly with dimension. The sharp infimum across all positive integer batch splits and all dimensions is the one-dimensional value
\[
R_1(t_1)=0.6804153100377522917794\ldots,\qquad
 t_1=0.6048675421548876022483\ldots.
\]
Thus the greatest **high-signal** relative risk reduction from the two-block adaptation in this model is \(31.95846899622477\ldots\%\). It is a supremum approached by integer ratios approximating \(t_1\), not an asserted finite-signal global optimum. It concerns mean-squared error, not computational time or generalization.

## Assumptions and scope

Let \(d\ge1\), \(x_0\in\mathbb R^d\), and \(F(x)=\|x\|_2^2/2\). Every sampled gradient is \(g(x,\xi)=x+\xi\), with independent, identically distributed centered noise vectors \(\xi\) satisfying \(v=\mathbb E\|\xi\|_2^2\in(0,\infty)\). A block of \(b\ge1\) gradients is averaged and all blocks use disjoint independent noise. At the current point, put \(s=\|x\|_2^2\) and choose the population/variance-oracle step
\[
\alpha_b(s)=\frac{s}{s+v/b}=\frac{bs}{bs+v},\qquad
x^+=x-\alpha_b(s)(x+\bar\xi_b).
\]
At \(s=0\), set \(\alpha_b(0)=0\). This is the one-step conditional mean-square optimal scalar step along the stochastic gradient, and is the exact quadratic specialization of the gradient-moment rule of Köhne, Kreis, Schiela and Herzog. Its evaluation presumes unavailable population information in typical stochastic optimization. All claims about strictness and the high-signal spectral law additionally assume \(\xi\sim N(0,\sigma^2I_d)\) for \(\sigma^2>0\), whence \(v=d\sigma^2\).

## Proof

**One-step risk and composition.** Conditioned on \(x\), the independent block mean has zero mean and second moment \(v/b\). With \(s=\|x\|_2^2\),
\[
\mathbb E[\|x^+\|_2^2\mid x]=(1-\alpha)^2s+\alpha^2v/b.
\]
The strict quadratic minimum occurs at \(\alpha=bs/(bs+v)\) for \(s>0\), and the resulting conditional risk is
\[
f_b(s)=\frac{vs}{v+bs}.
\]
For all positive integers \(b,c\) and \(s\ge0\), direct substitution gives \(f_b(f_c(s))=f_{b+c}(s)\). Moreover \(f_b\) is increasing and strictly concave on \([0,\infty)\) because \(f_b''(s)=-2bv^2/(v+bs)^3<0\).

For an arbitrary prescribed partition \(B=b_1+\cdots+b_k\), write \(S_j=\|x_j\|_2^2\), \(\mu_j=\mathbb E S_j\). Conditional expectation and Jensen yield
\[
\mu_j=\mathbb E f_{b_j}(S_{j-1})\le f_{b_j}(\mu_{j-1})\le f_{b_1+\cdots+b_j}(S_0).
\]
In particular, \(\mathbb E S_k\le f_B(S_0)\), exactly the risk of one pooled batch with \(B\) samples. Under nondegenerate Gaussian noise and \(S_0>0\), \(S_1\) is nonconstant and Jensen is strict at the second step; strictness propagates to every later block because \(f_b\) is increasing. This does not claim ordering between two arbitrary multi-block partitions, nor does it include sample-processing costs.

For two blocks the strict gap is explicitly a Jensen dispersion term. With \(a=b_2/v\) and \(\mu=f_{b_1}(S_0)\),
\[
f_{b_1+b_2}(S_0)-\mathbb ES_2=
\frac{a}{(1+a\mu)^2}\,
\mathbb E\left[\frac{(S_1-\mu)^2}{1+aS_1}\right].
\]
This follows by subtracting the tangent of \(s/(1+as)\) at \(\mu\), and confirms exact equality conditions.

**High-signal limit.** For the isotropic Gaussian specialization and fixed \(d,b_1,b_2\), let \(\|x_0\|_2^2\to\infty\). The first optimal step approaches one, while \((1-\alpha_{b_1})x_0\to0\), so \(x_1\to-\bar\xi_{b_1}\) in mean square. Since \(f_{b_2}(s)\) is continuous, bounded by \(v/b_2\), and increasing, dominated convergence (or bounded convergence in probability) gives
\[
\lim\mathbb ES_2=\mathbb E f_{b_2}(\|\bar\xi_{b_1}\|_2^2).
\]
Now \(\|\bar\xi_{b_1}\|_2^2=(\sigma^2/b_1)\chi_d^2\), while pooled risk tends to \(v/(b_1+b_2)\). Their ratio reduces exactly to \(R_d(b_1/b_2)\) displayed above.

**Unique optimal split.** Let \(Q\) have the law \(Q_d\). Differentiation under the integral, justified by positive denominators and finite moments, yields
\[
R_d'(t)=\mathbb E\left[\frac{Q(Q-1)}{(Q+t)^2}\right].
\]
Define a probability law by reweighting the distribution of \(Q\) with \(w_t(q)=q/(q+t)^2\). Then \(R_d'(t)\) has the sign of \(m_d(t)-1\), where \(m_d(t)\) is the reweighted mean of \(Q\). If \(t_2>t_1>0\), the ratio
\[
\frac{w_{t_2}(q)}{w_{t_1}(q)}
=\left(\frac{q+t_1}{q+t_2}\right)^2
\]
is strictly increasing in \(q\), proving that \(m_d(t)\) increases strictly (by strict positive covariance of two increasing functions). The gamma law gives
\[
\lim_{t\downarrow0}m_d(t)=
\begin{cases}0,&d\le2,\\ (d-2)/d,&d>2,\end{cases}
\qquad \lim_{t\to\infty}m_d(t)=1+2/d.
\]
Thus the derivative changes from negative to positive exactly once. Also \(R_d(0+)=R_d(\infty)=1\), so the sole stationary point is its unique global minimum, strictly below one.

**Dimension ordering and sharp constant.** Since \(Q_d\) is the arithmetic mean of \(d\) independent squared standard normals, \(Q_{d+1}\) is smaller than \(Q_d\) in convex order: it is the arithmetic mean of all \(d+1\) leave-one-out means of size \(d\). As \(q/(q+t)\) is strictly concave, \(R_{d+1}(t)>R_d(t)\) at every finite \(t>0\). Taking their unique minimizers shows \(\min_tR_{d+1}(t)>\min_tR_d(t)\). Moreover the exact Jensen-gap identity
\[
1-R_d(t)=\frac{t}{1+t}\,
\mathbb E\left[\frac{(Q_d-1)^2}{Q_d+t}\right]
\le\frac{2}{d(1+t)}\le\frac2d
\]
shows that the best gain tends to zero as dimension grows.

In dimension one, direct Gaussian integration (or a Laplace transform) gives
\[
K(t)=\mathbb E\frac1{Z^2+t}
=\sqrt{\frac\pi{2t}}e^{t/2}\operatorname{erfc}\left(\sqrt{t/2}\right),
\qquad Z\sim N(0,1),
\]
so \(R_1(t)=(1+t)[1-tK(t)]\) and
\[
R_1'(t)=\frac{t+3-(t^2+4t+1)K(t)}2.
\]
By the already established uniqueness, this equation has exactly one positive root. The stated numerical values are computed from this explicit scalar equation. Positive rational numbers \(b_1/b_2\) are dense in \((0,\infty)\), establishing sharpness of the dimension-one infimum over positive integer splits.

## Verification

Run `python verify.py` with `mpmath` installed. The supplied verifier performs 704 deterministic checks: 616 exact rational compositions, high-precision gamma/erfc and derivative consistency, dimension-order and root checks, and independently integrated finite-signal two-stage inequalities. In particular, its scalar optimizing ratio and minimal risk agree to more than 40 decimal places with the reported values. These calculations are reproducibility checks; the infinite-dimensional parameter ranges and uniqueness claims are established by the proof above.

## Relationship to prior work

Köhne, Kreis, Schiela and Herzog derived the general moment/variance-based adaptive step (equation (3.2) in arXiv:2311.16956), rather than the present fixed-oracle-budget comparison. Gower and collaborators analyzed sampling-dependent step sizes and sample complexity for general SGD, with optimal minibatch sizes in a different, non-adaptive-stepsize setting. Lau, Liu and Kolar studied adaptive batch-size schemes for AdaGrad rather than an exact finite-budget mean-square comparison under this oracle rule. The new claim is the combination of strict fixed-budget risk dominance, the complete high-signal split optimization and its dimension-sharp constant; neither the oracle rule nor generic minibatching or Jensen's inequality is claimed as new.

## Limitations

The rule is an **idealized population moment oracle**: it uses quantities that are generally unknown during real stochastic optimization. It is not an assessment of the empirical gradient-moment estimators or safeguards from the motivating paper. The batch-risk dominance is distribution-free only for additive centered independent gradient noise with finite positive second moment; its strictness and chi-square law use isotropic Gaussian noise. The sharp \(31.958\ldots\%\) gain concerns a high-initial-signal limit, with two sequential blocks and the same number of individual gradients. It is not a universal bound at finite signal, for more than two blocks, or for other objectives. Communication, parallel execution, gradient-query latency, and hardware throughput are excluded. Related equivalent results could exist in unindexed literature.

## References

1. F. Köhne, L. Kreis, A. Schiela and R. Herzog, *Adaptive Step Sizes for Preconditioned Stochastic Gradient Descent* (initial public version 2023-11-28); revised as *Adaptive Step Sizes for Stochastic Gradient Descent in Hilbert Spaces*. arXiv:2311.16956, https://arxiv.org/abs/2311.16956 ; section 3, equation (3.2).
2. R. M. Gower, N. Loizou, X. Qian, A. Sailanbayev, E. Shulgin and P. Richtárik, *SGD: General Analysis and Improved Rates*, arXiv:1901.09401, https://arxiv.org/abs/1901.09401 ; section 4.
3. T. T.-K. Lau, H. Liu and M. Kolar, *AdAdaGrad: Adaptive Batch Size Schemes for Adaptive Gradient Methods*, arXiv:2402.11215, https://arxiv.org/abs/2402.11215 ; sections 3–4.
