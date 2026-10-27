# Bivariate enumeration of dominating--locating-dominating partitions of cycles

## Finding

For every integer \(n\ge5\), let \(C_n\) be the simple cycle whose vertices are labeled \(0,1,\ldots,n-1\) in cyclic order. Let \(P_n(u)\) count vertex partitions \((D,L)\), where \(D\) dominates \(C_n\), \(L\) is a locating-dominating set, \(D\sqcup L=V(C_n)\), and a partition has weight \(u^{|L|}\). Then

\[
\boxed{\sum_{n\ge5}P_n(u)z^n =
\frac{2uz^2+u^2(3z^3+4z^4+5z^5)+6u^3z^6}
{1-uz^2-u^2(z^3+z^4+z^5)-u^3z^6}
-2uz^2-3u^2z^3-6u^2z^4.}
\]

Equivalently, encode \(D\) by zero and \(L\) by one. Such a partition of \(C_n\), for \(n\ge5\), is valid **if and only if** its labeled cyclic binary word avoids the three cyclic factors `000`, `111`, and `00100`. Thus the identity describes the entire set of valid partitions, not merely a minimum partition size.

For example,
\[
P_5(u)=5u^2+5u^3,\quad P_6(u)=14u^3+3u^4,\quad
P_7(u)=7u^3+14u^4,\quad P_8(u)=30u^4+8u^5.
\]

The cardinality-refined recurrence (for \(n\ge11\)) is
\[
P_n(u)=uP_{n-2}(u)+u^2\bigl(P_{n-3}(u)+P_{n-4}(u)+P_{n-5}(u)\bigr)+u^3P_{n-6}(u).
\]

## Assumptions and scope

A dominating set \(S\) requires each vertex outside \(S\) to have a neighbor in \(S\). A locating-dominating set additionally requires distinct vertices outside \(S\) to have distinct nonempty sets of neighbors in \(S\). We count ordered, typed pairs \((D,L)\); since the two parts have different duties, they must not be identified after swapping. Vertices are labeled (rotations are different unless the resulting labeled subset is identical). No loops or repeated edges occur. The theorem is for \(n\ge5\); the shorter cycles have exceptional coincidence of neighborhoods and are not covered by its word classification.

## Proof

**1. Local characterization.** Write zero on \(D\), one on \(L\). Each one-vertex has a zero-neighbor exactly when no cyclic `111` appears. Each zero-vertex has a one-neighbor exactly when no cyclic `000` appears. Therefore the two domination requirements are exactly avoidance of `111` and `000`.

Assume \(n\ge5\) and both domination requirements. If distinct zero-vertices have identical neighborhoods inside \(L\), these common neighborhoods are nonempty. Their neighbor sets on a simple cycle can intersect only if the vertices are at distance two. (In a cycle of length at least five, distinct adjacent vertices have no common neighbor.) Thus the zeros are the two neighbors of some one-vertex. To have *identical* neighborhoods inside \(L\), each of their other neighbors must be zero; these two other neighbors are distinct because \(n\ge5\). The resulting five consecutive labels, centered at their common one-neighbor, form `00100`. Conversely `00100` produces two zero-vertices whose only neighbor in \(L\) is the central one-vertex, violating location. This proves the equivalence. At length four the word `0101` exhibits a further identification obstruction, hence the stated boundary.

**2. Cyclic run transfer.** Avoiding `000` and `111` means zero-runs and one-runs all have length one or two. Enumerate cyclic run pairs \((a_i,b_i)\), where \(a_i\in\{1,2\}\) is the length of the \(i\)-th zero-run and \(b_i\in\{1,2\}\) is the length of the following one-run. The forbidden word `00100` appears precisely when the zero-run lengths before and after a one-run are both two while that one-run has length one. Hence the weighted transfer matrix, from the previous zero-run length to the next one, is

\[
T(z,u)=\begin{pmatrix}
z^2u+z^3u^2 & z^2u+z^3u^2\\
z^3u+z^4u^2 & z^4u^2
\end{pmatrix}.
\]

For each permitted pair \((a_i,b_i)\), its weight is \(z^{a_i+b_i}u^{b_i}\), so exponent of \(z\) is the number of vertices and exponent of \(u\) is the number in \(L\). With \(k\ge1\) zero-runs, \(\operatorname{tr}(T^k)\) records cyclic sequences with a marked zero-run. A word of length \(n\) with \(k\) zero-runs is represented by \(n\) placements of that marked run and is counted \(k\) times, giving the factor \(n/k\). This remains true for periodic words, since the count is of labeled placements rather than primitive necklace orbits.

Thus, as formal power series,
\[
H(z,u)=z\frac{\partial}{\partial z}\sum_{k\ge1}\frac{\operatorname{tr}(T(z,u)^k)}{k}
=-z\frac{\partial}{\partial z}\log\det(I-T(z,u)).
\]

Direct multiplication gives
\[
Q(z,u)=\det(I-T(z,u))=1-uz^2-u^2(z^3+z^4+z^5)-u^3z^6.
\]

Differentiating \(Q\) yields
\[
H(z,u)=\frac{2uz^2+u^2(3z^3+4z^4+5z^5)+6u^3z^6}{Q(z,u)}.
\]

The formal expression also enumerates cyclic words of lengths two, three, and four with coefficients \(2u\), \(3u^2\), and \(6u^2\), respectively. Remove these terms to obtain the formula starting at \(n=5\). All transfer-state edges have strictly positive vertex length, so the traces and logarithm are well-defined formal power series.

**3. Recurrence.** Multiplying the generating-function identity by \(Q\) and comparing coefficients at \(n\ge11\) gives the displayed recurrence. The cutoff avoids contamination by the deliberately removed degrees below five. This completes the proof of the full weight enumerator for every \(n\ge5\).

## Verification

The included standalone Python program `verify.py` independently exhausts all \(2^n\) labeled subsets for every \(5\le n\le17\). It checks the graph's domination and locating conditions directly, independently tests the three cyclic factors, and compares the cardinality distribution with the rational generating function using exact integer polynomial arithmetic. It checks the sparse determinant expansion separately. Run with `python verify.py`. Its recorded successful output is in `verify_output.txt`. These finite tests are corroboration; the unrestricted result follows from the proof above.

## Relationship to prior work

Chakraborty, Foucaud, Henning and Laihonen (2026) prove existence of a partition into one dominating and one locating-dominating set for every isolate-free graph; their full article treats constructive existence, not a size-refined census of all such partitions of cycles. The earlier Foucaud--Maniya--Paul--Pradhan work investigates partitions into **two** locating-dominating sets and proves existence for several graph classes; this stronger existence problem does not enumerate the present typed partitions. Chellali, Dobrynin, Foucaud, Golmohammadi and Valenzuela-Tripodoro study locating-dominating **coalition** partitions of cycles, whose defining condition requires no block itself to be locating-dominating; this is distinct from and incompatible with the present defining condition on \(L\). That paper also discusses the familiar restriction against consecutive two-vertex gaps in a locating-dominating set on a cycle; that local restriction by itself is not claimed as new here.

The univariate specialization \(P_n(1)\), for \(n\ge5\), coincides with the already tabulated **Fielder sequence OEIS A001636** (with an index shift) and its known rational generating function. Neither that integer sequence nor its known recurrence is claimed as original here. The assessed contribution is the joint typed-partition characterization and its **size-refined bivariate** exact enumerator, which is not supplied by the cited generic sequence entry.

## Limitations

Only simple cycles of order at least five and typed dominating/locating-dominating partitions are covered. The result does not classify partitions with both parts locating-dominating, coalitions, paths, general graphs, or unlabeled rotation classes. A generic transfer-matrix method is standard, and equivalent combinatorial interpretations may exist outside the inspected literature; that publication-priority risk remains. The finite tests do not prove the unlimited identity; the formal transfer argument does. Independent review has not been performed.

## References

1. D. Chakraborty, F. Foucaud, M. A. Henning, T. Laihonen, *A Note on Partitioning the Vertex Set of a Graph into a Dominating Set and a Locating Dominating Set*, Electronic Journal of Combinatorics 33(1), #P1.51 (published 2026-03-13), DOI: 10.37236/14049; https://www.combinatorics.org/ojs/index.php/eljc/article/download/v33i1p51/pdf/ .
2. F. Foucaud, P. V. Maniya, K. Paul, D. Pradhan, *Locating-dominating partitions for some classes of graphs*, arXiv:2506.12933 (first posted 2025-06-15); https://arxiv.org/abs/2506.12933 .
3. M. Chellali et al., *Locating-dominating coalitions in graphs*, arXiv:2602.18760 (first posted 2026-02-21); https://arxiv.org/html/2602.18760v2 .
4. OEIS A001636, *A Fielder sequence*, https://oeis.org/A001636 (including the published older coefficients and recurrence).
