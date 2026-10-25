# The exceptional rational homology module of two unordered particles on the Heawood graph

## Finding
Let \(H\) be the point--line incidence graph of the Fano projective plane and let \(X=\operatorname{UConf}_2(|H|)\) be the space of unordered pairs of distinct points of its geometric realization. The collineation group \(G=\mathrm{GL}_3(\mathbb F_2)\) acts on \(X\). There is an isomorphism of rational \(G\)-representations
\[
H_2(X;\mathbb Q)\cong W_6\oplus\operatorname{St}_8,
\]
where \(\operatorname{St}_8\) is the eight-dimensional Steinberg representation and \(W_6\) is the six-dimensional irreducible over \(\mathbb Q\) whose scalar extension to \(\mathbb C\) is the direct sum of the two Galois-conjugate, three-dimensional irreducibles. Equivalently, the character of \(H_2\) on the elements of orders \(1,2,3,4,7\), respectively, is \((14,-2,-1,2,0)\); both distinct classes of order seven have trace zero. There are no nonzero \(G\)-invariant rational degree-two classes.

For completeness, the integral homology is
\[
H_i(X;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=0,\\
\mathbb Z^8\oplus\mathbb Z/2,&i=1,\\
\mathbb Z^{14},&i=2,\\
0,&i>2.
\end{cases}
\]
The nonequivariant homology is a verification datum; the representation splitting is the focus of the finding.

## Assumptions and scope
The seven points of the Fano plane are nonzero vectors \(p\in\mathbb F_2^3\), the seven lines are nonzero covectors \(\ell\), and \(p\) is adjacent to \(\ell\) exactly when \(\ell(p)=0\). This defines a 14-vertex, 21-edge, cubic graph of girth six. The collineation action sends \(p\) to \(Ap\) and \(\ell\) to \(A^{-T}\ell\) for every \(A\in G\) and fixes neither particle label (the particles are unordered). The finite cubical model uses the original graph cellulation, with two particle supports required to have disjoint closures.

The usual Abrams graph-discretization hypotheses hold for two particles: any path between distinct vertices of valence other than two has at least one edge, and every simple cycle has at least three edges. Therefore the cubical unordered discrete-configuration model is homotopy equivalent to the continuous configuration space [1,2]. All conclusions concern ordinary singular homology of this space and its specified subgroup \(G\) of graph automorphisms.

## Proof
**Integral chain complex.** In the unordered Abrams cube complex, degree-zero cells are unordered distinct vertex pairs, degree-one cells consist of an oriented edge with a vertex not incident to it, and degree-two cells are unordered pairs of disjoint edges. Their respective counts are exactly \((91,252,168)\). Orient each graph edge from its smaller indexed endpoint to its larger one; orient a square by increasing ordered edge index. If \(e=(a,b)\), the boundary of \((e,v)\) is \((b,v)-(a,v)\). If \(e=(a,b)\) and \(f=(c,d)\) have disjoint closures, the boundary of the oriented square \((e,f)\) is \((f,b)-(f,a)-(e,d)+(e,c)\). These conventions yield exact integral boundary matrices \(\partial_1\) and \(\partial_2\) satisfying \(\partial_1\partial_2=0\).

The rank of \(\partial_1\) is 90. Exact integer Smith reduction of the \(252\times168\) matrix \(\partial_2\) yields 153 diagonal ones, one diagonal two, and fourteen zero columns. Thus \(\ker\partial_2\cong\mathbb Z^{14}\), while \(H_1\) has free rank \(252-90-154=8\) and one element of order two. There are no cells above dimension two. The free quotient \(\operatorname{im}\partial_1\) ensures torsion of \(\operatorname{coker}\partial_2\) agrees with torsion of \(H_1\). This proves the integral homology statements.

**First-homology representation.** Sending the moving edge of a particle one-cell to that edge of \(H\), and sending a particle zero-cell to the sum of its two graph vertices, gives the natural sum-of-trajectories chain map from the cubical configuration space to the graph. It is \(G\)-equivariant and annihilates \(\operatorname{im}\partial_2\). Over \(\mathbb F_{101}\), the rank of the matrix formed by stacking \(\partial_1\) with the 21-row edge-projection matrix is 98, whereas the rank of \(\partial_1\) is 90. Therefore the induced first-homology map has rank at least eight over \(\mathbb Q\). Both source and target have rational dimension eight, so it is a \(G\)-module isomorphism. In particular \(H_1(X;\mathbb Q)\cong H_1(H;\mathbb Q)\cong\operatorname{St}_8\). The graph-chain formula for the first-homology character is \(\chi_{H_1(H)}(g)=1-\operatorname{tr}(g\mid C_0(H))+\operatorname{tr}(g\mid C_1(H))\), with the edge orientation signs included.

**Degree-two equivariant character.** Enumerating the 168 invertible binary three-by-three matrices and their induced permutations of points and dual lines gives element-order multiplicities \((1,21,56,42,48)\) for orders \((1,2,3,4,7)\). For each element, the signed action on cubical chains is an integral signed permutation action, including the sign when two square directions exchange. The signed cellular Lefschetz identity gives
\[
\chi_{H_2}(g)=\operatorname{tr}(g\mid C_0(X))-\operatorname{tr}(g\mid C_1(X))
+\operatorname{tr}(g\mid C_2(X))-1+\chi_{H_1}(g).
\]
Exact enumeration gives the first-homology character \((8,0,-1,0,1)\) and second-homology character \((14,-2,-1,2,0)\), constant on both order-seven classes. Under \(G\cong\mathrm{PSL}_2(7)\), the first is the Steinberg irreducible \(\operatorname{St}_8\), and the difference \((6,-2,0,2,-1)\) equals the sum of the two conjugate complex degree-three characters. Their rational realization is \(W_6\). Comparison with the classical six-column character table of this finite simple group establishes the claimed rational decomposition. The average of the degree-two character over all 168 group elements is zero, giving no invariant vectors.

**Independent finite verification of the character.** In addition to computing the signed cellular Lefschetz traces, the verifier computes a 14-vector echelon basis for \(\ker(\partial_2\bmod101)\) and directly restricts every one of the 168 group actions to that kernel. The resulting trace agrees, after integer lifting, with the characteristic-zero Lefschetz value for every element. The exact Smith computation and characteristic-three and characteristic-101 rank checks independently bound possible characteristic-dependent rank errors; mod-two ranks detect the single two-torsion term.

## Verification
Execute `python heawood_conf2_verify.py` using Python 3.10 or newer and SymPy. The script constructs all matrices from the defining incidence relation, checks the chain identity, computes integer Smith invariant factors and modular ranks, checks the action of every collineation, and prints `VERIFY_OK` only after all assertions succeed. The recorded output in `heawood_conf2_verify_output.txt` can be compared byte-for-byte with a fresh run. The program uses no external downloaded data and no numerical tolerance.

## Relationship to prior work
Ghrist's 1999 paper [1] introduced graph-configuration topology in robotics; Abrams and Ghrist [2] developed the graph-configuration construction. Barnett and Farber [3] study the **ordered** two-point configuration space and intersection pairings, not this specific unordered collineation representation. Ko and Park [4] establish general first-homology and nonequivariant Betti information for graph braid groups, including nonplanar torsion phenomena. Their nonequivariant results do not determine the 14-dimensional rational action, which is the specific refinement here. The full character also differs in object from results on Heawood independence or matching complexes and from topological representations for Petersen and dodecahedral configuration spaces.

## Limitations
The result concerns the indicated 168-element collineation subgroup, not a claim to have decomposed every representation of the entire 336-element Heawood automorphism group. No presentation of the fundamental group or equivariant integral lattice classification is asserted. The finite verifier and self-review are reproducible mathematical evidence, not an independent audit. Equivalent calculations may exist in unindexed historical literature; absence from the queried sources is not a proof of priority.

## References
[1] R. Ghrist, *Configuration spaces and braid groups on graphs in robotics*, arXiv:math/9905023, first public version 1999-05-05, https://arxiv.org/abs/math/9905023.

[2] A. Abrams and R. Ghrist, *Finding topology in a factory: configuration spaces*, arXiv:math/0009118, first public version 2000-09-12, https://arxiv.org/abs/math/0009118.

[3] K. Barnett and M. Farber, *Topology of configuration space of two particles on a graph, I*, arXiv:0903.2180, first public version 2009-03-12, https://arxiv.org/abs/0903.2180.

[4] K. H. Ko and H. W. Park, *Characteristics of graph braid groups*, arXiv:1101.2648, first public version 2011-01-13, https://arxiv.org/abs/1101.2648.

[5] Character table of \(\mathrm{PSL}_2(7)\), including the two conjugate degree-three characters and the degree-eight Steinberg character, available at https://en.wikipedia.org/wiki/PSL(2,7) (used for identification only; the character calculation is reproduced independently).
