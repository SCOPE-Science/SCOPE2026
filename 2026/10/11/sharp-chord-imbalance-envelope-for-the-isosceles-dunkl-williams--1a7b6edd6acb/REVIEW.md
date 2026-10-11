# Same-model review

## Correctness
PASS. After a sign change, write \(a=\|x+y\|\ge b=\|x-y\|\) and \(r=b/a\). The unit-pair integrand is bounded by
\[
\frac{1+r}{2}\bigl(2+a(1-r)\bigr)
\le
(1+r)(2-r).
\]
For every \(0<r\le1\), the pair
\[
x_r=(1,1-2r),
\qquad
y=(1,1)
\]
in \(\ell_\infty^2\) has chord ratio exactly \(r\) and attains \((1+r)(2-r)\), so the conditional envelope is exact. Tracing equality through the three sharp inequalities shows that global equality requires and is implied by the stated three norm identities after a sign choice.

## Originality
PASS. The defining Fu--Xie--Li paper and the closest 2026 public sharp-bound result were inspected in full where relevant. The latter already contains the upper polynomial \(2+r-r^2\), so that inequality is not claimed as new. It gives only the global \(9/4\) theorem and expressly does not classify equality cases. Targeted searches found no source proving pointwise attainability for every \(r\), the resulting optimal stability law, or the necessary-and-sufficient pairwise equality criterion. The current own ledger through g000062 contains no such isosceles Dunkl--Williams profile.

## Value
PASS. The parameter \(r\) is the intrinsic sum/difference imbalance in the sharp global proof. Establishing the exact conditional supremum turns the one-number theorem into a best-possible stability profile and determines exactly how far a pair with unbalanced chords must lie below \(9/4\). The equality criterion also closes the most immediate structural limitation left by the prior sharp-bound result.

## Closest literature and limitations
Fu, Xie and Li introduced \(DW_I\), proved the unit-pair formula, and computed \(DW_I(\ell_\infty^2)=9/4\). A later public result proved the universal \(9/4\) bound and already derived the polynomial upper estimate used here. The new claim is restricted to pointwise sharpness of that estimate, its stability consequence, and equality of individual pairs. It does not classify spaces whose supremum is \(9/4\) but is not attained.

Same-model review: passed. Independent audit: not yet performed.
