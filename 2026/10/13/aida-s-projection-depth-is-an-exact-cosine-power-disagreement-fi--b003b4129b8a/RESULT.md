# Aida's projection depth is an exact cosine-power disagreement filter
## Finding

Aida modifies AdaBelief by repeatedly projecting the layerwise momentum and current gradient onto one another before using their squared difference to update the second moment. The defining paper proves that these projections do not increase the discrepancy and argues qualitatively that increasing the projection depth makes the adaptive stepsizes more compact.

The projection geometry has an exact angle law.

Let
\[
m^{(0)}=m\ne0,
\qquad
g^{(0)}=g\ne0,
\]
and define
\[
c=
\frac{|\langle m,g\rangle|}
{\lVert m\rVert_2\lVert g\rVert_2}
\in[0,1].
\]
For projection regularizer
\[
\xi\ge0,
\]
the Aida recursion is
\[
m^{(k+1)}
=
\frac{\langle g^{(k)},m^{(k)}\rangle}
{\lVert g^{(k)}\rVert_2^2+\xi}
g^{(k)}
\]
and
\[
g^{(k+1)}
=
\frac{\langle g^{(k)},m^{(k)}\rangle}
{\lVert m^{(k)}\rVert_2^2+\xi}
m^{(k)}.
\]

Whenever both projected vectors are nonzero, their signed angle is unchanged. Writing
\[
M_k=\lVert m^{(k)}\rVert_2,
\qquad
G_k=\lVert g^{(k)}\rVert_2,
\]
their norms satisfy the exact scalar recurrences
\[
\boxed{
M_{k+1}
=
cM_k
\frac{G_k^2}{G_k^2+\xi},
}
\]
and
\[
\boxed{
G_{k+1}
=
cG_k
\frac{M_k^2}{M_k^2+\xi}.
}
\]

Hence, for every
\[
K\ge1,
\]
\[
\boxed{
M_K\le c^K M_0,
\qquad
G_K\le c^K G_0.
}
\]
For positive \(\xi\), each nonzero factor is strictly smaller than the corresponding zero-regularizer value.

In the projection limit
\[
\xi=0,
\]
the norm relations become exact:
\[
M_K=c^K M_0,
\qquad
G_K=c^K G_0.
\]
Because the signed angle is also invariant,
\[
\boxed{
\lVert m^{(K)}-g^{(K)}\rVert_2
=
c^K
\lVert m-g\rVert_2.
}
\]

Therefore the total layerwise squared discrepancy used as Aida's second-moment innovation obeys
\[
\boxed{
\frac{
\lVert m^{(K)}-g^{(K)}\rVert_2^2
}{
\lVert m-g\rVert_2^2
}
=
c^{2K}
}
\]
when the tiny division regularizer is neglected.

For the source choice
\[
K=2,
\]
the idealized innovation-energy factor is exactly
\[
\boxed{c^4.}
\]

This exposes two sharp endpoints. If
\[
m\perp g,
\]
then the first projection has zero numerator and
\[
m^{(1)}=g^{(1)}=0
\]
for every
\[
\xi\ge0.
\]
The projected second-moment innovation vanishes immediately.

At the opposite endpoint, if \(m\) and \(g\) are collinear and
\[
\xi=0,
\]
then
\[
c=1
\]
and the projection does not suppress their discrepancy at all.

Thus Aida's projection depth is an angle-selective filter: it strongly suppresses disagreement when momentum and gradient are nearly orthogonal, but its suppression becomes arbitrarily weak as they approach collinearity.

## Assumptions and scope

The theorem isolates the mutual-projection subroutine that defines Aida's difference from AdaBelief.

The source algorithm uses a very small positive projection regularizer. The exact cosine-power discrepancy identity is stated for the zero-regularizer projection limit. For positive regularizer, the exact norm recurrences above remain valid and give the displayed cosine-power upper bounds on both projected norms.

The theorem concerns the layerwise Euclidean discrepancy energy. Aida stores coordinatewise squares of the projected discrepancy, so the result controls their layerwise sum rather than each coordinate separately.

The result does not assert a full optimization convergence rate. It quantifies the mechanism by which projection depth changes the second-moment innovation at one iteration.

## Proof

Let
\[
q_k=\langle g^{(k)},m^{(k)}\rangle.
\]
The two updates are scalar multiples of \(g^{(k)}\) and \(m^{(k)}\), respectively. Multiplying both directions by scalars with the same sign preserves the signed cosine of the angle whenever the vectors remain nonzero.

Since
\[
|q_k|
=
cM_kG_k,
\]
taking norms gives
\[
M_{k+1}
=
\frac{|q_k|G_k}{G_k^2+\xi}
=
cM_k\frac{G_k^2}{G_k^2+\xi},
\]
and similarly
\[
G_{k+1}
=
cG_k\frac{M_k^2}{M_k^2+\xi}.
\]

Because each rational factor is at most one,
\[
M_{k+1}\le cM_k,
\qquad
G_{k+1}\le cG_k.
\]
Iteration proves
\[
M_K\le c^KM_0,
\qquad
G_K\le c^KG_0.
\]

Now set
\[
\xi=0.
\]
Then
\[
M_K=c^KM_0,
\qquad
G_K=c^KG_0.
\]
Let
\[
s=
\frac{\langle m,g\rangle}
{\lVert m\rVert_2\lVert g\rVert_2}
\]
be the signed cosine. Since \(s\) is preserved,
\[
\lVert m^{(K)}-g^{(K)}\rVert_2^2
=
M_K^2+G_K^2-2sM_KG_K.
\]
Substituting the common factor gives
\[
\lVert m^{(K)}-g^{(K)}\rVert_2^2
=
c^{2K}
\left(
M_0^2+G_0^2-2sM_0G_0
\right),
\]
which is
\[
c^{2K}\lVert m-g\rVert_2^2.
\]

The orthogonal endpoint follows directly from \(q_0=0\). The collinear zero-regularizer endpoint has \(c=1\), so the discrepancy factor is one.

## Verification

The accompanying `verify.py` reconstructs the source mutual-projection recurrence directly.

It checks signed-angle invariance, both exact norm recurrences for positive projection regularizer, the cosine-power norm bounds, the exact zero-regularizer discrepancy law over randomized vector pairs and projection depths, the source-default \(K=2\) fourth-power energy law, and the orthogonal and collinear endpoint cases.

These computations are transcription guards. The identities and inequalities are proved analytically above.

## Relationship to prior work

Zhang, Niwa, and Kleijn introduce Aida by applying repeated mutual layerwise projections to the current gradient and first momentum before forming the AdaBelief-style squared discrepancy. Their defining equations are exactly the two projection recurrences used here.

The source proves that each projected vector is no longer than before, observes that the angle is unchanged, and concludes that the discrepancy norm is nonincreasing. It then argues that increasing the projection depth drives the scalar coefficients multiplying the original gradient and momentum toward zero when the layerwise angle is nonzero.

Those statements motivate the present question but do not give the exact dependence on the angle. The inspected full text does not state the cosine-power norm law, the exact factor
\[
c^{2K}
\]
for total discrepancy energy in the zero-regularizer limit, or the resulting \(c^4\) law at the source default \(K=2\).

Focused published-record searches for Aida, mutual projection depth, cosine contraction, angle-dependent adaptive-step suppression, and equivalent discrepancy formulas did not identify an implication-equivalent result.

## Limitations

The exact discrepancy multiplier uses the zero-regularizer projection limit; the practical source uses a tiny positive regularizer.

The theorem controls layerwise total squared discrepancy, not coordinatewise dispersion of Aida's second-moment vector.

The result does not classify the subsequent EMA dynamics or parameter trajectory.

The underlying projection identity is elementary Euclidean geometry; the scientific content here is its exact implication for Aida's defining depth parameter and second-moment innovation.

## References

1. Guoqiang Zhang, Kenta Niwa, and W. Bastiaan Kleijn, “A DNN Optimizer that Improves over AdaBelief by Suppression of the Adaptive Stepsize Range,” arXiv:2203.13273v1, first submitted 2022-03-24; later accepted by TMLR.
