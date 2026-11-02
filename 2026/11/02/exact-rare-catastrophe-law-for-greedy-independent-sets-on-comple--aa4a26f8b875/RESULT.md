# Exact rare-catastrophe law for greedy independent sets on complements of four-cycle-free bipartite graphs

## Finding
Let \(H=(U\sqcup V,E_H)\) be a finite simple \(d\)-regular bipartite graph with \(|U|=|V|=n\), no four-cycle, and integers \(d\ge 1\), \(n\ge d+2\). Form \(G=K_{n,n}\setminus E_H\), retaining the same vertex classes, and inspect all \(2n\) vertices in a uniform random order. Accept a vertex if it has no previously accepted neighbor in \(G\). Write \(I\) for the final maximal independent set and \(X=|I|\), and define
\[
 p_{n,d}=\frac{dn}{(n+d-1)(n-d+1)}.
\]
Then the **complete cardinality law** is
\[
\Pr(X=n)=1-p_{n,d},\qquad \Pr(X=d+1)=p_{n,d}.
\]
Moreover \(\Pr(I=U)=\Pr(I=V)=(1-p_{n,d})/2\). If \(d\ge2\), the other \(2n\) possible outputs are the distinct sets \(\{w\}\cup N_H(w)\) as \(w\) ranges over \(U\sqcup V\), each with probability
\[
\Pr(I=\{w\}\cup N_H(w))=\frac{p_{n,d}}{2n}=\frac{d}{2(n+d-1)(n-d+1)}.
\]
For \(d=1\), the \(n\) deleted matching edges are precisely the mixed outputs, each with probability \(1/n^2\). Therefore, for every integer \(r\ge1\),
\[
\mathbb E(n-X)^r=(n-d-1)^r p_{n,d},
\]
and in particular
\[
\mathbb EX=n-(n-d-1)p_{n,d},\quad
\operatorname{Var}(X)=(n-d-1)^2p_{n,d}(1-p_{n,d}).
\]

There is also a **sharp variance-order consequence across the whole family**. For any admissible sequence with \(n\to\infty\), allowing \(d=d_n\) to vary,
\[
 p_{n,d}\sim d/n,\qquad n-\mathbb EX\sim d,\qquad
 \operatorname{Var}(X)\sim dn,
\]
with multiplicative errors uniform across admissible \(d\). In particular
\[
 \limsup_{n\to\infty}\frac{\operatorname{Var}(X)}{n^{3/2}}\le1.
\]
The constant one is attainable along incidence graphs of finite projective planes of prime-power order: for plane order \(q\), take \(n=q^2+q+1\), \(d=q+1\); then \(\operatorname{Var}(X)/n^{3/2}\to1\).

## Assumptions and scope
A four-cycle in \(H\) means a subgraph on two vertices of each class containing all four cross-edges. No connectedness or vertex-transitivity is assumed for \(H\). The graph \(G\) is the **bipartite cross-edge complement** of \(H\), not the ordinary graph complement: it contains all cross-edges absent from \(H\), and no edges within either vertex class. The random order is uniform over all permutations of the \(2n\) vertices; equivalently, vertices have independent continuous priorities. The graph \(H\) is held fixed when the order is sampled. The restriction \(n\ge d+2\) makes the two possible cardinalities distinct. All finite formulas are exact for each admissible graph, not averages over graphs.

## Proof
**1. Support classification.** If \(I\) intersects both vertex classes, its intersections \(A=I\cap U\) and \(B=I\cap V\) form a complete bipartite subgraph of \(H\), because every pair across \(A\) and \(B\) must be a nonedge of \(G\). If both \(|A|\) and \(|B|\) were at least two, \(H\) would contain a four-cycle. Thus one side of a mixed independent set is a singleton, say \(B=\{v\}\). Maximality then forces \(A=N_H(v)\): every missing neighbor of \(v\) could otherwise be added, while every other vertex of \(U\) is adjacent to \(v\) in \(G\). Every other vertex of \(V\) is blocked by at least one vertex of \(N_H(v)\), because if a distinct \(v'\) were adjacent in \(H\) to all \(d\) vertices of \(N_H(v)\) with \(d\ge2\), the pair \(v,v'\) would form a four-cycle with two of them. Hence all these sets are maximal for \(d\ge2\). When \(d=1\), a deleted matching pair is maximal because each endpoint has no other missing cross-neighbor. A purely one-sided maximal independent set is necessarily the full class \(U\) or \(V\), since \(d<n\). Thus every outcome is either a full class (size \(n\)) or a centered star in \(H\) (size \(d+1\)). For \(d\ge2\), the centered stars are distinct; at \(d=1\), each matched pair is represented by its two endpoints.

**2. The probability of a mixed outcome.** By symmetry of the two class sizes and degrees, condition on the first accepted vertex being \(u\in U\). Among vertices that can be accepted next are the remaining \(n-1\) vertices of \(U\) and the \(d\) neighbors \(N_H(u)\) in \(V\). All other vertices of \(V\) are rejected because they are adjacent to \(u\) in \(G\). Conditional on the first vertex, the earliest eligible vertex is uniform among these \(n+d-1\) vertices (rejected vertices do not alter that relative ordering).

If this second accepted vertex lies in \(V\), which has probability \(d/(n+d-1)\), the output is necessarily mixed. Otherwise it is a different \(u'\in U\). For the final output to be mixed, \(u,u'\) must have a common neighbor \(v\in V\) in \(H\). The four-cycle-free condition makes such \(v\) unique, and as \(u'\) varies there are exactly \(d(d-1)\) qualifying choices: each of the \(d\) neighbors \(v\) of \(u\) has \(d-1\) other neighbors in \(U\), with no repetition. Following two accepted \(U\)-vertices that share \(v\), \(v\) is the only eligible opposite-class vertex. It is ultimately accepted precisely when its priority precedes the earliest priority of the \(n-d\) vertices of \(U\setminus N_H(v)\). Arrivals from the other \(d-2\) vertices of \(N_H(v)\) do not change this condition. By exchangeability, the chance is \(1/(n-d+1)\). In every other case the final set is purely \(U\). Consequently
\[
\Pr(I\text{ mixed}\mid\text{first vertex in }U)
 =\frac{d}{n+d-1}+\frac{d(d-1)}{(n+d-1)(n-d+1)}
 =\frac{dn}{(n+d-1)(n-d+1)}.
\]
The corresponding computation conditional on first vertex in \(V\) is identical, proving the claimed \(p_{n,d}\) and the two equal pure-output masses.

**3. Exact probabilities of individual mixed sets.** Fix \(v\in V\) and \(d\ge2\). To output \(\{v\}\cup N_H(v)\), only the following first-accepted-vertex scenarios are possible. First, \(v\) may appear first and an eligible \(u\in N_H(v)\) next; after this, among the \(d-1\) remaining eligible \(U\)-vertices and the \(d-1\) eligible \(V\)-vertices, the former must win the next race, of probability \(1/2\). Second, some \(u\in N_H(v)\) may appear first and \(v\) next, with the same last-race probability \(1/2\). Third, some \(u\in N_H(v)\) may appear first, some different \(u'\in N_H(v)\) next, and then \(v\) may precede all \(n-d\) outside \(U\)-vertices. The respective probabilities are
\[
 \frac{d}{4n(n+d-1)},\qquad
 \frac{d}{4n(n+d-1)},\qquad
 \frac{d(d-1)}{2n(n+d-1)(n-d+1)}.
\]
Their sum is \(d/[2(n+d-1)(n-d+1)]\), independent of the choice of \(v\) or of the global incidence geometry. The calculation for a fixed center in \(U\) is identical. When \(d=1\), after the first endpoint of a missing edge, the other endpoint is accepted before the other \(n-1\) vertices of that first side with probability \(1/n\); summing the two possible first endpoints gives \(\Pr(I=\{u,v\})=1/n^2\) for each deleted edge. This proves the full output-set law.

**4. Moments, degree restriction, and sharpness.** The two-point cardinality law gives the stated moments directly. Fix \(u\in U\). The \(d\) vertices in \(N_H(u)\) each have \(d-1\) further neighbors in \(U\); no two can share one, because that would produce a four-cycle together with \(u\). Hence
\[
 n\ge1+d(d-1),\qquad d\le\frac{1+\sqrt{4n-3}}2=O(\sqrt n).
\]
Uniformly for these degrees, \(d/n\to0\) and the exact probability satisfies \(p_{n,d}=(d/n)(1+o(1))\), so the exact moment identities imply the asymptotics and \(\operatorname{Var}(X)\le(1+o(1))n^{3/2}\). The point-line incidence graph of a projective plane of prime-power order \(q\) has \(n=q^2+q+1\) points and the same number of lines, each incident to \(d=q+1\) vertices on the other side, with no four-cycle (two points determine a unique line). As \(q\to\infty\), \(d/\sqrt n\to1\), making the asymptotic variance constant equal to one. This proves sharpness without assuming existence of planes of non-prime-power order.

## Verification
The self-contained script `check_greedy_c4free.py` computes exact rational distributions by a dynamic program on remaining eligible vertex masks, independently of the formula. On cycles of missing edges, disconnected unions of cycles, deleted perfect matchings, and the point-line incidence graph of the seven-point projective plane, it compares every possible output set, individual atom mass, support, expectation and variance against the theorem. For a missing eight-cycle it also enumerates all \(8!\) input orders independently. A separate four-cycle-containing construction verifies that deleting the no-four-cycle hypothesis can change the support. The executed script returned `PASS 441 independent exact checks`. These finite computations are corroboration, not a substitute for the preceding all-graph proof. Reproduce with Python 3 using `python check_greedy_c4free.py` without third-party packages.

## Relationship to prior work
Krivelevich, Mészáros, Michaeli and Shikhelman (2019 preprint, later journal version) analyze the same random-order greedy maximal-independent-set algorithm via locally convergent graphs and concentration under subfactorial path-growth conditions. Their inspected theorems do not provide an exact output-set law for \(K_{n,n}\) with a sparse regular incidence graph deleted. Here the **resulting graph** has degree \(n-d\to\infty\), and in general has numerous four-cycles; it does not satisfy the sparse bounded-local-growth regime of those theorems. Gamarnik and Goldberg's earlier finite-girth estimates concern the girth of the input graph itself, not the girth of its sparse deleted-edge graph, and likewise do not give this law.

Related exact random-greedy laws have been established for complete multipartite graphs and nested-neighborhood chain graphs. Those families do not cover the generic sparse-deletion complements here: even for missing cycles of length at least eight, the input graphs have nonnested neighborhoods, while the complete multipartite input has no partially deleted cross-neighborhoods. The present proof derives the atom probabilities rather than treating literature search failure as a uniqueness certificate. Shaikh's 2026 triangle-free variance bound applies to the bipartite input \(G\), but its generic edge-count bound is of order \(n^2\) here and does not give the exact output law or the sharper family-wise \(n^{3/2}\) variance envelope; only its abstract and bibliographic record were inspected.

## Limitations
Four-cycle-freeness is imposed on the deleted bipartite graph \(H\), not on the input \(G\). With four-cycles in \(H\), mixed maximal independent sets may have at least two vertices on both sides; the two-point and uniform-atom laws need not hold. The result concerns uniform random orders, not adversarial or adaptive orders, other greedy tie-breaking, or general nonregular missing graphs. The variance-order sharpness is asymptotic and attained along projective-plane parameter values; it does not classify the exact finite-order variance maximizer for each \(n\). No historical-priority guarantee is claimed beyond the specific comparisons in the research review.

## References
1. M. Krivelevich, T. Mészáros, P. Michaeli and C. Shikhelman, *Greedy Maximal Independent Sets via Local Limits*, arXiv:1907.07216, first submitted 16 July 2019; Random Structures & Algorithms 64 (2024), 986–1015, DOI: 10.1002/rsa.21200.
2. D. Gamarnik and D. A. Goldberg, *Randomized Greedy Algorithms for Independent Sets and Matchings in Regular Graphs: Exact Results and Finite Girth Corrections*, arXiv:0807.1277, first submitted 8 July 2008.
3. *Exact random-greedy maximal-independent-set law on chain graphs*, publicly available research record `2026/10/4/SCOPE-exact-random-greedy-maximal-independent-set-law-on-chain-graphs--36fe61ce32de`.
4. *Sharp variance of random greedy maximal independent sets on complete multipartite graphs*, publicly available research record `2026/9/19/SCOPE-random-greedy-mis-variance-complete-multipartite--9cd73ef8690f`.
5. M. Shaikh, *Variance of random greedy independent sets in triangle-free graphs*, arXiv:2609.14826, first submitted 13 September 2026 (abstract-level comparison only).
