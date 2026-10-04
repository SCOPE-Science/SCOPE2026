# Sequence b-colorings of complete multipartite graphs are rigid
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a finite simple connected complete multipartite graph with \(r\ge2\) and \(n_1\ge\cdots\ge n_r\ge1\). A finite non-increasing sequence \(S=(s_1,\ldots,s_k)\) is realized by a sequence \(b\)-coloring of \(G\) if and only if \(k=r\) and \(s_i\le n_i\) for every \(1\le i\le r\).

Every realizing coloring is obtained by assigning one distinct color to each multipartite part. Hence every vertex is a color-dominating vertex. In particular, \(G\) has the unique maximal realized sequence
\[
(n_1,\ldots,n_r).
\]
For an infinite sequence \(S=(s_1,s_2,\ldots)\), its \(S\)-spectrum on \(G\) is \(\{r}\) exactly when \(s_i\le n_i\) for \(1\le i\le r\), and otherwise it is empty.

There is also an exact count for labeled colors. For a realized length-\(r\) sequence set
\[
c_i=\left|\{j:n_j\ge s_i}\right|.
\]
Then the number of labeled realizing colorings is
\[
\prod_{i=1}^r(c_i-i+1).
\]
If some \(c_i<i\), there is no realizing coloring.

## Assumptions and scope
Graphs are finite, simple, connected, and complete multipartite. The multipartite parts are nonempty and their sizes are written in non-increasing order. A sequence is non-increasing and positive, as in the initiating definition of sequence \(b\)-coloring. A color-dominating vertex is one whose closed neighborhood contains every color used in the coloring.

The theorem concerns the exact set of realized sequences and the exact count of labeled realizing colorings. It does not make a claim for arbitrary co-cluster perturbations or for other generalized \(b\)-coloring variants.

## Proof
Write the parts of \(G\) as \(P_1,\ldots,P_r\). In any proper coloring, a color cannot occur in two distinct parts because every two vertices from distinct parts are adjacent.

Suppose some part \(P_j\) uses at least two colors. Let \(x\in P_j\). Its closed neighborhood is
\[
N[x]=\{x}\cup\bigl(V(G)\setminus P_j\bigr).
\]
Thus \(x\) sees its own color and every color used outside \(P_j\), but it sees no color used on another vertex of \(P_j\). Since every color used in \(P_j\) occurs nowhere outside \(P_j\), no vertex of \(P_j\) can be color-dominating. Therefore every color class contained in \(P_j\) lacks a color-dominating vertex, contradicting the requirement that the coloring be a \(b\)-coloring. Hence every part is monochromatic.

Different parts are pairwise complete to each other, so they must receive distinct colors. Therefore every \(b\)-coloring of \(G\) uses exactly \(r\) colors and is precisely the part coloring up to a permutation of color labels. Conversely, in such a part coloring, each vertex \(x\in P_j\) sees its own color at \(x\) and every other color on the other parts, so every vertex is color-dominating.

It follows that a length-\(r\) sequence can be realized exactly when its requirements can be matched to the part sizes. With both \((s_1,\ldots,s_r)\) and \((n_1,\ldots,n_r)\) sorted non-increasingly, such a matching exists exactly when \(s_i\le n_i\) for every \(i\). No sequence of any other finite length can be realized because every \(b\)-coloring has exactly \(r\) colors.

For the counting statement, process labeled colors in order \(1,2,\ldots,r\). For color \(i\), exactly \(c_i\) parts are large enough to meet requirement \(s_i\). Since \(s_1\ge\cdots\ge s_r\), every part chosen for an earlier color is also among these \(c_i\) eligible parts. After \(i-1\) choices, exactly \(c_i-i+1\) eligible parts remain. Multiplication gives the stated product.

## Verification
The accompanying standard-library verifier independently reconstructs complete multipartite graphs, enumerates every surjective proper coloring for all sorted part-size tuples with two to four parts and at most six vertices, identifies all color-dominating vertices from closed neighborhoods, and checks every \(b\)-coloring. Across the tested graphs it finds that every \(b\)-coloring uses exactly the number of multipartite parts and makes each part monochromatic.

The verifier also enumerates non-increasing requirement sequences and compares the direct number of labeled realizations with the product formula. Its replay output is stored in `verification_output.txt`.

## Relationship to prior work
Jakovac and Lang introduced sequence \(b\)-colorings in 2026, defined realized sequences and \(S\)-spectra, and explicitly posed the structural direction of determining which sequences a fixed graph realizes. Their paper treats complete graphs as an elementary example, gives a detailed classification for cycles, and studies regular graphs, but the inspected full text contains no occurrence of “multipartite” or “bipartite” and does not state the complete-multipartite classification above.

Classical \(b\)-coloring literature includes complete multipartite graphs as a basic co-cluster class. Balabán's 2026 parameterized study, for example, uses distance to co-cluster, where a co-cluster is exactly a complete multipartite graph. That literature concerns ordinary \(b\)-colorings and does not determine the new sequence requirements or the maximal realized sequence.

## Limitations
The proof uses the full completeness between different multipartite parts. It does not extend verbatim to general bipartite graphs, to graphs obtained by deleting cross edges, or to co-cluster perturbations. The sequence \(b\)-coloring notion is very recent, so unindexed concurrent work is a residual literature risk. The finite verifier is a stress test of the theorem and counting formula; the infinite family is proved by the structural argument above, not by enumeration.

## References
1. M. Jakovac and M. S. Lang, *Sequence b-colorings in graphs*, arXiv:2609.08484v1, 2026.
2. J. Balabán, *Finding b-Colorings Using Feedback Edges*, LIPIcs MFCS 2026, Article 36, DOI:10.4230/LIPIcs.MFCS.2026.36.
