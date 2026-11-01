# Integral two-torsion in three-cut complexes of folded cubes

## Finding

For each integer \(d\geq5\), let \(F_d\) be the folded \(d\)-cube: identify opposite vertices of the graph of the \(d\)-dimensional cube, retaining one edge for each coordinate step. Set
\[
N_d=2^{d-1},\qquad
B_d=2^{d-4}(d^2-5d+8)-1,\qquad
L_d=2^{d-2}\left(2^{d-1}-1-d-\binom{d}{2}\right).
\]
Let \(\Delta_3(F_d)\) be the **ordinary** three-cut complex, whose facets are complements of disconnected induced three-vertex subsets. Then its complete reduced integral homology is
\[
\widetilde H_i(\Delta_3(F_d);\mathbb Z)\cong
\begin{cases}
\mathbb Z^{B_d}\oplus\mathbb Z/2,&i=N_d-5,\\
\mathbb Z^{L_d},&i=N_d-4,\\
0,&\text{otherwise}.
\end{cases}
\]
In particular, every member of this natural infinite graph family has genuine integral two-torsion. Each three-cut complex is pure of dimension \(N_d-4\) but is neither shellable nor Cohen–Macaulay over any field (already its lower-dimensional rational homology is nonzero). At \(d=5\), the graph is the Clebsch graph and
\[
\widetilde H_{11}(\Delta_3(F_5);\mathbb Z)\cong\mathbb Z^{15}\oplus\mathbb Z/2,
\qquad\widetilde H_i=0\quad(i\ne11).
\]
At \(d=6\), the two nonzero groups are \(\mathbb Z^{55}\oplus\mathbb Z/2\) in degree \(27\) and \(\mathbb Z^{160}\) in degree \(28\).

## Assumptions and scope

Write the vertices of \(F_d\) as the vector-space quotient \(\mathbb F_2^d/\langle\mathbf1\rangle\), where \(\mathbf1\) is the all-ones vector, with edges corresponding to addition by one standard basis vector. This gives exactly \(N_d\) vertices, degree \(d\), and no loops or parallel edges for \(d\ge5\). A face of \(\Delta_3(F_d)\) is an arbitrary subset contained in the complement of some disconnected triple. The Alexander dual is taken relative to the full vertex set. All homology and cohomology groups are over \(\mathbb Z\), except where another coefficient ring is explicit. The formulas make no assertion for \(d<5\), for total cut complexes, or for larger cut thresholds.

## Proof

**1. Short walks in the folded cube.** A closed walk of length at most four has coordinate-step labels whose sum is either zero or \(\mathbf1\) in \(\mathbb F_2^d\). For \(d\ge5\), a sum of at most four basis vectors cannot be \(\mathbf1\). Consequently there are no triangles, every simple four-cycle uses two distinct coordinate labels twice each, and every length-two path belongs to exactly one four-cycle (the commuting square of those labels). Two distinct vertices have two common neighbors exactly when their graph distance is two, and none otherwise. The distance-one and distance-two sphere sizes are \(d\) and \(\binom{d}{2}\). The number of squares is \(N_d\binom{d}{2}/4\).

**2. The small Alexander-dual model.** Put \(K_d=(\Delta_3(F_d))^{\vee}\). By complementing the definition of a cut-complex facet, a subset belongs to \(K_d\) precisely when **every three of its vertices induce a connected graph**. Every vertex and pair therefore belongs to \(K_d\). Each three-face is a two-edge path; each four-face induces a four-cycle. Indeed, on four vertices, all four triples must have exactly two edges, so double counting forces four graph edges, hence the induced graph is a four-cycle. No five-face exists: ten connected triples would have twenty triple–edge incidences, whereas each induced edge is counted three times, an impossibility. Hence \(K_d\) consists exactly of the complete one-skeleton, the two-edge paths as triangles, and one tetrahedron for each four-cycle.

**3. Explicit elementary collapses.** For a four-cycle \(a-b-c-e-a\), remove its tetrahedron \(abce\) paired with triangle \(abc\), then remove triangle \(ace\) paired with its edge \(ac\). The first triangle belongs to exactly one tetrahedron, because each two-edge path lies in a unique square. After the first removal, the diagonal \(ac\) belongs to exactly one remaining triangle, because its endpoints have exactly two common neighbors. Thus both are genuine free-face collapses. These operations can be performed for every square independently; none of the indicated triangles or diagonals belongs to a second square. The residual triangles \(abe\) and \(bce\) triangulate the square disk, and all graph edges remain. The only other edges are the \(L_d\) pairs at graph distance at least three. Adjoining each such edge between points of a connected complex adds one circle up to homotopy, so
\[
K_d\simeq S_d\vee\bigvee^{L_d}S^1,
\]
where \(S_d\) is the two-dimensional CW square-filling complex of \(F_d\). Counting distant unordered pairs gives
\[
L_d=\frac{N_d}{2}\left(N_d-1-d-\binom{d}{2}\right).
\]

**4. Antipodal cubical covering and integral homology.** Let \(Q_d^{(2)}\) be the two-skeleton of the standard *cubical* cell decomposition of the \(d\)-cube. The coordinatewise antipodal map sends every vertex \(x\) to \(\mathbf1-x\). It acts freely on the two-skeleton when \(d\ge5\): a point fixed by that map would have all coordinates equal to one half, which is not in the two-skeleton. The quotient square complex is exactly \(S_d\): its one-skeleton is \(F_d\), and every square in \(F_d\) lifts to a pair of opposite cubical square faces by Step 1. The full cubical \(d\)-ball is contractible and is obtained from its two-skeleton by attaching cells of dimensions at least three, which cannot change its fundamental group. Hence \(Q_d^{(2)}\) is simply connected and the quotient is a two-sheeted covering with
\[
\pi_1(S_d)\cong\mathbb Z/2,\qquad H_1(S_d;\mathbb Z)\cong\mathbb Z/2.
\]
Its cell counts are \(N_d\) vertices, \(N_dd/2\) edges, and \(N_d\binom{d}{2}/4\) squares. Therefore
\[
\chi(S_d)=N_d-\frac{N_dd}{2}+\frac{N_d}{4}\binom{d}{2}
=2^{d-4}(d^2-5d+8).
\]
Since \(S_d\) is connected, two-dimensional and has finite first homology, \(H_2(S_d;\mathbb Z)\) is free of rank \(\chi(S_d)-1=B_d\). The universal coefficient theorem gives
\[
H^1(K_d;\mathbb Z)\cong\mathbb Z^{L_d},\qquad
H^2(K_d;\mathbb Z)\cong\mathbb Z^{B_d}\oplus\mathbb Z/2,
\]
with all other reduced cohomology groups zero.

**5. Combinatorial Alexander duality.** For a complex on \(N_d\) vertices, the integral duality is
\[
\widetilde H_i(\Delta_3(F_d);\mathbb Z)
\cong\widetilde H^{N_d-i-3}(K_d;\mathbb Z).
\]
Substituting the preceding cohomology groups proves the formula in the Finding. The complexes have disconnected triples and thus have facets of cardinality \(N_d-3\), so they are pure of dimension \(N_d-4\). Because \(B_d>0\), their lower-degree rational reduced homology does not vanish, violating the empty-face necessary condition for Cohen–Macaulayness over every field. Shellable pure complexes have reduced homology concentrated in top degree, so shellability also fails.

## Verification

Run `python3 verify_folded_cube_cut.py` using Python 3 and no third-party dependencies. It constructs the folded quotient graphs for \(d=5\) and \(d=6\), independently enumerates connected triples and all candidate four-faces, verifies every free-face removal of the explicit square collapses, and computes signed square-boundary ranks over three prime fields. It additionally checks the Alexander-dual definition over all \(2^{16}\) subsets when \(d=5\), and verifies an independent acyclic discrete-Morse matching with integral attaching degrees \(0\) or \(\pm2\). Its full actual output is embedded in `verification_output.txt`. These finite checks corroborate, but do not replace, the all-\(d\) argument in the Proof.

## Relationship to prior work

Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue introduced ordinary cut complexes and proved structural theorems for several graph classes. Their construction of a graph realizing a projective-plane complex shows that torsion is possible in artificially constructed cut complexes, but it does not give the present folded-cube family or the explicit homology groups. The sequel treats disjoint unions, squared paths and grids. Previous reductions of triangle-free graph cut complexes to square-filling topology also reduce the problem to the unknown integral topology of the square complex; the new ingredient here is the identification of that square complex as an antipodal quotient of the simply connected cubical two-skeleton, giving its exact \(\mathbb Z/2\) fundamental group and all integral Betti numbers. Four-cycle studies of rectagraphs include folded cubes, but do not supply this cut-complex homology classification.

## Limitations

Only reduced integral homology of the ordinary three-cut complexes is determined; no homotopy classification of the cut complexes, integral symmetry representation, or persistence-map classification is claimed. The square complex's fundamental group is computed, not the fundamental group of the cut complex. The result applies to the antipodal-vertex quotient model of folded cubes, not to the graph produced by *adding* antipodal edges without quotienting vertices. The exact formula requires \(d\ge5\); smaller dimensions admit extra short relations and require separate analysis. The statement does not claim to be the first example of torsion in cut complexes.

## References

1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675 (first posted 2023-04-26), later SIAM Journal on Discrete Mathematics 38 (2024), 1630–1675, DOI:10.1137/23M1569034.
2. M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram, L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158 (2024-07-11), later SIAM Journal on Discrete Mathematics 39 (2025), 1123–1157, DOI:10.1137/24M1676077.
3. K. Bouanane, A. Berrachedi, *4-cycle properties for characterizing rectagraphs and hypercubes*, Czechoslovak Mathematical Journal 67 (2017), 29–36, DOI:10.21136/CMJ.2017.0227-15.
