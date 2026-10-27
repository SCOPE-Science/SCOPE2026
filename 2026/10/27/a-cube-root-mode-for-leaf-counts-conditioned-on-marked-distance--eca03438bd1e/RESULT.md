# A cube-root mode for leaf counts conditioned on marked distance in Cayley trees

## Finding

Let \(T_n\) be a uniformly sampled labeled tree on the vertices \([n]\), with \(n\ge3\), and fix two distinct vertices \(u,v\). Write \(D=d_{T_n}(u,v)\) for their graph distance, and \(L\) for the total number of **unrooted** leaves, i.e. vertices of degree one. For every \(1\le k\le n-1\),
\[
\boxed{\mathbb E[L\mid D=k]=\left(n-k-1+\frac{2k}{k+1}\right)\left(\frac{n-1}{n}\right)^{n-k-2}.}
\tag{1}
\]
For \(1\le k\le n-2\), the successive conditional means have the exact difference
\[
\boxed{\mathbb E[L\mid D=k+1]-\mathbb E[L\mid D=k]
=\left(\frac{n-1}{n}\right)^{n-k-3}
\frac{2(n-1)-k(k+1)^2}{n(k+1)(k+2)}.}
\tag{2}
\]
Thus the regression of the *global* leaf count on marked-vertex distance is unimodal, with one or two adjacent maximizers. Its maximum changes from increasing to decreasing precisely when \(k(k+1)^2\) crosses \(2(n-1)\). Equal adjacent means occur **if and only if**
\[
 n=1+\frac{r^2(r-1)}2\qquad\text{for an integer }2\le r\le n-1,
\tag{3}
\]
where the tied distances are \(r-1\) and \(r\). The first cases are \(n=3,10,25,51\). If \(k_n\) is either maximizing distance, then
\[
\boxed{\frac{k_n}{(2n)^{1/3}}\longrightarrow1.}
\tag{4}
\]
In contrast, the probability that either fixed marked endpoint is a leaf **strictly increases** with \(k\), while the total expected number of leaves eventually decreases. For every \(n\ge4\), the first transition \(k=1\) to \(k=2\) is strictly increasing, whereas transitions sufficiently close to the largest distance are strictly decreasing.

## Assumptions and scope

The tree is uniform over all \(n^{n-2}\) Cayley labeled trees; its two marked vertices are fixed labels. Distances are in edges, and a leaf is a vertex of degree exactly one. The conditioning event \(D=k\) has positive probability for each \(1\le k\le n-1\). No additional conditioning on the vertices along the path is imposed.

Define \(q=(n-1)/n\) and \(r=k+1\). When \(r=n\), factors involving \(q^{-1}\) are unambiguously defined since \(q>0\). The deterministic \(n=2\) case is omitted only to avoid a vacuous maximization statement.

## Proof

**Rooted-forest count.** Fix a root set \(R\subseteq[n]\) of size \(r\). The number of undirected forests on \([n]\), each of whose \(r\) components contains exactly one prescribed root, is
\[
F(n,r)=r n^{n-r-1}.
\tag{5}
\]
For \(r=n\) this is \(1\). For \(1\le r<n\), it follows from the matrix-tree theorem for rooted forests: the nonroot Laplacian minor for the complete graph is \(nI_{n-r}-J_{n-r}\), with eigenvalues \(r\) once and \(n\) repeated \(n-r-1\) times. Equation (5) is also the classical rooted-forest enumeration discussed by Pitman.

**Conditioning on a path.** Condition on an exact ordered \(u\)-to-\(v\) path \(P\) using \(r=k+1\) distinct vertices. Removing the \(k\) edges of \(P\) gives a forest rooted at the vertices of \(P\), with precisely one path vertex in each component. Conversely, adding \(P\) to such a forest gives a tree having exactly that marked path. Every corresponding rooted forest is therefore equally likely.

Let \(w\) be one of the \(n-r\) vertices outside \(P\). The event that \(w\) is a leaf is equivalent to deleting \(w\) and its incident edge, leaving a rooted forest with the same \(r\) roots on \(n-1\) vertices. Each such forest has exactly \(n-1\) possible attachment locations for \(w\); hence for \(n>r\),
\[
\mathbb P(\deg(w)=1\mid P)
=\frac{(n-1)F(n-1,r)}{F(n,r)}=q^{n-r-1}.
\tag{6}
\]
At either endpoint of \(P\), degree one occurs exactly when its rooted forest component is an isolated vertex. Removing this isolated root leaves a forest with \(r-1\) prescribed roots on \(n-1\) vertices, so
\[
\mathbb P(\deg(u)=1\mid P)
=\mathbb P(\deg(v)=1\mid P)
=\frac{F(n-1,r-1)}{F(n,r)}
=\frac{r-1}{r}q^{n-r-1}.
\tag{7}
\]
The formula also holds for \(r=n\), when both endpoints are certainly leaves. Every internal path vertex has degree at least two, so cannot be a leaf. Summing the two endpoint contributions and the \(n-r\) off-path contributions in (6)--(7),
\[
\mathbb E[L\mid P]
=\left(n-r+\frac{2(r-1)}r\right)q^{n-r-1}.
\tag{8}
\]
The right side depends only on \(n,r\), not on which intermediate labels make up \(P\). Conditioning only on \(D=k\) therefore gives (1).

**Sharp mode.** Put \(f_n(r)=\left(n-r+2-2/r\right)q^{n-r-1}\). Algebra gives
\[
f_n(r+1)-f_n(r)
=\frac{q^{n-r-2}}{nr(r+1)}\bigl(2(n-1)-r^2(r-1)\bigr),
\qquad 2\le r\le n-1.
\tag{9}
\]
This is (2) after writing \(r=k+1\). The polynomial \(r^2(r-1)\) is strictly increasing for integer \(r\ge2\), so the signs of all successive differences change at most once, from positive to negative. At a zero there is precisely one two-point plateau; (3) is the integer equality condition. Since \(2(n-1)>4\) for \(n\ge4\), the first transition is positive; the last one is negative. Let \(r_n\) be the smallest integer \(r\ge2\) such that \(r^2(r-1)\ge2(n-1)\). It is the unique maximizing \(r\) unless equality holds, when both \(r_n\) and \(r_n+1\) maximize. The defining inequality and monotonic cubic growth give \(r_n\sim(2n)^{1/3}\), hence (4) for \(k_n=r_n-1\) or \(r_n\).

Finally, the endpoint-leaf probability in (7) is \(g(r)=\frac{r-1}{r}q^{n-r-1}\). For \(2\le r<n\),
\[
\frac{g(r+1)}{g(r)}=\frac{r^2}{q(r^2-1)}>1.
\tag{10}
\]
This proves the claimed contrast between local endpoint behavior and the global leaf-count mode.

## Verification

The standalone script `verify_cayley_leaves.py` constructs every Prüfer-coded tree for \(2\le n\le8\) (280,392 trees in total), independently computes both marked distance and every degree-one vertex, and checks all conditional means as exact rational numbers. It also separately verifies the endpoint and off-path contributions, the exact marked-distance law, and all increment signs. Across \(3\le n\le350\), exact rational arithmetic checks each algebraic difference (9), totaling 60,859 assertions. Run with `python verify_cayley_leaves.py`; the observed output ends `VERIFY_OK 60859 exact assertions, 280392 enumerated labeled trees`. These computations corroborate but do not replace the all-\(n\) argument.

## Relationship to prior work

Pitman's classical rooted-forest enumeration gives (5) and related forest-extension identities; they are used as counting tools, not claimed as new. Berzunza Ojeda and Janson analyze distance profiles of simply generated trees, with sections on marking edges and leaves, and establish asymptotic profile results. Their inspected relevant sections do not give (1)--(4), which concern finite-size conditioning of the *total* leaf count on a specified marked pair's distance.

A previously published result, **“Exact negative regression between endpoint degree and distance in a uniform Cayley tree,”** gives the full conditional degree law of one fixed marked endpoint and the monotone decrease of that degree with distance. In particular, it implies the endpoint-leaf probability (7) but does not determine the contribution of all off-path vertices, the complete conditional expectation (1), or its cubic-root maximization criterion. Other work establishes central limit behavior of leaf counts without this conditional finite-size law. The distinction matters: endpoint leaf probability is monotone, whereas the total-leaf regression is not.

## Limitations

The result is for unweighted uniform Cayley trees; it makes no assertion for conditioned Galton--Watson trees with other degree weights, preferential attachment, or uniform unlabelled trees. It establishes a conditional **mean**, not stochastic unimodality or any order of the full conditional leaf-count laws. The cubic-root maximizing distance is atypically short relative to the well-known order-\(\sqrt n\) distance scale. The asymptotic statement is about the location of the mode, not a new limit theorem for leaf counts. Classical forest-enumeration identities enable a short proof, so an earlier implicit derivation in a bivariate generating-function treatment remains a genuine historical-priority risk.

## References

1. G. Berzunza Ojeda and S. Janson, “The distance profile of rooted and unrooted simply generated trees,” arXiv:2009.00572, first public version 2020-09-01; *Combinatorics, Probability and Computing* 31 (2022), 368–410; DOI 10.1017/S0963548321000304.
2. J. Pitman, “Coalescent Random Forests,” Berkeley Statistics Technical Report 457 (publicly dated 1996-09-01); *Journal of Combinatorial Theory, Series A* 85 (1999), 165–193, especially §2.1 on rooted-forest enumeration.
3. “Exact negative regression between endpoint degree and distance in a uniform Cayley tree,” publicly available research note, 2026, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-negative-regression-between-endpoint-degree-and-distance-i--d9ddfb06a9ae.
4. “Distribution of tree parameters by martingale approach,” *Combinatorics, Probability and Computing* (2022), Corollary 1.2 on asymptotic normality of leaf counts.
