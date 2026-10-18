# Exact one-vertex recoloring geometry of the seven-point Fano plane
## Finding
Let \(F\) be the unique Steiner triple system on seven labeled points, with lines
\[
\begin{aligned}
&\{1,2,3\},\ \{1,4,5\},\ \{1,6,7\},\ \{2,4,6\},\\
&\{2,5,7\},\ \{3,4,7\},\ \{3,5,6\}.
\end{aligned}
\]
A *weak proper three-coloring* is a map \(\sigma:\{1,\ldots,7\}\to\{0,1,2\}\) for which no listed triple is monochromatic. Its recoloring graph \(\mathcal R_3(F)\) has these maps as vertices; two are adjacent when they differ at exactly one point. Colors are labeled, so global palette relabelings give different vertices.

The hypergraph admits no weak proper two-coloring. The graph \(\mathcal R_3(F)\) is connected and has **882 vertices and 3906 edges**, **radius and diameter both seven**, and
\[
h(\sigma,\tau)\ \le\ d_{\mathcal R_3(F)}(\sigma,\tau)\ \le\ h(\sigma,\tau)+1
\]
for *every* ordered pair of proper weak three-colorings. Among its \(\binom{882}{2}=388521\) unordered pairs, precisely **2268** need one extra recoloring; the remaining **386253** attain Hamming distance. The degree frequencies are \(252\) of degree \(8\), \(504\) of degree \(9\), and \(126\) of degree \(10\). Under the full line-preserving point-automorphism group together with color relabelings, the coloring orbits have sizes \(126,252,504\), characterized respectively by sorted color-class size vectors \((1,2,4)\), \((1,3,3)\), and \((2,2,3)\).

## Assumptions and scope
Identify each point with its nonzero three-bit vector, numbered \(1\) through \(7\); three points form a line precisely when their binary XOR is zero. The weak condition permits three distinct colors on a line but forbids one common color. Thus it differs from a *bicoloring* in the sense of Colbourn, Dinitz and Rosa [1], which demands exactly **two** colors on every line. A single recoloring must leave **every intermediate coloring** weakly proper. Both coloring and distance counts are for the fixed seven-point object, not for arbitrary Steiner triple systems.

## Proof
**1. Exhaustion and chromatic threshold.** There are \(3^7=2187\) maps of the seven points to the three allowed colors. For each map, test all seven explicitly stated triples and retain it exactly when none is monochromatic. This exhaustive predicate returns \(882\) colorings. The identical exhaustive test with the two-color alphabet returns zero. An independent count uses inclusion–exclusion on the seven events that one specified line is monochromatic. For any set of lines, identify all points within every chosen line and count the resulting equivalence classes. Enumerating the \(2^7=128\) line subsets gives the weak chromatic polynomial
\[
P_F(q)=q^7-7q^5+21q^3-21q^2+6q.
\]
Substitution yields \(P_F(3)=882\) and \(P_F(2)=0\).

**2. The exact recoloring graph.** From each proper coloring replace each of its seven coordinate colors in turn by each of the other two colors, retaining an edge only if the result is proper. This visits all and only Hamming-distance-one neighbors; a separate all-pairs comparison reconstructs the identical edge set. The resulting degree histogram is exactly \(\{8:252,9:504,10:126\}\). Since the sum of degrees is \(7812\), the edge count is \(3906\).

**3. Certified symmetry reduction.** The \(168\) invertible binary-linear maps of \(\mathbb F_2^3\) are generated exhaustively by assigning three linearly independent nonzero images to its standard basis. Each permutes the seven nonzero vectors and preserves the seven lines. Conversely, any line-preserving permutation is determined by its images of the three noncollinear basis points \(1,2,4\): their images must be noncollinear, and the line relations uniquely force the images of all four remaining points. Thus this is the full point-automorphism group. Together with all six permutations of the three color names, these transformations act as automorphisms of both \(\mathcal R_3(F)\) and ambient Hamming distance. Applying all such transformations to representatives and removing their orbits partitions the \(882\) colorings into orbits of sizes \(126,252,504\). Each orbit has constant sorted class-size vector \((1,2,4)\), \((1,3,3)\) or \((2,2,3)\), and these profiles separate the orbits. This exhausts the coloring set because the computed orbit sizes sum to \(882\). For a weak proper coloring with color classes \(C_0,C_1,C_2\), each monochromatic pair lies on a unique line and each two-color line contains one monochromatic pair. Thus the number of *rainbow* lines is exactly
\[
7-\sum_{i=0}^{2}\binom{|C_i|}{2}.
\]
It is respectively \(0,1,2\) on the three orbits. In particular, precisely the \(126\) colorings in the \((1,2,4)\) orbit satisfy the more restrictive all-lines-two-colored bicoloring condition; the other \(756\) states have at least one rainbow line and are absent from that historical state space.

**4. All-pairs distance bound.** Breadth-first search in the explicitly reconstructed graph from one representative of each of the three orbits visits all \(882\) states, and the largest reached distance is seven for each representative. For each target the checker computes both BFS distance \(d\) and the coordinate-difference count \(h\), verifying \(d-h\in\{0,1\}\). Group automorphisms preserve both metrics and send every source to one of those representatives, so the inequality holds for *all* coloring pairs. A second computation performs BFS from each of the \(882\) colorings without symmetry reduction, verifies eccentricity seven for every source, and counts \(2268\) unordered pairs with excess one and \(386253\) with excess zero. Hence connectedness, radius, diameter, sharp additive bound, and pair multiplicities follow from finite, exhaustive comparisons.

The additive term is genuinely necessary: colorings
\[
\sigma=(0,0,1,0,1,2,0),\qquad
\tau=(0,2,0,2,0,1,0)
\]
have \(h(\sigma,\tau)=5\) and verified shortest-path distance \(d=6\). A legal length-six recoloring path is, successively,
\[
\begin{gathered}
(0,0,1,0,1,2,0),\ (0,0,1,0,2,2,0),\\
(0,0,1,0,2,1,0),\ (0,0,1,2,2,1,0),\\
(0,2,1,2,2,1,0),\ (0,2,0,2,2,1,0),\\
(0,2,0,2,0,1,0).
\end{gathered}
\]
A diameter witness is \((0,0,1,0,1,2,0)\) and \((1,1,0,1,2,0,1)\), whose Hamming distance and graph distance both equal seven.

## Verification
Run `python3 verify_fano.py` with a standard Python 3 interpreter; no external packages, network connection or pre-existing data files are required. Its independent implementations compute all line constraints, all colorings, the two adjacency definitions, the \(168\) point symmetries, the palette-action orbits, exact breadth-first distances from three orbit representatives and separately from every source, the precise Hamming-excess histogram, and the independent inclusion–exclusion chromatic polynomial. All checks use integer arithmetic and assertions; there are no sampled states, numerical tolerances, heuristic timeouts or unverified solver outputs. The program prints PASS lines along with the numerical values in the finding. Reconfiguration edges and claimed shortest paths can be reproduced entirely from the seven triples above.

## Relationship to prior work
Colbourn, Dinitz and Rosa [1] distinguish ordinary weak coloring from their more restrictive *bicoloring*, and their Table in Section 2 lists the \((4,2,1)\) color-class split for a three-bicolorable order-seven design. This is an existence/split statement for only a subset of weak colorings; it does not classify **all** weak three-colorings or analyze one-point recoloring edges, distances or their excess above Hamming distance. De Brandes, Phelps and Rödl [2] investigate weak chromatic numbers and existence of highly chromatic Steiner triple systems, rather than this finite solution graph. Anastos and Frieze [3,4] define precisely the same one-coordinate-change graph for weak hypergraph colorings, but their theorems concern random hypergraphs under large-parameter probabilistic hypotheses and imply none of the exact seven-point counts or pairwise distance inequalities. Henning and Yeo [5] treat the two-colorability obstruction of the Fano plane and higher-uniformity free-set problems, not exact three-color recoloring. These contrasts are of the statements and hypotheses, not merely of paper titles.

## Limitations
The result is a finite classification of the uniquely specified \(7\)-point Fano-plane hypergraph with an *exactly three-color palette*, and gives no theorem for general projective planes, larger Steiner triple systems, additional colors, or mixing times. The checker is an executable exhaustive proof of the finite claims, not a formally verified proof in a proof assistant. The accessible literature search does not guarantee absence of unindexed prior work; some historically relevant full texts were accessible only as bibliographical descriptions or abstracts. No independent audit is asserted here.

## References
[1] C. J. Colbourn, J. H. Dinitz and A. Rosa, *Bicoloring Steiner Triple Systems*, Electron. J. Combin. **6** (1999), R25, first published 1999-05-24, DOI: 10.37236/1457. Open full text: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v6i1r25/pdf/.

[2] M. de Brandes, K. T. Phelps and V. Rödl, *Coloring Steiner Triple Systems*, SIAM J. Algebraic Discrete Methods **3** (1982), 241–249, DOI: 10.1137/0603023 (publisher abstract and bibliography consulted).

[3] M. Anastos and A. Frieze, *On the connectivity threshold for colorings of random graphs and hypergraphs*, arXiv:1803.05246 (2018), full preprint consulted: https://arxiv.org/pdf/1803.05246.

[4] M. Anastos and A. Frieze, *On the connectivity of proper colorings of random graphs and hypergraphs*, Random Structures & Algorithms **56** (2020), 988–997, DOI: 10.1002/rsa.20912.

[5] M. A. Henning and A. Yeo, *On 2-Colorings of Hypergraphs*, J. Graph Theory **80** (2015), 112–135, first online 2014-12-10, DOI: 10.1002/jgt.21843.
