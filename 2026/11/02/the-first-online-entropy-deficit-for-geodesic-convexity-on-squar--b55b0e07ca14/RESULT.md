# The first online entropy deficit for geodesic convexity on squared paths

## Finding

Let \(G_n=P_n^2\) be the graph on \(\{0,1,\ldots,n-1\}\) in which distinct indices are adjacent when their difference is at most two. Let \(\mathcal C_n\) be the family of all geodesically convex vertex sets, including the empty set. Vertex-membership is the instance/query relation, and \(\operatorname{Ldim}\) uses complete binary adaptive query trees.

**Theorem.** For every integer \(n\ge1\), the elements of \(\mathcal C_n\) are precisely the empty set, the nonempty consecutive intervals \(\{a,a+1,\ldots,b\}\), and the step-two progressions \(\{a,a+2,\ldots,b\}\) with at least two vertices. Consequently, writing \(n=2m\) or \(n=2m+1\),
\[
|\mathcal C_{2m}|=3m^2+1,\qquad |\mathcal C_{2m+1}|=3m^2+3m+2.
\]

The VC dimension is \(1\) for \(n=1\), \(2\) for \(n=2\), and \(3\) for \(n\ge3\). The complete static shattering polynomial is
\[
1+nz+\binom n2z^2+T_nz^3,\quad
T_{2m}=\frac{m(m^2-1)}3,\quad T_{2m+1}=\frac{m(m+1)(2m+1)}6.
\]
This static triple criterion is already implied by Tian and Xu's published general-position characterization, Lemma 4.2 (see Relationship to prior work); it is stated here to identify the online concept family, not as a separate novelty claim.

The **new online cutoff** is exact: \(n=10\) is the first order for which the elementary hypothesis-count upper bound is not attained,
\[
\operatorname{Ldim}(\mathcal C_{10})=5
<\left\lfloor\log_2|\mathcal C_{10}|\right\rfloor=6,
\quad |\mathcal C_{10}|=76.
\]
For all \(1\le n\le9\), the two dimensions in this inequality are equal. An exhaustive, independently reproducible rank recurrence gives the complete exact spectrum through order twenty:

| \(n\) | \(|\mathcal C_n|\) | \(\operatorname{Ldim}(\mathcal C_n)\) | \(\lfloor\log_2|\mathcal C_n|\rfloor\) |
|---:|---:|---:|---:|
| 1 | 2 | 1 | 1 |
| 2 | 4 | 2 | 2 |
| 3 | 8 | 3 | 3 |
| 4 | 13 | 3 | 3 |
| 5 | 20 | 4 | 4 |
| 6 | 28 | 4 | 4 |
| 7 | 38 | 5 | 5 |
| 8 | 49 | 5 | 5 |
| 9 | 62 | 5 | 5 |
| 10 | 76 | 5 | 6 |
| 11 | 92 | 6 | 6 |
| 12 | 109 | 6 | 6 |
| 13 | 128 | 6 | 7 |
| 14 | 148 | 6 | 7 |
| 15 | 170 | 6 | 7 |
| 16 | 193 | 7 | 7 |
| 17 | 218 | 7 | 7 |
| 18 | 244 | 7 | 7 |
| 19 | 272 | 7 | 8 |
| 20 | 301 | 7 | 8 |

The online and static dimensions have an unbounded separation:
\[
\operatorname{Ldim}(\mathcal C_n)=2\log_2 n+O(1),\qquad
\operatorname{VCdim}(\mathcal C_n)=3\quad(n\ge3).
\]
No exact closed form for the online dimension beyond \(n=20\) is asserted.

## Assumptions and scope

Graphs are finite, simple, unweighted and connected. Geodesic convexity means containing *every vertex on every shortest path* joining two included vertices. Empty and singleton sets are convex. A concept is one of these vertex sets, and each query specifies a vertex; the adversary answers its membership in a consistent unknown concept. A complete binary tree is shattered when each root-to-leaf answer sequence is realized by at least one concept. Counting distinct hypotheses supplies the upper bound on the tree depth. The exact finite dimension values are rigorously established by the complete recursion below, not by extrapolating the displayed table.

## Proof

**Shortest paths.** For indices \(a<b\), their graph distance is \(\lceil(b-a)/2\rceil\). If \(b-a\) is even, every shortest path consists of jumps of size two, so the unique geodesic contains \(a,a+2,\ldots,b\). If \(b-a\) is odd, every intermediate integer is on some shortest path: for any \(a\le t\le b\),
\[
\left\lceil\frac{t-a}{2}\right\rceil+
\left\lceil\frac{b-t}{2}\right\rceil=
\left\lceil\frac{b-a}{2}\right\rceil.
\]
The entire ordinary interval is therefore the geodesic interval in the odd case.

**Concept classification.** Let \(S\) be a nonempty convex subset with smallest and largest vertices \(a,b\). If \(b-a\) is odd, the preceding statement forces every integer between them into \(S\). If \(b-a\) is even, it forces the complete step-two progression. If \(S\) also contains an index \(t\) of the opposite parity, then \(t-a\) and \(b-t\) are both odd, so the geodesic intervals of the pairs \((a,t)\) and \((t,b)\) fill the whole interval. Conversely, each ordinary interval is convex because every shortest path between two indices remains between them, and each step-two progression is convex because its pairs have unique jump-two geodesics. Counting these disjoint types gives the asserted formulas.

**Static shattering.** Every two-vertex support is shattered (empty set, the two singletons, and an interval containing both). For \(a<b<c\), realizing the positive trace \(\{a,c\}\) without \(b\) is possible exactly when \(c-a\) is even and \(b-a\) is odd. Equivalently both gaps are odd. Then the other seven traces are supplied by an empty set, singletons, and consecutive intervals. For four ordered support vertices \(a<b<c<d\), shattering would require alternating parities to realize \(\{a,c\}\) and \(\{b,d\}\) without their intermediate vertices; however, the pair \(a,d\) would then have opposite parity and its convex hull would contain \(b,c\), a contradiction. Hence no four-support is shattered. To count triples, put \(b-a=2u+1\), \(c-b=2v+1\), and sum \(\sum_{s=1}^{\lfloor(n-1)/2\rfloor}s(n-2s)\). This gives the two displayed cubic coefficients, in agreement with the previously known general-position criterion.

**Exact finite online proof.** For a version space \(V\subseteq\mathcal C_n\), let \(V_x^+\) and \(V_x^-\) be its subsets accepting and rejecting vertex \(x\). Define
\[
D(V)=\begin{cases}0,&|V|\le1,\\1+\max_{x:\,V_x^+,V_x^-\ne\varnothing}\min\{D(V_x^+),D(V_x^-)\},&|V|\ge2,\end{cases}
\]
where a maximum over an empty set is interpreted so that \(D(V)=0\). By induction on \(|V|\), \(D(V)\) equals the largest depth of a complete shattered adaptive tree: every nonconstant first query partitions \(V\), and both branches must support the remaining depth. The supplied `verify.py` constructs every member of \(\mathcal C_n\) by the proved structural classification, represents each version space as a bitset, memoizes the exact recurrence and enumerates *every possible vertex* at each state. It thereby proves each finite line of the table, including the first deficit. Its construction of a depth-five tree for \(n=10\) is checked leaf by leaf against 32 distinct consistent hypotheses. Independently, a separate Boolean feasibility recursion verifies each computed rank and the failure of the next depth through \(n=12\). Thus no search timeout, heuristic pruning, or partial hypothesis enumeration is used as a negative certificate.

At \(n=10\), the exact first-query branch ranks for vertices \(0\) through \(9\) are
\[
(3,5),(4,5),(4,5),(5,4),(4,4),
(4,4),(5,4),(4,5),(4,5),(3,5).
\]
No first query has both branch ranks at least five, excluding depth six; the verified depth-five tree supplies the matching lower bound.

**Universal online growth.** Choose \(p=\lfloor(n-1)/2\rfloor\) and restrict to ordinary intervals \([a,b]\) with \(0\le a\le p\le b<n\). Questions on positions strictly left of \(p\) reveal only a left-endpoint threshold with \(p+1\) possibilities; questions strictly right reveal an independent right-endpoint threshold with \(n-p\) possibilities. Concatenating balanced binary search trees yields
\[
\lfloor\log_2(p+1)\rfloor+
\lfloor\log_2(n-p)\rfloor
\le \operatorname{Ldim}(\mathcal C_n)
\le\lfloor\log_2|\mathcal C_n|\rfloor.
\]
Both bounds are \(2\log_2 n+O(1)\). These universal inequalities do not establish an exact rank formula for orders beyond the checked finite range.

## Verification

Run `python3 verify.py` with Python 3.9 or later and no third-party packages. The program (i) exhaustively enumerates all \(2^n\) subsets and checks graph-distance geodesic convexity independently through \(n=11\); (ii) checks the parity triple characterization for every triple through \(n=20\); (iii) evaluates the exact online version-space recurrence through \(n=20\); (iv) cross-checks its result using a different Boolean feasibility recurrence through \(n=12\); and (v) constructs and validates all 32 leaf witnesses for a complete depth-five tree at \(n=10\). The terminal marker is `SQUARED_PATH_CONVEXITY_ALL_CHECKS_PASS`.

## Relationship to prior work

Tian and Xu determine the general-position number of powers of paths; their Theorem 3.2 already gives \(\operatorname{gp}(P_n^2)=3\), and their Lemma 4.2 identifies exactly the alternating-parity general-position triples. These facts imply the static support description here once the convex family is identified. We **do not** claim that the general-position criterion, the static VC dimension, or their immediate polynomial enumeration is new. Iršič, Klavžar, Rus and Tuite develop general-position polynomials; that invariant is adjacent to, but not an adaptive shattering rank. Thiessen and Gärtner study general online learning of convex sets on graphs. The accessible abstract supplies general mistake bounds but no verified exact finite online ranks for squared paths; its full paper was not accessible for this comparison, which is a genuine priority risk.

The present candidate contribution is the exact *online* cutoff at ten vertices, the complete initial adaptive spectrum through order twenty, and the documented failure windows relative to the hypothesis-count bound. The count and static characterization provide the independently checked input to that question; they are not passed off as separate discoveries. Generic upper bounds or the general-position number do not imply the exact adaptive rank of the 76-member hypothesis class at ten vertices.

## Limitations

The complete finite online table ends at order twenty; no unproved extrapolation to later orders is made. The asymptotic online dimension is proved only to additive constant. The prior source on online graph-convexity was not available in full text, so comprehensive historical priority is unverified. All audit and validation statements concern self-review mathematical and computational checking; independent scientific validation has not been performed.

## References

1. J. Tian and K. Xu, *On the general position number of the k-th power graphs*, Quaestiones Mathematicae 47 (2024), 2215–2230, DOI 10.2989/16073606.2024.2352568. Author-posted preprint made public by 2024-05-03, with Theorem 3.2 and Lemma 4.2.
2. V. Iršič, S. Klavžar, G. Rus and J. Tuite, *General Position Polynomials*, Results in Mathematics 79 (2024), article 110, DOI 10.1007/s00025-024-02133-3; arXiv:2401.05696.
3. M. Thiessen and T. Gärtner, *Online Learning of Convex Sets on Graphs*, ECML PKDD 2022, pp. 349–364, DOI 10.1007/978-3-031-26412-2_22.
