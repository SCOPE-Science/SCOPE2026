# Sharp scalar \(R=1\) boundary for dissipative Carleman truncation
## Finding
Consider the scalar unforced quadratic ODE
\[
\dot u(t)=-a\,u(t)-b\,u(t)^2,\qquad
u(0)=u_0,
\]
with
\[
a>0,\qquad b>0,\qquad u_0>0.
\]
For this family, the nonlinearity parameter used by Li and An is
\[
R=\frac{b u_0}{a}.
\]
The exact nonlinear solution is
\[
u(t)=
\frac{u_0e^{-at}}
{1+R(1-e^{-at})},
\qquad t\ge0.
\]
It is positive, global, strictly decreasing, and tends to zero for every \(R>0\).

Let \(\widehat u_N(t)\) denote the degree-one component of the source's standard order-\(N\) Carleman truncation, initialized by the exact monomials. After undoing any constant rescaling \(u_\gamma=\gamma u\), one has the exact formula
\[
\boxed{
\widehat u_N(t)
=
u_0e^{-at}
\sum_{k=0}^{N-1}
\bigl[-R(1-e^{-at})\bigr]^k
}.
\]
Therefore
\[
\boxed{
\frac{|\widehat u_N(t)-u(t)|}{u(t)}
=
\bigl[R(1-e^{-at})\bigr]^N
}.
\]

This gives a complete convergence trichotomy.

For a finite horizon \(T>0\),
\[
\widehat u_N\longrightarrow u
\quad\hbox{uniformly on }[0,T]
\]
if and only if
\[
R(1-e^{-aT})<1.
\]
When \(R>1\), define
\[
t_c=
\frac1a\log\frac{R}{R-1}.
\]
At \(t=t_c\), the relative error equals one for every \(N\), and for every fixed \(t>t_c\) it grows exponentially with \(N\). Thus finite-order Carleman truncations can converge for \(R>1\) on short horizons, but they necessarily fail at sufficiently late time on this globally stable scalar family.

On the whole half-line, absolute-error convergence has the sharp threshold
\[
\boxed{R\le1}.
\]
For \(R<1\), the relative error is uniformly bounded by \(R^N\). At the critical value \(R=1\), the relative error is not uniform in time, but the absolute error still converges uniformly. Its exact maximum is
\[
E_N:=
\sup_{t\ge0}
|\widehat u_N(t)-u(t)|
=
u_0
\frac{x_N(1-x_N)^N}{2-x_N},
\]
where
\[
x_N=
\frac{N+1-\sqrt{N^2+1}}{N}.
\]
In particular,
\[
E_N\sim\frac{u_0}{2eN}.
\]
Hence the boundary \(R=1\) changes the all-time convergence rate from geometric to algebraic.

There is also a matching obstruction at the lifted linear-system level. Under the rescaling prescribed by Li and An, every \(R>1\) has some finite truncation order satisfying
\[
N>\frac{R+3}{R-1}
\]
for which the Hermitian part of the truncated Carleman matrix has a positive Rayleigh quotient. Thus the lifted system cannot remain dissipative at all truncation orders once \(R>1\).

## Assumptions and scope
The result concerns the unshifted monomial Carleman embedding and the finite-section truncation used in arXiv:2608.25822v1. Constant rescaling of the dependent variable is allowed and does not change the decoded approximation or the parameter \(R\).

The scalar equation is deliberately chosen with a negative quadratic term. It is globally stable for every \(R>0\), so failure beyond the threshold is a truncation phenomenon rather than finite-time blow-up of the nonlinear ODE.

The theorem does not rule out convergence for particular multidimensional systems with \(R>1\), nor does it rule out pivot-shifted, contour-integral, Koopman, or other alternative linearization strategies. It shows that a universal stronger-nonlinearity extension of this specific unshifted Carleman mechanism cannot be justified from dissipativity of the original nonlinear flow alone.

## Proof
The exact solution follows by setting
\[
w(t)=\frac1{u(t)}.
\]
Then
\[
\dot w=aw+b,
\]
so
\[
w(t)=\frac{e^{at}}{u_0}+\frac ba(e^{at}-1),
\]
which gives the displayed formula for \(u(t)\).

For the Carleman lift, define
\[
y_j(t)=u(t)^j.
\]
The infinite system is
\[
\dot y_j=-ja\,y_j-jb\,y_{j+1},
\qquad j\ge1.
\]
The order-\(N\) finite section sets the coupling from level \(N\) to level \(N+1\) to zero and uses
\[
\widehat y_j(0)=u_0^j.
\]
Backward variation of constants gives, for \(1\le j\le N\),
\[
\widehat y_j(t)
=
u_0^j e^{-jat}
\sum_{k=0}^{N-j}
\binom{j+k-1}{k}
\bigl[-R(1-e^{-at})\bigr]^k.
\]
For \(j=1\), all binomial coefficients equal one, yielding
\[
\widehat u_N(t)
=
u_0e^{-at}
\sum_{k=0}^{N-1}(-z)^k,
\qquad
z=R(1-e^{-at}).
\]
Using
\[
\sum_{k=0}^{N-1}(-z)^k
=
\frac{1-(-z)^N}{1+z}
\]
and
\[
u(t)=\frac{u_0e^{-at}}{1+z}
\]
gives the exact relative-error identity
\[
\frac{|\widehat u_N(t)-u(t)|}{u(t)}=z^N.
\]

Because \(z(t)\) is increasing, the maximum relative error on \([0,T]\) is
\[
\bigl[R(1-e^{-aT})\bigr]^N.
\]
This proves the finite-horizon criterion and the critical time \(t_c\).

At \(R=1\), put
\[
x=e^{-at}.
\]
Then
\[
\frac{|\widehat u_N(t)-u(t)|}{u_0}
=
\frac{x(1-x)^N}{2-x}.
\]
The function vanishes at both endpoints of \([0,1]\). Its interior critical point satisfies
\[
N x^2-2(N+1)x+2=0.
\]
The unique root in \((0,1)\) is \(x_N\), so it gives the exact maximum \(E_N\). Since
\[
x_N\sim\frac1N,
\qquad
(1-x_N)^N\longrightarrow e^{-1},
\qquad
2-x_N\longrightarrow2,
\]
one obtains
\[
E_N\sim\frac{u_0}{2eN}.
\]

It remains to check the lifted dissipativity obstruction. Let the source's rescaled variable be
\[
u_\gamma=\gamma u.
\]
For the unforced scalar equation, the source's rescaling equation gives
\[
\frac b\gamma=\frac{1+R}{2}a=:c.
\]
The truncated Carleman matrix \(A_N\) is upper bidiagonal with
\[
(A_N)_{j,j}=-ja,
\qquad
(A_N)_{j,j+1}=-jc.
\]
Let
\[
H_N=\frac{A_N+A_N^\dagger}{2}
\]
and take the real alternating vector
\[
v_j=(-1)^j.
\]
Then
\[
v^\dagger H_Nv
=
-a\sum_{j=1}^N j
+
c\sum_{j=1}^{N-1}j
=
\frac N2\bigl[(c-a)N-(a+c)\bigr].
\]
Because
\[
\frac ca=\frac{1+R}{2},
\]
this Rayleigh quotient is positive whenever
\[
N>\frac{R+3}{R-1}.
\]
For every \(R>1\), such an integer \(N\) exists, proving the stated lifted-system obstruction.

Finally, constant rescaling cannot change the truncation formula: replacing \(u\) by \(u_\gamma=\gamma u\) changes \(b\) to \(b/\gamma\) and \(u_0\) to \(\gamma u_0\), leaving
\[
\frac{(b/\gamma)(\gamma u_0)}a=R
\]
unchanged. Dividing the degree-one truncated component by \(\gamma\) therefore returns exactly the same \(\widehat u_N(t)\).

## Verification
The universal statements above are analytic. The exact nonlinear solution, the full order-\(N\) Carleman formula, the geometric-series remainder, the critical-point equation at \(R=1\), and the lifted Rayleigh quotient are all derived symbolically.

The bundled checker independently verifies the finite-section formula against direct triangular ODE propagation for several exact rational parameter choices and truncation orders, checks the finite-horizon trichotomy numerically away from its exact boundary, verifies the \(R=1\) maximizing point, and confirms the lifted Rayleigh-quotient identity. Those finite computations are corroborative only and are not used to infer the universal theorem.

## Relationship to prior work
Li and An define
\[
R=
\frac1{-\mu(F_1)}
\left(
\|F_2\|\|u(0)\|
+
\frac{\|F_0\|}{\|u(0)\|}
\right)
\]
and prove their fast-forwarded algorithm under \(R<1\). Their numerical Section 5 deliberately tests dissipative systems with values up to approximately \(R=1.57\), observes convergence on the tested finite horizon, and concludes that \(R<1\) is sufficient but is not a sharp necessary condition for that numerical model. The theorem here is compatible with those observations: it shows exactly how \(R>1\) can still converge on a short horizon while failing at sufficiently late time in another, globally stable, dissipative system.

The 2025 paper *Carleman approximants for non-linear differential systems* studies the closely related Riccati equation
\[
\dot v=-v+v^2
\]
and writes its infinite monomial Carleman recurrence, low-order finite sections, and higher-order numerical illustrations. After a sign and scale change, that recurrence contains the scalar family used here. However, the inspected article does not state the all-order geometric remainder, the finite-horizon if-and-only-if criterion, the critical \(R=1\) algebraic uniform-error law, or the explicit eventual loss of lifted dissipativity for every \(R>1\).

Forets and Pouly develop general explicit local error bounds for Carleman linearization. Their results motivate quantitative truncation analysis but do not give the source-specific sharp \(R=1\) trichotomy proved here.

## Limitations
The scalar theorem is a sharp boundary example, not a characterization of all dissipative nonlinear systems. Some multidimensional systems can converge beyond \(R=1\), as the anchor paper demonstrates numerically. The result does not analyze pivot-shifted Carleman linearization or other embeddings that change the expansion center.

The lifted Rayleigh argument proves eventual non-dissipativity for the source-prescribed scaling when \(R>1\); it does not identify the smallest truncation order where the largest Hermitian-part eigenvalue becomes positive. The displayed integer threshold is a sufficient order obtained from an explicit test vector.

## References
1. Y. Li and D. An, *Fast-forwarding quantum algorithms for weakly nonlinear dissipative differential equations and beyond*, arXiv:2608.25822v1 (first public 2026-08-26).
2. J. C. M. Sancho, S. F. Escribano, and J. A. Oller, *Carleman approximants for non-linear differential systems*, Physica Scripta 100 (2025), DOI 10.1088/1402-4896/add65a.
3. M. Forets and A. Pouly, *Explicit Error Bounds for Carleman Linearization*, arXiv:1711.02552.
