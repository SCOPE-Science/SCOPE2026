# Exact triangle count and the three-rotation obstruction in Ulam one-deletion graphs

## Finding
For every integer \(n\ge 2\), let \(G_n\) be the simple graph on the permutations of \(n\) distinct labeled symbols. Two distinct permutations are adjacent precisely when deleting the same labeled symbol from both produces the same length-\(n-1\) sequence. Equivalently, their Ulam distance is one.

**Triangle classification.** Every unordered triangle of \(G_n\) belongs to exactly one of two disjoint types:

1. Its three permutations have one common deletion read, obtained by deleting the same uniquely determined symbol. There are exactly \(n!\binom n3\) such triangles.
2. Its three permutations are exactly the three cyclic rotations of a block of three consecutive positions, with all other positions identical. No symbol can be deleted to produce one read shared by all three. There are exactly \(n!(n-2)/3\) such triangles.

Consequently the exact total is
\[
T(G_n)=\frac{n!(n-2)(n^2-n+2)}6.
\]
The graph has degree \((n-1)^2\). For \(n\ge3\), its local clustering coefficient is the same at every vertex and equals
\[
\frac{n^2-n+2}{n(n-1)^2}.
\]

## Assumptions and scope
A permutation is a length-\(n\) sequence containing every element of \(\{1,\ldots,n\}\) exactly once. Deletion retains the **actual labels** and their order: no standardization is performed. Every triangle is an unordered set of three distinct permutations. The case \(n=2\) has no triangles and its local clustering coefficient is undefined because every vertex has just one neighbor. The formula is exact for every integer \(n\ge2\), not merely asymptotic.

## Proof
For two permutations \(u,v\), let \(D(u,v)\) be the simple graph on the symbol labels whose edges are pairs of labels that occur in opposite relative orders in \(u\) and \(v\). Deleting a symbol \(x\) from both permutations gives identical words **if and only if** every edge of \(D(u,v)\) is incident to \(x\). Thus distinct permutations are adjacent in \(G_n\) if and only if their nonempty disagreement graph is a star (a one-edge star may have either endpoint as center). For any three permutations \(u,v,w\), each label pair is inverted an even number of times around the triple, so
\[
D(u,w)=D(u,v)\mathbin\triangle D(v,w),
\]
where \(\triangle\) denotes symmetric difference of edge sets.

We use the following **three-star lemma**. Suppose three nonempty edge sets \(A,B,C\) are stars and \(C=A\triangle B\). Then either the three stars have a common center, or there are three distinct vertices \(a,b,c\) with
\[
A=\{ab,ac\},\qquad B=\{ab,bc\},\qquad C=\{ac,bc\},
\]
up to renaming the stars and vertices. To prove the lemma, choose centers \(a\) for \(A\) and \(b\) for \(B\). If they coincide, \(C\) has that center as well. If a center of \(C\) equals \(a\) or \(b\), the other star must be the single edge \(ab\), and that edge can be recentered to yield a common center. Otherwise take a center \(c\) of \(C\) distinct from \(a,b\). All edges of \(A\) and \(B\) not containing \(c\) must coincide; since their original centers differ, those edges can only be \(ab\). The remaining edges of \(A\), respectively \(B\), are contained in \(\{ac\}\), respectively \(\{bc\}\). If either is absent, the nonempty stars can be recentered to a common center. The only remaining possibility is that \(A\) and \(B\) both contain \(ab\), with \(ac\) in \(A\) and \(bc\) in \(B\), as displayed. This establishes the lemma.

Apply the lemma to the three pairwise disagreement graphs of a triangle. If they have a common center \(x\), the relative order of all other \(n-1\) symbols is identical in the three permutations: they share the deletion read for \(x\). Such a symbol is unique for a triangle. Indeed, if both deleting \(x\) and deleting \(y\) gave a common read, every comparison other than that between \(x\) and \(y\) would be identical across all three permutations. There are only two total orders differing solely in that comparison, not three distinct ones.

For each choice of deleted label \(x\) and each of the \((n-1)!\) orders of the other labels, there are \(n\) distinct permutations obtained by inserting \(x\) in one of the \(n\) positions. Any three give a common-deletion triangle. The unique deleted label prevents double counting, giving \(n(n-1)!\binom n3=n!\binom n3\) triangles of the first type.

Otherwise the lemma says that pairwise comparisons change only on one three-symbol set \(\{a,b,c\}\), and each pair of permutations reverses exactly two of the three comparisons. The orders of the three marked symbols therefore constitute one of the two parity classes in \(S_3\): precisely three cyclic rotations of one order. Every comparison between a marked and an unmarked symbol is identical in all three permutations. The three marked symbols must occupy consecutive positions; an unmarked symbol lying between two of them would change its relative order with a marked symbol under a cyclic rotation. Hence the triangle is exactly a triple-block rotation, and conversely every triple-block rotation is a triangle with no common deletion read.

Choose an initial permutation in \(n!\) ways and the left end of a three-position block in \(n-2\) ways. Each resulting triangle is counted three times, once for each of its rotations. Thus the second type contributes \(n!(n-2)/3\). Adding both types gives the claimed formula.

Finally, every nonidentity translocation of a permutation arises by moving one of the \(n\) labeled symbols to a different position. There are \(n(n-1)\) directed moves, and exactly \(n-1\) coincidences: every adjacent swap is produced by moving either of its two entries, whereas a longer move has a unique moved entry. Hence each vertex has degree \((n-1)^2\). Every triangle has three vertices, so the number through one vertex is
\[
\frac{3T(G_n)}{n!}=\frac{(n-2)(n^2-n+2)}2.
\]
Dividing this by \(\binom{(n-1)^2}{2}\) yields the stated clustering coefficient when \(n\ge3\).

## Verification
Run `python3 verify.py` alongside this file. The verifier constructs neighbors by literal single-entry moves, then independently tests adjacency by comparing actual single-symbol deletion reads, and checks every neighbor pair's triangle classification. It exhaustively checks every vertex for \(2\le n\le6\) (a total of 872 vertices), plus the identity vertex for each \(7\le n\le14\). It confirms the full triangle totals \(0,8,112,1320,15360\) for \(n=2,3,4,5,6\), respectively. These finite computations are corroboration; the proof above establishes the infinite statement.

## Relationship to prior work
Wang, Nguyen, Chee, and Vu define the permutation \(t\)-deletion confusability graph and prove an upper bound of order \(O_t(n!n^{3t})\) for its triangle count (Section III, Lemma 4); their bound specializes to order \(O(n!n^3)\) at \(t=1\). The present result gives the exact leading coefficient and lower-order terms in that case and classifies every triangle. Kong provides the single-translocation Ulam sphere size \(1+(n-1)^2\), which supplies the known degree but does not count edges among neighbors. Farnoud, Skachek, and Milenkovic establish the underlying translocation/Ulam coding framework and capacity bounds. These are comparisons of actual claims, not novelty certificates.

## Limitations
This theorem concerns only distinct labeled symbols, exactly one deletion, and simple undirected triangles. It does not determine optimal code sizes, larger cliques, the number of triangles for two or more deletions, or multipermutation/binary-string conflict graphs. Finite checks do not prove the general formula; the three-star argument is its mathematical proof. An equivalent graph-theoretic enumeration in unindexed literature remains a possibility, and no independent scientific audit has been performed.

## References
1. S. Wang, T. Nguyen, Y. M. Chee, and V. K. Vu, *Permutation and Multi-permutation Codes Correcting Multiple Deletions*, first arXiv public posting June 24, 2024, arXiv:2406.16656, especially Sections II–III and Lemma 4. https://arxiv.org/abs/2406.16656
2. J. Kong, *Ulam Sphere Size Analysis for Permutation and Multipermutation Codes Correcting Translocation Errors*, arXiv:1712.03639, especially Proposition III.2. https://arxiv.org/abs/1712.03639
3. F. Farnoud, V. Skachek, and O. Milenkovic, *Error-Correction in Flash Memories via Codes in the Ulam Metric*, arXiv:1202.0932, especially Section II. https://arxiv.org/abs/1202.0932
