# Conditional terminal-point laws and second-order dependence in uniform random mappings

## Finding

For every integer \(n\ge 2\), let \(F_n:[n]\to[n]\) be selected uniformly from the \(n^n\) functions. Write \(C_n\) for the number of *cyclic points* (vertices lying on directed cycles of the functional digraph) and \(Z_n\) for the number of *terminal points* (vertices with no preimages under \(F_n\)). For any integer \(1\le k<n\), set \(s=n-k\). Then for every integer \(0\le r\le s\),

\[
\mathbb E[(Z_n)_{\underline r}\mid C_n=k]
=(s)_{\underline r}\left(1-\frac r n\right)^{s-1}.
\]

Here \((u)_{\underline r}=u(u-1)\cdots(u-r+1)\), with \((u)_{\underline 0}=1\). For \(k=n\), \(Z_n=0\) identically. In particular, the entire conditional law is specified by its finite factorial moments, and

\[
g_n(k):=\mathbb E[Z_n\mid C_n=k]
= (n-k)\left(1-\frac1n\right)^{n-k-1}\quad(1\le k<n),
\qquad g_n(n)=0.
\]

The conditional regression \(g_n(k)\) is strictly decreasing in \(k=1,\ldots,n\). Consequently,

\[
\operatorname{Cov}(C_n,Z_n)<0\quad\text{for every }n\ge2.
\]

There is also an exact finite-size identity. Put
\(b_j=\sum_{\ell=1}^{j}(j)_{\underline\ell}/j^\ell\) for \(j\ge1\). Then

\[
\operatorname{Cov}(C_n,Z_n)
=n\left(1-\frac1n\right)^n(b_{n-1}-b_n).
\]

Let \(R\) have the Rayleigh density \(x\exp(-x^2/2)\) on \(x>0\). The conditional mean has a second-order, rather than first-order, response: for every fixed \(x\ge0\) and every integer sequence \(k_n\ge1\) with \(k_n/\sqrt n\to x\),

\[
\mathbb E[Z_n\mid C_n=k_n]
-\frac ne\longrightarrow\frac{1-x^2}{2e}.
\]

The typical cyclic-point count is of order \(\sqrt n\), yet its effect on the terminal-point mean is only of order one. The mixed covariance and correlation have sharp nonzero constants:

\[
\frac{\operatorname{Cov}(C_n,Z_n)}{\sqrt n}
\longrightarrow-\frac{\sqrt{\pi/2}}{2e},
\qquad
\sqrt n\,\operatorname{Corr}(C_n,Z_n)
\longrightarrow-
\frac{\sqrt{\pi/2}}{
2e\sqrt{(2-\pi/2)(e^{-1}-2e^{-2})}}.
\]

The first limit is about \(-0.2305342522\), and the coefficient in the correlation limit is about \(-1.1286279159\).

## Assumptions and scope

Each of the \(n\) images \(F_n(i)\) is independently uniform on \([n]\); self-loops are permitted. A cyclic point is periodic under iteration, whereas a terminal point has indegree zero. This latter definition must not be confused with a *terminal closer* in the literature on multiset permutations. A cyclic point cannot be terminal, because it has a predecessor on its directed cycle, possibly itself. The conditional formulas include every feasible \(k\) and \(r\); the identity for \(k=n\) is handled separately. No nonuniform mapping or fixed-degree model is claimed.

## Proof

**1. Conditional forest representation.** Fix a set \(S\subseteq[n]\) of \(k\) cyclic vertices. Restricting a mapping with cyclic set \(S\) to \(S\) gives a permutation of \(S\). Deleting its \(k\) outgoing cycle edges leaves a directed forest in which all \(n-k\) other vertices point towards roots in \(S\). Conversely, each permutation and such a rooted forest reconstruct one mapping. The two choices are independent and uniform conditional on \(S\); this classical decomposition is explicit in Pitman's conditional-forest formulas. When \(s=n-k\ge1\), there are exactly \(k n^{s-1}\) labeled directed rooted forests with prescribed roots \(S\). To see this independently, the directed matrix-tree determinant for the complete available parent graph, on the \(s\) nonroots, is \(\det(nI_s-J_s)=k n^{s-1}\), since its eigenvalues are \(k\) once and \(n\) with multiplicity \(s-1\). The case \(s=0\) has one empty forest. Hence

\[
\Pr\{C_n=k\}
=\binom nk k!\,k n^{n-k-1}/n^n
=\frac{k(n)_{\underline k}}{n^{k+1}},\qquad1\le k\le n,
\]

where the final expression is also valid at \(k=n\) by the empty-forest convention.

**2. Joint terminal events and conditional law.** All terminal vertices belong to the \(s\) nonroots. Fix a set \(A\) of \(r\) particular nonroots. The condition that every vertex in \(A\) is terminal says no forest edge points into \(A\). Deleting the \(r\) terminal vertices leaves a rooted forest on the remaining \(n-r\) vertices with the same roots, and each deleted vertex independently chooses its parent among these \(n-r\) vertices. The resulting number of forests is

\[
(n-r)^r\,k(n-r)^{s-r-1}=k(n-r)^{s-1},
\]

including the endpoint \(r=s\), for which the remaining forest is empty and there are \(k^s\) attachments. Division by \(k n^{s-1}\) shows

\[
\Pr\{A\subseteq\text{terminal points}\mid C_n=k\}
=\left(\frac{n-r}{n}\right)^{s-1}.
\]

Summing over the \((s)_{\underline r}\) ordered choices of terminal vertices establishes the factorial-moment formula. The collection for all \(r\le s\) determines the conditional distribution, or equivalently its probability generating polynomial. For example, for \(0\le j\le s\),

\[
\Pr\{Z_n=j\mid C_n=k\}
=\binom sj\sum_{t=0}^{s-j}(-1)^t\binom{s-j}{t}
\left(\frac{n-j-t}{n}\right)^{s-1}.
\]

**3. Strict regression and covariance sign.** Let \(a=1-1/n\). The conditional mean at \(s\ge1\) nonroots is \(f(s)=s a^{s-1}\), while \(f(0)=0\). For \(1\le s\le n-2\), \(f(s+1)>f(s)\), because \((s+1)a>s\) is equivalent to \(s<n-1\); and \(f(1)>f(0)=0\). There is no larger feasible \(s\) than \(n-1\), since \(k\ge1\). Thus \(g_n(k)\) decreases strictly as \(k\) increases. Using an independent copy \(C_n'\) and strict positivity of each feasible \(\Pr(C_n=k)\),

\[
2\operatorname{Cov}(C_n,g_n(C_n))
=\mathbb E[(C_n-C_n')(g_n(C_n)-g_n(C_n'))]<0.
\]

The tower property gives \(\operatorname{Cov}(C_n,Z_n)=\operatorname{Cov}(C_n,g_n(C_n))\).

**4. Exact mixed covariance by deleting a terminal point.** Fix \(v\in[n]\). On the event that \(v\) has no preimage, all other \(n-1\) images are independent uniform choices from \([n]\setminus\{v\}\). Their induced mapping is a uniform map on \(n-1\) vertices, while \(v\) cannot be cyclic. Therefore \(\mathbb E[C_n\mid v\text{ terminal}]=\mathbb E[C_{n-1}]=b_{n-1}\). The probability that \(v\) is terminal is \(a^n\), and \(\mathbb E C_n=b_n\) follows from the exact cycle-point law or summing expected directed cycle indicators. Sum \(\operatorname{Cov}(C_n,1_{\{v\text{ terminal}\}})\) over vertices to obtain the stated finite covariance formula.

**5. Second-order shift and covariance limit.** The cycle-point probability is

\[
\Pr(C_n=k)=\frac{k}{n}\prod_{j=0}^{k-1}\left(1-\frac jn\right).
\]

It follows by Riemann sums that \(C_n/\sqrt n\Rightarrow R\), and the bound \(\prod_{j=0}^{k-1}(1-j/n)\le \exp[-k(k-1)/(2n)]\) supplies Gaussian tails and convergence of all fixed positive moments. For \(k=O(\sqrt n)\), expand

\[
\log\!\left[\frac{e}{n}(n-k)a^{n-k-1}\right]
=\frac{1}{2n}-\frac{k^2}{2n^2}
+O\!\left(\frac{k+1}{n^2}+\frac{k^3}{n^3}\right).
\]

Hence \(g_n(k)=n/e+(1-k^2/n)/(2e)+o(1)\) when \(k/\sqrt n\) is bounded. The estimate is uniform for \(k\le n^{3/5}\), with its error after multiplication by \(n\) tending to zero. The complementary event has exponentially small probability by the Gaussian bound and contributes negligibly to the needed moments because \(0\le g_n(k)\le n\). Consequently the pair \((C_n/\sqrt n,\,g_n(C_n)-n/e)\) converges in moments sufficient to take covariance to \((R,(1-R^2)/(2e))\). Since \(\mathbb E R=\sqrt{\pi/2}\), \(\mathbb E R^2=2\), and \(\mathbb E R^3=3\sqrt{\pi/2}\),

\[
\frac{\operatorname{Cov}(C_n,Z_n)}{\sqrt n}
\longrightarrow
\operatorname{Cov}\!\left(R,\frac{1-R^2}{2e}\right)
=-\frac{\sqrt{\pi/2}}{2e}.
\]

**6. Correlation limit.** Rayleigh moment convergence gives \(\operatorname{Var}(C_n)/n\to2-\pi/2\). Since \(Z_n\) is the occupancy count of empty target bins in \(n\) independent uniform throws into \(n\) bins,

\[
\operatorname{Var}(Z_n)
=n a^n(1-a^n)+n(n-1)\left[(1-2/n)^n-a^{2n}\right].
\]

A first-order expansion shows \(\operatorname{Var}(Z_n)/n\to e^{-1}-2e^{-2}>0\). Dividing the covariance asymptotic by the standard deviations proves the asserted correlation limit.

## Verification

The accompanying standalone `verify.py` exhaustively enumerates all \(n^n\) labeled mappings for \(2\le n\le7\), with exact rational calculations of every admissible conditional factorial moment, the complete cyclic-point marginal, the covariance identity, and strict covariance negativity. For larger \(n\), its floating-point diagnostics compare covariance and correlation scaling with the analytically derived constants. Execute with `python3 verify.py` (standard library only). The exhaustive checks cover these small sizes only; the unrestricted statements follow from the counting and limiting arguments above.

## Relationship to prior work

Pitman (2001) gives the conditional uniform forest/permutation decomposition and the underlying forest enumerator; both are treated here as established background, not new results. Flajolet and Odlyzko (1990) analyze expected cyclic and terminal counts separately. Hansen and Jaworski (2010) analyze components conditional on the cyclic set size; Mutafchiev and Finch (2023) analyze the deepest random-mapping cycle. Drmota (1995) studies correlations between *distance-to-cycle strata*, which are not the indegree-zero vertices studied here. Buchanan and collaborators (2026) analyze *terminal closers*, a different statistic. The specific combined contribution assessed here is the conditional leaf factorial-moment law together with strict finite negative dependence, the order-one conditional regression at \(\sqrt n\) cyclic points, and sharp mixed covariance/correlation constants. Classical general forest enumeration makes related deductions possible, and priority of an equivalent specialized result has not been independently established.

## Limitations

The findings concern only uniform functions \([n]\to[n]\) and count indegree-zero vertices, not distance-to-cycle strata. The limit does not assert asymptotic independence. The conditional factorial-moment identity can be derived from the earlier general forest enumerator; novelty is assessed for the resulting mixed law and the cancellation/asymptotic dependence rather than for the enumerator itself. Historical-priority uncertainty remains, especially for specialized literature on random-forest leaves and random mappings. No independent scientific audit has been performed.

## References

1. L. Mutafchiev and S. Finch, *On the Deepest Cycle of a Random Mapping*, arXiv:2301.13829, first posted 2023-01-31; primary MSC2020 60C05. https://arxiv.org/abs/2301.13829
2. J. Pitman, *Random mappings, forests, and subsets associated with Abel-Cayley-Hurwitz multinomial expansions*, Statistics Department Technical Report 593, 2001. https://statistics.berkeley.edu/sites/default/files/tech-reports/593.pdf
3. P. Flajolet and A. M. Odlyzko, *Random Mapping Statistics*, Advances in Cryptology—EUROCRYPT '89, LNCS 434 (1990), DOI:10.1007/3-540-46885-4_34.
4. J. C. Hansen and J. Jaworski, *Random Mappings with a Given Number of Cyclical Points*, Ars Combinatoria 94 (2010), 341–359. https://combinatorialpress.com/article/ars/Volume%20094/volume-94-paper-34.pdf
5. M. Drmota, *Correlations on the strata of a random mapping*, Random Structures & Algorithms 6 (1995), 357–365, DOI:10.1002/rsa.3240060223.
6. T. Mylläri, *Limit distributions for the number of leaves in a random forest*, Advances in Applied Probability 34 (2002), 904–922, DOI:10.1239/aap/1037990959 (abstract reviewed; complete text not inspected).
7. C. Buchanan, F. Burghart, S. Wagner and M. Yin, *On Cycles in Multiset Permutations, Parking Functions, and Related Structures*, AofA 2026, DOI:10.4230/LIPIcs.AofA.2026.16.
