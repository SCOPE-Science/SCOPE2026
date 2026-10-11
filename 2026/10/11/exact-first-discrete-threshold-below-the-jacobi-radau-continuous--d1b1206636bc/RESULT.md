# Exact first discrete threshold below the Jacobi–Radau continuous barrier

## Finding

Let
\[
Q_m^{(\beta)}(x)
=
2^{-\beta-1}(1+x)^{\beta+1}P_{m-1}^{(0,\beta+1)}(x),
\qquad
\beta>-1,
\]
and let
\[
1>\xi_{1,m}^{(\beta)}>\cdots>\xi_{m-1,m}^{(\beta)}>-1
\]
be its interior critical points, ordered from the endpoint \(1\).

The recent equal-phase theorem proves
\[
\left|
Q_{m+1}^{(\beta)}
\left(
\xi_{k,m+1}^{(\beta)}
\right)
\right|
>
\left|
Q_m^{(\beta)}
\left(
\xi_{k,m}^{(\beta)}
\right)
\right|
\]
for every
\[
\beta\ge-\frac13.
\]
It also proves that the corresponding continuous comparison reverses near phase zero when
\[
-1<\beta<-\frac13,
\]
while explicitly leaving the optimal range of the separated discrete inequalities unresolved.

For the first nontrivial discrete comparison,
\[
m=2,
\qquad
k=1,
\]
there is a unique sharp threshold
\[
\beta_*\in
\left(
-1,-\frac13
\right)
\]
with
\[
\beta_*
=
-0.3646658445233908036558102183\ldots
\]
such that
\[
\left|
Q_3^{(\beta)}
\left(
\xi_{1,3}^{(\beta)}
\right)
\right|
\begin{cases}
<
\left|
Q_2^{(\beta)}
\left(
\xi_{1,2}^{(\beta)}
\right)
\right|,
&-1<\beta<\beta_*,
\\[0.4ex]
=
\left|
Q_2^{(\beta)}
\left(
\xi_{1,2}^{(\beta)}
\right)
\right|,
&\beta=\beta_*,
\\[0.4ex]
>
\left|
Q_2^{(\beta)}
\left(
\xi_{1,2}^{(\beta)}
\right)
\right|,
&\beta>\beta_*.
\end{cases}
\]

The companion position inequality is much more robust:
\[
\xi_{1,3}^{(\beta)}
>
\xi_{1,2}^{(\beta)}
\qquad
\text{for every }\beta>-1.
\]

Therefore the continuous barrier
\[
-\frac13
\]
is not the sharp barrier for the first discrete amplitude comparison. The discrete inequality survives strictly below it on
\[
\left(
\beta_*,-\frac13
\right).
\]

## Assumptions and scope

The normalization of
\[
Q_m^{(\beta)}
\]
and the enumeration of its critical points are exactly those of arXiv:2609.13030v1.

The parameter range
\[
\beta>-1
\]
is the natural Jacobi range in which
\[
P_{m-1}^{(0,\beta+1)}
\]
and
\[
P_{m-1}^{(1,\beta)}
\]
have the standard interior-zero structure used below.

The result classifies only the first nontrivial discrete comparison,
\[
m=2,\ k=1.
\]
It does not claim that the same number
\[
\beta_*
\]
is the optimal common threshold for every degree and every discrete phase.

No assertion about global Jacobi Lebesgue constants is made below
\[
-1/3,
\]
because the positive-product argument used by the source to identify endpoint and global Lebesgue constants is not available there.

## Proof

Put
\[
y=\frac{1+x}{2}.
\]
The degree-two member is
\[
Q_2^{(\beta)}(2y-1)
=
y^{\beta+1}
\left(
(\beta+3)y-(\beta+2)
\right).
\]
Its only interior critical point is
\[
y_2
=
\frac{\beta+1}{\beta+3}.
\]
At that point,
\[
Q_2^{(\beta)}(2y_2-1)
=
-
\left(
\frac{\beta+1}{\beta+3}
\right)^{\beta+1}.
\]
Hence
\[
A_2(\beta)
:=
\left|
Q_2^{(\beta)}
\left(
\xi_{1,2}^{(\beta)}
\right)
\right|
=
\left(
\frac{\beta+1}{\beta+3}
\right)^{\beta+1}.
\]

For the next degree,
\[
\begin{aligned}
Q_3^{(\beta)}(2y-1)
&=
\frac{y^{\beta+1}}2
\Bigl(
(\beta+4)(\beta+5)y^2
\\
&\qquad
-2(\beta+3)(\beta+4)y
+
(\beta+2)(\beta+3)
\Bigr).
\end{aligned}
\]
Its derivative has, apart from the positive factor
\[
y^\beta,
\]
the quadratic factor
\[
(\beta+4)(\beta+5)y^2
-
2(\beta+2)(\beta+4)y
+
(\beta+1)(\beta+2).
\]
The larger critical root, corresponding to
\[
\xi_{1,3}^{(\beta)},
\]
is
\[
y_3
=
\frac{
\beta+2+\sqrt{3(\beta+2)/(\beta+4)}
}{
\beta+5
}.
\]

At a critical root the quadratic relation reduces the polynomial factor in
\[
Q_3^{(\beta)}
\]
to
\[
(\beta+2)-(\beta+4)y.
\]
At the larger root this is negative, and therefore
\[
A_3(\beta)
:=
\left|
Q_3^{(\beta)}
\left(
\xi_{1,3}^{(\beta)}
\right)
\right|
=
y_3^{\beta+1}
\frac{
\sqrt{3(\beta+2)(\beta+4)}-(\beta+2)
}{
\beta+5
}.
\]

The threshold equation is therefore
\[
A_3(\beta)=A_2(\beta).
\]

To prove that it has exactly one solution, set
\[
t
=
\sqrt{
\frac{\beta+2}{\beta+4}
}.
\]
Then
\[
\frac1{\sqrt3}<t<1
\]
and
\[
\beta+1
=
\frac{3t^2-1}{1-t^2}.
\]
A direct simplification gives
\[
R(t)
:=
\frac{A_3(\beta)}{A_2(\beta)}
=
\frac{2t}{\sqrt3+t}
B(t)^{(3t^2-1)/(1-t^2)},
\]
where
\[
B(t)
=
\frac{
t(1+t^2)
}{
(\sqrt3+t)(\sqrt3t-1)
}.
\]
Moreover,
\[
B(t)-1
=
\frac{
(t-1)(t+1)(t-\sqrt3)
}{
(t+\sqrt3)(\sqrt3t-1)
}
>0.
\]

Let
\[
L(t)=\log R(t).
\]
Since
\[
\log B
>
\frac{2(B-1)}{B+1}
\qquad
(B>1),
\]
differentiation and simplification, with
\[
q=\sqrt3\,t,
\qquad
1<q<\sqrt3,
\]
give
\[
L'(t)
>
-\frac{
3\sqrt3\,F(q)
}{
(q+3)(q^2+3)(q^3+3q^2+9q-9)
},
\]
where
\[
F(q)
=
q^5+7q^4+8q^3+12q^2-81q-27.
\]
The denominator is positive on this interval. Also
\[
F'(q)
=
(q-1)
\left(
5q^3+33q^2+57q+81
\right)
>0,
\]
while
\[
F(\sqrt3)
=
72-48\sqrt3
<0.
\]
Thus
\[
F(q)<0
\]
throughout
\[
1<q<\sqrt3,
\]
and consequently
\[
L'(t)>0.
\]
Because \(t\) is strictly increasing in \(\beta\), the ratio
\[
A_3(\beta)/A_2(\beta)
\]
is strictly increasing in \(\beta\).

At the left endpoint,
\[
\lim_{\beta\downarrow-1}
\frac{A_3(\beta)}{A_2(\beta)}
=
\frac12.
\]
At
\[
\beta=-\frac13,
\]
the source's discrete corollary gives
\[
A_3(\beta)>A_2(\beta).
\]
The intermediate value theorem and strict monotonicity therefore produce exactly one root
\[
\beta_*
\in
\left(
-1,-\frac13
\right),
\]
and the three-way amplitude classification follows.

For the position comparison,
\[
y_2
=
\frac{\beta+1}{\beta+3},
\]
while the formula above gives \(y_3\). Their difference is
\[
y_3-y_2
=
\frac{
(\beta+3)\sqrt{3(\beta+2)/(\beta+4)}
-\beta+1
}{
(\beta+3)(\beta+5)
}.
\]
If
\[
-1<\beta<1,
\]
the numerator is positive immediately. If
\[
\beta\ge1,
\]
both sides of the required comparison are positive, and squaring reduces it to
\[
\begin{aligned}
&3(\beta+2)(\beta+3)^2
-
(\beta-1)^2(\beta+4)
\\
&\qquad
=
2(\beta+1)(\beta+5)^2
>0.
\end{aligned}
\]
Thus
\[
y_3>y_2
\]
for every
\[
\beta>-1,
\]
and hence
\[
\xi_{1,3}^{(\beta)}
>
\xi_{1,2}^{(\beta)}.
\]

## Verification

The recent primary preprint was inspected at the definition of
\[
Q_m^{(\beta)},
\]
its differentiation identity, Corollary 4.5, Proposition 4.6, Remark 4.7, and the Lebesgue-function section.

In particular, the source explicitly states that the continuous reversal below
\[
-1/3
\]
does not determine the optimal range of the discrete inequalities, whose relevant phases are separated rather than arbitrarily small.

The formulas for
\[
Q_2^{(\beta)}
\]
and
\[
Q_3^{(\beta)}
\]
were expanded directly from the Jacobi definition and differentiated exactly. The monotonicity argument for the amplitude ratio is symbolic and applies to the entire interval
\[
\beta>-1.
\]

High-precision evaluation of the exact threshold equation gives
\[
\beta_*
=
-0.36466584452339080365581021836986159\ldots.
\]
For orientation only,
\[
\log\frac{A_3}{A_2}
\]
is negative at
\[
\beta=-0.364666
\]
and positive at
\[
\beta=-0.364665.
\]
The numerical evaluation is not used to prove existence, uniqueness, or the sign classification.

## Relationship to prior work

Castillo and Hang prove the weighted Jacobi--Radau discrete comparison for
\[
\beta\ge-1/3
\]
as a consequence of a stronger continuous equal-phase theorem. They also prove that the continuous theorem is sharp at
\[
-1/3
\]
and explicitly distinguish that sharpness from the unresolved discrete parameter range below it.

At
\[
\beta=0,
\]
their weighted family reduces to the Jacobi polynomial
\[
P_m^{(0,-1)},
\]
whose relative-extremum inequalities were treated by Wong and Zhang. Those classical results do not classify the negative-\(\beta\) weighted family considered here.

Earlier general Jacobi-extremum work studies relative extrema of ordinary Jacobi polynomials and asymptotic degree comparisons. The present threshold concerns the weighted Radau family
\[
(1+x)^{\beta+1}P_{m-1}^{(0,\beta+1)}
\]
and a finite exact comparison across the continuous barrier.

Targeted searches for the exact source, the first discrete pair, degree-two/degree-three weighted extrema, and a threshold below
\[
-1/3
\]
did not locate an implication-equivalent statement.

## Limitations

The theorem completely classifies only the first nontrivial discrete comparison
\[
m=2,\ k=1.
\]
The optimal common parameter range for all degrees remains open.

The result does not extend the source's global Lebesgue-constant theorem below
\[
-1/3.
\]
Such an extension would additionally require control of where the Lebesgue function attains its maximum.

The threshold is characterized by an explicit transcendental equation. No simpler algebraic closed form is claimed.

## References

1. K. Castillo and P.-C. Hang, *Equal-Phase Monotonicity for Weighted Jacobi--Radau Functions and Jacobi Lebesgue Constants*, arXiv:2609.13030v1, 2026.
2. K. Castillo, *A proof of the Szegő conjecture on Jacobi extrema*, arXiv:2608.01404v1, 2026.
3. R. Wong and J.-M. Zhang, *On the Relative Extrema of the Jacobi Polynomials \(P_n^{(0,-1)}(x)\)*, SIAM Journal on Mathematical Analysis 25 (1994), 776--811, DOI: 10.1137/S0036141091223893.
4. R. Wong and J.-M. Zhang, *Asymptotic Monotonicity of the Relative Extrema of Jacobi Polynomials*, Canadian Journal of Mathematics 46 (1994), 1318--1337, DOI: 10.4153/CJM-1994-075-1.
