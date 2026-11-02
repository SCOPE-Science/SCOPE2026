# Maximal induced matchings of complete-graph incidence families: exact polynomials and cardinality gaps

## Finding

For every finite simple graph \(G\), write \(I(G)\) for its incidence graph, with one original vertex for each vertex of \(G\), one subdivision vertex for each edge, and an incidence edge for every endpoint–edge pair. An **induced matching** is a set of edges whose incident vertices induce a disjoint union of edges. It is **inclusion-maximal** if no incidence edge can be added without violating this property. Let \(\mathcal M_H(z)=\sum_{F}z^{|F|}\), summed over inclusion-maximal induced matchings \(F\) of \(H\). Let \(\mathrm S(i,j)\) be a Stirling number of the second kind, interpreted as zero for \(j>i\) or \(j<1\).

**Theorem.** For all integers \(a,b\ge1\),
\[
\begin{aligned}
\mathcal M_{I(K_{a,b})}(z)={}&b^a z^a+a^b z^b\\
&+\sum_{p=1}^{a-1}\sum_{q=1}^{b-1}
 \binom ap\binom bq
 (b-q)!\,\mathrm S(p,b-q)
 (a-p)!\,\mathrm S(q,a-p)z^{p+q}.
\end{aligned}
\]
For all integers \(n\ge2\),
\[
\mathcal M_{I(K_n)}(z)=
\sum_{k=\lceil n/2\rceil}^{n-1}
\binom nk (n-k)!\,\mathrm S(k,n-k)z^k.
\]
These count **every labeled inclusion-maximal induced matching by its number of edges**, not arbitrary matchings and not merely maximum induced matchings.

The possible cardinalities for \(I(K_n)\) are exactly the integers from \(\lceil n/2\rceil\) through \(n-1\). For \(1\le a\le b\), the possible cardinalities for \(I(K_{a,b})\) are \(\{1\}\) if \(a=b=1\); \(\{1,b\}\) if \(a=1<b\); and
\[
\{a\}\,\cup\,\{b,b+1,\ldots,a+b-2\}
\]
if \(a\ge2\). In particular, \(I(K_{2,b})\), for \(b\ge4\), has maximal induced matchings **only** of sizes \(2\) and \(b\), producing arbitrarily long internal gaps even among connected bipartite graphs. If \(3\le a\le b\), the number of maximum-cardinality maximal induced matchings is exactly \(ab\); for \(a=2\), \(b\ge3\), it is \(2^b+2b\).

## Assumptions and scope

All vertices are labeled and graphs are finite and simple. The construction \(I(G)\) is the **full single subdivision** of every original edge, not the line graph, not the original complete bipartite graph, and not an arbitrary matching-counting problem. There are no edges between original vertices or between subdivision vertices. The degenerate \(K_{1,1}\) case gives the path on three vertices and polynomial \(2z\). All powers and Stirling numbers use exact integer arithmetic.

## Proof

**1. Induced matching as a partial map.** Fix \(G\). Every incidence edge of \(I(G)\) has one original endpoint \(v\) and the subdivision vertex representing an original edge \(\{v,w\}\). Orient it as \(v\mapsto w\). A collection of these incidence edges is an induced matching exactly when its original tails are distinct and **no tail occurs as another incidence's head**. Indeed distinct tails prevent shared original endpoints; the induced condition excludes adjacency between any selected original tail and another selected subdivision vertex, which is precisely the forbidden tail–head relation. If two incidences use the same subdivision vertex, they would be the orientations of the same original edge in opposite directions and violate the same tail–head condition. Consequently selected incidences correspond bijectively to maps \(f:T\to V(G)\setminus T\) satisfying \(\{v,f(v)\}\in E(G)\) for every \(v\in T\).

**2. Complete graphs.** For \(G=K_n\) choose \(T\) with \(k\) elements. Its complement \(U\) has \(r=n-k\ge1\) elements, and the induced matching corresponds to any map \(f:T\to U\). It is maximal if and only if \(f\) is onto. If a vertex \(u\in U\) is not an image and \(r\ge2\), choose \(w\in U\setminus\{u\}\); adding \(u\mapsto w\) preserves the induced property. If \(r=1\), surjectivity is automatic. Conversely, when every \(u\in U\) is an image, no new tail can be chosen: every available original vertex is the head of an already selected incidence. Surjections onto the labeled set \(U\) are counted by \(r!\mathrm S(k,r)\). Choose \(T\) in \(\binom nk\) ways. Their existence is equivalent to \(1\le r\le k\), proving the second polynomial and its exact cardinality support.

**3. Complete bipartite graphs.** Write the fixed original shores as \(A,B\), with sizes \(a,b\). Let \(T_A,T_B\) be the selected tails and set \(p=|T_A|\), \(q=|T_B|\). By Step 1, the incidence selection consists of two independent functions
\[
f_A:T_A\to B\setminus T_B,\qquad
f_B:T_B\to A\setminus T_A.
\]
If \(T_A=A\), then necessarily \(T_B=\varnothing\), and every one of the \(b^a\) functions \(A\to B\) is maximal, since no unselected original vertex has a permitted neighbor outside the selected tail shore. This gives \(b^a z^a\). Symmetrically, \(T_B=B\) gives \(a^b z^b\). The two cases are disjoint since the graph has an edge.

In every remaining case, \(A\setminus T_A\ne\varnothing\) and \(B\setminus T_B\ne\varnothing\). If an unused original vertex \(x\in A\setminus T_A\) is not an image of \(f_B\), then for any \(y\in B\setminus T_B\), the incidence \(x\mapsto y\) can be added. The converse is equally direct: if every available original vertex on both shores appears as a head, no new tail can be added. Thus maximality is equivalent to **both maps being onto**. It forces \(1\le p<a\) and \(1\le q<b\). Choose the two tail sets in \(\binom ap\binom bq\) ways. The two independent surjection counts are \((b-q)!\mathrm S(p,b-q)\) and \((a-p)!\mathrm S(q,a-p)\). Multiplication and summation prove the first polynomial, with no double counting.

**4. Exact support and extremal counts.** An interior summand is positive exactly when
\[
1\le p<a,\quad1\le q<b,\quad p+q\ge\max(a,b).
\]
For \(2\le a\le b\), every integer \(k\) between \(b\) and \(a+b-2\) can be written as \(p+q=k\) satisfying these inequalities, while the all-\(A\) boundary supplies cardinality \(a\). There are no other values. For \(a=1\), the interior sum is empty. For \(I(K_n)\), the earlier surjection criterion gives all integers from \(\lceil n/2\rceil\) to \(n-1\). If \(a\ge3\), the unique interior index pair at the top degree \(a+b-2\) is \((p,q)=(a-1,b-1)\); its term equals \(ab\), and neither boundary term reaches this degree. For \(a=2\), the top degree is \(b\), with \(2^b\) boundary choices and \(2b\) interior choices when \(b\ge3\). All asserted boundaries follow.

## Verification

The independent executable `verify_incidence.py` constructs each incidence graph as an ordinary graph, forms the conflict graph of its incidence edges, recursively enumerates its induced matchings, tests inclusion-maximality by whether the chosen conflict neighborhoods cover all incidence edges, and compares complete coefficient dictionaries with the displayed formulas. It checks 25 labeled graph instances (19 complete-bipartite instances and six complete graphs), visiting 213715 independent-set recursion nodes; a separate exact-integer test checks 51 support cases. The final output was `VERIFY_OK`. This computation independently corroborates but does not replace the infinite bijective proof. Reproduce using `python3 verify_incidence.py` with Python 3 and no third-party packages.

## Relationship to prior work

Pippenger (2001), Sections 2, 4, and 5, enumerates **ordinary matchings** in the same incidence graphs and describes partial maps with restrictions on opposing two-cycles. His maps can use a vertex both as a head and as a tail; such configurations need not form induced matchings. Moreover arbitrary matching totals do not determine which induced matchings are inclusion-maximal. The present surjection and gap conclusions are therefore not a restatement or specialization of that matching enumeration.

Akbari, Ekim, Ghodrati, and Zare (2019) investigate well-indumatched graphs and minimum maximal induced matchings, principally through tree and girth classifications; no matching-size polynomial for these incidence families is supplied in the inspected material. Yuan, Yang, Zheng, and Gong (2024) establish sharp **general-graph extremal upper bounds on numbers** of maximal induced matchings, not the exact cardinality distribution within these subdivision families. The present formulas imply concrete size spectra and arbitrarily long gaps not contained in those stated bounds. A literature search did not identify equivalent all-parameter formulas; this is not a proof of publication priority.

## Limitations

The formulas concern only full subdivisions of complete and complete bipartite graphs, not arbitrary base graphs, partial subdivisions, hypergraph incidence graphs, or unlabeled isomorphism classes. The computational tests are finite, and publication priority is provisional: unindexed or inaccessible equivalent sources might exist. No independent mathematical audit has been performed.

## References

1. Nicholas Pippenger, *Enumeration of Matchings in the Incidence Graphs of Complete and Complete Bipartite Graphs*, University of British Columbia technical report TR-2001-12, first posted September 10, 2001; SIAM Journal on Discrete Mathematics 16 (2002), 47–63. https://www.cs.ubc.ca/tr/2001/tr-2001-12
2. S. Akbari, T. Ekim, A. H. Ghodrati, S. Zare, *Well-indumatched Trees and Graphs of Bounded Girth*, arXiv:1903.03197, March 7, 2019. https://arxiv.org/abs/1903.03197
3. Bo-Jun Yuan, Zhao-Yu Yang, Lu Zheng, Shi-Cai Gong, *Maximal and maximum induced matchings in connected graphs*, arXiv:2410.11288, October 15, 2024. https://arxiv.org/abs/2410.11288
