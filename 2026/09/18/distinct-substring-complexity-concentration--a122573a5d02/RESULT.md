# Near-root-\(n\) concentration for random distinct-substring complexity

## Statement

Let \(X_1,\ldots,X_n\) be i.i.d. symbols on a finite or countable alphabet, with
\[
p_*:=\sup_a \mathbb P(X_1=a)<1.
\]
Let \(D_n\) be the number of distinct nonempty contiguous substrings of \(X_1\cdots X_n\). Let \(L_n\) be the length of the longest substring that occurs at two different starting positions, with \(L_n=0\) if there is no repeated symbol.

For an integer \(\ell\ge1\), define
\[
c_\ell=\frac{\ell(\ell+1)}2,\qquad
M_n=\frac{n(n+1)}2,\qquad
\delta_\ell=\min\!\left\{1,\binom n2 p_*^{\ell+1}\right\}.
\]

Then for every \(t\ge0\),
\[
\boxed{
\mathbb P\!\left(
|D_n-\mathbb ED_n|\ge t+M_n\delta_\ell
\right)
\le
2\exp\!\left(-\frac{2t^2}{n c_\ell^2}\right)+\delta_\ell .
}
\tag{1}
\]

Moreover,
\[
\boxed{
\operatorname{Var}(D_n)
\le n c_\ell^2+2M_n^2\delta_\ell .
}
\tag{2}
\]

In particular, for
\[
\ell_n=
\max\!\left\{1,\left\lceil
\frac{8\log n}{\log(1/p_*)}
\right\rceil\right\},
\]
one has \(\delta_{\ell_n}\le(2n^6)^{-1}\), and hence
\[
\boxed{
\operatorname{Var}(D_n)=O_{p_*}\!\left(n(\log n)^4\right),
\qquad
D_n-\mathbb ED_n
=
O_{\mathbb P,p_*}\!\left(\sqrt n\,(\log n)^2\right).
}
\tag{3}
\]

This gives a quantitative concentration answer, though not a sharp variance asymptotic, to the long-standing variance question for the total distinct-substring complexity.

## Proof

### 1. A longest-repeat tail bound

Fix two different starting positions and a length \(r\). If the corresponding length-\(r\) blocks are disjoint, then, conditional on the first block, each symbol of the second block must match a prescribed value, so the matching probability is at most \(p_*^r\).

If the blocks overlap, let their starting positions differ by \(s<r\). Revealing the later variables from left to right, the equality event imposes the \(r\) conditions
\[
X_t=X_{t-s}.
\]
At each step the right-hand side is already determined, while \(X_t\) is an independent fresh symbol, so the conditional probability of satisfying the next condition is at most \(p_*\). Thus the same bound \(p_*^r\) holds in the overlapping case. Consequently
\[
\mathbb P(L_n\ge r)
\le
\binom n2 p_*^r.
\tag{4}
\]
For a uniform alphabet of size \(d\), the pairwise matching probability is exactly \(d^{-r}\), including for overlapping blocks.

### 2. The complexity is locally Lipschitz when long repeats are absent

Write \(D_{n,k}(x)\) for the number of distinct length-\(k\) substrings of a deterministic string \(x\), so
\[
D_n(x)=\sum_{k=1}^n D_{n,k}(x).
\]

Changing one coordinate of a string changes at most \(k\) of its length-\(k\) windows. Replacing one window word can change the support size of the multiset of window words by at most one. Hence, if two strings \(x,y\) have Hamming distance \(h\),
\[
|D_{n,k}(x)-D_{n,k}(y)|\le hk.
\tag{5}
\]

Now restrict to
\[
G_\ell=\{x:L_n(x)\le\ell\}.
\]
For every \(x\in G_\ell\) and every \(k>\ell\), all length-\(k\) windows are distinct, so
\[
D_{n,k}(x)=n-k+1.
\]
Therefore, for \(x,y\in G_\ell\),
\[
|D_n(x)-D_n(y)|
\le
h(x,y)\sum_{k=1}^{\ell}k
=
c_\ell h(x,y).
\tag{6}
\]
Thus \(D_n\) restricted to \(G_\ell\) is \(c_\ell\)-Lipschitz for Hamming distance.

### 3. Extend from the typical set and apply bounded differences

By the McShane extension theorem, the restriction of \(D_n\) to \(G_\ell\) has a \(c_\ell\)-Lipschitz extension \(F\) to the whole product space. Clamping \(F\) to \([0,M_n]\) preserves both the Lipschitz constant and its agreement with \(D_n\) on \(G_\ell\).

By (4),
\[
\mathbb P(G_\ell^c)
=
\mathbb P(L_n\ge \ell+1)
\le \delta_\ell.
\tag{7}
\]
Since \(0\le D_n,F\le M_n\) and \(D_n=F\) on \(G_\ell\),
\[
|\mathbb ED_n-\mathbb EF|
\le M_n\delta_\ell.
\tag{8}
\]
The bounded-differences inequality gives
\[
\mathbb P(|F-\mathbb EF|\ge t)
\le
2\exp\!\left(-\frac{2t^2}{n c_\ell^2}\right).
\tag{9}
\]
On \(G_\ell\), the event
\[
|D_n-\mathbb ED_n|\ge t+M_n\delta_\ell
\]
implies \(|F-\mathbb EF|\ge t\). Combining (7)--(9) proves (1).

For the variance, bounded differences also gives
\[
\operatorname{Var}(F)\le \frac12 n c_\ell^2.
\]
Writing \(Y=D_n-F\), one has \(Y=0\) on \(G_\ell\) and \(|Y|\le M_n\), hence
\[
\operatorname{Var}(Y)\le\mathbb EY^2\le M_n^2\delta_\ell.
\]
Therefore
\[
\operatorname{Var}(D_n)
\le 2\operatorname{Var}(F)+2\operatorname{Var}(Y)
\le n c_\ell^2+2M_n^2\delta_\ell,
\]
which is (2).

For \(\ell=\ell_n\), \(p_*^{\ell_n+1}\le p_*n^{-8}\), so
\[
\delta_{\ell_n}\le \frac{1}{2n^6}.
\]
Since \(c_{\ell_n}=O_{p_*}((\log n)^2)\), (2) gives the variance bound in (3), while (1) gives the stated stochastic fluctuation scale.

## Uniform-alphabet consequence

For an unbiased memoryless source on \(d\ge2\) symbols, Janson, Lonardi and Szpankowski (2004) proved
\[
\mathbb E D_n
=
\binom{n+1}{2}
-n\log_d n
+
\left(
\frac12+\frac{1-\gamma}{\ln d}
+\phi_d(\log_d n)
\right)n
+
O(\sqrt{n\log n}),
\]
where \(\phi_d\) is continuous and \(1\)-periodic. Combining that mean expansion with (3) yields
\[
D_n
=
\binom{n+1}{2}
-n\log_d n
+
\left(
\frac12+\frac{1-\gamma}{\ln d}
+\phi_d(\log_d n)
\right)n
+
O_{\mathbb P}\!\left(\sqrt n(\log n)^2\right).
\tag{10}
\]
Thus the order-\(n\) periodic correction in the mean is also visible at the level of a single random string up to a smaller stochastic error.

## Context and originality boundary

Janson, Lonardi and Szpankowski (2004) gave the sharp expectation expansion above and explicitly stated that asymptotic analysis of the variance remained open. Gheorghiciuc and Ward (2007) obtained sharp expectations for fixed-length subword complexity, and Ahmadi and Ward (2020) studied the first two moments of the fixed-\(k\) subword complexity. Those results do not by themselves control the covariance sum over all substring lengths that forms the variance of \(D_n\).

A recent paper of Godbole (2026) revisited \(\mathbb E D_n\) and explicitly asked whether concentration around \(\mathbb E D_n\) can be understood through the variance. The result above gives a partial answer: a finite-sample concentration inequality and the polynomial-logarithmic upper bound
\[
\operatorname{Var}(D_n)=O(n\log^4 n).
\]
To the best of our knowledge, these bounds for the total distinct-substring complexity have not appeared previously. The claim is limited to these concentration and variance upper bounds; no claim is made that the order \(n\log^4 n\) is sharp, or that the asymptotic variance, a central limit theorem, or an optimal tail inequality is known.

## Limitations

The concentration theorem assumes independent symbols and a nondegenerate atom bound \(p_*<1\). It does not cover general Markov or mixing sources. The \((\log n)^4\) variance factor comes from a worst-case Lipschitz estimate on strings whose longest repeat is \(O(\log n)\), and may be far from optimal. No matching variance lower bound, variance constant, or central limit theorem is proved. Older random-trie and suffix-tree literature may contain alternative consequences relevant to the same variance question; the originality assertion is therefore explicitly to the best of our knowledge.

## References

1. A. Godbole, *The Expected Number of Distinct Substrings in an Alphabet String*, arXiv:2609.19409, 2026. https://arxiv.org/abs/2609.19409
2. S. Janson, S. Lonardi, W. Szpankowski, *On average sequence complexity*, Theoretical Computer Science 326 (2004), 213--227. https://doi.org/10.1016/j.tcs.2004.06.023
3. I. Gheorghiciuc, M. D. Ward, *On Correlation Polynomials and Subword Complexity*, Discrete Mathematics & Theoretical Computer Science (2007). https://doi.org/10.46298/dmtcs.3553
4. L. Ahmadi, M. D. Ward, *Asymptotic Analysis of the kth Subword Complexity*, Entropy 22(2):207 (2020). https://doi.org/10.3390/e22020207
5. A. Flaxman, A. W. Harrow, G. B. Sorkin, *Strings with Maximally Many Distinct Subsequences and Substrings*, Electronic Journal of Combinatorics 11(1):R8 (2004). https://doi.org/10.37236/1761
