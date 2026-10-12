# Strong majority number of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a finite connected complete multipartite graph with \(r\ge2\), with every \(n_i\ge1\). A strong majority vertex-coloring is a vertex coloring for which, at every vertex and for every color, at most half of the open neighborhood has that color.

A strong majority vertex-coloring exists if and only if \(G\) is not a star \(K_{1,m}\) with \(m\ge1\). Whenever it exists,
\[
\operatorname{Maj}(G)=
\begin{cases}
2,&\text{if every }n_i\text{ is even},\\
4,&G\cong K_4\text{ or }G\cong K_{2,1,1},\\
3,&\text{otherwise}.
\end{cases}
\]
Thus the only colorable complete multipartite graphs requiring four colors are the two nonstar graphs of order four with all or all-but-one parts singleton.

## Assumptions and scope
Graphs are finite, simple, undirected, connected, and have at least two nonempty partite classes. For a vertex in part \(V_i\), its open neighborhood is exactly \(V(G)\setminus V_i\), of size \(N-n_i\), where \(N=\sum_i n_i\). The strong majority number is used only when the graph has minimum degree at least two, following the defining source.

A connected complete multipartite graph has a pendant vertex exactly when it is a star \(K_{1,m}\). Such a graph admits no strong majority coloring: a pendant vertex sees its unique neighbor's color on its entire neighborhood.

## Proof
First consider two colors. Let \(R_i\) and \(B_i\) be the two color counts in part \(V_i\), and let \(R=\sum_iR_i\), \(B=\sum_iB_i\). At any vertex of \(V_i\), both outside-part color counts are at most half of \(N-n_i\), and together they equal \(N-n_i\). Hence both are exactly half, so
\[
R-R_i=B-B_i
\]
for every \(i\). Writing \(D=R-B\) gives \(R_i-B_i=D\) for every part. Summing over the \(r\) parts gives \(D=rD\), so \(D=0\) because \(r\ge2\). Therefore \(R_i=B_i\) in every part and every \(n_i\) is even. Conversely, if all part sizes are even, coloring half of every part with each of two colors makes every open neighborhood exactly balanced. This proves the two-color branch.

The graph \(K_4\) requires four colors: this is the complete-graph exception already proved in the defining strong-majority paper. The graph \(K_{2,1,1}\) also requires four. Let its singleton vertices be \(a,b\) and its two-vertex part be \(\{x,y\}\). Since \(x\) has neighborhood \(\{a,b\}\), the vertices \(a,b\) must have different colors. Since \(a\) has degree three, the three vertices \(b,x,y\) must have pairwise distinct colors; similarly \(a,x,y\) must have pairwise distinct colors. With only three colors, \(x,y\) use two colors and both \(a\) and \(b\) are forced to use the third, contradicting that \(a,b\) differ. Four distinct colors work.

It remains to prove that every other nonstar profile not covered by the two-color branch has a strong majority three-coloring. There is a uniform construction for all orders \(N\ge12\). Arrange the vertices so that each part is a consecutive block, and color consecutive positions periodically with colors \(1,2,3,1,2,3,\ldots\). The total color-count triple has pairwise differences at most one, and the same is true within every block. Therefore, for every part, the three color counts in its outside neighborhood have pairwise differences at most two.

If three nonnegative integers sum to \(d\ge6\) and differ pairwise by at most two, none exceeds \(d/2\). Indeed, if the maximum \(M\) exceeded \(d/2\), then the other two entries would each be at least \(M-2\), giving \(d\ge3M-4\); checking the even and odd forms of \(d\ge6\) contradicts \(M> d/2\).

Consequently the periodic coloring works whenever every part has outside degree at least six. If some part has outside degree \(d<6\), choose a largest such part \(P\) and put its block last. Because the graph is a nonstar, \(2\le d\le5\). The neighborhood of a vertex of \(P\) is then the initial periodic segment of length \(d\), whose largest color count is \(\lceil d/3\rceil\le d/2\). Every other part has size at most \(d\), since all vertices outside \(P\) total \(d\), and hence its outside degree is at least \(N-d\ge7\). The preceding spread argument applies. Thus every nonstar complete multipartite graph of order at least twelve has a strong majority three-coloring.

The finitely many profiles of orders at most eleven are closed by exhaustive count-matrix enumeration. A coloring of a complete multipartite graph is relevant only through the number of vertices of each color in each part. The accompanying verifier enumerates every such count matrix for the needed palette sizes. It confirms that the only colorable profiles in this finite range lacking a three-coloring are \(K_4\) and \(K_{2,1,1}\). Combined with the exact two-color criterion, this completes the proof.

## Verification
The proof of the infinite range is analytic. The bundled `verify.py` performs three independent finite checks: exhaustive count-matrix searches for every nondecreasing multipartite profile of order at most eleven; direct testing of the periodic three-color construction for every nonstar profile of orders twelve through forty; and direct testing of the half-half two-color construction for every all-even profile through order thirty.

A replay of the verifier extracted from this package returned:

`ALL CHECKS PASSED; small_profiles_N<=11=183; small_search_calls=495; small_witnesses=173; periodic_profiles_N=12..40=215055; two_color_profiles_N<=30=28569; exception_profiles=K_4,K_{2,1,1}`

The finite computations are corroborative outside the explicitly finite \(N\le11\) closure; they are not used as evidence for the infinite construction.

## Relationship to prior work
Kalinowski, Kamyczura, Pilśniak, and Woźniak introduced strong majority vertex-coloring in 2026. Their paper proves the exact complete-graph values, including the exceptional value \(\operatorname{Maj}(K_4)=4\), but its full text contains no complete-multipartite or complete-bipartite theorem for the vertex parameter.

The two-color branch is not claimed as new. A strong majority coloring with exactly two colors is the same thing as a neighborhood-balanced two-coloring, because both neighborhood color counts must equal half the degree. Freyberg and Marr proved in 2024 that a complete multipartite graph admits such a coloring exactly when every part has even size. The present result uses that equivalence as prior coverage and determines the remaining exact strong-majority values: three colors always suffice except for \(K_4\) and \(K_{2,1,1}\).

Collins, Hook, McBee, and Trenk studied two-color neighborhood \(\lambda\)-balance in 2026 and obtained complete-multipartite balance bounds, but those are two-color discrepancy statements rather than the minimum palette size under the strong-majority constraint. Chawda, Nanoti, Sankarnarayanan, and Srinivasan studied strong-majority coloring games later in 2026 and restated the known static complete-graph values; their inspected text contains no complete-multipartite theorem for the static number.

## Limitations
The theorem is restricted to complete multipartite graphs. It does not classify strong majority numbers under edge deletions, list constraints, precoloring extension, or the game version. The proof for orders at most eleven uses exhaustive finite enumeration of part-by-color count matrices; the infinite range is proved separately by an explicit periodic construction. The two-color branch is previously known through neighborhood-balanced coloring and is included only to state the complete strong-majority classification.

## References
[1] R. Kalinowski, M. Kamyczura, M. Pilśniak, M. Woźniak, “Strong majority colorings of graphs,” arXiv:2605.23828, first public 2026-05-22. Primary MSC 05C15; secondary MSC 05C70.

[2] B. Freyberg, A. Marr, “Neighborhood Balanced Colorings of Graphs,” Graphs and Combinatorics 40 (2024), Article 41. Theorem 4 classifies neighborhood-balanced two-colorings of complete multipartite graphs.

[3] K. L. Collins, J. Hook, C. McBee, A. N. Trenk, “Color 2-switches and neighborhood \(\lambda\)-balanced graphs with \(k\) colors,” arXiv:2603.05705, 2026.

[4] Y. Chawda, S. G. Nanoti, B. Sankarnarayanan, E. Srinivasan, “Structural and computational aspects of majority coloring games,” arXiv:2609.37796, 2026.
