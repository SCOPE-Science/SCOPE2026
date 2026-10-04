# Exact uniform-convexity phase boundary for exponentially convex functions

## Finding

For
\[
0<\lambda\le\frac{\pi}{2},
\]
consider the exponentially convex Ma–Minda class
\[
\mathcal C_{e^\lambda}
=
\left\{
f\in\mathcal A:
1+\frac{zf''(z)}{f'(z)}
\prec
e^{\lambda z}
\right\}.
\]

There is a sharp threshold
\[
\lambda_{\mathrm{uc}}
=
0.6905440336407464277786112389\ldots
\]
such that
\[
\mathcal C_{e^\lambda}
\subset
\mathrm{UCV}
\quad\Longleftrightarrow\quad
0<\lambda\le\lambda_{\mathrm{uc}}.
\]

Define, for \(y\ge0\),
\[
a(y)
=
\frac12
\log\!\left(
\frac{y^4+6y^2+1}{4}
\right),
\qquad
b(y)
=
\arctan\!\left(
\frac{2y}{1+y^2}
\right),
\]
and
\[
N(y)
=
a(y)y(y^2+3)
+
b(y)(1-y^2).
\]
There is exactly one zero
\[
y_*\in(0,1)
\]
of \(N\). Numerically,
\[
y_*
=
0.2241944779359010240194013275\ldots,
\]
and
\[
\lambda_{\mathrm{uc}}
=
\sqrt{
a(y_*)^2+b(y_*)^2
}.
\]

The boundary contact point in the curvature plane is
\[
w_*
=
\frac{1+y_*^2}{2}+iy_*,
\]
with
\[
\log w_*
=
a(y_*)+ib(y_*).
\]

Equivalently, under the Alexander correspondence, the exact parabolic-starlikeness radius of the exponential class
\[
\mathcal S_e^*
=
\left\{
g\in\mathcal A:
\frac{zg'(z)}{g(z)}
\prec e^z
\right\}
\]
is \(\lambda_{\mathrm{uc}}\).

## Assumptions and scope

A normalized analytic function is uniformly convex precisely when
\[
\operatorname{Re}
\left(
1+\frac{zf''(z)}{f'(z)}
\right)
>
\left|
\frac{zf''(z)}{f'(z)}
\right|.
\]
Thus the curvature quantity
\[
p_f(z)
=
1+\frac{zf''(z)}{f'(z)}
\]
must lie in the parabolic domain
\[
\mathcal P
=
\left\{
w:
\operatorname{Re}w>|w-1|
\right\}.
\]

The result concerns the whole class \(\mathcal C_{e^\lambda}\), not merely one extremal. The upper obstruction uses the canonical extremal supplied by the defining 2026 source.

No claim is made about stronger conic classes with a different eccentricity parameter.

## Proof

Write
\[
w=u+iv.
\]
Because the parabolic inequality implies \(u>0\), squaring gives
\[
u>|w-1|
\quad\Longleftrightarrow\quad
2u>1+v^2.
\]
Hence
\[
\mathcal P
=
\left\{
u+iv:
u>\frac{1+v^2}{2}
\right\},
\]
whose boundary is
\[
w_y
=
\frac{1+y^2}{2}+iy,
\qquad
y\in\mathbb R.
\]

The domain \(\mathcal P\) lies in the right half-plane, so the principal logarithm is analytic there. Since the exponential is injective on every disk of radius at most \(\pi/2\), one has
\[
e^{\lambda\mathbb D}\subset\mathcal P
\quad\Longleftrightarrow\quad
\lambda\mathbb D\subset\Log\mathcal P.
\]
Therefore the largest admissible \(\lambda\) is
\[
\operatorname{dist}
\left(
0,\partial(\Log\mathcal P)
\right)
=
\min_{y\in\mathbb R}
|\Log w_y|.
\]

By conjugation symmetry it is enough to take \(y\ge0\). For such \(y\),
\[
\Log w_y
=
a(y)+ib(y),
\]
where
\[
a(y)
=
\frac12
\log\!\left(
\frac{y^4+6y^2+1}{4}
\right)
\]
and
\[
b(y)
=
\arctan\!\left(
\frac{2y}{1+y^2}
\right).
\]
Let
\[
L(y)
=
a(y)^2+b(y)^2
\]
and
\[
D(y)=y^4+6y^2+1.
\]
Direct differentiation gives
\[
a'(y)
=
\frac{2y(y^2+3)}{D(y)},
\qquad
b'(y)
=
\frac{2(1-y^2)}{D(y)}.
\]
Consequently,
\[
L'(y)
=
\frac{4N(y)}{D(y)},
\]
with
\[
N(y)
=
a(y)y(y^2+3)+b(y)(1-y^2).
\]

We now prove that \(N\) has exactly one positive zero. A second differentiation gives
\[
N'(y)
=
(1+y^2)(2+3a(y))-2yb(y)
\]
and
\[
N''(y)
=
2y(2+3a(y))
-2b(y)
+
\frac{
2y(3y^4+14y^2+7)
}{
D(y)
}.
\]

For
\[
0<y\le1,
\]
one has
\[
a(y)\ge-\log2,
\qquad
b(y)
\le
\frac{2y}{1+y^2},
\]
and
\[
\frac{
2(3y^4+14y^2+7)
}{
D(y)
}
\ge6,
\]
because the last inequality is equivalent to
\[
4(1-y^2)\ge0.
\]
Therefore
\[
N''(y)
\ge
6(1-\log2)y
>
0.
\]
Thus \(N'\) is strictly increasing on \((0,1)\). Moreover,
\[
N'(0)
=
2-3\log2
<
0,
\]
while
\[
N'(1)
=
4+3\log2-\frac{\pi}{2}
>
0.
\]
Hence \(N'\) has one zero on \((0,1)\), so \(N\) first decreases and then increases. Since
\[
N(0)=0
\]
and
\[
N(1)=2\log2>0,
\]
there is exactly one zero
\[
y_*\in(0,1)
\]
besides the endpoint zero at \(0\), with
\[
N(y)<0
\quad
(0<y<y_*),
\qquad
N(y)>0
\quad
(y_*<y\le1).
\]

For \(y\ge1\), use
\[
a(y)\ge\frac12\log2,
\qquad
0<b(y)\le\frac{\pi}{4}.
\]
Then
\[
N(y)
\ge
\frac12\log2\,y(y^2+3)
-
\frac{\pi}{4}(y^2-1).
\]
The right-hand side is positive at \(y=1\) and strictly increasing for \(y\ge1\), because its derivative is
\[
\frac12\log2\,(3y^2+3)
-
\frac{\pi}{2}y
>
0.
\]
Thus
\[
N(y)>0
\qquad
(y\ge1).
\]

It follows that \(L\) has exactly one positive global minimizer \(y_*\), proving
\[
\lambda_{\mathrm{uc}}
=
\min_{y\in\mathbb R}
|\Log w_y|
=
\sqrt{
a(y_*)^2+b(y_*)^2
}.
\]

Now suppose
\[
0<\lambda\le\lambda_{\mathrm{uc}}.
\]
The open disk
\[
\lambda\mathbb D
\]
lies in \(\Log\mathcal P\), so
\[
e^{\lambda\mathbb D}
\subset\mathcal P.
\]
For every
\[
f\in\mathcal C_{e^\lambda},
\]
subordination gives
\[
1+\frac{zf''(z)}{f'(z)}
\in
e^{\lambda\mathbb D}
\subset
\mathcal P,
\]
hence \(f\) is uniformly convex.

Conversely, let
\[
\lambda>\lambda_{\mathrm{uc}}.
\]
The 2026 source supplies the canonical extremal
\[
f_\lambda(z)
=
\int_0^z
\exp\!\left(
\int_0^t
\frac{e^{\lambda\xi}-1}{\xi}\,d\xi
\right)dt,
\]
for which
\[
1+\frac{zf_\lambda''(z)}{f_\lambda'(z)}
=
e^{\lambda z}.
\]
Set
\[
z_*
=
\frac{
a(y_*)+ib(y_*)
}{
\lambda
}.
\]
Then
\[
|z_*|
=
\frac{\lambda_{\mathrm{uc}}}{\lambda}
<
1
\]
and
\[
e^{\lambda z_*}
=
w_*
\in
\partial\mathcal P.
\]
Thus the strict uniform-convexity inequality fails at an interior point, so
\[
f_\lambda\notin\mathrm{UCV}.
\]
This proves the sharp equivalence.

## Verification

The defining 2026 paper was inspected in full around the class definition, the image domain
\[
e^{\lambda\mathbb D},
\]
and the sharp canonical extremal. Its Theorem 2.1 gives exactly the extremal used in the upper obstruction.

The classical parabolic criterion for uniform convexity was checked against the standard Ma–Minda/Rønning formulation.

The minimization is not inferred from a numerical search. The proof above shows analytically that \(N\) has exactly one positive zero and hence that the logarithmic boundary-distance function has exactly one global minimizer.

The packaged checker only evaluates the unique root and the resulting constant by high-precision bisection. It reproduces
\[
y_*
=
0.2241944779359010240\ldots
\]
and
\[
\lambda_{\mathrm{uc}}
=
0.6905440336407464278\ldots.
\]

## Relationship to prior work

Ahamed and Hossain's 2026 paper studies the parameterized class
\[
\mathcal C_{e^\lambda},
\qquad
0<\lambda\le\frac{\pi}{2},
\]
and focuses on growth, distortion, pre-Schwarzian and Schwarzian norms. It describes the exponential image geometry but does not determine the exact uniform-convexity phase boundary.

Shi, Wang, Su and Arif's 2020 paper studies initial coefficient problems for exponential-function classes and does not supply this geometric threshold.

For the unparameterized exponential starlike class, Mendiratta, Nagpal and Ravichandran state the parabolic-starlikeness radius as
\[
\log2.
\]
Their proof bounds the complex exponential displacement by a one-dimensional real-ray quantity. The exact logarithmic-parabola distance above shows that an off-axis boundary point is closer:
\[
\lambda_{\mathrm{uc}}
<
\log2.
\]
Indeed, the canonical exponential extremal reaches the parabolic boundary already at modulus
\[
\lambda_{\mathrm{uc}},
\]
so the larger radius cannot satisfy the strict parabolic condition.

Targeted searches for the 2026 source, exponential Ma–Minda uniform convexity, parabolic starlikeness, the claimed \(\log2\) radius, and the numerical threshold did not locate a published statement of the exact constant above.

## Limitations

The theorem concerns ordinary uniform convexity, corresponding to the parabolic domain
\[
\operatorname{Re}w>|w-1|.
\]
It does not classify all \(k\)-uniformly convex phase boundaries.

The constant is characterized implicitly through one transcendental scalar equation; no elementary closed form is claimed.

The result does not alter the growth, distortion or Schwarzian estimates of the defining 2026 paper.

## References

1. M. B. Ahamed and R. Hossain, *Growth, Distortion, and Schwarzian Norm Estimates for Exponentially Convex Functions*, arXiv:2609.27563v1, 2026.
2. R. Mendiratta, S. Nagpal and V. Ravichandran, *On a Subclass of Strongly Starlike Functions Associated with Exponential Function*, Bulletin of the Malaysian Mathematical Sciences Society 38 (2015), 365–386. DOI: 10.1007/s40840-014-0026-8.
3. L. Shi, Z.-G. Wang, R.-L. Su and M. Arif, *Initial successive coefficients for certain classes of univalent functions involving the exponential function*, Journal of Mathematical Inequalities 14 (2020), 1183–1201. arXiv:2003.09771.
4. W. C. Ma and D. Minda, *Uniformly convex functions*, Annales Polonici Mathematici 57 (1992), 165–175.
5. F. Rønning, *Uniformly convex functions and a corresponding class of starlike functions*, Proceedings of the American Mathematical Society 118 (1993), 189–196.
