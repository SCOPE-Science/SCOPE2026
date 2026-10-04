# A sharp flip frontier for the Polar-Express surrogate on scalar quadratics
## Finding

Consider
\[
f(x)=\frac a2x^2,\qquad a>0,
\]
and the deterministic unconstrained nonlinear-preconditioned gradient step
\[
x_{k+1}
=
x_k-\gamma\,h_4'(a x_k),
\qquad
h_4'(d)
=
\frac{d}{\bigl(\varepsilon^4+|d|^4\bigr)^{1/4}},
\]
where
\[
\gamma>0,\qquad \varepsilon>0.
\]
The nonlinear preconditioner \(h_4'\) is the smooth scalar surrogate identified in the source as a closer model of the Polar Express update than the exact sign map.

Introduce the dimensionless variables
\[
u_k=\frac{a x_k}{\varepsilon},
\qquad
\tau=\frac{\gamma a}{\varepsilon}.
\]
The iteration becomes
\[
u_{k+1}
=
T_\tau(u_k)
:=
u_k\left[
1-\frac{\tau}{(1+|u_k|^4)^{1/4}}
\right].
\]

The exact scalar phase diagram is as follows.

For
\[
0<\tau\le2,
\]
the origin is globally asymptotically stable. If
\[
0<\tau<2,\qquad \tau\ne1,
\]
then every nonzero trajectory that does not hit the origin finitely satisfies
\[
\lim_{k\to\infty}
\frac{|u_{k+1}|}{|u_k|}
=
|1-\tau|.
\]

At the matched step
\[
\tau=1,
\]
the linear term cancels and
\[
u_{k+1}
=
\frac14u_k^5+O(u_k^9),
\]
so the local convergence order is five.

At the sharp stability boundary
\[
\tau=2,
\]
all trajectories still converge to zero, but the decay is algebraic rather than linear. Every nonzero trajectory that does not hit zero finitely satisfies
\[
|u_k|
\sim
(2k)^{-1/4},
\]
and its sign eventually alternates. Consequently,
\[
|x_k|
\sim
\frac{\varepsilon}{a}(2k)^{-1/4},
\qquad
|\nabla f(x_k)|
\sim
\varepsilon(2k)^{-1/4},
\]
and
\[
f(x_k)
\sim
\frac{\varepsilon^2}{2a}(2k)^{-1/2}.
\]

For
\[
\tau>2,
\]
the origin is unstable and a nonzero symmetric two-cycle exists at
\[
u_\star
=
\left[
\left(\frac{\tau}{2}\right)^4-1
\right]^{1/4},
\qquad
T_\tau(u_\star)=-u_\star.
\]
This cycle is locally asymptotically stable for every \(\tau>2\). Its two-step linear multiplier is
\[
\left(1-\frac{32}{\tau^4}\right)^2<1.
\]

Thus the exact scalar fixed-step frontier is
\[
\gamma a=2\varepsilon.
\]
The smoothing scale \(\varepsilon\) is not only a shape parameter: on a quadratic mode it sets the exact learning-rate scale separating convergence to the minimizer from a persistent nonzero two-cycle.

## Assumptions and scope

The objective is one-dimensional and quadratic, the nonsmooth term is absent, gradients are exact, and the step \(\gamma\) is constant. The preconditioner is exactly
\[
h_4'(d)=d/(\varepsilon^4+|d|^4)^{1/4},
\]
the \(\kappa=4\) member of the family introduced in the source as a smooth model for Polar Express.

The result analyzes the source framework before the additional practical input-normalization layer used in its dedicated Polar Express theorem. It therefore concerns the base nonlinear preconditioned-gradient map
\[
x^{k+1}=x^k-\gamma\nabla\phi^*(\nabla f(x^k))
\]
with the new \(h_4\) reference function, not the separately pre-normalized stochastic update.

No claim is made for matrix-valued noncommuting modes, momentum, stochastic gradients, nonquadratic objectives, or the actual finite polynomial iteration used to compute the matrix polar factor.

## Proof

Since
\[
a x_k=\varepsilon u_k,
\]
we have
\[
h_4'(a x_k)
=
\frac{u_k}{(1+|u_k|^4)^{1/4}},
\]
and therefore
\[
u_{k+1}
=
u_k
\left[
1-\frac{\tau}{(1+|u_k|^4)^{1/4}}
\right].
\]

Let
\[
v_k=|u_k|,
\qquad
D(v)=(1+v^4)^{1/4}.
\]
Then
\[
v_{k+1}
=
v_k\left|1-\frac{\tau}{D(v_k)}\right|.
\]

If
\[
0<\tau\le2
\]
and \(v>0\), then \(D(v)>1\), hence
\[
0<\frac{\tau}{D(v)}<2.
\]
Thus
\[
0\le
\left|1-\frac{\tau}{D(v)}\right|
<1.
\]
It follows that \(v_k\) is strictly decreasing unless it reaches zero. Let its limit be \(\ell\ge0\). If \(\ell>0\), continuity gives a limiting multiplier strictly below one, contradicting \(v_k\to\ell>0\). Hence
\[
v_k\to0.
\]
This proves global asymptotic stability for \(0<\tau\le2\).

For
\[
0<\tau<2,\qquad \tau\ne1,
\]
continuity immediately yields
\[
\frac{v_{k+1}}{v_k}
\longrightarrow
|1-\tau|.
\]

For the matched value \(\tau=1\), the expansion
\[
(1+u^4)^{-1/4}
=
1-\frac14u^4+O(u^8)
\]
gives
\[
T_1(u)
=
u\left[
1-(1+u^4)^{-1/4}
\right]
=
\frac14u^5+O(u^9).
\]
Thus the local order is five.

At \(\tau=2\),
\[
(1+v^4)^{-1/4}
=
1-\frac14v^4+O(v^8),
\]
so, for sufficiently small positive \(v\),
\[
\left|1-\frac{2}{D(v)}\right|
=
1-\frac12v^4+O(v^8).
\]
Therefore
\[
v_{k+1}
=
v_k-\frac12v_k^5+O(v_k^9).
\]
Equivalently,
\[
v_{k+1}^{-4}-v_k^{-4}
=
2+o(1).
\]
By summation,
\[
v_k^{-4}\sim2k,
\]
which proves
\[
v_k\sim(2k)^{-1/4}.
\]
Moreover, once \(v_k^4<15\), we have \(D(v_k)<2\), so the signed multiplier is negative and the sign alternates thereafter.

Now suppose
\[
\tau>2.
\]
The derivative at the origin is
\[
T_\tau'(0)=1-\tau,
\]
whose modulus exceeds one, so the fixed point is unstable.

A symmetric two-cycle requires
\[
T_\tau(u_\star)=-u_\star,
\]
equivalently
\[
\frac{\tau}{D(u_\star)}=2.
\]
This has the unique positive solution
\[
u_\star
=
\left[
\left(\frac{\tau}{2}\right)^4-1
\right]^{1/4}.
\]

For \(u>0\),
\[
\frac{d}{du}
\left[
\frac{u}{(1+u^4)^{1/4}}
\right]
=
(1+u^4)^{-5/4},
\]
so
\[
T_\tau'(u)
=
1-\tau(1+u^4)^{-5/4}.
\]
At \(u_\star\),
\[
T_\tau'(u_\star)
=
1-\frac{32}{\tau^4}.
\]
Oddness gives the same derivative at \(-u_\star\), hence the derivative of the two-step map at either point of the cycle is
\[
\left(1-\frac{32}{\tau^4}\right)^2.
\]
For every \(\tau>2\),
\[
-1<
1-\frac{32}{\tau^4}
<1,
\]
so the cycle is locally asymptotically stable.

## Verification

The standalone script `artifacts/verify_polar_surrogate_scalar.py` checks the exact map, the \(\tau=1\) fifth-order coefficient, the \(\tau>2\) two-cycle and its multiplier, global magnitude contraction for representative points when \(0<\tau\le2\), and the critical asymptotic law numerically over a long trajectory.

The numerical asymptotic replay is supporting evidence only. The global stability statement, critical exponent, and local two-cycle stability are proved analytically above.

## Relationship to prior work

Oikonomidis, Quan, Antonakopoulos, Silveti-Falls, Cevher, and Patrinos introduce the family
\[
(h_\kappa^*)'(d)
=
\frac{d}{(\varepsilon^\kappa+|d|^\kappa)^{1/\kappa}}
\]
and identify the \(\kappa=4\) member as a substantially closer smooth model of Polar Express than the exact sign map. Their general deterministic framework covers fixed-step nonlinear preconditioned gradient maps and their dedicated Polar Express section studies an additional input-normalization layer. The inspected paper does not state the scalar quadratic flip frontier, the quintic matched-step cancellation, or the critical \(k^{-1/4}\) law.

The earlier nonlinear-preconditioning paper of Oikonomidis, Quan, Laude, and Patrinos develops the general map
\[
x^{k+1}
=
x^k-\gamma\nabla\phi^*(\lambda\nabla f(x^k))
\]
and analyzes several sigmoid-like preconditioners under generalized smoothness. Its inspected reference-function table and convergence theory do not contain the new \(\kappa=4\) Polar-Express surrogate or this scalar bifurcation calculation.

Amsel, Persson, Musco, and Gower introduce Polar Express as an adaptive polynomial algorithm for computing matrix polar factors. Their scalar iterations concern convergence of polynomial approximations to the sign function; they do not analyze the optimization iteration obtained by replacing the gradient with the smooth nonlinear surrogate above.

Targeted searches for the exact surrogate, scalar quadratic dynamics, fixed-step stability, period-two behavior, and fifth-order matched-step convergence did not locate a prior statement equivalent to this phase diagram.

## Limitations

The stable two-cycle for \(\tau>2\) is proved locally, not globally. The result does not classify all possible large-amplitude dynamics above the stability frontier.

The practical Polar Express implementation includes matrix normalization and a finite polynomial sign approximation. The source also studies a pre-normalized version of its surrogate. Those dynamics are different and are not covered by the present theorem.

The scalar result does not imply that \(\gamma L\le2\varepsilon\) is a necessary or sufficient matrix-wide condition in noncommuting or stochastic problems. Its role is to isolate the exact behavior of one quadratic mode of the newly introduced smooth surrogate.

## References

1. K. Oikonomidis, J. Quan, K. Antonakopoulos, A. Silveti-Falls, V. Cevher, P. Patrinos, *Constrained Stochastic Spectral Preconditioning Converges for Nonconvex Objectives*, arXiv:2605.11850v1, 2026.
2. K. Oikonomidis, J. Quan, E. Laude, P. Patrinos, *Nonlinearly Preconditioned Gradient Methods under Generalized Smoothness*, arXiv:2502.08532, 2025; Proceedings of Machine Learning Research 267, 2025.
3. N. Amsel, D. Persson, C. Musco, R. M. Gower, *The Polar Express: Optimal Matrix Sign Methods and Their Application to the Muon Algorithm*, arXiv:2505.16932, 2025.
