# Complete star-edge-colouring partition polynomial of \(K_{2,n}\)

## Finding

For every integer \(n\ge 1\), let \(K_{2,n}\) have distinguished degree-\(n\) vertices \(a,b\), and \(n\) labelled degree-two vertices \(v_1,\ldots,v_n\). A **star edge-colouring** is a proper edge-colouring in which no four-edge simple path and no four-edge cycle uses only two colours. A colour partition identifies colourings that differ only by permutations of colour names. Let \(s_{n,r}\) count star edge-colouring partitions having exactly \(r\) nonempty classes. Then

\[
s_{n,r}=\begin{cases}
\displaystyle\frac{n!}{(2n-r)!\,(2r-3n)!},&\lceil 3n/2\rceil\le r\le 2n,\\[4pt]
0,&\text{otherwise}.
\end{cases}
\]

Equivalently, for \(q\) prescribed, individually distinguishable available colours, allowing some colours to be unused, the number of star edge-colourings is the polynomial

\[
\operatorname{SEC}_n(q)=\sum_{k=0}^{\lfloor n/2\rfloor}\frac{n!}{k!(n-2k)!}(q)_{2n-k},\qquad
(q)_r=\prod_{j=0}^{r-1}(q-j).
\]

The full partition-count polynomial and its exponential generating function are

\[
S_n(z)=\sum_{k=0}^{\lfloor n/2\rfloor}\frac{n!}{k!(n-2k)!}z^{2n-k},
\qquad
\sum_{n\ge0}S_n(z)\frac{t^n}{n!}=\exp(z^2t+z^3t^2),
\]

where \(S_0(z)=1\) is an auxiliary empty-instance convention. The partition coefficients, read by increasing number of colours, are strictly log-concave whenever there are at least three nonzero terms. In particular, the number of colour partitions using the minimum possible number
\(r_*=2n-\lfloor n/2\rfloor\) of colours is

\[
\frac{n!}{\lfloor n/2\rfloor!\,(n-2\lfloor n/2\rfloor)!}.
\]

There are exactly \(r_*!\) times as many optimal edge-colourings with a prescribed palette of \(r_*\) named colours.

## Assumptions and scope

Graphs are simple and finite. Each edge \(av_i\) and \(bv_i\) is a distinct, labelled position, and \(a\) and \(b\) remain distinguished. Properness requires distinct colours on the edges incident with each of \(a\), \(b\), and \(v_i\). Four-edge paths have five distinct vertices; cycles of length four have four distinct vertices. The reported polynomial counts functions from the edge set to the named colour palette, rather than quotienting by graph automorphisms. A partition into exactly \(r\) colour classes is counted only once under colour renaming.

## Proof

Write \(x_i\) for the colour on \(av_i\), and \(y_i\) for the colour on \(bv_i\). Properness is equivalent to: the \(x_i\) are pairwise distinct, the \(y_i\) are pairwise distinct, and \(x_i\neq y_i\) for all \(i\). Consequently, any colour can appear on at most two edges. If it appears twice, it appears as \(x_i=y_j\) with \(i\neq j\), giving an oriented link from column \(i\) to column \(j\).

**Matching lemma.** A proper edge-colouring is a star edge-colouring if and only if the unoriented links defined by its repeated colours form a matching on the set of \(n\) columns. Indeed, two different links cannot have the same source (there is only one \(x_i\)) or the same target (there is only one \(y_i\)). If two links share a column, one must end there and the other begin there. If their other endpoints coincide, they are a directed two-cycle: precisely the two-coloured cycle \(a v_i b v_j a\) for the corresponding columns. If the other endpoints differ, the repeated colours provide a two-coloured four-edge path \(v_p a v_i b v_q\), or its reversal, with distinct \(p,i,q\). Thus a star colouring has vertex-disjoint links. Conversely, a two-coloured four-edge cycle gives two oppositely directed links between its two columns. Any two-coloured four-edge path necessarily has the form \(v_p a v_i b v_q\) or its reverse, with three distinct columns, and its alternating colours give two links meeting at the middle column. Hence every forbidden path or cycle is excluded exactly when the links form a matching.

If this matching has \(k\) links, choose the \(k\) unordered pairs of columns in \(n!/(2^k k!(n-2k)!)\) ways. Orient each linked pair independently in \(2^k\) ways, specifying which of the two columns has the \(a\)-side edge that shares a colour with the other column's \(b\)-side edge. A linked pair uses three distinct colour classes on its four edges. Each unmatched column uses two private colour classes. Colour classes belonging to different components must be distinct, for otherwise the repeated-colour links would extend beyond the chosen matching. Therefore exactly \(2n-k\) colour classes occur. Since all edge positions are distinguishable, assigning \(2n-k\) distinct named colours to the uniquely identified component roles has exactly \((q)_{2n-k}\) possibilities. Multiplication gives the displayed sum. Replacing the named palette by unlabeled colour classes sets the last factor equal to one and proves the coefficient formula.

Choosing unlinked single columns of weight \(z^2\) and linked pairs of weight \(2z^3\) gives the labelled exponential formula \(\exp(z^2t+z^3t^2)\). The minimum number of colours occurs when \(k=\lfloor n/2\rfloor\); every permissible value of \(k\) occurs. Finally, the coefficients indexed by \(k\), \(c_k=n!/(k!(n-2k)!)\), satisfy

\[
\frac{c_{k+1}}{c_k}=\frac{(n-2k)(n-2k-1)}{k+1},
\]

which strictly decreases wherever two successive quotients exist. Reversing the coefficient order does not change log-concavity. This proves the claimed strict log-concavity on the positive support and completes the proof.

## Verification

A standalone standard-library verifier, `verify.py`, independently enumerates all proper colour partitions in canonical restricted-growth form, generates every simple four-edge path and four-cycle from the graph adjacency, and rejects those with alternating equal colours. It compares exact integer counts for every nonempty number of colour classes at orders \(2\le n\le7\) against the formulas. It evaluates the finite arithmetic identities for \(1\le n\le100\). The recorded run is in `verification_output.txt` and ends with:

`VERIFICATION_OK direct_orders=2..7 canonical_candidates=71350 arithmetic_orders=1..100`

The finite checks do not constitute a proof for all orders; the matching lemma and the counting argument do.

## Relationship to prior work

Casselgren, Granholm and Raspaud proved that \(\chi'_{st}(K_{2,n})=2n-\lfloor n/2\rfloor\), thereby establishing the minimum number of colours (Proposition 2.1 in arXiv:1912.02467). That minimum is not new here. The present result classifies *every* valid colour partition and gives its exact multiplicity at every size, including all optimal colourings. The 2020 survey by Lei and Shi reproduces the scalar star chromatic index (Theorem 4.2(a)) but not a complete partition-count polynomial. Wang and Lu (2024) study an algorithm for deciding star edge-colourability under bounded treewidth and maximum degree; its cited algorithm does not itself provide the displayed closed counting formulas for these complete bipartite graphs. The equivalent statement about star vertex-colourings of the line graph \(L(K_{2,n})\cong K_2\square K_n\) must be included in priority searches.

## Limitations

The theorem is specialized to the two-vertex side of a complete bipartite graph. It supplies no general formula for \(K_{m,n}\) when \(m\ge3\), nor any claim about colour-list constraints or unlabelled graph-isomorphism classes. The scalar minimum is established prior work. Although relevant source texts and equivalence-based searches were checked, additional equivalent enumerations in unindexed literature cannot be excluded; there has been no independent external review.

## References

1. C. J. Casselgren, J. B. Granholm, and A. Raspaud, *On star edge colorings of bipartite and subcubic graphs*, arXiv:1912.02467v1, first posted 2019-12-05, Proposition 2.1. https://arxiv.org/abs/1912.02467
2. H. Lei and Y. Shi, *A survey on star edge-coloring of graphs*, arXiv:2009.08017v1, first posted 2020-09-17, Theorem 4.2. https://arxiv.org/html/2009.08017v1
3. Y. Wang and M. Lu, *A polynomial time algorithm to find star chromatic index on bounded treewidth graphs with given maximum degree*, arXiv:2402.04526v1, first posted 2024-02-07, Theorem 3.1. https://arxiv.org/abs/2402.04526
