# Integral inversion lattices and Euclidean Rips persistence of type-A root configurations

## Finding
Fix an integer \(n\ge 4\), and equip
\[
R_n=\{e_i-e_j\in\mathbb R^n:1\le i,j\le n,\ i\ne j\}
\]
with Euclidean chordal distance. Write \(K_r=\operatorname{VR}_{\le r}(R_n)\) for the inclusive Vietoris–Rips complex, \(m=\binom n2\), \(b=n(n-3)+1\), and \(k=n(n-3)/2\). Then the complete reduced **integral** homotopy sequence at all real \(r\ge0\) is
\[
K_r\simeq
\begin{cases}
\bigvee^{n(n-1)-1}S^0,&0\le r<\sqrt2,\\
\bigvee^b S^1,&\sqrt2\le r<2,\\
S^{n-2},&2\le r<\sqrt6,\\
S^{m-1},&\sqrt6\le r<2\sqrt2,\\
\ast,&r\ge2\sqrt2.
\end{cases}
\]
These stages give the complete all-coefficient-field barcode: the positive-degree intervals are \(b\) copies of \([\sqrt2,2)\) in degree one, one \([2,\sqrt6)\) in degree \(n-2\), and one \([\sqrt6,2\sqrt2)\) in degree \(m-1\). The \(n(n-1)-1\) finite reduced degree-zero bars die at \(\sqrt2\).

The natural group \(S_n\times C_2\) acts by coordinate permutations and central inversion \(\tau(v)=-v\). Its integral actions on the one-dimensional top homology groups of the two higher stages are respectively
\[
\sigma\mapsto\operatorname{sgn}(\sigma),\quad \tau\mapsto(-1)^{n-1}
\qquad\text{and}\qquad
\sigma\mapsto\operatorname{sgn}(\sigma)^{n-1},\quad \tau\mapsto(-1)^m.
\]
In the first nontrivial stage \(\sqrt2\le r<2\), \(H_1(K_r;\mathbb Z)\) has rank \(b\), and the full rational symmetry representation is
\[
H_1(K_r;\mathbb Q)\cong
\bigwedge\nolimits^2 U_n\;\oplus\;
\big(S^{(n-2,2)}\otimes\varepsilon\big),
\]
where \(U_n=\{(x_1,\ldots,x_n)\in\mathbb Q^n:\sum_i x_i=0\}\), \(\varepsilon\) is the sign of central inversion (trivial on \(S_n\)), and \(S^{(n-2,2)}\) denotes the indicated rational Specht module. Equivalently, if \(f\) is the number of fixed coordinates of \(\sigma\in S_n\), and \(t\) its number of two-cycles, then
\[
\operatorname{tr}(\sigma\mid H_1)=f^2-3f+1,
\qquad
\operatorname{tr}(\tau\sigma\mid H_1)=1-2t.
\]
The **integral strengthening** concerns the two primitive eigensublattices
\[
L^+=\ker(\tau-1\mid H_1(K_r;\mathbb Z)),\qquad
L^-=\ker(\tau+1\mid H_1(K_r;\mathbb Z)).
\]
They have ranks \(\binom{n-1}{2}\) and \(k\), yet their sum is not the complete lattice:
\[
\boxed{\ H_1(K_r;\mathbb Z)/(L^++L^-)\cong(\mathbb Z/2\mathbb Z)^k\ }.
\]
In particular, the two rational inversion eigenspaces give an index-\(2^k\) sublattice when intersected with integral homology. This exact integral obstruction is the principal refinement of the nonequivariant Rips types.

## Assumptions and scope
The parameters are all integers \(n\ge4\) and real \(r\ge0\). The Euclidean metric is the *ambient chordal* metric on the \(n(n-1)\) roots, not graph distance or spherical geodesic distance. Simplices require pairwise distance at most the inclusive threshold. All integral homology is ordinary singular homology of the geometric realization; \(H_1\) in the displayed lattice statements refers specifically to \(\sqrt2\le r<2\). Symmetric-group permutations act on coordinates and commute with \(\tau\). The assertions about the first, middle, and penultimate stages describe representations on their nonzero reduced homology; the homotopy equivalences themselves need not be equivariant homeomorphisms.

## Proof
**(1) Distance shells.** Each root has squared norm two. For distinct roots \(e_i-e_j\) and \(e_a-e_b\), the squared distance is \(4-2\langle e_i-e_j,e_a-e_b\rangle\). Their distinct-point inner products are \(1,0,-1,-2\), so the only nonzero squared distances are \(2,4,6,8\), and each occurs for \(n\ge4\). The initial and final phases follow immediately.

**(2) The first phase is a crown graph.** At squared threshold two, two distinct roots are adjacent exactly when they have the same positive endpoint or the same negative endpoint. Thus \(K_{\sqrt2}\) is the clique complex of the line graph of the connected bipartite crown graph \(\Gamma_n\), whose vertices are \(L_1,\ldots,L_n,R_1,\ldots,R_n\) and edges \(L_iR_j\) for \(i\ne j\). Every clique of a line graph of a bipartite graph is contained in an edge star. The star cliques form a cover by simplices with all multiple intersections either a vertex or empty. Its nerve is \(\Gamma_n\), hence the nerve lemma gives \(K_{\sqrt2}\simeq\Gamma_n\). The crown has \(2n\) vertices, \(n(n-1)\) edges, and is connected for \(n\ge3\). Therefore \(\beta_1=n(n-1)-2n+1=b\), with free integral homology. The cover is invariant under coordinate permutations and under interchange \(L_i\leftrightarrow R_i\), so the induced \(S_n\times C_2\)-action is that on the crown graph.

**(3) The middle phase is the type-A root-polytope sphere.** At squared threshold four, a set of distinct directed roots \(e_i-e_j\) is a clique if and only if no index occurs among both its positive endpoints and its negative endpoints. Indeed, equal positive endpoints or equal negative endpoints give squared distance two, disjoint endpoints give four, and an index occurring positively in one root and negatively in another gives squared distance six or eight. For a nonempty simplex \(F\), write \(A(F)\) for its positive endpoints and \(B(F)\) for its negative endpoints. These are disjoint and nonempty, and
\[
F\subseteq\{e_i-e_j:i\in A(F),\ j\in B(F)\}=:\mathcal R(A(F),B(F)).
\]
Taking the indicated rectangular closure is an ascending, idempotent, order-preserving map on the face poset; its image is the poset of all nonempty \(\mathcal R(A,B)\) with nonempty disjoint \(A,B\). This is exactly the face poset of the boundary of the type-A root polytope \(P_n=\operatorname{conv}(R_n)\): a nonconstant linear functional \(x\mapsto\sum c_i x_i\) is maximized on precisely the roots with \(i\) among the largest coordinates of \(c\) and \(j\) among its smallest, and every disjoint nonempty pair \(A,B\) is attained using values \(1,-1,0\). By the order-homotopy theorem, the barycentric subdivision of \(K_2\) retracts up to homotopy onto the order complex of this closure image, hence \(K_2\simeq\partial P_n\). The root polytope is full-dimensional in the hyperplane \(\sum x_i=0\), of dimension \(n-1\); its boundary is \(S^{n-2}\). Since the closure commutes with all coordinate permutations and with \(\tau\), the induced fundamental orientation class transforms by the determinant on that hyperplane: \(\operatorname{sgn}(\sigma)\) for permutations and \((-1)^{n-1}\) for inversion.

**(4) The penultimate sphere.** At squared threshold six, exactly the \(m\) pairs \(\{e_i-e_j,e_j-e_i\}\) remain nonedges. Hence \(K_{\sqrt6}\) is precisely the join of \(m\) discrete two-point sets, a triangulated \(S^{m-1}\). The inversion \(\tau\) exchanges the two vertices in every pair and has determinant \((-1)^m\) on top homology. A transposition of coordinate labels permutes the \(m\) antipodal pairs with sign \((-1)^{n-2}\) and reverses one of those pairs. Its total degree is therefore \((-1)^{n-1}\); since transpositions generate \(S_n\), the top character is \(\operatorname{sgn}(\sigma)^{n-1}\).

**(5) The degree-one rational character and decomposition.** Orient each crown edge \(L_iR_j\) from left to right and index it by \((i,j)\). Coordinate permutations carry \((i,j)\) to \((\sigma i,\sigma j)\) without orientation reversal; inversion carries it to the negative of \((j,i)\). Because the crown graph is connected, its equivariant rational cellular chain groups satisfy \([H_1]=[C_1]-[C_0]+[\mathbf1]\). An ordinary permutation fixing \(f\) labels fixes \(f(f-1)\) directed edges and \(2f\) vertices, yielding \(f^2-3f+1\). The composed inversion-permutation fixes no vertices and fixes with negative sign the two directed edges associated with every two-cycle of \(\sigma\), yielding \(1-2t\).

For an intrinsic decomposition, on the \(+1\) inversion chain space, antisymmetric edge coefficients form \(\bigwedge^2\mathbb Q^n\), and the graph boundary is the usual contraction by the all-ones covector; its kernel is \(\bigwedge^2U_n\). On the \(-1\) inversion chain space, symmetric edge coefficients form the permutation module on unordered two-subsets, and the boundary is the unsigned vertex-incidence map to \(\mathbb Q^n\). This map is surjective for \(n\ge3\): its annihilator consists of vectors satisfying \(a_i+a_j=0\) for every \(i\ne j\), hence is zero. Its kernel is the classical Specht summand \(S^{(n-2,2)}\) in \(\mathbb Q[\binom{[n]}2]\cong\mathbf1\oplus U_n\oplus S^{(n-2,2)}\). The two eigenspace ranks are respectively \(g=\binom{n-1}2\) and \(k=n(n-3)/2\).

**(6) Exact integral index of the inversion eigensublattices.** Let \(L=H_1(\Gamma_n;\mathbb Z)\), an integral cycle lattice, and write \(L^+=\ker(\tau-1)\), \(L^-=\ker(\tau+1)\). Because \(L^+\) is the kernel of a map between free abelian groups, it is primitive: \(L^+\cap 2L=2L^+\). The map
\[
L\longrightarrow L^+/2L^+,
\qquad x\longmapsto(1+\tau)x\bmod 2L^+
\]
has kernel precisely \(L^++L^-\): if \((1+\tau)x=2a\) for \(a\in L^+\), then \(x-a\in L^-\); the converse is immediate. Accordingly, the desired quotient is an elementary abelian two-group of rank equal to the rank of \((1+\tau)\) on \(L/2L\).

Reduce the crown chain complex modulo two. Its edge chains have basis \((i,j)\) for \(i\ne j\); \(\tau(i,j)=(j,i)\) in characteristic two. Since \(L/2L\cong H_1(\Gamma_n;\mathbb F_2)\), the kernel of \(1+\tau\) consists of symmetric edge cycles \(a_{ij}=a_{ji}\). The graph boundary condition then says \(\sum_{j\ne i}a_{ij}=0\) for every \(i\). This is exactly the mod-two cycle space of the ordinary complete graph on \(n\) labels, with \(m\) edges and rank of boundary \(n-1\), hence dimension \(g=m-n+1\). Rank-nullity on \(L/2L\) (dimension \(b=2m-2n+1\)) gives
\[
\operatorname{rank}_{\mathbb F_2}(1+\tau)=b-g=m-n=k.
\]
Thus \(L/(L^++L^-)\cong(\mathbb Z/2)^k\), and the exact index is \(2^k\). This completes the integral statement for **every** \(n\ge4\).

## Verification
Run `python3 verify_type_a_rips.py` with Python 3 and no external libraries. The verifier independently constructs every root pair and distance shell for \(4\le n\le7\); validates the squared-distance-two clique-star criterion and the squared-distance-four separation criterion; constructs a deterministic integral spanning-tree cycle basis of the crown for \(4\le n\le12\), checks every cycle's signed boundary, constructs the full integer involution matrix, checks its square equals the identity and its trace is one, and computes the exact rank of its mod-two norm map. It independently checks the two character formulas for **every** permutation when \(4\le n\le7\). Expected final marker: `VERIFY_OK_TYPE_A_EUCLIDEAN_RIPS_INTEGRAL_EIGENLATTICE`. All-range conclusions are mathematical deductions in the preceding proof, not extrapolations from these finite checks.

## Relationship to prior work
Babson and Kozlov, *Complexes of graph homomorphisms* (first public 2003-10-05), study \(\operatorname{Hom}(K_2,K_n)\simeq S^{n-2}\) and its involution; the rectangular face poset identified in step (3) is the face structure of that classical Hom complex. Accordingly the middle-stage sphere and swap action are not presented as independent newly discovered topological phenomena. Ardila, Beck, Hoşten, Pfeifle, and Seashore, *Root polytopes and growth series of root lattices* (first public 2008-09-30), determine type-A root-polytope boundary triangulations, not the metric filtration or its degree-one integral involution lattice. The previously published complete Euclidean cuboctahedral Rips filtration treats precisely the \(n=4\) specialization and already states its homotopy types and interval thresholds. Those known assertions are explicitly excluded from novelty for that case.

The proposed additional content is the **uniform all-rank metric identification together with the exact integral eigenlattice quotient**, both rational representation summands and character values, and their compatibility with the later orientation representations. The integral index is a covering-graph cycle-lattice computation, not a claim of an independent published priority determination. Searches comparing root-system aliases, crown double covers, dual formulations, published-finding corpus records, and the inspected primary full texts found no direct statement of this combined integral index in the Euclidean type-A Rips setting. Equivalence to an unindexed general theorem about eigensublattices of graph-covering homology remains a residual literature risk.

## Limitations
The result concerns the full, unrescaled type-A root set with Euclidean chordal distance, not a positive-root subset, a root-polytope surface sample, geodesic distances, type-B or type-D roots, or arbitrary root configurations. It gives homotopy types and homology representations, not a natural equivariant *homotopy-equivalence of spaces* at each stage or inter-stage equivariant persistent-module generators. Novelty is conditional on the inspected sources; in particular the full \(n=4\) filtration and the Hom-complex sphere have clear prior coverage. The integer index may be recoverable from broader graph-covering algebra not located during literature comparison. Independent scientific validation has not been performed.

## References
1. E. Babson and D. N. Kozlov, *Complexes of graph homomorphisms*, arXiv:math/0310056, first posted 2003-10-05, https://arxiv.org/abs/math/0310056.
2. F. Ardila, M. Beck, S. Hoşten, J. Pfeifle, and K. Seashore, *Root polytopes and growth series of root lattices*, arXiv:0809.5123, first posted 2008-09-30, https://arxiv.org/abs/0809.5123.
3. *Complete Vietoris–Rips filtration of the Euclidean cuboctahedron*, published-finding corpus publicly indexed record, 2026-10-04, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-complete-vietoris-rips-filtration-of-the-euclidean-cuboctahedron--c10ad684de7e.
