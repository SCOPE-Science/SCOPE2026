# Second-order small-parameter law for the Koumandos–Ruscheweyh critical curve

## Finding

Let
\[
I(\mu,\rho)
=
\int_0^{(1+\rho)\pi}
t^{\mu-1}\sin(t-\rho\pi)\,dt,
\]
and let
\[
\nu(\rho)=\mu^*(\rho)
\]
be its unique critical root from the recent proof of the Koumandos--Ruscheweyh conjecture.

The source proves
\[
\frac{\nu(\rho)}{\rho}
\longrightarrow
\kappa
=
\frac{\pi}{\operatorname{Si}(\pi)}
\qquad
(\rho\downarrow0).
\]
The first correction is explicit.

Put
\[
S=\operatorname{Si}(\pi),
\]
\[
A=
\int_0^1
\frac{\log t\,\sin(\pi t)}{t}\,dt,
\]
and
\[
B=
\int_0^1
\frac{\cos(\pi t)-1}{t}\,dt
=
\operatorname{Ci}(\pi)-\gamma-\log\pi.
\]
Then
\[
\nu(\rho)
=
\kappa\rho+\beta\rho^2+O(\rho^3),
\]
where
\[
\beta
=
\frac{\kappa^2}{S}(SB-A).
\]

Numerically,
\[
\kappa
=
1.6963819856764425\ldots,
\]
and
\[
\beta
=
-0.6128110975066010\ldots.
\]

Equivalently, for the source's root ratio
\[
q(\rho)=\frac{\nu(\rho)}{\rho},
\]
\[
q(\rho)
=
\kappa+\beta\rho+O(\rho^2).
\]

Thus the optimal parameter curve has an explicit tangent correction at the small-\(\rho\) endpoint, rather than only a limiting slope.

## Assumptions and scope

The critical curve is exactly the one in arXiv:2610.02285v1:
\[
0<\rho\le1,
\]
and
\[
\nu(\rho)
\]
is the unique root in
\[
(0,1]
\]
of the displayed oscillatory integral.

The source's normalized ratio is
\[
q(\rho)=\nu(\rho)/\rho.
\]
The result concerns the asymptotic regime
\[
\rho\downarrow0.
\]

No statement is made about a global approximation to
\[
\nu(\rho)
\]
away from the endpoint. The separate behavior near
\[
\rho=1
\]
is not part of this finding.

## Proof

The source introduces
\[
\nu=q\rho,
\qquad
a=(1+\rho)\pi,
\]
and
\[
C_0(\nu,a)
=
\int_0^1
t^{\nu-1}(\cos(at)-1)\,dt,
\]
\[
S_0(\nu,a)
=
\int_0^1
t^{\nu-1}\sin(at)\,dt.
\]
Its normalized root equation is
\[
F(q,\rho)
=
q\cos(\rho\pi)S_0(q\rho,a)
-
\pi\operatorname{sinc}(\rho\pi)
\left[
1+q\rho C_0(q\rho,a)
\right]
=
0.
\]

At
\[
\rho=0,
\]
\[
S_0(0,\pi)
=
\int_0^1\frac{\sin(\pi t)}{t}\,dt
=
S.
\]
Hence
\[
F(q,0)=qS-\pi,
\]
whose unique zero is
\[
q=\kappa=\pi/S.
\]

The functions
\[
C_0
\quad\text{and}\quad
S_0
\]
have continuous first and second derivatives in the parameters near
\[
(\nu,a)=(0,\pi).
\]
For \(C_0\), the numerator
\[
\cos(at)-1
\]
is quadratic at the origin; for \(S_0\), the numerator
\[
\sin(at)
\]
is linear there. Multiplication by one or two powers of
\[
\log t
\]
therefore remains integrable. Differentiation under the integral sign is justified.

Now
\[
F_q(\kappa,0)=S>0.
\]
The implicit-function theorem gives a \(C^2\) root function
\[
q(\rho)
\]
near zero.

Differentiate \(F\) with respect to \(\rho\), holding \(q\) fixed. The first derivatives at zero of
\[
\cos(\pi\rho)
\]
and
\[
\operatorname{sinc}(\pi\rho)
\]
vanish. Also
\[
\partial_\nu S_0(0,\pi)
=
A,
\]
and
\[
\partial_a S_0(0,\pi)
=
\int_0^1\cos(\pi t)\,dt
=
0.
\]
Finally,
\[
C_0(0,\pi)=B.
\]
Therefore
\[
F_\rho(\kappa,0)
=
\kappa^2A-\pi\kappa B.
\]

Implicit differentiation yields
\[
q'(0)
=
-\frac{F_\rho(\kappa,0)}{F_q(\kappa,0)}
=
-\frac{\kappa^2A-\pi\kappa B}{S}.
\]
Since
\[
\pi=\kappa S,
\]
this is
\[
q'(0)
=
\frac{\kappa^2}{S}(SB-A)
=
\beta.
\]
Thus
\[
q(\rho)
=
\kappa+\beta\rho+O(\rho^2),
\]
and multiplication by \(\rho\) gives
\[
\nu(\rho)
=
\kappa\rho+\beta\rho^2+O(\rho^3).
\]

## Verification

The primary source was inspected at the definition of the critical root, the normalized root equation in Section 6.1, and Proposition 6.1. In particular, the source explicitly proves
\[
q(\rho)\to\pi/\operatorname{Si}(\pi)
\]
and strict decrease of \(q\), but does not give the derivative at
\[
\rho=0.
\]

The derivative calculation was reconstructed directly from the displayed source equation. Every derivative needed at the endpoint reduces to an absolutely convergent integral. The special-function identity for \(B\) follows directly from the standard definition
\[
\operatorname{Ci}(x)
=
\gamma+\log x+
\int_0^x\frac{\cos u-1}{u}\,du.
\]

Independent high-precision evaluation of the exact integral formula gives
\[
\beta\approx-0.6128110975066010.
\]
This decimal value is a reproducibility check only; the proof uses the exact integral expression.

## Relationship to prior work

Koumandos and Ruscheweyh introduced the critical function
\[
\mu^*(\rho)
\]
in their 2007 conjecture. Their original paper established selected parameter cases.

Sangal and Swaminathan later proved the conjecture near
\[
\rho=1/3
\]
and in a weaker form at
\[
\rho=2/3.
\]
Those results do not analyze the endpoint
\[
\rho=0.
\]

The 2026 proof treats every
\[
0<\rho\le1
\]
and, in Proposition 6.1, proves the exact limiting ratio
\[
\lim_{\rho\downarrow0}\frac{\nu(\rho)}{\rho}
=
\frac{\pi}{\operatorname{Si}(\pi)}.
\]
It also proves that the ratio is strictly decreasing. The present calculation determines the first nonconstant term of that same normalized curve.

Targeted searches under the critical-root equation, the ratio limit, endpoint differentiation, and second-order small-\(\rho\) asymptotics did not locate an implication-equivalent statement.

## Limitations

The result is a local endpoint expansion. It does not replace the source's global proof of the conjecture or its computer-assisted positivity certificates.

The complete 2007 publisher article was not available through the lawful full-text route used in this check. Its public abstract states the conjecture and selected solved cases, but an unindexed endpoint remark in the inaccessible full text remains a residual originality risk.

The coefficient
\[
\beta
\]
is given exactly by convergent special-function integrals. No simpler elementary closed form is claimed.

## References

1. Y. Ma, *A Proof of the Koumandos--Ruscheweyh Conjecture*, arXiv:2610.02285v1, 2026.
2. S. Koumandos and S. Ruscheweyh, *On a conjecture for trigonometric sums and starlike functions*, Journal of Approximation Theory 149 (2007), 42--58, DOI: 10.1016/j.jat.2007.04.006.
3. P. Sangal and A. Swaminathan, *On a conjecture for trigonometric sums by S. Koumandos and S. Ruscheweyh*, arXiv:1806.06999v1, 2018.
