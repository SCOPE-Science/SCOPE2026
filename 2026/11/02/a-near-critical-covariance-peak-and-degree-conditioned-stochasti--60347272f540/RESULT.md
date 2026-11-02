# A near-critical covariance peak and degree-conditioned stochastic order for percolated recursive trees

## Finding

Let \(T_n\) be the uniform random recursive tree on labels \(1,\ldots,n\), with root \(1\): independently, each vertex \(j\ge2\) chooses a parent uniformly from \(\{1,\ldots,j-1\}\). Independently retain each tree edge with probability \(p\). Write \(D_n\) for the root's number of children **before** deletion, and \(C_n(p)\) for the size of the retained connected component containing the root. All statements below are for integers \(n\ge3\).

**Theorem (one joint dependence law).** For every \(p\in[0,1]\), the full vector of indicators that vertices remain connected to the root is stochastically nondecreasing, in coordinatewise order, as the conditioning value \(D_n=d\) increases through \(d=1,\ldots,n-1\). For \(0<p<1\), this comparison strictly increases \(\Pr(C_n(p)\ge2\mid D_n=d)\) at each adjacent \(d\).

Define
\[
M_n(a)=\prod_{t=1}^{n-1}\left(1+\frac{a}{t}\right),\qquad
A_n(p)=\frac1n+(1-p)\sum_{t=1}^{n-1}\frac{1}{(t+1)(t+p)}.
\]
Then the exact finite covariance is
\[
\boxed{\operatorname{Cov}(D_n,C_n(p))=M_n(p)A_n(p)-1.}
\]
It is strictly positive for \(0<p<1\), and equals zero at both endpoints. Its **maximum over retention probabilities** has the sharp limit
\[
\boxed{
\max_{0\le p\le1}\operatorname{Cov}(D_n,C_n(p))
\sim \frac{\zeta(2)-1}{e}\,\frac{n}{\log n}.
}
\]
For **every** sequence of maximizing probabilities \(p_n\),
\[
\boxed{(1-p_n)\log n\longrightarrow1.}
\]
More generally, for each fixed \(\lambda\ge0\), at \(p=1-\lambda/\log n\) whenever this belongs to \([0,1]\),
\[
\frac{\log n}{n}\operatorname{Cov}(D_n,C_n(p))
\longrightarrow (\zeta(2)-1)\lambda e^{-\lambda}.
\]
Finally, for each fixed \(0<p<1\), despite the strict conditional stochastic ordering, \(\operatorname{Corr}(D_n,C_n(p))\) tends to zero at rate \((\log n)^{-1/2}\), with the explicit positive constant given in the proof.

This is a statement about the original root degree and its *percolated* component. Replacing \(D_n\) by the root degree after deletion changes the object.

## Assumptions and scope

For \(j=2,\ldots,n\), let \(P_j\) be independent and uniform on \(\{1,\ldots,j-1\}\), and let \(B_j\) be independent Bernoulli variables of parameter \(p\), independent of every parent. Define \(X_1=1\) and \(X_j=B_jX_{P_j}\). Then \(C_j=\sum_{i=1}^j X_i\) is the root-component size after the first \(j\) vertices and \(D_n=\sum_{j=2}^n\mathbf1_{\{P_j=1\}}\). Boundary cases \(p=0\) and \(p=1\) are included; the strict assertions require \(0<p<1\). The optimization allows \(p\) to depend on \(n\); fixed-\(p\) asymptotics are stated separately.

For random binary vectors, stochastic increase in *coordinatewise order* means the existence of a coupling in which every coordinate of the lower-degree vector is no larger than its counterpart at the higher degree. In particular, every coordinatewise increasing observable has nondecreasing conditional expectation.

## Proof

**1. Conditional inclusion coupling.** For \(j\ge3\), write \(I_j=\mathbf1_{\{P_j=1\}}\) and introduce an independent \(U_j\), uniform on \(\{2,\ldots,j-1\}\). Then \(I_j\) is Bernoulli with parameter \(1/(j-1)\), and the parent can be represented by \(P_j=1\) when \(I_j=1\), and \(P_j=U_j\) otherwise. Also \(I_2=1\) deterministically. Conditional on \(D_n=d\), the selected subset \(\{j\in\{3,\ldots,n\}:I_j=1\}\) has size \(d-1\) and probability proportional to \(\prod_{j:I_j=1}(j-2)^{-1}\).

Here is a self-contained inclusion-coupling lemma. For any positive weights \(w_1,\ldots,w_m\), let \(\nu_k\) be the probability law on \(k\)-subsets giving each subset weight proportional to the product of its weights. There exists a coupling \(S_k\subseteq S_{k+1}\) with marginals \(\nu_k,\nu_{k+1}\). Induct on \(m\). If \(e_k\) is the \(k\)-th elementary symmetric polynomial in the first \(m-1\) weights, the chance the last item occurs at level \(k\) is \(\alpha_k=w_me_{k-1}/(e_k+w_me_{k-1})\). Log-concavity \(e_k^2\ge e_{k-1}e_{k+1}\), following for example from the real-rooted polynomial \(\prod_{i<m}(1+w_i z)\), implies \(\alpha_k\le\alpha_{k+1}\). Couple the two last-item indicators monotonically. If both are absent, couple residual sets of sizes \(k\) and \(k+1\) inductively; if both are present, couple sizes \(k-1\) and \(k\); and if only the larger set includes the last item, use identical residual \(k\)-subsets. The boundary levels are immediate. This proves the lemma without assuming equal weights.

Apply the lemma with \(w_j=(j-2)^{-1}\), and keep the same variables \(U_j,B_j\) under both degree conditionings. If any parent choice is changed from \(U_j\ge2\) to root \(1\), the recursion \(X_j=B_jX_{P_j}\) shows inductively that no root-connectivity indicator can decrease. Therefore the entire connectivity vector admits the asserted monotone coupling. At adjacent values of \(d\), at least one \(j\ge3\) is changed to a root child. With positive probability the edge at one such \(j\) is retained and all other edges are deleted. On that event \(C_n\) is larger in the upper configuration, proving strict increase of the upper tail at \(2\) when \(0<p<1\).

**2. Exact covariance.** Conditional on the past, the new vertex is root-connected with probability \(pC_{j-1}/(j-1)\). Thus
\[
\mathbb E[C_j\mid C_{j-1}]=\left(1+\frac p{j-1}\right)C_{j-1},
\quad \mathbb E[C_n]=M_n(p),
\quad \mathbb E[C_n\mid\mathcal F_j]=\frac{M_n(p)}{M_j(p)}C_j.
\]
Since \(I_j\) is independent of the past, \(\mathbb E[I_jX_j]=p/(j-1)\), whereas \(\mathbb E[X_j]=pM_{j-1}(p)/(j-1)\). Consequently, for every \(2\le j\le n\),
\[
\operatorname{Cov}(I_j,C_n)=
\frac{pM_n(p)}{(j-1)M_j(p)}
\left(1-\frac{M_{j-1}(p)}{j-1}\right).
\]
The term for \(j=2\) vanishes; all other terms are strictly positive for \(0<p<1\), because \(M_{j-1}(p)<M_{j-1}(1)=j-1\). For \(t=j-1\), the term divided by \(M_n(p)\) equals
\[
\frac1{M_t(p)}-\frac1{M_{t+1}(p)}
-\frac{p}{t(t+p)}.
\]
Summing telescopes and yields
\[
\operatorname{Cov}(D_n,C_n(p))=
M_n(p)\left(1-\sum_{t=1}^{n-1}\frac{p}{t(t+p)}\right)-1.
\]
The elementary identity
\[
\frac{1}{t(t+1)}-\frac{p}{t(t+p)}
=\frac{1-p}{(t+1)(t+p)}
\]
and \(\sum_{t=1}^{n-1}1/[t(t+1)]=1-1/n\) give the stated \(A_n(p)\) formula. This proof simultaneously establishes all finite boundaries and the local covariance contributions.

**3. Sharp near-critical optimization.** Set \(L=\log n\), \(\delta=1-p\), and \(T_n(p)=\sum_{t=1}^{n-1}[(t+1)(t+p)]^{-1}\). Then
\[
\frac{M_n(p)}n=
\prod_{t=1}^{n-1}\left(1-\frac{\delta}{t+1}\right),
\qquad A_n(p)=n^{-1}+\delta T_n(p).
\]
For \(\delta=\lambda/L\) with fixed \(\lambda\ge0\), the logarithm of the product is \(-\delta(H_n-1)+O(\delta^2)\), hence tends to \(-\lambda\). Also, by dominated convergence,
\[
T_n(p)\longrightarrow\sum_{t=1}^{\infty}\frac{1}{(t+1)^2}
=\zeta(2)-1.
\]
It follows that \((L/n)\operatorname{Cov}(D_n,C_n(p))\to(\zeta(2)-1)\lambda e^{-\lambda}\).

To show this identifies *global* maximizers, note that for all \(0\le p\le1\),
\[
\frac{M_n(p)}n\le\exp[-\delta(H_n-1)],
\quad 0\le T_n(p)\le1,
\quad 0\le\frac{L}{n}\operatorname{Cov}(D_n,C_n(p))
\le e^{-\delta(H_n-1)}(L/n+L\delta).
\]
At \(\lambda=1\) the normalized covariance has a positive limiting value, while the upper bound tends to zero along every sequence with \(L\delta\to0\) or \(L\delta\to\infty\). Hence any maximizing sequence has \(L\delta\) bounded away from zero and infinity. Every subsequential limit must maximize \((\zeta(2)-1)\lambda e^{-\lambda}\), whose unique maximizer on \([0,\infty)\) is \(\lambda=1\). This proves both the sharp maximum and the localization of all maximizing probabilities. No assertion of uniqueness at any specific finite \(n\) is needed.

**4. Fixed-retention decorrelation.** The root-degree variance is \(H_{n-1}-H_{n-1}^{(2)}\). For the rising factorial \(s^{\overline r}=s(s+1)\cdots(s+r-1)\), the one-step transition gives
\[
\mathbb E[C_j^{\overline r}\mid C_{j-1}=s]
=\left(1+\frac{rp}{j-1}\right)s^{\overline r}.
\]
Thus \(\mathbb E[C_n^{\overline r}]=r!M_n(rp)\), and in particular
\[
\operatorname{Var}(C_n(p))=2M_n(2p)-M_n(p)-M_n(p)^2.
\]
For fixed \(0<p<1\), define
\[
 a(p)=1-\sum_{t=1}^{\infty}\frac{p}{t(t+p)},
 \qquad v(p)=\frac2{\Gamma(1+2p)}-\frac1{\Gamma(1+p)^2}.
\]
Here \(a(p)>0\): each summand is smaller than its value at \(p=1\), whose sum is one. Also \(v(p)>0\): the function \(\log[2\Gamma(1+p)^2/\Gamma(1+2p)]\) decreases strictly from \(\log2\) at \(p=0\) to zero at \(p=1\), since the digamma function is strictly increasing. Using \(M_n(a)\sim n^a/\Gamma(1+a)\) gives the exact limit
\[
\boxed{
\sqrt{\log n}\operatorname{Corr}(D_n,C_n(p))
\longrightarrow
\frac{a(p)}{\Gamma(1+p)\sqrt{v(p)}}>0.
}
\]

## Verification

The standalone `verify.py` uses exact rational arithmetic to enumerate every parent vector and every edge-retention pattern for \(n=3,\ldots,7\) at \(p\in\{1/3,1/2,2/3\}\) and additionally \(n=8,p=1/2\). It checks both conditional tail ordering and strictness at tail \(2\), exact first and second moments, and the covariance formula. Independent mixed-moment and local-covariance recurrences are also checked through \(n=100\) at three rational retention parameters. Sixteen exhaustive models and 294 additional recursion comparisons pass. Numerical critical-window diagnostics are illustrations only and do not justify the asymptotic statements.

Reproduce with `python verify.py` using standard Python 3. The proof above, not the finite enumeration or numerical diagnostics, establishes the all-size stochastic comparison and optimizing limit.

## Relationship to prior work

Zhang, Zhou, Zhao, Guan and Zou (arXiv:0711.0080v1, 2007) study the equivalent imperfect-growth/percolation model and derive global marginal degree and component-size distributions; their finite random variable for vertex degree is the degree in the *retained* forest, not the original root degree used here. Their full four-page text does not give the cross-covariance or its retention-parameter optimizer. Baur (arXiv:1407.2508v1, 2014) studies the root cluster and the genealogy of deleted-edge clusters, especially asymptotics as retention tends to one, but not the root-degree/cluster-size joint response. A later root-deletion study (DOI:10.1017/jpr.2024.40) uses the root-parent-indicator coupling for degree-tail analysis rather than the present percolation statistic. Conditioning independent Bernoulli variables on their sum and log-concavity of weighted subset coefficients are standard tools; their general monotonicity is not claimed as new.

The specific claim here is the combined degree-conditioned connectivity ordering, exact joint covariance, and sharp optimizer of that covariance. The existence of general Bernoulli conditioning and percolation recurrences does not by itself state the model-specific optimizer or its \(\zeta(2)-1\) constant.

## Limitations

No assertion is made that the conditional laws are ordered in likelihood-ratio order, that the optimizing \(p\) is unique for every finite \(n\), or that analogous results hold for uniform Cayley trees or preferential-attachment trees. The global covariance maximum is not a maximum of correlation or of outbreak probability. Existing broad theorems could implicitly yield parts of this statement; the historical-priority comparison is not an independent literature audit. Finite code tests do not certify infinite claims. This is a mathematical dependence statement, not an empirical epidemic forecast.

## References

1. Z. Zhang, S. Zhou, S. Zhao, J. Guan and T. Zou, *Degree and component size distributions in generalized uniform recursive tree*, arXiv:0711.0080v1 (public 2007-11-01), https://arxiv.org/abs/0711.0080.
2. E. Baur, *Percolation on random recursive trees*, arXiv:1407.2508v1 (public 2014-07-09), https://arxiv.org/abs/1407.2508.
3. *Quenched worst-case scenario for root deletion in targeted cutting of random recursive trees*, Journal of Applied Probability, DOI:10.1017/jpr.2024.40, https://doi.org/10.1017/jpr.2024.40.
4. F. Pellerey and J. Navarro, *Stochastic monotonicity of dependent variables given their sum*, TEST 31 (2022), 543–561, https://doi.org/10.1007/s11749-021-00789-5 (historical discussion of Efron's conditional-sum theorem; not needed for the self-contained inclusion proof).
