# Same-model review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

PASS.

The rectangular factor-mask formula follows from diagonalizing the
additive channel in matrix characters and averaging first over one
uniform factor.  For a dual matrix of rank \(s\), the Fourier coefficient
is exactly \(q^{-rs}\), so the maximum is \(q^{-r}\).

For uniform rank-ball masks, the square proof in the motivating paper
extends with an \((m-1)\times(n-1)\) lower-right block.  The character
sum recurrence is
\[
 \sum_{\operatorname{rank}M\le r}\chi_H(M)
 =
 q^r\sum_{\operatorname{rank}D=r}\chi_{H'}(D).
\]
The triangle bound is attained by rank-one \(H\), yielding
\(q^rC_{m-1,n-1}(r)/V_{m,n}(r)\).  The extension count
\(q^{2r}C_{m-1,n-1}(r)\le V_{m,n}(r)\) gives the \(q^{-r}\) upper bound.

The converse was rederived directly by counting kernel-vector
pairs for a uniform \(m\times n\) matrix.  The mean, variance, and
cross-moment give the exact fixed-rank correlation
\[
 \frac{q^{m+n-t}-q^m-q^n+1}
 {(q^m-1)(q^n-1)}.
\]
It specializes exactly to the square expression in Theorem 5 of
arXiv:2609.18876.  The factor-two simplification follows for
\(r\le\min(m,n)-2\).

The tensor-product claim for two independent masked inputs is the standard
singular-value rule for product conditional-expectation operators.  The
differential-privacy inequality is the square argument with \(mn\)
entries and the rectangular factor-count entropy bound
\((m+n)r\log_2q\); substituting \(m=n\) recovers the published square
formula.

Exact enumeration over \(\mathbb F_2\) verifies the rank-ball formula in
four small rectangular/square instances and verifies the kernel
correlation on all \(3\times4\) matrices for a rank-one mask.

## Originality

PASS, qualified **to the best of our knowledge**.

The motivating paper arXiv:2609.18876 formulates the multiplication
protocol for rectangular matrices but explicitly states its
maximal-correlation upper theorem, universal converse, individual
security theorem, and differential-privacy obstruction for square
\(n\times n\) inputs.  Its proof introduces the general rectangular
rank counts \(C_{d,e}(t)\) and \(V_{d,e}(r)\), but then specializes the
privacy calculations to \(C_n,V_n\).  No rectangular maximal-correlation
formula or rectangular converse is stated there.

Targeted searches for combinations of "low-rank masking", "rectangular",
"maximal correlation", "rank ball", "finite-field matrices", and
"rank-metric additive noise" located the motivating paper and generic
maximal-correlation literature, but no prior statement of the theorem
package above.  The current SCOPE archive was searched by the source
identifier, low-rank masking, rank-ball privacy, and maximal-correlation
terminology; no overlapping record was found, and recent repository
changes were checked directly.

There is an important residual risk: character spectra of rectangular
rank classes are classical objects in the bilinear-forms association
scheme, so an equivalent rank-ball Fourier identity may exist in that
literature.  That would not by itself cover the privacy converse,
the factor-two optimality statement, the two-upload law, or the
rectangular differential-privacy obstruction, but it weakens any claim
that the character identity alone is new.  No novelty is claimed for
the general association-scheme spectral machinery.

The motivating preprint was submitted on 16 September 2026, so a
near-simultaneous author revision or response not yet indexed is also a
material originality risk.

## Value

PASS.

The source protocol is intrinsically rectangular, while its strongest
privacy guarantees are square-only.  The result closes that mismatch
without changing the protocol, gives exact maximal correlation for both
mask samplers, proves an explicit dimension-dependent converse even
under secret invertible transformations, and shows that the
dimension-free \(q^{-r}\) scale remains asymptotically optimal whenever
the rank budget is small compared with the shorter side of the matrix.
For an actual \(m\times n\) by \(n\times p\) multiplication, it also
identifies the weaker mask rank as the exact bottleneck for factor
masks.  The rectangular DP formula supplies a complementary
privacy boundary in terms of the harmonic aspect-ratio scale
\(mn/(m+n)\).

## Review status

This is a same-model scientific review, not independent validation or
peer review.  No cross-model review has been performed.
