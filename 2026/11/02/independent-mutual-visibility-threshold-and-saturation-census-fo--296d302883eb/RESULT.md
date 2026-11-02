# Independent mutual-visibility threshold and saturation census for \(P_L\square K_m\)

## Finding

Let \(G_{L,m}=P_L\square K_m\), where \(L,m\ge2\) are integers. A vertex set \(S\) is an **independent mutual-visibility set** if it is independent and, for every two distinct members, there exists a shortest path between them whose internal vertices avoid \(S\). Write \(\mu_i(G)\) for the maximum cardinality of such a set. Then

\[
\boxed{\mu_i(G_{L,m})=\min\{L,2m\}-\mathbf{1}_{\{L=2m\}}.}
\]

In particular, the only path length at which the natural bounds \(\mu_i(G_{L,m})\le\min\{L,2m\}\) fail to be attained is \(L=2m\), and the deficit there is exactly one.

**Complete saturated-extremizer classification.** Sets of size \(2m\) exist if and only if \(L\ge2m+1\). Every such set is obtained, uniquely, by choosing path positions
\[
1\le p_1<\cdots<p_m<p_{m+1}<\cdots<p_{2m}\le L,
\qquad p_{m+1}\ge p_m+2,
\]
and independently assigning a permutation of the \(m\) clique colors to the first \(m\) positions and another permutation of all \(m\) colors to the last \(m\) positions. Consequently their exact labeled count is
\[
\boxed{N_{2m}(L,m)=(m!)^2\binom{L-1}{2m}\qquad(L\ge2m+1).}
\]
Here \(\mathbf{1}_{\{L=2m\}}\) is one when \(L=2m\) and zero otherwise.

## Assumptions and scope

The graph has vertices \((i,c)\) with path coordinate \(i\in\{1,\ldots,L\}\) and clique color \(c\in\{1,\ldots,m\}\). Distinct vertices are adjacent exactly if their path coordinates agree, or if their clique colors agree and their path coordinates differ by one. For vertices \((i,a),(j,b)\),
\[
d_G((i,a),(j,b))=|i-j|+\mathbf 1_{\{a\ne b\}}.
\]
Whenever \(i<j\) and \(a\ne b\), every geodesic moves monotonically from layer \(i\) to layer \(j\) and changes clique color exactly once, at some layer in \(\{i,\ldots,j\}\).

The theorem concerns *independent* mutual-visibility sets, not ordinary, total, outer, dual, or connected mutual-visibility sets. Colors and path positions are labeled. The extremizer count covers only sets that meet the saturation bound \(2m\); it does not claim the number of maximum sets when \(L\le2m\).

## Proof

**Step 1: Two elementary upper bounds.** Each path layer induces a clique, so independence allows at most one member of \(S\) in each layer. Hence \(|S|\le L\). For each fixed clique color, its vertices induce a convex copy of \(P_L\); three selected vertices of that color would place the middle one on the unique shortest path between the outer two. Hence any mutual-visibility set has at most two members per color, and \(|S|\le2m\).

**Step 2: A forbidden disjoint-interval pattern.** Suppose \(|S|=2m\). Every color \(c\) then appears exactly twice, at path coordinates \(f_c<s_c\). If two colors \(a,b\) satisfied \(f_a<s_a<f_b<s_b\), consider the selected endpoints \((f_a,a)\) and \((s_b,b)\). On every geodesic between them the color changes from \(a\) to \(b\) exactly once. Changing before reaching layer \(s_a\) passes through the selected vertex \((f_b,b)\), and changing at or after layer \(s_a\) passes through \((s_a,a)\). Thus no such geodesic is clear. Interchanging colors gives the same conclusion for the reverse ordering. Therefore the open intervals \((f_c,s_c)\) for all colors are pairwise intersecting.

Open intervals on a line have the Helly property. Hence
\[
\max_c f_c<\min_c s_c.
\]
In the ordered list \(p_1<\cdots<p_{2m}\) of occupied path layers, the first \(m\) positions are therefore exactly the first occurrences of all colors, and the last \(m\) positions their second occurrences. Both blocks use each color once.

**Step 3: A mandatory unoccupied separator.** Suppose \(p_{m+1}=p_m+1\). Let \(a\) be the color at \(p_m\) and \(b\) the color at \(p_{m+1}\). If \(a=b\), these selected vertices are adjacent, contradicting independence. Otherwise take the first occurrence of \(b\) (before \(p_m\)) and the second occurrence of \(a\) (after \(p_{m+1}\)). On any geodesic joining them, a single switch from color \(b\) to color \(a\) is needed. To avoid the selected color-\(a\) vertex at \(p_m\), the switch must occur strictly later than \(p_m\); to avoid the selected color-\(b\) vertex at \(p_{m+1}\), it must occur strictly earlier than \(p_{m+1}\). No such layer exists. This contradiction proves \(p_{m+1}\ge p_m+2\), and in particular a size-\(2m\) set requires \(L\ge2m+1\).

**Step 4: Sufficiency of the two-permutation construction.** Conversely choose \(2m\) occupied positions separated between the two \(m\)-element blocks by at least one empty layer, and place one full permutation of the colors in each block. Independence holds: there is at most one choice per layer, adjacent occupied layers within a block have different colors, and the two blocks are separated by an empty layer.

Two vertices of the same color are visible along the unique monotone path within that color, because no third member has that color. Two vertices of different colors within one block are visible along a geodesic that switches color immediately at the earlier endpoint layer; the destination color does not occur anywhere else between the endpoints. For two different colors in opposite blocks, follow the first color to an empty separating layer, switch there, and then follow the second color to the endpoint. The first color occurs only once in the first block, and the second only once in the second block, so this geodesic has no selected internal vertex. The same-color cross-block case was already covered. Thus every described set is independent and mutually visible.

**Step 5: Saturated-set counting.** Given a sequence \(p_1<\cdots<p_{2m}\) with \(p_{m+1}\ge p_m+2\), define \(q_j=p_j\) for \(j\le m\) and \(q_j=p_j-1\) for \(j>m\). This gives an arbitrary \(2m\)-element subset of \(\{1,\ldots,L-1\}\). The inverse increases the last \(m\) positions by one; hence the positions have exactly \(\binom{L-1}{2m}\) possibilities. Each block carries an arbitrary permutation of \(m\) colors, independently. This yields \((m!)^2\binom{L-1}{2m}\) distinct labeled sets, and Steps 2--4 prove exhaustiveness and uniqueness.

**Step 6: Attainability of every remaining maximum.** For a path of \(2m-1\) layers, take the selected color word
\[
1,2,\ldots,m,1,2,\ldots,m-1.
\]
It is independent: consecutive entries differ, including across the two blocks because \(m\ge2\). Every color occurs at most twice. Two selected vertices of the same color have a clear unique vertical geodesic. For distinct colors in the same block, switch immediately to the endpoint's color; it does not occur again inside that block. For a pair in opposite blocks, use layer \(m\) as the color-switching layer. Before that layer the first selected color occurs only once, and after it the second selected color occurs only at the endpoint; the switched-to color is not the selected color \(m\) of the switch layer. Thus the word is a valid independent mutual-visibility set of size \(2m-1\).

Taking its first \(L\) layers when \(2\le L\le2m-1\) gives a valid set of size \(L\), since shorter prefix products are convex in the larger graph. If \(L=2m\), use all \(2m-1\) vertices of the word and leave the final layer empty. If \(L\ge2m+1\), Step 4 supplies a set of size \(2m\). The upper bounds from Step 1 and the strict obstruction at \(L=2m\) from Step 3 complete the scalar formula. \(\square\)

## Verification

A standalone C++17 verifier in `verify_independent_mv.cpp` enumerates candidate sets with at most one vertex per path layer, excludes immediately impossible instances with more than two occurrences of a color, and checks each remaining candidate by breadth-first search in the graph with all other selected vertices removed. It accepts a selected pair only when the resulting distance is equal to the original Cartesian-product distance, hence checks the original geodesic definition rather than the two-permutation characterization. It tests every candidate with cardinality at least the asserted optimum for \(m=2,3,4\) and \(2\le L\le2m+3\), comparing both the maximum size and the exact saturated count in the applicable range. Run the verifier with `c++ -O3 -std=c++17 verify_independent_mv.cpp -o verify_independent_mv && ./verify_independent_mv`; the included `verifier_output.txt` gives the observed counts and `VERIFY_OK`.

These are exhaustive **finite checks in the stated parameter ranges only**. The proof above, not the computation, establishes the assertions for all \(L,m\ge2\).

## Relationship to prior work

Cicerone, Di Stefano, and Klavžar (arXiv:2112.13024, first public 2021-12-24) introduce independent mutual visibility and give general Cartesian-product bounds and equality results for a different hypothesis. Their bounds imply the generic \(2m\) ceiling but do not identify the single excluded length, classify saturated sets, or count their configurations.

Korže and Vesel (2024) compute ordinary mutual visibility for products of paths and cycles, including \(P_2\square C_3\cong P_2\square K_3\), but ordinary mutual visibility is not the independent invariant. Brešar, Peterin, Samadi, and Yero (2025 preprint, 2026 publication) study independent mutual-visibility **colorings**, lexicographic products, and Cartesian-product coloring bounds; these do not determine the independent mutual-visibility maximum of a path--clique product. Tian, Bujtás, and Klavžar (2026) study general independent-visibility criteria and complexity, rather than the present two-parameter classification.

The claimed contribution is the exact independent mutual-visibility number for every \(L,m\ge2\), its isolated saturation defect, and the complete enumerated extremizer family when \(L\ge2m+1\). It does not claim that the basic invariant or general Cartesian-product upper bound is new.

## Limitations

The proof applies only to Cartesian products of a path and a clique. It gives no formula for maximum-set multiplicities at shorter path lengths, nor for products with cycles or arbitrary fibers. Finite enumeration is a check, not an infinite certificate. Available literature and mathematical-record searches are not a guarantee of publication priority; equivalent earlier results under different terminology may exist. No independent mathematical audit has been performed.

## References

1. S. Cicerone, G. Di Stefano, S. Klavžar, *On the mutual visibility in Cartesian products and triangle-free graphs*, arXiv:2112.13024 (first public 2021-12-24). https://arxiv.org/abs/2112.13024
2. D. Korže, A. Vesel, *Mutual-Visibility Sets in Cartesian Products of Paths and Cycles*, Results in Mathematics 79 (2024), article 116. https://doi.org/10.1007/s00025-024-02139-x
3. B. Brešar, I. Peterin, B. Samadi, I. G. Yero, *Independent mutual-visibility coloring and related concepts*, arXiv:2505.04144; Aequationes mathematicae 100 (2026), article 48. https://arxiv.org/abs/2505.04144
4. J. Tian, C. Bujtás, S. Klavžar, *Independent mutual-visibility sets and distance edge-critical graphs*, arXiv:2602.23403 (2026). https://arxiv.org/abs/2602.23403
