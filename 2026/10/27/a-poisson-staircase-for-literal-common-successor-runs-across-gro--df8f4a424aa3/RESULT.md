# A Poisson staircase for literal common successor runs across growing families of random orders

## Finding

Let \(\ell\ge2\) be a **fixed** integer. Independently and uniformly sample \(r=r(n)\) permutations \(\Pi_1,\ldots,\Pi_r\) of the same \(n\)-element labelled set, interpreting each as a directed linear-order successor relation \(S_i\). A **literal common run of length \(\ell\)** is an ordered tuple of \(\ell+1\) distinct labels that is consecutive, with the same orientation and all the same labels, in two of these orders. Its length counts **edges**, not vertices. Let \(Y_{n,r}^{(\ell)}\) count these runs with their unordered pair of order indices; let \(L_{n,r}\) be the greatest length of any common run in any order pair, and set it to zero if there is no common directed successor edge.

**Poisson staircase theorem.** For every fixed \(\ell\ge2\), if
\[
\frac{r}{n^{(\ell-1)/2}}\longrightarrow c\in[0,\infty),
\]
then
\[
Y_{n,r}^{(\ell)}\ \xrightarrow{\mathrm d}\ \operatorname{Poisson}(c^2/2).
\]
More quantitatively, writing \((n)_j=n(n-1)\cdots(n-j+1)\) and \(N=\binom r2\), for every fixed \(C\) and \(2\le r\le Cn^{(\ell-1)/2}\),
\[
d_{\mathrm{TV}}\!\left(\mathcal L(Y_{n,r}^{(\ell)}),\operatorname{Poisson}\left(N\frac{n-\ell}{(n)_{\ell}}\right)\right)
=O_{\ell,C}\left(n^{-(\ell-1)/2}+n^{-1}\right).
\]
For \(r/n^{(\ell-1)/2}\to\infty\), the existence probability of a length-\(\ell\) common run tends to one; for \(r/n^{(\ell-1)/2}\to0\), it tends to zero. At positive finite critical ratio, the extreme statistic obeys the sharper two-point law
\[
\Pr\{L_{n,r}=\ell\}\to1-e^{-c^2/2},\qquad
\Pr\{L_{n,r}=\ell-1\}\to e^{-c^2/2}.
\]
At criticality, with probability tending to one, different length-\(\ell\) witnesses share neither any order index nor any labelled vertex. The same particular pair of orders cannot contribute two different witnesses, with high probability.

These probabilistic statements imply a sharp limit curve for the varying-signature first-order existence sentence
\[
\psi_{\ell,r}=\exists x_0\cdots\exists x_{\ell}\;
\bigvee_{1\le i<j\le r}\ \bigwedge_{t=0}^{\ell-1}
\bigl(S_i(x_t,x_{t+1})\wedge S_j(x_t,x_{t+1})\bigr),
\]
namely \(0\), \(1-e^{-c^2/2}\), or \(1\), in the corresponding subcritical, positive critical, or supercritical regimes.

## Assumptions and scope

The labels are common to every order; orders are independent uniform permutations, and repeated sampled orders are allowed. A witness matches **exact labels in the same directed consecutive order**, not merely a pattern up to order-isomorphism. The parameter \(\ell\) is fixed as \(n\to\infty\), while \(r=r(n)\) is any integer at least two. The asymptotic extreme-value statement assumes a positive finite critical ratio. The sentence uses \(\ell+1\) first-order variables and a signature containing \(r\) successor symbols; it is **not** a two-variable or fixed-signature limit theorem. Boundary \(\ell=1\) is excluded from the Poisson theorem: at its nominal scale \(r=O(1)\), common single-edge counts generally do not converge to a Poisson distribution of this kind.

## Proof

**1. Exact one-pair moments.** Condition on an arbitrary first order \(\Pi_1\). It has exactly \(n-\ell\) windows of \(\ell\) edges. For a prescribed window of \(\ell+1\) distinct labels, the chance that an independently uniform second order contains the same window is \((n-\ell)!/n!=1/(n)_{\ell}\). Thus for the number \(Z=Z_{12}^{(\ell)}\) of common runs in one pair,
\[
\mu_{n,\ell}=\mathbb E Z=\frac{n-\ell}{(n)_{\ell}}.
\]
Two windows in the first order are at positive displacement \(d\). If \(1\le d\le\ell\), their requested arcs form one contiguous block of \(\ell+d\) edges, and both appear in the second order with probability \(1/(n)_{\ell+d}\). There are \(n-\ell-d\) such unordered pairs. If \(d>\ell\), the windows have disjoint label sets, so the two requested blocks together contract \(2\ell\) edges and both occur with probability \(1/(n)_{2\ell}\); their number is \(\binom{n-2\ell}{2}\). Hence, for \(n\ge2\ell+2\),
\[
\beta_{n,\ell}:=\mathbb E\binom Z2
=\sum_{d=1}^{\ell}\frac{n-\ell-d}{(n)_{\ell+d}}
+\frac{\binom{n-2\ell}{2}}{(n)_{2\ell}}.
\]
For fixed \(\ell\ge2\), \(\mu_{n,\ell}\sim n^{1-\ell}\) and \(\beta_{n,\ell}=O_{\ell}(n^{-\ell}+n^{2-2\ell})\). Set \(X_{ij}=\mathbf1_{\{Z_{ij}^{(\ell)}\ge1\}}\), and put \(p=\mathbb EX_{12}\). Since \(Z-\mathbf1_{\{Z>0\}}\le\binom Z2\) for nonnegative integer \(Z\),
\[
0\le\mu_{n,\ell}-p\le\beta_{n,\ell}.
\]

**2. A locally dependent Poisson process on order pairs.** Each \(X_{ij}\) depends only on \(\Pi_i,\Pi_j\). Disjoint pairs of order indices are jointly independent of \(X_{ij}\), yielding a dependency graph whose vertices are pairs \(\{i,j\}\) and whose edges join pairs with a common index. For distinct \(i,j,k\), the indicators \(X_{ij}\) and \(X_{ik}\) are in fact **exactly independent**: condition on \(\Pi_i\), and use independence of \(\Pi_j,\Pi_k\). The two conditional event probabilities both equal the same constant \(p\), because relabelling is transitive on fixed first orders. The local-dependency Chen–Stein estimate therefore gives, with \(W=\sum_{i<j}X_{ij}\),
\[
d_{\mathrm{TV}}(\mathcal L(W),\operatorname{Poisson}(Np))
\le C_0 r^3p^2,
\]
for an absolute constant \(C_0\). This is the usual bound in terms of the \(b_1\) and \(b_2\) dependency-neighborhood sums; here each has \(O(r^3)\) contributions of size \(p^2\), and the external-dependence term is zero. Coupling the witness count and pair-incidence count on the original orders gives
\[
\Pr\{Y_{n,r}^{(\ell)}\ne W\}\le N\beta_{n,\ell}.
\]
Replacing the Poisson mean \(Np\) by \(N\mu_{n,\ell}\) costs at most \(N\beta_{n,\ell}\) in total variation. Consequently
\[
d_{\mathrm{TV}}\bigl(\mathcal L(Y_{n,r}^{(\ell)}),\operatorname{Poisson}(N\mu_{n,\ell})\bigr)
\le C_0r^3\mu_{n,\ell}^2+2N\beta_{n,\ell}.
\]
Under \(r\le Cn^{(\ell-1)/2}\), the two terms are respectively \(O_{\ell,C}(n^{-(\ell-1)/2})\) and \(O_{\ell,C}(n^{-1})\). Also \(N\mu_{n,\ell}\to c^2/2\), proving the claimed Poisson law, including the zero limit.

**3. Supercritical existence.** Fix any \(K>0\). If \(r/n^{(\ell-1)/2}\to\infty\), retain only \(\lfloor K n^{(\ell-1)/2}\rfloor\) of the sampled orders. The critical law gives asymptotic existence probability \(1-e^{-K^2/2}\) in this subsample; monotonicity gives the same lower bound in the entire family. Then send \(K\to\infty\).

**4. Maximal-run staircase.** If \(r\sim cn^{(\ell-1)/2}\) for \(c>0\), a length-\(\ell+1\) common run has expected count
\[
\binom r2\frac{n-\ell-1}{(n)_{\ell+1}}=O_{\ell,c}(n^{-1}),
\]
so by Markov there is no longer run with high probability. A length-\(\ell-1\) run exists with high probability. For \(\ell\ge3\), this follows from the supercritical case applied at length \(\ell-1\). For \(\ell=2\), take \(\lfloor r/2\rfloor\) disjoint pairs of orders. For any one pair, the common single-edge count \(Z_1\) has \(\mathbb EZ_1=(n-1)/n\) and \(\mathbb E\binom{Z_1}{2}=(n-2)/(2n)\); hence \(\mathbb EZ_1^2\to2\), and the second-moment inequality gives \(\Pr(Z_1>0)\ge1/2-o(1)\). The disjoint order pairs are independent and their number grows, proving existence of a common single edge with high probability. The Poisson limit now gives the stated two-point distribution.

**5. Isolation of critical witnesses.** At \(r=O(n^{(\ell-1)/2})\), the expected number of two positive pair-incidence indicators sharing an order index is \(O(r^3p^2)=o(1)\). Also \(\Pr(Y\ne W)\le N\beta=o(1)\), so each positive pair has a unique run with high probability. In a positive order pair choose its run at the earliest starting position of its first order; this choice is equivariant under all relabellings. Conditional on existence, the chosen ordered label tuple is therefore uniform over all injections of \(\ell+1\) labels. Chosen runs from two disjoint index pairs are independent, and their vertex sets intersect with probability at most \((\ell+1)^2/n\). Summing over \(O(r^4)\) disjoint pairs of order pairs, weighted by their independent occurrence probabilities \(p^2\), gives \(O_{\ell}(r^4p^2/n)=O_{\ell,C}(n^{-1})\). Markov completes both isolation assertions.

## Verification

The accompanying `successor_run_checker.py` is standalone Python standard-library code. It exactly enumerates the second permutation for each reference permutation length \(3\le n\le8\) and checks both factorial-moment identities. It also checks conditional first-order invariance under multiple reference permutations and exhaustively enumerates all three-order configurations for \(n=4\) and \(\ell=2\). Its observed diagnostic was `SUCCESSOR_RUN_EXACT_OK 184884 588 [9120, 4392, 144, 168]`. These **finite calculations are not a proof of the asymptotic theorem**; Steps 1–5 provide that proof using known Poisson approximation.

## Relationship to prior work

Jeż, Michaliszyn and Witkowski (2026) establish finite satisfiability and model-size bounds for two-variable logic with arbitrarily many successor relations. This provides a fresh motivation for quantitative overlap questions in the same successor-structure class, but their logical satisfiability result does not determine the random-order run-collision law here. Our existence sentence uses \(\ell+1\) variables rather than their two-variable fragment.

Earnest, Godbole and Rudoy (2014) study longest common **relative-order subsequence patterns** in several permutations, not literal consecutive blocks of identical labels present in some unordered pair. Work on distinct consecutive permutation patterns similarly compares relative-order patterns inside a single permutation. Arratia, Goldstein and Gordon (1990) supply the general local-dependency Chen–Stein approximation framework; this theorem's random-order moment computation, growing-family scale, extreme-value staircase and simultaneous disjointness assertions are the specialized conclusions assessed here. The use of that established approximation method does not itself establish historical priority for this specialization.

## Limitations

The result fixes \(\ell\); no uniformity in growing run length is proved. Literal directed label agreement is essential: neither order-isomorphic patterns nor reversed paths are counted. The quantifier count grows with \(\ell\) and the vocabulary grows with \(r\). The Poisson statement does not include the exceptional \(\ell=1\) scale. General prior probability limit results may imply portions of these conclusions, and inaccessible or unlocated specialized literature can affect priority. No independent mathematical validation has been performed.

## References

1. A. Jeż, J. Michaliszyn, P. Witkowski, *Finite Satisfiability of Two-Variable Logic with Arbitrarily Many Successors*, arXiv:2610.19943, first version 2026-10-14, https://arxiv.org/abs/2610.19943.
2. K. Earnest, A. P. Godbole, V. Rudoy, *On the Longest Common Pattern Contained in Two or More Random Permutations*, arXiv:1402.0137 (2014), https://arxiv.org/abs/1402.0137.
3. R. Arratia, L. Goldstein, L. Gordon, *Poisson Approximation and the Chen–Stein Method*, Statistical Science **5** (1990), 403–434, https://doi.org/10.1214/ss/1177012015.
4. A. P. Godbole, A. Swickheimer, *An Alternative Proof for the Expected Number of Distinct Consecutive Patterns in a Random Permutation*, publicly available preprint; distinction used concerns relative-order consecutive patterns, not literal labelled blocks.
