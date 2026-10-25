# Paired-domination slides of triangular graphs as square-bouquet token swaps

## Finding
Let \(k\ge1\), put \(n=3k+1\), and let \(T_n=L(K_n)\) be the triangular graph: its vertices are unordered pairs from \([n]\), adjacent when they intersect. A paired-dominating set is a dominating vertex set whose induced graph has a perfect matching. Its *optimal slide graph* \(\mathcal P_k\) has all minimum paired-dominating sets as vertices; two such sets are adjacent when one vertex of \(T_n\) is replaced by an adjacent vertex while preserving minimum paired domination.

**Structural theorem.** The paired-domination number is \(\gamma_{\mathrm{pr}}(T_n)=2k\). Every optimum is uniquely a disjoint union of \(k\) two-edge stars \(P_3\) on \(3k\) of the original \(n\) labels, together with one unused label. These optima number
\[
N_k=\frac{(3k+1)!}{2^k k!}.
\]
The graph \(\mathcal P_k\) is connected, vertex-transitive, \(4k\)-regular, and has exactly \(2kN_k\) edges and \(2kN_k/3\) triangles. It is the simple quotient of the labeled token-swapping graph on a bouquet of \(k\) squares, identified by permutations of its squares and reflection of individual squares that fix their shared hub.

For the first three orders of this tight-coverage family, exhaustive shortest-path certificates determine the diameter exactly:
\[
\operatorname{diam}(\mathcal P_1)=3,\quad
\operatorname{diam}(\mathcal P_2)=6,\quad
\operatorname{diam}(\mathcal P_3)=10.
\]
The corresponding orders of the slide graphs are \(12\), \(630\), and \(75{,}600\); the edge counts are \(24\), \(2{,}520\), and \(453{,}600\). Each graph is self-centered by vertex transitivity. No all-order diameter formula is asserted.

## Assumptions and scope
All graphs are finite and simple, and the \(n\) vertices of \(K_n\) are distinctly labeled. The phrase *two-edge star* means the graph with three vertices and two edges meeting at a unique center. A dominating set of \(T_n\) need not be independent; paired domination demands only a perfect matching in the induced subgraph on selected vertices. A *slide* replaces one selected edge \(e\) of \(K_n\) by an unselected edge \(f\) satisfying \(e\cap f\ne\varnothing\); all other selected edges remain unchanged. Feasibility and optimum cardinality must hold at each endpoint. The universal theorem concerns exactly \(n\equiv1\pmod3\), \(n\ge4\). The finite distance statements concern only \(n\in\{4,7,10\}\).

## Proof
**Domination translation.** Regard a set \(D\subseteq V(T_n)\) as a selected edge set of \(K_n\), and let \(U(D)\) be the union of its endpoints. Then \(D\) dominates \(T_n\) if and only if \(|[n]\setminus U(D)|\le1\). Indeed, two unused labels determine an edge disjoint from every selected edge; conversely, if at most one label is unused, every edge meets some selected edge (or is itself selected).

**Sharp lower bound and equality.** A perfect matching in \(T_n[D]\), for \(|D|=2r\), partitions the selected edges of \(K_n\) into \(r\) pairs of intersecting edges. Each such pair occupies precisely three labels, so \(|U(D)|\le3r\). Domination therefore forces \(3r\ge n-1=3k\), hence \(r\ge k\). The disjoint union of \(k\) two-edge stars on \(3k\) labels is paired-dominating, proving the minimum is \(2k\). At equality, the \(k\) three-label supports have total size \(3k\); because their union must have at least \(3k\) labels, these supports are pairwise disjoint. The selected graph is therefore exactly the asserted star forest with a unique hole. Conversely every such forest is feasible. Its unique star decomposition yields the count by selecting the hole, partitioning the rest into unlabeled triples, then choosing one of three centers per triple:
\[
(3k+1)\frac{(3k)!}{(3!)^k k!}\,3^k=\frac{(3k+1)!}{2^k k!}.
\]

**Complete move classification.** In a configuration choose a star centered at \(c\), with leaves \(x,y\), and denote the unique unused label by \(h\). If its selected edge \(cx\) is removed, all other star components remain intact, including the edge \(cy\). For the result to be another disjoint star forest with one hole, the inserted edge can use only the labels \(c,x,y,h\); any attachment to a different star makes a component having more than two selected edges or leaves the edge \(cy\) isolated. The only feasible insertions that share a label with the removed edge are \(ch\) and \(xy\). The first exchanges hole \(h\) with leaf \(x\) while keeping center \(c\); the second exchanges center \(c\) with leaf \(y\), leaving the hole fixed. Removing \(cy\) gives the two analogous moves. Thus every one of the \(k\) stars contributes four distinct slides; \(\deg_{\mathcal P_k}=4k\).

**Square-bouquet model and connectivity.** Form a graph \(B_k\) from \(k\) copies of \(C_4\) by identifying one vertex of every copy into a distinguished hub \(H\). In square \(i\), write the other positions \(L_i,C_i,R_i\), with edges \(H L_i,L_i C_i,C_i R_i,R_i H\). Place the \(3k+1\) distinct labels bijectively on these positions, then take the \(k\) stars with centers at \(C_i\), leaves at \(L_i,R_i\), and hole at \(H\). Swapping labels along \(H L_i\) or \(H R_i\) is exactly a hole-leaf slide; swapping along \(C_iL_i\) or \(C_iR_i\) is exactly a center-leaf slide. Two position-labelings give the same star forest precisely when they differ by permutations of the square petals or swapping the two leaves of a petal. This proves the stated quotient description. The edge transpositions of a connected graph generate the full symmetric group on its positions (transport along a path), so token swaps on \(B_k\) join any two position-labelings; the quotient slide graph is connected. Relabeling \([n]\) acts transitively on all star forests, proving vertex transitivity.

**Edges and triangles.** The handshake lemma gives \(|E(\mathcal P_k)|=2kN_k\). Two different neighbors of a configuration can themselves be adjacent only when their moves concern the same star: moves concerning distinct stars alter two different original selected edges with incompatible replacement edges. Within each star, the two alternative hole-leaf moves have adjacent outputs, as do the two alternative center-leaf moves; no mixed pair of moves has adjacent outputs. Thus every configuration lies in exactly \(2k\) triangles. Dividing by three gives \(2kN_k/3\) triangles.

**Finite distances.** Vertex transitivity makes the diameter equal to the eccentricity of one arbitrary configuration. The included enumerators construct all \(N_k\) configurations and every legal slide for \(k=1,2,3\), then compute exact breadth-first distances from a representative. The three maximum distances are \(3,6,10\), respectively. These are complete finite exhaustive computations, not extrapolations to larger \(k\).

## Verification
Run `python verification_direct.py` and compile/run `verification_independent.cpp` using a C++17 compiler. The Python program independently tests paired domination on every size-optimal candidate among subsets of \(E(K_4)\) and \(E(K_7)\); it compares the full optimizer sets with a local-move construction. It also performs exhaustive breadth-first searches on the complete slide graphs for \(n=4,7,10\). The C++17 program independently enumerates the triple partitions with chosen centers, represents configurations as 64-bit subsets of edges of \(K_n\), and constructs adjacency by directly testing every allowed one-edge slide. It checks connectivity, degree, triangles, and breadth-first distance distributions. The two representations agree in all shared values.

The full distance histograms from a root, including distance zero, are:

* \(n=4\): \((1,4,6,1)\).
* \(n=7\): \((1,8,32,86,176,261,66)\).
* \(n=10\): \((1,12,78,383,1576,5331,13770,24664,23409,6144,232)\).

Their entries sum to \(N_1,N_2,N_3\), respectively. `direct_output.txt` and `independent_output.txt` record the executed source outputs. The proof covers every \(k\ge1\), whereas exhaustive distance checks end at \(k=3\).

## Relationship to prior work
Haynes and Slater introduced paired domination and basic inequalities. Studer, Haynes, and Lawson introduced induced-paired domination and proved broad bounds and results for cycles and trees. Suzuki, Mouawad, and Nishimura studied dominating-set reconfiguration under addition/removal steps and size allowances; that move model does not enforce an optimum paired dominating set at every state. The present theorem focuses on the triangular graph \(T_n=L(K_n)\) at its sharp three-labels-per-pair saturation and uses fixed-size token sliding, whose state space is smaller and subject to different restrictions. Standard connected-graph token-swapping transpositions explain reachability only after the square-bouquet quotient identification is established.

Published exact paired-domination profiles for complete multipartite and chain graphs do not subsume this family for \(n\ge7\): triangular graphs then contain triangles and are not complete multipartite (nonadjacency is not transitive). The \(n=4\) triangular graph is complete multipartite, so its optimizer count by itself is not asserted to be novel. No priority claim is made for paired-domination definitions or general token-swapping connectivity.

## Limitations
The theorem determines the minimum-solution classification and slide graph for \(n\equiv1\pmod3\), not the other congruence classes. No formula for diameter at \(n\ge13\), Hamiltonicity, or mixing time is proved. Exhaustive tests through \(n=10\) do not imply further distance formulas. Publication priority remains uncertain: an unindexed classification of paired domination in triangular graphs or a colored-token-swapping quotient might imply portions of the result. The foundational Haynes–Slater full text was not accessible in this comparison, and not every page of the scanned induced-paired paper was inspected.

## References
1. T. W. Haynes and P. J. Slater, *Paired-domination in graphs*, Networks **32** (1998), 199–206. DOI: `10.1002/(SICI)1097-0037(199810)32:3<199::AID-NET4>3.0.CO;2-F`. First published online 1998-12-07.
2. D. S. Studer, T. W. Haynes and L. M. Lawson, *Induced-Paired Domination in Graphs*, Ars Combinatoria **57** (2000), 111–128. `https://combinatorialpress.com/article/ars/Volume%20057/volume-57-paper-11.pdf`.
3. A. Suzuki, A. E. Mouawad and N. Nishimura, *Reconfiguration of Dominating Sets*, arXiv:1401.5714 (initial version 2014-01-22). `https://arxiv.org/pdf/1401.5714`.
4. K. Yamanaka et al., *Swapping colored tokens on graphs*, Theoretical Computer Science **729** (2018), 1–10. DOI: `10.1016/j.tcs.2018.03.016`.
