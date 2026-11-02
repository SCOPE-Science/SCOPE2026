# Two sharp windows for repeated zero-gap lengths in uniform weak compositions

## Finding
For integers \(n\ge 2\) and \(m\ge 0\), choose uniformly from all \(n\)-term weak compositions \(W=(W_1,\ldots,W_n)\) of \(m\). A *gap* is a maximal nonempty contiguous run of zero terms, including runs touching either endpoint. Let \(Y_{n,m}\) count unordered pairs of distinct gaps with equal lengths. All limits below are as \(n\to\infty\), with integer \(m=m(n)\).

1. If \(m/n^{1/3}\to 0\), then \(\Pr(Y_{n,m}>0)\to0\).
2. If \(m/n^{1/3}\to c\in(0,\infty)\), then \(Y_{n,m}\Rightarrow\operatorname{Pois}(c^3/4)\), and \(\Pr(Y_{n,m}>0)\to1-e^{-c^3/4}\).
3. If \(m/n^{1/3}\to\infty\) and \(m/n^2\to0\), then \(\Pr(Y_{n,m}>0)\to1\), with *no restriction* on the intermediate growth of \(m\).
4. If \(m/n^2\to b\in(0,\infty)\), then \(Y_{n,m}\Rightarrow\binom{Z_b}{2}\), where \(Z_b\sim\operatorname{Pois}(1/b)\). Thus \(\Pr(Y_{n,m}>0)\to 1-(1+1/b)e^{-1/b}\).
5. If \(m/n^2\to\infty\), then \(\Pr(Y_{n,m}>0)\to0\).

The principal classification is the persistent high-probability **intermediate regime** between two distinct transition scales. The low-mass Poisson spacing window is a transfer of classical work on coincident spacings; it is not claimed as a standalone new priority result.

## Assumptions and scope
The law is uniform over the \(\binom{m+n-1}{n-1}\) weak compositions, not multinomial allocation of \(m\) labeled balls. Gaps have strictly positive lengths: two zero-length intervals between consecutive occupied sites are **not** counted. Endpoint gaps count whenever nonempty. \(Y_{n,m}\) counts pairs rather than distinct repeated lengths.

## Proof
**1. Support and gaps.** Let \(K\) be the number of strictly positive terms and \(Z=n-K\) the number of zero terms. For \(m\ge1\),
\[
\Pr(K=k)=\frac{\binom nk\binom{m-1}{k-1}}{\binom{m+n-1}{n-1}},\quad
\mathbb EK=\frac{nm}{n+m-1},\quad
\mathbb EZ=\frac{n(n-1)}{n+m-1}.
\]
Conditionally on \(K=k\), the positive support is a uniformly random \(k\)-subset of the \(n\) positions. The \(L=k+1\) zero intervals before, between and after these sites form a **uniform weak composition** \((G_1,\ldots,G_L)\) of \(N=n-k\). Its positive entries are precisely the gap lengths, and
\[
Y_{n,m}=\sum_{1\le i<j\le L}\mathbf1\{G_i=G_j\ge1\}.
\]
The support indicators are negatively pairwise correlated because
\[
\Pr(W_i=W_j=0)=\frac{(n-1)(n-2)}{(n+m-1)(n+m-2)}
\le\left(\frac{n-1}{n+m-1}\right)^2.
\]
Therefore \(\operatorname{Var}(K)=\operatorname{Var}(Z)\le \mathbb EK\) and also \(\operatorname{Var}(Z)\le\mathbb EZ\).

**2. A uniform spacing-collision lemma.** Suppose \(L\to\infty\), \(N\to\infty\), and \(q=L/(N+L)\le2/3\); put \(p=1-q\). For a uniform weak composition \((G_i)_{i=1}^L\) of \(N\), every *fixed* finite system of positive equalities whose equality classes have sizes \(s_1,\ldots,s_h\ge2\) has probability
\[
(1+o(1))\prod_{j=1}^{h}\frac{q^{s_j}p^{s_j}}{1-p^{s_j}}.
\tag{1}
\]
The error is uniform along such sequences for a fixed equality pattern. To see this, take independent geometric random variables \(X_i\), each with \(\Pr(X_i=t)=qp^t\) for \(t\ge0\). Their law conditional on \(\sum_iX_i=N\) is exactly uniform over the weak compositions. Before conditioning, each equality class has probability \(\sum_{t\ge1}q^s p^{st}=q^s p^s/(1-p^s)\), independently across classes. Conditioned on these equality classes, the finitely many constrained variables have a total of order \(1/q\) with exponentially decaying tails on that scale. The remaining \(L-v\) variables, where \(v=\sum_j s_j\) is fixed, have negative-binomial mass
\[
\Pr\Big(\sum_{i=1}^{L-v}X_i=u\Big)=\binom{u+L-v-1}{L-v-1}q^{L-v}p^u.
\]
Stirling's formula applied at \(u=N-t\), uniformly for \(0\le t\le (\log L)^2/q\), shows that this mass divided by the mass \(\Pr(\sum_{i=1}^{L}X_i=N)\) tends to one: the center shifts by only \(O((\log L)^2/q)\), while the standard deviation is \(\asymp\sqrt L/q\). The same binomial mass formula bounds the ratio uniformly by a constant outside this range; exponential tails dispose of the remainder. This proves (1) without assuming independent gaps.

In particular, write
\[
a(q)=\frac{qp^2}{2-q},\qquad b(q)=\frac{q^2p^3}{3-3q+q^2}.
\]
A specified positive pair tie has probability \(a(q)(1+o(1))\), a positive triple tie has probability \(b(q)(1+o(1))\), and two disjoint pair ties have probability \(a(q)^2(1+o(1))\). For the pair-tie count \(Y\),
\[
\mathbb EY\sim\binom L2a(q),\qquad
\operatorname{Var}(Y)\le O(L^2q+L^3q^2)+o(L^4q^2),
\tag{2}
\]
whenever \(q\le2/3\). If \(L^3/(N+L)\to\infty\), this yields \(Y>0\) with probability tending to one, because \(a(q)\asymp q\), \(b(q)=O(q^2)\), and the variance divided by the squared mean tends to zero.

**3. Initial window.** If \(m\asymp n^{1/3}\), the expected excess \(m-K=m(m-1)/(m+n-1)\) tends to zero; hence \(K=m\) with high probability. Conditionally on that event the gap-vector length is \(L=m+1\), its sum is \(N=n-m\), and \(q=(m+1)/(n+1)\). The expected number of zero entries in the gap vector is \((m+1)m/n=o(1)\), so its nonempty gaps are exactly the \(L\) entries with high probability. By (1), an unordered specified pair coincides with probability \(\sim m/(2n)\). Consequently \(\mathbb EY\to c^3/4\) when \(m/n^{1/3}\to c\).

For every fixed integer \(r\ge1\), expand the factorial moment \(\mathbb E(Y)_r\) over ordered sets of \(r\) distinct edges on the \(L\) gap labels. The graphs consisting of \(r\) disjoint edges contribute
\[
\frac{(L)_{2r}}{2^r}\left(\frac{q}{2}\right)^r\longrightarrow(c^3/4)^r.
\]
Any graph containing a connected component of \(s\ge3\) vertices contributes negligibly: by (1), such a component has only \(O(L^s q^{s-1})=O(n^{(2-s)/3})=o(1)\) total contribution, while each two-vertex component has bounded total contribution. Thus all factorial moments converge to those of \(\operatorname{Pois}(c^3/4)\). For \(m=o(n^{1/3})\), the same first-moment argument bounds \(\Pr(Y>0)\) by \(O(m^3/n)\) if \(m\to\infty\); for bounded \(m\), direct weak-composition counting gives \(O(1/n)\). The case \(m=0\) has at most one gap.

**4. Persistence up to linear mass.** Suppose \(m\gg n^{1/3}\) and \(m\le n/2\). From \(\mathbb EK=nm/(n+m-1)\ge(2/3+o(1))m\) and \(\operatorname{Var}(K)\le\mathbb EK\), with high probability \(K\gg n^{1/3}\). With \(L=K+1\), \(N=n-K\), we have \(q=(K+1)/(n+1)\le2/3\) for large \(n\), and \(L^3/(N+L)\to\infty\). Applying (2) conditionally on \(K\) proves persistence throughout this range.

**5. Persistence from linear to nearly quadratic mass.** Suppose \(n/2\le m\ll n^2\). Then \(\mathbb EZ=n(n-1)/(n+m-1)\to\infty\), while \(\mathbb EZ/n\le2/3+o(1)\); because \(\operatorname{Var}(Z)\le\mathbb EZ\), with high probability \(Z\to\infty\) and \(Z/n\le3/4\). Given \(Z=z\), its positions are a uniformly random \(z\)-subset. Let \(J\) count zeros at interior sites whose two neighbors are nonzero. Exact hypergeometric counting gives
\[
\mathbb E(J\mid Z=z)=\frac{z(n-z)(n-z-1)}{n(n-1)}\asymp z
\]
for \(z\to\infty\) and \(z/n\le3/4\). The joint probability of two nonoverlapping isolated-zero events uses \((z)_2(n-z)_4/(n)_6\), which differs from the product of the respective marginals by a relative \(O(1/z+1/(n-z))\); there are only \(O(n)\) overlapping pairs. Thus \(\operatorname{Var}(J\mid Z=z)=O(z+z^2/n)=o((\mathbb E J)^2)\) uniformly in this range. Hence \(J\to\infty\) with high probability. Every such isolated zero is a distinct gap of length one, so \(Y>0\) with high probability. Together with Step 4, this establishes the entire intermediate regime even when \(m/n\) oscillates.

**6. Terminal window and extinction.** For each fixed positive integer \(r\),
\[
\mathbb E(Z)_r=\frac{(n)_r(n-1)_r}{(n+m-1)_r}.
\]
If \(m/n^2\to b\in(0,\infty)\), these factorial moments converge to \(b^{-r}\), so \(Z\Rightarrow\operatorname{Pois}(1/b)\). The expected number of adjacent zero pairs is
\[
(n-1)\frac{(n-1)(n-2)}{(n+m-1)(n+m-2)}=O(n^{-1}).
\]
Therefore all zero terms are isolated with high probability, giving \(Y=\binom Z2\) there and the stated terminal limit. If \(m/n^2\to\infty\), then \(\mathbb EZ\to0\), and Markov's inequality gives \(Y=0\) with high probability. This completes the classification.

## Verification
The accompanying `verify.py` uses Python's standard library and exact integers/rationals. It checks the support-size distribution, both displayed factorial zero moments, conditional uniform-gap pair counting, and specified positive-pair equalities for small parameters. Executing `python verify.py` passed 602 exact identities after enumerating 12,854 weak compositions. Independently, Monte Carlo tests of uniform supports at \((n,m)=(8000,20),(64000,40),(512000,80)\) gave approximate mean pair counts 0.256, 0.251 and 0.258, compared with the limiting value 0.25. These finite checks do not establish the asymptotic theorem; Steps 1--6 do.

## Relationship to prior work
Bevan and Threlfall (arXiv:2309.06287, first publicly posted 2023-09-12) systematically study pattern and gap-length thresholds for weak compositions and explicitly identify equal-length gaps/components as an untreated question. Their individual gap-length disappearance thresholds and no-gap scale do not directly provide the all-regimes pair-collision probability law or the intermediate persistence argument.

Klykova (2002/2003) proves a Poisson law for equal consecutive order-statistic spacings at the birthday scale for an iid discrete uniform sample. That earlier result has the same limiting constant as the *initial* window here, after a negligible-duplicates coupling; priority for this initial law is **not** asserted. The distinct contribution proposed here is the complete support-conditioned persistence theorem and the second, non-Poisson transition for the fixed-sum weak-composition model. Hitczenko and Louchard (2001) examine distinct part sizes under the different distribution of unrestricted-length positive compositions of one integer; that is not this fixed-number-of-positions, variable-mass gap problem.

## Limitations
The limits concern the *single-time* marginal law at each prescribed \(m=m(n)\). They do not construct a time-coupled growth process or claim monotonicity of the event as \(m\) changes; in fact its probabilities have two opposing transitions. The results do not extend automatically to multinomial allocations, dependent inputs or cyclic compositions. Klykova's original full text was not directly accessible; its published abstract gives the coincident-spacing Poisson theorem and materially limits claims of priority for the first window. Independent review and historical priority remain open.

## References
- D. Bevan and D. Threlfall, *On the evolution of random integer compositions*, arXiv:2309.06287 (first version 2023-09-12); Electronic Journal of Combinatorics 32(1), P1.21 (2025), doi:10.37236/13010. Open full text: https://pure.strath.ac.uk/ws/portalfiles/portal/265499486/Bevan-Threlfall-EJC-2025-On-the-evolution-of-random-integer.pdf
- N. V. Klykova, *Limit Distribution of a Number of Coinciding Intervals*, Theory of Probability and Its Applications 47(1), 151--156 (2003); Russian original 2002, doi:10.1137/S0040585X97979512. Abstract: https://epubs.siam.org/doi/10.1137/S0040585X97979512
- P. Hitczenko and G. Louchard, *Distinctness of compositions of an integer: A probabilistic analysis*, Random Structures & Algorithms 19 (2001), 407--437, doi:10.1002/rsa.10008. Abstract: https://onlinelibrary.wiley.com/doi/abs/10.1002/rsa.10008
