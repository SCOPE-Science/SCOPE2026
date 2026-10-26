# Annealed stable-extension sizes have a sharp Gaussian profile in one-attacker frameworks

## Finding

For every integer \(n\ge2\), let \(f:[n]\to[n]\) be selected uniformly among the \(n^n\) labelled maps and form an abstract argumentation framework with precisely the attacks \(f(v)\to v\), for \(v\in[n]\). Loops are permitted. Write \(Z_{n,k}(f)\) for the number of stable extensions of size exactly \(k\), and put \(w_n(k)=\mathbb E_f Z_{n,k}(f)\).

**Theorem (complete annealed size profile).** For all \(0\le k\le n\),
\[
w_n(k)=\begin{cases}
\displaystyle\binom nk\frac{(n-k)^k k^{n-k}}{n^n},&1\le k\le n-1,\\
0,&k\in\{0,n\}.
\end{cases}
\]
The sequence of its positive terms is symmetric and strictly log-concave (in the conventional sense that every inequality with two positive neighbors is strict). Its mode occurs at the integer(s) closest to \(n/2\). Moreover, uniformly for any fixed \(M>0\) and all integers \(k\) with \(|k-n/2|\le M\sqrt n\),
\[
\sqrt n\,w_n(k)=\sqrt{\frac2\pi}\exp\!\left(-8\frac{(k-n/2)^2}{n}\right)+o(1).
\]
Consequently \(\sum_k w_n(k)\to 1/2\). Under the **annealed pair law**, meaning a uniform choice from all pairs \((f,S)\) with \(S\) stable in \(f\),
\[
\frac{4(|S|-n/2)}{\sqrt n}\ \Longrightarrow\ \mathcal N(0,1),
\qquad \operatorname{Var}(|S|)\sim \frac n{16}.
\]

## Assumptions and scope

The domain is the labelled nonempty finite set \([n]=\{1,\ldots,n\}\). A random choice of attackers is made **independently for each attacked vertex**; outgoing attack counts are unrestricted. A stable extension \(S\) is conflict-free and attacks each vertex outside \(S\). Self-attack is allowed. The annealed pair law samples a mapping proportionally to its number of stable extensions and then a stable extension in it; it is **not** the law formed by uniformly sampling a solvable mapping and then an extension.

## Proof

**1. Exact counting.** In this one-attacker graph, \(S\) is stable if and only if, simultaneously for every vertex \(v\),
\[
\mathbf1_{\{v\in S\}}=1-\mathbf1_{\{f(v)\in S\}}.
\]
Indeed, an accepted vertex cannot have its sole attacker accepted, and a nonaccepted vertex must have that attacker accepted. Fix a subset \(S\) of size \(k\). Each of the \(k\) vertices in \(S\) chooses its attacker among the \(n-k\) vertices outside \(S\), and each of the other \(n-k\) vertices chooses its attacker among the \(k\) inside \(S\). Exactly \((n-k)^k k^{n-k}\) maps make \(S\) stable; there are \(\binom nk\) possible subsets \(S\). Dividing the number of distinguished pairs by \(n^n\) proves the identity, including the zero endpoints.

**2. Symmetry and log-concavity.** Complementing \(S\) gives \(w_n(k)=w_n(n-k)\). On the real interval \(0<t<n\), define
\[
h_n(t)=t\log(n-t)+(n-t)\log t.
\]
Direct differentiation gives
\[
h_n''(t)=-\frac1t-\frac1{n-t}-\frac n{t^2}-\frac n{(n-t)^2}<0.
\]
The generalized binomial coefficient \(\Gamma(n+1)/(\Gamma(t+1)\Gamma(n-t+1))\) is log-concave on this interval, since \(\log\Gamma\) is convex. Hence \(\log w_n(t)\) is strictly concave wherever defined. Restricting to integers proves strict log-concavity for interior consecutive positive terms. Symmetry and concavity imply the stated mode(s).

**3. Central local limit.** Write \(p=k/n\), \(\delta=p-1/2\). Uniform Stirling expansion on \(p\) bounded away from \(0,1\) gives
\[
w_n(k)=\frac{1+O(n^{-1})}{\sqrt{2\pi n p(1-p)}}\exp\left(n(1-2p)\log\frac p{1-p}\right).
\]
For \(\delta=x/\sqrt n\) with bounded \(x\),
\[
(1-2p)\log\frac p{1-p}=-8\delta^2+O(\delta^4),
\quad [2\pi p(1-p)]^{-1/2}=\sqrt{2/\pi}+O(\delta^2).
\]
This yields the announced compact-uniform local limit.

**4. Tails and annealed Gaussian law.** The elementary inequality \(\log\frac{1+2\delta}{1-2\delta}\ge4\delta\) for positive \(\delta\), together with symmetry, implies
\[
(1-2p)\log\frac p{1-p}\le-8\delta^2.
\]
On \(1/4\le p\le3/4\), uniform Stirling gives \(w_n(k)\le Cn^{-1/2}\exp[-8(k-n/2)^2/n]\). Outside this band, the entropy bound \(\binom nk\le\exp(n H(p))\) gives \(w_n(k)\le\exp(-n/2)\). Therefore the contribution outside \(|k-n/2|\le M\sqrt n\) has vanishingly small limsup as \(M\to\infty\). Riemann sums and the local limit now give
\[
\sum_k w_n(k)\longrightarrow\sqrt{\frac2\pi}\int_{-\infty}^{\infty}e^{-8x^2}\,dx=\frac12.
\]
The probability of size \(k\) under the uniform distinguished-pair law is \(w_n(k)/\sum_jw_n(j)\). Its local limit is the lattice-normal density with variance \(n/16\). The same Gaussian-tail envelope provides uniform integrability of squared centered fluctuations, establishing convergence of the normalized second moment and \(\operatorname{Var}(|S|)\sim n/16\). Exact symmetry gives \(\mathbb E|S|=n/2\) for every \(n\ge2\).

## Verification

The companion source `size_profile_checker.py` exhaustively enumerates every map and every possible stable subset for \(1\le n\le6\), independently computes the closed formula, and checks exact histogram equality and strict finite log-concavity. It also checks the normalized central coefficient numerically for three larger values of \(n\). These finite calculations corroborate but do not replace the proof for arbitrary \(n\). The limiting density and variance are established by the analytic estimates above.

## Relationship to prior work

Dung stable semantics and contemporary work on extension diversity motivate counting the accepted cardinality, rather than only deciding extension existence or finding distant pairs. Fichte, Hecher, Mahmood and Wang (2026) study diversity of extensions in general frameworks but do not develop this uniform one-attacker annealed size profile. Yakymiv (2015, 2022) develops general constrained random mappings, including a Gaussian **cycle-count** limit under even-cycle constraints; these statements concern cycle numbers and component sizes, **not** the cardinality of the accepted stable set. In contrast, the formula here counts individual stable subsets of every cardinality, with a distinct \(n/16\) Gaussian size variance. The proof does not assert novelty for the elementary mapping decomposition or the general Stirling method, and an unlocated equivalent bipartite-coloring calculation remains a priority risk.

## Limitations

This result is annealed: mappings with more stable extensions receive greater weight. It does not describe the size of a randomly chosen extension after first sampling a uniformly random framework conditioned on admitting one. Random mappings allowing loops and exactly one attacker per vertex form a restricted model. The findings make no claims for graphs with zero or several attackers at a vertex, nor do they prove a quenched local limit. The known constrained-random-mapping literature supplies stronger coverage for cycle counts but does not, in the inspected material, settle the marked-cardinality profile; complete historical priority has not been established.

## References

1. M. Fichte, M. Hecher, Y. Mahmood, and Z. Wang, *Diversity of Extensions in Abstract Argumentation*, arXiv:2605.13332 (initial public posting 2026-05-13), https://arxiv.org/abs/2605.13332 .
2. A. L. Yakymiv, *On a Number of Components in a Random A-Mapping*, Theory of Probability and Its Applications 59 (2015), DOI:10.1137/S0040585X97986928.
3. A. L. Yakymiv, *Random Mappings with Constraints on the Cycle Lengths*, Journal of Mathematical Sciences 267 (2022), DOI:10.1007/s10958-022-06128-9.
4. S. Finch, *Permute, Graph, Map, Derange*, arXiv:2111.05720 (2022), https://arxiv.org/abs/2111.05720 .
5. S. Gaspers and R. Li, *Enumeration of Preferred Extensions in Almost Oriented Digraphs*, MFCS 2019, DOI:10.4230/LIPIcs.MFCS.2019.74.
