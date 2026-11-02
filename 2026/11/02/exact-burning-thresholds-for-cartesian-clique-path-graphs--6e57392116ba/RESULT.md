# Exact burning thresholds for Cartesian clique–path graphs

## Finding

Write \(b(G)\) for the (ordinary, vertex) burning number of a finite simple graph. For every pair of integers \(m\ge3\) and \(n\ge1\), the Cartesian product of a clique with a path has the exact burning number

\[
 b(K_m\square P_n)=
 \begin{cases}
  1+\lceil\sqrt n\rceil,&m\ge4,\\
  2,&m=3,\ n=1,\\
  1+\max\{2,\lceil\sqrt{n-1}\rceil\},&m=3,\ n\ge2.
 \end{cases}
\]

Equivalently, for every integer \(k\ge3\), the greatest path length that can be burned in at most \(k\) rounds is exactly \((k-1)^2\) for every clique width \(m\ge4\), but exactly \((k-1)^2+1\) for width \(m=3\). For \(k=2\), the largest burnable path length is one in either case. This is a sharp, width-three extra-column phenomenon.

## Assumptions and scope

Let \(K_m\) be the complete graph on \(m\) vertices and let \(P_n\) be the path on the columns \(1,\ldots,n\). The product vertices are pairs \((a,j)\), where \(1\le a\le m\) and \(1\le j\le n\). Adjacency changes precisely one coordinate along an edge. Consequently

\[
 d((a,j),(b,h))=|j-h|+\mathbf 1_{a\ne b}.
\]

We use the standard ball-cover formulation of graph burning: \(b(G)\le k\) precisely when a sequence of sources \(x_1,\ldots,x_k\) has \(\bigcup_{i=1}^k N_{k-i}[x_i]=V(G)\). Sources are allowed to repeat or be redundant; this convention does not change the minimum burning number. Every assertion below is over integer parameters, not an inference from numerical experiments.

## Proof

**1. Full columns and tips.** Fix a hypothetical covering by \(k\ge2\) source balls. For each positive radius \(r=1,\ldots,k-1\), let the source be at column \(c_r\) and in row \(a_r\). The ball covers *all* \(m\) vertices in precisely the full-column interval

\[
 I_r=[c_r-r+1,c_r+r-1]\cap[1,n].
\]

It additionally covers at most two vertices outside that interval, namely the row-\(a_r\) vertices in columns \(c_r-r\) and \(c_r+r\), if these exist. The sole radius-zero ball covers one vertex. Thus \(|I_r|\le2r-1\), and

\[
 L:=\sum_{r=1}^{k-1}|I_r|\le\sum_{r=1}^{k-1}(2r-1)=(k-1)^2.
\]

Let \(U=\bigcup_{r\ge1}I_r\), let \(X=[1,n]\setminus U\) be the set of unfilled columns, and put \(W=L-|U|\). In each filled column \(p\in U\), write \(M_p\) for the number of intervals \(I_r\) containing \(p\). Hence \(W=\sum_{p\in U}(M_p-1)\). We call \(W\) the interval-overlap budget.

**2. Endpoints pay for holes.** For each hole \(x\in X\), let \(a_x\) count the intervals ending at \(x-1\) and let \(b_x\) count intervals beginning at \(x+1\). An interval can contribute a ball-tip at \(x\) only if it ends immediately before \(x\) or starts immediately after \(x\). In particular, even allowing coincident row choices and counting every contribution optimistically, at most \(a_x+b_x\) distinct rows at \(x\) are covered by positive-radius tips. Write \(z_x=1\) when the radius-zero source lies at \(x\), and zero otherwise. If the entire graph is covered, necessarily

\[
 a_x+b_x+z_x\ge m\qquad(x\in X),
 \qquad\sum_{x\in X}z_x\le1.
\]

Define \(R_x=(a_x-1)_++(b_x-1)_+\), where \((t)_+=\max\{0,t\}\). We claim the exact budget bound

\[
 \sum_{x\in X}R_x\le W.\tag{1}
\]

To prove (1), allocate \((a_x-1)_+\) to the filled column \(p=x-1\), if one exists, and \((b_x-1)_+\) to the filled column \(p=x+1\). If a filled column \(p\) is adjacent to a hole only on its right, every full interval that contains \(p\) must terminate there, so its charge is at most \(M_p-1\). The analogous statement holds if the hole is only on the left. If there are holes on both sides, every full interval containing \(p\) is the singleton interval \(\{p\}\). Since \(p\) is an interior column and there is only one radius-one ball, this forces \(M_p\le1\), and both charges are zero. Thus each filled column receives at most \(M_p-1\) in total. Summation proves (1), including boundary columns.

For nonnegative integers \(a,b\), one has \(a+b\le(a-1)_++(b-1)_++2\). Therefore any hole with \(a_x+b_x\ge3\) has \(R_x\ge1\). When \(m\ge4\), the covering condition forces \(a_x+b_x\ge m-z_x\ge3\) at *every* hole. Using (1),

\[
 |X|\le\sum_{x\in X}R_x\le W,
 \quad n=|U|+|X|\le |U|+W=L\le(k-1)^2.\tag{2}
\]

When \(m=3\), all holes except possibly the unique radius-zero source's column satisfy \(z_x=0\) and hence \(a_x+b_x\ge3\). Thus

\[
 |X|\le W+1,\qquad n\le(k-1)^2+1.\tag{3}
\]

A separate initial-round check is necessary: if \(k=2\) and \(m=3\), the radius-one source covers one full column and, in any other column, at most its own row. Adding the radius-zero source can cover at most a second row in one other column. No other column can have all three rows covered. Hence \(n\le1\) whenever \(k=2\), for \(m=3\). Also \(k=1\) cannot burn a clique of order at least three.

**3. Sharp constructions.** For any \(m\ge4\) and \(k\ge2\), partition the \((k-1)^2\) columns consecutively into intervals of lengths \(2r-1\), one for each \(r=1,\ldots,k-1\). Place the radius-\(r\) source in row one at the midpoint of its assigned interval. The entire interval is covered. Place the final radius-zero source arbitrarily. This gives \(n=(k-1)^2\), with equality in (2).

For \(m=3\) and \(k\ge3\), begin with a radius-two source at column 2 of row 1, a radius-one source at column 5 of row 2, and a radius-zero source at column 4 of row 3. The radius-two ball fills columns 1–3 and reaches row 1 of column 4. The radius-one ball fills column 5 and reaches row 2 of column 4. The radius-zero source covers row 3 of column 4. Thus five columns are covered with radii two, one, zero. For every additional radius \(r=3,\ldots,k-1\), tile the consecutive columns beginning at column 6 with an interval of length \(2r-1\) and place its source at that interval's midpoint (row 1). The total number of columns covered is

\[
 5+\sum_{r=3}^{k-1}(2r-1)=(k-1)^2+1.
\]

In either construction, for any shorter target path, clip every source column coordinate to the interval \([1,n]\). This operation cannot increase the distance from that source to any vertex of the shorter target graph, so the same radii still cover every target vertex. Finally, a single radius-one source burns \(K_3\) in two rounds. The constructions and bounds (2)–(3) prove the theorem and every boundary case.

## Verification

The file `verify.py` is a standalone Python 3, standard-library-only consistency checker. It tests 236 constructed maximal-length witnesses with several shorter truncations, independently solves 30 small instances by exact graph-ball dynamic search, and evaluates 891 endpoint-overlap budget cases from independently placed full intervals. Running `python3 verify.py` prints `VERIFY_OK 236 constructive infinite-family witness samples; 30 independent exact burning instances; 891 endpoint-budget instances` when all assertions pass. These finite tests are supplementary: the proof above establishes the result for every integer \(m\ge3,n\ge1\).

## Relationship to prior work

Mitsche, Prałat and Roshanbin [1, Section 3.1, Theorem 7] established general Cartesian-product burning bounds; in the present setting they yield \(\lceil\sqrt n\rceil\le b(K_m\square P_n)\le\lceil\sqrt n\rceil+1\). The same paper specifically notes equality of the upper bound for radius-one factors and square-order paths. Neither fact gives the exact values for every nonsquare path order, nor the width-three exceptional column. Their Theorem 7 and square-order observation are used as background, not asserted anew.

Antony and collaborators [2] study structural burning bounds, algorithms and hardness; the full accessible original manuscript contains no all-order formula for this clique–path family. Existing tabulated results for the ladder \(K_2\square P_n\) [3] concern a different width; the present theorem deliberately starts at \(m=3\). A targeted comparison found no equivalent all-parameter formula in the inspected accessible literature. This negative search is not a guarantee of publication priority.

## Limitations

The claim concerns ordinary vertex burning, not 2-burning, edge burning, total burning or the strong graph product. No result is claimed for clique width two, for cyclic base factors, or for arbitrary radius-one graph factors in place of cliques. The explicit proof establishes the theorem independently of the finite verifier. The earlier product paper's author-hosted PDF was identified but was not retrieved as a whole; the primary published text's relevant theorem and surrounding Section 3.1 were compared from accessible indexed material. Unindexed equivalent results remain a priority risk. Independent mathematical audit has not been performed.

## References

[1] D. Mitsche, P. Prałat and E. Roshanbin, *Burning number of graph products*, Theoretical Computer Science 746 (2018), 124–135. DOI: 10.1016/j.tcs.2018.06.036. Relevant comparison: Section 3.1, Theorem 7 and the following square-order observation. An author-hosted open copy is indexed at `https://math.torontomu.ca/~pralat/papers/2018_graph_products.pdf`.

[2] D. Antony, A. Das, S. Gosavi, D. Jacob and S. Kulamarva, *Graph Burning: Bounds and Hardness*, arXiv:2402.18984v1, first publicly posted 2024-02-29, `https://arxiv.org/abs/2402.18984`.

[3] E. W. Weisstein, *Burning Number*, MathWorld, `https://mathworld.wolfram.com/BurningNumber.html`, tabulated ladder-graph background (secondary reference, not a novelty certificate).
