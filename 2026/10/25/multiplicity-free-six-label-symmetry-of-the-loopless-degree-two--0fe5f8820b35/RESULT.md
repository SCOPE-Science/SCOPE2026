# Multiplicity-free six-label symmetry of the loopless degree-two graph complex

## Finding
Let \(\mathcal B_{6,2}\) have fifteen abstract vertices \(\{i,j\}\), indexed by unordered pairs from \(\{0,1,2,3,4,5\}\). A subset is a face exactly when its corresponding simple graph has degree at most two at each of its six graph vertices. The natural \(\mathfrak S_6\)-action permutes graph labels. The principal result is the multiplicity-free rational representation
\[
\widetilde H_4(\mathcal B_{6,2};\mathbb Q)\cong S^{(6)}\oplus S^{(4,2)}\oplus S^{(3,2,1)}\oplus S^{(2,2,2)}\oplus S^{(2,1,1,1,1)}.
\]
All five summands occur with multiplicity one; their dimensions are \(1,9,16,5,5\), respectively. Thus there is precisely one invariant line. The full character, indexed by the cycle partitions
\((6),(5,1),(4,2),(4,1,1),(3,3),(3,2,1),(3,1,1,1),(2,2,2),(2,2,1,1),(2,1,1,1,1),(1,1,1,1,1,1)\), is
\[
(2,1,0,0,0,0,0,8,4,0,36).
\]
In addition an integral discrete-Morse calculation establishes \(\mathcal B_{6,2}\simeq\bigvee^{36}S^4\). The integral fourth Betti number \(36\) and vanishing of other reduced integral homology were previously recorded by Jonsson [1, Table 12.2]; the new assertion is the complete six-label representation, not that numerical rank.

## Assumptions and scope
Graphs are finite, simple, undirected, and **loopless**, on six distinct labeled vertices. In particular they must not be identified with degree-bounded complexes admitting loops; inserting or deleting loop vertices does not preserve homology automatically. Chains are oriented by ascending lexicographic order on the fifteen graph edges. The action is the induced oriented-simplicial action. All integral statements use \(\mathbb Z\); irreducible decomposition is over \(\mathbb Q\), with ordinary rational Specht modules of \(\mathfrak S_6\). There is no claim for other graph orders or degree bounds.

## Proof
**Finite face poset.** Index the fifteen edges lexicographically, and encode each subset by a fifteen-bit integer. Checking six vertex-incidence masks, each of popcount at most two, gives exactly 1,858 faces including the empty face. The nonempty face vector in dimensions zero through five is \((15,105,395,735,537,70)\). The complex is nonpure: 117 maximal faces have dimension four and 70 have dimension five. A second independent edge-list degree predicate agrees for all \(2^{15}\) subsets.

**Integral homotopy calculation.** Match faces by ascending edge index: for each index, in ascending bitmask order pair every currently available face not containing that index with the face obtained by adjoining it, whenever both remain. This includes the empty face paired with the first singleton. Omit this latter pair in the ordinary face-poset gradient and retain the singleton as a critical vertex. The remaining matching has 896 pairs and exactly fourteen critical dimension-three cells and fifty critical dimension-four cells. Orient every ordinary Hasse incidence downward, except reverse matched incidences. Topological sorting of the resulting graph on all 1,857 nonempty faces visits every face with no directed cycle; it examines all 7,440 incidences. Hence the matching is acyclic.

Process the 897 augmented pairs in their prescribed order by exact integral algebraic Morse cancellation. At each cancellation the pivot coefficient is \(\pm1\). The remaining augmented boundary has fourteen rows (critical degree three) and fifty columns (critical degree four), with 122 nonzero entries and maximum entry magnitude three. With rows sorted by bitmask, columns sorted likewise, its fourteen-by-fourteen minor in zero-based column positions \((1,2,4,7,9,10,11,12,14,18,20,21,24,37)\) has exact determinant \(-1\). Therefore the boundary \(\mathbb Z^{50}\to\mathbb Z^{14}\) is split-surjective. Forman's theorem gives a CW complex with a single zero-cell, fourteen three-cells and fifty four-cells. Its three-skeleton is a wedge of fourteen three-spheres, with \(\pi_3\cong\mathbb Z^{14}\); attaching maps of the four-cells are completely determined by that same integer boundary matrix. Integral changes of cell bases reduce the matrix to a unit block and a zero block, cancel fourteen three–four pairs, and leave thirty-six four-spheres. Thus \(\mathcal B_{6,2}\simeq\bigvee^{36}S^4\).

**Representation character.** Fix \(g\in\mathfrak S_6\). On oriented chains, a set of edges contributes to the trace only if it is \(g\)-stable; its trace sign is the parity of the permutation of those edges. The reduced Hopf trace formula, using homology only in degree four, yields \(\chi_4(g)=\sum_{F\in\mathcal B_{6,2}}(-1)^{|F|-1}\operatorname{sgn}(g|_F)\), including the empty face with sign \(-1\). There is an independent evaluation: partition the fifteen edges into \(g\)-orbits; sum over all subcollections whose unions have maximum degree at most two, with summand \(-(-1)^k\) for \(k\) selected orbits. The two algorithms give the character values stated above for one representative of each of the eleven conjugacy classes. Because characters are constant on conjugacy classes, this proves the formula for all 720 permutations.

For each partition \(\lambda\vdash6\), evaluate the irreducible character \(\chi^\lambda\) via the Jacobi–Trudi alternating sum of permutation characters induced from Young subgroups, computed by distributing cycles among rows of prescribed lengths. Using the weighted character inner product \(\langle\chi_4,\chi^\lambda\rangle=(1/720)\sum_{\mu\vdash6}|C_\mu|\chi_4(\mu)\chi^\lambda(\mu)\), every multiplicity is zero except the five listed, each one. The dimensions sum to 36. Semisimplicity of \(\mathbb Q[\mathfrak S_6]\) completes the decomposition.

## Verification
The bundled Python 3 standard-library script `verify_maxdegree2_k6.py` enumerates all \(2^{15}=32,768\) candidate edge sets with two independent degree tests, reproduces the matching and full acyclicity topological sort, performs integer Morse cancellation and Bareiss exact determinant evaluation, and independently computes all six simplicial boundary ranks over \(\mathbb F_2\) and \(\mathbb F_3\) as \((1,14,91,304,431,70)\). It constructs the complete rational character in two independent ways and checks the Jacobi–Trudi irreducible multiplicities. Execute `python3 verify_maxdegree2_k6.py` in the same directory. The expected final output line is `VERIFY_OK`; full recorded output accompanies this result.

## Relationship to prior work
Jonsson [1], section 12.1.1 and Table 12.2, already provides the integral homology at six vertices: rank 36 in degree four and zero elsewhere. This result therefore **does not** present that Betti table as new. The independent contribution is the complete rational permutation-of-labels homology character, its multiplicity-free five-Specht decomposition, and the identified invariant line. Wachs [2, section 7], building on Reiner–Roberts, Karaguezian–Reiner–Wachs and Dong, studies graph complexes that **allow loops**, so its general Specht decomposition does not directly imply a character for this loopless complex. Jonsson [3] likewise works with a different loop-admitting family in its torsion results. The disjoint subject matter of nearby homology representations of Kneser and domination complexes does not imply this decomposition. No claim of global uniqueness is made.

## Limitations
The specific \(36\) Betti number and integral homology groups were known. Jonsson's directly relevant section was located through its indexed table and chapter listing but its complete full text could not be inspected from authorized sources in this calculation. An unindexed equivariant calculation, or a specialized representation theorem in that section, could therefore cover the representation. The finite verifier establishes only the stated six-vertex result and does not prove a general pattern. The self-review is not independent validation.

## References
[1] Jakob Jonsson, *Simplicial Complexes of Graphs*, Lecture Notes in Mathematics 1928, Springer, 2008, section 12.1.1 and Table 12.2; original KTH thesis, 2005. DOI: https://doi.org/10.1007/978-3-540-75859-4.

[2] Michelle L. Wachs, *Topology of Matching, Chessboard, and General Bounded Degree Graph Complexes*, Algebra Universalis 49 (2003), 345–385; particularly section 7. Author-hosted full manuscript: https://www.math.miami.edu/~wachs/papers/tmc.pdf.

[3] Jakob Jonsson, *3-torsion in the homology of complexes of graphs of bounded degree*, Canadian Journal of Mathematics 65 (2013), 843–862, DOI: https://doi.org/10.4153/CJM-2013-008-4.

[4] Dikran B. Karaguezian, Victor Reiner and Michelle L. Wachs, *Matching complexes, bounded degree graph complexes and weight spaces of GL_n-complexes*, Journal of Algebra 239 (2001), 77–92.
