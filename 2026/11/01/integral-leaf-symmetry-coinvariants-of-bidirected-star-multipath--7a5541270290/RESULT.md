# Integral leaf-symmetry coinvariants of bidirected-star multipath homology

## Finding
For every integer \(m\ge3\), let \(D_m\) denote the directed graph obtained from an undirected star with \(m\) leaves by replacing each spoke with the two opposite arcs. The symmetric group \(S_m\) permutes the leaves. Let \(X_m\) denote the multipath (directed linear-forest) simplicial complex: its vertices are arcs of \(D_m\), and its faces are sets of arcs forming vertex-disjoint directed paths, with isolated vertices allowed. Then
\[
\boxed{(H_1(X_m;\mathbb Z))_{S_m}\cong
\begin{cases}\mathbb Z/2\mathbb Z,&m=3,4,\\0,&m\ge5.\end{cases}}
\]
All rational coinvariants vanish. Thus an integral symmetry obstruction exists at precisely three and four leaves.

## Assumptions and scope
The statement concerns the **integral coinvariant module** \(M_{S_m}:=M/\langle \sigma z-z:\sigma\in S_m, z\in M\rangle\), not the invariant module, the quotient space's homology, or any geometric fixed-point locus. The graph has one central vertex, \(m\ge3\) labeled leaves, and exactly one arc in each direction along each spoke. Homology is integral singular or simplicial homology. An oriented edge \(e_{ij}\) always denotes an edge directed in the *simplicial complex* from its inward-spoke vertex to its outward-spoke vertex; it does not change its simplicial orientation under leaf permutations.

## Proof
**1. Crown-graph model.** Write \(a_i\) for the directed arc from leaf \(i\) to the hub and \(b_j\) for the directed arc from the hub to leaf \(j\). A face can contain at most one \(a\)-arc and one \(b\)-arc, and \(\{a_i,b_j\}\) is a face exactly when \(i\ne j\): equality yields a directed two-cycle. Therefore \(X_m\) is the one-dimensional crown graph, with edge set \(\{e_{ij}:i\ne j\}\). For \(m\ge3\) it is connected with \(2m\) vertices and \(m(m-1)\) edges. Its integral first homology is the free lattice
\[
L_m=\left\{(z_{ij})_{i\ne j}\in\mathbb Z^{m(m-1)}:\ 
\sum_{j\ne i} z_{ij}=0\ (\forall i),\quad
\sum_{i\ne j} z_{ij}=0\ (\forall j)\right\},
\]
of rank \(m^2-3m+1\). The induced \(S_m\)-action permutes both subscripts simultaneously.

**2. Generating four-cycles.** If \(a,b,c,d\) are pairwise distinct, put
\[
\Gamma(a,b;c,d)=e_{ac}-e_{ad}-e_{bc}+e_{bd}\in L_m.
\]
For \(m\ge4\), these elements generate \(L_m\) as an **integral** lattice. Indeed, in a connected graph every integral cycle is an integral sum of oriented simple cycles, by subtracting an oriented simple circuit and inducting on its coefficient mass (or using fundamental cycles of a spanning tree). Every cycle in the crown graph is even. A simple cycle of length at least eight has a chord: a row vertex on it is adjacent to every column vertex of that cycle except possibly its same-labeled partner; among at least four cycle columns there is a third neighbor in addition to its two cyclic neighbors. Splitting across a chord expresses its cycle vector as a sum of shorter cycles. A chordless six-cycle has three row labels \(\{a,b,c\}\), the same three column labels, and, up to orientation, vector
\[
\Theta(a,b,c)=e_{ab}+e_{bc}+e_{ca}-e_{ac}-e_{cb}-e_{ba}.
\]
Choosing a fourth label \(d\), direct expansion proves
\[
\Theta(a,b,c)=-\Gamma(a,b;c,d)+\Gamma(a,c;b,d)-\Gamma(b,c;a,d).
\]
Finally, all chordless four-cycles are precisely the \(\Gamma\) elements, up to orientation. This is an integral generation argument; no rational span assumption is used.

**3. Vanishing for at least five leaves.** Under diagonal permutations of the labels, all four-cycles \(\Gamma(a,b;c,d)\) with four distinct indices have the same image \(g\) in the coinvariants. For any five pairwise distinct indices, one has the exact lattice identity
\[
\Gamma(a,b;c,d)+\Gamma(a,b;d,e)=\Gamma(a,b;c,e).
\]
Passing to coinvariants gives \(g+g=g\), hence \(g=0\). By the integral generation just proved, \((L_m)_{S_m}=0\) for every \(m\ge5\).

**4. Four leaves.** The six generators obtained by putting the two row labels and their complementary two column labels in increasing order are, in that order,
\[
\Gamma(0,1;2,3),\quad\Gamma(0,2;1,3),\quad\Gamma(0,3;1,2),\quad
\Gamma(1,2;0,3),\quad\Gamma(1,3;0,2),\quad\Gamma(2,3;0,1).
\]
Their \(12\)-by-\(6\) edge-coordinate matrix has rank five: the submatrix formed by the first five generators and edge-coordinate rows \((0,1),(0,2),(1,0),(1,2),(2,0)\) has determinant \(-1\). Direct expansion gives their primitive unique relation (with coefficients in the displayed order)
\[
(1,-1,1,1,-1,1).
\]
In particular, each class is an integer multiple of the single coinvariant generator \(g\), and swapping the two row labels of \(\Gamma\) changes its sign, giving \(2g=0\). Conversely, the parity of the sum of coefficients in any expansion into these six generators is well-defined: the only integral relation has coefficient sum \(2\), which is even. Permuting the four labels sends any displayed generator to another displayed generator up to sign, so this parity is \(S_4\)-invariant and sends \(g\mapsto1\). It induces a surjection from coinvariants to \(\mathbb Z/2\mathbb Z\). Thus \((L_4)_{S_4}\cong\mathbb Z/2\mathbb Z\).

**5. Three leaves.** The crown graph is a hexagon. Its first integral homology is \(\mathbb Z\); a simultaneous transposition of two labels reverses the cyclic orientation, while three-cycles preserve it. Thus \(L_3\) is the integral sign representation of \(S_3\), and its coinvariants are \(\mathbb Z/2\mathbb Z\).

## Verification
The standalone `verify.py` reconstructs the graph and a fundamental integral cycle basis for each \(m=3,\ldots,8\), computes the actions of a transposition and an \(m\)-cycle, and obtains Smith normal forms of the integral coinvariant relation matrices. The invariant factors are \((2)\), \((1,1,1,1,2)\), and all ones for \(m=5,6,7,8\) respectively. For \(m\ge4\) in this tested range, it independently verifies that four-cycles generate the cycle lattice integrally. Run `python verify.py` with SymPy installed. These finite calculations corroborate but are not substituted for the all-\(m\) proof above.

## Relationship to prior work
Deshpande and Sawant (2026) develop topological and combinatorial criteria for directed-forest complexes and conflict graphs, furnishing the motivating class. Caputi et al. (2022) study the homotopy types of multipath complexes. Neither cited work is used for the cycle-lattice calculation, and neither of the inspected relevant passages identifies the exact **diagonal leaf-permutation integral coinvariants** of this crown-graph family. The identification with the classical crown graph is elementary and not claimed to be new; the result lies in the integral equivariant invariant and its sharp two-torsion threshold.

## Limitations
The theorem does not assert that the ordinary homology of the quotient \(X_m/S_m\) equals these coinvariants; finite stabilizers can invalidate such an identification over the integers. It does not classify higher multipath complexes or other actions. Finite checker ranges cannot prove the infinite case; the preceding generation and cancellation proof does that. Equivalent unindexed literature remains a residual novelty risk, and no independent audit has been performed.

## References
- M. Deshpande and V. Sawant, *Vertex decomposable complexes of directed forests, conflict graphs and chordality*, first posted February 16, 2026, arXiv:2602.14936, https://arxiv.org/abs/2602.14936.
- L. Caputi and collaborators, *On the homotopy type of multipath complexes*, first posted 2022, arXiv:2208.04656, https://arxiv.org/abs/2208.04656.
