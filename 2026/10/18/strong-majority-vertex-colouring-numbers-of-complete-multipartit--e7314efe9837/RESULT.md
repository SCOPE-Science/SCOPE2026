# Strong-majority vertex-colouring numbers of complete multipartite graphs

## Finding

**Theorem.** Let \(G=K_{n_1,\ldots,n_r}\) be a finite simple complete multipartite graph with \(r\ge 2\), every \(n_i\ge1\), and minimum degree \(\delta(G)=\sum_i n_i-\max_i n_i\ge2\). A *strong-majority vertex-colouring* is a vertex map \(c:V(G)\to[q]\) such that for every vertex \(v\) and every colour \(j\),
\[
2\,|N_G(v)\cap c^{-1}(j)|\le |N_G(v)|.
\]
Let \(\operatorname{Maj}(G)\) be the least permissible palette size (unused colours are allowed). Then
\[
\boxed{\operatorname{Maj}(G)=
\begin{cases}
2,&\text{every }n_i\text{ is even},\\
4,&\{n_1,\ldots,n_r\}=\{1,1,2\}\text{ or }\{1,1,1,1\},\\
3,&\text{otherwise}.
\end{cases}}
\]
The braces in the middle case denote multisets of part sizes. In particular, among complete multipartite graphs of minimum degree at least two, precisely two graph isomorphism types need four colours; three suffice on every other member. An explicit linear-time colouring construction is given in the proof. The two-colour part-parity characterization is already known in the equivalent language of neighbourhood-balanced colourings [2]; the new content is the sharp three-versus-four classification and the construction.

## Assumptions and scope

Graph vertices are distinct and finite, edges occur between every two different parts and never within a part, and vertex-colourings need not be proper. The open neighbourhood is used, not the closed neighbourhood; the condition applies to **every** colour, not merely the vertex's own colour. Since a degree-one vertex has one neighbour, it cannot meet the condition with any palette. The theorem therefore restricts to \(\delta(G)\ge2\); there is no claim of a finite invariant when \(\delta(G)=1\). The graph is connected because \(r\ge2\) and all parts are nonempty. The result concerns ordinary static colourings, not adversarial colouring games or majority C-colourings.

## Proof

**1. Two colours.** With two colours represented as \(+1\) and \(-1\), the strong-majority condition is exactly that each open neighbourhood have sign-sum zero. Let \(S_i\) be the sign-sum on part \(i\), and \(S=\sum_iS_i\). Every vertex in part \(i\) has neighbours exactly outside that part, hence \(S-S_i=0\) for all \(i\). Summing gives \((r-1)S=0\), so \(S=S_i=0\) for every \(i\). Thus each part has even order. Conversely, splitting every even part evenly between the two colours balances every open neighbourhood. Hence two colours are possible exactly when all parts have even order. One colour cannot work because every vertex has positive degree. The number of such assignments with two named colours is the known product \(\prod_i\binom{n_i}{n_i/2}\), stated only for context and not as a new enumerative claim.

**2. The two four-colour obstructions.** In \(K_4\), every open neighbourhood has three vertices; each colour may occur at most once in it. If two of the four vertices had the same colour, either of the other vertices would see the repeated colour twice, impossible. Thus all four vertices need different colours. In \(K_{1,1,2}\), write \(u,v\) for the singleton parts and \(x,y\) for the two-vertex part. The degree-two vertices \(x,y\) require \(c(u)\ne c(v)\). Each singleton has degree three, so \(\{c(v),c(x),c(y)\}\) and \(\{c(u),c(x),c(y)\}\) must each consist of three different colours. If only three colours were available, \(\{c(x),c(y)\}\) would be the complement of both \(c(u)\) and \(c(v)\) within that three-colour palette, forcing \(c(u)=c(v)\), a contradiction. Colouring all four vertices distinctly works for both exceptional graphs.

**3. Pair-extension lemma.** Suppose a complete multipartite graph has a strong-majority colouring with at most three colours. Add two new vertices to any one existing part and give them two **different** colours from the palette. Vertices in that part have unchanged neighbourhoods. Every other old vertex gains two neighbours, one of each of two different colours; for each colour the neighbourhood count rises by at most one. If its previous degree was \(d\), its previous count was at most \(\lfloor d/2\rfloor\), and the new count is at most \(\lfloor d/2\rfloor+1=\lfloor(d+2)/2\rfloor\). The new twins have the same neighbourhood as the old vertices of their part, so they also satisfy the condition. Thus the extension preserves strong-majority three-colourability. Repeating extensions proves all larger cases once a finite set of residual cores is coloured.

**4. Bipartite case.** If \(r=2\), the degree condition forces each part size to be at least two. Independently colour the vertices in each part by the repeating word \(1,2,3,1,2,3,\ldots\). Within a part of size \(m\ge2\), every colour occurs at most \(\lceil m/3\rceil\le\lfloor m/2\rfloor\) times. Each vertex sees precisely the other part, and thus all its neighbourhood colour counts meet the strong-majority bound. Consequently every admissible complete bipartite graph is three-colourable.

**5. Three or more parts: reduction.** For \(r\ge3\), reduce each part's order to \(1\) when it is odd or to \(2\) when it is even by successively removing pairs of vertices. The reduced core has every part size in \(\{1,2\}\), and minimum degree at least two. If its part-size multiset is neither \(\{1,1,1,1\}\) nor \(\{1,1,2\}\), colour it by the constructions below and restore the removed pairs by Step 3. If the reduced core is one of those two exceptional four-vertex graphs but the original graph is not the corresponding four-vertex graph, choose any original part from which at least one pair was removed and restore that pair *before* constructing the core colouring. The resulting six-vertex core has part sizes, up to order, \(\{3,1,1,1\}\), \(\{3,1,2\}\), or \(\{4,1,1\}\), which are explicitly coloured below. Any further removed pairs are then restored by Step 3.

**6. Colouring the cores.** For three vertices, the only core with at least three parts is \(K_3\), coloured distinctly \(1,2,3\). For five vertices, each part has size one or two. Give every two-vertex part the colours \(1,2\); if there are \(t\le2\) such parts, give the remaining singleton parts the multiset of colours consisting of \(2-t\) copies of colour \(1\), \(2-t\) copies of colour \(2\), and one copy of colour \(3\). The global counts are \((2,2,1)\): a singleton sees four neighbours with at most two of any colour, and a two-vertex part sees a rainbow triple.

For six vertices when every part has size at most two, assign the colours globally with counts \((2,2,2)\). Every vertex has degree at least four, so every neighbourhood automatically contains at most half of any colour. The three additional six-vertex cores have the following explicit assignments, listing the colour multiset separately within each part:
\[
\begin{array}{c|l}
\text{part sizes}&\text{corresponding colour lists}\\\hline
(3,1,1,1)&(123),(1),(2),(3)\\
(3,2,1)&(123),(23),(1)\\
(4,1,1)&(1233),(1),(2)
\end{array}
\]
In each row the overall colour counts are \((2,2,2)\). The part of size three has a rainbow three-vertex complement; the part of size four has a differently coloured two-vertex complement; all other vertices have degree at least four, so the global maximum count of two is allowed.

For seven vertices with parts of size at most two, use global colour counts \((3,2,2)\). There are at most three two-vertex parts; put one vertex of colour \(1\) in each such part, distribute the remaining colour-\(1\) vertices among singleton parts, and fill the other positions with two copies each of colours \(2\) and \(3\). Each two-vertex part sees five neighbours and excludes at least one of the three colour-\(1\) vertices, so every neighbourhood colour count is at most two. Each singleton sees six neighbours and the global counts are at most three, which is allowed.

For \(n\ge8\) vertices when every part has size at most two, colour the whole vertex set as equally as possible with three colours. Every colour appears globally at most \(\lceil n/3\rceil\), while every vertex has degree at least \(n-2\); the elementary inequality \(\lceil n/3\rceil\le\lfloor(n-2)/2\rfloor\) for \(n\ge8\) proves the condition. These cases exhaust every reduced core other than the two exceptional graphs. Together with Steps 3–5 they give three colours in all other admissible complete multipartite graphs. Combined with Steps 1–2, this proves the theorem. \(\square\)

## Verification

The included standalone Python script `verify_majority.py` reconstructs every relevant multipartite graph directly. Its `valid` routine enumerates open neighbourhoods and tests the defining count inequality at each vertex, independently of the mathematical case formula. It exhaustively searches the named binary and ternary vertex assignments for all \(51\) admissible unordered part-size types with \(3\le |V(G)|\le8\), checking the exact predicted existence thresholds. It also executes the constructive algorithm on \(9{,}246\) part-size types with orders \(3\) through \(25\), and on eight additional large unbalanced profiles. All checks passed. Reproduce by running `python3 verify_majority.py` using Python 3.10 or later; no third-party packages are required. Finite testing is not a proof of the infinite theorem; the unrestricted argument is in the preceding section.

## Relationship to prior work

Kalinowski, Kamyczura, Pilśniak, and Woźniak [1] introduced the strong-majority vertex-colouring invariant, computed it for cycles and complete graphs (including \(\operatorname{Maj}(K_4)=4\)), and proved a general upper bound depending on maximum degree. Freyberg and Marr [2, Theorem 4] already proved the even-part criterion for the equivalent two-colour neighbourhood-balanced property of complete multipartite graphs; Step 1 supplies a self-contained version but does **not** claim that criterion or its counting product as new. Collins, Hook, McBee, and Trenk [3, Section 7] study distinct two-colour neighbourhood \(\lambda\)-balance predicates for complete multipartite graphs; their classification does not establish the static three-colour strong-majority threshold. Chawda and collaborators [4, Section 7] consider the adversarial strong-majority colouring game, specifically cycles, rather than the present static multipartite classification. The new structural content is the universal three-colour construction together with the second, non-complete four-colour obstruction \(K_{1,1,2}\).

## Limitations

This theorem is restricted to finite complete multipartite graphs with \(\delta(G)\ge2\). It does not claim an analogous three-colour bound for arbitrary graphs, where strong-majority numbers are unbounded. It classifies the minimum palette size but not the number of all three-colour assignments, list colourability, or game variants. The bibliographic comparison concerns the listed accessible primary papers and targeted mathematical-record searches; unindexed equivalent work cannot be ruled out, and no independent external audit has been performed.

## References

[1] R. Kalinowski, M. Kamyczura, M. Pilśniak, and M. Woźniak, *Strong majority colorings of graphs*, arXiv:2605.23828, version 1 first posted 22 May 2026. https://arxiv.org/html/2605.23828

[2] B. Freyberg and A. Marr, *Neighborhood Balanced Colorings of Graphs*, *Graphs and Combinatorics* **40**, article 41 (2024), especially Theorem 4. https://doi.org/10.1007/s00373-024-02766-9

[3] K. L. Collins, J. Hook, C. McBee, and A. N. Trenk, *Color 2-switches and neighborhood λ-balanced graphs with k colors*, arXiv:2603.05705, first posted 5 March 2026. https://arxiv.org/abs/2603.05705

[4] Y. Chawda, S. G. Nanoti, B. Sankarnarayanan, and E. Srinivasan, *Structural and computational aspects of majority coloring games*, arXiv:2609.37796, first posted 29 September 2026. https://arxiv.org/html/2609.37796v1
