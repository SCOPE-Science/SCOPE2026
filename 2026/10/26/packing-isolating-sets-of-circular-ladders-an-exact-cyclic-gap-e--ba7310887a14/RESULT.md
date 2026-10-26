# Packing-isolating sets of circular ladders: an exact cyclic-gap enumeration

## Finding

Let \(P_n=C_n\square K_2\) be the simple circular ladder with \(n\ge3\) labeled columns. A **packing-isolating set** is a subset \(S\subseteq V(P_n)\) whose distinct vertices have disjoint closed neighborhoods and for which the graph induced by \(V(P_n)\setminus N[S]\) has no edges. Write \(i_{n,k}\) for the number of such sets of size \(k\), and set \(I_n(u)=\sum_k i_{n,k}u^k\).

**Structural characterization.** Every packing-isolating set consists of \(k\ge2\) selected vertices occupying different columns. In clockwise order the gaps between consecutive selected columns are all \(2\) or \(3\), and their row coordinates alternate at every step. Conversely, every such choice is packing-isolating. Consequently \(k\) is even, and
\[
 i_{n,k}=
 \begin{cases}
 \displaystyle\frac{2n}{k}\binom{k}{n-2k},&k\ge2\text{ even and }2k\le n\le3k,\\[4pt]
 0,&\text{otherwise}.
 \end{cases}
\]
In particular, for all integers \(n\ge3\),
\[
 \boxed{\displaystyle
 \sum_{n\ge3}I_n(u)t^n
 =\frac{2tu^2(t^2+t^3)(2t+3t^2)}{1-u^2(t^2+t^3)^2}.}
\]
Such a set exists exactly when \(n\ge4\) and \(n\ne7\). Whenever one exists, the minimum and maximum sizes of packing-isolating sets are respectively \(2\lceil n/6\rceil\) and \(2\lfloor n/4\rfloor\), and every even size between these two values occurs.

Setting \(u=1\), the total-count series is
\[
 \sum_{n\ge3}I_n(1)t^n
 =\frac{4t^4+10t^5+6t^6}{1-t^4-2t^5-t^6}.
\]
For \(n=3,4,\ldots,14\) the counts are \(0,4,10,6,0,4,18,30,22,10,26,70\). For \(n\ge7\), with lower subscripts treated as zero, the total counts satisfy \(I_n(1)=I_{n-4}(1)+2I_{n-5}(1)+I_{n-6}(1)\).

## Assumptions and scope

All graphs are finite, simple, undirected, and the cycle \(C_n\) has \(n\ge3\) vertices. The graph \(P_n\) has vertex set \(\{(j,r):j\in\mathbb Z/n\mathbb Z,\ r\in\{0,1\}\}\); two vertices are adjacent exactly when they have equal row and cyclically adjacent columns or equal column and different rows. Columns are labeled, rows are distinguished, and subsets are counted without quotienting by rotations or reflections. The closed neighborhood of a set is the union of its vertices and all their neighbors. Empty sets do not qualify since \(P_n\) has edges.

## Proof

**Step 1: at most one selection per column, and no adjacent selected columns.** Two vertices in one column are adjacent, while two vertices in adjacent columns are at distance at most two (even when in opposite rows). Each is impossible for a packing. Suppose selected columns \(a,b\) are consecutive in clockwise order and their forward gap is \(d\). Necessarily \(d\ge2\).

**Step 2: rule out a gap of four or more.** If \(d\ge4\), neither vertex of column \(a+2\) is in \(S\) or adjacent to any vertex of \(S\): its own and neighboring columns \(a+1,a+2,a+3\) have no selections. Thus both rung endpoints in that column are outside \(N[S]\), contradicting isolation. This applies even with only one selected column when \(n\ge4\).

**Step 3: rule out equal rows across either allowed gap.** When \(d=2\), same-row selected vertices are at distance two, contradicting packing. When \(d=3\), same-row selected vertices leave the opposite-row vertices of columns \(a+1,a+2\) outside \(N[S]\); those two vertices form an edge. Therefore the rows must differ across every gap. With a single selected vertex on \(P_3\), the two other vertices in its opposite row remain adjacent and undominated, so this final boundary case fails as well. We have proved that every packing-isolating set has at least two selections, gaps in \(\{2,3\}\), and alternating rows; in particular their number \(k\) is even.

**Step 4: prove sufficiency.** Conversely, suppose \(k\ge2\) is even and cyclically consecutive selected columns have gaps \(2\) or \(3\) with alternating selected rows. Different selections are at graph distance at least three: for neighboring selected columns a gap of two uses different rows and therefore has graph distance three; more remote pairs are separated by at least four columns along either route unless they are neighboring in the cyclic selection order. Thus \(S\) is a packing. A gap of two has its sole interior column completely dominated by its two endpoint selections (one from each row). A gap of three has two interior columns, each with one undominated vertex; these two vertices lie in different rows, so they are nonadjacent. A selected column is completely dominated. No undominated vertices in different gaps can be adjacent, because selected columns lie between the gaps. Thus \(P_n-N[S]\) is edgeless.

**Step 5: count.** Fix even \(k\ge2\). Every gap contributes either two or three to the column count; exactly \(q=n-2k\) of the \(k\) gaps must be three. The possible gap words number \(\binom{k}{q}\) if \(0\le q\le k\), and none otherwise. Mark a starting selected column in \(n\) ways and its row in two ways. The alternating row assignment closes consistently because \(k\) is even. Every set obtained is represented exactly \(k\) times, one per choice of distinguished selected column. Hence the coefficient formula.

For the bivariate generating function, put \(f(t)=t^2+t^3\). The marked cyclic-word count yields
\[
 \sum_{n\ge3}I_n(u)t^n
 =2t\frac{d}{dt}\sum_{\substack{k\ge2\\k\text{ even}}}\frac{u^k f(t)^k}{k}
 =2t\frac{u^2 f(t)f'(t)}{1-u^2f(t)^2}.
\]
Substituting \(f(t)\) gives the stated rational function. With \(u=1\), its denominator supplies the recurrence. Finally, the admissible even selection counts satisfy \(2k\le n\le3k\). They exist for \(n=4,5,6\), not for \(n=3,7\), and cover every integer \(n\ge8\) since the intervals for even \(k\ge4\) overlap. The least and greatest admissible even values are \(2\lceil n/6\rceil\) and \(2\lfloor n/4\rfloor\); all intervening even values obey the same inequalities.

## Verification

A standalone Python checker constructs the two-layer cyclic graph from adjacency rules, recursively enumerates all two-packings by an independently generated distance-two conflict mask, and tests whether the vertices outside their closed neighborhoods induce an edge. It compares the complete size distribution against the stated binomial formula for every \(3\le n\le21\). For every \(3\le n\le14\), it also compares the actual accepted vertex-set masks to a separate enumerator based solely on the gap characterization. The generating-function recurrence is checked against the formula through \(n=120\) with integer arithmetic. The recorded output ends with `RECURRENCE_120_OK` and `VERIFY_OK`.

To replay, run `python3 verify.py` from the directory containing `verify.py`; no nonstandard Python packages or external data files are required. These finite checks are corroboration, not the proof for unbounded \(n\), which is Steps 1–5 above.

## Relationship to prior work

Boyer, Goddard and Henning (2026) introduce packing-isolating sets explicitly, prove that every tree admits one, give graph families without one, and establish decision hardness. Their results do not yield the cyclic-gap classification or enumerator for the cubic circular ladders. Brešar, Klavžar and Rall (2023) consider ordinary two-packings and open packings in prism products; they do not impose the additional vertex-edge isolation condition, so their prism-packing equality does not imply this enumeration. The distance-packing domination work of Bujtás, Iršič Chenoweth, Klavžar and Zhang (2025/2026) uses distance domination, a different constraint that is weaker than edge isolation for the relevant radius, and determines conditions for cycles rather than circular ladders.

## Limitations

This theorem concerns only simple labeled circular ladders with at least three columns, not arbitrary prisms, Möbius ladders, or graphs of larger width. It does not compute the isolation number or the packing number separately, and does not claim a complete theory of packing-isolating sets on cubic graphs. The available literature searches did not identify a prior equivalent exact enumeration, but unindexed or differently formulated prior work is a residual bibliographic possibility.

## References

1. G. Boyer, W. Goddard, and M. A. Henning, *On the Relationships between Domination, Isolation, and Packing*, arXiv:2606.18172v1, first submitted 2026-06-16. https://arxiv.org/html/2606.18172
2. B. Brešar, S. Klavžar, and D. F. Rall, *Packings in bipartite prisms and hypercubes*, arXiv:2309.04963v1, first submitted 2023-09-10. https://arxiv.org/pdf/2309.04963
3. C. Bujtás, V. Iršič Chenoweth, S. Klavžar, and G. Zhang, *The d-distance p-packing domination number: complexity, cycles, and trees*, arXiv:2507.18272, first submitted 2025-07-24; Aequationes Mathematicae 100 (2026), Article 25. https://arxiv.org/abs/2507.18272
