# Exact detachment crossover for Paley–Wiener concentration

## Finding

Fix
\[
s>0,
\qquad
r=\frac{s}{2},
\]
and let \(\psi_s\) be the real, even, \(L^2\)-normalized first prolate spheroidal wave function for the Paley–Wiener concentration problem on
\[
I_s=(-r,r).
\]
Write
\[
u_s(x)=\psi_s(x)^2
\]
and define the optimal concentration deficit of a measurable set \(E\) of measure \(s\) by
\[
\eta(E)
=
\lambda_0(s)
-
\sup_{\substack{f\in PW\\ \|f\|_2=1}}
\int_E |f(x)|^2\,dx.
\]

For
\[
0<\varepsilon<r,
\qquad
b\ge\varepsilon,
\]
consider the detached-piece family
\[
E_{\varepsilon,b}
=
(-r,r-\varepsilon)
\cup
(r-\varepsilon+b,r+b).
\]

If
\[
b=b_\varepsilon\ge\varepsilon
\quad\text{and}\quad
b_\varepsilon\longrightarrow0
\]
as \(\varepsilon\to0\), then
\[
\eta(E_{\varepsilon,b_\varepsilon})
\sim
-u_s'(r)\,\varepsilon b_\varepsilon.
\]

The endpoint slope is strictly negative,
\[
u_s'(r)<0,
\]
so the leading coefficient is positive.

Consequently,
\[
\eta(E_{\varepsilon,\varepsilon})
\sim
-u_s'(r)\,\varepsilon^2.
\]
More generally, throughout the mesoscopic regime
\[
\varepsilon=o(b_\varepsilon),
\qquad
b_\varepsilon\to0,
\]
the deficit is asymptotically the product of the amount of mass moved and the distance through which it is moved:
\[
\eta(E_{\varepsilon,b_\varepsilon})
\sim
-u_s'(r)\,\varepsilon b_\varepsilon.
\]

## Assumptions and scope

The Paley–Wiener normalization is
\[
PW
=
\left\{
f\in L^2(\mathbb R):
\operatorname{supp}\widehat f
\subset
\left[-\frac12,\frac12\right]
\right\}.
\]

The recent stability theorem introduces the weighted discrepancy
\[
D_a(E)
=
\lambda_0(s)
-
\int_E u_s(x-a)\,dx,
\qquad
\mathcal D(E)=\inf_{a\in\mathbb R}D_a(E),
\]
and proves
\[
0
\le
\mathcal D(E)-\eta(E)
\le
A_s\mathcal D(E)^2
\]
for a constant \(A_s>0\) depending only on \(s\).

The same source records the classical prolate facts
\[
u_s'(r)<0,
\]
that zero is the unique optimal center of \(I_s\), and uniform bounds on the derivatives of \(u_s\).

The statement here concerns the joint limit
\[
\varepsilon\to0,
\qquad
b_\varepsilon\to0,
\qquad
b_\varepsilon\ge\varepsilon.
\]
It does not claim a uniform formula for displacements bounded away from zero.

## Proof

Let
\[
E=E_{\varepsilon,b}.
\]
At center zero,
\[
D_0(E)
=
\lambda_0(s)-\int_Eu_s(x)\,dx.
\]
Because
\[
\lambda_0(s)=\int_{-r}^{r}u_s(x)\,dx,
\]
the removed and added pieces give
\[
D_0(E)
=
\int_{r-\varepsilon}^{r}u_s(x)\,dx
-
\int_{r-\varepsilon+b}^{r+b}u_s(x)\,dx.
\]
After translating the second integral,
\[
D_0(E)
=
\int_{r-\varepsilon}^{r}
\bigl(u_s(x)-u_s(x+b)\bigr)\,dx.
\]
Equivalently,
\[
D_0(E)
=
\int_{r-\varepsilon}^{r}
\int_0^b
-u_s'(x+t)\,dt\,dx.
\]

Assume now that
\[
b=b_\varepsilon\to0
\quad\text{and}\quad
\varepsilon\le b.
\]
For
\[
r-\varepsilon\le x\le r,
\qquad
0\le t\le b,
\]
one has
\[
x+t\longrightarrow r
\]
uniformly. Continuity of \(u_s'\) therefore gives
\[
-u_s'(x+t)
=
-u_s'(r)+o(1)
\]
uniformly over the integration rectangle. Hence
\[
D_0(E)
=
-u_s'(r)\,\varepsilon b\,(1+o(1)).
\]

It remains to show that optimizing the center does not alter this first-order term.

Define
\[
\Phi_{\varepsilon,b}(a)
=
\int_Eu_s(x-a)\,dx,
\]
so
\[
D_a(E)=\lambda_0(s)-\Phi_{\varepsilon,b}(a).
\]
For the interval,
\[
\Phi_{0,0}(a)
=
\int_{-r}^{r}u_s(x-a)\,dx.
\]
The prolate ground-state properties imply that \(a=0\) is its unique global maximum. Moreover,
\[
\Phi_{0,0}''(0)
=
\int_{-r}^{r}u_s''(x)\,dx
=
u_s'(r)-u_s'(-r)
=
2u_s'(r)
<
0.
\]

Since
\[
|E\triangle I_s|=2\varepsilon,
\]
boundedness of \(u_s\), \(u_s'\), and \(u_s''\) implies uniform convergence of
\[
\Phi_{\varepsilon,b},
\quad
\Phi_{\varepsilon,b}',
\quad
\Phi_{\varepsilon,b}''
\]
to the corresponding interval quantities as \(\varepsilon\to0\), locally uniformly in \(a\). Uniform convergence of \(\Phi_{\varepsilon,b}\), together with the unique maximum of \(\Phi_{0,0}\), forces every maximizing center \(a_{\varepsilon,b}\) to satisfy
\[
a_{\varepsilon,b}\to0.
\]
For all sufficiently small \(\varepsilon\), the strict negative second derivative near zero then makes this maximizing center unique.

At zero,
\[
\Phi_{\varepsilon,b}'(0)
=
\int_{r-\varepsilon}^{r}u_s'(x)\,dx
-
\int_{r-\varepsilon+b}^{r+b}u_s'(x)\,dx
\]
and hence
\[
\Phi_{\varepsilon,b}'(0)
=
\int_{r-\varepsilon}^{r}
\bigl(u_s'(x)-u_s'(x+b)\bigr)\,dx.
\]
Since \(u_s''\) is bounded,
\[
\Phi_{\varepsilon,b}'(0)
=
O(\varepsilon b).
\]
The mean-value theorem applied to
\[
\Phi_{\varepsilon,b}'(a_{\varepsilon,b})=0
\]
and the uniform negative curvature near zero gives
\[
a_{\varepsilon,b}
=
O(\varepsilon b).
\]

Taylor expansion around zero now yields
\[
\Phi_{\varepsilon,b}(a_{\varepsilon,b})
-
\Phi_{\varepsilon,b}(0)
=
O(\varepsilon^2b^2).
\]
Therefore
\[
\mathcal D(E_{\varepsilon,b})
=
D_0(E_{\varepsilon,b})
+
O(\varepsilon^2b^2)
=
-u_s'(r)\,\varepsilon b\,(1+o(1)).
\]

Finally, the source comparison gives
\[
0
\le
\mathcal D(E_{\varepsilon,b})
-
\eta(E_{\varepsilon,b})
\le
A_s
\mathcal D(E_{\varepsilon,b})^2.
\]
Since
\[
\mathcal D(E_{\varepsilon,b})
\asymp
\varepsilon b
\longrightarrow0,
\]
the quadratic error is lower order. Thus
\[
\eta(E_{\varepsilon,b_\varepsilon})
\sim
-u_s'(r)\,\varepsilon b_\varepsilon.
\]

## Verification

The recent primary source was inspected through the definition of the detached-piece family, its two quoted endpoint orders, the weighted discrepancy, the strict prolate endpoint slope, the derivative bounds, the uniqueness of the interval center, and the quadratic comparison between weighted and spectral deficits.

The critical new calculation is local and deterministic. The discrepancy at center zero is exactly a double integral of
\[
-u_s'
\]
over a rectangle of side lengths
\[
\varepsilon
\quad\text{and}\quad
b.
\]
In the joint near-edge limit that integrand converges uniformly to
\[
-u_s'(r).
\]
The center optimization contributes only second order because the derivative of the translated mass at zero is itself
\[
O(\varepsilon b)
\]
while the interval has strictly negative center curvature.

No finite numerical experiment is used.

## Relationship to prior work

The 2026 optimal-concentration theorem proves that intervals maximize Paley–Wiener concentration at fixed measure. The October 2026 stability paper then introduces the detached family
\[
E_{\varepsilon,b}
\]
specifically to show that ordinary symmetric difference does not encode how far a removed piece is moved.

That paper records only the order statements
\[
\eta(E_{\varepsilon,\varepsilon})
\asymp_s
\varepsilon^2
\]
and
\[
\eta(E_{\varepsilon,b_0})
\asymp_{s,b_0}
\varepsilon
\]
for fixed
\[
b_0>0.
\]
It does not state an exact coefficient or the joint crossover when
\[
b=b_\varepsilon\to0.
\]

The new asymptotic
\[
\eta(E_{\varepsilon,b_\varepsilon})
\sim
-u_s'(s/2)\varepsilon b_\varepsilon
\]
fills that intermediate scale and identifies the local boundary slope of the optimal prolate profile as the governing invariant.

Targeted searches for detached Paley–Wiener pieces, mesoscopic displacement, prolate endpoint-slope asymptotics, and localization-operator perturbations did not locate a covering statement.

## Limitations

The result is local in the detachment distance:
\[
b_\varepsilon\to0.
\]
It does not provide a single uniform coefficient for all fixed or diverging displacements.

No second asymptotic term is claimed.

The coefficient
\[
-u_s'(s/2)
\]
is expressed intrinsically through the first prolate ground state; no elementary closed form is asserted.

## References

1. D. Zelent, *Stability of concentration in the Paley–Wiener space*, arXiv:2610.01299v1, 2026.
2. L. D. Abreu and M. Speckbacher, *Optimal concentration in the Paley–Wiener space*, arXiv:2607.19192v1, 2026.
3. H. J. Landau and H. O. Pollak, *Prolate spheroidal wave functions, Fourier analysis and uncertainty—II*, Bell System Technical Journal 40 (1961), 65–84.
4. D. L. Donoho and P. B. Stark, *A note on rearrangements, spectral concentration, and the zero-order prolate spheroidal wavefunction*, IEEE Transactions on Information Theory 39 (1993), 257–260.
