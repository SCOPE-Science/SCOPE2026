# A seven-petal trefoil requires a nine-petal detour
## Finding
Let \(\mathcal M=\{\mathsf T^{\pm},\mathsf X,\mathsf R,\mathsf S\}\) be the move set on petal words consisting of trivial petal addition/deletion, crossing exchange, cyclic rotation of heights, and the half-turn symmetry. For a knot \(K\), define the reduction excess of an \(N\)-petal representative \(p\) to be the least even integer \(E\ge 0\) for which \(p\) can be connected by \(\mathcal M\)-moves to a representative with \(p(K)\) petals while every intermediate word has at most \(N+E\) petals.

For the trefoil \(K\), the seven-petal word
\[
p=(0,2,4,6,1,3,5)
\]
has reduction excess exactly \(2\). Equivalently, it cannot be reduced to a minimum five-petal trefoil while staying at seven petals, but it can be reduced by a path whose largest word has nine petals. Therefore petal-diagram monotonic simplification can fail for a nontrivial knot, answering Question 7.4 of Vernitski affirmatively.

## Assumptions and scope
Petal words are taken up to cyclic shift of their positions, with the lexicographically smallest cyclic rotation used for display. The move definitions are exactly those in Vernitski's Section 3: \(\mathsf T^{\pm}\) changes the petal count by two, \(\mathsf X\) preserves the count, and \(\mathsf R,\mathsf S\) are petal-count-preserving isotopies.

The statement concerns the reduction problem for the particular trefoil representative above. It does not assert that every seven-petal trefoil is non-monotonically reducible, nor does it classify all nontrivial knots with this phenomenon.

The minimum petal number of the trefoil is \(5\). The source records the five-petal trefoil word \((3,1,4,2,0)\), cyclically equivalent to \((0,3,1,4,2)\). On the other hand, the only two three-petal words up to cyclic shift each have a trivial petal deletion to the one-petal unknot, so no nontrivial knot has a three-petal representative.

## Proof
Write
\[
p_7=(0,2,4,6,1,3,5).
\]
First, \(p_7\) has no trivial petal deletion: none of its cyclically adjacent letters are consecutive integers. Directly from the definitions,
\[
\mathsf R(p_7)=p_7,
\qquad
\mathsf S(p_7)=p_7
\]
after choosing the canonical cyclic rotation.

It remains to test crossing exchanges. For a seven-petal word, a crossing exchange is determined by a basepoint \(b\) and integers \(m,w\) with \(w\ge m+2\) and \(w+1\le6\). Exhausting all \(70\) such triples against the pair-partition and nesting condition in the definition of \(\mathsf X\) gives no legal crossing exchange for \(p_7\). The standalone verifier performs this finite check directly from the definition.

Consequently the entire component of \(p_7\) under the petal-count-preserving moves \(\mathsf X,\mathsf R,\mathsf S\) is the singleton \(\{p_7\}\), and no \(\mathsf T^-\) move is available there. Any path from \(p_7\) to a word with five petals must therefore use \(\mathsf T^+\) first and pass through at least nine petals. This proves the lower bound \(E\ge2\).

For the matching upper bound, use the explicit sequence
\[
(0,2,4,6,1,3,5)
\xrightarrow{\mathsf T^+}
(0,7,6,2,4,8,1,3,5)
\xrightarrow{\mathsf X(4,2,5)}
(0,7,5,3,4,8,1,2,6)
\xrightarrow{\mathsf T^-}
(0,5,3,1,2,6,4)
\xrightarrow{\mathsf T^-}
(0,3,1,4,2).
\]
The first arrow is the inverse of deleting the adjacent consecutive heights \(7,6\). For the crossing exchange, with basepoint position \(4\), the four paired value sets are \(\{8,1\},\{3,5\},\{0,7\},\{6,2\}\). Taking \(m=2\) and \(w=5\), the distinguished pairs are \(\{m,w+1\}=\{2,6\}\) and \(\{m+1,w\}=\{3,5\}\); the two remaining pairs are disjoint from the interval \([4,4]\). Thus the exchange is legal and swaps \(2\leftrightarrow3\) and \(5\leftrightarrow6\). The two final arrows are immediate trivial deletions.

The terminal word \((0,3,1,4,2)\) is a cyclic rotation of the source's displayed trefoil word \((3,1,4,2,0)\). Every arrow preserves knot type, so \(p_7\) is a trefoil. The path reaches the minimum petal number and never exceeds nine petals, proving \(E\le2\). Hence \(E=2\).

## Verification
The standalone program `artifacts/verify_trefoil_excess.py` implements the source's move definitions using exact integer and set operations. It verifies that \(p_7\) is fixed by \(\mathsf R\) and \(\mathsf S\), has no trivial deletion, and has no legal crossing exchange among all \(70\) admissible parameter triples. It then checks each step of the explicit nine-petal detour, replays the source's published crossing-exchange example as a regression test, and confirms that the two cyclic classes of three-petal words both delete to the one-petal unknot.

Its successful replay output is:

`VERIFY_OK candidate_x_triples=70 candidate_R=fixed candidate_S=fixed candidate_Tminus=none detour_max_petals=9 trefoil_petals=5 source_X_example=PASS`

The finite computation is exhaustive for the specific seven-petal word; it is not being extrapolated to other petal words or knots.

## Relationship to prior work
Vernitski introduces the monotonic-simplification problem for petal diagrams, proves that hard diagrams of the unknot first occur at nine petals, and ends with Question 7.4 asking whether an analogous obstruction occurs for a nontrivial knot. The paper supplies both the move set used here and the five-petal trefoil word, but it does not give a nontrivial-knot example answering that question.

Colton, Glover, Hughes, and Sandberg introduced trivial petal additions/deletions and crossing exchanges and proved their Reidemeister-type completeness theorem. That theorem guarantees a general move calculus but does not address the minimum intermediate petal count for the trefoil word above. Adams et al. introduced petal projections and petal number; their work concerns existence and minimization rather than monotonic move complexity.

Searches for the exact seven-petal word, trefoil hardness, nontrivial-knot petal excess, and formulations equivalent to Question 7.4 found no published statement implying this exact obstruction. The closest previously checked petal results concern hard unknots and other finite move-state questions; they do not imply a nontrivial-knot example.

## Limitations
The result is one explicit trefoil representative and one exact excess value. It does not determine the smallest seven-petal trefoil orbit with this property under any quotient larger than the stated move set, and it gives no classification for other knots. The motivating preprint is very recent, so a later revision or an unindexed independent note could contain the same example.

The crossing-exchange nonexistence is a finite exact check of the source's definition for this word. A transcription error in that definition would affect the certificate; the verifier includes the source's published Example 3.1 as a regression test through the same implementation.

## References
1. Alexei Vernitski, *Some petal diagrams of the unknot are hard*, arXiv:2610.01596v1, 2026. In particular Definition 1.1, Remark 2.3, Section 3, Results A--C, and Question 7.4.
2. Leslie Colton, Cory Glover, Mark Hughes, and Samantha Sandberg, *A Reidemeister type theorem for petal diagrams of knots*, arXiv:1812.08930; Topology and its Applications 267 (2019), 106896.
3. Colin Adams et al., *Knot projections with a single multi-crossing*, arXiv:1208.5742; Journal of Knot Theory and Its Ramifications 24 (2015), 1550011.
