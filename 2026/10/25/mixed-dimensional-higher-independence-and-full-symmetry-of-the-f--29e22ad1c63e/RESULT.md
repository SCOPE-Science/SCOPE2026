# Mixed-dimensional higher independence and full symmetry of the four-cube

## Finding
Let \(Q_4\) be the 4-dimensional hypercube graph. For its first higher-independence complex \(K=\operatorname{Ind}_2(Q_4)\), there is an **integral homotopy equivalence**
\[
K\simeq\left(\bigvee^{16}S^3\right)\vee S^4.
\]
Thus \(\widetilde H_3(K;\mathbb Z)=\mathbb Z^{16}\), \(\widetilde H_4(K;\mathbb Z)=\mathbb Z\), and all other reduced integral homology groups vanish.

The full automorphism group \(B_4=(C_2)^4\rtimes S_4\) acts on rational homology as
\[
\widetilde H_3(K;\mathbb Q)\cong V\oplus W,
\qquad
\widetilde H_4(K;\mathbb Q)\cong\operatorname{sgn}_{S_4}.
\]
Here \(V=\mathbb Q^4\) is the coordinate-permutation representation with trivial translation action. The twelve-dimensional module \(W\) has basis vectors \(e_{P,b}\) indexed by a two-element coordinate subset \(P\subseteq\{0,1,2,3\}\) and \(b\notin P\); for \(g=(t,\pi)\), where \(v\mapsto\pi(v)+t\), define
\[
g e_{P,b}=(-1)^{\sum_{j\in\pi(P)}t_j}e_{\pi(P),\pi(b)}.
\]
The translation subgroup acts trivially on \(\widetilde H_4\), while \(S_4\) acts there by its sign. Accordingly, the \(B_4\)-invariant parts of degrees three and four have dimensions \(1\) and \(0\), respectively.

## Assumptions and scope
The sixteen graph vertices are the bit vectors \(v\in\mathbb F_2^4\), encoded as integers \(0,\ldots,15\). Vertices \(v,w\) are adjacent exactly when they differ in one bit. By definition, a face is \(S\subseteq V(Q_4)\) with every connected component of the induced graph \(Q_4[S]\) containing at most two vertices. Since \(Q_4\) is triangle-free, equivalently every selected vertex has at most one selected neighbor. A face with \(q\) vertices has simplicial dimension \(q-1\). Orient its chain generator by increasing integer labels. The empty face is present for augmented chain computations.

This graph is also \(C_4\square C_4\), the **periodic** four-by-four square grid, not the nonperiodic \(4\times4\) rectangular grid. The result concerns only \(r=2\) and \(Q_4\); no formula for arbitrary cube dimension is asserted. The equivariant assertion is over \(\mathbb Q\), whereas the homotopy and ordinary homology assertions are integral.

## Proof
**1. Exhaustive face set.** Enumerate exactly the \(2^{16}\) vertex masks. Admit \(m\) exactly when for every selected \(v\), the intersection of \(m\) with \(\{v\oplus2^j:0\le j<4\}\) has at most one element. The resulting number of nonempty faces by dimensions \(0,\ldots,7\) is
\[
(16,120,464,964,960,440,80,10).
\]
There are \(3054\) nonempty faces and one empty face. The complex is nonpure: its facet dimensions \(3,5,7\) occur with multiplicities \(16,160,10\). The fact that all masks are checked—not just selected samples—is part of the supplied reproducibility algorithm.

**2. Acyclic discrete-Morse reduction.** On the augmented face poset, successively use the vertex toggles \(0,1,\ldots,15\): at stage \(v\), pair each still-unmatched face \(m\) not containing \(v\) with \(m\cup\{v\}\), provided both faces remain. Exactly \(1514\) pairs are formed. Direct an unmatched codimension-one incidence from coface to face, but reverse each matched incidence. Explicit topological sorting visits all \(3055\) nodes and all \(13584\) codimension-one incidences; hence the matching is acyclic. The unmatched faces comprise \(17\) three-faces, \(6\) four-faces, and \(4\) five-faces. Because the empty face is paired, the ordinary Morse CW model includes an additional base vertex, as in the augmented discrete-Morse convention.

**3. Exact oriented Morse boundaries.** Every simplex \(\{i_0<\cdots<i_q\}\) has boundary \(\sum_j(-1)^j\{i_0,\ldots,\widehat{i_j},\ldots,i_q\}\). Cancel the \(1514\) matched lower/upper generators, ordered by increasing dimension and then upper mask. Every actual pivot in the resulting integer matrices is \(\pm1\); use integer row elimination on the whole boundary system. Denote a critical cell by its integer vertex mask. The nonzero degree-four boundaries are precisely
\[
\partial[49442]=[49158]-[49162],\qquad
\partial[49682]=-[49158]+[49162].
\]
The four degree-five boundaries are
\[
\begin{aligned}
\partial[26904]&=-[10328],\\
\partial[26916]&=-[10340],\\
\partial[38424]&=-[5272]-[37442]+[49442]+[49682],\\
\partial[38530]&=[37442].
\end{aligned}
\]
All other degree-four boundaries and every degree-three boundary vanish. The degree-four-to-degree-three matrix has a unit rank-one image. The degree-five-to-degree-four matrix has a \(4\times4\) minor with rows \(5272,10328,10340,37442\) and columns \(26904,26916,38424,38530\) of determinant \(-1\). Therefore the degree-five matrix has rank four and a primitive image. The chain relation \(\partial^2=0\) is also verified exactly. The remaining reduced integral homology has ranks sixteen in degree three and one in degree four, without torsion.

**4. From homology to the full homotopy type.** The Morse CW model has one basepoint, no one- or two-cells, and exactly the critical cells described above. Its three-skeleton is a wedge of \(17\) three-spheres. The six attaching maps of four-cells lie in \(\pi_3(\bigvee^{17}S^3)\cong\mathbb Z^{17}\); their degree matrix has one primitive unit direction. A cellular change of basis and a homotopy cancellation remove one three/four-cell pair. The resulting four-skeleton is \(\bigvee^{16}S^3\vee\bigvee^5S^4\). All four five-cell attaching maps have a unimodular rank-four projection to the direct sum of the five \(\pi_4(S^4)\) factors. Such a primitive projection permits simultaneous homotopy cancellation of four four/five-cell pairs (any residual \(\pi_4\) components into the three-spheres can be absorbed by altering the four-sphere generators). The surviving complex is exactly \(\bigvee^{16}S^3\vee S^4\). This step uses the cell attachment data, not an invalid deduction that arbitrary homology ranks determine homotopy type.

**5. Symmetry.** For each of the \(384=2^4\cdot4!\) graph automorphisms \(g=(t,\pi)\), act on oriented simplices with the sorting-permutation sign. The critical four-cell mask \(5272\) lifts by reversing the exact eliminations to an integral simplicial cycle with \(92\) terms, each coefficient \(\pm1\). Direct computation checks that its simplicial boundary is zero and that the resulting class is a primitive generator of \(H_4\). For every \(g\), transport the cycle through the full oriented chain action and project through the same eliminations: the resulting multiple is \(\operatorname{sgn}(\pi)\). Thus \(\chi_4(t,\pi)=\operatorname{sgn}(\pi)\).

For degree three, enumerate every nonempty face preserved by \(g\), including its orientation sign, to obtain the simplicial Lefschetz number \(L(g)\). Since the only nonzero ordinary homology degrees are \(0,3,4\),
\[
\chi_3(g)=1+\chi_4(g)-L(g).
\]
For all \(384\) elements this agrees exactly with
\[
\chi_3(t,\pi)=\#\{j:\pi(j)=j\}
+\sum_{\substack{P\subseteq\{0,1,2,3\},\ |P|=2\\\pi(P)=P}}
(-1)^{\sum_{j\in P}t_j}
\#\{b\notin P:\pi(b)=b\}.
\]
Because \(\pi(P)=P\) within the sum, this is precisely the character of \(V\oplus W\) defined in the finding. Rational characters determine finite-dimensional \(\mathbb Q[B_4]\) modules. Averaging characters over translations leaves the four-dimensional \(V\) summand; subsequent averaging over \(S_4\) leaves one line. The degree-four sign character has no full-group invariant vector.

## Verification
Run `python3 verify.py` with Python 3.10 or later; it needs no external packages. The expected final line is `VERIFY_OK`. It enumerates all vertex masks; checks the full directed incidence graph for Morse acyclicity; constructs all oriented integer boundary matrices and exact unit cancellations; verifies the integral boundary minors and \(\partial^2=0\); independently computes original simplicial mod-two ranks; constructs and checks the primitive 92-term four-cycle; and evaluates the complete character comparison for all 384 symmetries. The embedded `verification_output.txt` records the tested program's output. The count of masks and full order of operations make the finite computations exhaustive and deterministic.

## Relationship to prior work
Zaker's 2015 preprint, arXiv:1507.07194, studies induced-subgraph vertex sets with maximum degree bounded by one (and more generally by a parameter), from the viewpoint of cardinality bounds; it does not compute the topology of the resulting simplicial complex. Salvetti's paper on \(d\)-independent graph complexes, DOI:10.1007/978-3-319-20155-9_22, relates such complexes to braid groups; its accessible abstract has no hypercube homotopy calculation, but the full source was not accessible and remains an overlap risk.

Deshpande and Singh, arXiv:2001.05448, define higher-independence complexes in this precise connected-component formulation and classify complete multipartite graphs, fully whiskered graphs, paths, cycles and rooted regular trees. Their inspected full text asks about grid graphs, explicitly using *nonperiodic* rectangular grids. Those classifications do not cover the periodic four-cube. Later work on chordal graphs likewise does not apply because \(Q_4\) has induced four-cycles. The ordinary independence complex \(\operatorname{Ind}_1(Q_4)\) is a different complex: its face predicate forbids every selected edge, rather than merely selected vertices of degree at least two.

## Limitations
This is a complete **finite** graph and one index \(r\), not an arbitrary-dimensional hypercube theorem or a claim of a general formula. The rational representation does not provide an integral representation classification. The proof depends on exact exhaustive computer-assisted finite verification, supplied in inspectable Python. The indexed and accessible literature search cannot prove global uniqueness, and Salvetti's plausible older full source was not inspected. Independent scientific audit and replication by a separate investigator have not been performed.

## References
- M. Zaker, *Lower bounds for independence and k-independence number of graphs using the concept of degenerate degrees*, arXiv:1507.07194, initially public 2015-07-26.
- M. Salvetti, *Some Combinatorial Constructions and Relations with Artin Groups*, DOI:10.1007/978-3-319-20155-9_22 (bibliographic year 2015; exact first-public day not independently established).
- P. Deshpande and A. Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types*, arXiv:2001.05448, 2020-01-15.
- F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy, and A. Singh, *Chordal Graphs, Higher Independence and Vertex Decomposable Complexes*, arXiv:2106.10863, 2021-06-21.
- R. Forman, *Morse Theory for Cell Complexes*, Adv. Math. 134 (1998), 90–145.
