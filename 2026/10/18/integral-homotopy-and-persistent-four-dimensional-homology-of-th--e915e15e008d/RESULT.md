# Integral homotopy and persistent four-dimensional homology of the Clebsch forest filtration

## Finding
Let \(C\) be the sixteen-vertex Clebsch graph, and let \(F_d(C)\) be the degree-bounded *induced-forest* complex defined below. The complete integral homotopy filtration is
\[
F_d(C)\simeq
\begin{cases}
\bigvee^{9}S^3,&d=0,\\
S^4,&1\le d\le4,\\
\bigvee^{15}S^5,&d\ge5.
\end{cases}
\]
The first stage is a previously published result and is included only to describe the complete filtration. The new statements concern all the positive-degree stages and their persistence maps. In particular, the inclusion \(F_1(C)\hookrightarrow F_4(C)\) is an isomorphism on \(H_4(-;\mathbb Z)\); hence all intermediate inclusions also induce integral isomorphisms on the unique fourth-homology summand. Every positive-degree reduced integral homology group is free. For any field, the complete reduced persistence barcode is nine intervals \([0,1)\) in degree three, one interval \([1,5)\) in degree four, and fifteen intervals \([5,\infty)\) in degree five.

## Assumptions and scope
Write \(V(C)=\{0,1,\ldots,15\}=\mathbf F_2^4\) using four-bit integers. Distinct vertices \(u,v\) are adjacent precisely when their bitwise exclusive-or lies in \(\{1,2,4,8,15\}\). This is the degree-five Clebsch, or folded five-cube, graph with strongly regular parameters \((16,5,0,2)\), not its degree-ten complement.

For each integer \(d\ge0\), the abstract simplicial complex \(F_d(C)\) contains the empty simplex and precisely those nonempty \(\sigma\subseteq V(C)\) for which the induced graph \(C[\sigma]\) is a forest and every vertex of that induced forest has degree at most \(d\). The filtration uses *inclusion maps on identical labelled vertices*. Since \(C\) has degree five, \(F_5(C)=F_\infty(C)\). No claim is made for arbitrary graphs, other folded cubes, or a continuous metric filtration. Coefficients are integral unless specified otherwise.

## Proof
**Exhaustive face criterion and reproducible matching.** For each of the \(2^{16}-1\) nonempty vertex subsets, the verifier independently tests acyclicity by component/edge counting and by union-find cycle detection; for a forest it also measures the induced maximum degree. For each \(d\in\{0,1,2,3,4,5\}\), it forms the entire face set. The numbers of nonempty faces, codimension-one face incidences and acyclic matching pairs, in increasing order of \(d\), are
\[
\begin{array}{c|rrrrrr}
d&0&1&2&3&4&5\\\hline
\text{faces}&392&2142&7262&12542&13822&13838\\
\text{incidences}&1200&9280&36160&68560&77520&77616\\
\text{pairs}&191&1070&3628&6270&6910&6911
\end{array}
\]
The matching is specified completely by the sixteen-vertex permutation `ORDERS[d]` in `verify.py`: for every vertex in the prescribed order, scan currently unmatched lower faces in increasing bit-mask order, pairing each lower face with its one-vertex upper face when the upper face is also unmatched. No unlisted pairing choices are permitted. Reverse all matched covering relations in the face-poset Hasse graph; keep unmatched relations directed upwards. Topological sorting consumes *every* face for each stage, establishing acyclicity of each entire matching (not merely sampled subgraphs). The critical faces have dimensions and multiplicities
\[
\begin{array}{c|l}
d&\text{critical cells}\\\hline
0&\text{one 0-cell; nine 3-cells}\\
1&\text{one 0-cell; one 4-cell}\\
2&\text{one 0-cell; two 3-cells; three 4-cells}\\
3&\text{one 0-cell; one 4-cell}\\
4&\text{one 0-cell; one 4-cell}\\
5&\text{one 0-cell; fifteen 5-cells}.
\end{array}
\]
By Forman's acyclic-matching theorem, for \(d=0,1,3,4,5\) the corresponding CW model consists only of one zero-cell and the listed same-dimensional positive cells, so it has exactly the claimed wedge-of-spheres homotopy type. The \(d=0\) case reconfirms, but does not newly claim, the independently published degree-zero classification.

**The degree-two stage.** To resolve the only mixed-dimensional Morse model, the verifier computes the *integral* Morse differential with the increasing-vertex orientation on all simplices. It recursively eliminates matched lower faces, with each coefficient determined by the signed simplicial boundary of its matched upper face. Sorting the two critical 3-cells and three critical 4-cells by bit-mask gives
\[
\partial_4^{\mathrm{Morse}}=
\begin{pmatrix}-1&-1&0\\-1&0&-1\end{pmatrix}.
\]
Its first two columns have determinant \(-1\). Thus its image is all of \(\mathbb Z^2\), its kernel is \(\mathbb Z\), and its integer Smith invariant factors are both one. Since the Morse model has no one- or two-cells, it is 2-connected; the attaching map of its three 4-cells lands in a wedge of two 3-spheres. The unimodular boundary matrix can be implemented by cellular slides and cancellations (equivalently, its associated 2-connected 4-complex is homotopy equivalent to \(S^4\) by Hurewicz and Whitehead). Hence \(F_2(C)\simeq S^4\), integrally, with no torsion.

**The persistence map, rather than only the stages.** The standalone `cycle_cocycle.json` stores an exact signed 4-chain \(z\) supported on 96 distinct four-simplices of \(F_1(C)\) and a signed 4-cochain \(\varphi\) supported on 143 four-simplices of \(F_4(C)\). Every listed coefficient is \(+1\) or \(-1\), and the labels are the same integer bit masks used throughout. `verify.py` computes every signed face of every term of \(z\) and confirms \(\partial z=0\). It checks \(\delta\varphi=0\) on all 4,360 five-simplices of \(F_4(C)\), and obtains the exact integer evaluation
\[
\langle\varphi,z\rangle=-1.
\]
Since \(H_4(F_1(C);\mathbb Z)\cong H_4(F_4(C);\mathbb Z)\cong\mathbb Z\), this unit pairing forces the image of the degree-four class from \(F_1(C)\) to be primitive and nonzero in \(H_4(F_4(C);\mathbb Z)\). The inclusion map is therefore multiplication by \(+1\) or \(-1\), hence an isomorphism. Factorization through \(F_2(C)\) and \(F_3(C)\), each also with \(H_4\cong\mathbb Z\), forces *each* consecutive map to be an integral isomorphism. The fourth-homology class dies at stage five because that stage has \(H_4=0\). The degree-three classes die at stage one and the degree-five classes first appear at stage five. These facts prove the stated barcode over \(\mathbb Z\) (as free interval summands here) and over every field.

## Verification
All computational prerequisites and outputs are embedded as three standalone files: `verify.py`, `cycle_cocycle.json`, and `verify_output.txt`. From a directory containing those files, execute `python3 verify.py` with a standard Python 3 interpreter. It must exit successfully, print the six `STAGE_` lines with full acyclicity checks, the integer Morse boundary and integral cycle/cochain evaluation, and end with `VERIFY_OK`. The exact captured output is in `verify_output.txt`. The verifier uses no network, external packages, random choices, or stored unverified face lists; it regenerates the complete face posets and matches.

Two independent forest-recognition algorithms must agree on all 65,535 nonempty subsets; the graph degree and pairwise common-neighbor specifications are also checked. The program verifies the Morse boundary at the mixed stage and tests the cycle and cocycle conditions on their full relevant domains. Finite computations give an exhaustive proof *for this specified finite graph*, not a theorem about all finite graphs.

## Relationship to prior work
Andrés Carnero Bravo introduced this degree-bounded induced-forest filtration and computed homotopy types for graph families including paths, cycles, double stars, cacti, joins and graph products; the manuscript classifies neither the sixteen-vertex Clebsch graph nor these persistence maps [1]. Its first public version appeared on July 25, 2023. Previously published exact work on the same Clebsch graph already established \(F_0(C)=\operatorname{Ind}(C)\simeq\bigvee^9S^3\) [2]. This starting term is prior art. The present complete positive-degree classification and the primitive degree-four persistence map are not logical consequences of that degree-zero classification. Neighborhood and Čech complexes of the same graph use different face conditions and do not imply the induced-forest statements.

## Limitations
This is an exact finite classification for the standard degree-five Clebsch graph; it does not classify arbitrary strongly regular graphs or higher folded cubes. The homotopy conclusions rely on exhaustive integer bit-mask computations, elementary discrete Morse theory, and standard connectivity theorems. The persistence computation proves the specified inclusion-induced maps, not the action of the automorphism group. Searches do not exclude unindexed equivalent literature; no independent mathematical audit has been performed.

## References
1. A. Carnero Bravo, *The Forest Filtration of a Graph*, arXiv:2307.13271, first public version July 25, 2023, especially Sections 1, 3, and 4. https://arxiv.org/abs/2307.13271
2. *The folded five-cube independence complex is a wedge of nine three-spheres*, published mathematical research record, identifier `fb89079b9172`, 2026 (previous \(d=0\) classification).
3. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145, DOI: 10.1006/aima.1997.1650.
