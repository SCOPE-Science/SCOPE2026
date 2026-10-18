# Uniform late-arrival influence on root protection in weighted recursive trees

## Finding

For every integer \(N\ge2\) and real parameter \(\theta>0\), consider a weighted recursive tree on vertices \(0,1,\ldots,N\), rooted at vertex 0. The root has attachment weight \(\theta\); every existing nonroot vertex has weight 1. Vertex 1 necessarily attaches to the root. For each \(2\le i\le N\), let \(B_i\) indicate attachment directly to the root. The root outdegree is \(K_N=1+\sum_{i=2}^N B_i\). Let \(H_N=1\) precisely when every root child has at least one child of its own, and otherwise \(H_N=0\); this is root protection.

**Strict finite influence.** For all \(N\ge2\), \(\theta>0\) and \(2\le i\le N\),
\[\operatorname{Cov}(B_i,H_N)<0.\]
Put \(p_i=\theta/(\theta+i-1)\) and \(\lambda_m(\theta)=\Pr(H_m=1)\), with \(\lambda_1=0\). Define
\[\Delta_{N,i}=\Pr(H_N=1\mid B_i=0)-\Pr(H_N=1\mid B_i=1).\]
The following explicit two-sided bounds hold:
\[
\frac{\theta+i-1}{\theta+N-1}\lambda_{N-1}(\theta)
\ \le\ \Delta_{N,i}\ \le\
\frac{\theta+i-1}{\theta+N-1}\lambda_{N-1}(\theta)
+\frac{\theta(\theta+i-1)}{(\theta+N-1)(\theta+i-2)}.
\]
Furthermore \(\operatorname{Cov}(B_i,H_N)=-p_i(1-p_i)\Delta_{N,i}\). Even when the displayed lower bound vanishes at \(N=2\), strict negativity holds.

**Asymptotically equal negative shares.** Fix \(\theta>0\). For every fixed \(\varepsilon\in(0,1)\),
\[
\sup_{\varepsilon N\le i\le N}
\left|N\operatorname{Cov}(B_i,H_N)+\theta e^{-\theta}\right|\to0
\qquad(N\to\infty).
\]
Consequently,
\[\boxed{\operatorname{Cov}(K_N,H_N)\longrightarrow-\theta e^{-\theta}.}\]
For the ordinary uniform recursive tree, take \(\theta=1\); its limit is \(-e^{-1}\). The local statement is stronger than this aggregate covariance limit.

## Assumptions and scope

All vertices and arrival indices are labeled, and the tree is rooted. The first nonroot vertex is a compulsory child of the root. The model has exactly one new vertex per step, with nonroot attachment weights identically one and root weight \(\theta\). The claims hold for all finite \(N\ge2\), all \(\theta>0\), and every \(i\) in the stated interval. The asymptotic statements hold with fixed \(\theta\); the uniformity is only over arrival indices bounded below by a fixed positive fraction of \(N\). No statement uniform as \(\theta\) varies with \(N\) is asserted.

## Proof

**1. Partition representation and independent switches.** Erase the root. Its child subtrees form a partition of the \(N\) nonroot vertices. This partition is the Chinese restaurant/Ewens partition with concentration \(\theta\): for \(i\ge2\), independently choose \(B_i\sim\operatorname{Bernoulli}(p_i)\), and if \(B_i=0\), choose an earlier parent uniformly among vertices \(1,\ldots,i-1\), independently of these switches. For \(B_i=1\), the parent is the root. Thus \(H_N=1\) if and only if no partition block is a singleton. Each singleton corresponds to a leaf child of the root.

**2. An edge-cut influence identity.** Fix the switches other than \(B_i\), and all potential earlier-parent choices. In the configuration with \(B_i=1\), call the component containing \(i\) component \(A\), and call the component containing its potential parent \(U_i\) component \(C\). With \(B_i=0\), the edge \(iU_i\) merges \(A\) and \(C\), which are distinct in the cut configuration. Merging blocks can eliminate singleton blocks but cannot create them. Therefore the protection indicator in the merged configuration is at least that in the cut configuration. The inequality is strict with positive probability: set every other switch to zero, let every other arrival after the first select parent vertex 1, and let \(U_i=1\). The cut configuration has singleton block \(\{i\}\), while the merged configuration has one block of size \(N\). Every prescribed finite choice has positive probability. Hence \(\Delta_{N,i}>0\), and independence of \(B_i\) from the potential parents proves \(\operatorname{Cov}(B_i,H_N)=-p_i(1-p_i)\Delta_{N,i}<0\).

**3. Quantitative influence bounds.** Under an Ewens partition of \(N\) labels, a given label is a singleton with probability \(\theta/(\theta+N-1)\). Conditional on that event, the remaining \(N-1\) labels form an Ewens partition of the same parameter. Moreover, a singleton at label \(i\) necessarily has \(B_i=1\). Since \(\Pr(B_i=1)=p_i\), the probability, conditional on the forced cut \(B_i=1\), that \(A=\{i\}\) and all other components have size at least two is exactly
\[L_{N,i}=\frac{\theta+i-1}{\theta+N-1}\lambda_{N-1}(\theta).\]
This event forces protection after merging but not before, so \(\Delta_{N,i}\ge L_{N,i}\).

Every additional configuration contributing to \(\Delta_{N,i}\) must have the component \(C\) containing \(U_i\) singleton. For any label \(j<i\), conditioning it to be singleton removes it and leaves an Ewens partition on \(N-1\) labels; the indicator for the original arrival \(i\) to start a block then has probability \(\theta/(\theta+i-2)\). Consequently,
\[\Pr(C\text{ singleton}\mid B_i=1)
=\frac{\theta}{\theta+N-1}\frac{\theta+i-1}{\theta+i-2}.\]
This bounds the additional probability and gives the upper bound. It is a bound, not an asserted equality for the residual contribution.

**4. Asymptotics.** Write \(\lambda_m(\theta)=\Pr_\theta(Z_m=0)\), where \(Z_m\) is the number of singleton blocks in an Ewens partition of \(m\). For every fixed positive integer \(r\),
\[\mathbb E_\theta[(Z_m)_r]=m^{\underline r}\theta^r\frac{(\theta)_{m-r}}{(\theta)_m}\longrightarrow\theta^r.\]
Here \((z)_k=z(z+1)\cdots(z+k-1)\) denotes rising factorial, whereas \(m^{\underline r}\) is falling factorial. Bonferroni bounds applied to these factorial moments prove \(\lambda_m(\theta)\to e^{-\theta}\). Substituting the finite influence bounds gives, uniformly for \(\varepsilon N\le i\le N\),
\[\operatorname{Cov}(B_i,H_N)
=-\frac{\theta(i-1)}{(\theta+i-1)(\theta+N-1)}\lambda_{N-1}(\theta)+O_{\theta,\varepsilon}(N^{-2})
=-\frac{\theta e^{-\theta}}{N}+o_{\theta,\varepsilon}(N^{-1}).\]
For the sum over **all** arrivals, the absolute aggregate error is bounded by
\[\frac{\theta^2}{\theta+N-1}\sum_{i=2}^N\frac{i-1}{(\theta+i-1)(\theta+i-2)}=O_\theta\!\left(\frac{\log N}{N}\right).\]
The main sum equals
\[-\frac{\theta\lambda_{N-1}(\theta)}{\theta+N-1}\sum_{i=2}^N\frac{i-1}{\theta+i-1}\longrightarrow-\theta e^{-\theta},\]
because the final sum is \(N+O_\theta(\log N)\). Since \(K_N=1+\sum_{i=2}^N B_i\), covariance additivity completes the proof.

## Verification

The accompanying self-contained Python checker, `verify.py`, enumerates every potential-parent tree on \(N+1\) vertices for \(2\le N\le8\), under three exact rational root weights \(\theta\in\{1/2,1,2\}\). It evaluates the weighted joint event probabilities, their covariances, the Ewens derangement probability computed independently by associated Stirling-number recurrence, and both sides of the finite influence bounds. It reports 210 exact-rational assertions passing. These finite computations corroborate, but do not replace, the preceding universal proof.

## Relationship to prior work

The classical Ewens sampling formula and its derangement probability are established; in particular, da Silva, Jamshidpey and Tavaré (2020), equations (5), (9), and (10), give the derangement probability and the cycle-count distribution and mean. The present claim **does not** claim these formulas, the ordinary Chinese restaurant representation, or the protected-node definition as new. The distinct assertion is the strict negative effect of **each individual arrival choice** on root protection, its explicit finite influence bounds, and the uniform bulk equal-share asymptotic, which do not follow merely by quoting the aggregate cycle-count marginal. Relevant protected-node profile results of Toofanpour, Javanian and Imany-Nabiyyi (2022) concern level-profile moments and limiting fluctuations rather than the labeled-arrival local influence. Its complete article text was not available for exhaustive comparison; this is an originality limitation.

## Limitations

The late-arrival asymptotic is not uniform for arrival indices \(i=o(N)\), and no uniform-in-\(\theta\) asymptotic is claimed. The general finite bound on \(\Delta_{N,i}\) is not an equality. The aggregate mixed moment can also be calculated indirectly from earlier Ewens derangement enumerations; the locally indexed influence classification, rather than that known enumerative input, is the intended contribution. Historical priority requires independent examination of any earlier work specifically treating root-protection dependence on individual recursive-tree attachments.

## References

1. P. H. da Silva, A. Jamshidpey, S. Tavaré, *Random derangements and the Ewens Sampling Formula*, arXiv:2006.04840v1 (first public version 2020-06-08), https://arxiv.org/abs/2006.04840.
2. J. Toofanpour, M. Javanian, R. Imany-Nabiyyi, *Normal Limit Law for Protected Node Profile of Random Recursive Trees*, *Theory of Probability & Its Applications* 67 (2022), 452–464, https://doi.org/10.1137/S0040585X97T991040.
