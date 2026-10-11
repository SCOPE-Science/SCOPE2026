# Review of Exact radial Schwarzian profile of the Lehtinen witness family

## Correctness

PASS. The cited 2026 source gives the exact formula
\[
S_{f_\alpha}(z)
=
\frac{1-\alpha^2}{2(1-z)^2}
+
\frac{(1-\alpha)\overline z}
{(1-|z|^2)(1-z)}
-
\frac{3\overline z^2}
{2(1-|z|^2)^2}.
\]
After multiplication by
\[
(1-|z|^2)^2,
\]
the only geometric factor is
\[
w=(1-|z|^2)/(1-z).
\]
For
\[
|z|=r,
\]
the sharp inequality
\[
|w|\le1+r
\]
has equality only at
\[
z=r.
\]
Because all coefficients have the same sign there, the triangle-inequality upper bound is attained exactly. This proves the circlewise maximum and the global norm.

The exact deficit is direct algebra. For an arbitrary extremizing sequence, the monotone radial profile forces
\[
|z_j|\to1,
\]
and the positive coefficient of
\[
|w|^2
\]
forces
\[
|w_j|\to2.
\]
The equality geometry of the reverse triangle inequality then forces
\[
z_j\to1.
\]

## Originality

PASS. The complete open-access 2026 article was inspected at the harmonic Schwarzian definition, Theorem 1, the explicit witness calculation, its two conjectures, and the references to the original non-univalent construction. The paper states only the upper estimate needed for
\[
\sigma_H(\mathbb D)\le3/2;
\]
it does not state equality, the exact circle profile, or extremizing-sequence concentration.

The original Wang--Liu--Rasila--Sun paper supplies the non-injective family but predates its use in the harmonic Schwarzian inner-radius problem. The general harmonic Schwarzian literature supplies the formalism rather than this family-specific extremal computation.

Dedicated published-finding and public-literature searches under the exact family, the harmonic Schwarzian norm, the formula
\[
2\alpha^2+2\alpha-\frac52,
\]
and boundary concentration at
\[
1
\]
did not locate an implication-equivalent statement.

## Value

PASS. The family
\[
f_\alpha
\]
is not an arbitrary example: it is the specific witness used to establish the best currently published upper bound
\[
\sigma_H(\mathbb D)\le3/2
\]
and motivates the source's conjecture that equality holds.

The exact profile shows that the source estimate has no hidden slack at any
\[
\alpha>1,
\]
not merely in the limit. It also identifies a rigid geometric mechanism: the complete norm is generated at one cusp boundary point, with an exact radial deficit and an exact threshold approach
\[
3/2+6(\alpha-1)+2(\alpha-1)^2.
\]
These data are relevant to any compactness or extremal analysis aimed at the conjectured threshold.

Same-model review: passed. Independent audit: not yet performed.
