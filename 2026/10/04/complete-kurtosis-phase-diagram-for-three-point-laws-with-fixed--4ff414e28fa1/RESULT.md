# Complete kurtosis phase diagram for three-point laws with fixed masses

## Finding

Fix
\[
a,b,c>0,
\qquad
a+b+c=1,
\]
and let \(X\) have three distinct ordered atoms
\[
x_1<x_2<x_3
\]
with respective masses \(a,b,c\). Define the Pearson kurtosis
\[
\kappa(X)
=
\frac{\mathbb E[(X-\mathbb EX)^4]}
{\operatorname{Var}(X)^2}.
\]

Because kurtosis is invariant under positive affine changes of support, normalize
\[
(x_1,x_2,x_3)=(0,t,1),
\qquad
0<t<1.
\]
Set
\[
h(u)=\frac1{u(1-u)}-3,
\]
\[
s_2=ab+bc+ca,
\qquad
s_3=abc.
\]

If
\[
a=b=c=\frac13,
\]
then
\[
\boxed{\kappa(t)=\frac32}
\]
for every \(0<t<1\).

Assume now that the mass profile is not uniform.

If
\[
a<\frac13
\quad\text{and}\quad
c<\frac13,
\]
then there is a unique interior minimum at
\[
t_*=\frac{1-3c}{3b-1},
\]
and
\[
\boxed{
\kappa_*=
\frac{1-3s_2}{s_2-9s_3}.
}
\]
The exact attainable set is
\[
\boxed{
\left[
\kappa_*,
\max\{h(a),h(c)\}
\right).
}
\tag{1}
\]

If
\[
a>\frac13
\quad\text{and}\quad
c>\frac13,
\]
then the same \(t_*\) is the unique interior maximum, and the exact attainable set is
\[
\boxed{
\left(
\min\{h(a),h(c)\},
\kappa_*
\right].
}
\tag{2}
\]

In every remaining nonuniform case, there is no interior stationary point and
\[
\boxed{
\kappa(t)\in
\left(
\min\{h(a),h(c)\},
\max\{h(a),h(c)\}
\right).
}
\tag{3}
\]

The two boundary values are sharp but unattained for a genuine three-point law:
\[
\lim_{t\downarrow0}\kappa(t)=h(c),
\qquad
\lim_{t\uparrow1}\kappa(t)=h(a).
\]
They are precisely the kurtoses of the two-level laws obtained by merging the lower or upper adjacent pair.

Thus the endpoint masses have a sharp phase transition at \(1/3\): two small endpoint masses force one interior minimum, two large endpoint masses force one interior maximum, and mixed endpoint regimes force monotonicity.

At the stationary support, the centered atom vector is, up to a nonzero scalar and an overall sign,
\[
(b-c,\ c-a,\ a-b).
\]
This gives a coordinate-free description of the unique extremal support shape.

## Assumptions and scope

The three probabilities are fixed and strictly positive. Only the ordered support locations vary.

Kurtosis means the fourth standardized central moment, not excess kurtosis. Subtracting \(3\) would translate every displayed value but would not change the phase diagram.

The support atoms are distinct. The two-level laws occur only as boundary limits.

The result is a complete classification for three support points. No claim is made here for four or more prescribed atoms.

## Proof

Under the normalization
\[
(x_1,x_2,x_3)=(0,t,1),
\]
the mean is
\[
\mu=bt+c.
\]
The variance can be written without expansion as
\[
V(t)
=
ab\,t^2+ac+bc(1-t)^2.
\tag{4}
\]
Let
\[
M_4(t)=\mathbb E(X-\mu)^4,
\qquad
\kappa(t)=\frac{M_4(t)}{V(t)^2}.
\]

Direct differentiation and simplification give the exact factorization
\[
\boxed{
\kappa'(t)
=
\frac{
4abc\,t(1-t)
}{
V(t)^3
}
\left[
(3b-1)t+(3c-1)
\right].
}
\tag{5}
\]
Every factor outside the final bracket is strictly positive for \(0<t<1\). Hence all shape information is carried by one affine function.

The bracket vanishes at
\[
t_*=\frac{1-3c}{3b-1}.
\tag{6}
\]
An interior root exists exactly when \(a\) and \(c\) lie on the same strict side of \(1/3\).

Indeed, if \(a,c<1/3\), then \(b>1/3\). The bracket in (5) is negative at \(t=0\) and positive at \(t=1\), so \(t_*\) is a unique minimum.

If \(a,c>1/3\), then \(b<1/3\). The bracket is positive at \(t=0\) and negative at \(t=1\), so \(t_*\) is a unique maximum.

If the endpoint masses do not lie on the same strict side of \(1/3\), the affine bracket has no zero in \((0,1)\), except that for
\[
a=b=c=\frac13
\]
it vanishes identically. Thus every nonuniform remaining profile is strictly monotone.

Substitution of (6) into the fourth standardized moment yields
\[
\kappa(t_*)
=
\frac{1-3(ab+bc+ca)}
{ab+bc+ca-9abc},
\]
which is the stated \(\kappa_*\). The denominator is positive in the two nonuniform stationary regimes because it is the positive variance factor arising from the nonconstant stationary support.

For the boundary values, setting \(t=0\) merges the first two atoms. The upper level then has mass \(c\), so the resulting Bernoulli kurtosis is
\[
h(c)=\frac1{c(1-c)}-3.
\]
Similarly,
\[
\kappa(1)=h(a).
\]
These boundary laws are not allowed because the three atoms must remain distinct, but they are approached as \(t\downarrow0\) and \(t\uparrow1\).

Equations (1)--(3) now follow from the derivative classification and continuity.

For the stationary support description, a constrained stationary point of the fourth central moment at fixed mean and variance satisfies
\[
4y_i^3=\lambda+2\eta y_i
\]
for the centered atom locations \(y_i\). Hence the three centered support values are the roots of one depressed cubic and their unweighted sum is zero. Together with
\[
ay_1+by_2+cy_3=0,
\]
this determines their direction as
\[
(y_1,y_2,y_3)
\propto
(b-c,\ c-a,\ a-b),
\]
up to overall sign and scale.

## Verification

The accompanying exact-rational checker differentiates the fourth standardized moment independently through moment derivatives and compares it to the factorization (5) for random rational profiles.

It verifies the two exact Bernoulli boundary values, the uniform identity \(\kappa=3/2\), the stationary location \(t_*\), the closed formula for \(\kappa_*\), and the minimum/maximum sign changes in thousands of rational examples.

Finite replay supports the algebra but does not replace the universal factorization proof.

## Relationship to prior work

Classical work on skewness and kurtosis establishes distribution-free relations between standardized third and fourth moments. Móri, Rohatgi, and Székely give a short full-text treatment of sharp skewness--kurtosis inequalities and their multivariate analogues. Their theorem is formulated over general distributions and does not condition on a fixed three-atom probability profile or vary the numerical support.

Sharma and Bhandari give Newton-inequality proofs of classical skewness--kurtosis bounds. Their archive preprint is the literature anchor for this direction. Its accessible abstract states general moment inequalities; it does not state a fixed-mass three-point phase diagram.

A modern full-text treatment by Jammalamadaka, Taufer, and Terdik systematically reviews cumulant-based skewness and kurtosis measures and their relations. It likewise treats distributions or parametric families as given rather than optimizing a three-level numerical coding under prescribed probabilities.

The equal-weight identity
\[
\kappa=\frac32
\]
for three equally weighted values is elementary and has circulated independently. The contribution here is the complete arbitrary-weight classification, including the \(1/3\) phase transition, the exact stationary support, and the closed extremal value.

Targeted searches using three-point distributions, fixed probabilities, weighted three values, standardized fourth moments, categorical scores, and support optimization did not locate formulas (1)--(6) as a prior theorem.

## Limitations

The theorem concerns exactly three ordered support points. Higher support cardinality produces more geometric degrees of freedom and is not covered.

The boundary kurtoses are limits of two-level coarsenings and are not attained by distinct three-point supports.

The originality search was targeted. An equivalent result could exist in older moment-space, weighted-data, or categorical-scoring literature under different terminology.

## References

1. R. Sharma and R. Bhandari, “Skewness, kurtosis and Newton's inequality,” arXiv:1309.2896, first submitted 2013-09-11; later *Rocky Mountain Journal of Mathematics* 45 (2015), 1639–1643.
2. T. F. Móri, V. K. Rohatgi, and G. J. Székely, “On multivariate skewness and kurtosis,” *Theory of Probability and Its Applications* 38, 547–551, DOI 10.1137/1138055.
3. V. K. Rohatgi and G. J. Székely, “Sharp inequalities between skewness and kurtosis,” *Statistics & Probability Letters* 8 (1989), 297–299.
4. S. R. Jammalamadaka, E. Taufer, and G. H. Terdik, “On Multivariate Skewness and Kurtosis,” *Sankhya A* 83 (2021), 607–644, DOI 10.1007/s13171-020-00211-6.
