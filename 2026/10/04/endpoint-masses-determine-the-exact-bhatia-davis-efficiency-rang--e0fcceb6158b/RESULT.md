# Endpoint masses determine the exact Bhatia–Davis efficiency range

## Finding

Let \(X\) be a finite nondegenerate random variable with distinct ordered atoms
\[
x_1<\cdots<x_m
\]
and fixed positive masses
\[
\Pr(X=x_i)=p_i,
\qquad
\sum_{i=1}^m p_i=1.
\]
Write
\[
\mu=\mathbb EX,
\qquad
\sigma^2=\operatorname{Var}(X),
\]
and define the Bhatia--Davis efficiency
\[
\eta(X)
=
\frac{\sigma^2}
{(x_m-\mu)(\mu-x_1)}.
\tag{1}
\]
The classical Bhatia--Davis inequality says
\[
\eta(X)\le1.
\]

Put
\[
a=p_1,
\qquad
c=p_m,
\]
and define
\[
\boxed{
\ell(a,c)
=
\frac{2\sqrt{ac}}
{\sqrt{ac}+\sqrt{(1-a)(1-c)}}.
}
\tag{2}
\]

For \(m=2\),
\[
\boxed{\eta(X)=1.}
\]

For \(m=3\), the exact attainable set is
\[
\boxed{
\eta(X)\in[\ell(a,c),1).
}
\tag{3}
\]
The lower endpoint is attained exactly when
\[
\boxed{
\frac{x_2-x_1}{x_3-x_1}
=
\frac{\sqrt{c(1-c)}}
{\sqrt{a(1-a)}+\sqrt{c(1-c)}}.
}
\tag{4}
\]

For every
\[
m\ge4,
\]
the exact attainable set is
\[
\boxed{
\eta(X)\in(\ell(a,c),1).
}
\tag{5}
\]
The lower endpoint is approached by collapsing all interior atoms toward the point in (4), while keeping them distinct. The upper endpoint is approached by collapsing all interior atoms toward either endpoint.

Every value strictly between the two sharp endpoints is attained.

A notable consequence is that the exact lower floor depends only on the two endpoint masses, not on how the remaining probability is divided among the interior categories.

For equal masses
\[
p_i=\frac1m,
\]
formula (2) becomes
\[
\boxed{
\ell=\frac2m.
}
\tag{6}
\]

## Assumptions and scope

The support is finite, every listed atom has positive mass, and the atoms are distinct.

The endpoint masses \(p_1\) and \(p_m\) are fixed together with the full probability profile; only the support locations vary.

The ratio in (1) is invariant under positive affine changes of the support, so the proof normalizes the endpoints to \(0\) and \(1\).

The result quantifies the tightness of the Bhatia--Davis bound. It does not optimize variance at a separately prescribed mean.

## Proof

Normalize
\[
x_1=0,
\qquad
x_m=1.
\]
Then
\[
\eta(X)=\frac{\sigma^2}{\mu(1-\mu)}.
\tag{7}
\]

Let
\[
a=p_1,
\qquad
c=p_m,
\qquad
b=1-a-c.
\]
If \(b=0\), then \(m=2\), the distribution is supported only at the endpoints, and equality holds in Bhatia--Davis:
\[
\eta=1.
\]

Assume now that
\[
b>0.
\]
Condition on the event that \(X\) is an interior atom, and let
\[
t=\mathbb E[X\mid 0<X<1].
\]
Then
\[
0<t<1,
\qquad
\mu=c+bt.
\tag{8}
\]
Writing the conditional interior variance as \(v_{\mathrm{int}}\),
\[
\mathbb E[X^2]
=
c+b(t^2+v_{\mathrm{int}}).
\]
Hence
\[
\sigma^2
=
c+bt^2-(c+bt)^2
+
b\,v_{\mathrm{int}}.
\tag{9}
\]
For fixed \(t\), the denominator in (7) is fixed, so (9) shows that the efficiency is minimized when the interior conditional variance vanishes.

It is therefore enough to study the collapsed three-level law with masses
\[
a,\ b,\ c
\]
at
\[
0,\ t,\ 1.
\]
For that law,
\[
\mu=c+bt
\]
and the exact identity
\[
\mu(1-\mu)-\sigma^2
=
b\,t(1-t)
\tag{10}
\]
gives
\[
\eta_0(t)
=
1-
b\,
\frac{t(1-t)}
{(c+bt)(1-c-bt)}.
\tag{11}
\]

Introduce the odds variable
\[
z=\frac{t}{1-t}>0.
\]
Since
\[
t=\frac{z}{1+z},
\]
a direct calculation gives
\[
\frac{t(1-t)}
{(c+bt)(1-c-bt)}
=
\frac{z}
{\bigl(c+(1-a)z\bigr)\bigl((1-c)+az\bigr)}.
\tag{12}
\]
Dividing the denominator in (12) by \(z\) yields
\[
a(1-a)z
+
\bigl(ac+(1-a)(1-c)\bigr)
+
\frac{c(1-c)}{z}.
\tag{13}
\]
By the arithmetic--geometric mean inequality,
\[
a(1-a)z+\frac{c(1-c)}{z}
\ge
2\sqrt{a(1-a)c(1-c)}.
\]
Thus
\[
\frac{t(1-t)}
{(c+bt)(1-c-bt)}
\le
\frac{1}
{\left(
\sqrt{ac}+\sqrt{(1-a)(1-c)}
\right)^2}.
\tag{14}
\]
Equality holds exactly when
\[
z
=
\sqrt{
\frac{c(1-c)}
{a(1-a)}
}.
\tag{15}
\]
Returning to \(t=z/(1+z)\), condition (15) is exactly (4).

Let
\[
S=
\sqrt{ac}+\sqrt{(1-a)(1-c)}.
\]
Equations (11)--(14) give
\[
\eta(X)
\ge
1-\frac{b}{S^2}.
\]
Since
\[
S^2-b
=
2\sqrt{ac}\,S,
\]
this lower bound is exactly
\[
\eta(X)\ge\ell(a,c).
\tag{16}
\]

The equality conditions are now explicit. Equality in (16) requires both the odds equality (15) and
\[
v_{\mathrm{int}}=0.
\]
For \(m=3\), there is only one interior atom, so the latter condition is automatic and the lower endpoint is attained precisely at (4). For \(m\ge4\), at least two distinct interior atoms have positive mass, so
\[
v_{\mathrm{int}}>0,
\]
and the lower inequality is strict. Clustering all interior atoms around the point in (4) proves sharpness of the lower infimum.

For the upper endpoint, the normalized Bhatia--Davis deficit is
\[
\mu(1-\mu)-\sigma^2
=
\mathbb E[X(1-X)].
\tag{17}
\]
If \(m\ge3\), at least one positive-mass atom lies strictly between \(0\) and \(1\), so the right side of (17) is positive and therefore
\[
\eta(X)<1.
\]
Letting all interior atoms approach \(0\), while keeping them distinct, makes the right side of (17) tend to zero and leaves
\[
\mu\to c\in(0,1).
\]
Hence
\[
\eta(X)\to1,
\]
so the upper endpoint is a sharp unattained supremum.

Finally, the open support simplex
\[
0<x_2<\cdots<x_{m-1}<1
\]
is connected, and \(\eta\) is continuous on it. Its image is therefore an interval. Combining the endpoint analysis proves (3) and (5), including attainment of every interior value.

## Verification

The accompanying exact-rational checker verifies the lower inequality after eliminating radicals, the Bhatia--Davis upper inequality, the conditional-variance reduction, and exact equality on a rational three-point family.

For positive
\[
\eta\le1,
\]
the lower inequality
\[
\eta\ge\ell(a,c)
\]
is equivalent to the rational certificate
\[
\eta^2(1-a)(1-c)
\ge
(2-\eta)^2ac.
\]
This makes the random replay exact rather than floating-point.

The checker also verifies lower-bound approach by clustered interior supports, upper-bound approach by endpoint collapse, and the equal-mass simplification.

The finite replay is supplementary. The universal statement follows from conditional variance, the one-variable odds optimization, and continuity.

## Relationship to prior work

The classical Bhatia--Davis inequality bounds
\[
\sigma^2
\le
(M-\mu)(\mu-m)
\]
for a bounded real random variable. Audenaert's full arXiv treatment reconstructs the classical real-variable argument before developing matrix generalizations. It optimizes over probability distributions subject only to a support interval and does not condition on prescribed masses at the two support endpoints.

Sharma, Gupta, and Kapoor study variance inequalities for a finite universe. Their full article states Bhatia--Davis alongside Popoviciu and von Szokefalvi--Nagy bounds, then develops refinements involving the harmonic mean and the third central moment. Their finite-universe setup uses equal weighting and does not derive the endpoint-mass efficiency floor (2).

Ellis studies the sharp maximum variance of an equally weighted finite sequence when its length, mean, minimum, and maximum are prescribed. His theorem corrects the Bhatia--Davis upper value by a term depending on the fractional part of the normalized mean times the sample size. That is a different constraint problem: the mean is fixed and all observations have equal weight. Here the endpoint probabilities are fixed, the mean is free to move with the support, and the object optimized is the ratio of the actual variance to its Bhatia--Davis bound.

Targeted searches using Bhatia--Davis efficiency, endpoint atom probabilities, fixed endpoint masses, and equivalent ratio formulations did not locate formula (2) or the complete attainable sets (3)--(5).

## Limitations

The result fixes positive endpoint masses. If either endpoint mass is allowed to tend to zero, the lower floor can tend to zero.

The support is finite. The proof extends to an arbitrary interior conditional distribution once positive endpoint atoms are fixed, but the attainment topology in (3)--(5) is stated for a finite list of distinct atoms.

The originality search was targeted. Older finite-population variance or moment-problem literature may contain an equivalent endpoint-mass ratio under different notation.

The original Bhatia--Davis Monthly article was only bibliographically accessible in the checked sources, so no whole-document noncoverage conclusion is made for it.

## References

1. K. M. R. Audenaert, “Variance bounds, with an application to norm bounds for commutators,” arXiv:0907.3913, first submitted 2009-07-22.
2. R. Sharma, M. Gupta, and G. Kapoor, “Some better bounds on the variance with applications,” *Journal of Mathematical Inequalities* 4 (2010), 355–363, DOI 10.7153/jmi-04-32.
3. J. L. Ellis, “The maximum variance of a finite sequence, given its mean, minimum, and maximum,” arXiv:2508.17525, first submitted 2025-08-24; later published in *The American Mathematical Monthly*.
4. R. Bhatia and C. Davis, “A Better Bound on the Variance,” *The American Mathematical Monthly* 107 (2000), 353–357, DOI 10.1080/00029890.2000.12005203.
