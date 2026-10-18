# Irreducible full-symmetry homology of two-particle configurations on balanced complete bipartite graphs

## Finding
For every pair of integers \(m,n\geq 3\), let \(G=K_{m,n}\) be the geometric realization of the ordinary complete bipartite graph, and let \(X_{m,n}=\operatorname{UConf}_{2}(G)\) be the space of *unordered distinct* pairs of points on it. Denote by \(V_r=S^{(r-1,1)}\) the standard rational representation of \(S_r\); let \(W_r=S^{(r-2,2)}\) for \(r\geq4\), with \(W_3=0\); and let \(Z_r=S^{(r-2,1,1)}\) for \(r\geq3\). These symbols denote ordinary Specht modules over \(\mathbb Q\), and \(\boxtimes\) denotes the outer tensor product for \(S_m\times S_n\).

There are isomorphisms of rational \(S_m\times S_n\)-representations
\[
H_1(X_{m,n};\mathbb Q)\cong V_m\boxtimes V_n,\qquad
H_2(X_{m,n};\mathbb Q)\cong
(W_m\boxtimes Z_n)\oplus(Z_m\boxtimes W_n).
\]
Furthermore \(H_i(X_{m,n};\mathbb Q)=0\) for \(i>2\), and \(H_0\cong\mathbb Q\). For \(m=n=r\geq4\), the **entire second homology is an irreducible rational representation** of the full automorphism group
\[
\operatorname{Aut}(K_{r,r})=(S_r\times S_r)\rtimes C_2,
\]
where the last factor exchanges the bipartition classes. Every element exchanging the two classes has trace zero on second rational homology. At \(r=3\) this second homology vanishes, so the nonzero irreducibility statement is restricted to \(r\geq4\).

In particular,
\[
\dim H_2(X_{m,n};\mathbb Q)=
\frac{m(m-3)(n-1)(n-2)+(m-1)(m-2)n(n-3)}4,
\]
with this polynomial valid at \(m=3\) or \(n=3\) as well. The balanced cases \(r=4,5\) have dimensions \(12,60\), respectively. For an element \((\sigma,\tau)\in S_m\times S_n\), its second-homology character is
\[
\chi_2(\sigma,\tau)=w_m(\sigma)z_n(\tau)+z_m(\sigma)w_n(\tau),
\]
where, if \(f\) is the number of fixed points and \(t\) the number of transpositions among the disjoint cycles of a permutation,
\[
w_r=\binom f2+t-f,\qquad z_r=\binom f2-t-f+1.
\]

## Assumptions and scope
All graphs are finite simple graphs with each edge realized as a closed unit interval. Configurations are unordered and collisions are *forbidden everywhere*, including graph vertices; this is not a sink-configuration model. The group \(S_m\times S_n\) independently permutes the two bipartition classes. If \(m=n\), its index-two extension by class exchange is the full graph automorphism group. Coefficients in all representation statements are \(\mathbb Q\). The nonplanarity and three-vertex connectivity assumptions used below hold because \(m,n\geq3\).

The standard two-particle Abrams cubical model has cells corresponding to unordered collections of two graph vertices/edges with pairwise disjoint *closures*. For these graphs it is a homotopy model of the continuous configuration space. Its only nonzero cellular chain groups occur in dimensions zero through two. Its action is cellular and commutes with all graph automorphisms.

## Proof
**1. Equivariant cellular chains.** Let \(U_r=\mathbb Q^{[r]}\) be the natural vertex permutation representation, \(P_r=\mathbb Q^{\binom{[r]}2}\) the permutation representation on unordered distinct vertex pairs, \(O_r=\mathbb Q^{\{(i,j):i\ne j\}}\) that on ordered distinct pairs, and \(D_r=\bigwedge^2U_r\). All are actual representations of \(S_r\).

In the Abrams model, a zero-cell chooses two distinct vertices, a one-cell chooses a graph edge and a vertex disjoint from its closure, and a two-cell chooses two vertex-disjoint edges; the orientation of a two-cell changes sign when its two edge factors are exchanged. Reading the respective \(S_m\times S_n\)-actions gives
\[
\begin{aligned}
C_0&=(P_m\boxtimes\mathbf1)\oplus(U_m\boxtimes U_n)\oplus(\mathbf1\boxtimes P_n),\\
C_1&=(O_m\boxtimes U_n)\oplus(U_m\boxtimes O_n),\\
C_2&=(D_m\boxtimes P_n)\oplus(P_m\boxtimes D_n).
\end{aligned}
\]
To verify the less immediate last identity, fix unordered pairs of distinct vertices from each side. There are exactly two ways to join these four vertices by two disjoint edges. Swapping the selected vertices on the first side interchanges the two matchings *with an orientation minus sign*, while swapping those on the second side interchanges them *without that sign*. The two-dimensional fiber is therefore the direct sum of the \(\mathrm{sign}\boxtimes\mathrm{triv}\) and \(\mathrm{triv}\boxtimes\mathrm{sign}\) stabilizer modules. Inducing these two modules over all pairs yields precisely \(D_m\boxtimes P_n\) and \(P_m\boxtimes D_n\). This also fixes all orientation conventions.

**2. The first homology module.** There is a natural total-motion homomorphism \(H_1(X_{m,n};\mathbb Q)\longrightarrow H_1(K_{m,n};\mathbb Q)\): for each one-cell with a moving particle on an oriented edge and the other particle fixed at a disjoint vertex, record the oriented moving edge. It is a cellular chain map after sending each zero-cell to the sum of its two vertices and sending two-cells to zero. Every graph cycle is a sum of four-cycles, and every four-cycle in \(K_{m,n}\) admits a vertex outside it when \(m,n\geq3\); holding one particle at that vertex and moving the other around the four-cycle proves surjectivity.

The theorem of Ko and Park for three-connected nonplanar graphs computes the first integral homology of the unordered two-strand graph braid space as \(\mathbb Z^{\beta_1(G)}\oplus\mathbb Z/2\), with \(\beta_1(K_{m,n})=(m-1)(n-1)\). Consequently the surjection just constructed is an isomorphism over \(\mathbb Q\). Under independent side permutations, the graph cycle space is the kernel of both row and column sums in the edge module \(U_m\boxtimes U_n\), namely \(V_m\boxtimes V_n\). Hence \(H_1(X_{m,n};\mathbb Q)\cong V_m\boxtimes V_n\).

**3. Exact determination of second homology.** The elementary Specht decompositions are
\[
\begin{aligned}
U_r&=\mathbf1\oplus V_r,\\
P_r&=\mathbf1\oplus V_r\oplus W_r,\\
D_r&=V_r\oplus Z_r,\\
O_r&=\mathbf1\oplus2V_r\oplus W_r\oplus Z_r.
\end{aligned}
\]
They hold for \(r=3\) with the indicated zero-module convention. Equivariant Euler–Poincaré in the rational representation ring is
\[
[H_2]=[C_2]-[C_1]+[C_0]-[H_0]+[H_1].
\]
Substitute the three explicitly established chain representations, \(H_0=\mathbf1\boxtimes\mathbf1\), and the just-proved first homology. Collecting terms cancels everything except \([W_m\boxtimes Z_n]+[Z_m\boxtimes W_n]\). Every rational representation of a finite group is semisimple, so equality of their Grothendieck classes is an actual representation isomorphism. The displayed character and dimension formulas follow from the hook-length formulas and the usual permutation characters of \(U_r,P_r,\bigwedge^2U_r\).

**4. Full automorphism-group irreducibility for a square board.** Fix \(r\geq4\) and the index-two normal subgroup \(H=S_r\times S_r\) in \(G=H\rtimes C_2\). Both \(W_r\boxtimes Z_r\) and \(Z_r\boxtimes W_r\) are irreducible \(H\)-modules, they are nonisomorphic because \(W_r\not\cong Z_r\), and the class-exchanging involution conjugates them into each other. The restriction of \(H_2\) to \(H\) is exactly their direct sum, with multiplicity one apiece. Any nonzero \(G\)-invariant subspace is an \(H\)-submodule and therefore contains one of these irreducible constituents; invariance under class exchange then forces it to contain both. Thus the whole \(G\)-module is irreducible. The class exchanger is off-diagonal relative to the two summands, so its composition with any \(H\)-element has trace zero. This proves the full-group assertion.

## Verification
The standalone `verify.py` constructs the actual unoriented-cell indexes and oriented cellular boundaries in dimensions zero, one and two. It first checks every incidence of \(\partial_1\partial_2=0\), then computes ranks and kernel bases by exact modular row reduction over the prime field with 1009 elements. Seven pairs of sizes were checked: \((3,3),(3,4),(3,5),(4,4),(4,5),(5,5),(5,6)\), yielding second Betti numbers \(0,2,5,12,27,60,104\). In the four cases \((3,3),(3,4),(4,4),(4,5)\), every side-preserving permutation was applied to the signed cellular two-cycles and its trace compared to the closed character formula. For the two balanced cases, every additional class-exchanging permutation was tested as well. In total this makes **4,248** direct signed homology character comparisons, all agreeing. These finite checks test the signs, boundaries, and representation formulas; the proof for all sizes is the four-step argument above, not extrapolation from the tests.

## Relationship to prior work
Farber–Hanbury established the mature-graph framework for two-point graph configuration spaces, including complete bipartite examples. Ko–Park determined first homology of braid spaces of three-connected nonplanar graphs, which is used in Step 2; no novelty is claimed for that rank. Ramos–Yun (2026), especially Section 3.3 and Theorem 3.17, computed the **diagonal** \(S_r\)-representation of unordered two-particle configuration homology of \(K_{r,r}\); their action simultaneously permutes paired labels on both sides. Its group is a proper subgroup of \(S_r\times S_r\), not the full automorphism group. Their result does not specify the two independent-side Specht factors, the arbitrary rectangular case, or the irreducibility and zero-swapping-trace statement for the whole wreath-product group. For example, at \(r=4\) restriction to the diagonal gives \(2S^{(3,1)}\oplus2S^{(2,1,1)}\), agreeing with the unordered part of their Table 3. Restricting our \(S_r\times S_r\) formula to their diagonal action is compatible with their published decomposition, but that restriction does not recover the extension uniquely. The construction here determines the finer representation in the actual full-group setting.

## Limitations
This gives rational homology representations, not a calculation of integral torsion in degree one beyond Ko–Park's cited theorem, nor the integral equivariant module structure of degree two. It does not determine the cohomology ring or the homotopy type. The representation-theoretic novelty claim is subject to potential independently discovered or unindexed fuller-group calculations. The Abrams cubical model is used only in its known range of validity for these graphs. No independent scientific audit is asserted.

## References
1. M. Farber and E. Hanbury, *Topology of configuration space of two particles on a graph, II*, arXiv:1005.2300v1 (first publicly posted 2010-05-13), https://arxiv.org/abs/1005.2300.
2. K. H. Ko and H. W. Park, *Characteristics of graph braid groups*, arXiv:1101.2648v1 (first publicly posted 2011-01-13), https://arxiv.org/abs/1101.2648; see the first-homology calculation for three-connected nonplanar graphs.
3. E. Ramos and C. He Yun, *Computing stable homology representations of graph configuration spaces*, arXiv:2606.13813v1 (first publicly posted 2026-06-11), https://arxiv.org/abs/2606.13813; compare Section 3.3, especially Theorem 3.17.
