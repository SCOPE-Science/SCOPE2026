# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The argument was checked separately at the three structural points on which the result depends.

First, under a two-coordinate balancing step with fixed sum \(S=x+y\), the terms containing exactly one of the two coordinates occur in pairs
\[
\sqrt{P_J}\left[\sqrt{x(R_J+y)}+\sqrt{y(R_J+x)}\right].
\]
Writing \(T=xy\), the square of the bracket is
\[
R_JS+2T+2\sqrt{T(R_J^2+R_JS+T)},
\]
which is strictly increasing in \(T\). Terms containing neither coordinate are fixed and terms containing both carry a factor \(\sqrt{xy}\). This proves strict increase under every nontrivial equalizing transfer. The same decomposition also verifies strict increase when one block is split into two positive blocks.

Second, the identity
\[
\sum_{|I|=d-1}
\left(\prod_{i\in I}b_i\right)
\left(n-\sum_{i\in I}b_i\right)
=
d\,e_d(b)
\]
was checked combinatorially: each \(d\)-subset contributes its full product once for each choice of the distinguished omitted coordinate. Cauchy--Schwarz and Maclaurin then give exactly
\[
W_d(b)
\le
\binom q{d-1}\sqrt{q-d+1}(n/q)^{d/2}.
\]
Equal block sizes attain equality.

Third, for
\[
V=\sum_i(b_i-n/q)^2,
\]
the exact identity
\[
\frac{e_2(b)}
{\binom q2(n/q)^2}
=
1-\frac{qV}{(q-1)n^2}
\]
combined with Maclaurin monotonicity from order \(2\) to order \(d\) yields the stated exponent \(d/4\) in the stability inequality.

Endpoint cases \(q=d\), \(q=n\), and nondivisible \(n\) were checked against the explicit balanced-block formula. The result is deliberately restricted to \(d\ge2\), since \(d=1\) gives the partition-independent value \(\sqrt n\).

## Originality

**PASS, to the best of our knowledge.**

The full accessible text of arXiv:2609.19473 was inspected at its definition of \(w_d\), its block-count corollary, its equal-block example, and its sharpness discussion. It proves a coarse \(q^{(d-1)/2}n^{d/2}\) block-count bound and evaluates equal blocks, but it does not prove that equal blocks maximize \(w_d\), does not state Schur concavity or refinement monotonicity, does not give the exact integer envelope, and does not give a quantitative near-equality theorem. Its sharpness paragraph explicitly says that no optimality is asserted for \(w_d\) when the number of blocks is greater than \(d\), or for the complete dependence on the number of blocks.

Searches using the source identifier and combinations of the terms `product-profile`, `multi-affine`, `block partition`, `balanced blocks`, `majorization`, `Schur concavity`, `elementary symmetric`, and `anti-concentration` did not locate an equivalent theorem. The older anti-concentration works cited by the source paper use coefficient, measure, or tensor normalizations rather than this newly introduced block invariant.

No inaccessible source was identified that is specifically known to use the invariant \(w_d\). The principal residual risk is unindexed contemporaneous work, because the source preprint introducing the invariant is very recent. The classical theory of majorization and Maclaurin inequalities supplies tools used in the proof, but no located source applies them to this product-profile scale.

The equal-block evaluation already present in arXiv:2609.19473 is not claimed as new.

## Value

**PASS.**

The result replaces the source paper's degree-dependent coarse block-count reduction by the exact extremal envelope of its structural invariant for every integer triple \((n,q,d)\). It simultaneously sharpens the block-count versions of the source small-ball, density, and quotient-Remez estimates, identifies refinement and balancing as the governing geometry of the scale, and gives a global quantitative rigidity statement for near-extremizers.

The scientific scope is intentionally narrower than an optimal anti-concentration theorem for \(q>d\): the result optimizes the structural invariant used by the source theorem, not the underlying concentration function over the full polynomial class.
