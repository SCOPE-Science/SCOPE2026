# Integral homotopy and persistence of the \(3\times4\times4\) Hamming box

## Finding
Let \(B=[3]\times[4]\times[4]\), where \([q]=\{0,\ldots,q-1\}\), with Hamming distance \(d(x,y)=|\{i:x_i\ne y_i\}|\). The inclusive Vietoris--Rips complex on \(B\), denoted \(R_r\), is the simplicial complex of all nonempty finite subsets of diameter at most \(r\). For all real \(r\ge0\),
\[
R_r\simeq
\begin{cases}
\bigsqcup^{48}\{\mathrm{pt}\},&0\le r<1,\\
\bigvee^{57}S^1,&1\le r<2,\\
\bigvee^{198}S^3,&2\le r<3,\\
\{\mathrm{pt}\},&r\ge3.
\end{cases}
\]
In particular, for the *categorical* graph product (adjacency requires every coordinate to differ),
\[
\operatorname{Ind}(K_3\times K_4\times K_4)\simeq\bigvee^{198}S^3.
\]
All reduced integral homology groups in this filtration are free abelian. Its reduced persistence intervals, including endpoint conventions, comprise 47 copies of \([0,1)\) in degree zero, 57 copies of \([1,2)\) in degree one, and 198 copies of \([2,3)\) in degree three, with no others.

## Assumptions and scope
The notation \(K_q\) means the simple complete graph on \(q\) vertices; \(\times\) means the categorical/tensor graph product, **not** the Cartesian graph product \(\square\). The Hamming graph on \(B\) is \(K_3\square K_4\square K_4\). All complexes are ordinary finite abstract simplicial complexes with geometric realization and integral homotopy types. The statement concerns precisely the fixed 48-point box, with no unproved extrapolation to other alphabet sizes. The radius convention is inclusive, so a simplex enters at its exact diameter.

## Proof
**Scales zero and three.** The only distances between distinct points are one, two, and three. Before one there are 48 isolated vertices; from three onward every subset is a simplex.

**Scale one.** A clique in the Hamming graph \(K_3\square K_4\square K_4\) lies in a coordinate line, so \(R_1\) is covered by the simplices corresponding to its 40 coordinate lines: \(4\cdot4+3\cdot4+3\cdot4=40\). The intersection of different coordinate-line simplices is either empty or a single vertex, hence every nonempty intersection is contractible. The nerve theorem identifies \(R_1\) with this cover's nerve. For each of the 48 original vertices, exactly three coordinate lines meet there; they generate one filled triangle in the nerve, and each nerve edge belongs to just one such triangle. Replace each filled triangle by a contractible three-legged star connecting its three line vertices to a new central vertex. This preserves homotopy type and yields a connected bipartite graph with \(40+48=88\) vertices and \(3\cdot48=144\) edges. Thus it has first Betti number \(144-88+1=57\), hence has homotopy type \(\bigvee^{57}S^1\).

**Scale two: identification.** The only forbidden pair at threshold two is a pair of Hamming distance three, i.e. words that differ in *every* coordinate. Those are precisely the edges of \(K_3\times K_4\times K_4\). Therefore \(R_2=\operatorname{Ind}(K_3\times K_4\times K_4)\).

**Scale two: finite, exact acyclic matching.** Index the 48 words lexicographically, from zero through 47. Represent a face \(F\) by its 48-bit integer mask. Enumerate the complete augmented face poset (including the empty face) recursively: from a partial independent face, choose each permissible later vertex, then forbid its graph neighbors. At stages \(v=0,1,\ldots,47\), pair *every still-unpaired* face \(F\) not containing \(v\) with \(F\cup\{v\}\) if both faces remain unpaired. All such pairs are disjoint at a stage and are genuine codimension-one face relations.

The standalone executable `CHECK.py` generates every face and every pair from these definitions, without an external data file. Exact enumerated face counts by cardinality 0 through 16 are

`(1,48,696,4192,12636,23904,35016,42336,43002,36128,24552,13200,5468,1680,360,48,3)`.

Their sum is 243270. The matching consists of 121536 pairs and exactly 198 remaining, unpaired four-vertex faces (three-dimensional simplices). To certify the nonstandard critical property, orient *every* Hasse cover downwards except matched covers, which point upwards. The executable forms the indegree of every one of the 243270 vertices using all 1843680 cover relations, and repeatedly removes indegree-zero vertices, updating **all** their outgoing arrows. Exactly 243270 vertices are removed; hence the directed graph is acyclic. This is a complete finite acyclicity proof, not a random test or a homology-only calculation. It is reproducible from the elementary loop definitions in `CHECK.py`.

The empty face is paired with the first vertex. Omitting the empty face from the ordinary face poset converts its partner into one critical zero-cell; all other pairs persist. The ordinary acyclic matching thus has one zero-cell and 198 three-cells, with no other critical cells. Discrete Morse theory gives a CW homotopy model with exactly these cells. Since every attaching map of a three-cell into a point is null-homotopic, the model is precisely \(\bigvee^{198}S^3\). This proves the integral, rather than merely rational or mod-two, assertion.

**Persistence.** At integer radii the reduced homology is supported respectively in degree zero, one, and three, while all groups vanish at scale three. The induced maps between distinct nonzero degrees are zero, and all groups are free. The barcode above follows exactly, including half-open intervals. No claim of a canonical splitting of chain complexes is needed.

## Verification
Run `python3 CHECK.py` from the directory containing that embedded file. Only the Python standard library is needed. The program constructs all 48 graph vertices and 432 categorical-product edges, recursively enumerates 243270 augmented faces, checks the complete face-cardinality histogram and reduced Euler characteristic, creates 121536 matching pairs, checks all 1843680 Hasse covers, proves acyclicity by a complete topological sort, and checks the scale-one incidence count. Its terminal success marker is `COMPLETE_HAMMING_3_4_4_FILTRATION_VERIFIED`. The program itself, not its output log, is the finite certificate. No external computation or mathematical independence review is claimed.

## Relationship to prior work
Goyal, Shukla and Singh (2019, arXiv:1905.06926, §3) established the two-factor case and proposed a three-factor sphere-wedge phenomenon, computing only binary-factor examples. Antolín Camarena and Carnero Bravo (2023, arXiv:2307.12401, introduction, §4, Proposition 25, and Conjecture 26) proved the three-factor case **when a factor is binary** and explicitly conjectured the general three-complete-factor three-sphere wedge. Their proof uses bipartiteness from the binary factor and does not cover this all-nonbinary \((3,4,4)\) box. An earlier exact \((3,3,3)\) calculation and a distinct \((3,3,4)\) calculation also concern different vertex sets and do not imply the present 48-point result. Here two coordinates have four symbols, making this a natural first two-quaternary-coordinate test of the general conjecture. The scale-one and full persistence description are proved as part of the same finite calculation; no global conjecture is claimed settled.

## Limitations
The homotopy and barcode statements hold only for \(B=[3]\times[4]\times[4]\). The matching is algorithmically specified and exhaustively checked but is not an all-parameter matching construction. Literature/database searches and inspection of the most directly relevant primary results found no implication-equivalent theorem; this is not proof of publication priority, and an unindexed earlier computation may exist. Self-review is not independent mathematical review.

## References
1. Shuchita Goyal, Samir Shukla, and Anurag Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, 2019, arXiv:1905.06926, https://arxiv.org/abs/1905.06926 (original public version dated 2019-05-16).
2. Omar Antolín Camarena and Andrés Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, 2023, arXiv:2307.12401, https://arxiv.org/abs/2307.12401 (original public version dated 2023-07-23; see Conjecture 26).
3. Robin Forman, *Morse theory for cell complexes*, Adv. Math. 134 (1998), 90--145, for the finite acyclic-matching-to-CW principle.
