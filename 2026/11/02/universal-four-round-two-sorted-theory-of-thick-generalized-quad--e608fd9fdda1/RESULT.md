# Universal four-round two-sorted theory of thick generalized quadrangles and its first four-way split

## Finding
Let \(\mathcal Q=(P,L,I)\) range over **all finite thick generalized quadrangles** of order \((s,t)\), where \(s,t\ge2\), with no symmetry, classicality or transitivity assumption. Regard each quadrangle as a one-domain relational structure with unary predicates \(P,L\), distinguishing points and lines, and the binary point-line incidence predicate \(I\). Then any two such structures have the same first-order sentences of quantifier rank at most four:
\[
\boxed{\mathcal Q\equiv_4\mathcal Q'}.\tag{1}
\]
This is true even when their two order parameters differ, and even though the two sorts are explicitly named.

The stronger local type statement is exact. Across every such quadrangle, the numbers of complete ordered-tuple types at the indicated remaining quantifier ranks are:
\[
\begin{array}{c|rrrr}
\text{tuple length}&3&2&1&0\\
\text{remaining rank}&1&2&3&4\\
\text{number of types}&84&10&2&1.
\end{array}\tag{2}
\]
Here types include equality patterns, all possible sorts and incidences; the number is not restricted to injective tuples.

The uniform sentence-rank bound is sharp, and the **first visible parameter split has at least four branches**: rank-five sentences independently detect whether \(s\ge3\) and whether \(t\ge3\). All four Boolean combinations occur in finite thick generalized quadrangles. We do **not** claim that these four branches exhaust the rank-five classification.

## Assumptions and scope
The defining generalized-quadrangle axioms are: each line is incident with exactly \(s+1\) points, each point with exactly \(t+1\) lines; two points share at most one line, and two lines share at most one point; and for every nonincident pair \((p,\ell)\) there is a unique pair \((m,q)\) with \(p I m I q I \ell\). The parameters satisfy \(s,t\ge2\). Thus the incidence graph has girth eight, and the *collinearity* relation between distinct points means that a line contains both; the dual relation between distinct lines is *concurrency*.

The logical language consists only of equality, the two unary sort predicates, and incidence; there are no constants, built-in cardinality predicates, arithmetic operations, or functions. Quantifier rank is nesting depth. In formulas \(I(x,y)\) may be treated as symmetric across the two sorts; it is false on same-sort pairs. The two-sort formalism is equivalent to sorted first-order logic with explicit point and line sorts.

## Proof
**1. Geometry and the enriched diagram.** Enrich an ordered tuple of at most three selected elements, only for the purpose of analyzing types, by recording equality, sort and incidence, and additionally whether each distinct same-sort pair is collinear (for points) or concurrent (for lines). These extra pair relations are definable with one additional existential quantifier. Three distinct points are pairwise collinear if and only if they lie on one line: otherwise the three joining lines would form a forbidden six-cycle. Dually, three pairwise concurrent lines have one common point.

**2. A triple's rank-one type is exactly its enriched diagram.** A rank-one formula tests which atomic extensions by a fourth element are possible. For three distinct points, an additional line can be incident with a specified subset of the three. For a subset of size three, this occurs precisely when they are collinear on one line; for size two, precisely when the pair is collinear and the third point is off that unique line. A subset of size one is always achievable because the chosen point has \(t+1\ge3\) lines and at most two are forbidden by the other selected points. The empty subset is achievable since the total number of lines is \((t+1)(st+1)\), strictly larger than \(3(t+1)\). The dual assertion holds for three lines.

For two distinct points and one selected line, a new line through both points exists exactly when those points are collinear; whether this new line equals the selected line is already determined by the existing incidences. A new line through exactly one of the two points (different from any selected line) exists because \(t+1\ge3\), and a line through neither also exists by the same global count. A new point on the selected line, avoiding the two named points, always exists because \(s+1\ge3\); a fresh point off it also exists. Swap sorts for the case of two lines and one point. Choices equal to earlier variables are explicitly controlled by equality. Choices of the same sort as all three old variables can always be fresh. Therefore **every** atomic fourth-vertex mask is determined by the enriched diagram, uniformly in \(s,t\).

Conversely, equality, sorts and incidence are atomic, while an existential common incident element tests collinearity or concurrency for any same-sort pair within one quantifier. Hence the enriched diagram is exactly recoverable from the complete rank-one triple type.

**3. Pair-extension saturation is independent of both parameters.** Consider two distinct points \(p,q\), and let \(k=s(t+1)\) be the number of other points collinear with a given point. If \(p,q\) are collinear, the numbers of possible fresh points \(z\) that are respectively collinear with both, with \(p\) alone, with \(q\) alone, and with neither are
\[
 s-1,\qquad st,\qquad st,\qquad st(s-1).
\]
If they are noncollinear, those four numbers are
\[
 t+1,\qquad (s-1)(t+1),\qquad (s-1)(t+1),\qquad s^2t-st-s+t.
\]
All eight expressions are positive for \(s,t\ge2\). These formulas follow from the total point count \((s+1)(st+1)\), the point-collinearity degree \(s(t+1)\), and the common-neighbor counts \(s-1\) or \(t+1\). A new line can meet neither point, either point alone, or both precisely when the pair is collinear; the first three choices always exist because each point has \(t+1\ge3\) lines and the total number of lines exceeds \(2(t+1)\). The dual calculation handles two distinct lines.

For a mixed pair \((p,\ell)\), record whether they are incident. If they are incident, a fresh point on \(\ell\) must be collinear with \(p\), while a fresh point off \(\ell\) can be collinear or noncollinear with \(p\); all three permitted cases occur. Dually, a fresh line through \(p\) must meet \(\ell\), while a fresh line not through \(p\) can meet or miss \(\ell\). If \(p\) and \(\ell\) are nonincident, **all four combinations** of membership in \(\ell\) and collinearity with \(p\) are realized by a fresh point, and dually all four combinations of passage through \(p\) and concurrency with \(\ell\) are realized by a fresh line. Specifically, the unique projection point on \(\ell\) and its unique joining line realize one combination; the other \(s\) points of \(\ell\), the other \(t\) lines through \(p\), and the remaining vertices realize the other combinations. For instance, among points outside \(\ell\) that are noncollinear with \(p\) there are \(s(st-1)>0\) choices. All assertions also allow repetitions, whose diagrams are fixed by equality.

It follows that the set of all enriched triple diagrams extending a fixed ordered pair depends **only** on the enriched pair diagram, never on \(s,t\). By Step 2 and the rank-one-extension recursion, the same is true of its rank-two type. The enriched pair diagram is conversely determined by this rank-two type: equality, sorts and incidence are atomic, and collinearity/concurrency is witnessed by one existential variable. The ten possibilities are three ordered point-point statuses (equal, collinear, noncollinear), three line-line statuses (equal, concurrent, nonconcurrent), and two incidence statuses in each of the two ordered mixed-sort orientations. All ten occur in every thick generalized quadrangle.

**4. The type-count identity.** There are eight possible collinearity graphs on three labeled distinct points, and likewise eight concurrency graphs on three lines. For two distinct points and one line there are seven consistent enriched diagrams: four incidence masks when the points are collinear and three when they are not; the line can occupy any of the three tuple positions. The dual case contributes another \(3\cdot7\). Thus there are \(8+8+3\cdot7+3\cdot7=58\) distinct-variable triples. For a tuple with exactly two equal entries, there are three choices of the equality pair and eight choices of the enhanced status of its two distinct elements, contributing \(24\). All-equal tuples contribute two. Therefore there are exactly \(58+24+2=84\) rank-one ordered-triple types. The pair-extension analysis proves that every such diagram is realized in **each** quadrangle, not merely in a sample.

**5. Singleton and sentence types.** Fix a point. There are other collinear and noncollinear points (the latter numbering \(s^2t>0\)), and both incident and nonincident lines. By Step 3 these realize every relevant rank-two pair type. The analogous statement holds for any line by duality. Hence the rank-three type of a singleton depends only on whether it is a point or a line: two such types, common to all thick quadrangles. Each quadrangle contains both sorts, so its empty-tuple rank-four type is the same singleton set of these two rank-three types. The standard back-and-forth/type recursion now proves (1) and (2).

**6. Sharpness and the first parameter split.** Let \(\Theta_s\) assert that some line is incident with four *pairwise distinct* points; and let \(\Theta_t\) assert that some point is incident with four pairwise distinct lines. Each sentence has rank exactly five, because it existentially chooses the supporting line or point and the four witnesses. The generalized-quadrangle axioms give
\[
 \mathcal Q\models\Theta_s\iff s\ge3,\qquad
 \mathcal Q\models\Theta_t\iff t\ge3.
\]
Classical finite examples realize all four combinations: the symplectic quadrangles \(W(3,2)\) and \(W(3,3)\) have orders \((2,2)\) and \((3,3)\); the elliptic-quadric example \(Q^-(5,2)\) has order \((2,4)\), and its point-line dual has order \((4,2)\). These four are pairwise distinguishable by \(\Theta_s\) and \(\Theta_t\) at rank five, but none is distinguishable at rank four by (1). Thus rank four is the exact universal agreement depth, and at least four independent rank-five parameter patterns occur.

## Verification
The accompanying `generate.py` constructs the two finite symplectic models directly from an alternating form over fields of orders two and three, and an elliptic quadric over the binary field from a quadratic form of Witt index two. It also constructs its dual. Running `generate.py`, then compiling and executing `verify.cpp`, verifies all incidence axioms for four models of orders \((2,2),(3,3),(2,4),(4,2)\). The C++ verifier implements complete first-order back-and-forth signatures for tuples at lengths/ranks \((3,1),(2,2),(1,3),(0,4)\), preserving *both* sort predicates. It finds exactly \(84,10,2,1\) signatures respectively and one common rank-four sentence type. Its last check verifies that the two rank-five degree-threshold sentences produce all four Boolean patterns. The actual output is in `verification_output.txt`.

The finite checks are calibration and reproducibility evidence, **not** an infinite proof. The infinite proof is Steps 1–6, including the parameter-uniform existence and positivity arguments.

## Relationship to prior work
The defining incidence axioms and classical examples are documented in Thas' study of finite generalized quadrangles; general Ehrenfeucht–Fraïssé quantifier-rank methods are developed in Verbitsky's work and the established finite-model-theory literature. Neither inspected source states the uniform coloured, nonsymmetric four-round conclusion or the four-way first parameter split.

A previously available restricted result concerns only *uncoloured* incidence graphs of *symmetric* quadrangles, with \(s=t\). That statement cannot imply (1), which names point and line sorts and quantifies over every admissible unequal pair of parameters. In particular, the four models in Step 6 include two asymmetric geometries. The restricted distance-regular argument cannot simply be applied to their generally biregular incidence graphs; the present proof instead uses an explicit two-sort pair-extension analysis.

Published results on Vietoris–Rips complexes of generalized-quadrangle incidence graphs concern homotopy and persistence, not first-order formulas. The paper on projective-plane point–line geometries addresses generalized triangles rather than generalized quadrangles. Neither implies this logical classification. No assertion is made that a literature search proves uniqueness of this result.

## Limitations
This concerns ordinary first-order logic **without counting quantifiers** and rank at most four. The theorem does not classify rank-five theories: the two rank-five sentences establish only a lower bound of four distinct classes. The finite verifier covers four classical examples, not all generalized quadrangles, and the infinite result depends on the explicit geometric proof. The group-theoretic and automorphism classifications of quadrangles are not resolved or used. Equivalent work in unpublished, unindexed, or inaccessible literature remains possible. Independent scientific validation has not been performed.

## References
1. O. Verbitsky, *The First Order Definability of Graphs with Separators via the Ehrenfeucht Game*, arXiv:math/0401361, first public preprint 2004-01-26, https://arxiv.org/abs/math/0401361 .
2. K. Thas, *Determination of generalized quadrangles with distinct elation points*, Journal of Algebraic Combinatorics **24** (2006), 5–22, DOI 10.1007/s10801-006-9098-3, https://doi.org/10.1007/s10801-006-9098-3 .
3. S. E. Payne and J. A. Thas, *Finite Generalized Quadrangles*, first edition 1984, second edition 2009. The monograph was not fully inspected for this comparison.
