# Sharp path–star bounds for source–sink covariance in randomly oriented trees

## Finding
Let \(T=(V,E)\) be an undirected finite simple tree on \(n\ge 2\) vertices. Orient every edge independently and fairly. Write \(S\) for the number of vertices with indegree zero (sources), \(K\) for the number with outdegree zero (sinks), and \(d_v\) for the degree of vertex \(v\). Then
\[
\operatorname{Cov}(S,K)=2\sum_{uv\in E}2^{-d_u-d_v}-\sum_{v\in V}4^{-d_v}.
\]
For every such tree with \(n\ge3\), the sharp bounds are
\[
\boxed{\frac{n-1}{2^{n-1}}-\frac{n-1}{4}-4^{-(n-1)}\ \le\ \operatorname{Cov}(S,K)\ \le\ \frac{n-4}{16}.}
\]
For \(n\ge4\), equality on the left holds **only** for the star \(K_{1,n-1}\), and equality on the right holds **only** for the path \(P_n\), up to graph isomorphism. At \(n=3\) both shapes are the same tree and the covariance is \(-1/16\). At \(n=2\), both counts equal one and the covariance is zero.

There is therefore a sharp finite-order sign boundary: no tree with fewer than five vertices has positive source–sink covariance, whereas on every order \(n\ge5\) the path has positive covariance and the star has negative covariance. In particular, independent edge orientations do not impose a universal sign on the covariance of the *numbers* of sources and sinks.

## Assumptions and scope
All edges are undirected before independent, equiprobable orientations. A source has indegree zero; a sink has outdegree zero. There are no isolated vertices because \(T\) is connected and \(n\ge2\). The result concerns covariance between the **two counts**, not the covariance of reachability events or the deterministic maximum number of sources in a chosen orientation. All bounds are exact for each finite \(n\), without limiting assumptions. The graph need not be labeled, since the covariance is invariant under relabeling.

## Proof
**1. Local dependence identity.** Put \(q_v=2^{-d_v}\). For each vertex let \(A_v\) indicate indegree zero and \(B_v\) indicate outdegree zero. Each has expectation \(q_v\). Since \(d_v\ge1\), \(A_vB_v=0\), giving \(\operatorname{Cov}(A_v,B_v)=-q_v^2\). When distinct \(u,v\) are nonadjacent their incident edge sets are disjoint, so their indicators are independent. If \(uv\in E\), simultaneous occurrence of \(A_u=B_v=1\) forces the common edge from \(u\) to \(v\), and forces the other \(d_u+d_v-2\) incident edges. Thus
\[
\mathbb P(A_u=B_v=1)=2^{-(d_u+d_v-1)}=2q_uq_v,
\quad \operatorname{Cov}(A_u,B_v)=q_uq_v.
\]
The same holds after interchanging \(u,v\). Summing over all ordered pairs proves the first formula.

**2. Extremal values.** On \(P_n\), for \(n\ge3\), the two ends have degree one and the other \(n-2\) vertices have degree two. Substituting the \(n-1\) edge contributions and \(n\) diagonal terms into the first formula gives \((n-4)/16\). On \(K_{1,n-1}\), its center has degree \(n-1\) and all other vertices have degree one, giving
\[
\operatorname{Cov}(S,K)=\frac{n-1}{2^{n-1}}-\frac{n-1}{4}-4^{-(n-1)}.
\]
For \(n=2\), a direct orientation check gives zero.

**3. Star is the unique minimizer.** Suppose \(n\ge4\) and \(T\) is not a star. It has at most \(n-2\) leaves and maximum degree at most \(n-2\). Every nonleaf has \(4^{-d_v}\le 1/16\); hence
\[
\sum_vq_v^2\le \frac{n-2}{4}+\frac2{16}=\frac{n-1}{4}-\frac18.
\]
At least two different edges meet leaves, and for each such edge \(uv\) its positive contribution \(2q_uq_v\) is at least \(2^{-(n-2)}\). Consequently
\[
\operatorname{Cov}(S,K)\ge -\frac{n-1}{4}+\frac18+2^{3-n}.
\]
For every integer \(n\ge4\), \(2^{n-4}+4\ge n-1\), so \(1/8+2^{3-n}\ge(n-1)2^{-(n-1)}\). Because the star formula has the additional strictly negative term \(-4^{-(n-1)}\), the last bound is strictly larger than the star covariance. Thus no nonstar minimizes.

**4. Pendant-path transplantation strictly increases covariance.** Suppose \(T\) is not a path. Choose a degree-at-least-three vertex \(u\) with at least two incident branches containing no other degree-at-least-three vertex. Such a vertex exists: take an end vertex in the minimal subtree joining all branch vertices, or any branch vertex if it is the only one. The two selected branches are pendant paths from \(u\). Write \(v\) for the first vertex on one, \(t\) for the terminal leaf of the other, and \(p\) for the parent of \(t\) on its path from \(u\). Detach the edge \(uv\) and add \(tv\). The result \(T'\) is again a tree, on the same vertex set, with \(d_u\) decreased by one, \(d_t\) increased from one to two, and all other degrees unchanged.

Set \(q=2^{-d_u}\le1/8\), \(b=2^{-d_v}\in\{1/4,1/2\}\). If \(p\ne u\), necessarily \(d_p=2\). Writing \(Q=\sum_{x\sim u,\,x\ne v}2^{-d_x}\) with degrees in \(T\), a direct subtraction using the covariance formula yields
\[
\operatorname{Cov}_{T'}(S,K)-\operatorname{Cov}_{T}(S,K)
=\frac3{16}-3q^2+2qQ+b(\tfrac12-2q)-\frac18
\ \ge\ \frac5{64}>0.
\]
If \(p=u\), the edge \(ut\) has unchanged product \(q_uq_t\); put \(Q'=\sum_{x\sim u,\,x\notin\{v,t\}}2^{-d_x}\). Then
\[
\operatorname{Cov}_{T'}(S,K)-\operatorname{Cov}_{T}(S,K)
=\frac3{16}-3q^2+2qQ'+b(\tfrac12-2q)
\ \ge\ \frac{13}{64}>0.
\]
Both inequalities follow from \(q\le1/8\), \(b\ge1/4\), and nonnegativity of \(Q,Q'\). The branch-excess integer \(\sum_v\max\{d_v-2,0\}\) drops by exactly one at each transplant. Hence finitely many transplants reduce every nonpath tree to \(P_n\) while strictly increasing covariance. This proves the unique maximum.

Finally, \((n-4)/16\) is positive precisely when \(n\ge5\), and the star value is negative for \(n\ge3\) (or follows directly from its being the strict minimum and a small negative orientation calculation). The stated sign boundary follows.

## Verification
The accompanying `verify.py` uses exact fractions. It enumerates all \(2^{n-1}\) orientations of every unlabeled tree with \(2\le n\le9\), checks the indicator-derived covariance against the closed formula, checks the unique path and star bounds for every unlabeled tree with \(2\le n\le12\), and tests every ordered pair of available pendant paths in those trees for a strictly increasing transplantation. Its output includes `EXACT_ORIENTATION_COUNTS_PASS 94`, `STRICT_PENDANT_PATH_TRANSFERS_PASS 12002`, and `VERIFY_OK`. The infinite-family claims are proved in Section 4, not inferred from these finite checks. Run using `python verify.py` after installing `networkx`; no network access is used during verification.

## Relationship to prior work
Bienvenu's *Positive association of the oriented percolation cluster in randomly oriented graphs* (2017/2020) analyzes association of path-reachability indicators for a common source set; it does not compare the local source and sink **counts** across fixed tree shapes. Guo and He's *Tight bounds for popping algorithms* (2020), Section 5, uses individual sink events to analyze sampling sink-free orientations, not mixed source–sink covariance extrema. Ralaivaosaona's *The Number of Sources and Isolated Vertices in Random Directed Acyclic Graphs* (2022) investigates a random directed graph conditioned on acyclicity, with a random underlying edge set; it does not hold a tree fixed and uniformly orient its edges. Kozerenko and Dekhtiar's *Line digraphs of polytrees* (2025), Sections 3.2–3.3, calculates means and line-digraph components using sources and sinks of orientations, but does not supply the stated covariance and extremal inequalities. The local covariance formula may be rediscoverable by standard indicator methods; the assessed result is the *sharp path–star tree classification with strict transplant mechanism*, not the trivial fact that sources or sinks individually have expected value \(\sum_v2^{-d_v}\).

## Limitations
No claim is made for general graphs with cycles, for biased or dependent edge orientations, or for the full joint distribution of source and sink counts. This is a self-contained analytic proof supplemented by finite exact checks, not independent certification. Earlier work not returned by the recorded literature searches may already imply the extremal theorem; this is a residual priority risk.

## References
- F. Bienvenu, *Positive association of the oriented percolation cluster in randomly oriented graphs*, arXiv:1711.08815v1 (23 November 2017), published in Combinatorics, Probability and Computing 28 (2019), 811–815; https://arxiv.org/abs/1711.08815.
- H. Guo and K. He, *Tight bounds for popping algorithms*, Random Structures & Algorithms 57 (2020), 371–392; https://doi.org/10.1002/rsa.20928.
- D. Ralaivaosaona, *The Number of Sources and Isolated Vertices in Random Directed Acyclic Graphs*, AofA 2022, Article 17; https://doi.org/10.4230/LIPIcs.AofA.2022.17.
- S. Kozerenko and B.-Y. Dekhtiar, *Line digraphs of polytrees*, Utilitas Mathematica 124 (2025), 3–24; https://doi.org/10.61091/um124-01.
