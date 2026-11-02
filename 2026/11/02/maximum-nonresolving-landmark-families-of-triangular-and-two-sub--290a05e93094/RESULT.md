# Maximum nonresolving landmark families of triangular and two-subset Kneser graphs

## Finding

A landmark set is **resolving** if each pair of distinct graph vertices has different distances to at least one landmark; otherwise it is **nonresolving**. Its **universal resolving threshold** \(\operatorname{th}(G)\) is the least \(t\) such that every \(t\)-element landmark set resolves. For the triangular graph \(T_n=J(n,2)=L(K_n)\), on the two-subsets of \([n]\), the exact threshold is
\[
\operatorname{th}(T_n)=\begin{cases}5,&n=4,5,\\\binom{n-2}{2}+2,&n\ge6.\end{cases}
\]
All inclusion-maximal nonresolving sets admit a simple graph-theoretic classification. Regard vertices of \(T_n\) as edges of the root \(K_n\), and write \(\binom X2\) for all unordered pairs from \(X\).

**Type A:** For any two-element subset \(B=\{b,c\}\) of \([n]\), let
\[
A_B=\binom{[n]\setminus B}{2}\cup\{B\}.
\]
As a root-edge set, \(A_B\) is a clique \(K_{n-2}\) plus a disjoint edge \(K_2\). Its size is \(\binom{n-2}{2}+1\).

**Type D:** For a four-element subset partitioned into two unordered two-element blocks \(P\mid Q\), let
\[
D_{P\mid Q}=\{\{p,q\}:p\in P,\ q\in Q\}\cup\binom{[n]\setminus(P\cup Q)}2.
\]
Its root-edge graph is \(C_4\) disjoint from \(K_{n-4}\), where \(K_1\) means an isolated vertex. Its size is \(4+\binom{n-4}{2}\).

The inclusion-maximal nonresolving sets and their counts are exactly:

| Range | Inclusion-maximal types | Count |
| --- | --- | ---: |
| \(n=4\) | Type D | \(3\) |
| \(n=5\) | Types A and D | \(25\) |
| \(n=6\) | Type A | \(15\) |
| \(n\ge7\) | Types A and D | \(\binom n2+3\binom n4\) |

The **maximum-cardinality** nonresolving sets (the sharp threshold obstructions) are Type D for \(n=4\), both types for \(n=5\), and Type A for \(n\ge6\). Their exact counts are \(3\), \(25\), and \(\binom n2\), respectively. For every \(n\ge5\), the Kneser graph \(KG(n,2)\) has precisely these same families, threshold, and counts.

## Assumptions and scope

The graphs are finite, simple, unweighted, and use shortest-path distance. The triangular-graph conclusion applies for each integer \(n\ge4\). The connected two-subset Kneser conclusion applies for each integer \(n\ge5\); \(KG(4,2)\) is disconnected and is not included. Here \(\operatorname{th}(G)\) is a worst-case property of **every** landmark subset of the prescribed cardinality, not the usual minimum cardinality \(\dim(G)\) of **some** resolving subset. A set is inclusion-maximal nonresolving if no strictly larger vertex subset is nonresolving.

## Proof

**1. Every failure is contained in a distance bisector.** For vertices \(X,Y\) of a connected graph, put \(E(X,Y)=\{W:d(W,X)=d(W,Y)\}\). A landmark set fails to resolve precisely when it is contained in \(E(X,Y)\) for some distinct \(X,Y\). Thus inclusion-maximal nonresolving sets are exactly inclusion-maximal members among these bisectors. For \(T_n\), the distance formula is \(d(X,Y)=2-|X\cap Y|\), so equality of distances is equality of intersection cardinalities.

**2. Every bisector has Type A or Type D.** If \(X=\{a,b\}\) and \(Y=\{a,c\}\), then \(|W\cap X|=|W\cap Y|\) if and only if \(W\) contains both or neither of \(b,c\). Since \(|W|=2\), this is precisely \(A_{\{b,c\}}\). If \(X=P\) and \(Y=Q\) are disjoint two-element sets, then equality requires \(W\) to contain exactly one point from each, or none of their four points. This is precisely \(D_{P\mid Q}\). There are no other pair-intersection types.

**3. The threshold and maximum-cardinality obstruction counts.** Their sizes differ by
\[
|A_B|-|D_{P\mid Q}|=2(n-5).
\]
Hence the maximum bisector size is \(4\) at \(n=4\); \(4\) at \(n=5\); and \(\binom{n-2}{2}+1\) for \(n\ge6\). Every set one larger than the largest bisector resolves, whereas a largest bisector itself does not. This proves the threshold formula. There are \(\binom n2\) distinct Type A sets for \(n\ge5\): the two-element component uniquely recovers \(B\). There are \(3\binom n4\) distinct Type D sets: its four-cycle component and its bipartition into two opposite pairs uniquely recover \(P\mid Q\). At \(n=5\), Type A and D have different root-edge structures \(K_3\sqcup K_2\) versus \(C_4\sqcup K_1\), so all \(10+15=25\) are distinct maximum obstructions. At \(n=4\), only the three Type D sets have the maximum size.

**4. Inclusion-maximal failures, including the smaller obstructions.** Containment of a Type D set in a Type A set means its root-edge graph has no edge crossing a two-point cut \(B\mid([n]\setminus B)\). Equivalently, \(B\) is the vertex union of connected components of \(C_4\sqcup K_{n-4}\). For \(n\ge5\), this is possible only when \(n=6\): the component \(K_{n-4}\) is then \(K_2\), giving \(D_{P\mid Q}\subsetneq A_{[n]\setminus(P\cup Q)}\). For \(n\ge7\), the component sizes are \(4\) and at least \(3\), so no two-point union exists. At \(n=5\), the Type A and D sets have equal cardinalities but different structures and so cannot contain one another. At \(n=4\), every Type A set is a two-edge matching contained in a four-cycle Type D set. For \(n\ge6\), a Type A set cannot be contained in any Type D set because it has strictly larger cardinality. This proves every inclusion-maximal-family assertion and its count.

**5. Kneser transfer.** For \(n\ge5\), the graphs \(T_n\) and \(KG(n,2)\) have identical vertices, complementary adjacency, and diameter two. For any three pairwise distinct vertices \(X,Y,W\), their positive distances satisfy \(d_{KG}(W,X)=3-d_T(W,X)\) and \(d_{KG}(W,Y)=3-d_T(W,Y)\), hence their equality relations coincide. If \(W=X\) or \(W=Y\), one compared distance is zero and the other positive in either graph, so equality fails in both. Consequently **every** pair bisector, and therefore **every** resolving and nonresolving vertex subset, is identical in the two graphs.

## Verification

The included standalone file `verify_threshold.py` independently constructs both graph adjacencies, derives all-pairs shortest-path distances by breadth-first search, enumerates every pair bisector, and compares all inclusion-maximal bisectors against the stated families. It also independently tests the definition of resolving for every landmark subset on the small graphs. Executing `python3 verify_threshold.py` completes with `VERIFY_OK` for \(4\le n\le10\) in the triangular case and \(5\le n\le10\) in the Kneser case. The infinite proof is the preceding five-step structural argument; the finite checks are consistency checks, not an extrapolation.

## Relationship to prior work

Korivand, Khashyarmanesh and Tavakoli (2022) introduced the universal metric-dimension threshold and proved \(\operatorname{th}(KG(5,2))=5\) for the Petersen graph. This result extends that finite calculation to all two-subset Kneser graphs and simultaneously to all triangular graphs, while classifying **all** maximal failures and counting the largest failures. Bailey and collaborators (2013) determine ordinary metric dimension and study constructions of resolving sets for Johnson and Kneser graphs; ordinary metric dimension is a different minimization problem. In particular the ordinary dimension of \(J(n,2)\) grows linearly with \(n\), whereas the universal threshold here grows quadratically. Kratica, Čangalović and Kovačević-Vujčić (2024) study equidistant dimension of these graph families, where **each exterior pair must have some equal-distance landmark**; their opposite quantifier does not give universal-resolving thresholds or the classification above. The distance-bisector vocabulary and the diameter-two complement relation are previously known and are not claimed as new.

## Limitations

The theorem does not give the ordinary metric dimension, nor the number of all resolving subsets of every size. It does not address \(J(n,k)\) for \(k\ge3\) or disconnected \(KG(4,2)\). The literature comparison supports but cannot guarantee publication priority; an earlier exact obstruction classification under alternative terminology may exist. Only the stated properties are proved, and the verification range is finite.

## References

- M. Korivand, K. Khashyarmanesh, M. Tavakoli, *Metric Dimension Threshold of Graphs*, Journal of Mathematics (2022), article 1838719, DOI: 10.1155/2022/1838719 (first public version September 14, 2022).
- R. F. Bailey, J. Cáceres, D. Garijo, A. González, A. Márquez, K. Meagher, M. L. Puertas, *Resolving sets for Johnson and Kneser graphs*, European Journal of Combinatorics 34 (2013), 736–751; arXiv:1203.2660 (first posted March 12, 2012).
- J. Kratica, M. Čangalović, V. Kovačević-Vujčić, *Equidistant dimension of Johnson and Kneser graphs*, arXiv:2406.17870 (first posted June 25, 2024).
