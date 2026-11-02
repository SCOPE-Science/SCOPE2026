# The Pappus graph has a six-block Rips sphere filtration with a surviving quotient class

## Finding
Let \(P\) be the eighteen-vertex Pappus graph, supplied explicitly in the proof, with its vertex shortest-path metric. Define the **inclusive** Vietoris–Rips complex \(R_r=\operatorname{VR}_{\le r}(V(P))\): a nonempty vertex subset is a simplex precisely when each pair is at distance at most \(r\). For every real \(r\ge0\),
\[
R_r\simeq
\begin{cases}
\bigvee^{17}S^0,&0\le r<1,\\
\bigvee^{10}S^1,&1\le r<2,\\
\bigvee^{26}S^2,&2\le r<3,\\
\bigvee^{64}S^5,&3\le r<4,\\
\mathrm{pt},&r\ge4.
\end{cases}
\]
These are **integral** homotopy equivalences: all reduced integral homology is torsion-free. Consequently, every positive-degree persistent homology interval, over any field, is one unit long; it appears only over the half-open intervals \([1,2)\), \([2,3)\), or \([3,4)\), with multiplicities \(10,26,64\) in degrees \(1,2,5\), respectively. There are also seventeen reduced degree-zero intervals \([0,1)\).

Moreover, the full automorphism group \(\Gamma=\operatorname{Aut}(P)\) has order \(216\). At scale three, the six distance-four vertex triples \(B_1,\ldots,B_6\) give a canonical \(\Gamma\)-module isomorphism
\[
\widetilde H_5(R_3;\mathbb Z)
\cong
\widetilde H_0(B_1;\mathbb Z)\otimes\cdots\otimes\widetilde H_0(B_6;\mathbb Z),
\]
where every factor is the rank-two augmentation lattice, and a permutation of the six factors carries the Koszul sign \(\operatorname{sgn}(\pi)\). Thus this is an explicit *integral* homology action, not merely a dimension count. For a symmetry \(g\), let \(\pi_g\) permute the six triples. For each cycle \(c\) of \(\pi_g\), let \(p_c\) be the permutation of three vertices obtained by transporting once around that cycle. Its entire fifth-homology character is
\[
\chi_5(g)=\operatorname{sgn}(\pi_g)
\prod_{c\in\operatorname{Cyc}(\pi_g)}
\bigl(\#\operatorname{Fix}(p_c)-1\bigr).
\]
In the full group, character values and their numbers of occurrences are \((-8,18),(-2,36),(0,54),(1,56),(4,42),(16,9),(64,1)\). The exact signed-simplex Lefschetz formula below also determines the complete second-homology character at scale two; its value/multiplicity pairs are \((-10,9),(-1,92),(0,54),(2,48),(5,12),(26,1)\). Consequently,
\[
\dim_{\mathbb Q}H_5(R_3/\Gamma;\mathbb Q)=1,
\qquad
\widetilde H_*(R_2/\Gamma;\mathbb Q)=0,
\]
where in the latter equality every reduced rational homology group vanishes. In particular, a rational quotient class emerges in degree five only at scale three.

## Assumptions and scope
Use a simple, undirected graph whose vertices are the residues \(0,1,\ldots,17\). Include all eighteen cycle edges \(\{i,i+1\}\) (indices modulo \(18\)); in addition include \(\{i,i+a_i\}\) for the period-six offset sequence \((a_i)_{i=0}^{17}=(5,7,-7,7,-7,-5)^3\), with repetitions counted only once. This is the standard LCF presentation of the Pappus graph. It has \(18\) vertices, \(27\) edges, girth \(6\), and diameter \(4\). No claim is made for other graphs, edge lengths, ambient Euclidean metrics, or the strict-distance convention.

The automorphisms act on all Rips complexes by relabeling vertices. The quotient assertions concern **ordinary topological quotients** and **rational homology**; they are not statements about orbifold or Borel equivariant homology. The full finite symmetry group may have nontrivial stabilizers.

## Proof
**1. Thresholds zero and one.** Distances between distinct graph vertices are positive integers, so complexes are constant on the indicated half-open intervals. At scale zero there are eighteen points. The Pappus graph has no triangles, so at scale one the Rips complex is the connected graph itself, whose first Betti number is \(27-18+1=10\).

**2. An exhaustive integral discrete-Morse collapse at scale two.** Generate every nonempty clique of the distance-two graph on the eighteen labeled vertices using the LCF presentation. The face vector by dimension is exactly \((18,81,108,18)\), so there are \(225\) nonempty faces. Perform the following deterministic matching: visit vertices in order \(0,1,\ldots,17\); for each vertex \(v\), match every as-yet-unmatched face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\), provided both faces remain unmatched and the larger face is a simplex. The accompanying self-contained checker specifies the unambiguous enumeration order (first by cardinality, then by bit-mask integer). It enumerates exactly \(99\) pairs: \(17\) vertex–edge, \(64\) edge–triangle, and \(18\) triangle–tetrahedron pairs. Exactly one vertex and \(26\) triangles remain critical.

The crucial acyclicity assertion is **checked on the entire Hasse graph**, not inferred merely from the matching counts. The checker directs every face–coface cover downwards except for matched covers, which it reverses, and topologically sorts all \(225\) vertices and \(558\) directed edges. Every vertex is removed, establishing the absence of a directed cycle. Forman's discrete-Morse theorem therefore gives a CW model with one zero-cell and exactly \(26\) two-cells, with no one-cells or higher cells. Every attaching map of a two-cell to the point is null, proving \(R_2\simeq\bigvee^{26}S^2\) *integrally*.

**3. Exact join decomposition at scale three.** Breadth-first distances from the displayed LCF graph show that the only pairs at distance four form six disjoint triangles in the missing-edge graph, on the vertex triples
\[
\begin{split}
&B_1=(0,10,14),\quad B_2=(1,11,15),\quad B_3=(2,6,16),\\
&B_4=(3,7,17),\quad B_5=(4,8,12),\quad B_6=(5,9,13).
\end{split}
\]
Thus the distance-three graph joins every pair in different blocks, but no pair within a block. Its clique complex is **exactly** the simplicial join of six discrete three-point sets \(B_1*\cdots*B_6\). Each factor is homotopy equivalent to \(S^0\vee S^0\); the reduced-homology join formula, or repeated suspension-smash decomposition, gives a wedge of \(2^6=64\) five-spheres. This identification holds over \(\mathbb Z\) and is natural under all graph automorphisms.

**4. Equivariance and quotient.** The join's cellular orientation rule contributes the sign of the block permutation, since exchanging two zero-dimensional factors in a join changes its top orientation by \(-1\). Each three-point factor has the reduced permutation lattice \(\ker(\mathbb Z[B_i]\to\mathbb Z)\), and tracing cycles of permuted tensor factors gives the displayed \(\chi_5\) formula. All \(216\) distance-preserving permutations are enumerated from the eighteen-by-eighteen shortest-path matrix (each vertex image is constrained by distance to previously mapped vertices). The formula is independently compared to the signed simplicial Lefschetz number for every one of these permutations and agrees in all cases.

At scale two, only ordinary \(H_0\) and \(H_2\) are nonzero. For each \(g\in\Gamma\), let \(F_k\) denote the actual set of \(k\)-simplices and \(\epsilon(g,\sigma)\) the sign of the induced vertex-order permutation if \(g\sigma=\sigma\). The identity
\[
\chi_2(g)=\sum_{k=0}^3(-1)^k\sum_{\substack{\sigma\in F_k\\g\sigma=\sigma}}\epsilon(g,\sigma)-1
\]
is the exact equivariant Euler–Poincaré formula; the finite character table above follows by enumeration. Likewise \(\chi_1(g)=1-L_1(g)\), with \(L_1\) the signed Lefschetz chain sum, at scale one. The checker independently verifies
\[
\sum_{g\in\Gamma}\chi_1(g)=0,\quad
\sum_{g\in\Gamma}\chi_2(g)=0,\quad
\sum_{g\in\Gamma}\chi_5(g)=216.
\]
For any finite group action, ordinary rational homology of the quotient equals invariant rational homology (by rational averaging/transfer on a suitable equivariant subdivision). Dividing the character sums by \(216\) proves all claimed quotient Betti numbers.

**5. Terminal scale.** The diameter is four, so \(R_r\) is a full simplex for \(r\ge4\). The homotopy filtration and persistence multiplicities now follow because no two adjacent nontrivial stages have reduced homology in the same positive degree.

## Verification
The complete dependency-free Python 3 checker is `check_pappus_rips.py`, embedded alongside this document. Execute it as `python3 check_pappus_rips.py`. It reconstructs the graph, all faces through scale three, the 99 Morse pairs, and their full directed Hasse acyclicity test; computes all graph automorphisms; checks all signed chain Lefschetz sums; and separately verifies the six-block tensor-character formula for every automorphism. It outputs `PAPPUS_RIPS_HOMOTOPY_216_CHARACTERS_EXACT_OK` only after all assertions pass. The exhaustive finite argument is the proof certificate for this specific graph; this is not a claim about infinite graph families.

## Relationship to prior work
Adamaszek and Adams (arXiv:2103.01040, first public March 1, 2021) compute graph-metric Rips complexes of hypercube graphs and demonstrate that higher-dimensional spheres appear at discrete distance scales. Feng (arXiv:2305.07084, first public May 11, 2023) determines their more complicated scale-three homotopy. Adamaszek (arXiv:1104.0433) studies clique complexes of graph powers and gives stability and special-family results; its theorem for graphs with no induced six-cycles does not apply to this girth-six Pappus graph. These works do not provide a Pappus-specific homotopy filtration or the six-block automorphism module.

There are published computations for other structures on this graph, notably its intrinsic graph Čech nerve and matching complexes. Those are not the pairwise-distance Vietoris–Rips complexes used here. The indexed Pappus scale-three Čech claim has \(44\) second-dimensional spheres, whereas the present scale-three Rips complex is a join with \(64\) fifth-dimensional spheres; neither assertion is a restatement of the other. No stronger covering result was identified in the inspected primary literature and mathematical index. Failure to locate an equivalent result is not proof of global novelty.

## Limitations
The homotopy identifications are nonequivariant; the group-action statement is an integral representation in degree five and a complete **rational character** in degree two, not an equivariant homotopy decomposition or a classification of integral second-homology lattices. Rational quotient homology is given, but integral quotient torsion is not determined. The construction concerns the canonical eighteen-vertex graph and no general incidence-graph family. Similar conclusions might exist in unindexed sources; the accessible summary of a related graph Čech result could be compared by its stated object and homology, but its complete source material could not be inspected.

## References
1. M. Adamaszek and H. Adams, *On Vietoris–Rips complexes of hypercube graphs*, arXiv:2103.01040 (first public March 1, 2021), https://arxiv.org/abs/2103.01040.
2. Z. Feng, *Homotopy types of Vietoris–Rips complexes of hypercube graphs*, arXiv:2305.07084 (first public May 11, 2023), https://arxiv.org/abs/2305.07084.
3. M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433, https://arxiv.org/html/1104.0433v3.
4. A. E. Brouwer, *Pappus graph* (graph description, intersection array and symmetry), https://aeb.win.tue.nl/graphs/Pappus.html.
5. E. W. Weisstein, *Pappus Graph*, MathWorld, https://mathworld.wolfram.com/PappusGraph.html.
