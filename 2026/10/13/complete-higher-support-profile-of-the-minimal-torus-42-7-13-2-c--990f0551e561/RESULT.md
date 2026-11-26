# Complete higher-support profile of the minimal-torus \([42,7,13]_2\) code
## Finding

Lorite López, Camazón Portela, and López Ramos attach in Example 5.3 a binary code to the minimal seven-vertex triangulation of the torus and obtain parameters
\[
[42,7,13]_2.
\]
As a specialization of the induced-subcomplex formula [5], its generalized Hamming-weight hierarchy is
\[
(d_1,d_2,d_3,d_4,d_5,d_6,d_7)=(13,23,30,35,39,41,42).
\]

The contribution here is the complete support-size distributions, with \(w:N\) meaning exactly \(N\) subcodes of support size \(w\), including the multiplicities of the known minima:
\[
r=1:\quad13:7,\ 20:42,\ 21:43,\ 24:21,\ 25:14,
\]
\[
r=2:\quad23:21,\ 27:196,\ 29:161,\ 30:182,\ 31:651,\ 32:315,\ 33:686,\ 34:126,\ 35:280,\ 36:28,\ 37:21,
\]
\[
r=3:\quad30:21,\ 31:14,\ 32:126,\ 33:210,\ 34:511,\ 35:1157,\ 36:1974,\ 37:2786,\ 38:2786,\ 39:1575,\ 40:553,\ 41:98,
\]
\[
r=4:\quad35:14,\ 36:119,\ 37:420,\ 38:1239,\ 39:3024,\ 40:3906,\ 41:2590,\ 42:499,
\]
\[
r=5:\quad39:119,\ 40:504,\ 41:1281,\ 42:763,
\]
\[
r=6:\quad41:42,\ 42:85,
\]
and
\[
r=7:\quad42:1.
\]
Thus the numbers of subcodes attaining the generalized Hamming weights are
\[
7,\ 21,\ 21,\ 14,\ 119,\ 42,\ 1.
\]

## Assumptions and scope

The source associates to a simplicial complex \(\Delta\) on \(k\) vertices the binary code whose generator columns are the characteristic vectors of the nonempty faces of \(\Delta\). Example 5.3 uses a triangulation of the torus with seven vertices, twenty-one edges, and fourteen triangular faces, so the code has \(42\) nonzero face columns.

The seven-vertex torus triangulation is unique up to combinatorial isomorphism. For reproducibility, use vertices \(\mathbb Z/7\mathbb Z\) and the fourteen facets
\[
\{i,i+1,i+3\},\qquad \{i,i+2,i+3\},
\]
for \(i\in\mathbb Z/7\mathbb Z\), with indices modulo seven. Vertex relabeling changes the associated code only by equivalence.

The claim concerns this exact torus code. It does not assert a formula for arbitrary surface triangulations.

## Proof

The cyclic facet list has fourteen distinct triangles. Every one of the twenty-one vertex pairs is an edge, every edge belongs to exactly two triangles, every vertex link is a six-cycle, and the facets admit a consistent orientation. The complex is therefore a connected orientable closed surface, and
\[
7-21+14=0.
\]
Hence it is a torus triangulation. By uniqueness it is combinatorially isomorphic to the seven-vertex torus in Example 5.3.

Let \(G\) be the \(7\times42\) binary matrix whose columns are the characteristic vectors of all nonempty faces. Every row has weight
\[
1+6+6=13,
\]
corresponding to the vertex itself, six incident edges, and six incident triangles. The matrix has rank seven. Enumerating its \(128\) codewords gives
\[
1+7z^{13}+42z^{20}+43z^{21}+21z^{24}+14z^{25},
\]
so its minimum distance is the published value \(13\).

Because \(G\) has rank seven, \(r\)-dimensional message subspaces are in bijection with \(r\)-dimensional code subcodes. Every message subspace has a unique reduced-row-echelon basis. Their numbers for \(r=1,\ldots,7\) are
\[
127,\ 2667,\ 11811,\ 11811,\ 2667,\ 127,\ 1,
\]
for a total of \(29211\).

For a basis \(u_1,\ldots,u_r\), the support of the generated subcode is exactly
\[
\operatorname{Supp}(u_1G)\cup\cdots\cup\operatorname{Supp}(u_rG).
\]
A coordinate is absent exactly when every basis word, and hence every word of the subcode, vanishes there. Exhaustive enumeration of all reduced-row-echelon message subspaces therefore proves the complete histograms above. Their minima are
\[
(13,23,30,35,39,41,42).
\]

These minima also follow directly from [5], which gives \(d_r=42-\max_{|P|=7-r}\#\{\sigma\ne\varnothing:\sigma\subseteq P\}\) over vertex subsets \(P\). At sizes \(6,5,4,3,2,1,0\) the maximum numbers of contained facets are \(8,4,2,1,0,0,0\), respectively: a removed vertex meets six facets, any removed pair meets ten, and any removed triple meets twelve plus one if it is itself a facet. A nonfacet triple exists. At size three one can take a facet. Adding \(|P|+\binom{|P|}{2}\) for vertices and edges gives the hierarchy without a subspace census. This formula supplies the minima, not the frequencies of the subcode supports.

## Verification

`artifacts/verify.py` uses only the Python standard library. It reconstructs the cyclic fourteen-facet complex, verifies the surface-incidence and orientability conditions, forms all forty-two nonempty face columns, and checks generator rank seven, row weight thirteen, and the ordinary weight distribution above.

It then generates every positive-dimensional subspace of \(\mathbb F_2^7\) exactly once in reduced-row-echelon form, checks the Gaussian-binomial totals, computes every subcode support, and compares every support histogram with `artifacts/certificate.json`.

Successful replay prints `VERIFY_OK`.

## Relationship to prior work

The primary paper develops a geometric interpretation of ordinary codeword weights for arbitrary simplicial complexes and derives classical code parameters. Example 5.3 records length \(42\), dimension \(7\), and minimum distance \(13\); it does not state generalized Hamming weights or subcode-support distributions.

Liu, Zheng, Lu, and Wang study generalized Hamming weights for simplicial-complex defining sets. Their general intersection identity applies to the binary face set here, and the induced-subcomplex formula [5] evaluates the whole hierarchy by considering only induced vertex subsets. That computation does not count all message subspaces, including the noncoordinate ones, even when restricted to minimizers. The distinction between the hierarchy and the distribution is essential here.

Pan, Chen, Liu, and Liu determine complete subcode-support distributions for several repeated-simplex and projective-subspace-deletion constructions. No table for this exact minimal-torus face-incidence code was identified in the comparisons. The Tutte polynomial of its generator-column matroid would determine the full table by counting sets of coordinates simultaneously zero on a subcode and applying binomial inversion; an evaluated polynomial for that exact matroid would therefore be relevant equivalent coverage.

## Limitations

This is an exact finite classification for one canonical topological example, not a general formula for every triangulated surface.

The result classifies subcodes by support size, not by automorphism-group orbit.

The generalized Hamming weights are prior implications. The claim here is the complete support distribution in every positive dimension, including the minimizer multiplicities.

An unindexed computation could contain the same finite census; no such source was found in the inspected literature.

## References

1. Antonio Jesús Lorite López, Daniel Camazón Portela, and Juan Antonio López Ramos, *Linear codes arising from geometrical operations*, AIMS Mathematics 11 (2026), 10033--10048, DOI 10.3934/math.2026414.
2. Chao Liu, Dabin Zheng, Wei Lu, and Xiaoqiang Wang, *The weight hierarchies of linear codes from simplicial complexes*, Discrete Mathematics 348 (2025), 114240, DOI 10.1016/j.disc.2024.114240; arXiv:2310.11873.
3. Xu Pan, Hao Chen, Hongwei Liu, and Shengwei Liu, *Optimal Few-SSW Linear Codes and Their Subcode Support Weight Distributions*, IEEE Transactions on Information Theory 71 (2025), 1028--1042, DOI 10.1109/TIT.2024.3519672.
4. V. K. Wei, *Generalized Hamming weights for linear codes*, IEEE Transactions on Information Theory 37 (1991), 1412--1418.
5. *Full generalized Hamming hierarchy from induced subcomplex maxima*, [archived result](https://github.com/Resultary/2026/blob/main/2026/10/12/SCOPE-full-generalized-hamming-hierarchy-from-induced-subcomplex-maxim--fc8afde3d48f/RESULT.md).
