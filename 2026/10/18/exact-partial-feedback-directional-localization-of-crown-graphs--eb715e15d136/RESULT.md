# Exact partial-feedback directional localization of crown graphs

## Finding

**Theorem.** For every integer \(n\ge5\), let \(\operatorname{Cr}_n=K_{n,n}-M_n\) be the crown graph obtained by removing a fixed perfect matching from the balanced complete bipartite graph. In the partial-feedback directional localization game of Jones and Kinnersley,
\[
\operatorname{dirloc}(\operatorname{Cr}_n)=n-1.
\]
Moreover, \(n-1\) cops have an adaptive strategy that identifies the robber within **two rounds**, while \(n-2\) cops cannot win in any bounded number of rounds. In comparison, \(\operatorname{dirloc}(K_{n,n})=n\) by Jones and Kinnersley's Proposition 2.2(iv). Thus removing a perfect matching decreases this search parameter by exactly one for all \(n\ge5\).

## Assumptions and scope

All graphs are finite, simple, connected and undirected. Label the two independent sets \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), with \(a_i b_j\) an edge precisely if \(i\ne j\). A probe at a vertex \(v\) must receive a **single** reported vertex \(w\): if the robber is at \(v\), the report is \(v\); otherwise \(w\) is adjacent to \(v\) and lies on a shortest path from \(v\) to the robber. Each cop simultaneously probes one vertex per round; after feedback, unless identified, the robber can stay or move across one edge. A strategy wins only if it determines the robber's location in a bounded number of rounds against all legal reports and moves. The assertion is about **partial feedback**, not full feedback. The proof of the upper bound actually works for \(n\ge4\), but the new theorem is stated for \(n\ge5\) to separate the already studied cube \(\operatorname{Cr}_4\cong Q_3\).

A *belief set* is the set of all robber vertices consistent with the feedback observed so far. Immediately after a round's reports, belief sets are intersected with the vertices compatible with those reports; after the robber's move they expand to the union of closed neighborhoods. The robber may force non-identification indefinitely if he can keep the belief set non-singleton after every round.

## Proof

**A two-round upper strategy.** Fix an index \(t\in\{1,\ldots,n\}\). In round one, probe all \(n-1\) vertices \(a_i\) with \(i\ne t\).

If the robber is at any probed vertex \(a_i\), that probe identifies him. If at \(b_t\), each probe returns \(b_t\), which is a response vector unique to that location. If at \(b_s\) with \(s\ne t\), every probe at \(a_i\) with \(i\notin\{s,t\}\) returns \(b_s\); the single probe at \(a_s\) can return a different neighbor \(b_j\). Distinct possibilities \(b_s,b_u\) are separated by a probe \(a_i\) outside \(\{s,u,t\}\), which exists for \(n\ge4\). Consequently no response vector can be compatible with two distinct vertices of \(B\).

The only unprobed vertex of \(A\) is \(a_t\). From \(a_i\), with \(i\ne t\), every shortest path to \(a_t\) starts through a vertex \(b_j\) with \(j\notin\{i,t\}\). Thus a response from \(a_t\) cannot use \(b_t\), and whenever it also matches a response from a vertex of \(B\), that vertex is a unique \(b_s\) with \(s\ne t\). Any nonterminal round-one feedback therefore leaves **exactly** the possible locations \(\{a_t,b_s\}\) for some \(s\ne t\).

The union of their closed neighborhoods is
\[
N[a_t]\cup N[b_s]=V(\operatorname{Cr}_n)\setminus\{a_s,b_t\},
\]
because the two missing matching edges are \(a_t b_t\) and \(a_s b_s\). Hence at the start of round two the robber cannot occupy \(a_s\) or \(b_t\). Probe every vertex of \(A\setminus\{a_s\}\). Every possible robber vertex in \(A\) is probed and immediately identified. Any two distinct possibilities \(b_j,b_k\) are separated by a probe \(a_i\) with \(i\notin\{s,j,k\}\), again available for \(n\ge4\). This probe is adjacent to both possible robber vertices and is forced to report the robber's actual vertex. Thus every legal response vector in round two singles out one vertex, so \(n-1\) cops always win by the end of that round.

**A perpetual lower strategy.** Consider the family of belief sets
\[
\mathcal F=\{V\}\ \cup\ \bigl\{V\setminus\{a_q,b_p\}:p,q\in\{1,\ldots,n\},\ p\ne q\bigr\}.
\]
At the start of the game the belief set contains \(V\in\mathcal F\). Maintain the invariant that, at the beginning of each round, the actual belief set **contains** some member of \(\mathcal F\). Suppose at most \(n-2\) vertices are probed. Their matching indices occupy at most \(n-2\) positions, leaving at least two unprobed indices in \(U\). Choose the member of \(\mathcal F\) contained in the actual belief set. We can choose **distinct** \(p,q\in U\) for which both \(a_p\) and \(b_q\) belong to that member. This is automatic for member \(V\). For \(V\setminus\{a_j,b_i\}\) with \(i\ne j\), we need \(p\ne j\) and \(q\ne i\); if two unused indices are considered, at least one of their two possible orders satisfies both inequalities, since both orders could fail only if \(i=j\). Larger \(U\) only gives more choices.

For **every** probe at \(a_h\), the robber can return \(b_q\), a reply consistent both with robber position \(a_p\) (the two-step path \(a_h,b_q,a_p\)) and with robber position \(b_q\) (direct edge). For every probe at \(b_h\), he can return \(a_p\), consistent both with position \(a_p\) (direct edge) and \(b_q\) (the two-step path \(b_h,a_p,b_q\)). These paths exist because \(h,p,q\) are pairwise distinct. After this common response vector, at least \(a_p,b_q\) remain possible. Recontamination from them includes exactly
\[
N[a_p]\cup N[b_q]=V\setminus\{a_q,b_p\},
\]
a member of \(\mathcal F\). The complete new belief set may be larger, but it **contains** this member of \(\mathcal F\). Hence the maintained containment invariant applies to the next round. Every round has at least two consistent robber positions. Standard belief-state/adversarial-play equivalence, or the finitely branching strategy tree argument, shows that no strategy using \(n-2\) or fewer cops can force localization in bounded time. Hence \(\operatorname{dirloc}(\operatorname{Cr}_n)\ge n-1\), completing the proof.

## Verification

The standalone program `verify_directional_crown.py` constructs the graph's exact geodesic response relation, computes all possible simultaneous feedback vectors for each probe set, and solves the resulting finite belief-state reachability game by attractor iteration. With standard Python 3.10 or later, run:

```bash
python verify_directional_crown.py
```

It verifies \(\operatorname{dirloc}(\operatorname{Cr}_n)=n-1\) for \(n=3,4,5,6\) without using either constructive proof strategy. It separately checks every response branch of the two-round strategy and the lower-invariant witness construction for \(n=5,6,7\). The general theorem follows from the preceding proof, **not** from those finite computations.

## Relationship to prior work

Jones and Kinnersley's 2026 introduction of the partial-feedback directional localization game establishes \(\operatorname{dirloc}(K_{m,n})=\min\{m,n\}\) and provides general bounds for degenerate graphs and various graph products. The exact perfect-matching-deletion law for all crown graphs with \(n\ge5\) does not follow from the cited complete-bipartite formula: deletion changes shortest paths, feedback options and contamination dynamics. Its explicit evasion invariant and adaptive two-round upper policy address those changes.

A previously published finite result gives \(\operatorname{dirloc}(Q_3)=3\) for the three-cube, which is isomorphic to \(\operatorname{Cr}_4\); that instance is outside the new theorem. Published results on crown-graph edge metric dimension also yield the number \(n-1\), but concern a static distance-resolving invariant, not the adversarial movable-robber game, and hence do not imply the present statement.

## Limitations

The theorem covers only the partial-feedback game and balanced complete bipartite graphs with **a full perfect matching** deleted. It does not determine the number for general matching-deleted rectangular bicliques, nor assert a similar formula under full-feedback rules. The inspected primary manuscript material establishes the rules and the closest complete-bipartite result; some later sections of that manuscript could not be inspected in full during this literature comparison. The resulting bibliographic risk, including unindexed equivalent work, remains even though searches found no covering theorem. No independent mathematical audit has been performed.

## References

1. John Jones and William B. Kinnersley, *The directional localization game on graphs*, arXiv:2609.01745v1 (first public version 2026-09-01), especially Definition of partial feedback and Proposition 2.2. https://arxiv.org/abs/2609.01745
2. *Directional localization of the three- and four-dimensional hypercubes*, published published-finding corpus research record dated 2026-10-04, identifier `2026/10/4/SCOPE-directional-localization-of-the-three-and-four-dimensional-hyper--0602bf7c55ae`, finite cube case. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-directional-localization-of-the-three-and-four-dimensional-hyper--0602bf7c55ae
3. *Edge metric bases of crown graphs*, published published-finding corpus research record dated 2026-10-04, identifier `2026/10/4/SCOPE-edge-metric-bases-of-crown-graphs--b5b3c45f23e8`; related graph family, different invariant. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-edge-metric-bases-of-crown-graphs--b5b3c45f23e8
