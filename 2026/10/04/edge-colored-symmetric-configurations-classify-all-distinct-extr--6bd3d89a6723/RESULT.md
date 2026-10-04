# Edge-colored symmetric configurations classify all-distinct extremal constant-composition codes
## Finding
For integers \(w\ge 2\) and \(n\ge w\), use the alphabet \(\{0,1,\ldots,w\}\). A word has composition \(\llbracket 1,\ldots,1\rrbracket\) when each nonzero symbol \(1,\ldots,w\) occurs exactly once. If a code \(C\) of such words has minimum Hamming distance at least \(2w-1\), then \(|C|\le n\).

Equality \(|C|=n\) holds if and only if the supports of the words form a symmetric configuration \(n_w\). More precisely, after coordinate and block labels are fixed, equality codes are exactly the proper \(w\)-edge-colorings of the Levi graphs of symmetric configurations \(n_w\), with the edge color at an incidence used as the nonzero symbol in the corresponding coordinate.

For \(w=6\), the known existence spectrum of symmetric configurations gives
\[
A_7(n,11,\llbracket1,1,1,1,1,1\rrbracket)=n
\]
if and only if \(n=31\) or \(n\ge34\). Hence
\[
N_{\mathrm{ccc}}(\llbracket1,1,1,1,1,1\rrbracket)=34.
\]

## Assumptions and scope
A symmetric configuration \(n_w\) is an incidence structure with \(n\) points and \(n\) blocks, every block incident with exactly \(w\) points, every point incident with exactly \(w\) blocks, and every two distinct points incident with at most one common block. Equivalently its Levi graph is a simple \(w\)-regular bipartite graph of girth at least six.

The coding statement concerns only the equality layer \(|C|=n\) for composition \(\llbracket1,\ldots,1\rrbracket\) and distance \(2w-1\). The numerical corollary uses the established spectrum for line size six: a symmetric configuration \(n_6\) exists exactly for \(n=31\) and for every \(n\ge34\).

## Proof
Let \(u,v\) be distinct codewords, put \(r=|\operatorname{supp}(u)\cap\operatorname{supp}(v)|\), and let \(t\) be the number of coordinates in that intersection at which the two nonzero symbols are equal. Since each word has Hamming weight \(w\),
\[
d_H(u,v)=2w-r-t.
\]
The distance condition therefore implies \(r+t\le1\). In particular, two supports meet in at most one coordinate, and if they meet then the two symbols there are different.

At a fixed coordinate, no nonzero symbol can occur in two codewords: that would give \(r\ge1\) and \(t\ge1\). There are only \(w\) nonzero symbols, so at most \(w\) codewords are nonzero in any coordinate. Counting nonzero incidences gives \(|C|w\le nw\), hence \(|C|\le n\).

Suppose \(|C|=n\). The incidence count is then \(nw\), while every one of the \(n\) coordinates has incidence degree at most \(w\). Thus every coordinate has degree exactly \(w\). Taking coordinates as points and supports as blocks gives \(n\) points and \(n\) distinct blocks, all point and block degrees equal to \(w\), with any two blocks meeting in at most one point. The dual incidence structure is therefore a symmetric configuration \(n_w\); symmetry makes the point/block convention immaterial.

The symbols already give a proper edge-coloring of the Levi graph: a block sees every nonzero symbol exactly once by the composition condition, and a point sees distinct symbols because equal symbols at a common coordinate are forbidden. Thus an equality code determines a proper \(w\)-edge-coloring.

Conversely, let a symmetric configuration \(n_w\) be given. Its Levi graph is \(w\)-regular and bipartite, so König's line-coloring theorem gives a proper edge-coloring with exactly \(w\) colors. For each block, form a length-\(n\) word whose entry at an incident point is the color of that incidence and whose other entries are zero. Properness at the block gives composition \(\llbracket1,\ldots,1\rrbracket\). Two blocks are disjoint or meet once; in the latter case properness at the point gives different colors. Hence their Hamming distance is respectively \(2w\) or \(2w-1\). This constructs an equality code and reverses the preceding map.

For \(w=6\), Kaski and Östergård prove that a symmetric configuration \(n_6\) exists exactly when \(n=31\) or \(n\ge34\). Applying the equivalence yields the exact equality spectrum for \(A_7(n,11,\llbracket1,1,1,1,1,1\rrbracket)\). Chee, Dau, Ling, and Ling define \(N_{\mathrm{ccc}}\) as the least threshold beyond which the Johnson equality holds for every length; because equality fails at \(n=33\) and holds for every \(n\ge34\), the threshold is exactly \(34\).

## Verification
The standalone verifier constructs the projective plane \(PG(2,5)\), which is a symmetric configuration \(31_6\). It decomposes the \(6\)-regular Levi graph into six perfect matchings, uses these as edge colors, builds the resulting seven-ary constant-composition code, and checks all \(\binom{31}{2}\) pairwise distances. The expected output is `VERIFY_OK points=31 blocks=31 degree=6 edge_colors=6 code_size=31 min_distance=11 max_distance=11`.

This finite computation is a stress test of both directions of the construction at one nontrivial parameter. The universal equivalence is proved symbolically above, and the \(n_6\) existence spectrum is a published theorem rather than a computational claim of this package.

## Relationship to prior work
Chee, Dau, Ling, and Ling (arXiv:1008.1611) determine almost all optimal constant-composition codes of total weight at most six. Their Section VIII identifies exactly two undetermined values in that range, \(A_7(n,11,\llbracket1,1,1,1,1,1\rrbracket)\) for \(n\in\{33,34\}\), and records only \(N_{\mathrm{ccc}}(\llbracket1,1,1,1,1,1\rrbracket)\in[33,35]\). Their counting proof also contains the support-intersection ingredients used above, but does not state the symmetric-configuration/edge-coloring equivalence.

Kaski and Östergård (Australasian Journal of Combinatorics 38 (2007), 273–277) prove that a symmetric configuration with line size six exists exactly for \(n=31\) or \(n\ge34\). Davydov, Faina, Giulietti, Marcugini, and Pambianco (arXiv:1203.0709) survey symmetric configurations, their Levi graphs, and the same \(32_6\)/\(33_6\) nonexistence data. The inspected configuration sources discuss incidence structures and LDPC applications, not the all-distinct constant-composition equality correspondence above.

## Limitations
The theorem classifies only codes at the upper-bound equality \(|C|=n\); it does not determine the exact subextremal values when no symmetric configuration exists. In particular, it does not by itself give the exact value below \(n\) at \(n=32\) or \(n=33\). It also does not enumerate nonisomorphic equality codes or proper edge-colorings. The exact threshold \(34\) depends on the published line-size-six configuration spectrum.

## References
1. P. Kaski and P. R. J. Östergård, “There exists no symmetric configuration with 33 points and line size 6,” *Australasian Journal of Combinatorics* 38 (2007), 273–277.
2. Y. M. Chee, S. H. Dau, A. C. H. Ling, and S. Ling, “Linear Size Optimal q-ary Constant-Weight Codes and Constant-Composition Codes,” arXiv:1008.1611, first posted 2010-08-10.
3. A. A. Davydov, G. Faina, M. Giulietti, S. Marcugini, and F. Pambianco, “On constructions and parameters of symmetric configurations \(v_k\),” arXiv:1203.0709, first posted 2012-03-04.
