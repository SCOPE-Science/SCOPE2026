# Richardson acceleration creates a sharp positivity barrier for backward Euler
## Finding
Consider the positive scalar decay equation
\[
y'(t)=-\lambda y(t),
\qquad
\lambda>0,
\qquad
y(0)>0,
\]
over one macro-step of length \(H>0\), and put
\[
z=\lambda H.
\]
A single backward Euler step has amplification
\[
B_1(z)=\frac{1}{1+z},
\]
while \(r\) equal backward Euler substeps, with integer refinement factor \(r\ge2\), have amplification
\[
B_r(z)=\left(1+\frac{z}{r}\right)^{-r}.
\]

The two-level Richardson extrapolate that cancels the first-order error is
\[
R_r(z)
=
\frac{rB_r(z)-B_1(z)}{r-1}
=
\frac{r\left(1+z/r\right)^{-r}-(1+z)^{-1}}{r-1}.
\]
It is second order at the origin:
\[
R_r(z)
=
1-z+\frac{z^2}{2}+O(z^3).
\]

For every integer \(r\ge2\), there is a unique number \(z_r>0\) satisfying
\[
\left(1+\frac{z_r}{r}\right)^r
=
r(1+z_r),
\]
and the extrapolated step has the exact sign classification
\[
R_r(z)>0
\quad\Longleftrightarrow\quad
0\le z<z_r,
\]
\[
R_r(z_r)=0,
\qquad
R_r(z)<0
\quad\Longleftrightarrow\quad
z>z_r.
\]
Thus Richardson extrapolation destroys backward Euler's unconditional positivity even on the one-dimensional decay test problem.

For the standard two-level choice \(r=2\),
\[
R_2(z)
=
\frac{-z^2+4z+4}{(1+z)(2+z)^2},
\]
so the exact positivity threshold is
\[
z_2=2+2\sqrt2
=
4.8284271247\ldots.
\]
In particular, a positive exact solution and positive backward Euler base approximations produce a negative extrapolated value whenever
\[
\lambda H>2+2\sqrt2.
\]

Increasing the refinement factor cannot restore unconditional positivity. In fact,
\[
z_r
=
\log r+\log\log r+o(1)
\qquad
(r\to\infty).
\]
Hence obtaining a positivity radius of order \(Z\) from this two-level construction requires a refinement factor exponential in \(Z\), up to logarithmic corrections. The stiff tail is always negative:
\[
R_r(z)
=
-\frac{1}{(r-1)z}
+
O\!\left(z^{-2}\right)
+
O\!\left(z^{-r}\right)
\qquad
(z\to\infty).
\]

## Assumptions and scope
The theorem concerns exact arithmetic and the two-level Richardson extrapolation of the backward Euler base method. The refinement factor \(r\) is an integer at least two because \(B_r\) is formed by \(r\) equal substeps over the same macro-step.

The positivity statement is deliberately scalar. Failure on this positive decay equation is already enough to rule out unconditional positivity for any broader class that contains scalar linear decay. The result does not claim a complete strong-stability-preserving or absolute-monotonicity radius for nonlinear systems.

The statement also does not apply to positivity-preserving modifications, clipping, constrained extrapolation, or other extrapolation tableaux whose final combination differs from the displayed two-level Richardson formula.

## Proof
For a first-order approximation \(A(H)\), two-level Richardson extrapolation with refinement factor \(r\) is
\[
\frac{rA(H/r)-A(H)}{r-1}.
\]
On the scalar decay equation, one backward Euler step of size \(H\) is \(B_1(z)\), while \(r\) backward Euler substeps of size \(H/r\) give \(B_r(z)\). This proves the displayed formula for \(R_r\).

Expanding at the origin,
\[
B_1(z)
=
1-z+z^2+O(z^3),
\]
and
\[
B_r(z)
=
1-z+\frac{r+1}{2r}z^2+O(z^3).
\]
Therefore
\[
R_r(z)
=
1-z+\frac{z^2}{2}+O(z^3),
\]
so the extrapolate is second order.

Because every denominator in \(R_r(z)\) is positive for \(z\ge0\),
\[
R_r(z)\ge0
\]
is equivalent to
\[
r(1+z)\ge\left(1+\frac zr\right)^r.
\]
Define
\[
F_r(z)
=
\frac{(1+z/r)^r}{1+z}.
\]
Then
\[
\frac{d}{dz}\log F_r(z)
=
\frac{r}{r+z}-\frac{1}{1+z}
=
\frac{(r-1)z}{(r+z)(1+z)}.
\]
This derivative is strictly positive for \(z>0\). Also
\[
F_r(0)=1<r,
\]
whereas
\[
F_r(z)\longrightarrow\infty
\]
as \(z\to\infty\). Consequently there is exactly one positive solution \(z_r\) of \(F_r(z)=r\), and the complete sign classification follows.

For \(r=2\),
\[
R_2(z)
=
\frac{2}{(1+z/2)^2}-\frac{1}{1+z}
=
\frac{-z^2+4z+4}{(1+z)(2+z)^2}.
\]
The positive zero of the numerator is
\[
z_2=2+2\sqrt2.
\]

It remains to prove the large-\(r\) law. The defining equation is
\[
r\log\left(1+\frac{z_r}{r}\right)
=
\log r+\log(1+z_r).
\]
Since \(\log(1+x)\le x\),
\[
z_r
\ge
\log r+\log(1+z_r)
>
\log r.
\]
For \(z=2\log r\), the elementary inequality
\[
\log(1+x)\ge x-\frac{x^2}{2},
\qquad x\ge0,
\]
gives
\[
r\log\left(1+\frac{2\log r}{r}\right)
\ge
2\log r-\frac{2(\log r)^2}{r}.
\]
For all sufficiently large \(r\), this exceeds
\[
\log r+\log(1+2\log r),
\]
so the unique root satisfies
\[
z_r<2\log r.
\]
Thus \(z_r=O(\log r)\), and hence
\[
\frac{z_r^2}{r}\longrightarrow0.
\]
Using
\[
r\log\left(1+\frac{z_r}{r}\right)
=
z_r+O\!\left(\frac{z_r^2}{r}\right)
=
z_r+o(1)
\]
in the defining equation yields
\[
z_r
=
\log r+\log(1+z_r)+o(1).
\]
The bound \(z_r=O(\log r)\) first gives
\[
z_r=\log r+O(\log\log r),
\]
so \(z_r/\log r\to1\). Therefore
\[
\log(1+z_r)
=
\log\log r+o(1),
\]
and substitution proves
\[
z_r=\log r+\log\log r+o(1).
\]

Finally, for fixed \(r\ge2\),
\[
\left(1+\frac zr\right)^{-r}=O(z^{-r}),
\qquad
(1+z)^{-1}=z^{-1}+O(z^{-2}),
\]
which gives the negative stiff-tail expansion.

## Verification
The accompanying `verify.py` uses exact rational arithmetic to reconstruct \(R_r\) from one coarse backward Euler step and \(r\) refined substeps. It checks the cancellation of the first-order extrapolation error and the exact second-order Taylor coefficients for many integer refinement factors.

For \(r=2\), it verifies the exact rational-function identity
\[
R_2(z)
=
\frac{-z^2+4z+4}{(1+z)(2+z)^2}
\]
and brackets the unique positive zero around \(2+2\sqrt2\). For several larger refinement factors it independently brackets the unique sign transition and verifies that the sign agrees with the comparison
\[
(1+z/r)^r
\lessgtr
r(1+z).
\]

The uniqueness of the root for every \(r\) and the asymptotic law are analytic consequences of the derivative and logarithmic estimates in the proof; finite numerical checks are not used as substitutes for those arguments.

## Relationship to prior work
Richardson extrapolation for ordinary differential equations is classical. Shampine describes extrapolation methods as combining several subintegrations with a simple base method and emphasizes that the substep sequence influences the resulting formula and efficiency. Constantinescu and Sandu construct high-order extrapolated time-stepping methods based on Euler steps, give the Aitken--Neville extrapolation recurrence for arbitrary integer substep counts, and analyze linear stability. Those construction, order, and stability facts are prior work.

The inspected Constantinescu--Sandu full text supplies exactly the two ingredients used here: an Euler base calculation with a macro-step divided into \(n_j\) substeps, and the extrapolation recurrence that for two rows reduces to the displayed Richardson combination. Its stability analysis treats scalar linear test equations, but the inspected text does not state the positivity threshold above or the refinement-factor asymptotic.

The present result addresses a different structural property: sign preservation on positive stiff decay. It gives the exact if-and-only-if positivity boundary for every two-level refinement factor, the closed standard threshold \(2+2\sqrt2\), the inevitable negative stiff tail, and the logarithmic growth law
\[
z_r=\log r+\log\log r+o(1).
\]
This quantifies how accuracy acceleration can destroy a qualitative property that every backward Euler subintegration individually preserves.

## Limitations
The theorem is only about the second-order two-level extrapolate. Higher columns of an extrapolation tableau can have different sign structures and are not classified here.

Scalar positivity is weaker than nonlinear monotonicity or strong-stability preservation, so the result should not be read as an exact nonlinear SSP coefficient. Conversely, a scalar sign failure is decisive for unconditional positivity because it already occurs on the positive linear decay equation.

Extrapolation and monotonicity literature is extensive. An equivalent scalar threshold may exist under absolute-monotonicity or stability-function terminology not located in the searches performed here. The inspected older Shampine paper focuses on extrapolated midpoint constructions and sequence efficiency rather than this backward-Euler positivity question; the directly relevant Constantinescu--Sandu paper was inspected in full through an open author copy.

## References
1. Emil M. Constantinescu and Adrian Sandu, *Achieving Very High Order for Implicit Explicit Time Stepping: Extrapolation Methods*, Virginia Tech Computer Science Technical Report TR-08-13, July 18, 2008.
2. Emil M. Constantinescu and Adrian Sandu, *Extrapolated Implicit-Explicit Time Stepping*, SIAM Journal on Scientific Computing 31 (2010), 4452--4477, DOI: 10.1137/080732833.
3. L. F. Shampine, *Efficient Extrapolation Methods for ODEs*, IMA Journal of Numerical Analysis 3 (1983), 383--395, DOI: 10.1093/imanum/3.4.383.
