# Opposite short-chord effects on random-greedy jamming of cycles

## Finding

Let \(J(G)\) be the number of accepted vertices when a finite simple graph \(G\) is examined in a uniformly random vertex order, accepting each vertex exactly when no previously accepted neighbor is present. For \(n\ge4\), let \(C_n\) have vertex set \(\{0,\ldots,n-1\}\) and cyclic edges, and let \(C_n^{(d)}\) be obtained by inserting the edge \(\{0,d\}\). Define
\[
\Delta_{n,d}=\mathbb E J(C_n^{(d)})-\mathbb E J(C_n).
\]
For the two shortest nontrivial chords, the signs admit a complete classification:
\[
\begin{aligned}
&\Delta_{n,2}<0 &&(n\ge4,\ n\ne5),&\quad \Delta_{5,2}&=0;\\
&\Delta_{n,3}>0 &&(n\ge6,\ n\ne7),&\quad \Delta_{7,3}&=0.
\end{aligned}
\]
Thus forming a triangle by a chord reduces the expected jammed population (apart from the five-cycle exception), whereas forming a quadrilateral by a chord increases it (apart from the seven-cycle exception). In particular, even among chord additions to cycles, random-greedy occupancy is not monotone under inserting an edge.

## Assumptions and scope

All graphs are finite, undirected and simple; no multiple chords are inserted. Each vertex receives an independent continuous uniform priority, processed from smallest to largest. Distances \(d=2\) and \(d=3\) are measured along the displayed cyclic labelling; the stipulated ranges ensure \(\{0,d\}\) is not already a cycle edge. Every expected value refers to the final maximal independent set, not to the maximum independent set.

## Proof

**Exact finite recurrence.** Define \(F(\varnothing)=0\), and for every nonempty graph \(G\),
\[
F(G)=1+\frac{1}{|V(G)|}\sum_{v\in V(G)}F(G-N_G[v]),
\]
where \(N_G[v]\) denotes the closed neighborhood. Conditioning on the first vertex proves this identity exactly; restriction of the remaining random order is uniform. The recurrence is also additive over disjoint components. A standalone rational-arithmetic implementation uses bitmask induced subgraphs and memoization and computes all the signs for \(4\le n\le29\) with \(d=2\), and \(6\le n\le29\) with \(d=3\). It finds only the stated zero cases. Independent full permutation enumeration confirms the recurrence for \(n=6,7,8\) in both chord families.

**Uniform locality estimate.** Couple the greedy processes on \(C_n\) and \(C_n^{(d)}\) by giving corresponding vertices identical independent continuous priorities. A disagreement in acceptance can first arise only at one of the two chord endpoints. Any later disagreement can be traced backwards along a strictly decreasing-priority neighbor chain to one of those endpoints. Equivalently, it is reached from an endpoint by a strictly increasing-priority simple path. The graph \(C_n^{(d)}\) has at most two vertices of degree three and all others have degree two; from any starting vertex there are at most eight self-avoiding paths of each positive length: each degree-three vertex can branch at most once. The probability that any prescribed path of length \(k\) has increasing priorities is \(1/(k+1)!\). Consequently, letting \(B_r\) be the union of the short arc from \(0\) to \(d\) and the first \(r\) vertices along each of the two rays away from its endpoints on the complementary long arc, the expected number of vertices outside \(B_r\) whose acceptance changes upon inserting the chord is bounded by
\[
16\sum_{k\ge r+1}\frac1{(k+1)!}.
\]
The factor sixteen counts two possible endpoint roots times at most eight paths of each length.

To compare different cycle orders, choose \(R>r\) and \(n,m\ge d+2R+2\). The graphs induced by \(B_R\) in either unchorded or chorded cycles are canonically identical for orders \(n\) and \(m\); assign these local copies the same priorities. For a fixed \(v\in B_r\), its decision in the whole graph differs from its decision in the induced \(B_R\) only if a decreasing-priority path from \(v\) exits \(B_R\). Such a path has length at least \(R-r+1\), and the probability is at most
\[
8\sum_{k\ge R-r+1}\frac1{(k+1)!}.
\]
There are \(d+1+2r\) vertices in \(B_r\). Comparing both graph models and both cycle orders gives four such local errors per vertex; each of the two cycle orders additionally contributes the outside error above. Hence
\[
|\Delta_{n,d}-\Delta_{m,d}|\le
32(d+1+2r)\sum_{k\ge R-r+1}\frac1{(k+1)!}
+32\sum_{k\ge r+1}\frac1{(k+1)!}.
\]
The bound is for **expectations**, because disagreement vertices are bounded by the number of increasing paths; no independence between different disagreement events is assumed.

Set \(r=6\) and \(R=12\). For \(k\ge7\), the factorial tail is at most
\[
\sum_{k\ge7}\frac1{(k+1)!}\le\frac1{8!}\frac98=\frac1{35840}.
\]
Since \(d\le3\), all \(n,m\ge29\) satisfy
\[
|\Delta_{n,d}-\Delta_{m,d}|\le \frac{17}{1120}.
\]
The exact recurrence gives
\[
\Delta_{29,2}=-\frac{20784848750122134973}{96152177125598343750}
\quad\text{and}\quad
\Delta_{29,3}=\frac{7886534621278669}{174822140228360625}.
\]
The first is strictly less than \(-17/1120\), and the second strictly greater than \(17/1120\). Comparing every \(n\ge29\) to order twenty-nine forces the claimed strict signs. The finitely many smaller orders, including both exceptions, were covered by the exact rational recurrence. This proves the statement for all permitted orders.

## Verification

Run `python3 chord_greedy_verifier.py` using only Python's standard library. The checker recomputes fifty exact recurrence cases covering the full required finite range through order twenty-nine, independently enumerates all priority permutations for six small graph pairs, verifies the factorial-tail constant, and checks that both rational twenty-nine-vertex values lie beyond the uniform error bound. The checker reports `VERIFIED`, `TAIL_BOUND 17/1120`, and the two rational differences above. Exhaustive finite checking is a proof of the required finite cutoff only; the locality argument supplies the extension to every larger order.

## Relationship to prior work

The random greedy maximal independent-set model, path/cycle background, and factorially decreasing influence of monotone-priority paths are well established. Krivelevich, Mészáros, Michaeli and Shikhelman explicitly note that expected greedy-set size need not be monotone under deleting an edge, using a pair-of-stars example; their work also develops the decreasing-priority path locality method. The present result is not a claim to discover that general nonmonotonicity principle or the locality method. It establishes a different, fully quantified sign distinction for all simple cycles with either of the two shortest chords. Pippenger's earlier adsorption work establishes general jamming theory and treats various short-cycle regimes. The named sources inspected did not state this all-order sign classification; unexamined prior variants remain a priority risk.

## Limitations

The result concerns exactly one added chord of cyclic distance two or three, uniformly random priorities, and expected final occupancy. It neither orders the entire distributions nor determines signs for longer chords or arbitrary host graphs. The finite computation does not on its own establish any infinite claim; the proof additionally requires the path-counting and locality bounds. Independent validation and definitive historical-priority certification have not been performed.

## References

1. M. Krivelevich, T. Mészáros, P. Michaeli and C. Shikhelman, *Greedy maximal independent sets via local limits*, arXiv:1907.07216 (first publicly posted 2019-07-16), https://arxiv.org/html/1907.07216v6 .
2. N. Pippenger, *Random Sequential Adsorption on Graphs*, SIAM Journal on Discrete Mathematics 2 (1989), 393–402, https://doi.org/10.1137/0402034 .
3. G. Brightwell, S. Janson and M. Luczak, *The Greedy Independent Set in a Random Graph with Given Degrees*, Random Structures & Algorithms 51 (2017), 565–586, https://doi.org/10.1002/rsa.20716 .
