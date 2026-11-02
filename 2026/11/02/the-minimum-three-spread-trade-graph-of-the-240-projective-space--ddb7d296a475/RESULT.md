# The minimum three-spread trade graph of the 240 projective-space packings

## Finding

Let \(\Pi=\operatorname{PG}(3,2)\), the three-dimensional projective space over the two-element field. A spread is a five-element family of pairwise skew lines partitioning the 15 points. A packing (also called a line parallelism) is an unordered family of seven spreads partitioning all 35 lines. For packings \(P,Q\), define their trade size by \(\tau(P,Q)=7-|P\cap Q|\), using common *whole spreads* rather than common individual lines. For \(r\ge1\), the exact-\(r\) trade graph joins distinct packings with \(\tau(P,Q)=r\).

**Theorem.** Exactly 240 packings exist. Any distinct packings have trade size at least three. The exact-three-trade graph \(\mathcal T_3(\Pi)\) is a connected bipartite 7-regular graph on 240 vertices with 840 edges, girth six and diameter five. From every starting packing the numbers of packings at distances \(0,1,2,3,4,5\) are exactly
\[
(1,7,42,105,77,8).
\]
Moreover, in a classical presentation using an eight-symbol set \(X\), a packing is represented by a Fano triple system on seven of the eight symbols. Its seven three-trade neighbors are exactly the transpositions of the unused symbol with each used symbol. The two bipartition classes have 120 vertices each and are the two parity classes of the corresponding \(S_8\) coset action.

The static counts and classical eight-label correspondence are historical inputs, not newly claimed results. The new content is the complete *smallest-possible trade* rule, its global connectivity and exact metric.

## Assumptions and scope

Throughout, packings and spreads are **unordered** subsets, and a move replaces *exactly three distinct entire spreads*, not three projective lines, while remaining a packing. The space has exactly 15 points and 35 distinct lines; the result makes no assertion for other finite fields or higher dimensions.

For an eight-element label set \(X\), model the 35 projective lines by unordered complementary partitions \(\{Q,X\setminus Q\}\) with \(|Q|=4\). For each \(T\in\binom X3\), define its five-line spread
\[
S(T)=\{\{T\cup\{x\},X\setminus(T\cup\{x\})\}:x\in X\setminus T\}.
\]
The known identification of these 56 objects with the 56 spreads of \(\operatorname{PG}(3,2)\) is given by Bussemaker and Seidel, Theorem 5.2, and reiterated in Green, Section 2. It is used here as a geometric correspondence, not a proposed discovery.

## Proof

**1. The eight-symbol classification.** By direct consideration of complementary four-subsets, two distinct spreads \(S(T)\) and \(S(U)\) are disjoint if and only if \(|T\cap U|=1\). Indeed, shared partitions occur when their three-subsets lie on the same or complementary sides of a four-plus-four split. Their intersection count is zero exactly for intersection size one; it is one for intersection size two and two for disjoint three-subsets. Thus a packing is a family \(\mathcal F\) of seven three-subsets of \(X\) that pairwise meet in exactly one label; its disjoint seven spreads then cover all \(7\cdot5=35\) lines.

Let \(d_x\) be the number of triples of \(\mathcal F\) containing \(x\). If four triples contained one label, their other pairs would have to be disjoint and would require eight other symbols, although only seven exist. Hence \(d_x\le3\). Counting block incidences and pairs of blocks gives
\[
\sum_{x\in X}d_x=21,\qquad \sum_{x\in X}\binom{d_x}{2}=\binom72=21.
\]
It follows that \(\sum_xd_x(d_x-3)=0\). Since all summands are nonpositive, every \(d_x\) is zero or three, and exactly seven labels have degree three. Any two of those seven labels occur in exactly one triple, because the three triples through each one have pairwise disjoint other-label pairs. The seven triples therefore form a Steiner triple system \(\mathrm{STS}(7)\), the unique Fano plane, with exactly one label omitted. Conversely, each Fano plane on any seven-subset of \(X\) gives seven mutually disjoint spreads, hence a packing. As the Fano plane has automorphism group of order 168, there are \(8\cdot7!/168=240\) packings.

**2. Seven explicit three-trades.** In a labelled Fano plane \(F\) with omitted symbol \(z\), fix one used symbol \(y\). There are precisely three Fano triples containing \(y\). The transposition \((z\,y)\) fixes the other four triples and replaces those three by triples containing \(z\), so produces a valid packing at trade size exactly three. Varying \(y\) gives seven distinct neighbors. These moves generate a connected graph: all Fano labellings form the transitive \(S_8\)-orbit of one Fano plane, and transpositions between the current omitted symbol and any other symbol are the usual star-transposition generators, which generate \(S_8\).

For bipartiteness, the Fano automorphism subgroup \(\operatorname{GL}(3,2)\) lies in \(A_8\). One elementary reason is that the elementary transvections generating \(\operatorname{GL}(3,2)\) induce two disjoint transpositions on the seven nonzero three-vectors and hence are even. Accordingly, the parity of an eight-symbol permutation carrying a fixed reference packing to a given packing is well-defined. Every displayed three-trade changes it, and transitivity makes each class of size 120.

**3. Exclusion of other trades and exact metric.** The following fully finite, exhaustive incidence certificate determines all possible exchange edges and distances. The standalone program `verify_projective_exact_cover.py` constructs the 35 distinct projective lines as \(\{a,b,a\oplus b\}\) for \(1\le a<b\le15\), enumerates all partitions of the 15 points by disjoint lines, obtaining exactly 56 spreads, and then enumerates all partitions of the 35 lines by disjoint spreads, obtaining exactly 240 packings. Each recursion always selects the least uncovered incidence element, so every completion occurs, with no unexamined cases. It compares all \(\binom{240}{2}=28{,}680\) unordered pairs. The counts of pairs sharing \(0,1,2,3,4\) entire spreads are respectively
\[
(13560,8400,5040,840,840),
\]
and no two different packings share five, six, or seven spreads. Thus no trade of size one or two exists; exactly \(840\) unordered pairs admit a three-trade; each packing has exactly seven such partners. Consequently the seven symbol transpositions in step 2 are **all** valid minimum trades, not merely some of them.

The same program reconstructs the entire 240-by-240 adjacency relation, performs breadth-first search from **every** packing, and verifies the distance distribution \((1,7,42,105,77,8)\). In particular the graph is connected and has diameter exactly five. It checks that adjacent vertices have opposite BFS parity and that any pair of distinct vertices has at most one common neighbor. Hence triangles and quadrilaterals do not occur. A six-cycle does exist: every vertex has seven neighbors and 42 vertices at distance two, but just 105 at distance three; the 42 distance-two vertices have \(42\cdot6=252\) outward edges, so at least two such outward edges land at the same distance-three vertex, creating a length-six closed walk whose absence of triangles and quadrilaterals forces a six-cycle. Therefore the girth equals six. Finally \(240\cdot7/2=840\) edges.

**4. Independent representation check.** The second standalone program `verify_fano_cosets.py` constructs all 35 complementary four-subset partitions, all 56 five-line spreads, and the 30 distinct labelled Fano systems on each of eight choices of omitted label. It checks that each of the resulting 240 families covers precisely the 35 lines; verifies the exact correspondence between *all* common-four-spread pairs and the seven star-transposition images; and independently runs all-root shortest paths. It also checks permutation parity over all \(8!=40{,}320\) eight-label permutations. Both exact finite constructions produce the stated graph and metrics. This is a complete finite decision procedure for this one projective space, not extrapolation from numerical samples.

## Verification

Both certificate scripts require only Python's standard library. Execute `python verify_projective_exact_cover.py` and `python verify_fano_cosets.py` from the directory containing these files. Their successful completion prints the distinct success labels documented in `VERIFICATION.md`; all assertions are required. The algorithms use exhaustive exact-cover recursion and exact finite permutations, not random sampling, floating-point approximations, or timeout-based inference.

## Relationship to prior work

The eight-symbol model of the 56 spreads comes from Bussemaker and Seidel (1970), Theorem 5.2. Historical accounts and Soicher's partial-spread classifications and Betten's publicly uploaded 2015 study supply the finite-geometry setting. The static enumeration and two collineation orbits of the 240 packings are established in the literature and independently revisited by Magaud (2021, 2022). Green's 2025 preprint explicitly represents packings as eight-labelled Fano planes and studies transposition actions and a different Bruhat-like partial order; the present proof does **not** claim those representations or actions as new. We inspected its Sections 1–4 and the related discussion of disjointness in Section 6. Its propositions on permutations do not give the exact geometric three-spread trade relation or the complete all-source shortest-path counts \((1,7,42,105,77,8)\). The novel assertion is specifically the minimum-trade graph and its complete metric; a group action alone is not a diameter statement.

## Limitations

The result is restricted to the 240 labelled packings of \(\operatorname{PG}(3,2)\) and to trades of **three whole spreads**. The exact metric is established by auditable finite enumeration, not a closed-form formula for an infinite family. An older study of special line sets in the same projective space (Jeurissen, 1995) was not available in full, leaving a historical possibility that equivalent reconfiguration facts appear there or under other terminology. The historical report is dated only by month (July 1970), and Soicher's 2000 date describes the state of a classification, not a verified first public release. The exact `2015-04-13` source date is the dated public full-text upload of Betten's 2015 study explicitly discussing these packings, not a claim that the topic first appeared then. Independent scholarly review has not occurred.

## References

1. F. C. Bussemaker and J. J. Seidel, *Symmetric Hadamard Matrices of Order 36*, TH Report 70-WSK-02, July 1970, Theorem 5.2. https://pure.tue.nl/ws/files/1804543/252823.pdf
2. L. H. Soicher, *Computation of Partial Spreads*, projective-geometry classification recorded **as of 10 August 2000**, without an independently verified publication day. https://webspace.maths.qmul.ac.uk/l.h.soicher/partialspreads/
3. A. Betten, *The Packings of PG(3,3)*, full text publicly uploaded 13 April 2015, which records background on packings of the binary projective three-space. https://www.researchgate.net/publication/274837528_The_packings_of_PG33
4. N. Magaud, *Spreads and Packings of PG(3,2), Formally!*, 2021, https://doi.org/10.4204/EPTCS.352.12
5. N. Magaud, *Proof Pearl: Formalizing Spreads and Packings of the Smallest Projective Space PG(3,2)*, 2022, https://doi.org/10.4230/LIPIcs.ITP.2022.25
6. R. M. Green, *A Partial Order on the 240 Packings of PG(3,2)*, arXiv:2511.03040, first posted 4 November 2025. https://arxiv.org/abs/2511.03040
7. R. H. Jeurissen, *Special Sets of Lines in PG(3,2)*, Linear Algebra and its Applications 226–228 (1995), 617–638, https://doi.org/10.1016/0024-3795(95)00200-B (full text not examined).
