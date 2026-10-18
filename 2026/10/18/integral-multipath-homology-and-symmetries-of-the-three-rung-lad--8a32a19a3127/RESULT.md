# Integral multipath homology and symmetries of the three-rung ladder

## Finding
Let \(L=P_3\square K_2\) be the undirected three-rung ladder on six vertices, and let \(D=\overleftrightarrow L\) contain both orientations of each of its seven undirected edges. Write \(X(D)\) for the simplicial complex of all nonempty subsets of arcs that form vertex-disjoint directed paths, with directed cycles excluded (and include the empty face in the abstract complex). Then its reduced **integral** homology is
\[
\widetilde H_k(X(D);\mathbb Z)\cong
\begin{cases}
\mathbb Z^3,&k=2,\\
\mathbb Z^4,&k=3,\\
\mathbb Z^2,&k=4,\\
0,&\text{otherwise}.
\end{cases}
\]
In particular there is no homological torsion. The complex is connected.

The full graph automorphism group is \(V_4=\langle h,v\mid h^2=v^2=1,\ hv=vh\rangle\), where \(h\) exchanges the two rows and \(v\) reverses the three columns. Its **rational** homology characters, in the order \((1,h,v,hv)\), are
\[
\chi_2=(3,1,-1,1),\qquad
\chi_3=(4,0,0,0),\qquad
\chi_4=(2,0,0,-2).
\]
Writing \(\mathbb Q_{\epsilon,\delta}\) for the one-dimensional representation on which \(h\) acts by \(\epsilon\in\{+1,-1\}\) and \(v\) acts by \(\delta\in\{+1,-1\}\), the decompositions are
\[
\begin{aligned}
\widetilde H_2(X(D);\mathbb Q)&\cong \mathbb Q_{+,+}\oplus\mathbb Q_{+,-}\oplus\mathbb Q_{-,-},\\
\widetilde H_3(X(D);\mathbb Q)&\cong\mathbb Q[V_4],\\
\widetilde H_4(X(D);\mathbb Q)&\cong \mathbb Q_{+,-}\oplus\mathbb Q_{-,+}.
\end{aligned}
\]
Thus the invariant subspace dimensions in degrees \(2,3,4\) are \((1,1,0)\).

## Assumptions and scope
Label the top row \(0,1,2\), the bottom row \(3,4,5\), and take the edges
\[
\{01,12,34,45,03,14,25\}.
\]
For reproducibility index the directed arcs, starting at zero, by
\[
(0,1),(1,2),(3,4),(4,5),(0,3),(1,4),(2,5),
(1,0),(2,1),(4,3),(5,4),(3,0),(4,1),(5,2).
\]
Each face is encoded by the nonnegative integer whose binary digits indicate its selected arcs. A set of arcs is a multipath precisely when every vertex has indegree and outdegree at most one **and** it contains no directed cycle. This characterization includes disjoint unions of isolated vertices as spanning components. The theorem concerns this particular symmetric digraph, not every orientation, not a directed path-homology theory, and not a general ladder family.

## Proof
**Face enumeration.** There are fourteen possible arc vertices. Checking every binary mask from \(1\) to \(2^{14}-1\) by the preceding indegree/outdegree and directed-cycle test yields exactly \(290\) nonempty faces with dimension counts
\[
(f_0,f_1,f_2,f_3,f_4)=(14,64,116,80,16).
\]
The enumeration criterion is necessary and sufficient: indegree/outdegree at most one makes every connected component an oriented path or directed cycle, and the cycle test excludes the latter. The file `verify_morse.py` implements this criterion; `verify_independent.py` implements it separately.

**Acyclic matching.** Process the arc indices in the fixed order
\[
5,6,8,1,3,9,12,0,7,13,2,11,4,10.
\]
For each index, pair every currently unpaired face omitting that arc with its union with the arc, whenever the latter is also currently unpaired. Each face is used at most once. The complete collection of \(140\) pairs and its \(10\) unmatched faces is recorded in `matching_certificate.json`. Reverse the covering arrows of the face Hasse diagram on matched pairs, leaving the other covering arrows oriented downward. The explicit topological ordering in that certificate respects all \(876\) resulting arrows, proving acyclicity; `verify_morse.py` checks every arrow. The remaining critical-cell counts are
\[
(c_0,c_1,c_2,c_3,c_4)=(1,0,3,4,2).
\]

**Integral Morse differential.** Orient a simplicial face by increasing arc index. The ordinary integral boundary is the alternating sum obtained by deleting one index. For every matched pair \((s,t)\), with \(s\) the lower-dimensional face, the coefficient \(a=[s]\partial t\) is \(+1\) or \(-1\) at the moment of cancellation. For every surviving cell \(x\) of the same dimension as \(t\), replace its boundary by
\[
\partial'x=\partial x-\frac{[s]\partial x}{a}(\partial t-a s),
\]
and remove the matched generators. This is an integral unit-pivot chain contraction. All \(140\) operations are performed with explicit integer coefficients by `verify_morse.py`; every pivot is a unit and the **entire** resulting differential on the ten critical cells is zero. By acyclic discrete Morse theory (or the displayed elementary integral chain contractions), the Morse chain complex computes the integral homology of \(X(D)\). One critical vertex establishes connectedness, and the remaining nine critical cells give the groups in the statement without torsion. This argument proves homology, not an asserted wedge-of-spheres homotopy type.

**Equivariance.** The automorphisms are the identity, the row swap \(h=(0\,3)(1\,4)(2\,5)\), the column reversal \(v=(0\,2)(3\,5)\), and their product. On the original simplicial chain complex, an automorphism maps each arc to its image and multiplies a face by the sorting-permutation sign. The integral chain contractions above yield an explicit chain projection to, and cycle lifts from, the critical generators. Consequently the action on the zero-differential Morse complex is computed by: lift each critical cell as an integral cycle, apply the signed simplicial action, and project to critical cells. The program `verify_symmetry.py` implements both maps, checks that every lift is a cycle and projects back to its generator, verifies the relations \(h^2=v^2=1\) and \(hv=vh\) on each homology group, and obtains exactly the three stated characters. Orthogonality of the four characters of \(V_4\) gives the displayed rational decompositions.

## Verification
All necessary artifacts are included alongside this text: `matching_certificate.json`, `verify_morse.py`, `verify_symmetry.py`, `verify_independent.py`, and the three corresponding `.out.txt` files. Running each script with Python 3 requires no third-party packages. The first script checks all \(290\) faces, \(140\) pairs, \(876\) Hasse arrows, integral unit pivots and vanishing Morse boundaries. The symmetry script calculates the integral matrices and rational characters. The independent enumeration verifies the mod-two ranks
\[
(\operatorname{rank}\partial_1,\operatorname{rank}\partial_2,
\operatorname{rank}\partial_3,\operatorname{rank}\partial_4)
=(13,51,62,14),
\]
plus the reduced signed Lefschetz numbers \((1,1,-1,-1)\) for \((1,h,v,hv)\). The latter agree with the alternating sums of the computed homology traces. These independent checks do not replace the integral unit-pivot argument.

## Relationship to prior work
Caputi, Collari and Smith (2026) develop multipath complexes of *bidirectional paths and polygons*, including a bidirected-path suspension formula, polygon connectivity and homology computations. Their results do not state the integral homology or symmetry character for two adjacent bidirected squares. Caputi, Collari, Di Trani and Smith (2022/2024) determine various **oriented** grid multipath complexes; the products in their grid section are directed grids with specified orientations, not fully bidirected ladders with two-cycles. Hence the identified grid results cannot be substituted for the present directed graph. The related ordinary discrete-Morse complex of the same ladder and total-cut complexes of ladders have different simplices and different homology functors.

This finite result isolates the first two-square attachment beyond one bidirected square. In contrast with the one-cycle and path cases, it exhibits nonzero reduced homology in **three consecutive dimensions**, together with a nontrivial distribution among the four natural symmetries. Searches of accessible scholarly records found no theorem implying these groups or characters; this is a bounded literature comparison, not a claim of exhaustive global novelty.

## Limitations
No homotopy equivalence to a wedge of spheres is claimed. In particular, zero integral Morse differentials do not exclude higher homotopy attaching maps in this dimension range. There is no assertion for longer ladders, other edge orientations, arbitrary digraphs, or unrestricted directed path homology. The originality assessment is limited by search indexing and unavailable full texts of some potentially related mathematical records. No independent external mathematical audit has been performed.

## References
1. L. Caputi, C. Collari, J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670 (initial public version 2026-01-09), especially Definition 1.2 and Section 2. https://arxiv.org/pdf/2601.05670
2. L. Caputi, C. Collari, S. Di Trani, J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656 (2022), especially Section 4.3 on oriented small grids. https://arxiv.org/pdf/2208.04656
3. L. Caputi, C. Collari, S. Di Trani, *Combinatorial and topological aspects of path posets, and multipath cohomology*, Journal of Algebraic Combinatorics (2023), especially the definition of the multipath complex. https://doi.org/10.1007/s10801-022-01180-9
