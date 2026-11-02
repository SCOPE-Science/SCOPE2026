# Joint Gaussian fluctuations and a positive descent–inversion correlation in random-to-top shuffles

## Finding

Start an ordered deck \(1,\ldots,n\) and repeatedly select one of its \(n\) labels independently and uniformly, moving the selected card to the top. After \(r\geq1\) moves write \(D_{n,r}\) for the number of adjacent descents, \(I_{n,r}\) for the number of inversions, and \(K_{n,r}\) for the number of distinct labels selected.

**Finite-size theorem.** For every integer \(n\geq2\) and \(r\geq1\), conditional on \(K_{n,r}=k\in\{1,\ldots,n\}\),
\[
\begin{aligned}
 \mu_D(k)&:=\mathbb E[D_{n,r}\mid K_{n,r}=k]=\frac{k-1}{2}+\frac{n-k}{n-k+1},\\
 \mu_I(k)&:=\mathbb E[I_{n,r}\mid K_{n,r}=k]=\frac{k(2n-k-1)}4,\\
 C_{n,k}&:=\operatorname{Cov}(D_{n,r},I_{n,r}\mid K_{n,r}=k)
 =\frac{k-1}{4}+\frac{n-k}{2(n-k+1)}.
\end{aligned}
\]
Consequently the following **exact**, strictly positive covariance identity holds for all such \(n,r\):
\[
\operatorname{Cov}(D_{n,r},I_{n,r})
 =\mathbb E[C_{n,K_{n,r}}]
 +\operatorname{Cov}(\mu_D(K_{n,r}),\mu_I(K_{n,r}))>0.
\]

**Critical-regime joint limit.** Fix \(c>0\), set \(r_n=\lfloor cn\rfloor\), and define \(b=e^{-c}\), \(a=1-b\), and \(t=b-(1+c)b^2>0\). Then
\[
\begin{pmatrix}
 (D_{n,r_n}-na/2)/\sqrt n\\
 (I_{n,r_n}-n^2(1-b^2)/4)/n^{3/2}
\end{pmatrix}
\xrightarrow{\ d\ }
\mathcal N_2\!\left(0,\begin{pmatrix}
 a/12+t/4&bt/4\\
 bt/4&(1-b^3)/36+b^2t/4
\end{pmatrix}\right).
\]
In particular,
\[
\lim_{n\to\infty}\frac{\operatorname{Cov}(D_{n,r_n},I_{n,r_n})}{n^2}
 =\frac{e^{-c}\big[e^{-c}-(1+c)e^{-2c}\big]}4>0.
\]
This nonzero limiting correlation is absent for uniformly random permutations under the same marginal normalization. The two marginal variances coincide with those found in the prior univariate limit theorems.

## Assumptions and scope

All moving-card choices are independent and uniform on the fixed set of card labels; a card may be selected repeatedly. A descent occurs at a position \(i<n\) with deck value in position \(i\) exceeding that in position \(i+1\). An inversion is a pair of positions \(i<j\) with the earlier value larger. The finite-size identities hold for every integer \(n\geq2\) and \(r\geq1\). The asymptotic joint theorem holds for each fixed finite \(c>0\), with \(n\to\infty\) and \(r_n=\lfloor cn\rfloor\); no uniformity in \(c\) as \(c\downarrow0\) or \(c\uparrow\infty\) is asserted. All stated covariances are unconditional unless explicitly marked as conditional.

## Proof

### 1. Uniform-prefix representation and exact conditional moments

Let \(K\) denote the number of distinct selected labels. The standard last-selection-time representation says that conditional on \(K=k\), the deck is distributed as \((\pi_1,\ldots,\pi_k,s_1,\ldots,s_{n-k})\), where \(\pi\) is a uniform permutation of \(\{1,\ldots,n\}\), and \(s_1<\cdots<s_{n-k}\) are the values \(\{\pi_{k+1},\ldots,\pi_n\}\) in increasing order. The conditional prefix distribution is independent of the precise shuffle count \(r\). This representation is established in Clay [1, Proposition 4.1].

Let \(D^{\mathrm p}\) count the \(k-1\) descents internal to the prefix. Let \(B=\mathbf1\{\pi_k>s_1\}\), with \(B=0\) if \(k=n\). Then \(D=D^{\mathrm p}+B\). Define the ordinary Lehmer digits of \(\pi\) by \(R_i=\#\{j>i:\pi_j<\pi_i\}\), \(1\le i\le n\). These are independent, with \(R_i\) uniform on \(\{0,\ldots,n-i\}\). Rearranging the suffix does not change the inversions starting in the first \(k\) positions; therefore \(I=\sum_{i=1}^{k}R_i\). The boundary descent is exactly \(B=\mathbf1\{R_k>0\}\). Thus \(\mathbb EB=(n-k)/(n-k+1)\) and \(\mathbb E I=\sum_{i=1}^k(n-i)/2=k(2n-k-1)/4\). Internal prefix order is uniform, giving \(\mathbb ED^{\mathrm p}=(k-1)/2\).

To compute the covariance, first \(\operatorname{Cov}(B,I)=\operatorname{Cov}(\mathbf1\{R_k>0\},R_k)=(n-k)/(2(n-k+1))\) by digit independence. Separately write \(I=I^{\mathrm p}+I^{\mathrm cross}\), where \(I^{\mathrm p}\) counts inversions inside the prefix and \(I^{\mathrm cross}\) counts inversions between prefix and sorted suffix. The prefix relative order is independent of its selected value set, so \(D^{\mathrm p}\) is independent of \(I^{\mathrm cross}\). For a uniform permutation of \(k\) values, \(\operatorname{Cov}(D^{\mathrm p},I^{\mathrm p})=(k-1)/4\): an adjacent descent indicator has covariance \(1/4\) with the corresponding adjacent inversion indicator, and all other pair-comparison contributions cancel in pairs by symmetry of ranks (equivalently [2, Lemma 2.6]). This proves the three exact conditional formulas. The total covariance formula follows from conditional covariance decomposition. As functions of \(k\), both means are nondecreasing, so their covariance under any law of \(K\) is nonnegative by the independent-copy identity; moreover \(C_{n,k}>0\) for every \(1\le k\le n\) when \(n\ge2\). Hence strict positivity.

### 2. Conditional joint central limit theorem

Take any deterministic sequence \(k_n/n\to a\in(0,1)\). Conditional on \(K=k_n\), let \(U\) be the uniform \(k_n\)-element subset of labels in the prefix; its relative permutation order is uniform and independent of \(U\). Decompose
\[
I=I^{\mathrm p}+I^{\mathrm cross},\qquad
I^{\mathrm cross}=\sum_{u\in U}u-\frac{k_n(k_n+1)}2,
\]
while \(D=D^{\mathrm p}+B\) and \(0\le B\le1\). Sampling without replacement yields
\[
\operatorname{Var}(I^{\mathrm cross}\mid K=k_n)
=\frac{k_n(n-k_n)(n+1)}{12},
\]
and its centered version divided by \(n^{3/2}\) converges to a normal law with variance \(a(1-a)/12\). One may prove this by the standard finite-population central limit theorem: population labels lie in \([1,n]\), the sampling fraction stays bounded away from 0 and 1, and the largest centered label divided by the standard deviation of the sample sum is \(O(n^{-1/2})\).

To treat the prefix order, generate its uniform relative ranks from independent \(X_1,\ldots,X_{k_n}\sim\mathrm{Uniform}(0,1)\). Then
\[
D^{\mathrm p}=\sum_{i=1}^{k_n-1}\mathbf1\{X_i>X_{i+1}\},\qquad
I^{\mathrm p}=\sum_{1\le i<j\le k_n}\mathbf1\{X_i>X_j\}.
\]
The Hájek (first-order Hoeffding) projection of the centered inversion sum is
\[
P_{k_n}=\sum_{i=1}^{k_n}(k_n+1-2i)(X_i-1/2).
\]
A direct comparison-indicator calculation gives
\[
\operatorname{Var}(I^{\mathrm p}-\mathbb EI^{\mathrm p}-P_{k_n})
=\frac{k_n(k_n-1)}{24}=O(n^2),
\]
so that projection error is negligible on the \(n^{3/2}\) scale. Its projected variance is \(k_n(k_n^2-1)/36\), yielding limiting variance \(a^3/36\). The descent indicators are bounded, stationary and one-dependent, with variance \((k_n+1)/12\) for their sum, giving the limiting variance \(a/12\) on the \(\sqrt n\) scale. The cross-covariance of the descent sum with the projection equals \((k_n-1)/6=O(n)\), because each descent indicator interacts only with the two coefficients at its adjacent positions, differing by two.

Every Cramér–Wold combination of the normalized descent sum and projected inversion sum is a triangular array of bounded, one-dependent contributions of order \(n^{-1/2}\), and hence satisfies the one-dependent triangular-array central limit theorem. For completeness, partition into blocks of length \(\lfloor n^{1/4}\rfloor\), removing a single variable between consecutive blocks: removed terms have vanishing variance, independent blocks have maximal magnitude \(O(n^{-1/4})\) and satisfy Lindeberg. Their limiting cross-covariance is zero, so their limiting Gaussian coordinates are independent. Since \(U\) is independent of the relative prefix order, the cross inversion component contributes a third independent Gaussian. We obtain, for every such \(k_n\),
\[
\left(\frac{D-\mu_D(k_n)}{\sqrt n},\frac{I-\mu_I(k_n)}{n^{3/2}}\right)
\xrightarrow{\ d\ }
\mathcal N_2\!\left(0,\operatorname{diag}\!\left(\frac a{12},\frac{a^3+3a(1-a)}{36}\right)\right).
\]
The second diagonal element simplifies to \((1-(1-a)^3)/36\). The asserted convergence along every deterministic sequence with \(k_n/n\to a\) implies conditional convergence in probability for random \(K/n\to a\), by the subsequence principle. It also gives asymptotic independence of the conditional Gaussian noise from the occupancy fluctuation.

### 3. Occupancy fluctuations and the joint limit

For \(r_n=\lfloor cn\rfloor\) iid selections, classical uniform occupancy statistics (recorded explicitly in [1, Proposition 3.1]) give
\[
\frac{K-na}{\sqrt n}\xrightarrow{\ d\ }\mathcal N(0,t),\quad
\frac Kn\xrightarrow{\ P\ }a,\quad
\frac{\operatorname{Var}K}n\longrightarrow t,
\]
where \(a=1-e^{-c}\), \(t=e^{-c}-(1+c)e^{-2c}\). The exact variance is
\[
\operatorname{Var}K=n(1-1/n)^{r_n}+n(n-1)(1-2/n)^{r_n}
-n^2(1-1/n)^{2r_n}.
\]
Taylor expansion of the exact conditional means, uniformly when \(K=an+O_{\mathbb P}(\sqrt n)\), gives
\[
\begin{aligned}
\frac{\mu_D(K)-na/2}{\sqrt n}&=\frac{K-na}{2\sqrt n}+o_{\mathbb P}(1),\\
\frac{\mu_I(K)-n^2(1-b^2)/4}{n^{3/2}}
&=\frac b2\frac{K-na}{\sqrt n}+o_{\mathbb P}(1).
\end{aligned}
\]
Thus the limiting pair is distributed as \((G_D+H/2,G_I+bH/2)\), with independent centered Gaussians
\[
\operatorname{Var}G_D=a/12,\quad
\operatorname{Var}G_I=(1-b^3)/36,\quad
\operatorname{Var}H=t.
\]
This yields the stated full covariance matrix. The matrix is positive definite since \(a>0\), \(1-b^3>0\), and \(t>0\).

For the covariance limit (which does not follow solely from convergence in law), apply the *finite exact* conditional covariance formula. Its first contribution satisfies \(\mathbb E C_{n,K}=O(n)\), hence is negligible compared with \(n^2\). For the second, \(\mu_D(K)=K/2+O(1)\) and \(\mu_I(K)=nK/2-K^2/4+O(n)\). Taylor expansion about \(na\) and \(\operatorname{Var}K/n\to t\) show
\[
\frac1{n^2}\operatorname{Cov}(\mu_D(K),\mu_I(K))\to\frac{bt}{4}.
\]
The remainder is justified by \(\mathbb E(K-\mathbb EK)^4=O(n^2)\), which follows from bounded differences since changing one of the \(r_n=O(n)\) independent selections changes \(K\) by at most one. This proves both the joint limit and the covariance asymptotic.

## Verification

The accompanying self-contained Python 3 checker uses exact rational arithmetic to enumerate every uniform conditional prefix distribution for \(2\le n\le7\) and \(1\le k\le n\), and every actual move sequence for \(2\le n\le6\), \(1\le r\le6\). It compares means and covariances with the exact theoretical identities and checks their signs. A deterministic occupancy recursion evaluates the normalized finite-size covariance at \(n=80,160,320,640\) for \(c=0.5,1,2\) and compares with the nonzero asymptotic constant. All **219 assertions passed** in the recorded execution. The proof, not the finite enumeration, establishes the unbounded-\(n\) limit. Run `python3 checker.py` without external dependencies.

## Relationship to prior work

Clay [1] establishes the random-to-top conditional prefix representation, occupancy fluctuation theorem, and **separate** critical-regime marginal central limit theorems for descents and inversions. The present joint two-dimensional limit is not obtained from marginal weak convergence alone: it identifies a strictly positive shared-occupancy fluctuation, an exact finite-size cross-covariance and an explicit limiting correlation. Dörr and Heiny [2, Lemma 2.6 and Section 3] compute the uniform-permutation descent–inversion covariance and their joint asymptotic independence; a uniform permutation corresponds to full randomization, not the nonuniform critical random-to-top law. The key phenomenon is that conditional descent–inversion dependence is asymptotically negligible after joint scaling, while fluctuations of the number of moved labels create nonzero dependence.

## Limitations

These are self-review mathematical arguments and computational checks, not independent verification. The result concerns a sorted starting deck, uniform move-to-top selection, and fixed \(c\in(0,\infty)\). It gives no convergence rates, no result for nonuniform card selection, and no uniform statement across the degenerate limits \(c\downarrow0\) or \(c\uparrow\infty\). Historical priority is provisional: sufficiently general unindexed multivariate shuffle-statistic theorems could contain an equivalent statement. Finite checks cannot certify an infinite asymptotic claim; their role is to corroborate the exact formulas used in its proof.

## References

[1] A. Clay, *On the statistics of random-to-top shuffles*, arXiv:2603.09008, first posted 2026-03-09, https://arxiv.org/abs/2603.09008 . Especially Proposition 3.1, Proposition 4.1 and Theorems 1.2–1.3, 4.2–4.3, 6.1 and 7.1.

[2] P. Dörr and J. Heiny, *Joint extremes of inversions and descents of random permutations*, arXiv:2309.17314, first posted 2023-09-29, https://arxiv.org/abs/2309.17314 . Especially Lemma 2.6 and the discussion of the joint central limit theorem.
