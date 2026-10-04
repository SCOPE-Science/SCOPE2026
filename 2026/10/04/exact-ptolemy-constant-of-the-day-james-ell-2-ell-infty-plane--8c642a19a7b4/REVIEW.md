# Same-model review

## Claim
For the real Day--James plane \(X=\ell_2-\ell_\infty\), with \(\|(u,v)\|_{2,\infty}=\sqrt{u^2+v^2}\) when \(uv\ge0\) and \(\|(u,v)\|_{2,\infty}=\max\{|u|,|v|\}\) when \(uv\le0\), the Ptolemy constant is exactly \(C_{\mathrm{Pt}}(X)=3/2\).

## Correctness
**PASS.** The Hilbert norm
\[
H(u,v)=\frac12\sqrt{3u^2+2uv+3v^2}
\]
satisfies the exact global inequalities
\[
H\le\|\cdot\|_{2,\infty}\le\sqrt{3/2}\,H.
\]
Each inequality is verified separately on the two sign regions by factorization into nonnegative polynomial expressions. Hilbert Ptolemy therefore gives the upper bound \(3/2\). The triple \((-1,-1),(2,-2),(1,-3)\) has numerator \(9\) and denominator \(6\), so the upper bound is attained.

## Originality
**PASS, with an explicit access residual.** The exact-object 2013 source computes the Dunkl--Williams constant rather than the Ptolemy constant. After transforming the norm to an absolute normalized norm, the Euclidean comparison ratio is maximized at \(t=2-\sqrt2\), so the midpoint exactness hypothesis in Zuo (2012) does not imply equality. The inspected later 2018 off-midpoint comparison theorems impose symmetry absent from this associated function.

A 2015 reconsideration by Zuo states in its abstract that it gives additional sufficient conditions. Its readable full text could not be obtained through bounded open-access, arXiv, and institutional retrieval attempts. This source is therefore retained as an unresolved coverage risk rather than counted as evidence of novelty.

## Value
**PASS.** This determines a standard geometric invariant for an established Day--James plane already used as a benchmark for exact Banach-space constants. The proof is structural: the sharp value is the square of a best Hilbert-comparison factor and is independently attained by an explicit Ptolemy configuration.

## Closest literature and limitations
The closest inspected sources are Mizuguchi--Saito--Tanaka (2013), Zuo (2012), and Zuo (2018). Zuo (2015) remains access-limited. The claim is confined to the real two-dimensional \(\ell_2-\ell_\infty\) Day--James norm and does not assert a formula for general \(p,q\).

Same-model review: passed. Independent audit: not yet performed.
