# Exact strong-majority edge-colouring palette polynomial of friendship graphs

## Finding

Let \(F_n=K_1\vee(nK_2)\) be the labelled friendship graph formed by \(n\ge1\) triangles sharing exactly one central vertex. A strong-majority edge colouring with the named palette \([q]=\{1,\ldots,q\}\) assigns a colour to every edge such that for every edge and every colour, no more than half its adjacent edges have that colour. The map need not use every available colour.

For integers \(n\ge1\) and \(q\ge2\), let \(P_n(q)\) count such maps. Define
\[
\begin{aligned}
A_0(n,q)&=[q(q-1)]^n-q[2(q-1)]^n+\binom q2 2^n,\\
A_1(n,q)&=q[2(q-1)]^n-q(q-1)2^n,\\
A_2(n,q)&=\binom q2 2^n.
\end{aligned}
\]
Then the exact labelled-palette enumerator is
\[
\boxed{P_n(q)=q^n A_0(n,q)+(q-1)^n A_1(n,q)+(q-2)^n A_2(n,q).}
\]
Here \(A_k(n,q)\) counts the oriented spoke colourings in which exactly \(k\) colours occur on a spoke in **every** triangle; always \(k\in\{0,1,2\}\). In particular,
\[
P_n(2)=0,\qquad P_n(3)=18^n-3\cdot12^n+3\cdot8^n+3\cdot6^n-6\cdot4^n+3\cdot2^n.
\]
There is a valid three-colour assignment for every \(n\ge1\), so the strong-majority index of \(F_n\) is \(3\). This index consequence is **not** asserted to be a new discovery: it already follows from the Eulerian, edge-count-divisible-by-three case of [1, Proposition 21]. The claimed contribution is the full named-palette count and its structural characterization, not the minimum index.

## Assumptions and scope

All graphs are finite, simple, undirected, and vertex-labelled. The hub is distinguished by its role (for \(n=1\), fix a chosen hub of the triangle). For each triangle \(i\in\{1,\ldots,n\}\), denote its two distinguishable hub-to-leaf spoke edges by \(s_i,t_i\) and its leaf-to-leaf base edge by \(b_i\). The palette has exactly \(q\) named options; unused colours are permitted. Adjacent edges are distinct edges sharing an endpoint; the edge itself is never counted as its own neighbour. Statements hold for all integers \(n\ge1\) and \(q\ge2\); the trivial \(q=1\) case has no colouring, since each base edge has two neighbours.

## Proof

Write \(a_i,b_i\) for the colours on the two spokes in triangle \(i\) and \(c_i\) for its base. For a palette colour \(\alpha\), let \(S_\alpha\) be the number of spoke edges of colour \(\alpha\) among all \(2n\) spokes.

**Local characterization.** A base edge has exactly two adjacent edges: its own triangle's spokes. The strong-majority condition at that base edge is therefore equivalent to \(a_i\ne b_i\). Under this requirement each colour occurs on at most one spoke of each triangle, so \(S_\alpha\le n\). A spoke has exactly \(2n\) adjacent edges: the other \(2n-1\) spokes at the hub and its own triangle's base edge. For any spoke of colour \(\beta\), the number of adjacent edges of colour \(\alpha\) is
\[
S_\alpha-\mathbf1_{\{\alpha=\beta\}}+\mathbf1_{\{\alpha=c_i\}}.
\]
If \(S_\alpha<n\), this count is at most \(n\), even when the base is \(\alpha\). If \(S_\alpha=n\) and the base of triangle \(i\) is coloured \(\alpha\), then the triangle has one spoke coloured \(\alpha\) and its other spoke is of another colour. That other spoke sees \(n+1\) adjacent edges coloured \(\alpha\), violating the required bound \(n\). Conversely, if no base uses a colour satisfying \(S_\alpha=n\), every displayed adjacency count is at most \(n\), and the base constraints hold. Thus a complete colouring is strong-majority **if and only if** its two spokes differ in every triangle and no base receives a spoke colour common to all triangles.

**Classification of universal spoke colours.** There are \([q(q-1)]^n\) unrestricted choices of the ordered, distinct spoke-colour pair in each triangle. For a fixed colour \(\alpha\), the number of such choices using \(\alpha\) in every triangle is \([2(q-1)]^n\). For a fixed pair of distinct colours \(\alpha,\beta\), requiring both to occur in every triangle leaves exactly \(2^n\) assignments, as every spoke pair must equal \((\alpha,\beta)\) in some order. Three globally common colours are impossible because each triangle has only two spokes. Inclusion-exclusion therefore gives precisely the three expressions \(A_0,A_1,A_2\) in the finding.

For a spoke assignment with exactly \(k\) universal colours, each of the \(n\) base edges may independently receive any of the remaining \(q-k\) colours, giving \((q-k)^n\) extensions. The three classes are disjoint and exhaustive. Summing yields the boxed formula with no overcounting.

**Minimum palette.** Two named colours cannot work: the two differently coloured spokes in every triangle force both colours to be universal, leaving zero choices for a base. For three colours, choose the same two spoke colours in each triangle, and use the third colour for every base; this is valid by the characterization. Hence the minimum number of colours is three. Substitution \(q=3\) in the count gives the six-exponential expression. For example \(P_1(3)=6\), \(P_2(3)=108\), \(P_3(3)=2472\), and \(P_4(3)=57456\).

## Verification

The standalone script `verification/verify_friendship.py` constructs edge adjacency directly from the graph, checks the original condition for every edge and every named colour, independently checks the structural characterization, and compares both enumerations to the closed formula. Exact enumeration of 834,518 labelled assignments across twelve cases with \(2\le q\le5\) and \(1\le n\le4\) produced full agreement. The actual output is `verification/output.txt`; execute `python3 verification/verify_friendship.py` to reproduce it. These finite enumerations corroborate but do not prove the formula for arbitrary \(n,q\); that proof is the preceding counting argument.

## Relationship to prior work

Kalinowski, Kamyczura, Pilśniak, and Woźniak [1, Section 3] define strong-majority edge colourings and prove general existence bounds. In particular [1, Proposition 21] already implies the index-three consequence for each friendship graph because all degrees are even and there are \(3n\) edges. Antoniuk, Prorok, and Salia [2] improve the general upper bound. Pękała and Przybyło [3] prove stronger degree-dependent bounds and consider other graph families. The accessible primary texts [1]–[3] were inspected for formulas for friendship graphs, triangle windmills, and full palette counts; no such result was located. Prior studies of strong majority **vertex** colourings on line graphs have a related formalism, but the search located no formula dominating this particular count.

## Limitations

This result counts named-colour edge maps, not orbits under palette or graph automorphisms and not only surjective colourings. It concerns the shared-vertex triangle construction, not windmills of larger cliques. The index-three observation is prior-implied rather than a novelty claim. Absolute bibliographic priority and independent mathematical validation remain open; unindexed equivalent formulations or later revisions could contain overlapping enumerations.

## References

[1] R. Kalinowski, M. Kamyczura, M. Pilśniak, M. Woźniak, *Strong majority colorings of graphs*, arXiv:2605.23828v1, first publicly available 22 May 2026; Section 3 and Proposition 21. https://arxiv.org/html/2605.23828v1

[2] S. Antoniuk, M. Prorok, N. Salia, *Strong Majority Edge-Coloring*, arXiv:2607.00212, first posted 30 June 2026. https://arxiv.org/abs/2607.00212

[3] P. Pękała, J. Przybyło, *On Strong Majority Edge Colourings with Few Colours*, arXiv:2608.04122, first posted 4 August 2026. https://arxiv.org/abs/2608.04122
