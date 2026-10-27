# A 34-landmark counterexample at \(GP(25,2)\)

## Finding
For the generalized Petersen graph \(G=GP(25,2)\), the strong metric dimension is exactly
\[
\operatorname{sdim}(G)=34.
\]
In particular, the proposed equality \(\operatorname{sdim}(GP(4k+1,2))=5k+5\) for all \(k\ge5\), explicitly stated in the conclusion of Kratica–Kovačević-Vujčić–Čangalović [1], fails at \(k=6\), where it predicts \(35\). This is a counterexample to a conjectural equality, not to their proved upper bound.

## Assumptions and scope
The graph has outer vertices \(u_i\) and inner vertices \(v_i\), indexed by \(i\in\mathbb Z/25\mathbb Z\), with edges \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+2}\). Graph distance is the ordinary shortest-path distance \(d\). A vertex \(w\) *strongly resolves* distinct vertices \(a,b\) if \(d(a,w)=d(a,b)+d(b,w)\) or \(d(b,w)=d(a,b)+d(a,w)\). The strong metric dimension is the minimum size of a vertex set strongly resolving all unordered vertex pairs.

Two vertices \(a,b\) are *mutually maximally distant* (MMD) when every neighbor of \(a\) is at distance at most \(d(a,b)\) from \(b\), and every neighbor of \(b\) is at distance at most \(d(a,b)\) from \(a\). Let \(H\) be the graph on these fifty vertices with an edge for each MMD pair. For a residue \(j\), write \(\lVert j\rVert_{25}=\min\{j\bmod25,(-j)\bmod25\}\).

## Proof
**1. The MMD graph.** Translation and reflection reduce the distance calculation to the following rows, with the columns indexed by \(j=0,1,\ldots,12\):

| Distance | Values at successive \(j\) |
|---|---|
| \(d(u_0,u_j)\) | 0, 1, 2, 3, 4, 5, 5, 6, 6, 7, 7, 8, 8 |
| \(d(v_0,v_j)\) | 0, 3, 1, 4, 2, 5, 3, 6, 4, 7, 5, 7, 6 |
| \(d(u_0,v_j)\) | 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7 |

These are ordinary graph distances, obtainable by breadth-first search on the three displayed edge types. Comparing the distance of each vertex to the three neighbors of the other vertex, and then applying translation/reflection, gives the **complete** MMD adjacency characterization:
\[
\begin{aligned}
u_i u_j\in E(H)&\iff \lVert i-j\rVert_{25}\in\{5,7,9,11,12\},\\
v_i v_j\in E(H)&\iff \lVert i-j\rVert_{25}\in\{9,11\},\\
u_i v_j&\notin E(H)\quad\text{for all }i,j.
\end{aligned}
\]
The resulting MMD graph has \(125\) outer–outer edges and \(50\) inner–inner edges and no mixed edges. The companion verifier reconstructs these relations independently from all shortest-path distances, rather than using the displayed offset sets as its definition.

**2. Outer omission bound.** In any independent set of the outer component of \(H\), translate a chosen vertex to \(u_0\). Its remaining indices must lie in
\[
A=\{1,2,3,4,6,8,10,15,17,19,21,22,23,24\}.
\]
This set is partitioned into five cliques of the outer MMD graph:
\[
\{1,6,19\},\quad\{2,15,22\},\quad\{3,8,21\},\quad\{4,17,24\},\quad\{10,23\}.
\]
Indeed every pair in each displayed group has cyclic distance in \(\{5,7,9,11,12\}\). At most one vertex from each clique can be added to \(u_0\), hence the outer component has independence number at most \(6\). Equality is attained by \(\{u_0,u_2,u_4,u_6,u_8,u_{10}\}\).

**3. Inner omission bound.** For \(t=0,1,2,3,4\), define
\[
C_t=\{v_{5t},v_{5t+9},v_{5t+18},v_{5t+2},v_{5t+11}\},
\]
with indices modulo \(25\), and take the displayed order as a cycle. Four consecutive steps have offset \(+9\) and the closing step has offset \(-11\), so each \(C_t\) is a five-cycle in the inner MMD graph. These five cycles are vertex-disjoint and cover all twenty-five inner vertices: the five positions within \(C_0\) have distinct residues modulo \(5\), and translation by multiples of \(5\) exhausts the corresponding residue classes. Each cycle contributes at most two vertices to any independent set; hence the inner independence number is at most \(10\). Equality is attained by
\[
W=\{v_i:i\bmod5\in\{0,3\}\}.
\]
All inner MMD offsets are congruent to \(\pm1\pmod5\), whereas two residues in \(\{0,3\}\) differ by \(0\) or \(\pm2\pmod5\).

**4. Lower and upper bounds.** Every strong resolving set contains at least one endpoint of each MMD pair. For if \(a,b\) are MMD and both absent, a third vertex \(w\) resolving \(a,b\) would force a shortest path to continue from one endpoint in a direction strictly farther from the other, contradicting maximal distance. Thus the omitted vertices form an independent set of \(H\). Since \(H\) has disjoint outer/inner components, at most \(6+10=16\) vertices can be omitted, and every strong resolving set has at least \(50-16=34\) vertices.

Let
\[
U=\{u_0,u_2,u_4,u_6,u_8,u_{10}\},\qquad W=\{v_i:i\bmod5\in\{0,3\}\},
\]
and put \(S=V(G)\setminus(U\cup W)\). Both sets are independent in their respective MMD components, and there are no mixed MMD edges, so \(S\) is a vertex cover of \(H\). The strong-resolving-graph theorem of Oellermann and Peters-Fransen [2] therefore makes \(S\) a strong resolving set. Independently of that theorem's converse, the attached finite verifier checks the shortest-path betweenness condition directly for all \(\binom{50}{2}=1225\) unordered pairs using \(|S|=34\). Therefore the lower bound is attained and \(\operatorname{sdim}(G)=34\).

## Verification
Run `python3 verify_gp25.py` with a standard Python 3 interpreter. The script constructs the 50-vertex graph using only its adjacency definition, computes distances by both breadth-first search and Floyd–Warshall relaxation, tests every MMD pair against the offset description, validates the five clique groups and five disjoint five-cycles, checks the sixteen-vertex independent omission set, and directly checks all 1225 strong-resolution requirements. It exits with `VERIFY_OK` when every assertion succeeds. No external graph or optimizer package is required.

## Relationship to prior work
Kratica, Kovačević-Vujčić, and Čangalović [1, Section 2, Corollary 1] proved the upper bound \(\operatorname{sdim}(GP(4k+1,2))\le5k+5\) for \(k\ge3\). Their conclusion conjectures equality for \(k\ge5\), while their exact computational table stops at \(n\le19\). The present result gives \(34<35\) at \(n=25\) and supplies a structural minimum-size proof. The general vertex-cover reduction [2] makes the finite argument possible but does not determine the particular MMD graph or its independence number. Raza and Ji [3] study **mixed** metric dimension, defined by distinguishing vertices and edges; that is a different invariant and does not imply this strong metric dimension value.

## Limitations
The exact conclusion concerns only \(GP(25,2)\); it does not establish a corrected formula for all \(GP(4k+1,2)\), or uniqueness of the exceptional parameter. The result relies on the stated finite MMD table, which is completely reproducible from the edge definition and checked by independent shortest-path routines. The literature comparison cannot exclude unindexed earlier computational results. No external independent mathematical audit has been performed.

## References
[1] J. Kratica, V. Kovačević-Vujčić, M. Čangalović, *The strong metric dimension of some generalized Petersen graphs*, arXiv:1507.00881 (first public version 2015-07-03); *Applicable Analysis and Discrete Mathematics* 11 (2017), 1–10, DOI:10.2298/AADM161110032K.

[2] O. R. Oellermann and J. Peters-Fransen, *The strong metric dimension of graphs and digraphs*, *Discrete Applied Mathematics* 155 (2007), 356–364, DOI:10.1016/j.dam.2006.06.009.

[3] H. Raza and Y. Ji, *Computing the Mixed Metric Dimension of a Generalized Petersen Graph P(n, 2)*, *Frontiers in Physics* 8 (2020), article 211, DOI:10.3389/fphy.2020.00211.
