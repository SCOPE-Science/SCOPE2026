# Integral four-cut homology separates the Shrikhande and rook graphs

## Finding
Let \(S\) be the Shrikhande graph and \(R=K_4\square K_4\) the four-by-four rook graph. Both are strongly regular with parameters \((16,6,2,2)\). For a finite simple graph \(G\), let \(\Delta_4(G)\) denote the **ordinary** four-cut complex: its facets are the complements of four-vertex subsets inducing disconnected subgraphs, rather than complements of independent four-sets.

The complete reduced **integral** homology groups are
\[
\widetilde H_i(\Delta_4(S);\mathbb Z)\cong
\begin{cases}
\mathbb Z^{12},&i=9,\\
\mathbb Z^{2},&i=10,\\
\mathbb Z^{65},&i=11,\\
0,&\text{otherwise},
\end{cases}
\]
and
\[
\widetilde H_i(\Delta_4(R);\mathbb Z)\cong
\begin{cases}
\mathbb Z^{21},&i=10,\\
\mathbb Z^{96},&i=11,\\
0,&\text{otherwise}.
\end{cases}
\]
In particular, both are pure eleven-dimensional and **non-shellable**. Their equal reduced Euler characteristic, \(-75\), does not detect the degree-nine homology carried by the Shrikhande complex but absent from the rook complex. These are additive integral homology calculations; a complete homotopy classification is not asserted.

## Assumptions and scope
Vertices of both graphs are pairs \((a,b)\in(\mathbb Z/4\mathbb Z)^2\), encoded by integers \(4a+b\) with \(a,b\in\{0,1,2,3\}\). In \(S\), two vertices are adjacent if and only if their coordinate difference lies in
\[
\{(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1)\}\pmod4.
\]
In \(R\), two distinct vertices are adjacent if and only if their first or their second coordinates agree. The graph edge sets are unoriented, undirected, and loop-free. Every homology group above has integral coefficients; the geometric realization of the finite abstract simplicial complex is understood.

Set \(V=V(G)\) and \(L_G=\Delta_4(G)^\vee\), using the Alexander dual on **all sixteen** graph vertices. Explicitly,
\[
L_G=\{A\subseteq V:\text{every four-element subset of }A\text{ induces a connected graph}\}.
\]
This description includes the empty face and every face of cardinality at most three. It is not the clique or independence complex of \(G\).

## Proof
**1. Exact dual construction.** A subset \(B\subseteq V\) is a face of \(\Delta_4(G)\) precisely when \(V\setminus B\) contains a disconnected induced four-set. Thus \(A\in\Delta_4(G)^\vee\) precisely when \(A\) contains no such four-set, proving the displayed formula for \(L_G\). Encode a subset by a sixteen-bit mask. All \(\binom{16}{4}=1820\) four-sets are classified by an exact breadth-first connectivity search on the induced graph. There are \(668\) connected four-sets for \(S\) and \(620\) for \(R\), hence \(1152\) and \(1200\) disconnected four-sets, respectively. For cardinality greater than four, a mask belongs to \(L_G\) if and only if **every** single-vertex deletion does. This is equivalent to the original four-subset definition: any forbidden four-set is contained in a codimension-one deletion when the mask has at least five vertices. Iterating all \(2^{16}\) masks gives the face vectors by dimension
\[
(f_0,f_1,f_2,f_3,f_4,f_5)(L_S)=(16,120,560,668,288,0),
\]
\[
(f_0,f_1,f_2,f_3,f_4,f_5)(L_R)=(16,120,560,620,288,48).
\]
An independent direct check tests each mask for containment of any disconnected four-set. Both dual complexes have exactly \(1652\) nonempty simplices, and reduced Euler characteristic \(75\).

**2. Complete acyclic matchings.** Use the nonempty face poset of either \(L_G\). For vertex indices \(v=0,1,\ldots,15\) in that order, examine currently unmatched faces by increasing cardinality and then integer mask. Whenever both \(F\) and \(F\cup\{v\}\) are unmatched and \(v\notin F\), match that lower–upper pair and remove both from the unmatched set. For \(S\) this gives \(776\) pairs and critical cells consisting of one vertex, \(69\) two-cells, \(12\) three-cells, and \(18\) four-cells. For \(R\) it gives \(767\) pairs, one critical vertex, \(96\) two-cells, and \(21\) three-cells. Orient each Hasse incidence from upper to lower, reversing matched incidences. Exhaustive directed acyclicity tests traverse **every** nonempty-face incidence: \(6032\) for \(S\) and \(6128\) for \(R\). A complete topological ordering on all \(1652\) faces exists in both cases. Consequently these are genuine acyclic discrete-Morse matchings, producing integral cellular Morse chain complexes with exactly these critical cells.

**3. Integral Morse differentials, with no hidden torsion.** Orient each simplex by its increasing vertex sequence, so omission of vertex in position \(j\) has boundary coefficient \((-1)^j\). The standard acyclic-matching reduction gives explicit Morse boundaries via signed gradient-path sums. For a critical lower face \(c\), let \(P(c)=c\); for a face that is the upper member of a pair let \(P(c)=0\). For a lower face \(c\) paired with a higher face \(h\), define recursively
\[
P(c)=-[c:\partial h]^{-1}
\sum_{\substack{d\subset h,\ |d|=|c|\\d\ne c}}
[d:\partial h]P(d).
\]
Here the incidence \([c:\partial h]\) is \(\pm1\), and the verified acyclicity makes the recursion finite. For critical cells, the signed simplicial boundary followed by \(P\) yields the integral Morse boundary. Its consecutive compositions are independently checked to vanish. The remaining matrices have dimensions \(69\times12\) and \(12\times18\) for \(S\), and \(96\times21\) for \(R\). Both matrices for \(S\) admit complete **integer** row and column reductions with only unit pivots; the Smith nonzero invariant factors are four copies of \(1\) in degree three and six copies of \(1\) in degree four. No nonunit residual block remains. The rook Morse boundary vanishes identically. These operations are unimodular and rule out **all** integral torsion, not only torsion at tested primes.

Thus the reduced integral homology of the Alexander duals is
\[
\widetilde H_j(L_S;\mathbb Z)=
\begin{cases}\mathbb Z^{65},&j=2,\\\mathbb Z^2,&j=3,\\\mathbb Z^{12},&j=4,\\0,&\text{otherwise},\end{cases}
\]
\[
\widetilde H_j(L_R;\mathbb Z)=
\begin{cases}\mathbb Z^{96},&j=2,\\\mathbb Z^{21},&j=3,\\0,&\text{otherwise}.\end{cases}
\]
As an independent computational cross-check, ordinary (unreduced) simplicial boundary ranks over \(\mathbb F_2\), without using Morse reduction, are \((15,105,390,276,0)\) for \(S\) and \((15,105,359,240,48)\) for \(R\) in degrees one through five. Their Betti numbers agree with the integral result.

**4. Integral Alexander duality and shellability.** Combinatorial Alexander duality on sixteen vertices gives, for every integer \(i\),
\[
\widetilde H_i(\Delta_4(G);\mathbb Z)
\cong\widetilde H^{13-i}(L_G;\mathbb Z).
\]
Because the dual homology groups are free, the universal coefficient theorem identifies their cohomology with integer duals of the same ranks. Substituting the groups just computed proves both displayed cut-complex classifications. Since disconnected induced four-sets exist, every four-cut facet has twelve vertices, and both cut complexes are pure of dimension eleven. Each has nonzero reduced homology below dimension eleven; by the pure shellability theorem, neither is shellable.

## Verification
Extract `evidence/verify.py` alongside this document and run `python3 evidence/verify.py` using standard Python 3; the checker requires no external libraries or data. It independently enumerates every subset, verifies graph adjacency and strongly regular parameters, reconstructs the dual faces by two formulations, checks each acyclic matching against its full oriented Hasse diagram, calculates the signed integral Morse differentials, verifies their square-zero identities, performs exact unimodular row/column reductions, and independently recomputes the original mod-two boundary ranks. A successful complete execution ends with `SHRIKHANDE_ROOK_ORDINARY_4CUT_INTEGRAL_HOMOLOGY_OK`. Exact observations are asserted only for these two finite graphs; exhaustive computation is appropriate because **all** possible vertex subsets and all incidence edges are checked, not sampled.

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue introduced the ordinary cut complex and established general structural and shellability results in *Topology of Cut Complexes of Graphs* (first public 2023, arXiv:2304.13675). Their full paper treats trees, cycles, complete multipartite graphs, certain squared cycles, and clique prisms, but does not state the present two four-cut classifications. Their sequel, *Topology of Cut Complexes II* (arXiv:2407.08158), studies disjoint unions, powered paths, and Cartesian **path** grids, not these two strongly regular graphs. In particular, the rook graph \(K_4\square K_4\) is a Cartesian product of **complete** graphs, not the Cartesian path grid \(P_4\square P_4\).

Prior published calculations classify the **three-cut** complex of rook graphs and the **independence** complexes of the Shrikhande/rook pair. Those statements do not determine the ordinary **four-cut** integral homology, and indeed these cut complexes have different defining facets and homological degrees. A previously determined four-cut complex of the triangular graph \(J(5,2)\) is also a different graph and parameter instance. High-girth four-cut sphere-wedge results do not apply: both graphs here have triangles and four-cycles. The full explicit cross-source comparison is in the accompanying review. No originality claim rests on merely unmatched titles or numerical coincidence.

## Limitations
The claim is the additive integral homology of these two specific four-cut complexes, not their full homotopy types, cup-product rings, automorphism modules, or a theorem about all strongly regular graphs. It does not claim the graphs themselves had previously been indistinguishable. Although their four-cut homology differs, many established invariants already distinguish the pair. A mathematically equivalent computation could exist outside the inspected literature. No independent external mathematical audit has been performed.

## References
1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675, first public 26 April 2023, especially Sections 1, 6, 7, https://arxiv.org/abs/2304.13675.
2. M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram and L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158, first public 11 July 2024, Sections 3–6, https://arxiv.org/abs/2407.08158.
3. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145. The acyclic-matching theorem supplies the integral cellular model.
4. Standard combinatorial Alexander duality and the universal coefficient theorem, as described in Reference 1, Section 1.
