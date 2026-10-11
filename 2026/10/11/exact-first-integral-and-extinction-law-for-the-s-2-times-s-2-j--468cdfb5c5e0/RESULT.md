# Exact first integral and extinction law for the \(S^2\times S^2\) \(J\)-flow

## Finding

Consider the unnormalized \(J\)-flow of Chen, Kang, and Yuan on product metrics
\[
g_{A,B}
=
A\,g_{S^2}\oplus B\,g_{S^2},
\qquad
A(0)=A_0>0,\quad B(0)=B_0>0.
\]
Their product reduction is
\[
A'
=
\frac{B-2A}{3AB},
\qquad
B'
=
\frac{A-2B}{3AB}.
\]

Put
\[
S=A+B,
\qquad
D=A-B,
\qquad
S_0=A_0+B_0,
\]
and define
\[
c
=
\frac{A_0-B_0}{(A_0+B_0)^3}.
\]
Then the flow has the exact first integral
\[
\boxed{
\frac{A-B}{(A+B)^3}=c.
}
\]

Consequently, for every \(0\le t<T\), the whole trajectory is determined by the unique \(S(t)\in(0,S_0]\) satisfying
\[
\boxed{
t
=
\frac38\bigl(S_0^2-S(t)^2\bigr)
-
\frac{c^2}{8}\bigl(S_0^6-S(t)^6\bigr),
}
\]
through
\[
\boxed{
A(t)
=
\frac{S(t)}2\bigl(1+cS(t)^2\bigr),
\qquad
B(t)
=
\frac{S(t)}2\bigl(1-cS(t)^2\bigr).
}
\]

The extinction time is therefore
\[
\boxed{
T
=
\frac{A_0^2+4A_0B_0+B_0^2}{4}.
}
\]
Both factors tend to zero simultaneously at \(T\).

There is also an exact remaining-time law for the signed anisotropy
\[
\delta(t)
=
\frac{A(t)-B(t)}{A(t)+B(t)}.
\]
Namely,
\[
\boxed{
T-t
=
\frac{S(t)^2}{8}\bigl(3-\delta(t)^2\bigr).
}
\]
If \(A_0\ne B_0\), equivalently \(c\ne0\), this becomes the scalar cubic law
\[
\boxed{
T-t
=
\frac{\delta(t)\bigl(3-\delta(t)^2\bigr)}{8c}.
}
\]

As \(t\uparrow T\),
\[
\boxed{
\delta(t)
=
\frac{8c}{3}(T-t)
+
O\!\left((T-t)^3\right),
}
\]
and hence
\[
\boxed{
\frac{A(t)}{B(t)}
=
1+\frac{16c}{3}(T-t)
+
O\!\left((T-t)^2\right).
}
\]

Thus the source's qualitative conclusions—finite-time extinction and convergence of \(A/B\) to \(1\)—can be sharpened, on this invariant product family, to an exact first integral, an exact extinction time, and an exact scalar shape law.

## Assumptions and scope

The factors \(g_{S^2}\) are the unit-round metrics used in the source, so each scaled factor has Gauss curvature \(A^{-1}\) or \(B^{-1}\).

The statement concerns the unnormalized fourth-order \(J\)-flow restricted to the invariant two-parameter family
\[
A\,g_{S^2}\oplus B\,g_{S^2}.
\]
No assertion is made that an analogous first integral exists for arbitrary metrics or for perturbations outside the product ansatz.

The signed constant \(c\) can be positive, negative, or zero. Since
\[
|c|S_0^2
=
\frac{|A_0-B_0|}{A_0+B_0}
<1,
\]
all formulas below preserve positivity of both \(A\) and \(B\) until the common extinction time.

## Proof

Starting from
\[
A'
=
\frac{B-2A}{3AB},
\qquad
B'
=
\frac{A-2B}{3AB},
\]
define
\[
S=A+B,
\qquad
D=A-B.
\]
Direct addition and subtraction give
\[
S'
=
-\frac{S}{3AB},
\qquad
D'
=
-\frac{D}{AB}.
\]
Therefore, wherever \(S>0\),
\[
\frac{dD}{dS}
=
\frac{D'}{S'}
=
\frac{3D}{S}.
\]
It follows that
\[
\frac{D}{S^3}
\]
is constant. Evaluating at \(t=0\) yields
\[
D=cS^3,
\qquad
c=\frac{A_0-B_0}{S_0^3}.
\]
This proves the first integral.

Because
\[
A=\frac{S+D}{2},
\qquad
B=\frac{S-D}{2},
\]
we obtain
\[
A
=
\frac S2(1+cS^2),
\qquad
B
=
\frac S2(1-cS^2).
\]
In particular,
\[
AB
=
\frac{S^2}{4}(1-c^2S^4).
\]
The equation for \(S\) becomes
\[
S'
=
-\frac{4}{3S(1-c^2S^4)}.
\]
Since
\[
|c|S^2
\le
|c|S_0^2
<1
\]
as \(S\) decreases, the denominator remains positive. Thus \(S\) is strictly decreasing for the entire positive solution.

Separating variables gives
\[
\frac{dt}{dS}
=
-\frac34S(1-c^2S^4).
\]
Integrating from \(S_0\) to \(S(t)\) yields
\[
t
=
\frac38(S_0^2-S^2)
-
\frac{c^2}{8}(S_0^6-S^6).
\]
The right-hand side is strictly increasing as \(S\) decreases from \(S_0\) to \(0\), so this relation determines a unique \(S(t)\in(0,S_0]\).

At \(S=0\), the elapsed time is
\[
T
=
\frac38S_0^2
-
\frac{c^2}{8}S_0^6.
\]
Since
\[
c^2S_0^6=(A_0-B_0)^2,
\]
we find
\[
T
=
\frac{3(A_0+B_0)^2-(A_0-B_0)^2}{8}
=
\frac{A_0^2+4A_0B_0+B_0^2}{4}.
\]
The formulas for \(A\) and \(B\) show that both approach zero as \(S\downarrow0\).

For the shape law, put
\[
\delta=\frac{D}{S}=cS^2.
\]
Subtracting the time relation from its extinction value gives
\[
T-t
=
\frac38S^2-\frac{c^2}{8}S^6
=
\frac{S^2}{8}(3-\delta^2).
\]
When \(c\ne0\), substituting
\[
S^2=\frac{\delta}{c}
\]
gives
\[
T-t
=
\frac{\delta(3-\delta^2)}{8c}.
\]

Finally, set
\[
\tau=T-t,
\qquad
x=S^2.
\]
The exact relation is
\[
\tau
=
\frac38x-\frac{c^2}{8}x^3.
\]
Local inversion at \(x=0\) gives
\[
x
=
\frac83\tau+O(\tau^3).
\]
Therefore
\[
\delta=cx
=
\frac{8c}{3}\tau+O(\tau^3).
\]
Since
\[
\frac AB
=
\frac{1+\delta}{1-\delta},
\]
we also obtain
\[
\frac AB
=
1+\frac{16c}{3}\tau+O(\tau^2).
\]
This completes the proof.

## Verification

The bundled symbolic checker reconstructs the \(S,D\) system from the two published product equations and verifies
\[
\frac{d}{dt}\left(\frac{D}{S^3}\right)=0.
\]
It then verifies the exact formulas for \(A\), \(B\), \(AB\), the integrated time relation, and the simplification
\[
\frac38(A_0+B_0)^2-\frac18(A_0-B_0)^2
=
\frac{A_0^2+4A_0B_0+B_0^2}{4}.
\]

The checker also verifies the exact identity
\[
T-t
=
\frac{S^2}{8}(3-\delta^2)
\]
and the local inverse expansion
\[
S^2
=
\frac83(T-t)
+
O\!\left((T-t)^3\right).
\]

As a normalization check, if
\[
A_0=B_0=a,
\]
then \(c=0\), the exact extinction time becomes
\[
T=\frac32a^2,
\]
and the system reduces to
\[
A'=B'=-\frac{1}{3A},
\]
which gives
\[
A(t)^2=a^2-\frac23t.
\]
This reaches zero at exactly the same time.

All trajectory and extinction conclusions are analytic. No finite sampling is used as a substitute for the proof.

## Relationship to prior work

Chen, Kang, and Yuan introduce the fourth-order flow
\[
\partial_tg=-2J_g
\]
and study its analytic and geometric properties. In their \(S^2\times S^2\) product example, they derive exactly the two-dimensional ODE used here. They solve the volume-normalized ratio equation explicitly and prove that the unnormalized product flow becomes extinct in finite time while
\[
A/B\longrightarrow1.
\]
For the unnormalized flow, their argument passes through a time-dependent homothety of the normalized solution and proves finiteness of the extinction time qualitatively.

The inspected source does not state the invariant
\[
(A-B)/(A+B)^3,
\]
an exact extinction-time formula in terms of \(A_0,B_0\), or the exact cubic relation between anisotropy and remaining time. These are obtained by solving the equality structure of the source's two-dimensional unnormalized ODE directly.

The \(J\)-flow here is a newly introduced higher-order Riemannian flow and is unrelated to the classical Kähler \(J\)-flow, as the source itself emphasizes. Targeted searches using the source identifier, the product ODE, extinction-time terminology, first-integral terminology, and equivalent anisotropy variables did not locate a prior statement covering the formulas above.

## Limitations

The exact formulas hold only inside the \(S^2\times S^2\) product-metric family. They do not give nonlinear stability rates for general perturbations of the product metric.

The coefficient \(c\) depends on the scale of the initial metric:
\[
c=\frac{A_0-B_0}{(A_0+B_0)^3}.
\]
Accordingly, the linear coefficient in the remaining-time asymptotic is not scale invariant by itself; the exact cubic relation records the correct scale dependence.

The result gives a complete trajectory law through the scalar variable \(S\), but solving the resulting cubic equation for \(S^2\) in radicals is neither required nor geometrically more informative.

## References

1. Jiaqi Chen, Xudong Kang, and Wei Yuan, *A geometric flow associated to \(Q\)-curvature*, arXiv:2610.02993v1, first submitted 2 October 2026.
