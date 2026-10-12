# Exact equitable DP-colorability spectrum of stars
## Finding
For every integer \(n\ge2\) and every integer \(k\ge1\), let \(S_n=K_{1,n-1}\) and put \(m=\lceil n/k\rceil\). Then \(S_n\) is equitably DP \(k\)-colorable if and only if
\[
(k-1)\left\lceil\frac{n}{k}\right\rceil\ge n.
\]
Thus the entire equitable-DP palette spectrum of a star is arithmetic rather than monotone. For example, \(S_9\) is equitably DP \(4\)-colorable, is not equitably DP \(5\)-colorable, is equitably DP \(6\)-, \(7\)-, and \(8\)-colorable, is not equitably DP \(9\)-colorable, and is equitably DP \(k\)-colorable for every \(k\ge10\).

## Assumptions and scope
A \(k\)-cover assigns to every graph vertex a set of exactly \(k\) colors and to every graph edge a matching between the two endpoint color sets. An \(H\)-coloring selects one color at every graph vertex while avoiding all matched endpoint pairs. For an \(n\)-vertex graph and a fixed \(k\), write \(m=\lceil n/k\rceil\). An \(H\)-coloring is \(m\)-bounded when no global color label is used more than \(m\) times. A graph is equitably DP \(k\)-colorable when every \(k\)-cover admits an \(m\)-bounded \(H\)-coloring. These are the definitions of Kierstead, Kostochka, and Xiang.

The theorem concerns all finite stars with at least one edge and every positive integer \(k\). It does not concern the stronger SEDP condition, which additionally controls the number of large color classes.

## Proof
Let \(r\) be the center of \(S_n\), and let \(X\) be its \(n-1\) leaves.

Assume first that
\[
m(k-1)\ge n.
\]
Fix an arbitrary \(k\)-cover \(H\), and choose any color \(\alpha\in H(r)\) for the center. For each leaf \(x\), the selected center node can be matched to at most one node in \(H(x)\). Hence, after fixing \(r\) to \(\alpha\), the available set \(A_x\subseteq H(x)\) has size at least \(k-1\).

Give every global color label capacity \(m\), except that the label \(\alpha\) has residual capacity \(m-1\) because it is already used at the center. Consider any nonempty set \(Y\subseteq X\) of leaves and put \(U_Y=\bigcup_{x\in Y}A_x\). Since each \(A_x\) has at least \(k-1\) elements, \(|U_Y|\ge k-1\). The total residual capacity on \(U_Y\) is therefore at least
\[
m(k-1)-1\ge n-1\ge |Y|.
\]
The capacitated form of Hall's theorem, equivalently Hall's theorem after replacing each color by the appropriate number of clones, now assigns one available color to every leaf without exceeding any residual capacity. Together with the center color \(\alpha\), this is an \(m\)-bounded \(H\)-coloring. Since \(H\) was arbitrary, the star is equitably DP \(k\)-colorable.

Conversely, suppose \(m(k-1)<n\). If \(k=1\), the star has an edge and a full one-color matching on that edge gives no \(H\)-coloring. Now assume \(k\ge2\). Use the common palette \(\mathbb Z_k\) at every vertex, and on every center-leaf edge use the same full matching induced by the cyclic permutation \(\tau(i)=i+1\pmod{k}\). If the center receives \(\alpha\), every leaf is forbidden from receiving \(\tau(\alpha)\), while the center itself has already consumed one unit of the capacity of \(\alpha\). Because \(\tau(\alpha)\ne\alpha\), the total capacity available to all \(n-1\) leaves is at most
\[
(m-1)+m(k-2)=m(k-1)-1<n-1.
\]
Thus this cover has no \(m\)-bounded coloring, so the star is not equitably DP \(k\)-colorable. This proves the equivalence.

## Verification
The proof is analytic and covers all \(n\ge2\) and \(k\ge1\). The supplied checker independently exhausts every plain full correspondence cover for \(2\le n\le4\) and \(1\le k\le4\), solving the bounded-coloring problem by backtracking and confirming that every cover is colorable exactly in the parameter pairs predicted by the theorem. It also checks the Hall-capacity inequality and the cyclic obstruction for every \(2\le n\le200\), \(1\le k\le200\). The replay output is:

`ALL CHECKS PASSED; exhaustive_plain_full_covers=14699; exhaustive_parameter_cases=12; arithmetic_cases=39800; cyclic_bad_cases=3475; star_order_range_exhaustive=2..4; k_range_exhaustive=1..4; arithmetic_n_k_range=2..200,1..200; good_k_for_n9=[4, 6, 7, 8, 10]`

The finite checks are stress tests only; they are not used as an infinite proof.

## Relationship to prior work
Kierstead, Kostochka, and Xiang introduced equitable DP coloring in arXiv:2605.17783v1. Their definition of EDP colorability is the one used here. Their Example 7 shows that stars can fail the stronger SEDP condition for every \(k\le n\). Their Corollary 7 gives an EDP result for forests in the high-color range and isolates a star obstruction at \(k=n\), while Proposition 5 gives strong equitable DP colorability for an \(n\)-vertex \(1\)-degenerate graph when \(k\ge n+1\). Those results do not state the all-\(k\) star spectrum above, including the lower-color arithmetic islands such as \(S_9\) at \(k=4\).

Targeted searches for the exact inequality, for EDP star spectra, for correspondence-coloring aliases, and for equitable-DP chromatic parameters found no statement implying the theorem. Older DP-coloring work concerns correspondence colorability without the global \(m\)-bounded condition, and equitable list-coloring work concerns list assignments rather than arbitrary correspondence covers.

## Limitations
The theorem is specific to stars. The Hall argument uses the fact that after coloring the center the leaves form an independent set and each loses at most one color. It does not directly extend to double stars or general trees. No claim is made here about the stronger SEDP spectrum. The originality search cannot exclude an uncatalogued equivalent statement under different terminology, although the initiating EDP paper and targeted semantic and exact-term searches were checked.

## References
1. H. A. Kierstead, A. Kostochka, and Z. Xiang, *An introduction to equitable DP coloring of graphs*, arXiv:2605.17783v1, first public 2026-05-18. Primary classifications listed in the manuscript: \(05\mathrm C07\), \(05\mathrm C15\), \(05\mathrm C35\). DOI: 10.48550/arXiv.2605.17783.
2. Z. Dvořák and L. Postle, *Correspondence coloring and its application to list-coloring planar graphs without cycles of lengths 4 to 8*, Journal of Combinatorial Theory, Series B 129 (2018), 38–54. This is background for DP/correspondence coloring, not for equitable DP colorability.
