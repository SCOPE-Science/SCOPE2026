# Two-scale stabilization of differential harmonic Landau radii

## Finding

Fix
\[
M\ge\frac{\pi}{4}
\]
and write
\[
a=\frac{\pi}{4M}.
\]
For
\[
\alpha\ge0,
\]
define
\[
S_\alpha(r)
=
2\sum_{m=1}^{\infty}
\frac{r^m}{1+\alpha m},
\qquad
0\le r<1.
\]
Let
\[
\rho_\alpha\in(0,1)
\]
be the unique root of
\[
S_\alpha(\rho_\alpha)=a.
\]
Define
\[
T_\alpha(r)
=
2\sum_{m=1}^{\infty}
\frac{r^{m+1}}
{(m+1)(1+\alpha m)}
\]
and
\[
R_\alpha=a\rho_\alpha-T_\alpha(\rho_\alpha).
\]

The series are the coefficient-series quantities appearing in the recent Landau theorem for the harmonic class
\[
\mathcal W_{\mathcal H}^{0}(\alpha).
\]
They give the theorem's guaranteed univalence radius and guaranteed schlicht-disc radius without using its special-function reparametrization.

Both radius functions are strictly increasing in the differential parameter:
\[
\alpha_2>\alpha_1\ge0
\quad\Longrightarrow\quad
\rho_{\alpha_2}>\rho_{\alpha_1}
\]
and
\[
R_{\alpha_2}>R_{\alpha_1}.
\]

At the undamped endpoint,
\[
\rho_0
=
\frac{\pi}{\pi+8M},
\]
and
\[
R_0
=
\frac{\pi}{4M}
+
2\log\frac{8M}{\pi+8M}.
\]

At the opposite end, the univalence deficit is exponentially small:
\[
\log\frac1{1-\rho_\alpha}
=
\frac{\pi\alpha}{8M}
+
\psi\!\left(1+\frac1\alpha\right)
+
\gamma
+
o(1),
\qquad
\alpha\to\infty,
\]
where
\[
\psi
\]
is the digamma function and
\[
\gamma
\]
is Euler's constant. Hence
\[
1-\rho_\alpha
=
\exp\!\left(
-\frac{\pi\alpha}{8M}
\right)
(1+o(1)).
\]

The schlicht-disc quantity has a different asymptotic scale:
\[
R_\alpha
=
\frac{\pi}{4M}
-
\frac2\alpha
+
\frac{2(\pi^2/6-1)}{\alpha^2}
+
O_M(\alpha^{-3}).
\]

Thus the two geometric guarantees stabilize at parametrically different rates: the univalence disk fills the unit disk exponentially fast, while the covering radius approaches its limiting value only at inverse-linear speed.

## Assumptions and scope

The recent source studies normalized harmonic maps
\[
f=h+\overline g
\]
in the unit disk and the class
\[
\mathcal W_{\mathcal H}^{0}(\alpha)
=
\left\{
f:
\operatorname{Re}\bigl(h'(z)+\alpha z h''(z)\bigr)
>
\left|g'(z)+\alpha z g''(z)\right|
\right\},
\]
with
\[
\alpha\ge0.
\]

Its coefficient estimate is
\[
|a_n|+|b_n|
\le
\frac{2}
{\alpha n^2+n(1-\alpha)}
=
\frac{2}
{n[1+\alpha(n-1)]},
\qquad
n\ge2.
\]
The Landau argument combines this with
\[
\lambda_f(0)\ge\frac{\pi}{4M}
\]
for maps satisfying
\[
f(0)=0,
\qquad
J_f(0)=1,
\qquad
|f(z)|<M.
\]
The restriction
\[
M\ge\pi/4
\]
is necessary for this bounded normalized family to be nonempty, because
\[
1=J_f(0)\le\Lambda_f(0)^2
\]
while the harmonic Schwarz estimate gives
\[
\Lambda_f(0)\le4M/\pi.
\]

The present theorem concerns the radius quantities obtained from that coefficient-series Landau argument. It does not rely on, or add any assertion about, optimality of the source theorem's extremal construction.

## Proof

The source root equation is
\[
\frac{\pi}{4M}
-
2\sum_{n=2}^{\infty}
\frac{r^{n-1}}
{\alpha n+(1-\alpha)}
=
0.
\]
Putting
\[
m=n-1
\]
gives exactly
\[
S_\alpha(r)=a.
\]

For each fixed
\[
\alpha\ge0,
\]
the function
\[
S_\alpha
\]
is strictly increasing in
\[
r
\]
because every coefficient is positive. Also,
\[
S_\alpha(0)=0,
\]
while
\[
S_\alpha(r)\to\infty
\]
as
\[
r\uparrow1.
\]
Thus
\[
\rho_\alpha
\]
exists and is unique.

For fixed
\[
0<r<1,
\]
the function
\[
S_\alpha(r)
\]
is strictly decreasing in
\[
\alpha.
\]
Indeed,
\[
\frac{\partial S_\alpha}{\partial\alpha}(r)
=
-2
\sum_{m=1}^{\infty}
\frac{m r^m}{(1+\alpha m)^2}
<0,
\]
while
\[
\frac{\partial S_\alpha}{\partial r}(r)
=
2
\sum_{m=1}^{\infty}
\frac{m r^{m-1}}{1+\alpha m}
>0.
\]
Implicit differentiation gives
\[
\rho_\alpha'
=
-
\frac{\partial_\alpha S_\alpha(\rho_\alpha)}
{\partial_r S_\alpha(\rho_\alpha)}
>0.
\]
Thus the univalence radius is strictly increasing.

The covering series satisfies
\[
T_\alpha'(r)=S_\alpha(r).
\]
Hence
\[
R_\alpha
=
a\rho_\alpha-T_\alpha(\rho_\alpha)
=
\int_0^{\rho_\alpha}
\bigl(a-S_\alpha(t)\bigr)\,dt
>0.
\]
Differentiating with respect to
\[
\alpha
\]
and using
\[
S_\alpha(\rho_\alpha)=a
\]
cancels every term containing
\[
\rho_\alpha'.
\]
Therefore
\[
R_\alpha'
=
-\partial_\alpha T_\alpha(\rho_\alpha)
=
2\sum_{m=1}^{\infty}
\frac{
m\rho_\alpha^{m+1}
}{
(m+1)(1+\alpha m)^2
}
>0.
\]
This proves strict monotonicity of the covering radius.

When
\[
\alpha=0,
\]
the root equation becomes
\[
2\frac{\rho_0}{1-\rho_0}=a,
\]
so
\[
\rho_0=\frac{a}{a+2}
=
\frac{\pi}{\pi+8M}.
\]
Also,
\[
T_0(r)
=
2\sum_{m=1}^{\infty}\frac{r^{m+1}}{m+1}
=
-2\log(1-r)-2r.
\]
Using the root equation gives
\[
R_0
=
a+2\log(1-\rho_0)
=
\frac{\pi}{4M}
+
2\log\frac{8M}{\pi+8M}.
\]

Now let
\[
\alpha\to\infty.
\]
Strict monotonicity shows that
\[
\rho_\alpha
\]
has a limit at most \(1\). If that limit were
\[
L<1,
\]
then
\[
S_\alpha(\rho_\alpha)
\le
2\sum_{m=1}^{\infty}
\frac{L^m}{1+\alpha m}
\longrightarrow0,
\]
contradicting
\[
S_\alpha(\rho_\alpha)=a>0.
\]
Hence
\[
\rho_\alpha\to1.
\]

Put
\[
\beta=\frac1\alpha,
\qquad
\delta_\alpha=1-\rho_\alpha.
\]
The root equation becomes
\[
\frac{a\alpha}{2}
=
\sum_{m=1}^{\infty}
\frac{\rho_\alpha^m}{m+\beta}.
\]
Split the sum as
\[
\sum_{m=1}^{\infty}\frac{r^m}{m+\beta}
=
\sum_{m=1}^{\infty}\frac{r^m}{m}
+
\sum_{m=1}^{\infty}
r^m
\left(
\frac1{m+\beta}-\frac1m
\right).
\]
The first sum is
\[
-\log(1-r).
\]
For the second sum, the coefficient difference has absolute value at most
\[
\frac{\beta}{m^2},
\]
so dominated convergence is uniform as
\[
\beta\downarrow0.
\]
At
\[
r=1,
\]
the second sum equals
\[
-\psi(1+\beta)-\gamma.
\]
Consequently,
\[
\frac{a\alpha}{2}
=
-\log\delta_\alpha
-
\psi\!\left(1+\frac1\alpha\right)
-
\gamma
+
o(1).
\]
Rearranging yields
\[
\log\frac1{\delta_\alpha}
=
\frac{a\alpha}{2}
+
\psi\!\left(1+\frac1\alpha\right)
+
\gamma
+
o(1).
\]
Since
\[
\psi(1+x)+\gamma\to0
\]
as
\[
x\downarrow0,
\]
we get
\[
\delta_\alpha
=
e^{-a\alpha/2}(1+o(1))
=
\exp\!\left(
-\frac{\pi\alpha}{8M}
\right)
(1+o(1)).
\]

For the covering radius, first evaluate
\[
T_\alpha(1)
=
2\sum_{m=1}^{\infty}
\frac1{(m+1)(1+\alpha m)}.
\]
Expanding
\[
\frac1{1+\alpha m}
=
\frac1{\alpha m}
-
\frac1{\alpha^2m^2}
+
O\!\left(
\frac1{\alpha^3m^3}
\right)
\]
and summing absolutely gives
\[
T_\alpha(1)
=
\frac2\alpha
-
\frac{2}{\alpha^2}
\sum_{m=1}^{\infty}
\frac1{m^2(m+1)}
+
O(\alpha^{-3}).
\]
The elementary partial-fraction sum is
\[
\sum_{m=1}^{\infty}
\frac1{m^2(m+1)}
=
\frac{\pi^2}{6}-1.
\]
Thus
\[
T_\alpha(1)
=
\frac2\alpha
-
\frac{2(\pi^2/6-1)}{\alpha^2}
+
O(\alpha^{-3}).
\]

Finally,
\[
T_\alpha(1)-T_\alpha(\rho_\alpha)
=
\int_{\rho_\alpha}^{1}
S_\alpha(t)\,dt.
\]
The logarithmic representation above shows that this integral is exponentially small in
\[
\alpha,
\]
because
\[
1-\rho_\alpha
=
\exp(-a\alpha/2+o(\alpha)).
\]
Therefore it is
\[
o(\alpha^{-N})
\]
for every fixed
\[
N.
\]
Since
\[
a\rho_\alpha=a+o(\alpha^{-N})
\]
as well, substitution into
\[
R_\alpha=a\rho_\alpha-T_\alpha(\rho_\alpha)
\]
gives
\[
R_\alpha
=
a
-
\frac2\alpha
+
\frac{2(\pi^2/6-1)}{\alpha^2}
+
O_M(\alpha^{-3}),
\]
as claimed.

## Verification

The coefficient denominator was checked directly:
\[
\alpha n+(1-\alpha)
=
1+\alpha(n-1).
\]
Thus the index shift used in
\[
S_\alpha
\]
does not change the source root equation.

The identity
\[
T_\alpha'(r)=S_\alpha(r)
\]
was checked term by term on every compact subdisk, where both series converge uniformly. This identity supplies both the positivity formula for
\[
R_\alpha
\]
and the cancellation in its parameter derivative.

The digamma constant follows from the standard identity
\[
\psi(1+\beta)+\gamma
=
\sum_{m=1}^{\infty}
\frac{\beta}{m(m+\beta)}.
\]
Hence
\[
\sum_{m=1}^{\infty}
\left(
\frac1{m+\beta}-\frac1m
\right)
=
-\psi(1+\beta)-\gamma.
\]

The second covering coefficient was independently reduced by
\[
\frac1{m^2(m+1)}
=
-\frac1m+\frac1{m^2}+\frac1{m+1},
\]
so the sum equals
\[
\pi^2/6-1.
\]

No finite computation, truncated series, or numerical fitting is used to establish the monotonicity or the asymptotic laws.

## Relationship to prior work

Ahamed and Hossain introduced the bounded-harmonic Landau calculation for
\[
\mathcal W_{\mathcal H}^{0}(\alpha)
\]
and derived its radius equation from the coefficient estimate
\[
|a_n|+|b_n|
\le
\frac{2}{n[1+\alpha(n-1)]}.
\]
Their paper expresses the general radii through the Lerch transcendent and displays the special values
\[
\alpha=0
\]
and
\[
\alpha=1
\]
numerically and in closed form.

The inspected paper does not state global monotonicity in
\[
\alpha,
\]
does not analyze
\[
\alpha\to\infty,
\]
and contains no asymptotic result. The present theorem stays at the underlying positive coefficient series, where the parameter dependence becomes transparent enough to prove strict monotonicity and to expose two different stabilization scales.

Ghosh and Vasudevarao developed the class
\[
\mathcal W_{\mathcal H}^{0}(\alpha)
\]
and its sharp coefficient estimates in earlier work. Those coefficient results are an input to the recent Landau theorem; they do not contain the bounded-harmonic radius comparison or the large-parameter asymptotics proved here.

Targeted literature searches for equal radius equations, monotonicity in the differential parameter, large-\(\alpha\) Landau asymptotics, and equivalent digamma or exponential boundary-layer formulations did not locate a statement implying this result.

## Limitations

The result analyzes the specific coefficient-series radii furnished by the recent Landau theorem. It does not independently certify the optimality of those radii among all bounded mappings in the class.

The asymptotic regime keeps
\[
M
\]
fixed while
\[
\alpha\to\infty.
\]
Joint limits in which
\[
M
\]
also varies may have different transition scales.

The second-order expansion is given for
\[
R_\alpha
\].
Only the leading multiplicative law is asserted for
\[
1-\rho_\alpha
\];
higher corrections can be obtained from the digamma expansion and a sharper uniform remainder analysis.

## References

1. M. B. Ahamed and R. Hossain, *Sharp Landau-Type Theorems and Schlicht Disc Radii for certain Subclasses of Harmonic Mappings*, arXiv:2603.28806v1, first posted 28 March 2026.
2. N. Ghosh and A. Vasudevarao, *On Some Subclass of Harmonic Close-to-convex Mappings*, Monatshefte für Mathematik 188 (2019), 247--267, DOI: 10.1007/s00605-017-1138-7.
