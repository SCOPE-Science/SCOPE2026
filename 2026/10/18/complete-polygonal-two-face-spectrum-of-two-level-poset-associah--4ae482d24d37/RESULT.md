# Complete polygonal two-face spectrum of two-level poset associahedra

## Finding
Let \(P_{p,q}\) be the ordinal sum of two nonempty antichains, of cardinalities \(p\) and \(q\). Put \(n=p+q\ge4\), and let \(\mathscr A(P_{p,q})\) denote the simple poset associahedron in the sense of Galashin (equivalently the combinatorial type realized by Sack). It has dimension \(d=n-2\). Write \(F_j(p,q)\) for its number of two-dimensional faces with exactly \(j\) vertices. Let
\[
 V=pq(n-2)!.
\]
**Complete polygon spectrum theorem.** Every two-face has exactly four, six, or eight vertices, and for all \(p,q\ge1\) with \(n\ge4\),
\[
\begin{aligned}
 F_4(p,q)&=\binom{n-3}{2}\,\frac{V}{4},\\
 F_6(p,q)&=(n-4)\frac{V}{6}
 +\left[p\binom q3+q\binom p3\right](n-4)!,\\
 F_8(p,q)&=\binom p2\binom q2(n-4)!,\\
 F_j(p,q)&=0\quad\text{for }j\notin\{4,6,8\}.
\end{aligned}
\]
Here \(\binom ab=0\) for integer \(b>a\). In particular, octagonal two-faces exist **if and only if** \(p,q\ge2\), and their exact multiplicity is \(\binom p2\binom q2(n-4)!\). Thus each genuine two-level biclique-poset associahedron, with both level sizes at least two, is not combinatorially equivalent to a generalized permutohedron: generalized permutohedra have no polygonal two-faces with more than six edges.

The 2-dimensional examples are \(\mathscr A(P_{1,3})\), a hexagon, and \(\mathscr A(P_{2,2})\), an octagon. At \((p,q)=(2,3)\), the three-dimensional polytope has nine square, eight hexagonal, and three octagonal facets; their counts sum to twenty. At \((p,q)=(4,4)\), its two-face spectrum is \((F_4,F_6,F_8)=(28800,8448,864)\).

## Assumptions and scope
The poset has lower elements \(A\) and upper elements \(B\) with \(|A|=p\), \(|B|=q\), no relations within each level, and every element of \(A\) below every element of \(B\). The two-face counts refer to the abstract face lattice, not Euclidean shape or regularity. Galashin's poset associahedron is important here: other polytopes named poset associahedra have different tube definitions and must not be substituted. We assume \(n\ge4\) so that the two-face notion is nondegenerate. Factorials and binomial coefficients have their standard exact integer meanings.

## Proof
**1. Identify the tubes.** Galashin's proper tubes are the connected, order-convex proper subsets containing at least two labels. In \(P_{p,q}\), a subset is connected with at least two points exactly when it meets both levels. Every such subset is order-convex, because the poset has height two. Thus the proper tubes are exactly the mixed subsets of sizes \(2,\ldots,n-1\). If two mixed tubes are disjoint, each contains a lower and an upper element. Galashin's directed tube graph then contains an arrow in both directions between them, violating its acyclicity condition. Hence two tubes can occur together precisely when they are nested: proper tubings are exactly strict chains of mixed proper subsets.

**2. Identify vertices and faces.** The associahedron is simple of dimension \(d=n-2\), with a codimension-\(k\) face for each tubing containing \(k\) proper tubes. A maximal chain must use every subset cardinality \(2,3,\ldots,n-1\). Its first member is a pair \(\{a,b\}\) with \(a\in A\), \(b\in B\); thereafter the remaining \(n-2\) labels may be inserted in arbitrary order. Therefore it has exactly \(V=pq(n-2)!\) vertices. Every two-face corresponds to a chain of \(d-2=n-4\) tubes, obtained from any containing maximal chain by omitting exactly two of the ranks \(2,\ldots,n-1\). The number of vertices on that two-face equals the number of maximal chains extending its fixed subchain.

**3. Two omitted nonadjacent ranks.** If ranks \(r<s-1\) are absent, each missing rank other than rank two sits between fixed neighboring subset sizes differing by two, and there are two possible intermediate subsets. When the lower omitted rank is two, there is no rank-one tube: the fixed three-element mixed set contains exactly two admissible mixed two-subsets, because its level composition is necessarily \((1,2)\) or \((2,1)\). Thus there are again exactly two choices for the first gap. The choices at the two separated gaps are independent. Each such two-face is a quadrilateral. There are \(\binom{n-3}{2}\) unordered nonadjacent pairs among the \(n-2\) ranks. Every vertex belongs to precisely one two-face of each chosen omitted-rank type; each quadrilateral is incident to four vertices. Double-counting these incidences yields \(F_4=\binom{n-3}{2}V/4\).

**4. Two adjacent ranks away from the bottom.** If omitted ranks are \(r,r+1\) with \(r\ge3\), the surrounding fixed sizes are \(r-1\) and \(r+2\), differing by three labels, which may be inserted in \(3!=6\) orders. Thus this is a hexagon. There are \(n-4\) choices of such consecutive rank pairs. Double-counting vertex–two-face incidences yields \((n-4)V/6\) hexagons of this kind.

**5. The initial rank pair.** For the omitted ranks \(2,3\), the first fixed four-element set \(S\) must be mixed. If \(n=4\), interpret it as the complete ground set (which is not itself a proper tube), and the same counting applies. Suppose \(|S\cap A|=a\), \(|S\cap B|=b\), so \(a+b=4\) and \(a,b\ge1\). A maximal chain below \(S\) chooses its first mixed two-element subset in \(ab\) ways, then inserts the other two labels in either order, giving \(2ab\) vertices on the corresponding two-face. For \((a,b)=(1,3)\) or \((3,1)\) this is a hexagon; for \((a,b)=(2,2)\) it is an octagon. There are \(p\binom q3+q\binom p3\) ways to choose a mixed four-set of the former type, and \(\binom p2\binom q2\) of the latter. A fixed four-set extends through ranks \(5,\ldots,n-1\) in exactly \((n-4)!\) ways. This gives the remaining claimed hexagon count and all octagons. The three cases exhaust all pairs of omitted ranks, proving the displayed spectrum.

**6. Generalized-permutohedron obstruction.** Any generalized permutohedron in type \(A\) has every edge parallel to a root \(e_i-e_j\). The root directions lying in a fixed two-dimensional linear subspace form at most the six directions of an \(A_2\) subsystem, or four of an \(A_1\oplus A_1\) subsystem. A convex polygon has at most one edge for each directed ray (consecutive collinear edges coalesce into a single edge), so its number of sides is at most six. The strictly positive octagon count when \(p,q\ge2\) excludes even combinatorial equivalence with any generalized permutohedron.

## Verification
The supplied standalone `verify.py` enumerates every maximal tube chain directly for all 25 ordered pairs \((p,q)\) with \(p,q\ge1\) and \(4\le p+q\le8\). It deletes each pair of ranks, groups the resulting subchains, counts the distinct maximal completions in every group, and compares the observed complete polygon spectrum with the closed formulas. This independent finite recomputation checked 216,147 different polygon faces, and all 25 parameter pairs passed. The code uses only Python's standard library. Run `python3 verify.py`; the terminal marker is `VERIFY_OK`. This is a finite cross-check; the all-parameter assertion follows from the preceding combinatorial proof.

## Relationship to prior work
Galashin, *Poset associahedra* (arXiv:2110.07257, first publicly posted 2021-10-14), establishes the exact tube and tubing definitions and the simple-polytope face correspondence used here. Sack, *A realization of poset associahedra* (arXiv:2301.11449, first publicly posted 2023-01-26), constructs a realization and, in the FPSAC 2023 extended abstract Section 5.1, gives descent enumerators for the \(h\)-vector of the complete bipartite-height-two family. Those existing face-count and \(h\)-vector results are not presented as new. An unrefined face vector determines only the sum of the three polygon counts; the simple-polytope incidence identity gives their vertex-weighted sum, but leaves an octagon-frequency degree of freedom. The new assertion is the full **polygon-type refinement** of the two-face count for all part sizes, including the exact octagon multiplicity and the complete exclusion of other polygon sizes.

An older construction with the similar name *Convex polytopes from nested posets* (2015) is explicitly distinguished by Galashin (Remark 1.4). Its examples include octagonal faces in a different family, so octagons as a phenomenon are not claimed to be newly discovered here. They do not supply the present all-parameter Galashin-type polygon spectrum. The complete-bipartite *graph* associahedron is also a different polytope from the complete-bipartite-*poset* associahedron and cannot serve as a covering identity. No previously published exact all-parameter square/hexagon/octagon formulas for this family were identified in the checked records, but terminology-based bibliographic omissions remain possible.

## Limitations
This is a two-face combinatorial classification for complete two-level posets, not a formula for polygon side lengths, Euclidean areas, all face types, or arbitrary posets. The finite checker is not an exhaustive proof beyond \(n=8\). Galashin's theorem supplies the existence of the relevant simple polytopes; this work supplies a closed combinatorial refinement, not a new realization. Independent peer evaluation and an exhaustive global novelty search have not been performed.

## References
1. Pavel Galashin, *Poset associahedra*, arXiv:2110.07257 (first public 2021-10-14), particularly Definition 1.1, Theorem 1.2, and Remark 1.4. https://arxiv.org/abs/2110.07257
2. Andrew Sack, *A realization of poset associahedra*, arXiv:2301.11449 (first public 2023-01-26). https://arxiv.org/abs/2301.11449
3. Andrew Sack, *A realization of poset associahedra*, FPSAC 2023 extended abstract, Section 5.1. https://www.mat.univie.ac.at/~slc/wpapers/FPSAC2023/24.pdf
4. Satyan L. Devadoss et al., *Convex polytopes from nested posets*, European Journal of Combinatorics 43 (2015), 229–248, DOI 10.1016/j.ejc.2014.08.018. The construction is different from Galashin's.
