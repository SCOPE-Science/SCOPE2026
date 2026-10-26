# A quadratic discount window reverses singleton–doubleton covariance in Pitman–Yor partitions

## Finding

The two-parameter Ewens–Pitman sampling model exhibits a sharp, local dependence transition at its Dirichlet-process boundary. For a fixed strength \(\theta>1\), increasing the discount from zero through a window of order \(n^{-2}\) reverses the covariance between the number of species seen once and the number seen twice. With the notation below, if \(n^2\alpha_n\to c\in[0,\infty)\), then

\[
\lim_{n\to\infty}n^2\operatorname{Cov}(M_{1,n},M_{2,n})
=\theta^2(1-\theta)+\frac{\theta c}{2}.
\]

For every fixed \(\theta>1\), a unique zero \(\alpha_{*,n}(\theta)\) exists in a fixed neighborhood of zero for all sufficiently large \(n\), with

\[
n^2\alpha_{*,n}(\theta)\longrightarrow 2\theta(\theta-1).
\]

The covariance is strictly negative below this zero and strictly positive above it *within that neighborhood*. The result does not classify the entire interval of discounts and does not fix the eventual sign on a sequence for which the displayed limiting coefficient vanishes.

## Assumptions and scope

Fix \(\theta>0\). For every integer \(n\ge3\) and \(0\le\alpha<1\), construct an exchangeable random partition of the labels \(1,\ldots,n\) by the following predictive rule: after \(m\) arrivals in \(k\) blocks of sizes \(b_1,\ldots,b_k\), the next label joins block \(j\) with probability \((b_j-\alpha)/(m+\theta)\), and starts a new block with probability \((\theta+k\alpha)/(m+\theta)\). Define \(M_{r,n}\) as the number of final blocks containing exactly \(r\) labels, and set \((x)_0=1\), \((x)_k=\prod_{j=0}^{k-1}(x+j)\). The proof does not assume that \(\alpha\) remains fixed when \(n\) grows. All comparisons below are for the unconditioned partition law, not posterior prediction for unseen species.

## Proof

**Exact one- and two-block moments.** Exchangeability and the sampling consistency of the Chinese-restaurant law give the probabilities that a specified singleton block, a specified doubleton block, or specified disjoint singleton and doubleton blocks survive until time \(n\):

\[
\begin{aligned}
\Pr(\{1\}\text{ is a block})&=\frac{(\theta+\alpha)_{n-1}}{(\theta+1)_{n-1}},\\
\Pr(\{1,2\}\text{ is a block})&=\frac{(1-\alpha)(\theta+\alpha)_{n-2}}{(\theta+1)_{n-1}},\\
\Pr(\{1\},\{2,3\}\text{ both are blocks})&=\frac{(1-\alpha)(\theta+\alpha)(\theta+2\alpha)_{n-3}}{(\theta+1)_{n-1}}.
\end{aligned}
\]

For example, the last identity follows by first forming the singleton and the doubleton under the predictive rule and then requiring that every remaining arrival avoid both marked blocks; equivalently it is the two-marked-block specialization of the Ewens–Pitman sampling formula. Multiplying by \(n\), \(\binom n2\), and \(n\binom{n-1}2\) possible label choices, respectively, yields

\[
\begin{aligned}
\mu_1&:=\mathbb E M_{1,n}=\frac{n(\theta+\alpha)_{n-1}}{(\theta+1)_{n-1}},\\
\mu_2&:=\mathbb E M_{2,n}=\frac{\binom n2(1-\alpha)(\theta+\alpha)_{n-2}}{(\theta+1)_{n-1}},\\
\mu_{12}&:=\mathbb E(M_{1,n}M_{2,n})=\frac{n\binom{n-1}2(1-\alpha)(\theta+\alpha)(\theta+2\alpha)_{n-3}}{(\theta+1)_{n-1}}.
\end{aligned}
\]

Since \(\mu_1\mu_2>0\), the sign of the covariance is the sign of \(R_n-1\), where cancellation gives the exact rational product

\[
R_n(\alpha,\theta)=\frac{\mu_{12}}{\mu_1\mu_2}
=\frac{n-2}{n}\frac{(\theta+\alpha)(\theta+2\alpha)_{n-3}(\theta+1)_{n-1}}{(\theta+\alpha)_{n-1}(\theta+\alpha)_{n-2}}.
\]

At the Ewens boundary \(\alpha=0\), cancellation yields

\[
R_n(0,\theta)-1=\frac{2(1-\theta)}{n(n+\theta-3)}.
\]

**Uniform local derivative control.** Define \(g_n(\alpha)=\log R_n(\alpha,\theta)\). Directly differentiating the product gives

\[
g_n'(0)=\frac1\theta-\frac2{n+\theta-3}-\frac1{n+\theta-2}\longrightarrow\frac1\theta>0.
\]

Differentiating again, for \(0\le\alpha\le1/2\), gives

\[
\begin{aligned}
g_n''(\alpha)={}&-\frac1{(\theta+\alpha)^2}
-4\sum_{j=0}^{n-4}\frac1{(\theta+2\alpha+j)^2}\\
&+\sum_{j=0}^{n-2}\frac1{(\theta+\alpha+j)^2}
+\sum_{j=0}^{n-3}\frac1{(\theta+\alpha+j)^2}.
\end{aligned}
\]

Empty sums are interpreted as zero. Consequently \(|g_n''(\alpha)|\le C_\theta\), independently of \(n\) and \(\alpha\) in this interval, where

\[
C_\theta=\theta^{-2}+6\sum_{j=0}^{\infty}(\theta+j)^{-2}<\infty.
\]

Choose \(\delta=\min\{1/2,1/(4\theta C_\theta)\}>0\). For all sufficiently large \(n\), \(g_n'(0)\ge 3/(4\theta)\), so throughout \([0,\delta]\) one has \(g_n'(\alpha)\ge1/(2\theta)>0\). If \(\theta>1\), then \(g_n(0)<0\) for every \(n\ge3\), whereas \(g_n(\delta)>0\) for all sufficiently large \(n\), since \(g_n(0)\to0\). Strict increase therefore gives exactly one local root and its sign classification.

**Boundary scale.** At \(\alpha=0\), the exact boundary identity implies

\[
n^2g_n(0)\longrightarrow 2(1-\theta).
\]

If \(n^2\alpha_n\to c<\infty\), Taylor's theorem and the uniform \(g_n''\) bound yield

\[
n^2g_n(\alpha_n)=n^2g_n(0)+n^2\alpha_n g_n'(0)+O(n^2\alpha_n^2)
\longrightarrow 2(1-\theta)+\frac c\theta.
\]

The exact mean formulas show \(\mu_1\to\theta\) and \(\mu_2\to\theta/2\): compare the products at \(\alpha_n\) and zero logarithmically, bounding the product perturbations by \(O(\alpha_n\log n)=o(1)\), and use the elementary Ewens expressions. As \(g_n(\alpha_n)=O(n^{-2})\), we have \(n^2(R_n-1)-n^2g_n\to0\). Multiplying by \(\mu_1\mu_2\to\theta^2/2\) proves the covariance limit.

Finally, for \(\theta>1\), the unique root must tend to zero (since \(g_n'(\alpha)\ge1/(2\theta)\) and \(g_n(0)=O(n^{-2})\)), and the mean-value bound first shows \(\alpha_{*,n}=O(n^{-2})\). Substituting \(\alpha_n=\alpha_{*,n}\) into the same Taylor expansion gives \(n^2\alpha_{*,n}\to2\theta(\theta-1)\). This completes the proof.

## Verification

The accompanying `verification.py` uses only Python standard-library exact rational arithmetic. It independently propagates all Chinese-restaurant block-size states through eight arrivals over twelve rational parameter combinations per size, checks the three marked-block moments and the moment ratio, verifies the exact \(\alpha=0\) identity through \(n=200\), and tests finite near-boundary sign examples. Running `python verification.py` gave **2315 exact assertions passed**. These finite tests do not prove the unlimited-\(n\) statement; the uniform logarithmic derivative bounds above provide that proof.

## Relationship to prior work

Balocchi, Favaro, and Naulet give the Ewens–Pitman sampling formula and related species-prevalence calculations, including an exact distributional framework from which marked-block probabilities can be obtained. Franssen and van der Vaart analyze inference for the discount/type parameter and its asymptotics. Thus the sampling model, the exact law, and the ability to derive factorial moments are prior work. The claim here is only the *local, moving-discount covariance sign transition* at positive strength \(\theta>1\), its \(n^{-2}\) scale, and its limiting coefficient. A previous calculation for the special strength \(\theta=0\) gives a distinct sign transition near discount one and does not imply the present positive-strength transition near discount zero. Related random-partition and occupancy dependence results concern different probability laws or different statistics.

## Limitations

Historical priority is not definitive: a specialized prior treatment of joint frequency counts might contain an equivalent boundary calculation. The transition is microscopic in absolute covariance, which is \(O(n^{-2})\) in the stated window; the result is about sign and precise crossover, not a large finite-sample dependence. Local root uniqueness does not rule out additional roots at larger discounts. At the critical limit \(c=2\theta(\theta-1)\), a higher-order expansion is needed to decide eventual sign along a particular sequence. No independent mathematical audit has been performed, and the result does not concern posterior prediction or general Gibbs partitions.

## References

1. C. Balocchi, S. Favaro and Z. Naulet, *Bayesian Nonparametric Inference for “Species-sampling” Problems*, arXiv:2203.06076, first public version 2022-03-11. https://arxiv.org/abs/2203.06076
2. S. E. M. P. Franssen and A. W. van der Vaart, *Empirical and Full Bayes estimation of the type of a Pitman-Yor process*, arXiv:2208.14255, first public version 2022-08-30. https://arxiv.org/abs/2208.14255
