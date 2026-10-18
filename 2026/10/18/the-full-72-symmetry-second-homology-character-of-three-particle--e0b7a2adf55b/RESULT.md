# The full 72-symmetry second-homology character of three particles on \(K_{3,3}\)

## Finding
Let \(\Gamma=K_{3,3}\) be the abstract complete bipartite graph with parts \(L=\{0,1,2\}\), \(R=\{0,1,2\}\), and let \(X=\operatorname{UConf}_3(|\Gamma|)\) be the space of unordered triples of pairwise distinct points on its geometric realization. Its graph automorphism group is \(G=(S_3\times S_3)\rtimes C_2\), of order \(72\), where the last factor exchanges \(L\) and \(R\). Work over \(\mathbb Q\).

Let \(V\) denote the two-dimensional standard \(S_3\)-module, \(\varepsilon\) the sign line, and \(N=S_3\times S_3\). Write \(V_-\) for the four-dimensional extension of \(V\boxtimes V\) to \(G\) on which exchanging the two factors acts by **minus** the tensor-factor flip. Then
\[
H_2(X;\mathbb Q)\cong V_-\oplus\operatorname{Ind}_{N}^{G}(\varepsilon\boxtimes V).
\]
Both summands are nonisomorphic absolutely irreducible four-dimensional rational representations, with multiplicity one. In particular \(H_2(X;\mathbb Q)^G=0\).

This is equivalently a complete character formula. Write \(g=(p,q,s)\) with \(p,q\in S_3\), and \(s=0\) for a bipartition-preserving automorphism, \(s=1\) for an interchange. Let \(v(p)=|\operatorname{Fix}(p)|-1\) and \(e(p)=\operatorname{sgn}(p)\). Then
\[
\chi_2(p,q,0)=v(p)v(q)+e(p)v(q)+v(p)e(q),\qquad
\chi_2(p,q,1)=-v(pq).
\]
The rational Betti numbers are \(b_0=1\), \(b_1=4\), \(b_2=8\), and \(b_i=0\) for \(i\ge3\). The dimensions were known previously; the complete natural symmetry action is the finding.

## Assumptions and scope
The three particles are **unlabelled**, are forbidden to collide anywhere (including vertices), and move on the one-dimensional realization of the unoriented graph. Group elements act by graph automorphisms, not by particle-label permutations. The representation and its irreducibility statements use characteristic zero. The chosen ordering of the two graph parts is for notation only; changing it conjugates the group description.

## Proof
**Finite equivariant model.** Subdivide every edge of \(K_{3,3}\) once, obtaining 15 vertices and 18 edges. By the sufficient-subdivision criterion for Abrams's discretized configuration space, sharpened by Prue and Scrimshaw, the resulting cubical discrete unordered configuration space \(D_3\) is a deformation retract of \(X\). The shortest path between distinct essential vertices now has two edges, satisfying the \(n-1=2\) threshold, and every essential loop has at least eight edges, exceeding \(n+1=4\). The inclusion \(D_3\hookrightarrow X\) is natural under all 72 graph automorphisms; because it induces a homology isomorphism it identifies their rational homology representations.

An oriented \(d\)-cube is indexed by \(d\) pairwise disjoint open subdivided edges and \(3-d\) vertices disjoint from their closures. Its orientation is the increasing order of the edge indices. Exhaustively enumerating these cubes gives chain-group ranks \((455,1404,1386,432)\) in degrees \(0,1,2,3\). If a cube has oriented edge coordinates \(e_1<\cdots<e_d\), its boundary is the sum over coordinates of \((-1)^{i-1}\) times (terminal-face minus initial-face); vertex indices are canonically sorted. These rules uniquely determine the integral boundary matrices.

**Ranks and concentration.** The supplied standalone exact verifier constructs all three boundary matrices and confirms the two consecutive boundary compositions vanish. Gaussian elimination modulo two finds \(\operatorname{rank}\partial_1=454\) and \(\operatorname{rank}\partial_3=432\); elimination modulo three finds \(\operatorname{rank}\partial_2=946\). Every rank over a prime field is a lower bound for the rational rank. The rational rank of \(\partial_1\) is at most 454 because the sum-of-coefficients functional annihilates its image, so equality holds. The rank of \(\partial_3\) cannot exceed its 432 columns, so equality also holds.

For an upper bound on \(\operatorname{rank}_{\mathbb Q}\partial_2\), use the natural total-motion homomorphism \(H_1(X;\mathbb Q)\to H_1(\Gamma;\mathbb Q)\), obtained by summing the tracks of the three unordered particles. It is onto: for each \(i,j\in\{1,2\}\), traverse the square \(L_0,R_0,L_i,R_j,L_0\) with one particle while parking two particles at the unique unused original vertex on each side. The resulting four cycles map to a basis of \(H_1(\Gamma;\mathbb Q)\), since each uses its own non-tree edge \(L_iR_j\). Consequently \(b_1(X)\ge4\), and \(\operatorname{rank}_{\mathbb Q}\partial_2\le 1404-454-4=946\). The modulo-three lower bound forces equality. Thus \(b_1=4\), \(b_2=1386-946-432=8\), and \(b_3=0\).

The total-motion map is an isomorphism on rational first homology because its source and target both have dimension four. Its \(G\)-equivariance implies \(H_1(X;\mathbb Q)\cong H_1(\Gamma;\mathbb Q)\). Taking graph chains in the left-to-right edge orientation identifies this latter module with \(V_-\): the normal subgroup acts as \(V\boxtimes V\), while interchanging the sides reverses the orientation and flips the tensor factors. Equivalently, \(\chi_1(g)=\operatorname{tr}(g|C_1(\Gamma))-\operatorname{tr}(g|C_0(\Gamma))+1\).

**Exact homological character.** For every one of 72 automorphisms, its action on oriented \(d\)-cubes permutes cube generators with signs determined by both oriented-edge reversals and the parity of reordered edge coordinates. The code calculates \(t_d(g)=\operatorname{tr}(g|C_d(D_3;\mathbb Q))\) as a signed fixed-cube sum and computes \(L(g)=\sum_{d=0}^{3}(-1)^dt_d(g)\). Because \(H_0\) is trivial, \(H_3=0\), and \(H_1\cong V_-\), equivariant Euler–Poincaré gives \(\chi_2(g)=L(g)-1+\chi_1(g)\).

In the order: bipartition-preserving pairs of permutation cycle types \((1^3,1^3)\), \((1^3,21)\), \((1^3,3)\), \((21,21)\), \((21,3)\), \((3,3)\), then side-exchanging permutations with product cycle type \(1^3\), \(21\), \(3\), the nine class sizes are \((1,6,4,9,12,4,6,18,12)\) and character values are
\[
(8,-2,-1,0,1,-1,-2,0,1).
\]
The explicit formulas in the Finding reproduce these values **for every group element**, not merely representatives.

**Irreducible decomposition.** The group \(S_3\wr C_2\) has nine absolutely irreducible characteristic-zero representations: six extensions \(U_+\), \(U_-\) of \(U\boxtimes U\) (where \(U\) runs through the trivial, sign, and standard \(S_3\)-representations), and three induced representations from the unordered pairs of distinct choices of \(U\). Their characters on preserving and swapping elements are explicitly implemented in the verifier. Exact character inner products using all 72 elements give multiplicity one for \(V_-\), multiplicity one for \(\operatorname{Ind}_{N}^{G}(\varepsilon\boxtimes V)\), and zero for all seven other irreducibles. The two summands have dimension four and are defined over \(\mathbb Q\); the character checks over \(\mathbb C\) establish absolute irreducibility. Neither is the trivial representation, so there are no globally fixed second-homology classes.

## Verification
Run `python3 verify.py` with Python 3.8 or later. The script is standalone, uses only the standard library, regenerates all cubes and integral boundaries, checks \(\partial^2=0\), performs exact modular elimination, enumerates all 72 signed cubical automorphisms, verifies the nine conjugacy-class characters and their irreducible inner products. Expected output consists of four lines beginning with `PASS`. The independently justified four moving-particle cycles and the rank upper bounds turn these modular certificates into the asserted rational Betti numbers; the finite checks are exact for this finite model and do not claim an infinite-family result.

## Relationship to prior work
Abrams and Prue–Scrimshaw provide the graph-configuration cubical-model framework. Maciążek and Sawicki, *Non-abelian Quantum Statistics on Graphs*, Section 5.5, establish the known rank \(b_2=8\) for three particles on \(K_{3,3}\) from twelve product cycles, of which eight are independent. They do not tabulate the natural 72-element automorphism action or the two absolutely irreducible rational summands. Their cycle presentation gives a related starting point but does not supply the signed quotient representation without further symmetry computations. Ramos and He Yun (2026) analyze stable homology representations of two-particle configurations of complete bipartite graph families; their three-particle results concern complete graphs, not this claim. This result supplies the missing full-group character and decomposition for the specific three-particle \(K_{3,3}\) space.

## Limitations
No assertion is made about integral \(G\)-lattices, other numbers of particles, or larger complete bipartite graphs. The ordinary homology ranks and the product-cycle generation are prior results, not new. Exact cellular calculations plus a proof of rational homology concentration establish the displayed representation; independent external mathematical validation has not been performed. A literature search is not a uniqueness theorem, and further unindexed equivariant computations might overlap.

## References
1. A. D. Abrams, *Configuration spaces and braid groups of graphs*, PhD thesis, UC Berkeley, first listed 2000-05-01. https://math.berkeley.edu/publications/configuration-spaces-and-braid-groups-graphs
2. P. Prue and T. Scrimshaw, *Abrams's stable equivalence for graph braid groups*, first posted 2009-09-30, arXiv:0909.5511. https://arxiv.org/abs/0909.5511
3. T. Maciążek and A. Sawicki, *Non-abelian Quantum Statistics on Graphs*, Commun. Math. Phys. 371 (2019), Section 5.5, DOI:10.1007/s00220-019-03583-5. https://doi.org/10.1007/s00220-019-03583-5
4. E. Ramos and C. He Yun, *Computing stable homology representations of graph configuration spaces*, first posted 2026-06-11, arXiv:2606.13813. https://arxiv.org/abs/2606.13813
