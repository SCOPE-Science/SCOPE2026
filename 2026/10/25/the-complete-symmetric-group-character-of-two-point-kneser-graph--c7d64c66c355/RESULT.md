# The complete symmetric-group character of two-point Kneser graph configuration homology

## Finding
For every integer \(n\ge 6\), let \(G_n=KG(n,2)\) be the Kneser graph of the two-element subsets of \(\{1,\ldots,n\}\), two vertices adjacent precisely when disjoint. Put \(X_n=\operatorname{UConf}_2(|G_n|)\), the space of two *unordered distinct* particles on the geometric realization of the graph. Its natural \(S_n\)-representation in rational degree-two homology has the following complete character formula. For \(g\in S_n\), write

\[
\begin{aligned}
F&=\#\{x\in V(G_n):gx=x\},&F_2&=\#\{x\in V(G_n):g^2x=x\},\\
T&=\operatorname{tr}(g\mid C_1(G_n;\mathbb Q)),&T_2&=\operatorname{tr}(g^2\mid C_1(G_n;\mathbb Q)),\\
P&=\#\{\{x,y\}\in E(G_n):gx=x,\ gy=y\}.
\end{aligned}
\]

The edge-chain orientations in \(T\) and \(T_2\) are genuine *signed* permutation representations: a fixed graph edge reversed by \(g\) contributes \(-1\). For each vertex \(x\) fixed by \(g\), put
\[
a_x=\#\{y\sim x:gy=y\},\qquad b_x=\#\{y\sim x:g^2y=y\},\qquad L=\sum_{gx=x}(a_x^2-b_x).
\]
Then
\[
\boxed{\displaystyle
\operatorname{tr}\!\left(g\mid H_2(X_n;\mathbb Q)\right)
=\frac{T^2-T_2-L}{2}-TF+2P+\frac{F^2+F_2}{2}-2F+T.}
\]
This depends only on fixed vertices, fixed graph edges, and neighbors of fixed vertices. It computes every character value for every \(n\ge6\), without constructing the configuration-space homology matrices.

For the first case beyond the Petersen graph, \(G_6\) has \(15\) vertices and \(45\) edges. Its second homology has rank \(315\), and as a rational \(S_6\)-module its **complete decomposition** is
\[
\begin{aligned}
H_2(X_6;\mathbb Q)\cong{}&S^{(5,1)}\oplus3S^{(4,2)}\oplus5S^{(4,1,1)}\oplus S^{(3,3)}\\
&\oplus7S^{(3,2,1)}\oplus6S^{(3,1,1,1)}\oplus2S^{(2,2,2)}\\
&\oplus4S^{(2,2,1,1)}\oplus2S^{(2,1,1,1,1)},
\end{aligned}
\]
where \(S^\lambda\) is the ordinary rational Specht module indexed by \(\lambda\vdash6\). No trivial or sign representation occurs. In particular, \(H_2(X_6;\mathbb Q)^{A_6}=0\), and the entire integral \(H_2(X_n;\mathbb Z)\) is torsion-free for all \(n\ge6\).

## Assumptions and scope
The graph is finite and simple, with the usual 1-dimensional CW realization; particles are distinct and **unlabeled**. Edges of \(G_n\) join disjoint two-subsets of the symbol set; \(S_n\) acts by permuting those symbols. Homology is rational for character and decomposition statements, integral only for the asserted torsion-freeness of second homology. The claim starts at \(n=6\); no assertion is made for \(n=5\) or for higher particle numbers.

## Proof
**1. Connectivity and first homology.** Write \(v=\binom n2\), \(d=\binom{n-2}{2}\) and \(e=vd/2\). For \(n\ge6\), adjacent vertices in \(G_n\) are disjoint two-subsets. Nonadjacent distinct vertices share exactly one symbol, and have at least \(\binom{n-3}{2}\ge3\) common neighbors. Thus deletion of any two graph vertices leaves a connected graph, proving 3-vertex-connectivity. The graph \(G_6\) has \(15\) vertices and \(45\) edges, exceeding the planar bound \(3v-6=39\); it is an induced subgraph of every \(G_n\) for \(n\ge6\). Hence all these graphs are nonplanar. The first-homology theorem of Ko–Park [2, Theorem 3.16] gives \(\dim_{\mathbb Q}H_1(X_n;\mathbb Q)=e-v+1\).

There is a canonical \(S_n\)-equivariant homomorphism on rational homology
\[\Phi_*:H_1(X_n;\mathbb Q)\longrightarrow H_1(G_n;\mathbb Q),\]
obtained by adding the trajectories of the two particles (the Abel–Jacobi map of their unordered divisor). Fix a breadth-first spanning tree rooted at any graph vertex. Since every graph-vertex distance from the root is at most two, each fundamental cycle of a nontree edge has at most five vertices. Since \(v\ge15\), we may park one particle at a graph vertex outside that cycle while moving the other once around it. The resulting configuration loop maps to the given fundamental graph cycle. These cycles form a basis of \(H_1(G_n;\mathbb Q)\), so \(\Phi_*\) is surjective. Both spaces have rational first-homology dimension \(e-v+1\); thus \(\Phi_*\) is an \(S_n\)-equivariant isomorphism. Consequently,
\[\operatorname{tr}(g\mid H_1(X_n;\mathbb Q))=T-F+1.\]

**2. Signed cubical chain modules.** For two particles, the standard unordered discrete configuration complex is a deformation retract because every simple cycle has at least three edges and each essential-vertex path at least one edge [2, §1]. Its degree-zero cells are unordered pairs of distinct graph vertices, degree-one cells are an oriented graph edge and a vertex not on it, and degree-two cells are unordered pairs of vertex-disjoint graph edges. These descriptions respect all graph automorphisms. Its dimension is two.

The degree-zero trace is \(\chi_0=(F^2+F_2)/2-F\). The degree-one trace is \(\chi_1=TF-2P\): start with all signed edge–vertex tensors, then exclude the two incidences at each graph edge fixed pointwise. A graph edge reversed by \(g\) fixes no incident vertex and contributes no excluded pair.

Let \(E=C_1(G_n;\mathbb Q)\), with oriented graph edges as its signed basis. The trace on \(\bigwedge^2 E\) is \((T^2-T_2)/2\). Its basis elements are unordered pairs of *distinct* graph edges with exterior-ordering signs. Remove the pairs sharing a graph vertex. A pair sharing exactly one vertex \(x\) that is fixed as a set under \(g\) necessarily has \(gx=x\). Orient both incident edges away from that fixed center. Their signed action becomes the ordinary permutation action on the neighbor set \(N(x)\), and the excluded-pair trace is the trace on its second exterior power, \((a_x^2-b_x)/2\). Every intersecting edge pair has one unique shared vertex, so no term is subtracted twice. Thus \(\chi_2=(T^2-T_2-L)/2\).

**3. Equivariant Euler–Poincaré.** Because the cubical model is two-dimensional and connected,
\[
[H_2(X_n;\mathbb Q)]=[C_2]-[C_1]+[C_0]-[H_0]+[H_1]
\]
in the rational representation ring. Insert \(\chi_2,\chi_1,\chi_0\), \(\chi_{H_0}=1\), and \(\chi_{H_1}=T-F+1\) to obtain the boxed formula. Since its degree-two integral chain group is free and there are no degree-three cells, \(H_2(X_n;\mathbb Z)=\ker\partial_2\) is torsion-free.

**4. The six-symbol irreducibles.** Enumerating the eleven conjugacy classes of \(S_6\), the character values for cycle types in the following order are:

| Cycle type | \((6)\) | \((5,1)\) | \((4,2)\) | \((4,1,1)\) | \((3,3)\) | \((3,2,1)\) | \((3,1,1,1)\) | \((2,2,2)\) | \((2,2,1,1)\) | \((2,1,1,1,1)\) | \((1^6)\) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Trace | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 3 | -9 | -9 | 315 |

Taking inner products with the eleven irreducible \(S_6\)-characters, computed by the rim-hook (Murnaghan–Nakayama) rule, gives multiplicities \((0,1,3,5,1,7,6,2,4,2,0)\), in partition order \((6),(5,1),(4,2),(4,1,1),(3,3),(3,2,1),(3,1,1,1),(2,2,2),(2,2,1,1),(2,1,1,1,1),(1^6)\). Their dimension-weighted sum is \(315\). As the trivial and sign multiplicities both vanish, the \(A_6\)-fixed part vanishes too (induction of the trivial \(A_6\)-module to \(S_6\) is the sum of trivial and sign).

## Verification
Run `python3 verify.py` with Python 3.9 or newer; it requires no external packages. It reconstructs the full \(G_6\) unordered configuration complex with cell numbers \((105,585,765)\), verifies \(\partial_1\partial_2=0\), and computes exact \(\mathbb F_3\)-rank \(450\) and \(\mathbb F_2\)-rank \(449\) for \(\partial_2\). The former, combined with \(\operatorname{rank}\partial_1=104\) and the surjective graph-cycle map above, independently traps the rational first Betti number at \(31\). The different mod-two rank is consistent with the known exchange two-torsion in first homology; no integral torsion classification is claimed.

Every one of the \(720\) symbol permutations is checked: a direct signed permutation trace on all cubical cells is required to agree with the displayed fixed-data formula. The program also independently evaluates the eleven Specht characters using rim-hook removal and checks the entire multiplicity decomposition. For \(G_7\), representatives of all fifteen permutation cycle types are checked directly. Successful output ends in `VERIFY_OK_KNESER_GRAPH_BRAID_CHARACTER`.

## Relationship to prior work
Ko and Park [2] establish the *nonequivariant* first-homology formula for graph braid groups, including the two-torsion of nonplanar triconnected graphs. The present proof uses that result, not a new claim about first Betti numbers. Their analysis and its ordinary Euler-characteristic consequence also determine nonequivariant Betti ranks; those are not new here. Farber and Hanbury [1] establish graph-configuration methods and the ordered two-particle intersection-form framework, rather than this \(S_n\) character. The new assertion is the closed fixed-data character for this infinite Kneser family and the complete degree-two \(S_6\) decomposition. Published studies of neighborhood, Čech, and independence complexes on the same graph involve different topological constructions and do not supply these representations.

## Limitations
The character formula is for rational homology and two **unordered** particles, and no integral \(S_n\)-module splitting is asserted. The statement does not determine the cohomology ring, fundamental group, integral first-homology torsion for arbitrary graphs, or analogous representations for three or more particles. Its originality is subject to possible equivalent unindexed results on automorphism actions. The finite checker supplies exact independent checks at two values of \(n\); only the preceding general argument proves the infinite family.

## References
[1] Michael Farber and Elizabeth Hanbury, *Topology of configuration space of two particles on a graph, II*, arXiv:1005.2300, first posted 2010-05-13. https://arxiv.org/abs/1005.2300

[2] Ki Hyoung Ko and Hyo Won Park, *Characteristics of graph braid groups*, arXiv:1101.2648, first posted 2011-01-13, especially Theorem 3.16 and the cubical model in §1. https://arxiv.org/abs/1101.2648
