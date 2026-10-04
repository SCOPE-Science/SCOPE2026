# Review

## Correctness

PASS. The equality analysis follows the same normalization and support-parameter decomposition as the published proof. The low branch is strictly below \(4/21\) because
\[
\frac4{21}-\operatorname{cen}_y(P_w)
=-\frac{(w-2)(7w^3+17w^2+8w-28)}{21w(w^2+3w+4)}>0
\]
for \(1\le w\le w_0<2\). On the high branch the published comparison polynomial factors as
\[
f(w,z)=(w-2)q(w,z),
\]
and
\[
q(w,z)=28(w-1)\left(z-\frac{5w}{14(w-1)}\right)^2+
\frac{w^2(7w-8)(7w+18)}{7(w-1)}>0
\]
for \(w\ge w_0>8/7\). Hence equality forces \(w=2\), where the comparison construction is the single pentagon \(P_*\). The lower-star deletion is also strict whenever it removes positive area because all deleted points have nonpositive vertical coordinate while the extremal centroid is positive.

The only remaining possible loss is Steiner symmetrization. If the symmetrized body is \(P_*\), horizontal slice lengths are fixed. Convexity makes the slice-center function affine on each interval where the half-width is affine, and the three prescribed hexagon slices force those affine functions to vanish. Thus the original body equals \(P_*\) as well. Exact rational replay confirms the algebraic identities and the centroid \((0,4/21)\).

Risk: the argument uses Lassak’s published structural comparison decomposition as a premise rather than reconstructing every preliminary containment lemma independently. Those portions were inspected in full and the equality-critical steps were independently checked.

## Originality

PASS with residual literature risk. The primary article itself does not classify equality: after exhibiting the sharp pentagon it explicitly says that the author expects there are no more examples besides affine images of it. The present statement proves that expectation. Exact-form and alias searches for the constant, the affine-regular hexagon, the sharp pentagon, equality cases, and affine extremizers found no source stating the classification. Topic-adjacent later centroid-distance work uses affine-regular hexagons for a different invariant and does not supply this equality theorem.

Risk: a short equality observation could exist under different terminology or in an unindexed source. No claim of exhaustive bibliographic certainty is made.

## Value

PASS. Equality classification is a natural completion of a sharp geometric inequality and resolves an explicit expectation stated by the author of the primary theorem. The result is structural rather than a numerical recomputation: it identifies the entire extremal class, replaces numerical critical-point checks by exact factorizations, and shows that Steiner symmetrization introduces no hidden nonsymmetric extremizers.

Risk: no quantitative near-equality stability estimate is obtained.

Same-model review: passed. Independent audit: not yet performed.
