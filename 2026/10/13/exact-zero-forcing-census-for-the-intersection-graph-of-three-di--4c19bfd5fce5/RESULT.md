# Exact zero forcing census for the intersection graph of three-dimensional ternary space

## Finding

Let \(V=\mathbb F_3^3\), and let \(\mathcal G(V)\) be the intersection graph whose vertices are the nonzero proper subspaces of \(V\), with distinct vertices adjacent exactly when their intersection is nonzero. Then \[\mathcal Z(\mathcal G(V);u)=1246986u^{13}+3599154u^{14}+4874220u^{15}+4326426u^{16}+2872233u^{17}+1515501u^{18}+651950u^{19}+229801u^{20}+65767u^{21}+14950u^{22}+2600u^{23}+325u^{24}+26u^{25}+u^{26}.\] Consequently \(Z(\mathcal G(V))=M(\mathcal G(V))=13\) and the real symmetric minimum rank is \(\operatorname{mr}(\mathcal G(V))=13\). There are exactly \(1{,}246{,}986\) minimum zero forcing sets. Under the natural \(\operatorname{PGL}(3,3)\)-action these minimum sets form exactly \(254\) orbits, with orbit-size histogram \(234^1,936^9,1404^2,2808^{44},5616^{198}\). Among the minimum sets, \(556{,}686\) contain six one-dimensional subspaces and \(690{,}300\) contain seven.

This gives a complete forcing census for the first odd-order projective-plane instance of this module-intersection graph, together with an exact inverse-eigenvalue parameter and a symmetry classification of all minimum forcing sets.

## Assumptions and scope

Let
\\[
V=\\mathbb F_3^3.
\\]
Following the module-intersection-graph convention, the vertices are the nonzero proper subspaces of \\(V\\), and two distinct subspaces are adjacent exactly when their intersection is nonzero.

There are thirteen one-dimensional subspaces and thirteen two-dimensional subspaces. Identify the one-dimensional subspaces with the points of \\(\\operatorname{PG}(2,3)\\), and identify the two-dimensional subspaces with the projective lines. Thus the graph has \\(26\\) vertices.

The one-dimensional vertices form an independent set. The two-dimensional vertices form a clique, since two planes in a three-dimensional vector space have nonzero intersection. Point-plane adjacency is exactly projective incidence.

For reproducibility, normalize every nonzero vector by scaling its first nonzero coordinate to \\(1\\). In lexicographic order the thirteen normalized projective representatives are
\[
(0,0,1),(0,1,0),(0,1,1),(0,1,2),(1,0,0),(1,0,1),(1,0,2),
(1,1,0),(1,1,1),(1,1,2),(1,2,0),(1,2,1),(1,2,2).
\]
Vertices \\(0,\\ldots,12\\) are the corresponding one-dimensional subspaces. Vertices \\(13+j\\), \\(0\\le j<13\\), are the planes whose normalized normal vectors are the same thirteen representatives in the same order.

## Proof

Let \\(B\\) be the \\(13\\times13\\) point-line incidence matrix of \\(\\operatorname{PG}(2,3)\\) in the ordering above. Every point is on four lines, every line contains four points, and two distinct points determine exactly one line. Hence
\\[
BB^{\\mathsf T}=3I+J.
\\]

Consider the real symmetric matrix
\\[
C=
\\begin{pmatrix}
I&B\\\\
B^{\\mathsf T}&B^{\\mathsf T}B
\\end{pmatrix}
=
\\begin{pmatrix}I\\\\B^{\\mathsf T}\\end{pmatrix}
\\begin{pmatrix}I&B\\end{pmatrix}.
\\]
Its upper-left off-diagonal entries are zero, matching the independent point set. Its point-line block is precisely the incidence matrix. Finally,
\\[
B^{\\mathsf T}B=3I+J,
\\]
so every off-diagonal line-line entry is nonzero, matching the line clique. Thus \\(C\\) has exactly the required off-diagonal zero pattern.

The top \\(13\\) rows of the left factor contain \\(I\\), so
\\[
\\operatorname{rank} C=13.
\\]
Therefore
\\[
\\operatorname{mr}(\\mathcal G(V))\\le13,
\\qquad
M(\\mathcal G(V))\\ge26-13=13.
\\]
The standard inequality \\(M(G)\\le Z(G)\\) gives
\\[
Z(\\mathcal G(V))\\ge13.
\\]

For the reverse inequality, the following thirteen vertices are an explicit zero forcing set:
\\[
\\{0,1,2,3,4,5,8,13,14,15,17,18,20\\}.
\\]
With the ordering fixed above, one valid chronological force sequence is
\\[
0\\to23,\\ 1\\to19,\\ 4\\to16,\\ 8\\to21,\\ 3\\to25,\\ 5\\to22,\\ 2\\to24,
\\]
\\[
14\\to6,\\ 16\\to12,\\ 18\\to9,\\ 15\\to11,\\ 20\\to10,\\ 13\\to7.
\\]
Hence \\(Z(\\mathcal G(V))\\le13\\), and therefore
\\[
Z(\\mathcal G(V))=M(\\mathcal G(V))=\\operatorname{mr}(\\mathcal G(V))=13.
\\]

The complete polynomial and the orbit data are finite exact enumerations. The standalone enumerator checks every one of the \\(2^{26}=67{,}108{,}864\\) vertex subsets by the standard color-change rule. It obtains exactly
\\[
1246986u^{13}+3599154u^{14}+4874220u^{15}+4326426u^{16}+2872233u^{17}+1515501u^{18}
\\]
\\[
{}+651950u^{19}+229801u^{20}+65767u^{21}+14950u^{22}+2600u^{23}+325u^{24}+26u^{25}+u^{26}.
\\]
The coefficients sum to \\(2^{26}\\), as required for an all-subset census.

For symmetry, four explicit projective linear transformations in `verify.py` generate a permutation group of order \\(5616\\), equal to \\(|\\operatorname{PGL}(3,3)|\\). Acting on all \\(1{,}246{,}986\\) minimum zero forcing sets gives \\(254\\) orbits. Their sizes and multiplicities are
\\[
234:1,\\qquad 936:9,\\qquad 1404:2,\\qquad 2808:44,\\qquad 5616:198.
\\]
The orbit sizes account for every minimum set exactly. The independent-set occupancy census is
\\[
556{,}686
\\]
minimum sets with six point vertices and
\\[
690{,}300
\\]
with seven point vertices.

## Verification

The actual packaged `verify.py` was read before replay. It reconstructs the projective points and lines directly over \\(\\mathbb F_3\\), verifies all row and column sums of \\(B\\), checks \\(BB^{\\mathsf T}=3I+J\\), row-reduces the graph-pattern witness exactly over the rationals, and replays the explicit zero forcing sequence. It also constructs the projective action from four \\(3\\times3\\) matrices and verifies that the generated permutation group has order \\(5616\\).

Replay output:

```text
PG(2,3) incidence: 13 points, 13 lines, row/column sum 4, BB^T=3I+J
Gram-pattern witness: exact real rank 13 and correct off-diagonal graph pattern
explicit forcing witness mask: 1499455
forcing sequence: [(0, 23), (1, 19), (4, 16), (8, 21), (3, 25), (5, 22), (2, 24), (14, 6), (16, 12), (18, 9), (15, 11), (20, 10), (13, 7)]
PGL generator action: order 5616
VERIFY_OK
```

The packaged `enumerate.cpp` is an independent complete subset census for this finite graph. Its stored exact output is:

```text
polynomial 13:1246986 14:3599154 15:4874220 16:4326426 17:2872233 18:1515501 19:651950 20:229801 21:65767 22:14950 23:2600 24:325 25:26 26:1
minimum_sets=1246986 orbits=254 orbit_hist 234:1 936:9 1404:2 2808:44 5616:198
minimum_point_profile 6:556686 7:690300
ENUMERATE_OK
```

The rank argument proves the minimum forcing size without relying on exhaustive search. Exhaustive enumeration is used for the complete polynomial and the finite symmetry census, for which it is a complete proof because every vertex subset is examined.

## Relationship to prior work

Akbari, Tavallaee, and Khalashi Ghezelahmad introduced the intersection graph of nontrivial submodules and studied connectivity, diameter, girth, clique number, and chromatic number. Yaraneri develops the general module-intersection framework and explicitly defines a proper submodule to mean one different from both \\(0\\) and the whole module. His full text lists primary Mathematics Subject Classification \\(16D10\\) and treats connectedness, domination, finiteness, coloring, and planarity. A full-text search of that source finds no occurrence of “zero forcing.”

Jafari Rad and Jafari study the intersection graph of subspaces of a finite-dimensional vector space over a finite field, focusing on clique, chromatic, domination, and independence numbers. Their published abstract does not state a zero forcing or minimum-rank result.

General zero forcing theory supplies \\(M(G)\\le Z(G)\\), and the general zero forcing polynomial literature supplies the counting invariant. Targeted searches using the module-intersection, subspace-intersection, projective-plane split-graph, incidence, minimum-rank, and zero-forcing formulations did not locate the polynomial, the rank-
\\(13\\) theorem, or the \\(254\\)-orbit classification above.

A previous finite computation at field order \\(2\\) is a different parameter instance and does not imply the ternary polynomial or its projective symmetry census. Prior general results on domination of subspace-intersection graphs concern a different invariant.

## Limitations

The theorem is only for \\(V=\\mathbb F_3^3\\). No formula for arbitrary field order or arbitrary dimension is claimed.

The \\(254\\)-orbit statement is under the natural \\(\\operatorname{PGL}(3,3)\\)-action. It does not claim that this is the full automorphism group of the split graph.

The complete polynomial and orbit decomposition rely on exhaustive finite enumeration, supplied as reproducible code and output. The minimum-size equality itself has an independent symbolic rank lower bound and an explicit forcing witness.

The first-public-date field uses the earliest exact public day verified for a source materially used here. An earlier 2012 journal article on the same graph family was located with month-level issue evidence but without a verified first-public day; no day is invented from that evidence.

## References

1. S. Akbari, H. A. Tavallaee, and S. Khalashi Ghezelahmad, “Intersection Graph of Submodules of a Module,” *Journal of Algebra and Its Applications* 11 (2012), 1250019. DOI: 10.1142/S0219498811005452.
2. E. Yaraneri, “Intersection Graph of a Module,” *Journal of Algebra and Its Applications* 12 (2013), 1250218. arXiv:1208.1897; DOI: 10.1142/S0219498812502180. First arXiv submission 9 August 2012.
3. N. Jafari Rad and S. H. Jafari, “A Note on the Intersection Graph of Subspaces of a Vector Space,” *Ars Combinatoria* 125 (2016), 401–407.
4. AIM Minimum Rank — Special Graphs Work Group, “Zero forcing sets and the minimum rank of graphs,” *Linear Algebra and its Applications* 428 (2008), 1628–1648. DOI: 10.1016/j.laa.2007.10.009.
5. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, and C. Reinhart, “The zero forcing polynomial of a graph,” *Discrete Applied Mathematics* 258 (2019), 35–48. arXiv:1801.08910.
