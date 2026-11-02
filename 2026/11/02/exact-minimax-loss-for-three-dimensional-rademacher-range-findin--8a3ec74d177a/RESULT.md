# Exact minimax loss for three-dimensional Rademacher range finding

## Finding

Let \(A\in\mathbb R^{3\times3}\) be invertible, let \(\ell\ge1\) be an integer, and draw \(\Omega\in\{-1,1\}^{3\times\ell}\) with mutually independent equiprobable entries. Let \(P\) be the orthogonal projector onto \(\operatorname{range}(A\Omega)\). Then the exact sharp finite-sample bound is

\[
\frac{\mathbb E\|(I-P)A\|_F^2}{\|A\|_F^2}
\le \frac{2^{\ell+1}-4/3}{4^\ell}.
\]

Equality holds **if and only if** \(A^\top A=\alpha I_3\) for some \(\alpha>0\). For every invertible \(A\), including at sketch widths exceeding three,

\[
\mathbb P\{\operatorname{rank}(A\Omega)<3\}=
\frac{6}{2^\ell}-\frac8{4^\ell}.
\]

The exact rank probabilities are \(4^{1-\ell}\) for rank one, \(6(2^\ell-2)/4^\ell\) for rank two, and the complementary probability for rank three. For instance, three sign-sketch columns fail to span a full-rank three-dimensional target with probability \(5/8\); the largest expected squared-Frobenius-loss fraction at that width is \(11/48\). An independent Gaussian sketch of width at least three has zero residual almost surely, so a finite sign alphabet creates a genuine exact-recovery obstruction.

## Assumptions and scope

All matrices and sketches are real and computations are in exact arithmetic. The target \(A\) is an arbitrary invertible \(3\times3\) matrix, without assumptions on its singular values or right singular-vector orientation. The integer \(\ell\) is arbitrary and positive, including \(\ell>3\). Every sign entry has probability \(1/2\) of either value and all entries are independent. The approximation is \(PA\), the full orthogonal range-projection approximation, **not** an additionally truncated rank-\(k\) SVD. The error is the *squared* Frobenius norm, normalized by \(\|A\|_F^2\).

For a more detailed exact expectation, set \(G=A^\top A\), \(T=\operatorname{tr}G\), and choose four sign-line representatives

\[
\mathcal U=\{(1,1,1)^\top,(1,1,-1)^\top,
(1,-1,1)^\top,(-1,1,1)^\top\}.
\]

Let \(\mathcal V=\{e_i+e_j,e_i-e_j:1\le i<j\le3\}\), six two-coordinate directions. The *exact matrix-specific error*, valid without diagonalizing \(G\), is

\[
\mathbb E\|(I-P)A\|_F^2
=\frac{1}{4^\ell}\left[
\sum_{u\in\mathcal U}\left(T-\frac{u^\top G^2u}{u^\top Gu}\right)
+(2^\ell-2)\sum_{v\in\mathcal V}
\frac{2}{v^\top G^{-1}v}\right].
\]

## Proof

**1. Projective reduction and probabilities.** Negating any column of a sketch does not change its span. The eight sign columns therefore collapse to the four equiprobable projective directions in \(\mathcal U\). Every three distinct representatives are linearly independent (their determinants are \(\pm4\)); invertibility of \(A\) preserves this fact. Consequently a sketch spans a line exactly when all \(\ell\) directions agree, a plane exactly when precisely two different directions occur, and three dimensions otherwise. There are four constant direction-words, and for each of the six unordered pairs there are \(2^\ell-2\) words using both directions. Division by \(4^\ell\) gives the rank probabilities and hence the exact deficiency probability.

**2. Exact losses for the two deficient ranks.** For a single projective direction \(u\), orthogonal projection onto \(Au\) captures squared Frobenius energy \((u^\top G^2u)/(u^\top Gu)\). Its loss is therefore \(T-(u^\top G^2u)/(u^\top Gu)\). For distinct projective representatives \(u,u'\), the line normal to \(\operatorname{span}(Au,Au')\) is \(A^{-\top}(u\times u')\). The six cross products, up to their nonzero scalar multiples, are precisely the six directions in \(\mathcal V\). As \(\|v\|_2^2=2\), projection onto the normal has residual energy \(2/(v^\top G^{-1}v)\). A span of three distinct directions has zero residual. Multiplying these exact losses by their word counts proves the matrix-specific expectation formula.

**3. Two tight-frame inequalities.** The four vectors in \(\mathcal U\) and six in \(\mathcal V\) satisfy

\[
\sum_{u\in\mathcal U}uu^\top=4I_3,
\qquad \sum_{v\in\mathcal V}vv^\top=4I_3.
\]

Cauchy--Schwarz gives, for every \(u\in\mathcal U\),
\[
\frac{u^\top G^2u}{u^\top Gu}\ge
\frac{u^\top Gu}{\|u\|_2^2}=
\frac{u^\top Gu}{3}.
\]
Summing yields
\[
\sum_{u\in\mathcal U}
\left(T-\frac{u^\top G^2u}{u^\top Gu}\right)
\le\frac83T.
\]

Likewise, \((v^\top Gv)(v^\top G^{-1}v)\ge\|v\|_2^4=4\) gives
\[
\frac2{v^\top G^{-1}v}\le\frac12v^\top Gv.
\]
Summing the six directions gives \(\sum_{v\in\mathcal V}2/(v^\top G^{-1}v)\le2T\). Substituting in the expectation formula yields
\[
\mathbb E\|(I-P)A\|_F^2
\le 4^{-\ell}\left(\frac83+2(2^\ell-2)\right)T
=\frac{2^{\ell+1}-4/3}{4^\ell}\,T.
\]

**4. Sharpness and uniqueness.** If \(G=\alpha I_3\), all Cauchy--Schwarz inequalities above are equalities, proving attainment. Conversely, the singleton events have positive probability for every finite \(\ell\). Equality in the global bound forces equality in their Cauchy--Schwarz inequalities and thus makes every \(u\in\mathcal U\) an eigenvector of \(G\). All pairs of these vectors have nonzero inner product; since distinct-eigenvalue eigenvectors of a real symmetric matrix are orthogonal, all four must share one eigenvalue. They span \(\mathbb R^3\), so \(G=\alpha I_3\). This proves uniqueness of the Gram shape, with arbitrary left orthogonal factor and positive scaling.

## Verification

The standalone `verify.py` uses exact rational arithmetic in SymPy. It exhaustively enumerates all projective sketch words at lengths one through five for six explicitly invertible rational test matrices, compares the direct orthogonal-projector residual against the matrix-specific formula, checks the universal upper bound and its strictness away from scaled orthogonality, and checks eight exact rank probability identities. It executes 180 exact-rational inequalities and equalities plus eight distribution checks. The argument above, not finite enumeration, proves the assertion for every invertible real matrix and all positive integer sketch widths.

Run from the directory containing this file: `python verify.py` (requires Python and SymPy).

## Relationship to prior work

Lynch-Davies and Webb, *Sketching Outside the Hilbert Space for the Infinite-Dimensional Randomised SVD* (arXiv:2610.31333v1, 22 October 2026), study Gaussian and sub-Gaussian sketches and illustrate Rademacher performance. Their results are general high-probability bounds rather than the above exact low-dimensional matrix-specific expectation and sharp minimax constant. Saibaba and Międlar, *Randomized low-rank approximations beyond Gaussian random matrices* (arXiv:2308.05814v1, 10 August 2023), provide broad non-Gaussian bounds with unspecified constants; their preprint's Theorem 5 treats independent sub-Gaussian entries, but it does not give the displayed three-dimensional exact finite-sample distribution or the unique worst-case Gram shape. The general randomized SVD framework goes back, among others, to Halko--Martinsson--Tropp (2011). Standard Bernoulli-matrix singularity theory determines related rank events but does not by itself imply the matrix-dependent mean projection residual or its sharp minimax bound. Earlier specialized exact results could remain relevant to priority.

## Limitations

This is a finite, rank-three full-column-dimension result and not a dimension-independent sharp constant. It does not apply directly to rank-deficient targets, correlated or biased sign sketches, sparse signs, finite precision, truncation to a prescribed lower rank, or operator-norm error. The expected squared loss is not a high-probability bound. Literature comparisons and exact-algebra checks are not independent mathematical validation.

## References

1. M. Lynch-Davies and M. Webb, *Sketching Outside the Hilbert Space for the Infinite-Dimensional Randomised SVD*, arXiv:2610.31333v1 (2026-10-22). https://arxiv.org/html/2610.31333v1
2. A. K. Saibaba and A. Międlar, *Randomized low-rank approximations beyond Gaussian random matrices*, arXiv:2308.05814v1 (2023-08-10); SIAM Journal on Mathematics of Data Science **7** (2025), 136--162. https://arxiv.org/html/2308.05814v1
3. N. Halko, P.-G. Martinsson, and J. A. Tropp, *Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions*, SIAM Review **53** (2011), 217--288.
