# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

For a cyclic quadrilateral, Brahmagupta's formula and the substitution \(y_i=(P/2-a_i)/(P/4)\) turn the area into \((P/4)^2\sqrt{y_1y_2y_3y_4}\), while the perimeter and side variance become \(\sum y_i=4\) and \(\sum(y_i-1)^2=q\). For \(q<4/3\), this sphere is contained in the open box \((0,2)^4\). Lagrange multipliers therefore classify all product extrema by the \(1+3\) and \(2+2\) multiplicity patterns. Exact factorization shows the stated \(1+3\) branch is the unique minimum up to permutation.

At \(q=4/3\), the constraint first reaches a zero coordinate. The displayed boundary family realizes every \(q\in[4/3,4)\) in the closure with zero product, so the cyclic area infimum is zero thereafter. The reverse stability inequality follows from the exact lower envelope and the factorization
\[
(1-r)(1+r/3)^3-(1-r^2)^2
=4r^2(1-r)(7r+9)/27.
\]
The constant 12 is forced by the lower-envelope family as \(q\uparrow4/3\).

The algebraic identities and limiting cases were checked symbolically. No numerical evidence is used in place of proof.

## Originality

PASS, to the best of our knowledge, with an important prior-coverage boundary.

Giugiuc--Oai--Altintas (2018) was inspected in detail because it is directly adjacent. Its Theorem 1.1 gives a sharp area inequality for convex quadrilaterals, and its Lemmas 1.2 and 1.3 solve the corresponding **maximum-product** problem with fixed normalized first and second moments. After rewriting, their theorem also supplies the sharp lower bound
\[
(12-16/\sqrt3)V\le P^2-16K.
\]
Accordingly, neither the upper fixed-variance area profile nor that inequality is claimed as new here.

The claimed contribution is the complementary **minimum-product** result for cyclic quadrilaterals: the exact lower area profile below \(q=4/3\), the zero-infimum transition at \(q=4/3\), and the sharp reverse inequality \(P^2-16K\le12V\). Targeted searches used cyclic quadrilateral, side variance, sum of squared sides, fixed perimeter, minimum area, reverse stability, Brahmagupta, and the equivalent formula \(4K\ge P^2-3\sum a_i^2\). No located source states these results.

Indrei--Nurbekyan (2015) and Indrei (2016) concern quantitative polygonal isoperimetric stability but do not give this exact cyclic lower profile. Historical Brahmagupta/Bretschneider sources provide the area formulas but not the fixed-second-moment minimum located here.

Residual risk remains because the minimum-product inequality is elementary after normalization and could exist in an older symmetric-polynomial or inequality collection under nongeometric notation. No specific located source gave evidence of such coverage.

## Value

PASS.

The result supplies the missing opposite side of a sharp fixed-moment quadrilateral problem: it determines exactly when nonzero area is forced by side variance, identifies the unique minimizing side pattern below threshold, detects the degeneracy threshold, and produces a best global reverse stability constant. Combined with the known 2018 inequality, it gives a sharp two-sided equivalence between cyclic quadrilateral isoperimetric deficit and side variance.

## Limitations

- Nondegenerate convex cyclic Euclidean quadrilaterals only.
- For \(q\ge4/3\), the lower value is an infimum on the degenerate boundary.
- No lower-area claim is made for arbitrary noncyclic flexible quadrilaterals.
- The upper fixed-variance product profile and the opposite sharp deficit bound are explicitly treated as prior work.
- Equivalent older symmetric-polynomial formulations may exist.
