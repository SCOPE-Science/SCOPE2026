# Proper conflict-free colorings of friendship graphs

## Finding

For an integer \(k\ge1\), let
\[
F_k=K_1\vee kK_2
\]
be the friendship graph formed by \(k\) triangles having a common center \(z\). Write the remaining \(2k\) vertices as pairs
\[
a_i,b_i\qquad(1\le i\le k),
\]
where \(a_ib_i\) is an edge.

A proper coloring of \(F_k\) is proper conflict-free if and only if at least one color occurs exactly once among the \(2k\) leaves
\[
\{a_1,b_1,\ldots,a_k,b_k\}.
\]

Therefore
\[
\boxed{
\chi_{\mathrm{pcf}}(F_k)=
\begin{cases}
3,&k=1,\\
4,&k\ge2.
\end{cases}}
\]

The complete color-count spectrum is
\[
\boxed{
\{3\}\quad\text{for }k=1,
\qquad
\{4,5,\ldots,2k+1\}\quad\text{for }k\ge2.
}
\]

There is also a closed count for minimum-color solutions. Let \(M_k\) be the number of surjective proper conflict-free colorings onto a fixed labeled palette of
\[
\chi_{\mathrm{pcf}}(F_k)
\]
colors. Then
\[
\boxed{
M_1=6,\qquad M_2=96,\qquad
M_k=24k\,2^k\quad(k\ge3).
}
\]

## Assumptions and scope

All graphs are finite, simple, and undirected. A proper conflict-free coloring is a proper vertex coloring in which every non-isolated vertex has a color occurring exactly once in its open neighborhood.

The friendship graph \(F_k\) has one center and \(k\) disjoint leaf edges, with the center adjacent to every leaf. The count \(M_k\) treats colors as labeled and requires every color in the minimum palette to be used.

The theorem concerns ordinary proper conflict-free coloring, not list coloring or proper \(h\)-conflict-free coloring for \(h>1\).

## Proof

Let \(\varphi\) be a proper coloring of \(F_k\).

Because the center \(z\) is adjacent to every leaf, its color cannot occur on any leaf. On each leaf edge \(a_ib_i\), properness gives
\[
\varphi(a_i)\ne\varphi(b_i).
\]

Consider a leaf \(a_i\). Its open neighborhood is
\[
N(a_i)=\{z,b_i\}.
\]
The two vertices in this neighborhood have distinct colors, because the center color is absent from all leaves. Hence each of those two colors occurs exactly once in \(N(a_i)\). The same argument applies to every \(b_i\). Thus every leaf automatically satisfies the conflict-free condition in every proper coloring.

The center has open neighborhood consisting of all \(2k\) leaves. It has a conflict-free witness precisely when some leaf color occurs exactly once among those leaves. This proves the structural characterization.

For \(k=1\), the graph is a triangle, so properness already requires three colors, and the two leaves have distinct colors. Hence
\[
\chi_{\mathrm{pcf}}(F_1)=3.
\]

Now let \(k\ge2\). The center requires a color not used on the leaves. If the leaves used only two colors, then every edge \(a_ib_i\) would use both of them. Each of the two colors would therefore occur exactly \(k\) times among the leaves, so neither would be a singleton. Thus at least three leaf colors are required, and
\[
\chi_{\mathrm{pcf}}(F_k)\ge4.
\]

Three leaf colors suffice. Color one leaf edge with colors \(1\) and \(3\), and every remaining leaf edge with colors \(1\) and \(2\). Color the center with a fourth color. Color \(3\) occurs exactly once among the leaves, so this is proper conflict-free. Hence
\[
\chi_{\mathrm{pcf}}(F_k)=4
\]
for every \(k\ge2\).

For the color-count spectrum, the preceding construction uses exactly three leaf colors. Whenever fewer than \(2k\) leaf colors are currently used, some leaf color is repeated. Recolor one occurrence of such a repeated color with a fresh color. This preserves properness because the new color is fresh, and it preserves a singleton witness because either an existing singleton remains or the new color itself is a singleton. Repeating this operation realizes every number of leaf colors from \(3\) through \(2k\). Adding the center's distinct color gives every total from \(4\) through \(2k+1\).

It remains to count the minimum colorings. For \(k=1\), \(F_1=K_3\), so a fixed labeled three-color palette gives
\[
M_1=3!=6.
\]

Let \(k\ge2\) and use a fixed labeled four-color palette. The center color can be chosen in \(4\) ways. The leaves then use the remaining three colors. For a specified leaf color \(c\), count proper leaf colorings in which \(c\) occurs exactly once. Choose the unique vertex carrying \(c\) in
\[
2k
\]
ways. Its mate has two choices among the other two colors. Each of the remaining \(k-1\) leaf edges must use the two other colors in one of the two possible orders. Hence the number is
\[
2k\,2^k.
\]

There are three choices for the specified singleton color. For \(k\ge3\), two distinct leaf colors cannot both be singleton: if they were, after removing their two vertices at least one whole leaf edge would remain, and every remaining vertex would have to receive the third color, contradicting properness on that edge. Thus the three singleton events are disjoint for \(k\ge3\), and the number of good leaf colorings is
\[
3(2k\,2^k)=6k\,2^k.
\]
Multiplying by the \(4\) center-color choices gives
\[
M_k=24k\,2^k
\qquad(k\ge3).
\]

For \(k=2\), a pair of specified colors can both be singleton. For each fixed pair, the two singleton vertices must lie on different leaf edges; there are
\[
4\cdot2=8
\]
ordered placements. There are three pairs of colors. Inclusion-exclusion therefore gives
\[
3(4\cdot2^2)-3(8)=48-24=24
\]
good leaf colorings, and hence
\[
M_2=4\cdot24=96.
\]
This completes the proof.

## Verification

The accompanying script `artifacts/verify.py` constructs \(F_k\) directly and evaluates properness and the open-neighborhood conflict-free condition from adjacency.

It exhaustively checks all proper colorings of \(F_1,F_2,F_3\) for every palette size up to the number of vertices, comparing the direct definition with the singleton-leaf characterization and confirming the full used-color spectrum.

It separately checks the explicit spectrum construction for every \(2\le k\le20\) and every feasible used-color count. Finally, it enumerates all proper three-colorings of the leaf matching for \(2\le k\le8\) and verifies the closed minimum-color count.

Replay output:

`ALL CHECKS PASSED; proper_colorings_checked=247410; pcf_colorings_checked=234798; spectrum_constructions=380; minimum_count_formula_k=2..8; minimum_counts={2: 96, 3: 576, 4: 1536, 5: 3840, 6: 9216, 7: 21504, 8: 49152}`

The finite checks are corroborative. The statements for arbitrary \(k\) follow from the analytic proof above.

## Relationship to prior work

Qi, Song, and Cao study proper conflict-free choosability in sparse graphs. Their first public version appeared on September 10, 2026, and lists primary MSC \(05C15\). Their main theorem concerns degree-dependent lists under girth and maximum-average-degree hypotheses, rather than exact colorings of friendship graphs.

Caro, Petruševski, and Škrekovski established exact values for several basic classes, including trees, cycles, hypercubes, and subdivisions of complete graphs, and developed general upper bounds. Their published scope does not identify friendship graphs as an exact family.

Sharma, Paul, and Pandey give 2026 upper bounds for broad perfect-graph subclasses including \(P_4\)-sparse graphs. Friendship graphs are cographs and hence \(P_4\)-sparse, so those class bounds are relevant stronger upper-bound prior art. However, the accessible abstract states class-wide ratio and upper-bound results, not a characterization of every proper conflict-free coloring, the complete used-color spectrum, or the labeled minimum-color count. The full conference paper was not available through the inspected open route, so a family-specific scalar statement inside it remains a residual literature risk.

Targeted searches using both “friendship graph” and “windmill graph” terminology found no source stating the singleton-leaf characterization, the exact spectrum, or the minimum-color count above.

## Limitations

The theorem is specific to the friendship family
\[
K_1\vee kK_2.
\]
The same center-witness idea extends to some generalized windmills, but no such broader claim is made here.

The originality assessment is literature-based rather than a proof of global uniqueness. In particular, the inaccessible full text of the 2026 \(P_4\)-sparse upper-bound paper could contain a friendship-graph example; that would not by itself imply the all-coloring characterization, spectrum, or labeled enumeration proved here.

The enumeration \(M_k\) counts minimum colorings with labeled colors. Quotienting by graph automorphisms or color permutations is a different enumeration problem.

## References

1. X. Qi, H. Song, and Z. Cao, “Proper conflict-free choosability of sparse graphs with girth at least seven,” arXiv:2609.11249v1, first public September 10, 2026, MSC \(05C15\).
2. Y. Caro, M. Petruševski, and R. Škrekovski, “Remarks on proper conflict-free colorings of graphs,” arXiv:2203.01088v1; Discrete Mathematics 346 (2023), 113221.
3. A. Sharma, K. Paul, and A. Pandey, “Improved Bounds on Proper Conflict-Free Coloring of Graphs,” Combinatorial Algorithms, LNCS 16587 (2026), 500–514, DOI 10.1007/978-3-032-27732-9_35.
4. D. W. Cranston and C.-H. Liu, “Proper Conflict-Free Coloring of Graphs with Large Maximum Degree,” SIAM Journal on Discrete Mathematics 38 (2024), 3004–3027, DOI 10.1137/23M1563281.
