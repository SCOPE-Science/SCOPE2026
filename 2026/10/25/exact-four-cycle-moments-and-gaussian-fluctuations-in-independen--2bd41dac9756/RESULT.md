# Exact four-cycle moments and Gaussian fluctuations in independently twisted hypercubes

## Finding

Let \(C_n\) count unoriented distinct simple cycles of length four in the independently twisted hypercube \(G_n\), a random simple graph with \(2^n\) vertices. For every integer \(k\ge2\), put \(m_k=2^{k-1}\), \(d_k=k-1\), and
\[
 a_k=\frac{m_kd_k^2}{2(m_k-1)},\qquad
 b_2=0,\qquad
 b_k=\frac{m_kd_k^2(m_k-k)^2}{2(m_k-3)(m_k-1)^2}\quad(k\ge3).
\]
For every \(n\ge2\), the **exact finite-size moments** are
\[
 \mathbb E C_n=\sum_{k=2}^n2^{n-k}a_k,\qquad
 \operatorname{Var}(C_n)=\sum_{k=3}^n2^{n-k}b_k.
\]
The convergent series
\[
 \lambda=\sum_{k=2}^\infty\frac{a_k}{2^k}
   =1.7748212947227267785\ldots,\qquad
 \sigma^2=\sum_{k=3}^\infty\frac{b_k}{2^k}
   =0.9405739688839245918\ldots>0
\]
give the laws
\[
 \frac{C_n}{2^n}\longrightarrow\lambda\quad\text{in }L^2,
 \qquad
 \frac{C_n-\mathbb E C_n}{2^{n/2}}
 \Longrightarrow\mathcal N(0,\sigma^2).
\]
The first convergence is also almost sure on **any** common probability space carrying these marginal distributions.

Writing \(A_n\) for the adjacency matrix, there is the exact identity
\[
 \operatorname{tr}(A_n^4)=2^n(2n^2-n)+8C_n.
\]
Consequently the centered fourth adjacency trace, divided by \(2^{n/2}\), converges to \(\mathcal N(0,64\sigma^2)\).

## Assumptions and scope

Construct \(G_0\) as an isolated vertex. For each \(n\ge1\), take **independent** instances \(H_0,H_1\) of \(G_{n-1}\), and join them by an independent uniformly distributed perfect matching between their two vertex sets. This gives a simple \(n\)-regular graph on \(2^n\) vertices. Every permutation at every node of the recursive construction is independent, and each edge is counted once. The theorem is for this independent-copy model, not the dependent-copy duplicube model. The Gaussian limit concerns the fixed four-cycle length while \(n\to\infty\).

## Proof

**1. Crossing cycle decomposition.** Every simple four-cycle in the union of \(H_0,H_1\) and their matching lies wholly in one child or crosses the cut twice. It cannot cross it four times because a vertex has only one incident matching edge. A twice-crossing four-cycle corresponds bijectively to a pair of child edges taken to one another by the matching permutation. Thus, for a uniform bijection \(\pi:V(H_0)\to V(H_1)\),
\[
 C_n=C_{n-1}^{(0)}+C_{n-1}^{(1)}+X_n,
 \quad X_n=\sum_{e\in E(H_0)}\mathbf1_{\{\pi(e)\in E(H_1)\}}.
\]
The children have \(m=2^{n-1}\) vertices and constant degree \(d=n-1\).

**2. The universal matching-overlap moments.** More generally, fix any two simple \(d\)-regular graphs on the same \(m\)-element vertex set, with \(m\ge4\). Let \(q=md/2\) be their number of edges, \(N=\binom m2\), and \(p=d/(m-1)\). For a fixed edge in the first graph, its image is a uniform two-subset, so \(\mathbb EX=qp\).

Among *ordered distinct* pairs of first-graph edges, precisely \(A=md(d-1)\) share one endpoint and \(D=q(q-1)-A\) are disjoint. Under a random permutation, their respective joint image-edge probabilities are
\[
 P_{\mathrm{adj}}=\frac{d(d-1)}{(m-1)(m-2)},\qquad
 P_{\mathrm{dis}}=\frac{D}{\binom m2\binom{m-2}2}.
\]
Indeed the denominator for the latter counts ordered disjoint pairs in the complete graph, and the favorable count in the second graph equals \(D\). Hence
\[
 \operatorname{Var}(X)
 =qp(1-p)+A(P_{\mathrm{adj}}-p^2)
       +D(P_{\mathrm{dis}}-p^2)
 =\frac{md^2(m-d-1)^2}{2(m-3)(m-1)^2}.
\]
This algebraic equality follows by substituting \(q,A,D,p\) and collecting rational terms. Crucially, **both conditional moments depend only on \(m,d\)**, not on either child graph's shape. At \(n=2\), the two children are single edges and the crossing-cycle count is deterministically one; this is the exceptional formula \(b_2=0\).

**3. Exact total moments.** Conditional on both children, \(\mathbb E(X_n\mid H_0,H_1)=a_n\) and \(\operatorname{Var}(X_n\mid H_0,H_1)=b_n\). The two children are independent, and the conditional mean is constant, so \(X_n\) is uncorrelated with the children’s cycle counts. Therefore
\[
 \mathbb E C_n=2\mathbb EC_{n-1}+a_n,\qquad
 \operatorname{Var}(C_n)=2\operatorname{Var}(C_{n-1})+b_n.
\]
Since \(C_1=0\), these recursions give the asserted sums including \(C_2=1\).

**4. Gaussian limit with negligible upper-level contribution.** Fix any \(L\ge3\). The \(2^{n-L}\) subgraphs at recursive level \(L\) are independent copies of \(G_L\). Write \(C_n-\mathbb EC_n\) as their centered four-cycle sum plus \(R_{n,L}\), the sum of centered crossing contributions \(X_k-a_k\) at levels \(k>L\). Distinct centered crossing contributions are orthogonal: when the respective recursive nodes are disjoint they are independent, and when nested, conditioning on the two children of the higher node gives zero conditional mean against all descendant randomness. Thus
\[
 \frac{\mathbb ER_{n,L}^2}{2^n}
 =\sum_{k=L+1}^{n}\frac{b_k}{2^k}
 \le\sum_{k>L}\frac{b_k}{2^k}.
\]
Because \(b_k=O(k^2)\), this bound tends to zero as \(L\to\infty\) uniformly in \(n\ge L\). For fixed \(L\), the ordinary i.i.d. central limit theorem gives
\[
 \frac{\sum_{j=1}^{2^{n-L}}(C_L^{(j)}-\mathbb EC_L)}{2^{n/2}}
 \Longrightarrow\mathcal N\left(0,\frac{\operatorname{Var}(C_L)}{2^L}\right).
\]
The limiting variances tend to \(\sigma^2\) as \(L\to\infty\). The uniform \(L^2\) remainder bound and a bounded-Lipschitz (or characteristic-function) approximation establish the stated Gaussian limit. The exact mean and variance imply \(\mathbb E C_n/2^n\to\lambda\) and \(\operatorname{Var}(C_n/2^n)=O(2^{-n})\), so \(L^2\) convergence follows. Since the tail probabilities of any fixed deviation are summable, Borel–Cantelli also gives almost sure convergence without requiring independence across values of \(n\).

**5. Spectral correspondence.** For any finite simple \(n\)-regular graph on \(N\) vertices, closed walks of length four that contain no simple four-cycle contribute exactly \(N(2n^2-n)\); each distinct simple four-cycle contributes eight oriented rooted closed walks. This proves \(\operatorname{tr}(A_n^4)=2^n(2n^2-n)+8C_n\) and its fluctuation corollary.

## Verification

The accompanying standalone standard-library Python program `verify_four_cycles.py` enumerates all \(24\) matchings in the level-three construction and all \(4\cdot8!=161{,}280\) matchings across the four possible pairs of representative level-three graph types. It recomputes edge-overlap moments with **exact rational arithmetic**, directly counts simple four-cycles in 140 further sampled recursive constructions, and checks boundary constants. It reports \(a_3=8/3\), \(b_3=8/9\), \(a_4=36/7\), \(b_4=576/245\). Run `python verify_four_cycles.py` with Python 3; no packages or external data are required. The infinite-dimensional convergence claims are proved above, not inferred from these finite tests.

## Relationship to prior work

Dudek and collaborators introduced and studied the independent-copy model, proving diameter and routing properties [3]. Benjamini and collaborators proved a semicircle law and gave bounds on short cycles; their Remark 18 notes a guaranteed linear number of four-cycles and separately discusses the *duplicube* [2]. Baran and Šarković study random-walk mixing, cover time and chromatic number of the independent model [1]. The present exact nonasymptotic cycle mean and variance, concentration, Gaussian fluctuation and centered fourth-trace limit do not follow from those stated geometric, mixing or weak spectral-law conclusions: weak semicircle convergence does not determine the order-one density of four-cycles or centered fluctuations of the unnormalized fourth trace.

## Limitations

The conclusions require independent child copies and independently uniform matchings at all levels; the proof does not transfer automatically to duplicubes or other dependent-copy constructions. It treats only simple cycles of length four and the corresponding fourth adjacency trace, not all cycle lengths or the full spectral fluctuation field. The normal limit is asymptotic, and finite verification does not establish it by itself. Priority against every possible broader subgraph-count theorem has not been independently certified.

## References

[1] Baran and Šarković, *Mixing time of the lazy and simple random walk on a randomly twisted hypercube*, arXiv:2610.21976v1, https://arxiv.org/html/2610.21976v1 (first posted 15 October 2026).

[2] Benjamini, Dikstein, Gross and Zhukovskii, *Randomly twisted hypercubes — between structure and randomness*, arXiv:2211.06988v3, https://arxiv.org/html/2211.06988v3.

[3] Dudek, Pérez-Giménez, Prałat, Qi, West and Zhu, *Randomly twisted hypercubes*, European Journal of Combinatorics **70** (2018), 364–373, https://doi.org/10.1016/j.ejc.2018.01.013.
