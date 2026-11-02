# Exact radius-four spheres in the flag-rank metric

## Finding

Let \(q\) be a prime power and \(n\ge3\). Write \(\mathrm U(n,\mathbb F_q)\) for the upper-triangular \(n\times n\) matrices. For \(M\in\mathrm U(n,\mathbb F_q)\) define the flag-rank weight
\[
\operatorname{fr}(M)=\sum_{i=1}^{n}\operatorname{rank}_{\mathbb F_q}M_{[i]},
\qquad M_{[i]}=M[\{1,\ldots,i\},\{i,\ldots,n\}].
\]
Let \(s_q(n,4)\) be the number of such matrices of flag-rank weight exactly four. Then
\[
\boxed{\begin{aligned}
s_q(n,4)={}&\binom n4(q-1)^4
 +(n-1)\binom{n-2}{2}q^2(q-1)^3\\
&+\binom{n-2}{2}q^4(q-1)^2
 +(n-2)(n-3)q^4(q-1)^2\\
&+(n-3)q^6(q-1)
 +(n-2)q^2(q^2-1)(q^2-q).
\end{aligned}}
\]
The six summands enumerate six disjoint configurations; the last is the first sphere contribution containing a crossing matrix of rank two. In particular, the radius-four ball size is explicitly \(b_q(n,4)=\sum_{j=0}^{4}s_q(n,j)\), using the established radii-zero-through-three formulas in [1]. For every \(n\ge4\),
\[
b_q(n,4)\equiv\binom{n-1}{4}\pmod q.
\]
Thus a nontrivial perfect *linear* flag-rank-metric code of minimum distance nine and length \(n\ge4\) must satisfy \(q\mid\binom{n-1}{4}\). This is a necessary condition, not an existence assertion.

## Assumptions and scope

The parameter \(q\) ranges over all prime powers, including proper prime powers, and all ranks are over \(\mathbb F_q\). The length is every integer \(n\ge3\). Coordinates are labeled in their natural order; no quotient by isometries is taken. A matrix with a nonzero entry in position \((r,c)\), where \(r\le c\), has a nonzero crossing submatrix at every cut \(i\in\{r,\ldots,c\}\); hence that entry alone forces \(\operatorname{fr}(M)\ge c-r+1\). Write \(v=q-1\) for counting.

## Proof

**Crossing-rank dichotomy.** Let \(\rho_i=\operatorname{rank}M_{[i]}\). If \(\sum_i\rho_i=4\) and some \(\rho_i\ge2\), there must be a nonzero row above row \(i\) and a nonzero column to the right of column \(i\): otherwise the \(i\)-th crossing submatrix would have just one possibly nonzero row or column. Consequently \(\rho_{i-1}\ge1\) and \(\rho_{i+1}\ge1\), forcing \(\rho_{i-1}=\rho_{i+1}=1\), \(\rho_i=2\), and every other \(\rho_j=0\). Thus the support is confined to a consecutive upper-triangular three-by-three block
\[
\begin{pmatrix}a&b&c\\0&d&e\\0&0&f\end{pmatrix}
\]
whose middle crossing block is \(\begin{pmatrix}b&c\\d&e\end{pmatrix}\), required to be invertible. The end diagonal entries \(a,f\) are arbitrary. There are \(n-2\) placements and \(q^2|\operatorname{GL}(2,q)|=q^2(q^2-1)(q^2-q)\) choices per placement. This is configuration **F**, the sixth term. In particular rank three or two distinct rank-two cuts cannot occur at total weight four.

**Four rank-one cuts.** Otherwise all crossings have rank zero or one, and exactly four cuts are nonzero. Every nonzero matrix entry lies on the main diagonal or one of the first three superdiagonals. Classify by the largest superdiagonal containing a nonzero entry.

**A: main diagonal only.** Exactly four diagonal entries are nonzero. The count is \(\binom n4v^4\).

**B and C: first superdiagonal.** Adjacent nonzero first-superdiagonal entries would give an invertible two-by-two crossing minor at their shared cut because the second superdiagonal is zero. Thus selected first-superdiagonal positions are nonadjacent. A single such entry occupies two cuts; the other two occupied cuts must arise from two nonzero diagonal entries outside its two endpoints. There are \((n-1)\binom{n-2}{2}q^2v^3\) matrices (**B**): the two endpoint diagonal entries are unrestricted. Alternatively there are exactly two nonadjacent first-superdiagonal entries and no further occupied cuts (**C**). There are \(\binom{n-2}{2}\) pairs of nonadjacent first-superdiagonal positions, and their four endpoint diagonal entries are unrestricted, giving \(\binom{n-2}{2}q^4v^2\).

**D: second superdiagonal.** If \(c=M_{i,i+2}\ne0\), cuts \(i,i+1,i+2\) are occupied. Another nonzero second-superdiagonal entry would either occupy too many cuts or force a rank-two crossing where its span overlaps the first. No off-diagonal entry may introduce a fourth cut: a first-superdiagonal edge joining an endpoint of this three-position block to the outside forces a nonzero two-by-two crossing minor (the missing third-superdiagonal entry is zero), while an edge further away introduces at least two cuts. Hence the fourth cut comes from one nonzero diagonal entry outside the block. The middle crossing rank-one requirement for
\[
\begin{pmatrix}a&b&c\\0&d&e\\0&0&f\end{pmatrix}
\]
is \(be=cd\). Since \(c\ne0\), choose \(a,b,e,f\) freely, \(c\) nonzero, and set \(d=be/c\). There are \((n-2)(n-3)q^4v^2\) choices, including the exterior nonzero diagonal entry.

**E: third superdiagonal.** A nonzero \(t=M_{i,i+3}\) occupies exactly four cuts, so no entries outside the corresponding consecutive four-by-four block are possible and all four crossing ranks equal one. Write the block as
\[
\begin{pmatrix}
a&b&c&t\\0&d&e&f\\0&0&g&h\\0&0&0&j
\end{pmatrix},\qquad t\ne0.
\]
The two interior rank-one crossing conditions give precisely \(d=bf/t\), \(e=cf/t\), and \(g=ch/t\). The variables \(a,b,c,f,h,j\) are arbitrary, while \(t\) is nonzero. There are \((n-3)q^6v\) such matrices.

The cases are exhaustive by the maximum-superdiagonal classification and disjoint by the rank profile, superdiagonal height, and number of occupied entries. Adding the six counts proves the formula.

For the congruence, the known lower-radius counts are
\[
\begin{aligned}
s_q(n,0)&=1,\\
s_q(n,1)&=nv,\\
s_q(n,2)&=\binom n2v^2+(n-1)q^2v,\\
s_q(n,3)&=\binom n3v^3+(n-1)(n-2)q^2v^2+(n-2)q^4v.
\end{aligned}
\]
All contributions other than the diagonal-only terms in \(s_q(n,0),\ldots,s_q(n,4)\) are divisible by \(q\). Therefore
\[
b_q(n,4)\equiv\sum_{j=0}^4(-1)^j\binom nj=\binom{n-1}{4}\pmod q,
\]
using the alternating-binomial identity. The perfect-code implication follows because a perfect linear code has \(b_q(n,4)=q^{\alpha}\) for its positive codimension \(\alpha\), as in [1].

## Verification

The included dependency-free C++17 checker enumerates all upper-triangular matrices over \(\mathbb F_2\) for \(n=3,4,5,6\), over \(\mathbb F_3\) for \(n=3,4\), and over \(\mathbb F_4\) for \(n=3,4\). It directly computes every crossing rank by finite-field elimination, independently classifies every weight-four matrix into A through F, and checks each of the six summands separately. The eight complete exhaustive runs all passed. In particular, the counts at \((n,q)=(4,2),(4,3),(4,4),(5,2),(6,2)\) are respectively \(173,3526,26337,397,711\). The source and exact stdout are supplied as `verify_flag_rank_radius4.cpp` and `verification_output.txt`. Reproduction: compile with `g++ -O3 -std=c++17 verify_flag_rank_radius4.cpp -o flag_rank_check` and run `./flag_rank_check`. The all-parameter theorem rests on the six-case proof, not on extrapolation from finite runs.

## Relationship to prior work

Alfarano, Mushrraf and Zullo [1] define the same flag-rank sphere sizes and prove explicit formulas for radii zero, one, two and three. Their Section 3 discusses general bounds and does not furnish the exact radius-four count; their perfect-code analysis includes asymptotic obstructions for minimum distance nine but not the radius-four polynomial above. The classification here adds the first rank-two crossing stratum, captured by the \(\operatorname{GL}(2,q)\) factor. Alfarano, Neri and Zullo [2] study maximum flag-rank-distance codes and a Singleton-like bound, not this sphere count. Fourier and Nebe [3] introduce the underlying flag-rank coding model. The claim is not a new general perfect-code existence theorem, a result for unrestricted full matrix rank-metric spheres, or a reevaluation of the earlier sphere counts.

## Limitations

The count concerns radius exactly four and the resulting ball of radius four, not arbitrary radii; it does not determine perfect-code existence for distance nine. The congruence is only a necessary arithmetic obstruction. Although the proof applies to every prime power, computational testing covers only the listed small fields and dimensions. A differently expressed historical formula in adjacent quiver/rank-stratification literature cannot be ruled out solely by database searches; independent mathematical and literature assessment remains open.

## References

[1] G. N. Alfarano, U. Mushrraf and F. Zullo, *On perfect flag-rank metric codes*, arXiv:2606.12934, first posted 11 June 2026, Section 3 and Section 5. https://arxiv.org/abs/2606.12934

[2] G. N. Alfarano, A. Neri and F. Zullo, *Maximum Flag-Rank Distance Codes*, arXiv:2303.16653, first posted 29 March 2023. https://arxiv.org/abs/2303.16653

[3] G. Fourier and G. Nebe, *Degenerate flag varieties in network coding*, *Advances in Mathematics of Communications* 17 (2023), 888–899, DOI 10.3934/amc.2021027. https://www.aimsciences.org/article/doi/10.3934/amc.2021027
