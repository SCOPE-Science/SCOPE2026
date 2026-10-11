# Exact rank-stratified vertex degrees of rectangular matching polytopes

## Finding
For all integers \(a,b\ge1\), let \(Q_{a,b}\) be the convex hull in \(\mathbb R^{a\times b}\) of all \(0\)-\(1\) matrices with at most one \(1\) per row and column. Equivalently, it is the matching polytope of \(K_{a,b}\) or the rectangular doubly substochastic matrix polytope. Fix a vertex representing a matching of size \(k\), where \(0\le k\le\min(a,b)\). Define
\[
\alpha_k=\sum_{t=1}^k\frac{k!}{(k-t)!},\qquad
\beta_k=\sum_{t=2}^k\binom kt(t-1)!,\qquad
p=a-k,\quad q=b-k.
\]
Empty sums are zero. The number of edges of the one-skeleton incident to this vertex is **exactly**
\[
\boxed{d_{a,b}(k)=pq+(p+1)(q+1)\alpha_k+\beta_k.}
\]
Exactly \(\binom ak\binom bk k!\) vertices have this degree before merging coincident degree values. If \(\min(a,b)\ge2\), the sequence \(d_{a,b}(0),\ldots,d_{a,b}(\min(a,b))\) is strictly increasing, **except** that \(d_{2,2}(1)=d_{2,2}(2)=5\), while \(d_{2,2}(0)=4\). If \(\min(a,b)=1\), all vertex degrees equal \(\max(a,b)\). Thus this gives the complete degree multiset, all exceptional equalities, and the full rank-to-local-degree order. In particular the total number of one-skeleton edges is
\[
\frac12\sum_{k=0}^{\min(a,b)}\binom ak\binom bk k!\,d_{a,b}(k).
\]

## Assumptions and scope
All dimensions and parameters are finite positive integers. Adjacency refers to ordinary polytope edges (one-dimensional faces), not adjacency of nonzero matrix entries, the combinatorial matching complex, or the shortest-path graph distance. The natural affine hull of \(Q_{a,b}\) is full-dimensional in \(\mathbb R^{ab}\): the origin and the \(ab\) unit coordinate matrices belong to it. Every vertex is an incidence matrix of a partial matching, by the total unimodularity of the bipartite incidence constraint system. Conversely each such \(0\)-\(1\) point is extreme because it uniquely maximizes the linear form which rewards its own \(1\) entries and penalizes all other entries.

## Proof
**1. Edges and alternating components.** The classical edge characterization for matching polytopes states that two distinct matching-incidence vertices are adjacent exactly when the symmetric difference of the matchings is one connected alternating path or one alternating even cycle. This is an established theorem, not asserted as new. Given a fixed rank-\(k\) matching, label its matched edges by \(1,\ldots,k\). There are \(p\) unmatched left vertices and \(q\) unmatched right vertices. All alternations inside \(K_{a,b}\) between distinct matched pairs are possible. The path/cycle characterization yields four disjoint classes, indexed by their endpoints or by being a cycle.

A path with both endpoint edges in the old matching uses \(t\ge1\) old matched edges and \(t-1\) new edges. An ordered list of \(t\) distinct old pairs uniquely specifies the path; these contribute \(\sum_{t=1}^k(k)_t=\alpha_k\), where \((k)_t=k!/(k-t)!\).

A path whose endpoints are unmatched left and unmatched right vertices uses \(t\ge0\) old edges and \(t+1\) new ones. Choosing its endpoints and an ordered list of old pairs gives \(pq\sum_{t=0}^k(k)_t=pq(1+\alpha_k)\).

A path with exactly one unmatched endpoint and the other endpoint on a matched edge has equal numbers of old and new edges; it consists of \(t\ge1\) ordered old pairs, together with a choice of one unmatched endpoint on either side. There are \((p+q)\alpha_k\) such paths.

An alternating cycle uses \(t\ge2\) matched edges and \(t\) new edges. Choosing its \(t\) matched edges and a cyclic order gives \(\binom kt(t-1)!\) cycles; summing gives \(\beta_k\). Distinct components produce distinct neighboring matchings, and every permissible symmetric difference occurs in exactly one class. Therefore
\[
d_{a,b}(k)=\alpha_k+pq(1+\alpha_k)+(p+q)\alpha_k+\beta_k
=pq+(p+1)(q+1)\alpha_k+\beta_k.
\]
There are \(\binom ak\) choices of occupied left vertices, \(\binom bk\) choices of occupied right vertices, and \(k!\) bijections, proving the multiplicities. Summing degrees and dividing by two gives the edge-count identity.

**2. Strict ranking and all exceptions.** The elementary recurrence
\[
\alpha_{k+1}=(k+1)(\alpha_k+1)
\]
gives, for \(k<\min(a,b)\) and \(p=a-k\ge1,q=b-k\ge1\),
\[
\Delta_k:=d_{a,b}(k+1)-d_{a,b}(k)
=pqk+(p-1)(q-1)
 +(pqk-p-q-1)\alpha_k+(\beta_{k+1}-\beta_k).
\]
Every \(\beta_{k+1}-\beta_k\) is nonnegative, and it is positive for \(k\ge1\). For \(k=0\), direct substitution yields \(\Delta_0=(a-1)(b-1)\). If \(k\ge2\), then \(pqk-p-q-1\ge0\) unless \(p=q=1,k=2\). In that sole exceptional sign case, \(\alpha_2=4\), \(\beta_3-\beta_2=4\), and the displayed difference equals \(2-4+4=2>0\). Thus \(\Delta_k>0\) for \(k\ge2\).

If \(k=1\), the potentially negative coefficient equals \((p-1)(q-1)-2\). If \(p=1\), then \(\Delta_1=q-1\); symmetrically if \(q=1\), then \(\Delta_1=p-1\). Hence equality occurs there only for \(p=q=1\), i.e. \(a=b=2\). If \(p=q=2\), direct substitution gives \(\Delta_1=5\). For all remaining \(p,q\ge2\), the coefficient is nonnegative and the positive leading term forces \(\Delta_1>0\). Finally when \(\min(a,b)=1\), the \(ab\)-dimensional polytope is a simplex with \(\max(a,b)+1\) vertices, each of degree \(\max(a,b)\). These cases exhaust every parameter range and prove the claimed strict rank order and exceptions.

## Verification
The standalone file `verify.py` enumerates every matching and every neighboring pair independently of the four-class formula for ten dimensions \((a,b)\), up to \((4,5)\). It checks all degrees and rank multiplicities of **1,011 actual vertices**, using the connected-alternating-symmetric-difference criterion. It additionally checks the claimed strict inequalities and exceptions by exact integer arithmetic for all \(1\le a\le b\le40\). Run `python3 verify.py`; its final line is `VERIFY_OK vertex_count 1011 integer_pairs 820`. The code cannot establish the infinite theorem; the argument above covers all integer parameters.

## Relationship to prior work
The matching-polytope alternating path/cycle adjacency criterion is classical. Abreu, Costa, Nascimento, and Patuzzi (2019, Theorems 2 and 4) formulate this criterion and a general degree count through good alternating paths/cycles; they already prove nondecreasing degree under matching inclusion (Theorem 6), which by the symmetries of complete bipartite graphs implies nondecreasing degree by rank; they also identify the minimum possible local degree. Merino and Mütze (arXiv first posted 2023, journal 2024, primary MSC 52B05) investigate matching-polytope skeletons in the context of Hamilton paths and Gray-code traversal. Neither of their inspected statements gives the exact two-parameter degree multiset or its strict order by matching size. The present result is the explicit bivariate rank-profile evaluation, strictness and complete equality-case classification; it does not claim novelty for adjacency, weak rank monotonicity, or the general minimum-degree bound. Cao and Chen (2022) describe faces, including one-dimensional faces, of the square doubly substochastic matrix polytope. Its full article was not available during this comparison, so it remains a relevant residual priority for literature verification.

## Limitations
The formula requires the complete bipartite graph; graph edge deletion generally changes the admissible alternating paths, so this is not a degree formula for arbitrary matching polytopes. All asserted ranks and exceptional equalities are covered by the proof. This report does not claim originality of the known matching adjacency criterion. The known general inclusion-monotonicity theorem already gives the non-strict ordering. The inaccessible square-polytope face article may contain equivalent special cases; absence of a database match is not proof of novelty. Independent validation has not been performed.

## References
- A. Merino and T. Mütze, *Traversing combinatorial 0/1-polytopes via optimization*, arXiv:2304.08567 (first public version 17 April 2023), *SIAM Journal on Computing* **53** (2024), 1257–1292, DOI:10.1137/23M1612019. Journal primary MSC 52B05.
- N. M. M. Abreu, L. M. G. C. Costa, C. H. P. Nascimento, and L. Patuzzi, *A Note on the Matching Polytope of a Graph*, *TEMA* **20** (2019), 189–196, DOI:10.5540/tema.2019.020.01.0189.
- L. Cao and Z. Chen, *Faces of the polytope of doubly substochastic matrices*, *Linear Algebra and its Applications* **637** (2022), 59–81, DOI:10.1016/j.laa.2021.11.012. Only bibliographic metadata and abstract were accessible for this comparison.
