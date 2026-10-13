# Two-radius saturation for packing-total coloring of friendship graphs

## Finding

For an integer \(n\ge 1\), let \(F_n=K_1\vee(nK_2)\) be the friendship graph consisting of \(n\) triangles with one common vertex. For an integer \(q\ge0\), consider the nondecreasing sequence
\[
S^{(q)}=(1,\underbrace{2,\ldots,2}_{q\text{ terms}},3,3,\ldots).
\]
The exact \(S^{(q)}\)-packing total chromatic number is
\[
\boxed{\chi_{S^{(q)}}^{\prime\prime}(F_n)=
\begin{cases}
5,&n=1,\\
4n+1,&n\ge2,\ q=0,\\
3n+2,&n\ge2,\ q=1,\\
3n+1,&n\ge2,\ q\ge2.
\end{cases}}
\]
In particular, allowing one distance-three-reusable color saves \(n-1\) colors, and allowing a second saves exactly one further color. Additional such colors yield no improvement.

## Assumptions and scope

All graphs are finite, simple, and undirected. An \(S\)-packing total coloring assigns a positive integer color to each vertex and edge of \(G\); two distinct elements receiving color \(i\) must have total-element distance strictly greater than \(S_i\). Vertices and edges together form the total graph \(T(G)\): two elements are adjacent when they are adjacent vertices, incident vertex and edge, or incident edges. We use ordinary shortest-path distance in \(T(G)\), equivalently the endpoint formulas stated in the motivating work. The number \(\chi_S^{\prime\prime}(G)\) is the least largest color label in a valid coloring. The theorem assumes exactly the displayed sequence; it makes no claim about other \(S\).

Write \(h\) for the common vertex of \(F_n\), and \(a_i,b_i\) for the other two vertices of triangle \(i\), for \(1\le i\le n\). Write \(s_i=ha_i\), \(t_i=hb_i\), and \(r_i=a_ib_i\) for the three edges of that triangle. The total graph has \(5n+1\) elements. Its diameter is \(2\) when \(n=1\) and \(3\) when \(n\ge2\).

## Proof

**Distance structure.** Every element of \(\{h,s_1,t_1,\ldots,s_n,t_n\}\) is at distance at most \(2\) from every other element. The three elements \(a_i,b_i,r_i\) are mutually adjacent in the total graph. For distinct indices \(i,j\), the total-element distances satisfy
\[
d(r_i,r_j)=3,\qquad d(a_i,r_j)=d(b_i,r_j)=3,
\]
while distinct peripheral vertices in different triangles are at distance \(2\). These statements follow either by explicitly walking through \(h\) or by the endpoint rules
\[
d(v,xy)=1+\min\{d_G(v,x),d_G(v,y)\},
\]
\[
d(xy,uv)=1+\min\{d_G(x,u),d_G(x,v),d_G(y,u),d_G(y,v)\}.
\]
Consequently \(n\ge2\) gives total-graph diameter \(3\).

**Packing bounds.** A distance-greater-than-one set in \(T(F_n)\) meets the clique \(\{h,s_1,t_1,\ldots,s_n,t_n\}\) at most once and each clique \(\{a_i,b_i,r_i\}\) at most once. Therefore its size is at most \(n+1\), attained by \(\{h,r_1,\ldots,r_n\}\). A distance-greater-than-two set containing \(h\) or any spoke is a singleton. Otherwise it contains at most one element from each triangle's triple \(\{a_i,b_i,r_i\}\); hence for \(n\ge2\) its size is at most \(n\), attained by the \(n\) rim edges. For \(n=1\), total-graph diameter \(2\) makes the second bound \(1\).

**Case \(n=1\).** Color \(1\) can occupy at most \(2\) elements, while each other color can occupy only one because the total graph has diameter \(2\). The six elements therefore need at least \(5\) colors. Assign color \(1\) to \(h\) and \(r_1\), and distinct colors \(2,3,4,5\) to the other elements.

Now assume \(n\ge2\). For \(q=0\), every color from \(2\) onward requires mutual distance greater than \(3\), so every such class is a singleton. Since color \(1\) occupies at most \(n+1\) elements, the \(5n+1\) elements need at least \(4n+1\) colors. Equality follows by assigning color \(1\) to \(\{h,r_1,\ldots,r_n\}\) and giving every remaining element its own color.

For \(q=1\), color \(1\) occupies at most \(n+1\) elements, color \(2\) at most \(n\), and every other color occupies at most one. Thus with maximum label \(t\),
\[
5n+1\le(n+1)+n+(t-2),
\]
so \(t\ge3n+2\). Equality holds by giving color \(1\) to
\[
\{s_1,b_1,b_2,\ldots,b_n\},
\]
color \(2\) to \(\{r_1,\ldots,r_n\}\), and pairwise-distinct colors \(3,\ldots,3n+2\) to the remaining elements.

For \(q\ge2\), the set
\[
J=\{h\}\cup\{a_i,b_i,s_i,t_i:1\le i\le n\}
\]
has \(4n+1\) elements and total-element distance at most \(2\) between every pair. At most \(n+1\) of these elements can receive color \(1\); all other elements of \(J\) require mutually distinct color labels greater than \(1\). Consequently every coloring has maximum label at least \(3n+1\).

To attain this bound, assign color \(1\) to \(\{s_1,b_1,\ldots,b_n\}\). Assign color \(2\) to \(\{a_1,r_2,\ldots,r_n\}\) and color \(3\) to \(\{a_2,r_1\}\). Because \(q\ge2\), colors \(2\) and \(3\) both require total-element distances at least \(3\), which the stated sets possess. Give every remaining element a separate color, using \(4,\ldots,3n+1\). This exhausts all \(5n+1\) elements and achieves the lower bound.

Together these cases prove the claimed formula for every \(n\ge1\) and integer \(q\ge0\).

## Verification

The standalone standard-library Python program `verify_friendship.py` independently builds the total graph, computes breadth-first distances, and checks them against direct graph-endpoint distance formulas. It checks the displayed construction for each \(1\le n\le14\) and \(q\in\{0,1,2,3,8\}\). For \(1\le n\le6\), an exact branch-and-bound search verifies the two maximum packing sizes, and it checks the clique structure used in the lower bound. The recorded output `verification_output.txt` ends with `ALL_CHECKS_PASS`. Run with `python3 verify_friendship.py`. These finite tests are sanity checks; universal validity comes from the proof above.

## Relationship to prior work

Ferme, Hedžet, Melicharová and Mesarič Štesl (arXiv:2609.10107, first available September 9, 2026) introduced \(S\)-packing total coloring and report exact studies for complete bipartite graphs, paths and cycles, together with general bounds. The friendship-graph sequence-threshold classification above is a different family and a different exact statement. The preceding paper of Ferme and Mesarič Štesl (arXiv:2508.08691) introduced the original packing-total coloring, whose color radii correspond to a different sequence. No prior theorem is asserted to be disproved or repaired.

The originating preprint's full body could not be accessed for direct theorem-by-theorem inspection; the comparison is to accessible original abstracts and bibliographic descriptions, supplemented by targeted published-record searches. Thus exact novelty remains subject to a full-text and independent literature review. This is not a claim that the papers have been exhaustively ruled out from their snippets.

## Limitations

The formula applies to triangle friendship graphs \(F_n\), not general windmills, arbitrary cactus graphs, or unrestricted sequences. The verification covers finite parameters only and is not a computer-assisted proof of the infinite statement. The closed-form result has undergone a self-review, not independent validation; a previously unknown equivalent result remains a literature risk.

## References

1. J. Ferme, J. Hedžet, P. Melicharová, D. Mesarič Štesl, *On \(S\)-packing total colorings*, arXiv:2609.10107 (first publicly available 2026-09-09). https://arxiv.org/abs/2609.10107
2. J. Ferme, D. Mesarič Štesl, *On packing total coloring*, arXiv:2508.08691 (2025-08-12). https://arxiv.org/abs/2508.08691
