# All minimum power-dominating pairs in generalized Petersen graphs and a distance-three obstruction

## Finding

For every integer \(n\ge 9\), let \(G_n=GP(n,2)\) be the generalized Petersen graph defined below. **Its minimum power-dominating sets are exactly**
\[
\bigl\{\{a_i,a_{i+3}\}:i\in\mathbb Z_n\bigr\}
\;\cup\;
\bigl\{\{b_i,b_{i+1}\}:i\in\mathbb Z_n\bigr\}
\;\cup\;
\bigl\{\{a_i,b_{i+d}\}:i\in\mathbb Z_n,\ d\in\{-4,-3,3,4\}\bigr\}.
\]
In particular, \(\gamma_P(G_n)=2\), and there are exactly \(6n\) minimum power-dominating sets. Every vertex belongs to precisely six such sets.

Let \(X_n\) join two minimum power-dominating sets when one sensor location can be exchanged while preserving cardinality and power domination. The graph \(X_n\) is connected, \(10\)-regular, and has \(6n\) vertices and \(30n\) edges. Indeed, \(X_n\) is the line graph of the connected \(6\)-regular graph on \(\{a_i,b_i:i\in\mathbb Z_n\}\) whose edges are exactly the displayed successful pairs.

There is a sharp qualification to the earlier geodesic-distance-three assertion about these graphs: **for every \(n\ge13\), exactly \(n\) of the \(7n\) unordered pairs of vertices at graph distance three fail power domination**, namely
\[
\bigl\{\{b_i,b_{i+6}\}:i\in\mathbb Z_n\bigr\}.
\]
Thus precisely one seventh of distance-three pairs fail, while all other distance-three pairs succeed. This gives an explicit counterexample to the unconditional assertion in Lemma 4 of Girish--Somasundaram (2024) that every distance-three pair power dominates \(GP(n,2)\).

## Assumptions and scope

Indices lie in the cyclic group \(\mathbb Z_n\). The vertex set is \(\{a_i,b_i:i\in\mathbb Z_n\}\), with edges \(a_i a_{i+1}\), \(a_i b_i\), and \(b_i b_{i+2}\) for all \(i\). In particular, the inner rim may be disconnected when \(n\) is even; the graph is nevertheless connected because of its spokes.

Given sensors \(S\), mark the closed neighborhood \(N[S]\) observed. A *force* marks the unique unobserved neighbor of any observed vertex that has exactly one unobserved neighbor. Iterate until no force remains. The set \(S\) *power dominates* precisely when all \(2n\) vertices are observed. This formulation is equivalent to the usual vertex-and-edge monitoring rules (the standalone checker implements both definitions).

For distinct minimum sets \(S,T\), a *single-sensor exchange* means \(|S\mathbin{\triangle}T|=2\). No claim is made here for \(n<9\), for larger sensor sets, or for changes involving two simultaneous sensor substitutions.

## Proof

**Step 1: at least two sensors.** For \(n\ge9\), the graph is cubic, and each adjacent pair has no common neighbor (in particular, the girth is at least five). From one sensor, the initially observed vertices are the sensor and its three neighbors. Each of those neighbors has exactly two unobserved neighbors, so no propagation is possible. Thus \(\gamma_P(G_n)\ge2\).

**Step 2: an effective four-column block.** Suppose for some cyclic interval of four consecutive indices \(j,j+1,j+2,j+3\), all eight vertices \(a_r,b_r\) at those indices have been observed. At the left boundary, \(a_j\) forces \(a_{j-1}\) and \(b_{j+1}\) forces \(b_{j-1}\); at the right boundary, \(a_{j+3}\) forces \(a_{j+4}\) and \(b_{j+2}\) forces \(b_{j+4}\), unless these vertices are already observed. Thus the observed block expands in both directions until the whole graph is observed. This works for every \(n\ge9\).

**Step 3: classify all pairs for \(n\ge21\).** Rotations and reversal of cyclic indices reduce unordered pairs at distance at most three to the following types, with the first index normalized to zero:

| Type | Possible positive offsets \(d\) |
|---|---|
| \(\{a_0,a_d\}\) | \(1,2,3\) |
| \(\{a_0,b_d\}\) | \(0,1,2,3,4\) |
| \(\{b_0,b_d\}\) | \(1,2,4,6\) |

For mixed pairs the indices \(\pm d\) are equivalent by reflection. The table is exhaustive: in any walk of at most three edges, the outer-rim steps change an index by \(\pm1\), the inner-rim steps by \(\pm2\), and a spoke changes type without changing the index. Listing the edge-type words of length at most three yields exactly these offsets for each endpoint type. Distances \(\ge4\) are impossible starting pairs: the two sensor closed neighborhoods are disjoint with no edges between them, so no observed nonsensor vertex has a unique unobserved neighbor and propagation does not begin.

Direct application of the domination step and the parallel forcing rule gives the following **successful** configurations. Here the column range is modulo \(n\), and “by round” counts subsequent parallel forcing rounds after \(N[S]\):

| Initial sensors | Full observed consecutive columns | By round |
|---|---|---:|
| \(\{a_0,a_3\}\) | \(0,1,2,3\) | 1 |
| \(\{a_0,b_3\}\) | \(0,1,2,3\) | 2 |
| \(\{a_0,b_4\}\) | \(0,1,2,3\) | 3 |
| \(\{b_0,b_1\}\) | \(-1,0,1,2\) | 1 |

By Step 2, all these pairs power dominate. Their cyclic rotations and reflections give exactly the three families in the theorem.

The remaining distance-at-most-three pairs **stall**. The next table supplies their *entire* observed state after all forces; \(O\) and \(I\) list the outer and inner observed indices, respectively, with indices modulo \(n\). The displayed state is obtained from the initial closed neighborhood by zero or one parallel rounds. A direct check from the three neighbors of each displayed observed vertex shows that every observed vertex has either zero or at least two unobserved neighbors. Every listed set has fewer than \(2n\) observed vertices, so none power dominates.

| Initial sensors | \(O\) | \(I\) |
|---|---|---|
| \(\{a_0,a_1\}\) | \(-1,0,1,2\) | \(0,1\) |
| \(\{a_0,a_2\}\) | \(-1,0,1,2,3\) | \(-2,0,1,2,4\) |
| \(\{a_0,b_0\}\) | \(-1,0,1\) | \(-2,0,2\) |
| \(\{a_0,b_1\}\) | \(-2,-1,0,1,2\) | \(-3,-1,0,1,3\) |
| \(\{a_0,b_2\}\) | \(-1,0,1,2,3\) | \(-2,0,1,2,4\) |
| \(\{b_0,b_2\}\) | \(0,2\) | \(-2,0,2,4\) |
| \(\{b_0,b_4\}\) | \(0,2,4\) | \(-2,0,2,4,6\) |
| \(\{b_0,b_6\}\) | \(0,2,4,6\) | \(-2,0,2,4,6,8\) |

For \(9\le n\le20\), cyclic aliasing can merge offsets, so the stabilized table is not used. Instead, the standalone exhaustive checker constructs every pair, computes its complete forcing closure using **three distinct implementations** (synchronous vertex forcing, sequential vertex forcing, and the original edge-monitoring rules), and confirms that exactly the displayed families succeed, for each of the twelve values of \(n\). This is an exhaustive finite certificate, not an extrapolation from sampled examples. Combining it with the proof for \(n\ge21\) establishes the pair classification for every \(n\ge9\).

**Step 4: exchange graph.** Let \(H_n\) have the original \(2n\) vertices with one edge for every successful sensor pair. The classification gives each outer vertex two outer partners at offsets \(\pm3\) and four inner partners at offsets \(\pm3,\pm4\); each inner vertex has two inner partners at offsets \(\pm1\) and four outer partners. Thus \(H_n\) is simple and \(6\)-regular with \(6n\) edges. Its inner vertices form a spanning cycle of the inner part, and every outer vertex attaches to inner vertices, so \(H_n\) is connected. (This is a cycle in \(H_n\), not necessarily in the inner rim of \(G_n\).) Exchanging exactly one member of a successful pair is equivalent to taking two incident edges of \(H_n\). Consequently \(X_n=L(H_n)\) is connected, with \(6n\) vertices, degree \(2(6-1)=10\), and \(6n\cdot10/2=30n\) edges.

**Step 5: distance-three correction.** For \(n\ge21\), the length-three walk table in Step 3 shows the distance-three unordered pairs consist of the four successful types \(\{a_i,a_{i+3}\}\), \(\{a_i,b_{i\pm3}\}\), \(\{a_i,b_{i\pm4}\}\), \(\{b_i,b_{i+1}\}\), and the unsuccessful type \(\{b_i,b_{i+6}\}\). These contain \(n+2n+2n+n+n=7n\) distinct unordered pairs, of which precisely \(n\) are unsuccessful. The same statement for \(13\le n\le20\) follows from explicit exhaustive distance computations in the standalone checker.

An especially small transparent counterexample is \(n=13\) with sensors \(\{b_0,b_6\}\): the path \(b_0,b_2,b_4,b_6\) has length three, and the two endpoints have distance exactly three. After \(N[S]\) and one forcing round, the observed vertices are precisely
\[
\{a_0,a_2,a_4,a_6\}\cup\{b_0,b_2,b_4,b_6,b_8,b_{11}\}.
\]
Every one of these ten observed vertices has zero or at least two unobserved neighbors, so the process stalls with sixteen vertices unobserved. This explicitly refutes the stated sufficiency of graph distance three without making claims about other results of that source.

## Verification

Run `python3 verify.py` with a standard Python 3 interpreter and no third-party packages. It checks all sensor pairs and all singletons for \(9\le n\le20\), compares synchronous, sequential, and independent edge-monitoring propagation rules, checks the \(6n\) minimum-set count, the exact \(30n\) exchange-edge count, degree ten and connectivity, and independently enumerates distance-three exceptions for \(13\le n\le20\). It additionally checks all pairs for \(n\in\{21,22,23,29,37,61\}\) and verifies the stable local forcing and stalling states for \(n\in\{21,22,49,97\}\). The run terminates with `ALL_VERIFY_OK`.

The finite check supplies an exhaustive proof for the finite residual range. The stated symbolic walk classification and boundary-forcing arguments establish the infinite tail. Computations alone would not establish the all-parameter statement.

## Relationship to prior work

Barrera--Ferrero (first publicly available 18 October 2010) prove general power-domination upper bounds for generalized Petersen graphs; Section 5, Lemma 5.1 and Corollary 5.2 show the scalar value two for the odd-indexed subfamily. Xu--Kang (2011) address power-domination numbers of generalized Petersen graphs, including numerical bounds and a special parameter family, rather than this complete minimum-pair classification (only its abstract and secondary citation context were accessible).

Girish--Somasundaram (2024), Lemma 4, assert unconditionally that graph distance three between two vertices suffices for power domination of \(GP(n,2)\). Their primary publisher-indexed text was inspected around that lemma. The explicit distance-three pair \(\{b_0,b_6\}\subseteq GP(13,2)\) fails, so that asserted implication does not cover the theorem and is contradicted. The corrected exhaustive characterization, exact exceptional fraction, and line-graph exchange structure are the contributions here. The numerical minimum two and basic propagation principle are credited to prior work.

## Limitations

The theorem concerns exactly two initial sensors and \(n\ge9\). Neither maximal time to full observation nor counts of larger power-dominating sets are asserted. The stabilized local argument requires \(n\ge21\); smaller parameters are covered by a self-contained exhaustive finite checker. An unavailable full version of the Xu--Kang 2011 article and the uninspected portions of the Girish--Somasundaram 2024 article leave some residual risk of prior equivalent formulations. The published distance-three statement was checked against its primary indexed lemma text; no other conclusions from that article were audited. No independent external mathematical audit has been performed.

## References

1. R. Barrera and D. Ferrero, “Power domination in cylinders, tori, and generalized Petersen graphs,” *Networks* 58 (2011), 43–49; first online 18 October 2010. DOI: 10.1002/net.20413. Open author-hosted PDF: https://cpb-us-e1.wpmucdn.com/wp.txstate.edu/dist/1/556/files/2015/03/BarreraFerrero.pdf.
2. G. Xu and L. Kang, “On the power domination number of the generalized Petersen graphs,” *Journal of Combinatorial Optimization* 22 (2011), 282–291. DOI: 10.1007/s10878-010-9293-y.
3. L. Girish and K. Somasundaram, “Bound for the \(k\)-Fault-Tolerant Power-Domination Number,” *Symmetry* 16 (2024), article 781; Lemma 4. DOI: 10.3390/sym16070781. https://www.mdpi.com/2073-8994/16/7/781.
