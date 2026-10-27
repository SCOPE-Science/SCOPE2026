# A reentrant positivity window for unstabilized second-order exponential Runge–Kutta decay

## Finding
For the scalar decay equation \(u'=-(a+b)u\), \(a,b>0\), use the standard two-stage Hochbruck–Ostermann exponential Runge–Kutta method of stiff order two, with stage abscissa \(c_2=1\), treating \(-au\) exponentially and \(-bu\) as the remainder. Write \(x=ah>0\), \(\rho=b/a\), and let \(R_\rho(x)\) be the one-step multiplier. Then
\[
R_\rho(x)=e^{-x}+\rho^2(1-e^{-x})-\rho(1+\rho)\frac{(1-e^{-x})^2}{x}.
\]
For every \(0<\rho\le 1/4\) and every \(x>0\), \(|R_\rho(x)|<1\): the method strictly dissipates the scalar quadratic energy for every positive step. Yet for every sufficiently small \(\rho>0\) (in particular, every \(0<\rho\le1/100\)) there are *exactly two* positive simple zeros \(x_-(\rho)<x_+(\rho)\); the multiplier is negative precisely on \((x_-,x_+)\), and positive elsewhere. Its unique minimum occurs at \(x_m(\rho)\). With \(L=\log(1/\rho)\), the sharp singular asymptotics are
\[
 x_-=L+\log L+o(1),\qquad x_m=L+2\log L+o(1),\qquad x_+=\rho^{-1}+1+o(1),
\]
\[
 \min_{x>0}R_\rho(x)=-\frac{\rho}{\log(1/\rho)}(1+o(1)).
\]
Thus sign failure occurs on a bounded intermediate-step interval whose upper endpoint diverges reciprocally with the remainder-to-exponential split ratio, while all-step energy contraction survives.

## Assumptions and scope
The stage rule is \(v=e^{-x}u-hb\varphi_1(-x)u\), followed by
\[
 u^+=e^{-x}u-hb\{[\varphi_1(-x)-\varphi_2(-x)]u+\varphi_2(-x)v\},
\]
where \(\varphi_1(z)=(e^z-1)/z\) and \(\varphi_2(z)=(e^z-1-z)/z^2\), continuously extended at zero. This is exactly the \(c_2=1\) method of Quan–Zheng–Zhou, equation (41), and the classical method analyzed for linear stability by Caliari–Cassini–Einkemmer–Ostermann, equation (5). Statements concern exact arithmetic, fixed one-step output, scalar real initial values, and the indicated positive splitting \(a,b\). They do not apply to all exponential integrators, arbitrary nonlinear remainders, or arbitrary matrix splits. The positivity property means \(u\ge0\implies u^+\ge0\).

## Proof
Put \(q=e^{-x}\) and \(s=1-q\). Since \(\varphi_1(-x)=s/x\) and \(\varphi_2(-x)=(x-s)/x^2\), direct substitution in both stages gives the displayed exact multiplier. For \(x>0\), \(0<s<x\), hence \(J=1-s/x\) lies in \((0,1)\). Rearrangement yields
\[
 1-R_\rho(x)=(1+\rho)s(1-\rho J)>0
\]
when \(0<\rho\le1/4\). Moreover \(0<s<\min\{x,1\}\) implies \(s^2/x<1\); therefore
\[
 R_\rho(x)>-\rho(1+\rho)s^2/x>-\rho(1+\rho)>-1.
\]
This proves strict energy contraction independently of the sign. The endpoints are \(R_\rho(0+)=1\) and \(R_\rho(+\infty)=\rho^2>0\).

Differentiation, with positive factor \(q\) extracted, gives
\[
 R_\rho'(x)=q\left[-(1-\rho^2)-2\rho(1+\rho)\frac{s}{x}+\rho(1+\rho)\left(\frac{2\sinh(x/2)}{x}\right)^2\right].
\]
The function \(s/x\) decreases strictly from \(1\) to \(0\), whereas \(2\sinh(x/2)/x\) increases strictly from \(1\) to infinity. Consequently the bracket is strictly increasing, from \(-(1+\rho)\) to infinity. Thus \(R_\rho\) has exactly one stationary point, a strict global minimum.

Take \(L=\log(1/\rho)\) and \(x=2L\). Then \(q=\rho^2\), and
\[
 R_\rho(2L)\le 2\rho^2-\frac{\rho(1-\rho^2)^2}{2L}<0
\]
for every \(0<\rho\le1/100\). The last inequality follows from \(4\rho\log(1/\rho)\le4(1/100)\log100<(1-10^{-4})^2\). By the positive endpoint limits and the unique minimum, the graph crosses zero exactly twice and is negative only between the two crossings.

For any fixed \(0<\delta<1\), at \(x=(1-\delta)L\) the exponential \(q=\rho^{1-\delta}\) dominates the negative term of size at most \(O(\rho/L)\), whereas at \(x=(1+\delta)L\) the negative term \(-\rho/x\) dominates both \(q=\rho^{1+\delta}\) and \(\rho^2\). Hence \(x_-/L\to1\). At its zero, using \(x_-\asymp L\), the exact equation becomes \(e^{-x_-}=\rho/x_-(1+o(1))\). Taking logarithms proves \(x_-=L+\log L+o(1)\).

At \(x=k/\rho\), for fixed \(k>0\), the same formula gives \(R_\rho(k/\rho)/\rho^2\to1-1/k\). Thus \(\rho x_+\to1\). At the exact upper zero the exponential terms are exponentially smaller than any power of \(\rho\), so solving its equation gives the sharper \(x_+=(1+\rho)/\rho+o(1)\).

At the unique minimum \(x_m\), the derivative equation reads
\[
 e^{-x_m}=\frac{\rho(1+\rho)(1-e^{-x_m})^2}{x_m^2\left[1-\rho^2+2\rho(1+\rho)(1-e^{-x_m})/x_m\right]}.
\]
Comparing derivative signs at \((1\pm\delta)L\) first gives \(x_m/L\to1\). The right-hand side is therefore \(\rho/x_m^2(1+o(1))\), and taking logarithms gives \(x_m=L+2\log L+o(1)\). Substitution into \(R_\rho\) then gives \(\min R_\rho=-\rho/L(1+o(1))\), because \(e^{-x_m}=O(\rho/L^2)\) and \(\rho^2=o(\rho/L)\). All little-oh statements are as \(\rho\downarrow0\).

## Verification
`check_etdrk2.py` independently evaluates the two stages and the closed formula, checks energy contraction and sign crossings across tested positive parameters, and numerically checks the slowly converging singular asymptotics. It passed 261 deterministic assertions. The proof above, not the finite checks, establishes the quantified theorem. For example \(\rho=0.1\) and \(x=6\) give \(R_\rho(x)\approx-0.00578859\), although the exact multiplier is \(e^{-6.6}>0\).

## Relationship to prior work
Quan, Zheng, and Zhou (2026), equation (41) and Section 4.1, supply the exact method and sufficient energy-dissipation step restriction for general gradient flows. The scalar unconditional *linear stability* fact is already covered by Caliari, Cassini, Einkemmer, and Ostermann (2023), Theorem 2.4: with their linear-split fraction \(\lambda=1/(1+\rho)\), \(c_2=1\), unconditional stability holds for \(\rho\le1\). Neither prior energy/stability claim implies positivity. The contribution here is precisely the bounded reentrant sign-loss interval, uniqueness of its endpoints, and three distinct asymptotic scales and depth. Work on specially designed positivity-preserving exponential Runge–Kutta schemes does not imply positivity of this unstabilized Hochbruck–Ostermann scheme.

## Limitations
This is a scalar *split-dependent* counterexample: a different splitting of the same differential equation may have different behavior. The theorem does not determine the largest possible \(\rho\) giving sign loss, though it gives the explicit nonempty range \(0<\rho\le1/100\) and complete small-ratio asymptotics. The unconditional contraction statement is prior literature and is included as motivation rather than a novelty claim. No multivariate, nonlinear, finite-precision, or adaptive-step conclusion follows automatically. Historical priority for the new sign-window asymptotics remains subject to independent verification.

## References
1. C. Quan, P. Zheng, Z. Zhou, *A unified framework for original energy dissipation of equilibrium-preserving exponential Runge–Kutta methods for L2 gradient flows*, arXiv:2610.11532v1 (first posted 2026-10-08), Sections 2.1 and 4.1, equation (41). https://arxiv.org/html/2610.11532v1
2. M. Caliari, F. Cassini, L. Einkemmer, A. Ostermann, *Accelerating exponential integrators to efficiently solve semilinear advection-diffusion-reaction equations*, arXiv:2303.15861 (first posted 2023-03-28), Section 2 and Theorem 2.4. https://arxiv.org/pdf/2303.15861
3. J. Hu, R. Shu, *A second-order asymptotic-preserving and positivity-preserving exponential Runge–Kutta method for a class of stiff kinetic equations*, arXiv:1807.03728 (2018); a different positivity-designed scheme. https://arxiv.org/abs/1807.03728
