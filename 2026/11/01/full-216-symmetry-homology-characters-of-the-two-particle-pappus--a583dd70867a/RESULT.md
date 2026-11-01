# Full 216-symmetry homology characters of the two-particle Pappus configuration space

## Finding
Let \(P\) be the 18-vertex Pappus graph with LCF sequence \([5,7,-7,7,-7,-5]^3\) and let \(X=\operatorname{UConf}_2(|P|)\) be the ordinary space of two *unordered, distinct* points on its geometric realization. The graph automorphism group \(G=\operatorname{Aut}(P)\) has order 216 and 13 conjugacy classes. Its complete graded **rational homology character** is given by the following table. Entries \(\lambda_V\) and \(\lambda_E\) specify the cycle partitions on the 18 graph vertices and 27 graph edges, respectively; class labels enumerate representatives in the standalone verifier, which also records them as explicit permutations.

| Class | Size | Order | \(\lambda_V\) | \(\lambda_E\) | \(\operatorname{tr}H_1\) | \(\operatorname{tr}H_2\) |
|---:|---:|---:|---|---|---:|---:|
|1|1|1|\(1^{18}\)|\(1^{27}\)|10|27|
|2|18|2|\(2^7 1^4\)|\(2^{12}1^3\)|0|−3|
|3|9|2|\(2^6 1^6\)|\(2^{12}1^3\)|−2|3|
|4|36|6|\(6^2 3\,2\,1\)|\(6^4 3\)|0|0|
|5|12|3|\(3^5 1^3\)|\(3^9\)|−2|0|
|6|18|2|\(2^9\)|\(2^{12}1^3\)|−2|−3|
|7|18|4|\(4^3 2^3\)|\(4^6 1^3\)|−2|3|
|8|36|6|\(6^3\)|\(6^4 3\)|1|0|
|9|18|12|\((12,6)\)|\((12,12,3)\)|1|0|
|10|12|3|\(3^6\)|\(3^9\)|1|0|
|11|18|6|\(6^2 3^2\)|\(6^4 3\)|1|0|
|12|18|12|\((12,6)\)|\((12,12,3)\)|1|0|
|13|2|3|\(3^6\)|\(3^9\)|1|0|

The underlying rational Betti numbers are \((1,10,27)\) in dimensions 0, 1 and 2; all higher rational homology vanishes. The two degree-one and degree-two representations are completely determined up to rational representation isomorphism by these character values, without asserting an integral representation-lattice decomposition.

Averaging each character over the full group \(G\), and separately over its 108-element bipartition-preserving subgroup \(G^+\), gives zero in both positive degrees. Consequently
\[
\widetilde H_*(|X|/G;\mathbb Q)=\widetilde H_*(|X|/G^+;\mathbb Q)=0.
\]
Every order-three subgroup, by contrast, fixes a nine-dimensional subspace of \(H_2(X;\mathbb Q)\). This isolates symmetry information not determined by the ordinary Betti numbers.

## Assumptions and scope
The simple, connected graph \(P\) is built on vertices numbered 0 through 17 using the Hamiltonian cycle and chords specified by \([5,7,-7,7,-7,-5]^3\). Edges are oriented from their smaller to their larger vertex. The 27 graph edges are indexed lexicographically; the cubical two-cells are oriented by increasing graph-edge index. All homology and all character statements in this finding are over \(\mathbb Q\).

The unordered Abrams cubical model \(UD_2(P)\) consists of unordered pairs of graph cells with disjoint closures. The graph has girth six and all its vertices are essential, so for two particles it satisfies the sufficient-subdivision hypotheses; the standard model is homotopy equivalent to \(X\). Since graph automorphisms preserve these cells, the model carries the stated natural group action. There are 153 zero-cells (unordered distinct vertices), 432 one-cells (an edge and a nonincident vertex), and 297 two-cells (two vertex-disjoint edges).

## Proof
**1. Signed cubical boundaries.** For a graph edge \(e_i=(a,b)\), \(a<b\), and another vertex \(v\notin\{a,b\}\), the one-cell \((e_i,v)\) has boundary \((\{b,v\})-(\{a,v\})\). For a two-cell \((e_i,e_j)\), \(i<j\), with \(e_i=(a,b)\) and \(e_j=(c,d)\), the boundary is
\[
(e_j,b)-(e_j,a)-(e_i,d)+(e_i,c).
\]
The verifier constructs every signed incidence and checks \(\partial_1\partial_2=0\) exactly over the integers. Its ranks are \(\operatorname{rank}\partial_1=152\) and \(\operatorname{rank}_{\mathbb F_3}\partial_2=270\); the latter gives the rational lower bound 270.

**2. Exact rational rank upper bound.** Choose the deterministic breadth-first spanning tree rooted at vertex 0. The ten non-tree edges give ten fundamental graph cycles. Each such cycle omits at least one graph vertex; holding a particle at that omitted vertex and moving the other around the cycle produces a closed one-chain in \(UD_2(P)\). The natural chain map that sends \((e_i,v)\) to \(e_i\) and a two-cell to zero maps these ten cycles to the ten standard, linearly independent graph cycles. Therefore \(\dim H_1(X;\mathbb Q)\ge10\), forcing \(\operatorname{rank}_{\mathbb Q}\partial_2\le432-152-10=270\). Combined with the finite-field lower bound, the rank is exactly 270. Thus \(\beta_1=10\) and \(\beta_2=297-270=27\). In particular, the natural map \(H_1(X;\mathbb Q)\to H_1(P;\mathbb Q)\) is an isomorphism, compatible with graph automorphisms. Independent modular checks also give \(\operatorname{rank}_{\mathbb F_2}\partial_2=269\) and ranks 270 modulo 5 and 101. The mod-two difference is not used to assert a complete integral torsion classification.

**3. Characters.** For any graph automorphism \(g\), put \(t_j(g)=\operatorname{tr}(g\mid C_j(UD_2(P);\mathbb Q))\). Each trace is computed by summing orientation signs over precisely the fixed cubical cells, including the coordinate-swap sign on two-cells. The equivariant isomorphism in degree one gives
\[
\chi_1(g)=1+\operatorname{tr}(g\mid C_1(P;\mathbb Q))-\operatorname{tr}(g\mid C_0(P;\mathbb Q)).
\]
The cellular Hopf–Lefschetz trace identity then gives
\[
\chi_2(g)=t_0(g)-t_1(g)+t_2(g)-1+\chi_1(g).
\]
An exhaustive graph-isomorphism enumeration returns exactly 216 automorphisms. Conjugation partitions them into 13 classes of the displayed sizes, and the verifier confirms that all class members have identical characters. It verifies the full signed cellular action commutes with both differentials for every automorphism and every cell. The table results by exact integer arithmetic.

**4. Quotients.** The character sums are zero over \(G\) and \(G^+\) in both positive degrees; connectivity gives no reduced degree-zero homology. In characteristic zero the homology of a finite-group orbit space identifies with the invariant subspace, yielding the quotient assertions. Each order-three element has \(\chi_2=0\); averaging \((27,0,0)\) over its cyclic subgroup gives invariant dimension nine.

## Verification
Run `python3 verify_pappus_configuration.py` with Python 3 and `networkx` installed. It constructs the graph from the displayed LCF sequence, enumerates the cubical cells and boundary matrices, checks all zero compositions, computes exact ranks modulo 2, 3, 5 and 101, verifies all ten explicit stationary-particle cycle lifts, enumerates the entire automorphism group and its conjugacy classes, verifies all chain-action signs and commutative squares, and calculates the character table and subgroup averages. Successful output ends in `VERIFY_OK`. The recorded output is `verification_output.txt`. These computations are exact, not floating-point approximations.

## Relationship to prior work
The unordered graph-braid results of Ko and Park already describe first-homology ranks and the standard nonplanar two-torsion phenomenon for graph braid spaces; neither is presented as new here. Barnett–Farber and Farber–Hanbury establish the foundational two-particle deleted-product and intersection-form methods, mainly for ordered spaces. Their inspected results do not supply the 216-element rational automorphism characters on the Pappus unordered space. The published three-particle Pappus top-homology calculation concerns a different particle number and is not a statement about this degree-two representation. Existing two-particle results for Petersen and dodecahedral graphs concern distinct graphs and groups. A general exchange-sign Borel–Moore homology calculation concerns a different homology theory and local coefficients, not ordinary rational homology of this space. The exact novelty assessed here is the *full graded Pappus group character and its symmetry-quotient consequences*, not the familiar computation of ordinary Betti numbers.

## Limitations
The result is confined to two unordered particles, the Pappus graph, and rational homology representations. It does not determine the integral lattice action or the complete integral torsion invariants, braid-group presentations, quotient fundamental groups, or quotient homotopy types. Literature searches are not a proof of novelty; an inaccessible or unindexed specialized equivariant calculation is possible. The numerical output by itself would not prove the theorem without the chain model, exact-rank sandwich, and signed-action formula above. No independent audit has been performed.

## References
1. K. Barnett and M. Farber, *Topology of Configuration Space of Two Particles on a Graph, I*, arXiv:0903.2180v1 (first public 2009-03-12), especially §1 and Lemma 1.1.
2. M. Farber and E. Hanbury, *Topology of configuration space of two particles on a graph, II*, arXiv:1005.2300v1 (first public 2010-05-13), especially §§1–2.
3. K. H. Ko and H. W. Park, *Characteristics of graph braid groups*, arXiv:1101.2648v1 (first public 2011-01-13), especially §§1–3.
4. Public mathematical record, *Top homology of the three-particle Pappus configuration space*, published-finding corpus record `94f23a73ed7c` (distinct particle count).
5. Public mathematical record, *Dodecahedral two-point configuration homology as an A5 × C2-module*, published-finding corpus record `d0e364decb52` (distinct graph).
6. Public mathematical record, *Exchange-sign Borel–Moore homology of two-point graph configurations*, published-finding corpus record `68e49e70a285` (distinct homology theory).
