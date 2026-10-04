# A sharp three-knot positivity defect for natural cubic interpolation
## Finding
Let \(x_0<x_1<x_2\), put
\[
h=x_1-x_0,\qquad k=x_2-x_1,\qquad r=\frac{k}{h}>0,
\]
and let \(S\) be the natural cubic spline interpolating data
\[
0\le y_0,y_1,y_2\le M,
\qquad M>0.
\]
Then the exact worst possible undershoot is
\[
\min_{0\le y_i\le M}\ \min_{x\in[x_0,x_2]} S(x)
=
-M\,C(r),
\]
where
\[
C(r)=
\frac{\max\{r^{-1},r^2\}}{3\sqrt{3}(1+r)}.
\]

The bound is attained. If \(0<r\le1\), the data \((y_0,y_1,y_2)=(0,0,M)\) attain
\[
S\!\left(x_0+\frac{h}{\sqrt3}\right)
=
-\frac{M}{3\sqrt3\,r(1+r)}.
\]
If \(r\ge1\), the data \((y_0,y_1,y_2)=(M,0,0)\) attain
\[
S\!\left(x_1+k\left(1-\frac1{\sqrt3}\right)\right)
=
-\frac{Mr^2}{3\sqrt3(1+r)}.
\]

Equal spacing is uniquely best:
\[
C(r)\ge C(1)=\frac1{6\sqrt3},
\]
with equality only at \(r=1\). In contrast,
\[
C(r)\longrightarrow\infty
\]
as \(r\to0^+\) or \(r\to\infty\). Thus bounded nonnegative three-point data can produce arbitrarily large negative values when the adjacent mesh ratio is sufficiently skewed.

The phenomenon persists for strictly positive data. For \(0<r\le1\), if
\[
0<\varepsilon<
\frac{c_r}{1+c_r},
\qquad
c_r=\frac1{3\sqrt3\,r(1+r)},
\]
then the data \((\varepsilon M,\varepsilon M,M)\) produce a negative value at \(x_0+h/\sqrt3\). The reflected construction gives the same conclusion for \(r\ge1\).

Two knots cannot exhibit this behavior, because the natural interpolant through two values is the line segment joining them. Hence three knots are the minimal data size for positivity loss.

## Assumptions and scope
The theorem concerns the ordinary interpolating natural cubic spline, characterized by
\[
S''(x_0)=S''(x_2)=0
\]
and \(C^2\) continuity at \(x_1\). No shape-preserving postprocessing, extra knots, clipping, rational modification, or slope limiting is applied.

The result is scale invariant in the ordinate and depends on the abscissae only through the adjacent mesh ratio \(r=k/h\). It is an exact real-arithmetic statement. It does not assert that all cubic or Hermite interpolation schemes have the same defect.

## Proof
Translate \(x_0\) to zero. The unique interior second derivative is
\[
S''(x_1)
=
\frac{3}{h+k}
\left(
\frac{y_2-y_1}{k}
-
\frac{y_1-y_0}{h}
\right).
\]

On the left interval write
\[
t=\frac{x-x_0}{h}\in[0,1].
\]
Substitution into the natural-spline formula gives
\[
S(x)=A_0(t)y_0+A_1(t)y_1+A_2(t)y_2,
\]
with
\[
A_0(t)=
\frac{(1-t)(2r+2-t-t^2)}{2(1+r)},
\]
\[
A_1(t)=
\frac{t(2r+1-t^2)}{2r},
\]
and
\[
A_2(t)=
-\frac{t(1-t^2)}{2r(1+r)}.
\]
For \(0\le t\le1\),
\[
A_0(t)\ge0,\qquad A_1(t)\ge0,\qquad A_2(t)\le0,
\]
and
\[
A_0(t)+A_1(t)+A_2(t)=1.
\]
Therefore, at fixed \(t\), the smallest value over the cube \(0\le y_i\le M\) is obtained by taking
\[
(y_0,y_1,y_2)=(0,0,M),
\]
and equals \(M A_2(t)\). Since
\[
\max_{0\le t\le1} t(1-t^2)=\frac{2}{3\sqrt3},
\]
attained uniquely at \(t=1/\sqrt3\), the sharp left-interval undershoot is
\[
-\frac{M}{3\sqrt3\,r(1+r)}.
\]

On the right interval write
\[
u=\frac{x-x_1}{k}\in[0,1].
\]
The same substitution gives
\[
S(x)=B_0(u)y_0+B_1(u)y_1+B_2(u)y_2,
\]
where
\[
B_0(u)=
-\frac{r^2u(1-u)(2-u)}{2(1+r)},
\]
\[
B_1(u)=
\frac{(1-u)(2+2ru-ru^2)}2,
\]
and
\[
B_2(u)=
\frac{u(2+3ru-ru^2)}{2(1+r)}.
\]
Thus
\[
B_0(u)\le0,\qquad B_1(u)\ge0,\qquad B_2(u)\ge0,
\]
and the coefficients again sum to one. The fixed-\(u\) minimum is therefore obtained by \((M,0,0)\) and equals \(M B_0(u)\).

Putting \(v=1-u\) gives
\[
u(1-u)(2-u)=v(1-v^2).
\]
Its maximum on \([0,1]\) is \(2/(3\sqrt3)\), attained when
\[
u=1-\frac1{\sqrt3}.
\]
Hence the sharp right-interval undershoot is
\[
-\frac{Mr^2}{3\sqrt3(1+r)}.
\]

Taking the more negative of the two interval minima gives
\[
C(r)=
\frac{\max\{r^{-1},r^2\}}{3\sqrt3(1+r)}.
\]
The two branches cross only at \(r=1\). On \(0<r\le1\),
\[
C(r)=\frac1{3\sqrt3\,r(1+r)}
\]
is strictly decreasing, while on \(r\ge1\),
\[
C(r)=\frac{r^2}{3\sqrt3(1+r)}
\]
is strictly increasing. This proves the unique equal-spacing minimum and the divergence for skew meshes.

For the strictly positive construction on the left, at the sharp point \(A_2=-c_r\) and \(A_0+A_1=1+c_r\). Thus the data \((\varepsilon M,\varepsilon M,M)\) give
\[
\frac{S}{M}
=
\varepsilon(1+c_r)-c_r,
\]
which is negative exactly when \(\varepsilon<c_r/(1+c_r)\). The right-hand statement follows by reflection.

Finally, with only two knots the natural conditions force the unique cubic spline to be affine, so nonnegative endpoint data remain nonnegative.

## Verification
The accompanying `verify.py` reconstructs the two cardinal-coefficient triples from the natural-spline equations using exact rational arithmetic. It verifies their partition-of-unity identities for several independent rational mesh ratios and sample points, checks the sign pattern algebraically through the factorized formulas, and checks the extremal data selections against direct spline evaluation.

The location and value of the continuous extrema are proved analytically from
\[
\frac{d}{dt}\bigl(t-t^3\bigr)=1-3t^2
\]
and the reflected identity
\[
u(1-u)(2-u)=v-v^3,\qquad v=1-u.
\]
Finite replay is therefore supplementary rather than a substitute for the all-\(r\) proof.

## Relationship to prior work
Fritsch and Carlson derived conditions and algorithms for monotone piecewise cubic interpolation because ordinary cubic interpolation does not generally preserve data shape. Fritsch and Butland later gave a simple local monotone cubic method; that paper is indexed primarily under MSC \(65D05\).

More directly, Fischer, Opfer, and Puri state that an interpolating spline through positive function values need not remain positive. Their nonnegative-spline algorithm starts from the interpolating natural spline and modifies intervals on which it becomes negative by adding extra knots. Thus the qualitative fact that natural cubic interpolation can violate positivity is established prior work and is not claimed here.

The distinction of the present result is quantitative and sharp for the minimal nontrivial knot count. It identifies the complete worst-case negative excursion over all bounded nonnegative three-point data at a fixed mesh ratio, proves the extremizing data and locations, and shows that mesh skew makes the defect unbounded while equal spacing uniquely minimizes it.

Equivalently, because at every point exactly one of the three cardinal coefficients can be negative, the three-knot natural-spline interpolation operator has Lebesgue constant
\[
\Lambda(r)=1+2C(r).
\]
This equivalence was used as an additional literature-search alias; no inspected source stated the displayed closed form.

## Limitations
The theorem covers exactly three interpolation knots. It does not give a sharp positivity defect for longer natural-spline grids, where several cardinal basis functions can contribute with alternating signs.

The most relevant older paper, by Fischer, Opfer, and Puri, was available during this review at the abstract and bibliographic level, including its explicit statement that natural interpolation may become negative. A full-text copy was not recovered through the lawful routes attempted, so an equivalent three-knot sharp constant inside that paper cannot be excluded. Classical spline-stability or Lebesgue-constant literature may also contain an equivalent formula under operator-norm terminology. These are residual originality risks, not correctness limitations.

## References
1. F. N. Fritsch and R. E. Carlson, *Monotone Piecewise Cubic Interpolation*, SIAM Journal on Numerical Analysis 17 (1980), 238--246, DOI: 10.1137/0717021.
2. F. N. Fritsch and J. Butland, *A Method for Constructing Local Monotone Piecewise Cubic Interpolants*, SIAM Journal on Scientific and Statistical Computing 5 (1984), 300--304, DOI: 10.1137/0905021.
3. Bernd Fischer, Gerhard Opfer, and Madan L. Puri, *A Local Algorithm for Constructing Non-Negative Cubic Splines*, Journal of Approximation Theory 64 (1991), 1--16, DOI: 10.1016/0021-9045(91)90082-L.
4. C. A. Hall, *Natural Cubic and Bicubic Spline Interpolation*, SIAM Journal on Numerical Analysis 10 (1973), 1055--1060, DOI: 10.1137/0710088.
