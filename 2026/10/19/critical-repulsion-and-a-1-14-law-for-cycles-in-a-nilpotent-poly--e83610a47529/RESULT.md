# Critical repulsion and a \(1/14\)-law for cycles in a nilpotent polynomial oscillator

## Finding

Consider the real analytic planar system
\[
\dot x=y^3-x^5,\qquad \dot y=-x+m y^9,\qquad m\in\mathbb R.
\]
At the natural stability threshold \(m_*=1/3\), the origin is **locally repelling**, even though the first generalized Lyapunov coefficient vanishes. More precisely, let \(P_m(\rho)\) denote the positive-\(y\)-axis first-return coordinate of the trajectory started at \((x,y)=(0,\rho)\). There exists \(\rho_*>0\) for which this map is defined when \(0<\rho<\rho_*\) and \(m\) is sufficiently close to \(m_*\). At equality,
\[
P_{1/3}(\rho)=\rho+I\rho^{22}+O(\rho^{29}),\qquad
I=\frac{158\sqrt2}{49725}\,\mathrm B\left(\frac34,\frac12\right)>0.
\]
Here \(\mathrm B(a,b)=\int_0^1 t^{a-1}(1-t)^{b-1}\,dt\) is Euler's beta function, and \(I\approx0.01076799737737\).

Furthermore, put \(\delta=1/3-m\). For every sufficiently small \(\delta>0\) there is an **unstable hyperbolic limit cycle** near the origin, meeting the positive \(y\)-axis at an amplitude \(\rho_\delta>0\) such that
\[
\rho_\delta\sim\left(\frac{K}{I}\delta\right)^{1/14},\qquad
K=\frac{15\sqrt2}{77}\,\mathrm B\left(\frac14,\frac12\right)>0.
\]
Its physical-time period \(\mathcal T_\delta\) satisfies
\[
\mathcal T_\delta\sim
\sqrt2\,\mathrm B\left(\frac14,\frac12\right)
\left(\frac{I}{K\delta}\right)^{1/14}.
\]
The existence assertion is local; no assertion about other, distant limit cycles is made.

## Assumptions and scope

The phase variables and parameter are real, with no positivity restriction on the phase variables. All conclusions are local near the equilibrium \((0,0)\), and the bifurcating-cycle asymptotics concern \(\delta\downarrow0\). The Poincaré section is the **positive** \(y\)-axis in the original variables, oriented by crossings with \(\dot x>0\). The amplitude \(\rho\) is the original \(y\)-coordinate, not an arbitrary norm or formal normal-form radius. The stated coefficient and clock therefore have a fixed normalization.

The family is the \(k=2\), \(s=4\) member of the generalized Bacciotti polynomial systems studied in the reference below. The source establishes attraction for \(m<1/3\) and repulsion for \(m>1/3\), while expressly leaving the equality case for \(k>1\) uncomputed. That omission motivates the critical coefficient and cycle law here.

## Proof

**1. Exact generalized polar system.** Interchange the original coordinates, putting \(X=y\), \(Y=x\). Then
\[
\dot X=-Y+mX^9,\qquad \dot Y=X^3-Y^5.
\]
Define periodic functions \(C(\theta),S(\theta)\) by
\[
C'=-S,\quad S'=C^3,\quad C(0)=1,\quad S(0)=0.
\]
They satisfy \(C^4+2S^2=1\) and have period
\[
T=\sqrt2\,\mathrm B\left(\frac14,\frac12\right).
\]
The change of variables \(X=rC(\theta),\ Y=r^2S(\theta)\) parametrizes every sufficiently small punctured neighborhood with \(r=(X^4+2Y^2)^{1/4}>0\) and \(\theta\) modulo \(T\). Direct differentiation gives the **exact** equations
\[
\dot r=r^9 A_m(\theta),\quad
\dot\theta=r\bigl(1-r^7 B_m(\theta)\bigr),
\]
where
\[
A_m=mC^{12}-S^6,\qquad B_m=CS^5+2mC^9S.
\]
For small \(r\), angular motion is strictly positive. Consequently the return map on the indicated section is the time-\(T\) map of
\[
\frac{dr}{d\theta}=\frac{r^8A_m}{1-r^7B_m}.
\tag{1}
\]
Analytic dependence on \(r\) and \(m\) implies a convergent local expansion of the form \(P_m(r)=r+\sum_{j\ge1}a_j(m)r^{7j+1}\), with coefficients analytic in \(m\).

**2. Exact cancellation of the first two orders.** Fix \(m=m_*=1/3\) and write \(A=A_{1/3}\), \(B=B_{1/3}\). The function
\[
F(\theta)=\frac{CS(3+C^8)}{12}
\]
satisfies \(F'=A\), as follows by differentiating and using \(S^2=(1-C^4)/2\). Since \(F(0)=F(T)=0\),
\[
\int_0^T A\,d\theta=0.
\]
The symmetry \(C(T-\theta)=C(\theta)\), \(S(T-\theta)=-S(\theta)\) makes \(A\) even and \(B\) odd under reflection, so
\[
\int_0^T AB\,d\theta=0.
\]
In (1), set \(z=r^{-7}\). Its exact equation is
\[
z'=-7A\frac{z}{z-B}=-7A\left(1+\frac Bz+\frac{B^2}{z^2}+O(z^{-3})\right).
\]
For large \(z_0=\rho^{-7}\), expand \(z=z_0+u_1+z_0^{-1}u_2+z_0^{-2}u_3+O(z_0^{-3})\), each \(u_j(0)=0\). Equating powers gives
\[
u_1'=-7A,\qquad u_2'=-7AB,\qquad
u_3'=-7A(B^2-Bu_1).
\]
Thus \(u_1=-7F\), \(u_1(T)=u_2(T)=0\), and
\[
z(T)=z_0-7z_0^{-2}\int_0^T A(B^2+7BF)\,d\theta+O(z_0^{-3}).
\tag{2}
\]

**3. Exact positivity of the first surviving coefficient.** Set \(u=C^4\). On the energy oval, \(S^2=(1-u)/2\), and the factors appearing in (2) reduce to
\[
A=\frac{11u^3-9u^2+9u-3}{24},\quad
B=CS\frac{11u^2-6u+3}{12},\quad
F=CS\frac{u^2+3}{12}.
\]
It follows that
\[
A(B^2+7BF)=C^2 P(u),
\]
where
\[
P(u)=\frac{(1-u)(3u^2-u+4)(11u^2-6u+3)(11u^3-9u^2+9u-3)}{1152}.
\]
Under the normalized positive weight \(C^2\,d\theta\), the variable \(u=C^4\) has beta distribution with parameters \((3/4,1/2)\). Its moments are
\[
\mathbb E[u^j]=\frac{(3/4)_j}{(5/4)_j},\qquad j\in\mathbb Z_{\ge0},
\]
where \((a)_j\) is the ordinary rising factorial. Expanding \(P\) and applying these rational moments gives the **exact** identity
\[
\mathbb E[P(u)]=\frac{158}{49725}>0.
\]
Because \(\int_0^T C^2\,d\theta=\sqrt2\,\mathrm B(3/4,1/2)\), the integral in (2) is exactly \(I\) as displayed in the finding. Finally, converting \(z(T)=\rho^{-7}-7I\rho^{14}+O(\rho^{21})\) back to the radius yields
\[
P_{1/3}(\rho)=\rho+I\rho^{22}+O(\rho^{29}).
\]
Since \(I>0\), each sufficiently small nonzero point spirals out across successive local sections: the nilpotent equilibrium is repelling. No finite numerical experiment is used for this sign.

**4. Perturbation, limit-cycle birth and original-time clock.** For arbitrary \(m\) near \(1/3\), the leading coefficient of (1) integrates to
\[
a_1(m)=\int_0^T A_m\,d\theta=K(m-1/3),\quad
K=\int_0^T C^{12}\,d\theta
=\frac{15\sqrt2}{77}\,\mathrm B(1/4,1/2).
\]
Here \((1/4)_3/(3/4)_3=15/77\) gives the final equality. Analytic dependence and the two cancellations proved above show that, uniformly near \(m=1/3\),
\[
P_{1/3-\delta}(r)-r
=r^8\left[-K\delta+O(\delta r^7)
+\bigl(I+O(\delta)\bigr)r^{14}+O(r^{21})\right].
\tag{3}
\]
Set \(r=\delta^{1/14}R\) in (3), divide by \(\delta r^8\), and let \(\delta\downarrow0\). On every compact positive \(R\)-interval the result converges in \(C^1\) to \(-K+IR^{14}\). Its unique positive zero \(R_*=(K/I)^{1/14}\) is simple. The implicit-function argument therefore produces a positive return-map fixed point with
\[
\rho_\delta\sim R_*\delta^{1/14}.
\]
The derivative of the actual return map there is
\[
P'_{1/3-\delta}(\rho_\delta)
=1+14I\rho_\delta^{21}+o(\rho_\delta^{21})>1,
\]
so this orbit is an unstable hyperbolic limit cycle. Along this small cycle \(r(\theta)=\rho_\delta(1+O(\rho_\delta^7))\) over a complete angular circuit, while \(\dot\theta=r(1-r^7B_m)\). Hence the original physical duration of one circuit is \(T/\rho_\delta(1+o(1))\), proving the asserted period asymptotic.

## Verification

The companion `verify.py` checks the coordinate identities modulo \(C^4+2S^2=1\), the polynomial antiderivative \(F'=A\), the exact rational beta-moment identity \(158/49725\), and the ratio \((1/4)_3/(3/4)_3=15/77\). It also integrates the **unexpanded** generalized-polar equations at three finite amplitudes; these values approach the analytical coefficient \(I\) from above as the amplitude decreases. Run from the package directory using `python verify.py` with Python 3, SymPy and SciPy installed. Output should begin with `VERIFY_OK`.

The finite-amplitude calculations provide a cross-check only. The sign, powers, and local existence assertions are established by the exact ODE and beta-integral proof above.

## Relationship to prior work

García-Saldaña, Gasull and Giacomini (arXiv:1304.2163, first submitted 2013-04-08) studied this generalized polynomial family. Their Theorem 1.3 determines the origin's stability on either side of the boundary and treats the degenerate equality \(k=1\), but explicitly states that the cases \(s=2k\), \(k>1\), at exact equality were not computed. Their generalized-polar formula (8) supplies the starting reduction, not the critical \(k=2\) coefficient, its sign, or the new cycle and physical-time scalings.

Huang and Liang (arXiv:1708.07959) establish criteria for bounds on the *number* of limit cycles in sums of quasihomogeneous planar fields. Those existence/uniqueness conditions do not yield the present high-order critical local displacement or its exact amplitude constant. Standard nilpotent-center/focus techniques explain why one should compute higher Lyapunov coefficients, but the coefficient \(I\) and its cancellation structure require the case-specific calculation here.

## Limitations

Only the first omitted integer case \(k=2\) is solved; the exact critical boundary for general \(k>2\) is not classified. The existence and instability of one **local** small cycle for \(m\uparrow1/3\) do not exclude other cycles away from the origin. The coefficient and scaling are tied to the original positive-axis crossing amplitude. No rigorous classification of all global invariant sets or complete parameter bifurcation diagram is claimed. Historical priority beyond the inspected material requires independent literature assessment.

## References

1. J. D. García-Saldaña, A. Gasull and H. Giacomini, *Bifurcation diagram and stability for a one-parameter family of planar vector fields*, arXiv:1304.2163, first posted 2013-04-08; see Theorem 1.3 and Section 2, especially equations (7)–(12). https://arxiv.org/abs/1304.2163
2. J. Huang and H. Liang, *Limit cycles of planar system defined by the sum of two quasi-homogeneous vector fields*, arXiv:1708.07959, first posted 2017-08-26; see Theorem 1.1 and the hypotheses for cycle-count bounds. https://arxiv.org/abs/1708.07959
3. G. Galeotti and F. Gori, *Bifurcations and limit cycles in a family of planar polynomial dynamical systems* (1988), as cited and discussed in reference 1. Bibliographic and scientific attribution here relies on reference 1; the 1988 primary text was not independently inspected.
