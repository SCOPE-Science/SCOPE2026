# Initial integral homotopy types of circular-ladder matching complexes

## Finding

For every integer \(3\le n\le8\), write \(P_n=C_n\square K_2\) and let \(\mathcal M(P_n)\) be the ordinary matching complex. Its integral homotopy type is

\[
\begin{aligned}
\mathcal M(P_3)&\simeq\bigvee^{6}S^1,\\
\mathcal M(P_4)&\simeq\bigvee^{4}S^2,\\
\mathcal M(P_5)&\simeq\bigvee^{2}S^2\vee\bigvee^{2}S^3,\\
\mathcal M(P_6)&\simeq\bigvee^{12}S^3,\\
\mathcal M(P_7)&\simeq\bigvee^{14}S^4,\\
\mathcal M(P_8)&\simeq\bigvee^{3}S^4\vee\bigvee^{7}S^5.
\end{aligned}
\]

The four orders \(5\le n\le8\) are the new finite classification. The smaller orders are included to fix conventions and continuity; the cube case \(n=4\) already appears in a mathematical record. The answer gives **integral homotopy**, stronger than Betti-number calculations.

## Assumptions and scope

Here \(C_n\) is the simple cycle on \(\mathbb Z/n\mathbb Z\); the vertex set of \(P_n\) is \(\{(i,a): i\in\mathbb Z/n\mathbb Z,\ a\in\{0,1\}\}\). Its \(3n\) graph edges are \(\{(i,a),(i+1,a)\}\) for each rim layer \(a=0,1\) and index \(i\), and \(\{(i,0),(i,1)\}\) for each rung \(i\). A face of \(\mathcal M(P_n)\) is any collection of those edges having mutually disjoint endpoints. This is **not** the perfect matching complex, and not a graph cut complex. All homotopy equivalences are of unbased finite CW spaces, with integer coefficients and no localization. The range \(3\le n\le8\) is exhaustive for this statement; no recurrence or asymptotic extrapolation is claimed.

## Proof

We give a finite, algorithmically exhaustive integral proof, specified by the self-contained script `prism_morse_certificate.py`. This script uses only Python's standard library. It lists every nonempty matching face as a bitset of graph-edge indices, in the exact edge order defined above: first \(n\) edges of layer zero, then \(n\) edges of layer one, then \(n\) rungs. The complete face counts for \(n=3,4,5,6,7,8\) are \(31,107,341,1103,3543,11395\), respectively.

For each of the six values, `ORDERS[n]` supplies an explicit permutation of the \(3n\) edge indices. Process pivots from left to right. At a pivot index, pair every currently unmatched face not containing the pivot with its coface obtained by adjoining the pivot, provided both faces are still available; remove both and continue. This specifies all matched Hasse edges unambiguously. The checker explicitly orients each unmatched covering relation downward and each matched relation upward, constructs the full directed Hasse graph, and topologically sorts it. A complete topological sort, checked on every covering relation, proves **acyclicity** of the matching and hence validates the discrete-Morse reduction.

The resulting numbers of critical simplices by dimension are

\[
\begin{array}{c|r|r|l}
n&\text{faces}&\text{matched pairs}&\text{critical counts}\ 
3&31&12&1\text{ in degree }0,\ 6\text{ in degree }1\\
4&107&51&1\text{ in degree }0,\ 4\text{ in degree }2\\
5&341&168&1\text{ in degree }0,\ 2\text{ in degree }2,\ 2\text{ in degree }3\\
6&1103&545&1\text{ in degree }0,\ 12\text{ in degree }3\\
7&3543&1764&1\text{ in degree }0,\ 14\text{ in degree }4\\
8&11395&5691&1\text{ in degree }0,\ 4\text{ in degree }4,\ 8\text{ in degree }5.
\end{array}
\]

The degree-zero cell is unique in every case. With no critical cells in adjacent positive dimensions, the claimed one-degree sphere wedges for \(n=3,4,6,7\) follow immediately from the Morse CW complexes (the one-dimensional case is a bouquet of circles).

For mixed-dimensional cases, the **integral** boundary, not just its rank modulo a field, is required. The script recursively projects simplicial boundaries along the matched gradient paths. Signs come from the increasing edge-index orientation, and the recursion uses the equation obtained by setting the boundary of every matched upper cell equal to zero to eliminate its lower partner. This computes the signed cellular boundary of the critical-cell Morse complex.

For \(n=5\), the complete \(2\)-by-\(2\) degree-three-to-degree-two Morse boundary is the zero matrix, so the two 3-cells attach trivially to a bouquet of two 2-spheres. Since \(\pi_2(S^2\vee S^2)\cong\mathbb Z^2\), an attaching map with zero degree vector is null-homotopic. This gives the stated wedge with two 2-spheres and two 3-spheres.

For \(n=8\), in the script's critical-cell order, the complete degree-five-to-four Morse matrix has eight rows and four columns. Only rows 3, 6 and 8 (one-based) are nonzero, and these are respectively \((1,0,0,-1)\), \((1,0,0,-1)\), and \((-1,0,0,1)\). Thus the matrix has rank one and a unit maximal minor, with Smith normal form \(\mathrm{diag}(1,0,0,0)\). In the corresponding CW complex the initial four 4-cells form \(\bigvee^4S^4\), and the homotopy classes of the eight attaching maps are determined by their integer degree vectors in \(\pi_4(\bigvee^4 S^4)\cong\mathbb Z^4\). Integral basis changes reduce the primitive rank-one map to a unit attaching map, which cancels one 4-cell and one 5-cell. Seven 5-cells and three 4-cells remain, producing the asserted integral wedge. There are no other critical cells or attaching maps.

For each value all simplex enumeration, pair counts, DAG orientations, critical-cell lists, signed boundaries, and rank assertions are regenerated and checked, rather than copied from an external log. The explicit pivot permutations and edge-label conventions make the proof finite, deterministic, and reproducible.

## Verification

Run `python3 prism_morse_certificate.py` and compare the resulting stdout byte-for-byte to `prism_morse_certificate_output.txt`. It checks every face and every directed Hasse covering edge, and calculates each required integer Morse matrix. The numbers of directed Hasse edges in order \(n=3,4,5,6,7,8\) are \(48,252,1020,4002,15022,55272\).

Independently run `python3 prism_f2_independent.py` and compare its stdout to `prism_f2_output.txt`. This second implementation enumerates faces by graph-vertex occupancy recursion, rather than by edge-index compatibility, and performs exact bitset Gaussian elimination on **original** simplicial boundary matrices over \(\mathbf F_2\). Its reduced mod-two Betti numbers in the positive degrees are respectively \((6),(4),(2,2),(12),(14),(3,7)\), agreeing with the homotopy types; the Morse checker supplies the crucial integral and attaching-map proof.

## Relationship to prior work

Agarwal and Basak, arXiv:2608.30601 (first public version August 31, 2026), determine the independence and **perfect** matching complexes of Möbius and circular ladders. Their Problem 26 explicitly asks for the homotopy types of the **ordinary matching complexes**. Those existing perfect-matching results do not imply our ordinary-matching classification because the complexes have different definitions and face sets. Bayer, Jelić Milutinović, and Vega, arXiv:2411.04601, prove the wedge property for outerplanar graphs. Our prism graphs are planar but not outerplanar: a nonempty finite outerplanar simple graph has a vertex of degree at most two, whereas every prism vertex has degree three. Therefore that theorem does not apply. Existing records giving the three-cube's ordinary matching type cover only \(n=4\). Other circular-ladder cut-complex and Möbius-ladder matching results study different simplicial complexes or different graphs. Searches using matching-complex/circular-ladder, prism homotopy, each size and mixed-dimensional sphere terms identified no statement covering the four new cases, subject to the risks below.

## Limitations

The proved result is restricted to the six sizes \(3\le n\le8\); **nothing** is proved here about larger prisms, or all planar graphs. There is no claim of a conceptual uniform recurrence or shellability. The code is a fully exhaustive finite certificate rather than an infinite-family argument. A finite original statement is not a proof of the unrestricted open Problem 26. Bibliographic searches cannot establish uniqueness, and obscure or unindexed contemporaneous treatments might overlap. Mod-two computations alone cannot detect integral torsion or verify homotopy; the complete signed Morse computation is essential.

## References

1. Anshu Agarwal and Biplab Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601, first version August 31, 2026, especially Problem 26. https://arxiv.org/abs/2608.30601
2. Margaret Bayer, Marija Jelić Milutinović, and Julianne Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601, first version November 7, 2024. https://arxiv.org/abs/2411.04601
3. R. Forman, *Morse Theory for Cell Complexes*, Adv. Math. 134 (1998), 90–145 (discrete-Morse CW and gradient-path boundary framework).
