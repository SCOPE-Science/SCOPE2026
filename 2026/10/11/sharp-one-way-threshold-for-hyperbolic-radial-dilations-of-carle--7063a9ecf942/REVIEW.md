# Review of Sharp one-way threshold for hyperbolic radial dilations of Carleson interpolation

## Correctness

PASS. In hyperbolic polar coordinates, the inverse of
\[
D_a(R,\theta)=(aR,\theta)
\]
has radial stretch
\[
1/a
\]
and tangential stretch
\[
\sinh(R/a)/\sinh R.
\]
For
\[
a\ge1,
\]
convexity of \(\sinh\) bounds both stretches by \(1/a\), so the inverse is globally \(1/a\)-Lipschitz in the hyperbolic metric. Hence every pseudohyperbolic pair distance, and therefore every factor in Carleson's product-separation criterion, can only increase.

For
\[
0<a<1,
\]
the two-point packet construction has fixed source separation and geometrically decreasing boundary depths, so the source packet lemma makes the union interpolating. The corresponding image-pair distance is governed by
\[
\sinh(aR_n)/\sinh R_n\to0,
\]
which destroys pairwise separation. All quantifiers, endpoint cases, and the inverse relation
\[
D_a^{-1}=D_{1/a}
\]
were checked.

## Originality

PASS. The 2026 primary paper states the general continuous-preserver characterizations and treats only the single hyperbolic radial dilation
\[
a=2
\]
as its smooth one-way example. It does not state the full parameter classification.

The closest earlier theorem concerns quasiconformal preservers. The nonidentity members of this hyperbolic radial family are not quasiconformal because their Euclidean radial-to-tangential distortion is unbounded at the boundary.

Searches under hyperbolic radial dilation, the explicit \(\tanh(a\operatorname{artanh}r)\) formula, the source identifier, and one-way interpolation preservation did not locate the exact threshold theorem. A separate recent result on radial quasiconformal twists concerns angular twisting with fixed radius and does not imply the radial-dilation phase diagram.

## Value

PASS. The fresh paper uses the member \(a=2\) to demonstrate that one-way and bidirectional preservation differ, but leaves that witness isolated.

The accepted result turns it into a natural exact classification of the full multiplicative hyperbolic-dilation semigroup. The threshold
\[
a=1
\]
separates all forward preservers from all failures, while the bidirectional class meets the semigroup only at the identity. This gives a clean structural model of the asymmetry identified by the source rather than a routine perturbation of its numerical example.

Same-model review: passed. Independent audit: not yet performed.
