# Sharp three-token exchange geometry of minimum 2-rainbow functions on \(Q_4\)

## Finding

Let \(Q_4\) be the graph on \(\mathbb F_2^4\), with adjacency at Hamming distance one. A 2-rainbow dominating function assigns to each vertex a subset of the two named colors \(\{1,2\}\), requiring that every vertex assigned the empty set sees both colors in the union of its neighbors' labels. Its weight is the total number of assigned color tokens, counting a vertex labeled \(\{1,2\}\) twice.

There are exactly \(320\) minimum 2-rainbow dominating functions, all of weight \(7\). Under affine automorphisms of the four-cube together with a global interchange of the two colors, they form two orbits of sizes \(192\) and \(128\). The first orbit has no doubly labeled vertex; the second has exactly one.

Identify each assignment with a seven-element subset \(T\) of the \(32\) vertex-color slots \(\mathbb F_2^4\times\{1,2\}\). For two minimum assignments define the token-exchange distance \(\delta(T,U)=|T\setminus U|=7-|T\cap U|\). Among unordered pairs of different minima, its distribution is

\[
\begin{array}{c|ccccc}
\delta&3&4&5&6&7\\\hline
\#\text{pairs}&4320&1440&22080&11520&11680.
\end{array}
\]

In particular, any two different minima require changing at least three color-token slots. Join two minima when \(\delta=3\), permitting exactly three simultaneous token relocations and requiring feasibility only at the endpoints. This exchange graph is connected, \(27\)-regular, and has \(320\) vertices, \(4320\) edges, radius \(3\), and diameter \(3\). The two orbit classes form an equitable partition: a vertex with no doubled label has \(15\) neighbors within its orbit and \(12\) in the other; a vertex with one doubled label has \(9\) neighbors within its orbit and \(18\) in the other.

## Assumptions and scope

The graph is the fixed, labeled four-dimensional binary cube, with vertices identified with integers \(0,\ldots,15\) in binary and neighbors obtained by toggling exactly one of the four bits. Both colors are named. A token is a pair \((v,c)\), not an unlabeled vertex. In the three-token exchange graph, intermediate configurations are not required to remain dominating; only the two endpoint functions are feasible minimum-weight functions. All enumeration counts distinguish labeled assignments. The isomorphism \(Q_4\cong C_4\square C_4\) places the result in the square toroidal-grid setting.

## Proof

Encode the placements of colors \(1\) and \(2\) by two masks \(A,B\subseteq\{0,\ldots,15\}\). The weight is \(|A|+|B|\), with overlaps counted twice. Write \(N(v)=\{v\mathbin{\mathrm{xor}}1,v\mathbin{\mathrm{xor}}2,v\mathbin{\mathrm{xor}}4,v\mathbin{\mathrm{xor}}8\}\). The necessary and sufficient condition for a 2-rainbow dominating function is

\[
\forall v\notin A\cup B:\quad N(v)\cap A\ne\varnothing\quad\text{and}\quad N(v)\cap B\ne\varnothing.
\]

Every assignment of weight at most \(7\) appears exactly once among the pairs \((A,B)\) with \(|A|+|B|\le7\); equivalently, it is a subset of size at most \(7\) of the \(32\) named vertex-color slots. There are precisely \(\sum_{k=0}^7\binom{32}{k}=4{,}514{,}873\) such subsets. The embedded standalone Python checker enumerates each of them directly, applies the displayed necessary-and-sufficient test, and obtains feasible counts \((0,0,0,0,0,0,0,320)\) at weights \(0,\ldots,7\). The independently implemented C++ checker loops instead over paired color masks grouped by their separate Hamming weights and obtains identical counts. Hence the minimum is \(7\) and its multiplicity is \(320\); no smaller or omitted cases are possible.

The affine automorphism group consists of all maps \(v\mapsto\pi(v)\mathbin{\mathrm{xor}}b\), where \(\pi\) permutes the four bit positions and \(b\) is a four-bit vector. Its order is \(16\cdot24=384\). Together with the global color swap, it acts on feasible functions via a group of order \(768\). Representatives, written as the pair of hexadecimal \((A,B)\) masks, are \((0x0118,0xe001)\) and \((0x0181,0x6801)\). Both satisfy the feasibility condition and have weight seven. Direct enumeration of their images under the stated \(768\) transformations gives orbit sizes \(192\) and \(128\), respectively, whose total \(320\) exhausts the minimum functions. Overlap cardinality \(|A\cap B|\) is invariant, and equals zero on the first orbit and one on the second, so the two orbits are distinct.

For any two minima, the token distance is half the population count of the XOR of their two distinct \(32\)-bit slot masks. Checking all \(\binom{320}{2}=51{,}040\) unordered pairs yields the distance table above, including zero pairs at distances one or two. For the distance-three graph, connect exactly those pairs whose XOR has population count six. The table gives \(4320\) edges, and an exhaustive neighbor count gives degree \(27\) at each vertex. Breadth-first search from *every* one of the \(320\) vertices reaches all \(320\) and attains maximum distance \(3\). Therefore the graph is connected with radius and diameter three. Counting neighbors by the invariant \(|A\cap B|\) proves the asserted equitable-partition row sums. All exhaustive bounds and checks are implemented in `code/verify_colortokens.py` and independently corroborated for the cardinalities, distances, regularity, and diameter by `code/verify_color_masks.cpp`.

## Verification

Run `python3 code/verify_colortokens.py`. The program uses only the Python standard library and checks all \(4{,}514{,}873\) assignments of weight at most seven, both symmetry orbits, all \(51{,}040\) distinct pairs and breadth-first distances. Run `c++ -O2 -std=c++17 code/verify_color_masks.cpp -o verify_color_masks` followed by `./verify_color_masks`; this separately enumerates the two 16-bit color masks and rechecks the principal metrics. Their actual recorded outputs are in `logs/colortokens.out` and `logs/color_masks.out`. Both implementations passed their embedded assertions on execution. The mathematical force of these exhaustive checks is finite and does not extend to cubes of other dimensions.

## Relationship to prior work

The identity \(Q_4\square K_2\cong Q_5\) translates these functions into minimum dominating sets of the five-cube, or optimal binary radius-one covering codes of length five. Östergård and Weakley (2000) classify optimal binary covering codes of length at most eight up to full cube equivalence. Thus the optimum cardinality, and possibly much of the underlying optimizer enumeration, lie within earlier stronger code-classification coverage. That prior result does not visibly state the distance-three exchange graph, its connected diameter-three structure, or the equitable partition with degrees \((15,12)\) and \((18,9)\); those sharpened exchange properties are the sole proposed novelty, with the unresolved full-text comparison explicitly acknowledged. Stȩpień, Szymaszkiewicz and Zwierzchowski (first public 19 September 2013) study 2-rainbow domination in Cartesian products of cycles and characterize equality in a general lower bound. Their published open-access text neither formulates this seven-token optimum-state exchange graph nor gives the displayed orbit/distance classification. Shao, Li, Erveš and Žerovnik (2019) determine the minimum 2-rainbow domination numbers of \(C_4\square C_n\) and \(C_8\square C_n\). The value seven is thus context rather than a claimed discovery. The available abstract does not give the full optimizer geometry, but its full article could not be examined; the resulting priority uncertainty remains genuine. Other work on Cartesian-cycle 2-rainbow domination gives scalar bounds and constructions, not a verified coverage comparison with all optimizer-state geometry. The proposed contribution is the *sharp three-token exchange graph, its diameter, and its equitable two-class degree structure*, not the already studied covering-code classification, rainbow domination number, or bare enumeration of optimum functions.

## Limitations

This is a finite exact theorem only for \(Q_4\). Exchange edges allow simultaneous relocation of three color tokens between endpoint solutions, without requiring that intermediate configurations remain feasible. The complete 2019 rainbow-domination article and 2000 optimal-covering-code classification were inaccessible in this examination, leaving a material unresolved publication-priority comparison. Publication priority is not independently certified. Exhaustive code execution constitutes reproducible finite reasoning, not independent peer review or a general-dimensional proof.

## References

1. Z. Stȩpień, L. Szymaszkiewicz and M. Zwierzchowski, *The Cartesian product of cycles with small 2-rainbow domination number*, first published 2013-09-19, Journal of Combinatorial Optimization 30 (2015), 668–674. DOI: 10.1007/s10878-013-9658-0. https://link.springer.com/article/10.1007/s10878-013-9658-0
2. Z. Shao, Z. Li, R. Erveš and J. Žerovnik, *The 2-Rainbow Domination Numbers of \(C_4\square C_n\) and \(C_8\square C_n\)*, National Academy Science Letters 42 (2019), 411–418. DOI: 10.1007/s40009-018-0779-y. https://link.springer.com/article/10.1007/s40009-018-0779-y
3. S. Brezovnik, D. Rupnik Poklukar and J. Žerovnik, *The 2-rainbow domination number of Cartesian product of cycles*, Ars Mathematica Contemporanea 25 (2025), paper P3.04. DOI: 10.26493/1855-3974.3168.74d.

4. P. R. J. Östergård and W. D. Weakley, *Classification of binary covering codes*, Journal of Combinatorial Designs 8 (2000), 391–401; first public 2000-10-16. DOI: 10.1002/1520-6610(2000)8:6<391::AID-JCD1>3.0.CO;2-R.
