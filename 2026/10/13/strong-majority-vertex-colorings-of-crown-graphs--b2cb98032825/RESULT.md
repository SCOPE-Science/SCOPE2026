# Strong majority vertex-colorings of crown graphs

## Finding

For an integer \\(n\\ge3\\), let
\\[
\\operatorname{Cr}_n=K_{n,n}-M_n
\\]
be the crown graph. Write its bipartition as
\\[
A=\\{a_1,\\ldots,a_n\\},\\qquad B=\\{b_1,\\ldots,b_n\\},
\\]
where the deleted perfect matching consists of the pairs \\(a_i b_i\\). Put
\\[
h=\\left\\lfloor\\frac{n-1}{2}\\right\\rfloor.
\\]

For a vertex-coloring \\(c\\), let
\\[
A_\\alpha=|\\{a_i:c(a_i)=\\alpha\\}|,
\\qquad
B_\\alpha=|\\{b_i:c(b_i)=\\alpha\\}|.
\\]
Then \\(c\\) is a strong majority vertex-coloring if and only if
\\[
\\boxed{A_\\alpha\\le h\\quad\\text{and}\\quad B_\\alpha\\le h
\\quad\\text{for every color }\\alpha.}
\\]

Thus the two sides are governed independently by the same capacity bound. In particular,
\\[
\\boxed{
\\operatorname{Maj}(\\operatorname{Cr}_n)
=
\\left\\lceil\\frac{n}{\\lfloor(n-1)/2\\rfloor}\\right\\rceil
=
\\begin{cases}
4,&n=4,\\\\
3,&n=3\\text{ or }n\\ge5.
\\end{cases}}
\\]
The full spectrum of numbers of colors occurring in strong majority colorings is
\\[
\\boxed{\\{\\operatorname{Maj}(\\operatorname{Cr}_n),\\operatorname{Maj}(\\operatorname{Cr}_n)+1,\\ldots,2n\\}.}
\\]

There is also an exact enumeration. For a fixed labeled \\(q\\)-color palette define
\\[
E_{n,q}
=
\\sum_{\\substack{x_1+\\cdots+x_q=n\\\\0\\le x_j\\le h}}
\\frac{n!}{x_1!\\cdots x_q!},
\\]
and set \\(E_{n,0}=0\\). The number of strong majority colorings into the palette, allowing unused colors, is
\\[
\\boxed{E_{n,q}^2.}
\\]
The number using all \\(q\\) colors is
\\[
\\boxed{
S_{n,q}
=
\\sum_{j=0}^{q}(-1)^j\\binom qj E_{n,q-j}^2.
}
\\]
For the optimal value \\(q=\\operatorname{Maj}(\\operatorname{Cr}_n)\\), every valid palette coloring is automatically surjective, so the number of labeled optimal colorings is \\(E_{n,q}^2\\). For example, the counts are \\(36\\) for \\(n=3\\), \\(576\\) for \\(n=4\\), and \\(8100\\) for each of \\(n=5,6\\).

## Assumptions and scope

Graphs are finite and simple. A strong majority vertex-coloring is a map from the vertex set to a color set such that for every vertex and every color, at most half of the open neighborhood has that color. Colorings need not be proper.

The theorem concerns crown graphs of order \\(2n\\) for \\(n\\ge3\\). The case \\(n=3\\) is the cycle \\(C_6\\), so its scalar value \\(3\\) is already implied by the cycle result in the initiating paper; the structural criterion, all-color spectrum, and enumeration are stated uniformly for the whole crown family.

## Proof

Every vertex of \\(\\operatorname{Cr}_n\\) has degree \\(n-1\\), so the strong-majority threshold for an integer color multiplicity is
\\[
h=\\left\\lfloor\\frac{n-1}{2}\\right\\rfloor.
\\]
Consider a color \\(\\alpha\\) on the side \\(B\\).

If
\\[
B_\\alpha\\le h,
\\]
then every vertex \\(a_i\\) sees at most \\(B_\\alpha\\le h\\) vertices of color \\(\\alpha\\), because its neighborhood is \\(B\\setminus\\{b_i\\}\\).

Conversely, suppose
\\[
B_\\alpha\\>h.
\\]
If \\(B_\\alpha<n\\), choose an index \\(i\\) for which \\(b_i\\) does not have color \\(\\alpha\\). Then \\(a_i\\) is adjacent to all \\(B_\\alpha\\) vertices of color \\(\\alpha\\), contradicting the strong-majority condition. If \\(B_\\alpha=n\\), every \\(a_i\\) sees \\(n-1\\) vertices of color \\(\\alpha\\), and
\\[
n-1>h
\\]
for \\(n\\ge3\\), again a contradiction. Hence every color satisfies \\(B_\\alpha\\le h\\). The same argument with the two sides exchanged gives \\(A_\\alpha\\le h\\).

This proves the capacity criterion.

Each side has \\(n\\) vertices and every color contributes at most \\(h\\) of them, so any strong majority coloring using \\(q\\) colors satisfies
\\[
qh\\ge n.
\\]
Therefore
\\[
q\\ge\\left\\lceil\\frac nh\\right\\rceil.
\\]
Conversely, with
\\[
q=\\left\\lceil\\frac nh\\right\\rceil,
\\]
one can partition each of \\(A\\) and \\(B\\) independently into \\(q\\) nonempty color classes of sizes at most \\(h\\). Applying the same labeled palette on both sides gives a strong majority coloring. Thus
\\[
\\operatorname{Maj}(\\operatorname{Cr}_n)=\\left\\lceil\\frac nh\\right\\rceil.
\\]
Substituting \\(h=\\lfloor(n-1)/2\\rfloor\\) gives the displayed \\(3,4,3\\) transition.

Starting from an optimal coloring, repeatedly recolor one vertex by a fresh color. This can only decrease color-class multiplicities on its original color and creates a singleton class, so the capacity criterion remains valid. Hence every used-color count through \\(2n\\) is realizable.

For the enumeration, a coloring of side \\(A\\) into a fixed \\(q\\)-color palette is feasible exactly when its multiplicity vector
\\[
(x_1,\\ldots,x_q)
\\]
sums to \\(n\\) and every coordinate is at most \\(h\\). For a fixed vector, the number of assignments is the multinomial coefficient
\\[
\\frac{n!}{x_1!\\cdots x_q!}.
\\]
Summing over all admissible vectors gives \\(E_{n,q}\\). The choices on \\(A\\) and \\(B\\) are independent, so the total is \\(E_{n,q}^2\\).

Finally, inclusion-exclusion over palette colors omitted from the entire graph gives
\\[
S_{n,q}
=
\\sum_{j=0}^{q}(-1)^j\\binom qj E_{n,q-j}^2.
\\]
At the minimum palette size, a valid coloring cannot omit a color, because otherwise it would use fewer than \\(\\operatorname{Maj}(\\operatorname{Cr}_n)\\) colors. This proves the optimal-color count.

## Verification

The accompanying `artifacts/verify.py` constructs crown graphs directly from the deleted-perfect-matching definition. It evaluates the strong-majority condition from each open neighborhood, independently checks the side-capacity characterization, and compares exact palette and surjective counts with the multinomial and inclusion-exclusion formulas.

The exhaustive comparison covers \\(n=3,4\\) for palettes through four colors and \\(n=5,6\\) for palettes through three colors. Formula-level existence and minimality are additionally checked for every \\(3\\le n\\le50\\).

Replay output:

`ALL CHECKS PASSED; color_assignments_checked=672856; exhaustive_cases=[(3, 3, 36), (4, 4, 576), (5, 3, 8100), (6, 3, 8100)]; structural_formula_n=3..50`

The finite computation is corroborative only. The arbitrary-order statement follows from the analytic side-capacity proof.

## Relationship to prior work

Kalinowski, Kamyczura, Pilśniak, and Woźniak introduced strong majority vertex-coloring in 2026. Their paper defines the same open-neighborhood condition and determines the parameter for cycles and complete graphs before proving general upper and lower phenomena. In particular, their cycle result already gives the scalar value for \\(\\operatorname{Cr}_3=C_6\\), and their complete-graph example has its own exceptional order-four behavior.

The inspected full text contains no occurrence of “crown,” “matching,” or “complete bipartite,” and it does not state the crown side-capacity criterion or its enumeration. Their general bipartite construction showing arbitrarily large strong majority number does not imply the crown value: it builds a very different incidence graph with prescribed neighborhoods.

Nearby 2026 literature on strong majority edge-coloring concerns an edge invariant. A public database search likewise returned strong-majority edge-coloring results and unrelated exact crown-graph invariants, but no strong-majority vertex theorem for crowns.

## Limitations

The theorem uses the exact deleted-matching neighborhood structure of \\(K_{n,n}-M_n\\). It does not directly classify strong majority colorings of arbitrary bipartite graphs with a sparse set of deleted edges.

The enumeration counts colorings with labeled colors. Quotienting by graph automorphisms or color permutations is a different problem.

The originality assessment is literature-based rather than an absolute uniqueness proof. Crown graphs also appear under the notation \\(K_{n,n}-M\\), and equivalent work under alternate terminology could be poorly indexed; those aliases were included in targeted searches.

## References

1. R. Kalinowski, M. Kamyczura, M. Pilśniak, and M. Woźniak, “Strong majority colorings of graphs,” arXiv:2605.23828v1, first public May 22, 2026, MSC \\(05C15,05C70\\).
2. S. Antoniuk, M. Prorok, and N. Salia, “Strong Majority Edge-Coloring,” arXiv:2607.00212v1, June 30, 2026.
