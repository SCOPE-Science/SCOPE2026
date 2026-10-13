# Exact state-count positivity law for ROS2 on serial decay chains

## Finding
Let \(N_n\) be the nilpotent lower shift,
\[
(N_n)_{i+1,i}=1,
\qquad
N_n^n=0,
\]
and consider the positive linear system
\[
u'=J_nu,
\qquad
J_n=-I+N_n.
\]
Because \(J_n\) is Metzler,
\[
e^{tJ_n}
=
e^{-t}
\sum_{k=0}^{n-1}\frac{t^k}{k!}N_n^k
\]
is entrywise nonnegative for every \(t\ge0\).

Apply the standard L-stable two-stage Rosenbrock method ROS2 with exact Jacobian and
\[
\gamma=1+\frac1{\sqrt2}.
\]
Its one-step matrix is \(R(hJ_n)\), where
\[
R(z)
=
\frac{1-(1+\sqrt2)z}
{\left(1-\left(1+\frac1{\sqrt2}\right)z\right)^2}.
\]

For every \(h>0\),
\[
\boxed{
R(hJ_n)\ge0
\quad\Longleftrightarrow\quad
n\le2+\sqrt2+(3+2\sqrt2)h.
}
\]
Equivalently:

- for \(n\le3\), ROS2 is positivity preserving for every \(h\ge0\);
- for every \(n\ge4\),
\[
R(hJ_n)\ge0
\quad\Longleftrightarrow\quad
h=0
\ \text{or}\ 
h\ge h_n,
\]
where
\[
h_n
=
3n-2-(2n-1)\sqrt2.
\]

The first failing dimension is \(n=4\), and its exact recovery threshold is
\[
h_4=10-7\sqrt2\approx0.1005050634.
\]
Thus positivity is re-entrant: the zero step is positive, every sufficiently small positive step fails, and a sufficiently large step restores positivity.

## Assumptions and scope
The matrix \(J_n\) is the unit-rate serial decay chain with terminal leakage. It is Metzler and Hurwitz. The claim concerns the end-of-step map of ROS2 with the exact Jacobian on this linear autonomous problem.

The ROS2 parameter is the larger L-stable value
\[
\gamma=1+\frac1{\sqrt2},
\]
used in the original atmospheric-chemistry construction. The smaller L-stable branch is not classified here.

The result concerns componentwise nonnegativity of the completed ROS2 step. It does not assert internal-stage positivity, nonlinear positivity, positivity for arbitrary Metzler matrices, or a general absolute-monotonicity radius.

## Proof
For the L-stable ROS2 branch, the quadratic numerator coefficient in the general stability function vanishes. Writing
\[
a=\gamma=1+\frac1{\sqrt2},
\qquad
c=2\gamma-1=1+\sqrt2,
\]
gives
\[
R(z)=\frac{1-cz}{(1-az)^2}.
\]
The partial-fraction decomposition is
\[
R(z)
=
\frac{c/a}{1-az}
+
\frac{(1-a)/a}{(1-az)^2}.
\]
Therefore, for every integer \(k\ge0\),
\[
R^{(k)}(z)
=
\frac{k!a^{k-1}}
{(1-az)^{k+2}}
\left[
c(1-az)+(k+1)(1-a)
\right].
\]
At \(z=-h\) with \(h\ge0\), the denominator and the prefactor outside the bracket are positive. Hence
\[
\operatorname{sgn}R^{(k)}(-h)
=
\operatorname{sgn}
\left(
c(1+ah)+(k+1)(1-a)
\right).
\]
Multiplying the bracket by the positive number \(\sqrt2\) yields
\[
1+\sqrt2-k+(3+2\sqrt2)h.
\]
This quantity is strictly decreasing in \(k\).

Since
\[
hJ_n=-hI+hN_n
\]
and \(N_n\) is nilpotent, analytic functional calculus gives the finite Taylor identity
\[
R(hJ_n)
=
\sum_{k=0}^{n-1}
\frac{h^k}{k!}R^{(k)}(-h)N_n^k.
\]
The matrices \(N_n^k\) have disjoint nonzero subdiagonals. For \(h>0\), the \(k\)-th subdiagonal coefficient therefore has exactly the sign of \(R^{(k)}(-h)\). Thus
\[
R(hJ_n)\ge0
\]
if and only if
\[
R^{(k)}(-h)\ge0
\qquad
(0\le k\le n-1).
\]
Because the sign factor decreases with \(k\), it is enough and necessary to check \(k=n-1\):
\[
2+\sqrt2-n+(3+2\sqrt2)h\ge0.
\]
This proves
\[
n\le2+\sqrt2+(3+2\sqrt2)h.
\]

For \(n\le3\), the left side at \(h=0\) is already positive, so all \(h\ge0\) are safe. For \(n\ge4\), solving the equality for \(h\) gives
\[
h_n
=
\frac{n-2-\sqrt2}{3+2\sqrt2}
=
3n-2-(2n-1)\sqrt2.
\]
At \(h=0\), the step is \(R(0)I=I\), so zero remains an isolated positive point below the positive threshold.

For \(n=4\),
\[
h_4=10-7\sqrt2.
\]
At \(h=1/20\), the sign factor for \(k=3\) becomes
\[
\frac{44-37\sqrt2}{40}<0,
\]
since
\[
\left(\frac{44}{37}\right)^2<2.
\]
Therefore the third subdiagonal entry of \(R(hJ_4)\) is negative, while the exact semigroup remains entrywise nonnegative.

## Verification
The embedded `verify.py` checks the closed-form threshold algebra and evaluates the ROS2 matrix coefficients directly from the derivative formula.

It verifies that the first three derivative coefficients are positive for every positive step, that the fourth required coefficient changes sign exactly at
\[
10-7\sqrt2,
\]
and that the \(n\)-state threshold sequence is
\[
h_n=3n-2-(2n-1)\sqrt2.
\]
It also checks the exact sign witness at
\[
n=4,\qquad h=\frac1{20},
\]
using only rational comparisons to certify
\[
44-37\sqrt2<0.
\]

The checker is a replay of displayed algebra. The all-\(n\) result is proved analytically above.

## Relationship to prior work
Verwer, Spee, Blom, and Hundsdorfer introduced ROS2 for stiff atmospheric photochemical systems. Their report derives the same stability function, selects the larger L-stable parameter
\[
\gamma=1+\frac1{\sqrt2},
\]
and emphasizes that the scalar stability function remains positive on the negative real axis. That scalar fact does not imply positivity of \(R(hJ)\) for a coupled Metzler matrix.

Bonaventura and Della Rocca later analyze ROS2 in the framework of monotonicity and positivity. They explicitly note that the stability function and its first two derivatives are positive on the negative real axis, while a third derivative obstruction makes the absolute-monotonicity radius zero. They describe this as a form of weak absolute monotonicity.

The present result gives that derivative observation an exact finite-dimensional meaning. On the serial decay family, derivatives of order up to \(n-1\) are not merely sufficient tests: they are exactly the distinct subdiagonal entries of the step matrix. This yields a complete state-count phase law, identifies dimension four as the first possible failure, and shows that the failure is re-entrant rather than an ordinary upper-step restriction.

Targeted searches for ROS2 together with serial decay, Jordan chains, pure-birth chains, state-count positivity, and derivative-based matrix positivity did not locate this implication-equivalent classification.

## Limitations
The theorem is exact for the specific serial Metzler family
\[
J_n=-I+N_n.
\]
It does not classify general Metzler matrices or nonlinear reaction networks.

The exact-Jacobian ROS2 method is used. Rosenbrock \(W\)-method variants with approximate Jacobians need not have the same matrix function.

Only completed-step positivity is classified. The first internal stage, other Rosenbrock methods, and other choices of the L-stable parameter are outside the claim.

Residual originality risk remains that older matrix-function or Rosenbrock literature may encode the same derivative-to-Jordan-block argument without using the state-count language recovered in the targeted searches.

## References
1. J. G. Verwer, E. J. Spee, J. G. Blom, and W. Hundsdorfer, “A Second Order Rosenbrock Method Applied to Photochemical Dispersion Problems,” CWI Report MAS-R9717, 1997-08-31; later SIAM Journal on Scientific Computing 20 (1999), 1456–1480, DOI 10.1137/S1064827597326651.
2. L. Bonaventura and A. Della Rocca, “Monotonicity, positivity and strong stability of the TR-BDF2 method and of its SSP extensions,” arXiv:1510.04303, 2015-10-14.
