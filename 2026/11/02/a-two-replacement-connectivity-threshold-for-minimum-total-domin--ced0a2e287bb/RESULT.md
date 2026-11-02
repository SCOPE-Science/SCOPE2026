# A two-replacement connectivity threshold for minimum total dominating sets of the five-cube

## Finding
Let \(Q_5\) be the graph on \(\mathbb F_2^5\) with edges at Hamming distance one. Call \(S\subseteq V(Q_5)\) *total dominating* if every vertex has a neighbor in \(S\), including the vertices belonging to \(S\). Write \(\mathcal M\) for its family of minimum total dominating sets. For \(r=1,2\), let \(\mathcal R_r\) be the graph on \(\mathcal M\) in which two different sets are adjacent precisely when exactly \(r\) vertices are removed and exactly \(r\) other vertices are inserted; thus \(|S\mathbin{\triangle}T|=2r\). Intermediate configurations within one such simultaneous replacement are not required to be feasible.

Define the \(5\)-regular Clebsch graph \(C\) on the even-weight words of \(\mathbb F_2^5\), with edges at Hamming distance four. Define \(H\) to have the \(40\) distinct four-cycles of \(C\) as vertices, adjacent when two cycles share an edge of \(C\). Then:

1. \(\gamma_t(Q_5)=8\), and every member of \(\mathcal M\) is the disjoint union of one four-cycle of \(C\) on the even words and one corresponding four-cycle on the odd words. Consequently \(|\mathcal M|=40^2=1600\). This cardinality and count were previously known and are not claimed as new.
2. \(\mathcal R_1\cong 1600K_1\): **all optimal configurations are frozen under any single-vertex replacement**.
3. \(\mathcal R_2\cong H\square H\). The graph \(H\) has \(40\) vertices, \(240\) edges, valency \(12\), diameter two, and the distance distribution \((1,12,27)\) from every vertex. Consequently \(\mathcal R_2\) is connected, \(24\)-regular, has \(1600\) vertices, \(19200\) edges, diameter four, and distance distribution
\[
(1,24,198,648,729)
\]
from every vertex, in distances zero through four, respectively.

In particular, the minimum permitted number of simultaneous arbitrary vertex replacements needed to connect *all* optimal total dominating sets is exactly two. The substantive claim is the complete one-/two-replacement exchange geometry, not the known static optimum or number of optima.

## Assumptions and scope
All graphs are finite, undirected and simple, and selected sets consist of distinct vertices. One move in \(\mathcal R_2\) replaces exactly two vertices, not at most two; vertex positions are unrestricted, and no feasibility condition is imposed between removal and insertion inside one move. Every endpoint of a move must remain a minimum total dominating set. The Clebsch graph here is specifically the \(5\)-regular graph with adjacency at Hamming distance four, *not* its \(10\)-regular complement. The result concerns the fixed graph \(Q_5\); no assertion is made for higher-dimensional cubes.

## Proof
**1. Minimum total domination reduces to two four-point covers.** Let \(E,O\) denote the \(16\) even- and \(16\) odd-weight vertices of \(Q_5\). Each vertex has exactly five neighbors, all in the other parity class. Every total dominating set therefore contains at least \(\lceil16/5\rceil=4\) vertices of each parity. If each class is covered by the neighbors of four selected vertices of the opposite parity, these independent selections form an eight-vertex total dominating set. We now classify every such four-cover.

**2. Four-covers are precisely Clebsch quadrangles.** Translation by an even word acts on \(E\), preserves the covering condition and fixes the parity classes. Translate a four-cover \(A\subset E\) to arrange \(0\in A\). Write \(w_i\) for the weight-four word whose unique zero coordinate is \(i\); write \(e_i+e_j\) for the weight-two word supported on \(\{i,j\}\). Of the other three elements of \(A\), let \(k\) have weight four. The odd weight-five word must be covered, so \(k\ge1\).

If \(k=1\), the single \(w_i\) covers the four odd weight-three words *not* containing \(i\), leaving the six triples containing \(i\). A weight-two word containing \(i\) covers exactly three of those six triples; one not containing \(i\) covers at most one. Both remaining weight-two words must therefore contain \(i\), and then their three-element supersets overlap, so they cover at most five of the six. Impossible.

If \(k=2\), the two distinct words \(w_i,w_j\) leave exactly the three odd weight-three words containing both \(i\) and \(j\). The remaining weight-two word must be \(e_i+e_j\), which covers all three. These choices do cover all odd vertices (the zero word covers the five weight-one words, and the weight-five word is covered by either weight-four word). Thus the only four-covers through zero are
\[
\{0,w_i,w_j,e_i+e_j\},\qquad 1\le i<j\le5.
\]
If \(k=3\), the odd weight-three word supported by the three omitted coordinates is adjacent to none of the selected words. Impossible.

The graph \(C\) is triangle-free, and nonadjacent pairs have precisely two common neighbors: from zero, its neighbors are the five \(w_i\), whereas for a weight-two word \(e_i+e_j\) the common neighbors are exactly \(w_i,w_j\). Hence the displayed four-sets are four-cycles in \(C\), and conversely every four-cycle containing zero has this form. Translation gives the classification for every center. There are ten four-cycles through each of the sixteen even vertices; dividing vertex incidences by four gives \(40\) four-cycles in \(C\). The odd parity class is an isomorphic translate, independently yielding another \(40\) possibilities. This proves the first assertion.

**3. No single replacement is legal.** Two different four-cycles in a triangle-free graph with exactly two common neighbors per nonadjacent pair can never share three vertices: any three vertices of a four-cycle contain an opposite (nonadjacent) pair, and that pair uniquely determines both common neighbors and hence the cycle. To preserve four selected vertices in each parity class, a one-vertex replacement must occur entirely in one parity class. It would require distinct four-cycles sharing three vertices, which is impossible. Thus \(\mathcal R_1\) has no edges.

**4. Exactly two replacements factor through edge-sharing four-cycles.** Two minimum sets have equal counts of even and odd vertices. If two removed vertices have different parities, the two inserted vertices must likewise have different parities. Such a move would replace a single vertex in each of the two four-cycles, contradicting step 3. Every legal two-replacement move therefore acts within one parity class. Distinct four-cycles may share two vertices only when those vertices are adjacent: if opposite, their unique two common neighbors would determine the same cycle. Accordingly, replacing two vertices of a four-cycle to obtain another is possible precisely when the cycles share an edge. This is the adjacency of \(H\) on one factor with the other factor fixed, proving \(\mathcal R_2\cong H\square H\).

**5. Exact finite incidence lemma and metric.** In \(C\), each edge lies in exactly four four-cycles. For an edge incident to \(0\) and \(w_i\), choose the second neighbor \(w_j\) of \(0\) from the four indices \(j\ne i\); its second common neighbor with \(w_i\) is \(e_i+e_j\). Thus exactly four quadrangles contain that edge. By edge transitivity under even translations and coordinate permutations the same holds for every edge. No two different quadrangles share more than one edge, by step 3. Each quadrangle has four edges, each lying in three other quadrangles, hence \(H\) is \(12\)-regular and has \(40\cdot12/2=240\) edges.

For completeness, here is a finite exact incidence certificate for its diameter. Label the vertices of \(C\) by \(z\), \(a_i\) for \(1\le i\le5\), and \(b_{ij}\) for \(1\le i<j\le5\), with corresponding binary words \(0\), \(w_i\), and \(e_i+e_j\). All forty quadrangles are explicitly
\[
\{z,a_i,a_j,b_{ij}\}\quad(i<j),
\]
and
\[
\{a_i,b_{ij},b_{ik},b_{\ell m}\},\quad
\{j,k\}\subseteq[5]\setminus\{i\},\ j<k,\quad
\{\ell,m\}=[5]\setminus\{i,j,k\}.
\]
There are ten of the first and thirty of the second. The standalone program `verify_clebsch.py` builds these forty sets independently, checks them against the binary-vector enumeration, compares all \(\binom{40}{2}=780\) pairs, and verifies that every nonadjacent pair of quadrangles has at least one common edge-sharing neighbor in \(H\). Its exact pair census is: 240 adjacent pairs (four common neighbors), 240 nonadjacent pairs with two common neighbors, and 300 nonadjacent pairs with four common neighbors. These integer loops are exhaustive over the explicitly listed finite objects, so this is an exact finite proof of the incidence lemma, not statistical evidence. Consequently \(H\) has diameter two and, from every quadrangle, one vertex at distance zero, twelve at distance one, and the other twenty-seven at distance two.

Distances in the Cartesian product add. Squaring the distance generating polynomial gives
\[
(1+12t+27t^2)^2=1+24t+198t^2+648t^3+729t^4.
\]
The degree, number of edges, connectedness, diameter, and optimal two-replacement threshold now follow.

## Verification
Two complete standalone programs are included: `verify_clebsch.py` (Python 3, standard library) and `verify_direct.cpp` (C++17, standard library). Run `python3 verify_clebsch.py`; compile the second with `g++ -O3 -std=c++17 verify_direct.cpp -o verify_direct` and run `./verify_direct`. The first separately checks the Clebsch four-cover classification, all forty explicit quadrangles, the 780-pair incidence lemma, all 40 breadth-first distance profiles, and the Cartesian-product distance distribution. The second does not construct the Clebsch graph: it tests all \(\binom{32}{8}=10{,}518{,}300\) eight-sets directly against the open-neighborhood total domination condition, then constructs every one- and two-replacement possibility and checks all 1600 all-source distance profiles. Both checks complete successfully. In the mathematical argument, the lower bound for sizes below eight is proved separately, not inferred from eight-subset enumeration.

## Relationship to prior work
Azarija, Henning, and Klavžar prove the prism identity for total domination and obtain the previously known minimum for hypercubes. OEIS A323515 already records the 1600 minimum total dominating sets of \(Q_5\). The standard Clebsch graph data already give the \((16,5,0,2)\) parameters and forty quadrangles. None of those static assertions is claimed as new. Alikhani, Fatehi, and Mynhardt study total domination reconfiguration by *adding or deleting* a single vertex in sets bounded by a parameter; this is different from fixed-optimum simultaneous replacement. Křišťan and Svoboda study general generalized token-jumping rules for ordinary domination and related optimization problems; the inspected work does not determine this specific total-domination reconfiguration graph. The focus here is the exact connectivity threshold and complete degree/distance profile for two replacements on \(Q_5\).

## Limitations
The result concerns precisely five dimensions and the stated replacement rules; it does not claim optimality for other hypercubes, a general all-graph reconfiguration theorem, or a result about token *sliding* along original graph edges. The finite incidence lemma has an exhaustive standalone checker whose correctness depends on its explicit definitions and deterministic loops; a noncomputational hand proof of that specific forty-object diameter comparison is not supplied. An equivalent historical reconfiguration analysis under covering-code or square-intersection terminology remains possible. No independent scholarly audit has been performed.

## References
1. J. Azarija, M. A. Henning, S. Klavžar, *\((\text{Total})\) Domination in Prisms*, arXiv:1606.08143v1 (first made public 2016-06-27), https://arxiv.org/abs/1606.08143.
2. OEIS A323515, *Number of minimum total dominating sets in the hypercube graph*, https://oeis.org/A323515.
3. Clebsch graph, graph-data summary distinguishing the \(5\)- and \(10\)-regular conventions, https://jaanos.github.io/tables/graphs/Clebsch.html.
4. S. Alikhani, D. Fatehi, C. M. Mynhardt, *On \(k\)-Total Dominating Graphs*, arXiv:1711.04363, https://arxiv.org/abs/1711.04363.
5. J. M. Křišťan and J. Svoboda, *Reconfiguration Using Generalized Token Jumping*, arXiv:2411.12582, https://arxiv.org/abs/2411.12582.
