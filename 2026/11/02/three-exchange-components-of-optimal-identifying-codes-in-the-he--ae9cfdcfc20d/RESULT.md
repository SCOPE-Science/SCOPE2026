# Three exchange components of optimal identifying codes in the Heawood graph

## Finding
Let \(H\) be the fourteen-vertex point–line incidence graph of the Fano plane. A radius-one identifying code is a set \(S\subseteq V(H)\) for which all fourteen traces \(S\cap N_H[v]\) are nonempty and pairwise distinct. The minimum identifying-code size is \(7\), and there are exactly \(268\) minimum codes.

Let \(\mathcal R_1\) have these codes as vertices, with two codes adjacent when one selected vertex is exchanged for one unselected vertex. Write \(L(H)\) for the line graph of \(H\), and \(\vee\) for graph join. Then
\[
\mathcal R_1\cong (K_1\vee L(H))\sqcup\mathcal C\sqcup(K_1\vee L(H)),
\]
where \(\mathcal C\) is a connected, self-centered graph with \(224\) vertices, \(532\) edges, and radius and diameter both \(6\). Each outer component has \(22\) vertices, \(63\) edges, radius \(1\), and diameter \(2\). Globally \(\mathcal R_1\) has \(658\) edges and degree enumerator
\[
D_{\mathcal R_1}(t)=2t^{21}+56t^4+210t^5.
\]

Allowing a move that exchanges **at most two** selected vertices for the same number of unselected vertices, while requiring the new configuration to remain an optimal identifying code, yields a connected graph \(\mathcal R_{\le2}\) with \(4438\) edges, radius \(3\), and diameter exactly \(5\). Thus two simultaneous replacements are necessary and sufficient for global reachability. The exactly-two-only exchange graph, unlike \(\mathcal R_{\le2}\), has a component of order \(266\) and two isolated vertices.

## Assumptions and scope
The Fano plane is labelled by points \(P_i\) and lines \(L_i\) for \(i\in\{0,\ldots,6\}\), with
\[
L_i=\{P_i,P_{i+1},P_{i+3}\},
\]
indices modulo \(7\). The Heawood graph has the fourteen objects as vertices, joining a point to a line precisely when they are incident. Here \(N_H[v]\) is the **closed** neighborhood, including \(v\). All sets are unordered sets of named vertices. An exchange of size \(r\) replaces exactly \(r\) distinct selected vertices by \(r\) previously unselected vertices, with no constraint that the paired original and replacement vertices be adjacent in \(H\). A move of size at most two has \(r\in\{1,2\}\); validity is required at the two endpoints, not at an intermediate one-exchange state.

## Proof
**1. Complete finite incidence test.** For a selected set \(S\), define its fourteen signatures \(I_S(v)=S\cap N_H[v]\). The criterion that the signatures be nonempty and pairwise different is equivalent to the defining identifying-code condition. The displayed seven cyclic triples each have size three, each point lies on three triples, and any two points lie on exactly one triple; thus they give the full Fano incidence graph. The standalone checker `verify_incidence.py` enumerates every subset of size \(0\) through \(7\) (there are \(6476\) subsets of size at most \(6\) and \(3432\) seven-subsets), computes these signatures exactly as fourteen-bit integers, and returns counts \(0,0,0,0,0,0,0,268\) by size. In particular, the absence of smaller codes and the existence of seven-codes are both exhaustive, rather than consequences of a general bound.

**2. Geometric census.** If \(p\) of the seven selected vertices represent points, the exact seven-code counts for \(p=0,1,2,3,4,5,6,7\) are respectively
\[
(1,21,0,112,112,0,21,1).
\]
For \(p=1\), precisely the \(21\) codes consisting of a selected point \(P_i\) and all lines except one of the three lines incident with \(P_i\) are valid. The \(p=6\) family is point–line dual. For \(p=3\), each of the seven collinear three-point sets extends to exactly four minimum codes, and each of the twenty-eight noncollinear three-point sets extends to exactly three; the \(p=4\) counts are dual. These are finite incidence identities verified separately by direct trace tests, not assumptions about any omitted configurations.

**3. Two explicit small components.** A one-exchange changes the number \(p\) of selected points by at most one. Since no optimal code has \(p=2\) or \(p=5\), the three classes \(p\in\{0,1\}\), \(p\in\{3,4\}\), and \(p\in\{6,7\}\) cannot communicate. In the first class, the all-line code is adjacent to every one-point code. Index the latter by a flag \((P_i,L_j)\) with \(P_i\in L_j\), where \(L_j\) is the single omitted line. Two such codes are adjacent precisely when their flags share their point or their line. This is exactly adjacency in the line graph \(L(H)\) on the \(21\) flags. Adding the all-line vertex makes the join \(K_1\vee L(H)\). Point–line duality gives the other component. Since \(H\) is cubic, \(L(H)\) is four-regular with \(42\) edges, so each join has \(63\) edges.

**4. The remaining component.** The remaining \(224\) codes have \(p\in\{3,4\}\). The complete one-exchange adjacency test is a comparison of selected sets with intersection size \(6\), a necessary-and-sufficient condition. A breadth-first search using every permitted neighbor confirms that these \(224\) form one component with \(532\) edges, \(56\) degree-four vertices, \(168\) degree-five vertices, and eccentricity exactly \(6\) for every root. These conclusions are fully finite: `verify_incidence.py` checks the one-exchange graph and all-source BFS, and the independent incidence construction in `verify_geometry.py` reproduces the component count and degree census without reusing the bitmask representation. The same independent code constructs the full \(336\)-element point–line automorphism action and verifies code orbit sizes \(2,42,56,168\).

**5. Sharp two-exchange threshold.** Comparing any two seven-codes shows that one move of size at most two is legal precisely when their symmetric difference has cardinality \(2\) or \(4\). Exhaustive graph construction gives \(4438\) edges, one component, radius \(3\), and diameter \(5\). The distance lower bound is also transparent: selected-point counts can only be \(0,1,3,4,6,7\), and one such move changes the count by at most two. Therefore any path from the all-point code to the all-line code must pass through all six count levels, requiring at least five moves. Equality is attained, for example, by the six seven-vertex sets (with vertices numbered \(0\) to \(6\) for points and \(7\) to \(13\) for lines)
\[
\begin{aligned}
&\{0,1,2,3,4,5,6\},\\
&\{0,1,2,3,4,5,10\},\\
&\{0,1,2,3,7,10,11\},\\
&\{0,1,2,7,8,10,12\},\\
&\{0,7,8,9,10,11,12\},\\
&\{7,8,9,10,11,12,13\}.
\end{aligned}
\]
Each is a valid minimum code, and consecutive sets differ in at most two selected vertices. The all-source finite distance check supplies the matching global upper bound. Restricting instead to exactly two simultaneous exchanges strands the all-point and all-line codes, whose intersections with any other minimum code have size \(6\) or at most \(4\), but never \(5\).

## Verification
Run the standalone, standard-library-only scripts from the same directory: `python3 verify_incidence.py` and `python3 verify_geometry.py`. They must respectively print `HEAWOOD_IDENTIFY_BITMASK_EXHAUSTIVE_PASS` and `HEAWOOD_IDENTIFY_VECTOR_GEOMETRY_PASS`. The first builds a cyclic-difference Fano plane and checks the entire relevant subset space, every one- and two-exchange edge, every connected component, and all-source distances. The second constructs the incidence plane from nonzero binary three-vectors and orthogonality, uses set-valued signatures and explicit exchanges, checks all candidate subsets up to size seven, and independently computes Fano collineation and duality orbits. Every claimed integer is checked by a finite exhaustive operation; neither implementation extrapolates to other graphs.

## Relationship to prior work
The definition and motivation of identifying codes originate in the 1998 work of Karpovsky, Chakrabarty, and Levitin. Gravier, Parreau, Rottey, Storme, and Vandomme study identifying codes in vertex-transitive and strongly regular graphs, including the general integer and fractional optimization formulations; their 2014 preprint and 2015 article do not report this Heawood optimal-code exchange decomposition. Honkala, Hudry, and Lobstein's 2015 enumeration article studies extremal multiplicities of optimal codes and explicitly points to their 2016 article for the ensemble and distances between optimal codes. The latter establishes a universal connection between optimal-code exchange graphs and induced subgraphs of Johnson graphs; the abstract does not assert an exact Heawood census, component structure, or two-replacement threshold. Its complete text could not be obtained, so an unlocated Heawood example remains a priority risk. The 2024 survey of Hudry, Junnila, and Lobstein covers optimal code counts in other settings but contains no Heawood-specific reconfiguration result. Standard Heawood/Fano references establish the incidence structure and automorphisms, not the configuration-exchange graph. All general definitions, incidences, and symmetry facts are background; the particular 268-code census, decomposition, exact mobility threshold, and metric are the candidate contribution.

## Limitations
This is an exact finite theorem for the standard fourteen-vertex Heawood graph, with one fixed radius and one fixed exchange rule. It makes no claim for larger projective planes, arbitrary symmetric cubic graphs, or token sliding. Bibliographic searches cannot establish universal priority, especially because the closely related 2016 ensemble study could not be examined beyond its indexed abstract. The finite proof relies on reproducible exhaustive code for the large component's connectedness and diameter, not on a shorter symbolic formula for those quantities.

## References
1. M. G. Karpovsky, K. Chakrabarty, and L. B. Levitin, *On a new class of codes for identifying vertices in graphs*, IEEE Transactions on Information Theory 44 (1998), 599–611.
2. S. Gravier, A. Parreau, S. Rottey, L. Storme, and É. Vandomme, *Identifying codes in vertex-transitive graphs and strongly regular graphs*, Electronic Journal of Combinatorics 22(4) (2015), P4.6; first arXiv submission 2014-11-19, https://arxiv.org/abs/1411.5275.
3. I. Honkala, O. Hudry, and A. Lobstein, *On the number of optimal identifying codes in a twin-free graph*, Discrete Applied Mathematics 180 (2015), 111–119, https://doi.org/10.1016/j.dam.2014.08.020.
4. I. Honkala, O. Hudry, and A. Lobstein, *On the ensemble of optimal identifying codes in a twin-free graph*, Cryptography and Communications 8 (2016), 139–153, first online 2015-06-30, https://doi.org/10.1007/s12095-015-0148-3.
5. O. Hudry, V. Junnila, and A. Lobstein, *On Iiro Honkala's contributions to identifying codes*, Fundamenta Informaticae 191 (2024), https://arxiv.org/abs/2402.08264.
6. DistanceRegular.org, *Heawood graph / incidence graphs*, https://www.math.mun.ca/distanceregular/indexes/incidencegraphs.html.
