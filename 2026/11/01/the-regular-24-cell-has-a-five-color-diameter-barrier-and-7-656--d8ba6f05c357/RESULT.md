# The regular 24-cell has a five-color diameter barrier and 7,656 optimal triangular partitions

## Finding

Let \(V\subset\mathbb R^4\) be the 24 vertices of the regular 24-cell in the root-system normalization
\[
V=\{\varepsilon e_i+\delta e_j:1\leq i<j\leq4,\ \varepsilon,\delta\in\{-1,1\}\}.
\]
For every integer \(k\geq1\), let \(\beta_k(V)\) be the minimum, over partitions of \(V\) into at most \(k\) nonempty subsets, of the largest class diameter divided by \(\operatorname{diam}(V)\). Then
\[
\boxed{\beta_k(V)=\begin{cases}
1,&k=1,\\
\sqrt3/2,&2\leq k\leq4,\\
1/\sqrt2,&5\leq k\leq7,\\
1/2,&8\leq k\leq23,\\
0,&k\geq24.
\end{cases}}
\]
In particular, the diameter-threshold graph forbidding inner products \(\langle u,v\rangle<0\) has chromatic number exactly **five**, although its largest independent set has six vertices, so a cardinality bound alone allows four colors.

Moreover, exactly **7,656 unordered partitions into eight sets** attain the optimal ratio \(\beta_8(V)=1/2\). Each class is necessarily the vertex triple of one of the 96 triangular faces. To refine this count, call a triangular face a *signed-coordinate star* when its three roots share a common nonzero signed coordinate, and a *signed-coordinate cycle* otherwise. If \(N_j\) is the number of these partitions having exactly \(j\) star classes in the displayed coordinate realization, then
\[
\boxed{\sum_{j=0}^8N_jz^j=8+2848z^4+4480z^6+320z^8.}
\]
The decomposition by star count is relative to the displayed signed-coordinate realization; the total of 7,656 is an isometry-invariant count.

## Assumptions and scope

All distances are Euclidean. The vertex set is finite, with no repeated roots. The zero-diameter singleton convention is used. A partition may have fewer than \(k\) nonempty classes, equivalently allowing empty classes in a \(k\)-tuple. Partitions counted in the second assertion are **unlabeled**, have exactly eight nonempty classes, and are counted once regardless of the order of the classes. The statement concerns vertices, not all points of the solid 24-cell, and uses the stated edge-length normalization \(\sqrt2\) and diameter \(2\sqrt2\).

## Proof

**1. Four distance shells.** Every root has squared norm \(2\). For distinct roots \(u,v\), the dot product lies in \(\{-2,-1,0,1\}\). Consequently
\[
\|u-v\|^2=4-2\langle u,v\rangle\in\{8,6,4,2\}.
\]
An admissible diameter bound is therefore equivalent to coloring one of four graphs defined by the forbidden dot-product thresholds. For a maximum squared diameter \(6\), only the twelve antipodal pairs must be separated, so two classes are necessary and sufficient. For maximum squared diameter \(2\), classes must be pairwise-positive root sets. For maximum diameter zero, all vertices must be singletons.

**2. The non-obtuse six-vertex classes.** Write \(C_i^s=\{v\in V:v_i=s\}\) for \(i\in\{1,2,3,4\}\) and \(s\in\{-1,1\}\), and \(D_\sigma=\{v\in V:\langle v,\sigma\rangle=2\}\) for \(\sigma\in\{-1,1\}^4\). Each of these eight coordinate and sixteen diagonal sets has six elements, all pairwise dot products nonnegative. These are exactly the 24 six-element sets with this property, and none extends to seven elements. The finite classification is an exhaustive, 134,596-candidate elementary lemma: inspect every six-subset, checking its 15 inner products; the attached `verify.py` implements the full test, checks equality with the explicitly specified 24 sets, and verifies that none admits a seventh compatible root. Thus the independence number at threshold \(\langle u,v\rangle<0\) is exactly six.

If four colors sufficed at this threshold, all 24 roots would split into four disjoint classes of six, hence four pairwise disjoint sets from the list \(C_i^s,D_\sigma\). This is impossible for a structural reason. Two coordinate classes are disjoint only when they are \(C_i^+\) and \(C_i^-\); this opposite pair cannot both be disjoint from a diagonal class. Also, two diagonal classes are disjoint precisely when their sign vectors have Hamming distance at least three. Three binary strings of length four cannot have all three pairwise Hamming distances at least three: summed over the three pairs the required distance would be at least nine, while any one coordinate contributes at most two, giving at most eight. Thus a family of pairwise disjoint six-classes has size at most three.

Five classes do suffice. Choose any \(\sigma\in\{-1,1\}^4\). The five six-element sets
\[
C_1^{-\sigma_1},\ C_2^{-\sigma_2},\ C_3^{-\sigma_3},\ C_4^{-\sigma_4},\ D_\sigma
\]
cover \(V\): every root either has a coordinate opposite to \(\sigma\), or has both nonzero coordinates agreeing with \(\sigma\) and belongs to \(D_\sigma\). Resolving overlaps arbitrarily gives five disjoint admissible classes. Therefore the corresponding graph is five-chromatic, and squared diameter \(4\) is attainable exactly from five parts onward.

**3. Eight positive triples.** Two distinct roots have positive dot product only if their underlying two-coordinate supports intersect in one index with equal signs. There cannot be four pairwise-positive roots: their four distinct two-element supports would be pairwise intersecting edges of the complete graph on four coordinates, whereas a pairwise intersecting family of distinct edges has at most three members. Thus any diameter-\(\sqrt2\) class has at most three points, requiring at least eight classes.

For a matching upper bound, create one class for every signed coordinate \((i,s)\) (eight classes). Assign a root \(s e_i+t e_j\), \(i<j\), to \((i,s)\) if \(s=t\), otherwise to \((j,t)\). Every signed-coordinate class receives exactly one root from each of the other three coordinate positions. Its three roots share the same signed coordinate and are pairwise at distance \(\sqrt2\). This is an eight-class partition. It proves the remaining diameter threshold and the piecewise formula.

**4. Exact count of optimal eight-class partitions.** Eight classes of size at most three must each be a triple, and all pairs in a triple must have dot product \(1\). The three two-element supports of such a triple either form a three-edge star (a common signed coordinate), or a three-edge cycle (three supported coordinates with consistently chosen signs). There are \(8\cdot2^3=64\) star triples and \(\binom43\cdot2^3=32\) cycle triples, giving exactly 96 possible face triples.

Index the roots in the explicit lexicographic order in `verify.py`; represent each triple by its 24-bit occupancy mask. For a used-root mask \(M\), let \(v(M)\) be the least-indexed uncovered root; let \(\epsilon(T)\) be \(1\) for a star triple and \(0\) for a cycle. Define the polynomial
\[
F(M;z)=\sum_{T\ni v(M),\,T\cap M=\varnothing}z^{\epsilon(T)}F(M\cup T;z),\qquad F(V;z)=1.
\]
Every unordered exact cover has exactly one first triple containing the smallest uncovered vertex, so no labeling or multiplicity factor enters. The exhaustive integer recurrence visits 12,367 distinct masks and returns
\[
F(\varnothing;z)=8+2848z^4+4480z^6+320z^8.
\]
The provided standard-library verifier reconstructs all 96 triangles from integer dot products, checks both the structural lemmas and the coefficients, and needs no numerical tolerance, external table, or solver. The displayed recurrence covers all allowed triples, not a sampled subset.

## Verification

Execute `python3 verify.py` in a directory containing that file. It constructs all 24 integer roots, all six-element non-obtuse classes, all positive triangles, and the complete finite exact-cover recurrence. The recorded check passed: 24 six-classes, no extending seven-class, no four pairwise-disjoint six-classes, 96 allowed triangles (64 stars, 32 cycles), and the polynomial above with 7,656 total covers. An independent nonmemoized exact-cover recursion over the same 96 triangles also returned the same coefficient vector. The exact analytic geometric statements are justified in the proof; the only computation-dependent pieces are finite, completely enumerated claims.

## Relationship to prior work

Voronov (2026) formulates quantitative Borsuk diameter ratios through threshold-graph chromatic numbers and constructs a different 101-point counterexample in three dimensions, with additional examples in dimensions four through six. That work motivates exact benchmarks but supplies neither this 24-cell spectrum nor the triangular-partition count. Cohn, Conway, Elkies and Kumar (2006/2007) study the 24-cell as the \(D_4\) spherical code, including energy and design properties, but do not derive these partition invariants. Standard 24-cell tables give 24 vertices, 96 triangular faces and four nonzero distance shells; these data do not by themselves establish the five-color obstruction or the exact 7,656 decompositions. In particular, traditional decompositions into *great* triangles of longer edge length are not the edge-triangle partitions counted here.

## Limitations

Only the 24 **vertices** are classified; the optimum diameter for partitions of the full four-dimensional solid is not determined. The signed-coordinate refinement depends on the chosen root-system chart, though the total number of optimal unlabeled partitions is intrinsic. The novelty comparison addresses the primary sources and indexed mathematical results consulted, not every historical unpublished enumeration. The finite computation is independently replayable but has not received an independent mathematical audit.

## References

1. V. Voronov, *A counterexample to Gale's conjecture in R3*, first public 20 October 2026, arXiv:2610.28828, https://arxiv.org/abs/2610.28828.
2. H. Cohn, J. H. Conway, N. D. Elkies and A. Kumar, *The D4 root system is not universally optimal*, Experimental Mathematics **16** (2007), 313–320; arXiv:math/0607447, https://arxiv.org/abs/math/0607447.
3. E. W. Weisstein, *24-Cell*, MathWorld, https://mathworld.wolfram.com/24-Cell.html (standard geometric counts and coordinates).
4. F. Martinez-Figueroa, *Generalized Borsuk Graphs*, Discrete & Computational Geometry **72** (2024), 1377–1416, https://doi.org/10.1007/s00454-024-00695-1 (general chromatic-topological background; not an exact 24-cell spectrum).
