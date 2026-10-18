# Reverse likelihood-ratio ordering and residual degree–parity correlation in random labeled trees

## Finding

Let \(T_n\) be a uniformly distributed tree on the labels \(\{1,\ldots,n\}\), with root label \(1\), for an integer \(n\ge2\). Let \(B_n\) be the number of vertices at even graph distance from the root, including the root, and let \(D_n\) be its degree.

**Exact joint law and reverse likelihood-ratio order.** For every \(1\le k\le n-1\),
\[
D_n\mid\{B_n=k\}\ \stackrel{d}{=}\ 1+\operatorname{Bin}\!\left(n-k-1,\frac1k\right).
\]
Equivalently, with \(m=n-k\), for integers \(1\le d\le m\),
\[
\Pr(B_n=k,D_n=d)=\frac{\binom{n-1}{k-1}m^{k-1}\binom{m-1}{d-1}(k-1)^{m-d}}{n^{n-2}},
\]
where \(0^0=1\). For \(k<\ell\) and \(d<e\), the joint probability kernel \(p\) satisfies the *reverse total-positivity inequality*
\[
p(k,d)p(\ell,e)\le p(k,e)p(\ell,d).
\]
For all nondecreasing real functions \(f,g\) on the corresponding finite state spaces, \(\operatorname{Cov}(f(B_n),g(D_n))\le0\). For \(n\ge3\) this is strict when both functions are strictly increasing; the variables are nonconstant. In particular the distinguished degree is stochastically decreasing, indeed decreasing in likelihood-ratio order, as the size of its even-distance class increases.

**A finite covariance identity and a nonvanishing asymptotic residue.** Define \(q_n(k)=\frac{n}{2k}\Pr(B_n=k)\). This is a probability distribution symmetric under \(k\mapsto n-k\). With \(V_n\) its variance,
\[
\operatorname{Cov}(B_n,D_n)=-\frac{4(n-1)}{n^2}V_n,
\qquad
\operatorname{Var}(B_n)=V_n\left(1-\frac{4V_n}{n^2}\right).
\]
As \(n\to\infty\),
\[
\operatorname{Cov}(B_n,D_n)\longrightarrow-\frac14,
\qquad
\sqrt n\,\operatorname{Corr}(B_n,D_n)\longrightarrow-1.
\]
At the same time, there is **joint asymptotic independence**:
\[
\left(\frac{4(B_n-n/2)}{\sqrt n},D_n\right)
\ \Longrightarrow\ (Z,1+P),
\]
where \(Z\sim N(0,1)\) and \(P\sim\operatorname{Poisson}(1)\) are independent. Thus weak asymptotic independence coexists with a nonzero limiting unscaled covariance; this does not contradict asymptotic independence because the first variable's fluctuations grow as \(\sqrt n\).

## Assumptions and scope

All trees are simple, unrooted, uniformly labeled Cayley trees, with a fixed distinguished root at label \(1\); by label invariance this has the same distribution as a uniformly random root. The class \(B_n\) contains exactly the vertices at even distance from this root, not the greedy independent set on the same tree. Although these two class-size statistics have equal *marginal* laws [Contat], that equality does not transfer their joint law with \(D_n\). For \(n=2\), both random variables are constant and all covariances are zero. For \(n\ge3\) all \(k\in\{1,\ldots,n-1\}\) have positive probability.

## Proof

**1. Weighted tree count.** Fix an even class \(A\subseteq[n]\) of size \(k\) containing the root, and its complement \(C\) of size \(m=n-k\). Every tree with this bipartition is a spanning tree of the complete bipartite graph \(K_{k,m}\). Assign weight \(x_a\) to every edge incident to \(a\in A\), and set \(S=\sum_{a\in A}x_a\). The weighted spanning-tree enumerator is
\[
\tau(x)=m^{k-1}S^{m-1}\prod_{a\in A}x_a.
\]
To verify the identity without an external counting lemma, delete any vertex of \(C\) from the weighted Laplacian. Its principal cofactor has the \(k\times k\) diagonal block \(m\operatorname{diag}(x_a)\), and its remaining \((m-1)\times(m-1)\) Schur complement equals \(S(I_{m-1}-J_{m-1}/m)\). The latter has eigenvalues \(S\) (multiplicity \(m-2\)) and \(S/m\) (multiplicity one); when \(m=1\), the block is empty, with determinant one. The matrix-tree theorem gives the displayed enumerator, including all edge cases.

Set \(x_1=z\) and all other \(x_a=1\). The exponent of \(z\) counts the degree of the root; therefore the enumerator becomes \(m^{k-1}z(k-1+z)^{m-1}\). There are \(\binom{n-1}{k-1}\) choices of \(A\). Taking its coefficient of \(z^d\), then dividing by the total \(n^{n-2}\) of labeled trees, gives the joint law. Setting \(z=1\) gives the previously known parity-class marginal
\[
\Pr(B_n=k)=\frac{\binom{n-1}{k-1}k^{n-k-1}(n-k)^{k-1}}{n^{n-2}}.
\]
Dividing the weighted enumerator by its value at \(z=1\) establishes the conditional binomial law.

**2. Monotone likelihood ratio.** Let \(h_k(d)=\Pr(D_n=d\mid B_n=k)\). For \(2\le k<n\), whenever both adjacent masses are positive,
\[
\frac{h_k(d+1)}{h_k(d)}=\frac{n-k-d}{d(k-1)}.
\]
For \(k<\ell\), this adjacent-mass ratio is at least as large at \(k\) as at \(\ell\); the supports \(\{1,\ldots,n-k\}\) are nested. The case \(k=1\) is a point mass at \(n-1\). Together these facts establish the reverse total-positivity inequality, even at zero entries. The distribution \(D_n\mid B_n=k\) is consequently nonincreasing in stochastic order with \(k\). Hence \(k\mapsto\mathbb E[g(D_n)\mid B_n=k]\) is nonincreasing for every increasing \(g\); the covariance of an increasing and a decreasing function of the same variable is nonpositive. For \(n\ge3\), the conditional laws at \(k=1\) and \(k=n-1\) have distinct, ordered point masses; this proves strictness for strictly increasing \(f,g\).

**3. Exact covariance and symmetrization.** The binomial regression gives
\[
\mathbb E[D_n\mid B_n=k]=\frac{n-1}{k},\quad
\mathbb E[B_nD_n]=n-1.
\]
The classical ordinary Prüfer code gives \(D_n\stackrel d=1+\operatorname{Bin}(n-2,1/n)\). Thus
\[
\mathbb E D_n=\frac{2(n-1)}n,\qquad
\operatorname{Var}(D_n)=\frac{(n-1)(n-2)}{n^2},\qquad
\operatorname{Cov}(B_n,D_n)=\frac{n-1}n(n-2\mathbb E B_n).
\]
The explicit class-size law gives \(\Pr(B_n=k)/\Pr(B_n=n-k)=k/(n-k)\), and the regression plus \(\mathbb E D_n\) gives \(\mathbb E(1/B_n)=2/n\). Thus \(q_n(k)=n\Pr(B_n=k)/(2k)\) is normalized and symmetric about \(n/2\). Write \(V_n=\mathbb E_{q_n}(k-n/2)^2\). By symmetry all odd centered moments of \(q_n\) vanish. Using \(\Pr(B_n=k)=2k q_n(k)/n\), the first two moments are
\[
\mathbb E B_n=\frac n2+\frac{2V_n}{n},\quad
\mathbb E B_n^2=\frac{n^2}{4}+3V_n.
\]
Substitution proves both displayed finite variance and covariance identities. Since \(V_n>0\) for \(n\ge3\), covariance is strictly negative.

**4. Asymptotics and independent limits.** Contat's parity-class theorem [Contat, Theorems 1–2] proves both a local Gaussian limit with normalization \(4(B_n-n/2)/\sqrt n\) and the existence of a \(\{0,1\}\)-valued \(\varepsilon_n\) such that \(B_n\stackrel d=n-B_n+\varepsilon_n\) and \(\Pr(\varepsilon_n=1)\to1/4\). Taking expectations yields \(2\mathbb E B_n-n\to1/4\); therefore \(4V_n/n\to1/4\), or \(V_n/n\to1/16\). The exact formulas above now give \(\operatorname{Cov}(B_n,D_n)\to-1/4\), \(\operatorname{Var}(B_n)/n\to1/16\), and hence \(\sqrt n\operatorname{Corr}(B_n,D_n)\to-1\), since \(\operatorname{Var}(D_n)\to1\).

For the joint limit, the marginal Gaussian limit implies \(B_n/n\to1/2\) in probability. For each \(0\le z\le1\), the conditional probability generating function is
\[
\mathbb E[z^{D_n}\mid B_n=k]
=z\left(1+\frac{z-1}{k}\right)^{n-k-1}.
\]
When \(k/n\to1/2\), this converges to \(z\exp(z-1)\), the generating function of \(1+\operatorname{Poisson}(1)\); convergence is uniform for \(k/n\) in any shrinking central band that converges to \(1/2\). Joint test functions of the normalized class size and \(z^{D_n}\), followed by convergence of the marginal Gaussian law, factorize. Tightness of the integer-valued degree laws (from their bounded mean) and uniqueness of probability generating functions establish the stated independent joint limit.

## Verification

Run `python verify.py` with Python 3 and only the standard library. The checker independently constructs each labeled tree by its ordinary Prüfer code for \(2\le n\le8\), extracts the even-distance class and root degree, and compares every joint count to the coefficient formula. It also checks the reverse total-positivity inequalities through \(n=22\), the exact symmetric reweighting and variance identities, and numerical asymptotic values at \(n=100,500,1000\). In the recorded execution the checker passed 203981 assertions. Finite enumeration is not a proof of an all-\(n\) statement; the all-size claims follow from the Laplacian determinant and algebra above, and the limiting assertions use the cited marginal limit results.

## Relationship to prior work

Féray and Kortchemski [FK] derive joint population-size identities for conditioned alternating two-type trees, providing an existing probabilistic setting for colored tree counts; their Corollary 3.4 concerns type-population sizes, not the distinguished-degree reverse likelihood-ratio ordering. Contat [Contat] establishes the exact marginal distribution of the even-depth class and its local Gaussian and near-symmetry laws. Those marginal theorems are reused explicitly; they do not furnish a joint root-degree probability kernel or the all-increasing-functions covariance inequalities. The weighted complete-bipartite tree-count identity is classical; the claim here is its probabilistic synthesis into the reverse likelihood-ratio law, exact covariance identities, and asymptotic dependence phenomenon. The older literature on equicolourable trees is relevant background [Pippenger] but provides no inspected matching joint statement. Novelty remains conditional on the inspected literature, not a claim of exhaustive historical priority.

## Limitations

The result concerns a specified root, not a uniformly chosen new root after conditioning on the tree. The parity class and the greedy independent set have equal marginal distributions but no joint equivalence with root degree is asserted. Independence is an asymptotic statement for the *scaled* parity-class count and the unscaled root degree; the unscaled covariance remains nonzero. No quantitative error bound on joint convergence is proved. Some earlier literature on rooted degree refinements of bitype tree enumeration could implicitly imply the result; historical-priority verification is not exhaustive. Independent auditing has not been performed.

## References

[FK] V. Féray and I. Kortchemski, *The geometry of random minimal factorizations of a long cycle via biconditioned bitype random trees*, Annales Henri Lebesgue 1 (2018), 149–226; first arXiv version 2017-12-18, arXiv:1712.06542; DOI:10.5802/ahl.5.

[Contat] A. Contat, *Surprising identities for the greedy independent set on Cayley trees*, first arXiv version 2021-03-05, arXiv:2103.03800, especially Theorems 1 and 2.

[Pippenger] N. Pippenger, *Enumeration of Equicolourable Trees*, University of British Columbia Technical Report TR-2000-04 (2000); relevant classical bipartite-tree enumeration background.
