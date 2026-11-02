# Sharp token-jump diameter and two maximal-matching strata in subdivided complete graphs

## Finding

Let \(S(K_n)\) be the graph obtained by replacing each edge of a complete graph on \(n\) labelled vertices with a path of length two, for an integer \(n\geq3\). Define its *maximal-matching token-jump graph* \(\mathcal R_n\): vertices are the inclusion-maximal matchings of \(S(K_n)\), and two are adjacent if their edge sets have symmetric difference of size two (one matched edge is replaced by one different edge).

Every inclusion-maximal matching has cardinality \(n-1\) or \(n\). There are exactly \(n\) matchings of size \(n-1\), and each is an isolated vertex of \(\mathcal R_n\). Write \(a_n\) for the already-known number of maps \(f:[n]\longrightarrow[n]\) such that \(f(f(i))\ne i\) for every \(i\) (OEIS A134362). The remaining \(a_n\) configurations have size \(n\). For every \(n\geq4\), their induced token-jump graph \(\mathcal U_n\) is connected, is regular of degree \(n(n-3)\), has \(\tfrac12a_n n(n-3)\) edges, and has **exact diameter**

\[
\operatorname{diam}(\mathcal U_n)=n+\left\lfloor\frac n3\right\rfloor.
\]

Consequently, \(\mathcal R_n\) has exactly \(n+1\) connected components for \(n\geq4\), of which \(n\) are isolated vertices. At \(n=3\), all five vertices of \(\mathcal R_3\) are isolated; the two size-three configurations have no connecting edge. The maximum-tier counting sequence \(a_n\) and its inclusion–exclusion formula are **not** claimed as new. The new assertion is the sharp reconfiguration metric and complete component/degree structure of the matching configuration graph.

## Assumptions and scope

The underlying graph is finite, simple and undirected, with original vertex set \([n]=\{1,\ldots,n\}\), and a new subdivision vertex \(e_{ij}\) adjacent to exactly \(i,j\) for each original pair \(\{i,j\}\). A matching is a set of pairwise vertex-disjoint graph edges; it is *maximal* if no edge can be added while remaining a matching. Maximal is not synonymous with maximum. A token jump may replace an edge with any other edge, whether or not they share a vertex, provided the final matching is inclusion-maximal. Token jumps preserve cardinality. Graph diameter is asserted only for the connected maximum-cardinality tier, not for disconnected \(\mathcal R_n\).

For reference, the known count has the explicit form

\[
a_n=\sum_{k=0}^{\lfloor n/2\rfloor}(-1)^k\frac{n!}{2^k k!(n-2k)!}(n-1)^{n-2k}.
\]

Thus the previously known counting sequence gives the straightforward maximal-matching cardinality enumerator \(nz^{n-1}+a_nz^n\). The formula is included for identification and reproducibility, not asserted as an independent novel result.

## Proof

**1. Two cardinality strata.** Each matching uses at most one edge incident with each of the \(n\) original vertices. If two original vertices \(i,j\) were both unmatched, then the subdivision vertex \(e_{ij}\) would also be unmatched and an incident graph edge could be added. Thus a maximal matching leaves at most one original vertex unmatched, and its cardinality is either \(n-1\) or \(n\). If exactly \(i\) is unmatched, every subdivision vertex \(e_{ij}\) must be matched, necessarily to original vertex \(j\), for all \(j\ne i\). Hence this matching is uniquely specified by \(i\), is indeed maximal, and no other size-\(n-1\) matching exists. Any two different such matchings have more than one edge in their symmetric difference when \(n\ge3\), so they have no token-jump adjacency. They cannot jump to the size-\(n\) stratum because a jump preserves size.

**2. Function representation and degree.** A size-\(n\) matching saturates each original vertex. Write \(f(i)=j\) when original vertex \(i\) is matched to subdivision vertex \(e_{ij}\). Distinct matching edges cannot use the same subdivision vertex, hence \(f(f(i))\ne i\). Conversely, every map satisfying these inequalities defines a size-\(n\) matching, and any such matching is automatically maximal. This is a bijection with the functions counted in OEIS A134362. Changing a single matching edge means changing precisely one value \(f(i)\). For a fixed coordinate \(i\), the permissible new targets are all \(j\notin\{i,f(i)\}\) with \(f(j)\ne i\). There are \(n-2-d_f^-(i)\) choices, where \(d_f^-(i)=|\{j:f(j)=i\}|\), because the forbidden targets are disjoint under the no-reciprocal-pair hypothesis. Summing over coordinates gives \(n(n-2)-\sum_i d_f^-(i)=n(n-3)\). The handshaking lemma yields the edge count.

**3. Sharp upper bound on distance.** Fix valid functions \(f,g\). Call \(i\) *wrong* if \(f(i)\ne g(i)\). As long as a wrong \(i\) satisfies \(f(g(i))\ne i\), updating \(f(i)\) directly to \(g(i)\) is permitted and permanently corrects that coordinate. Suppose all wrong coordinates are blocked: \(f(g(i))=i\) for every wrong \(i\). Such \(g(i)\) must also be wrong; otherwise \(f(g(i))=g(g(i))=i\) would contradict validity of \(g\). Moreover, \(g\) is injective on the set \(C\) of wrong coordinates because \(f(g(i))=i\), so \(g|_C\) is a permutation of \(C\). Its cycles all have length at least three: a fixed point or two-cycle would violate \(g(g(i))\ne i\). On each cycle, \(f\) is the inverse permutation of \(g\).

Select a cycle of length \(L\ge3\). There is a vertex \(j\) on it with \(d_f^-(j)\le n-3\): if every vertex on the cycle had indegree at least \(n-2\), then \(\sum_i d_f^-(i)\ge 3(n-2)>n\) for \(n\ge4\), impossible. Hence \(j\) admits a legal target \(k\) distinct from both \(f(j)\) and \(g(j)\). Temporarily change \(f(j)\) to \(k\). Now set to its desired value the predecessor of \(j\) under \(g\); continue backwards along this target cycle, setting each predecessor to its target, and finish by setting \(j\) to \(g(j)\). Each of those \(L\) updates is legal: it points to a vertex whose outgoing target was just corrected, and a \(g\)-cycle of length at least three has no reciprocal pair. The cycle is fixed after exactly \(L+1\) moves, without altering any coordinate outside it. All other direct corrections take one move each. The cycles resolved by detours are disjoint and each uses at least three previously wrong coordinates. Thus, at most \(\lfloor n/3\rfloor\) detours occur, while exactly \(|\{i:f(i)\ne g(i)\}|\le n\) final-setting moves occur. Every pair is connected by at most \(n+\lfloor n/3\rfloor\) jumps.

**4. Sharp lower bound.** Partition \([n]\) into \(q=\lfloor n/3\rfloor\) cycles of lengths at least three: take \(q-1\) three-cycles and one cycle of length \(n-3(q-1)\), which is \(3\), \(4\), or \(5\). Let \(g\) be the successor map on these cycles and \(f=g^{-1}\). Both maps are valid and differ at every one of the \(n\) coordinates. Thus any reconfiguration requires at least \(n\) coordinate edits. Additionally, for each of the \(q\) cycles, the first edit to a coordinate in that cycle cannot assign its final desired value, because for every \(i\) in that cycle, initially \(f(g(i))=i\), and changes outside that cycle cannot remove the reciprocal-edge obstruction. Each cycle therefore requires at least one edit **in addition to** the \(n\) final-setting edits, irrespective of interleaving. This gives the lower bound \(n+q\), which matches the upper bound.

For \(n=3\), the only valid maps are the two directed three-cycles; a permitted one-coordinate update never exists, so those two vertices and the three smaller maximal-matchings are all isolated. This completes the proof.

## Verification

The accompanying standalone Python program `VERIFY.py` constructs each original subdivided graph from its incidence edges; independently enumerates candidate matchings; tests the original inclusion-maximality condition; and reconstructs token-jump adjacencies. It checks all configurations for \(3\le n\le6\), and all ordered pairs of maximum matchings at \(n=4,5\) by the constructive routing algorithm; it samples 2,000 fixed-seed ordered pairs at \(n=6\). It independently computes exact full-graph diameter for \(n=4,5\) and verifies the sharp diameter lower-bound witness at \(n=6\). The total maximal-matching counts are \(5,34,449,7366\), respectively, and all finite comparisons pass. These tests do not replace the proof for general \(n\).

Reproduce using a standard Python 3 interpreter with `python VERIFY.py`; no external dependencies or other files are required.

## Relationship to prior work

Baste, Fürst, Henning, Mohr and Rautenbach (2019) study the classical minimum maximal-matching/edge-domination problem and its approximation bounds (primary MSC 05C69). Bousquet, Hatanaka, Ito and Mühlenthaler (2018) investigate token-jump matching reconfiguration and establish general algorithms and connectivity criteria, which provide important prior context; general connectivity is therefore **not** represented as a newly introduced notion. Neither inspected paper gives the exact specialized \(n+\lfloor n/3\rfloor\) diameter law or the complete two-tier degree/component description for \(S(K_n)\). The function-count correspondence and its inclusion–exclusion formula match **OEIS A134362**, recorded since 2008, and are explicitly credited as prior art. The new diameter concerns the graph of these already-enumerated functions under legal one-coordinate changes, not their number.

## Limitations

The theorem concerns one-subdivisions of complete graphs and the specifically defined token-jump move; other reconfiguration conventions can produce different distances. The full graph \(\mathcal R_n\) is disconnected, so no finite diameter is assigned to it. The claim has been mathematically checked and subjected to finite verification, but it has no independent audit or formal machine proof. Literature searches do not establish absolute novelty; unindexed matching-reconfiguration papers, or equivalent work under other descriptions of functional digraphs, remain possible priority risks.

## References

1. J. Baste, M. Fürst, M. A. Henning, E. Mohr and D. Rautenbach, *Bounding and approximating minimum maximal matchings in regular graphs*, arXiv:1905.12241, initial public version 2019-05-29, https://arxiv.org/html/1905.12241v1.
2. N. Bousquet, T. Hatanaka, T. Ito and M. Mühlenthaler, *Shortest Reconfiguration of Matchings*, arXiv:1812.05419, initial public version 2018-12-13, https://arxiv.org/html/1812.05419v1.
3. OEIS Foundation, Sequence A134362, *Number of maps whose second iterate has no fixed points*, https://oeis.org/A134362 (entry created 2008; published inclusion–exclusion expression dated 2016).
