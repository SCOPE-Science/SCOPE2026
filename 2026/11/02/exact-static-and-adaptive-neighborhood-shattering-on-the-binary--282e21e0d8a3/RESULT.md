# Exact static and adaptive neighborhood shattering on the binary 35-line Grassmann graph

## Finding

Let \(V=\mathbb F_2^4\), and let \(\mathscr L\) consist of its 35 two-dimensional linear subspaces. The binary Grassmann graph \(G=J_2(4,2)\) has vertex set \(\mathscr L\), with distinct vertices adjacent precisely when their intersection has dimension one. Define the Boolean open-neighborhood concept class
\[
\mathcal H=\big\{N_G(U):U\in\mathscr L\big\},
\]
where the query associated with \(W\in\mathscr L\) asks whether \(W\in N_G(U)\). Then
\[
\boxed{\operatorname{VCdim}(\mathcal H)=4,\qquad\operatorname{Ldim}(\mathcal H)=5.}
\]
Exactly 41,160 of the 52,360 four-query supports are VC-shattered, and none of the 324,632 five-query supports is shattered. A complete adaptive-shattering tree of depth five exists and is witnessed by 32 distinct concepts.

The graph is strongly regular with parameters \((35,18,9,9)\). This is the first strict static/adaptive separation along the rank-two binary Grassmann series: the rank-two graph over \(\mathbb F_2^3\) is complete on seven vertices, with both dimensions one; the graph over \(\mathbb F_2^2\) is a single isolated vertex, with both dimensions zero.

## Assumptions and scope

All subspaces are **linear** (not affine) and all neighborhoods are **open** (the center is excluded). The domain of allowable queries and the set of possible concepts are each exactly the 35 lines. For \(U\ne W\), their intersection is either the zero subspace or a one-dimensional subspace; the query returns one in the latter case and zero otherwise. No claim is made about the exact dimensions for higher ambient dimensions or larger finite fields.

A nonzero vector in \(\mathbb F_2^4\) is encoded by an integer from 1 through 15, with bitwise exclusive OR as vector addition. A two-dimensional subspace is encoded by its sorted triple of nonzero vectors \((a,b,a\oplus b)\). Sort all 35 distinct triples lexicographically, and number them from 0 through 34. Both supplied certificates use this canonical indexing.

## Proof

**Subspace enumeration and incidence.** Every two-dimensional binary subspace has exactly three nonzero elements. Choosing distinct nonzero vectors \(a,b\) produces exactly that subspace with nonzero triple \(\{a,b,a\oplus b\}\); each subspace is produced by six ordered generator pairs. There are \(15\cdot14/6=35\) distinct subspaces. Two different triples describe intersecting lines precisely when they share a nonzero vector. The checker constructs the complete Boolean adjacency matrix from these rules, confirms the number of distinct subspaces, checks the absence of diagonal adjacency, and confirms the regularity and common-neighbor parameters. These tests verify the finite object rather than assume a separately supplied graph matrix.

**VC lower bound.** The four query lines with canonical indices \((0,1,3,7)\) are shattered. The sixteen center indices, ordered by the binary response mask from \(0000\) to \(1111\), are explicitly stored in `grassmann35_cert.json`. The verifier constructs the graph independently and checks all sixteen responses against the corresponding centers, establishing \(\operatorname{VCdim}(\mathcal H)\ge4\).

**VC upper bound.** For every one of the \(\binom{35}{5}=324632\) five-element query sets \(S\), form the trace \(\big(N_G(U)\cap S\big)_{U\in\mathscr L}\). The standalone checker enumerates all 35 centers and verifies that the resulting collection contains fewer than \(2^5=32\) distinct response masks. This is a *complete finite enumeration* of the query supports, not a random sample. Therefore no five-query support is shattered; a shattered larger support would contain a shattered five-query subset, giving \(\operatorname{VCdim}(\mathcal H)\le4\). The four-support census finds exactly 41,160 shattered sets among the \(\binom{35}{4}=52360\) possibilities.

**Adaptive lower bound.** The certificate also contains a full depth-five binary decision tree. Its 31 internal nodes each specify one line-query index; its 32 leaves each specify a center-line index. For each root-to-leaf path, `verify_grassmann35.py` recomputes all incidence answers from the binary subspaces, checks they equal the prescribed branch labels, and verifies that the leaf centers are pairwise distinct. Hence all 32 possible answer histories are realized and \(\operatorname{Ldim}(\mathcal H)\ge5\).

**Adaptive upper bound.** A deterministic Boolean concept follows one path in a given adaptive query tree. Consequently, all \(2^d\) leaves of a shattered depth-\(d\) tree require distinct concepts. Since there are exactly 35 distinct open-neighborhood concepts and \(35<2^6\), there cannot be a shattered tree of depth six. Hence \(\operatorname{Ldim}(\mathcal H)\le5\).

**Boundary cases.** Over \(\mathbb F_2^3\), distinct two-dimensional subspaces meet in dimension one, so the graph is \(K_7\), with co-singleton neighborhoods. Each query has a negative branch containing just one concept, ruling out depth two; two query points cannot be VC-shattered because the joint negative response is impossible. Both dimensions equal one. Over \(\mathbb F_2^2\), the only rank-two subspace gives an empty neighborhood and both dimensions zero.

## Verification

The files `grassmann35_cert.json` and `verify_grassmann35.py` are a complete reproducible finite certificate. In the same directory, run `python verify_grassmann35.py` using a standard-library Python 3 interpreter. The program independently constructs the 35 subspaces and their 35-by-35 adjacency relation, checks 16 static witnesses, exhausts all 52,360 four-query and 324,632 five-query supports, and checks each of the 32 paths through the depth-five adaptive tree. Its expected exact output appears in `verification_stdout.txt`.

The finite exhaustive program is used as a proof of the VC upper bound; no unbounded extrapolation is made. The adaptive upper bound is a direct cardinality argument. A human-independent scientific audit has not been conducted.

## Relationship to prior work

Adler, Benediktsson and Macpherson (arXiv:2007.16042, first public 2020-07-31) proved VC-dimension bounds for ordinary Johnson and Hamming graph neighborhood families, not this finite-field Grassmann graph. The binary Grassmann graph here is a \(q\)-analogue of a Johnson graph, not an ordinary Johnson graph nor an induced subgraph of one identified by that paper. Their proof and theorems do not supply the present VC census or adaptive decision tree.

Liang, Tan and Koolen (2021, DOI 10.37236/10586) examine when sufficiently large-diameter distance-regular graphs with Grassmann parameters are identifiable as Grassmann graphs. Their main hypothesis includes Grassmann rank at least thirteen for the binary case, whereas the present graph has rank two; their object definition is relevant but their main theorem is not a statement about neighborhood shattering.

Byrne, Byrne and Cioabă (arXiv:2609.10330, public 2026-09-09) study VC dimension in strongly regular graphs and explicitly cover all such graphs through 28 vertices, while this graph has 35. Their abstract also describes bounds in terms of the smallest eigenvalue, so a more general implication for the VC portion remains a historical-priority risk. The full preprint was not accessible during the comparison; no assertion of complete noncoverage is made. The present joint static/adaptive assertion includes an explicit depth-five online certificate, absent from the accessible statements of those sources.

## Limitations

This is an exact finite result for a canonical 35-concept family, not a classification of all Grassmann graphs. Exhaustive checking of 324,632 supports relies on the correctness of the supplied short program and its specified arithmetic, not on a separately formalized proof assistant. The compiled concept table is not assumed: it is reconstructed from field operations. Searches do not establish absolute historical originality, and one relevant newer preprint's full text was inaccessible. Independent audit remains unperformed.

## References

1. I. Adler, B. G. Benediktsson and D. Macpherson, *Vapnik–Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042 (first posted 2020-07-31), https://arxiv.org/abs/2007.16042.
2. X. Liang, Y.-Y. Tan and J. H. Koolen, *Thin Distance-Regular Graphs with Classical Parameters ... Are the Grassmann Graphs*, Electronic Journal of Combinatorics 28(4), P4.45 (2021), DOI:10.37236/10586, https://www.combinatorics.org/ojs/index.php/eljc/article/view/v28i4p45.
3. I. Byrne, J. Byrne and S. M. Cioabă, *The VC-dimension of strongly regular graphs*, arXiv:2609.10330 (first posted 2026-09-09), https://arxiv.org/abs/2609.10330.
