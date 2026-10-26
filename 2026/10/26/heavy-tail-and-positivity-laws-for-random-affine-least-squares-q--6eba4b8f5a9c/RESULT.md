# Heavy-tail and positivity laws for random affine least-squares quadrature

## Finding

**Theorem (sharp finite-sample stability law).** Let \(M\geq2\) be an integer and let \(X_1,\ldots,X_M\) be independent uniform random variables on \([-1,1]\). For each realization with two distinct nodes, project sampled values in unweighted least squares onto the affine space \(V=\operatorname{span}\{1,x\}\), then integrate the fitted affine function against the uniform probability measure on \([-1,1]\). Denote the resulting quadrature weights by \(w_i\) and their absolute condition number by \(\kappa_M=\sum_{i=1}^{M}|w_i|\).

Write \(H_M=\{v\in\mathbb R^M:\sum_i v_i=0\}\), \(\mathbb S_M=\{v\in H_M:\|v\|_2=1\}\), and let \(d\sigma\) be the ordinary surface measure on this unit sphere (counting measure on its two points when \(M=2\)). Then, as \(u\to\infty\),

\[
\Pr(\kappa_M>u)\sim C_M u^{-(M-1)},\qquad
C_M=\frac{\sqrt M}{2^{M-1}M(M-1)}
\int_{\mathbb S_M}\Bigl(\sum_{i=1}^{M}|v_i|\Bigr)^{M-1}d\sigma(v)>0.
\]

Consequently, for every real \(p>0\),

\[
\mathbb E[\kappa_M^p]<\infty\quad\Longleftrightarrow\quad p<M-1.
\]

The first two sharp constants are \(C_2=1\) and

\[
C_3=\frac12+\frac{\pi}{3\sqrt3}=1.104599788078\ldots.
\]

The three-node rule also has the exact *positive-weight probability*

\[
\Pr(w_1>0,\ w_2>0,\ w_3>0)=\Pr(\kappa_3=1)
=\frac{14-\pi}{16}=0.678650459150\ldots.
\]

For independently corrupted sample values with additive, centered, equal-variance noise \(\varepsilon_i\) of variance \(0<\sigma^2<\infty\), independent of the nodes, the unconditional expected squared **noise contribution** to the quadrature value is infinite precisely when \(M=2\) or \(M=3\), and finite for every \(M\geq4\). The assertion concerns unmodified least-squares weights, without rejection, truncation, or conditioning on a well-conditioned design.

## Assumptions and scope

The sampling distribution and the integration probability measure are both \(\operatorname{Unif}[-1,1]\). The least-squares objective assigns identical unit weights to all sampled function values. Arithmetic is exact. The Gramian is nonsingular almost surely, since independent continuously distributed nodes coincide all together with probability zero. All equalities in the theorem concern the *intermediate* (unpruned) quadrature rule, including its random weights; they do not claim the same laws for pruned positive rules.

The error quantity used for the noise statement is \(\sum_i w_i\varepsilon_i\), not the total quadrature error for an arbitrary fixed nonsmooth integrand. For distinct nodes, \(\kappa_M\) is the exact operator norm of the quadrature map acting on arbitrary bounded sampled values with norm at most one. At coincident nodes, which have probability zero here, the norm must combine repeated evaluations.

## Proof

**1. Exact least-squares weights.** Put \(t=M^{-1}\sum_i X_i\), \(v_i=X_i-t\), and \(S=\sum_i v_i^2\). The affine design matrix has rows \((1,X_i)\); the target integral evaluates its basis as \((1,0)\). Inverting the two-by-two Gramian yields, on \(S>0\),

\[
w_i=\frac1M-\frac{t v_i}{S}.
\]

It follows directly that \(\sum_iw_i=1\), \(\sum_iw_iX_i=0\), and

\[
\sum_iw_i^2=\frac1M+\frac{t^2}{S}.
\]

**2. Exact radial asymptotic.** Regard the sample vector as \(X=t\mathbf1+r\omega\), where \(\omega\in\mathbb S_M\) and \(r=\sqrt{S}>0\). The Euclidean volume element is \(\sqrt M\,r^{M-2}\,dt\,dr\,d\sigma(\omega)\); the sample-cube probability density is \(2^{-M}\). Thus

\[
\kappa_M(t,r,\omega)=\sum_{i=1}^{M}
\left|\frac1M-\frac{t\omega_i}{r}\right|.
\]

In the probability integral for \(\kappa_M>u\), replace \(r\) by \(s/u\). For almost every fixed \((t,s,\omega)\) with \(t\in(-1,1)\), \(s>0\), the indicator converges to that of \(s<|t|\sum_i|\omega_i|\). The sample-cube restriction tends to no restriction at all for these interior \(t\). There is a uniform dominating region: by the triangle inequality, \(\kappa_M\leq1+|t|\sqrt M/r\), so for \(u\geq2\), the tail event forces \(s\leq2\sqrt M\). Dominated convergence therefore gives

\[
\begin{aligned}
\lim_{u\to\infty}u^{M-1}\Pr(\kappa_M>u)
&=\frac{\sqrt M}{2^M}\int_{-1}^{1}dt\int_{\mathbb S_M}d\sigma(\omega)
\int_0^{|t|\sum_i|\omega_i|}s^{M-2}\,ds\\
&=\frac{\sqrt M}{2^{M-1}M(M-1)}
\int_{\mathbb S_M}\Bigl(\sum_i|\omega_i|\Bigr)^{M-1}d\sigma(\omega).
\end{aligned}
\]

This constant is finite and strictly positive. The layer-cake identity for nonnegative random variables then proves \(\mathbb E[\kappa_M^p]<\infty\) exactly for \(p<M-1\); equality at the boundary gives logarithmic divergence.

**3. Explicit angular constants.** For \(M=2\), \(\mathbb S_2\) consists of \(\pm(1,-1)/\sqrt2\). The constant formula gives \(C_2=1\). For \(M=3\), write

\[
\omega_j=\sqrt{\frac23}\cos\left(\theta+\frac{2\pi(j-1)}3\right),
\qquad 0\leq\theta<2\pi.
\]

Because the three coordinates sum to zero, \(\sum_j|\omega_j|=2\max_j|\omega_j|\). The circle partitions into six congruent angular arcs; on each arc the maximum absolute coordinate equals \(\sqrt{2/3}\cos\varphi\) for \(-\pi/6\leq\varphi\leq\pi/6\). Hence

\[
\int_{\mathbb S_3}\Bigl(\sum_j|\omega_j|\Bigr)^2d\sigma
=16\int_{-\pi/6}^{\pi/6}\cos^2\varphi\,d\varphi
=\frac{8\pi}{3}+4\sqrt3.
\]

Multiplication by \(\sqrt3/24\) gives the stated \(C_3\).

**4. Three-node positivity.** Order the nodes as \(x<y<z\), an event with sorted joint density \(3!/2^3=3/4\) on \(-1<x<y<z<1\). The greatest-node weight is negative precisely when

\[
 x(x-z)+y(y-z)<0.
\]

This requires \(z>0\). If \(0<x<y<z\), the admissible \((x,y)\)-area for fixed \(z\) is \(z^2/2\). In the remaining possible region \(x<0<y<z\), substitute \(x=-zu\), \(y=zv\); the inequality becomes \(u(u+1)<v(1-v)\). Its area is \(z^2(\pi-2)/8\), since

\[
\int_0^1\frac{\sqrt{1+4v(1-v)}-1}{2}\,dv=\frac{\pi-2}{8}.
\]

Integration over \(0<z<1\) gives

\[
\Pr(w_{\mathrm{greatest}}<0)
=\frac34\int_0^1 z^2\left(\frac12+\frac{\pi-2}{8}\right)dz
=\frac{\pi+2}{32}.
\]

By sign symmetry the same probability holds for the smallest-node weight. These events are disjoint: the weights form an affine function of the node coordinate and sum to one, so both extremes cannot simultaneously have negative weight. The middle-node weight cannot be the sole negative weight. Accordingly the total nonpositive-weight probability is \((\pi+2)/16\), yielding the stated positivity probability. Equality of a weight to zero has probability zero.

**5. Noise-variance threshold.** Conditional on the nodes, independence and centering give

\[
\mathbb E_{\varepsilon}\left[\left(\sum_iw_i\varepsilon_i\right)^2\bigg|X\right]
=\sigma^2\left(\frac1M+\frac{t^2}{r^2}\right).
\]

The first term is always finite. The second has finite expectation for \(M\geq4\), because \(|t|\leq1\) and the singular radial integral near zero is bounded by a multiple of \(\int_0^1 r^{M-4}dr\). For \(M=2,3\), restrict \(t\) to \([1/4,1/2]\) and \(r\) to a small interval on which the entire centered sphere remains inside the sample cube. There \(t^2\geq1/16\), so the same radial integral diverges. This proves both directions without assumptions about higher noise moments.

## Verification

Run `python3 verification/verify_affine_ls.py` using Python's standard library. The standalone program checks 3,000 independently sampled weight identities and affine moment constraints, 350,000 Monte Carlo triplets against the exact positivity probability, a 7,200-angle calculation of the angular integral, direct finite-threshold radial integrals at three thresholds, and collision-scaling identities. The recorded execution passed all these checks. Finite Monte Carlo and angular quadrature are consistency checks, not substitutes for the integral identities or dominated-convergence argument above.

## Relationship to prior work

Bělík, Narayan, and Turnage (2026, arXiv:2609.09506v1) introduce a general randomized least-squares quadrature framework. Its Section 3.3 gives general Gramian-inverse weight formulas; Sections 2.4, 2.6, and 4.5 establish high-probability weight concentration, stability, and positivity for suitable sampling budgets and assumptions. The theorem here specializes the *unmodified* intermediate rule to uniform affine sampling and instead determines its exact fixed-sample heavy-tail exponent, explicit three-node tail constant, exact positivity probability, and a sharp unconditional noise-variance threshold. Those statements do not follow from the cited high-probability estimates without additional analysis.

Migliorati and Nobile (first circulated 2018, later published 2022) study stable high-order randomized cubature and positive weights at sufficiently large sample sizes. Cohen and Migliorati (2017) and Xu and Zhang (2024) analyze random least-squares approximation stability. Wilson (1970) treats discrete least squares and quadrature construction. These related frameworks do not by themselves establish the stated exact three-node constants. Some relevant historical full texts were not accessible for a definitive priority comparison; mathematical priority therefore remains subject to further independent literature assessment.

## Limitations

The theorem does not classify higher-degree polynomial spaces, nonlinear function classes, importance sampling, positive pruning, ridge-regularized least squares, rejection of ill-conditioned designs, or floating-point implementations. The heavy tail concerns an *unconditional*, unmodified fixed-sample rule. High-probability stability statements for a sufficiently large sample budget are entirely compatible with its finite-sample heavy tail. The exact probability and explicit \(C_3\) concern three independent continuous uniform nodes only. The singular noise risk concerns independent centered additive errors of common positive finite variance.

## References

1. F. Bělík, A. Narayan, J. Turnage, *Constructive Tchakaloff results and well-conditioned quadrature through randomized least squares*, arXiv:2609.09506v1, first posted 2026-09-08. https://arxiv.org/html/2609.09506v1
2. G. Migliorati, F. Nobile, *Stable high-order randomized cubature formulae in arbitrary dimension*, arXiv:1812.07761, first posted 2018-12-19; Journal of Approximation Theory 275 (2022), 105706. https://arxiv.org/abs/1812.07761
3. A. Cohen, G. Migliorati, *Optimal weighted least-squares methods*, SMAI Journal of Computational Mathematics 3 (2017), 181–203; arXiv:1608.00512. https://arxiv.org/abs/1608.00512
4. Z. Xu, X. Zhang, *Stability of Least Square Approximation under Random Sampling*, arXiv:2407.10221, first posted 2024-07-14. https://arxiv.org/abs/2407.10221
5. M. W. Wilson, *Discrete Least Squares and Quadrature Formulas*, Mathematics of Computation 24 (1970), 271–282. https://doi.org/10.1090/S0025-5718-1970-0275677-3
