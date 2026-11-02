# Exponentially thin attracting-cycle windows at the critical grazing slope

## Finding
Consider the continuous one-dimensional grazing map
\[
f_{\mu}(x)=\begin{cases}
\nu x+e(\mu-x)^{\gamma},&x<\mu,\\
\nu x,&x\geq\mu,
\end{cases}
\qquad
\gamma=\frac qp\in(0,1),\quad
\nu=\frac{1}{1+\gamma}=\frac p{p+q},\quad e>0.
\]
Here \(p>q\) are coprime positive integers. There exists an integer \(M_0=M_0(\gamma)\) such that for every integer \(M\geq M_0\), an explicit nonempty interval of \(\mu>0\) supports an attracting primitive period-\(M\) orbit with exactly one visit to the nonlinear region \(x<\mu\) and \(M-1\) visits to \(x>\mu\). The intervals are pairwise disjoint for all sufficiently large \(M\) and accumulate at \(\mu=0\).

The exact interval and its limiting relative width are as follows. Set
\[
\varepsilon_M=\nu^M,\qquad
z_M^*=\frac{1+\varepsilon_M}{1+\gamma+(1-\gamma)\varepsilon_M},
\]
\[
\lambda_M^*=\left[\varepsilon_M+(1-\varepsilon_M)\frac{z_M^*}{\nu}
\left(\frac{1-\nu}{1-z_M^*}\right)^\gamma\right]^{-1/\gamma},
\]
\[
\mu_M(\lambda)=
\left(\frac{e\nu^{M-2}(1-\nu)^\gamma}
{\lambda^{-\gamma}-\varepsilon_M}\right)^{1/(1-\gamma)}.
\]
For all sufficiently large \(M\), \(\nu^{1/\gamma}<\lambda_M^*<1\), and the attracting interval is **exactly**
\[
\boxed{\quad \mu_M(\lambda_M^*)<\mu<\mu_M(1)\quad}
\]
within the class of primitive \(M\)-cycles with one nonlinear iterate and \(M-1\) linear iterates. Its unique cycle has multiplier \(-1\) at the lower boundary (where the cycle is still regular), is attracting throughout this open interval, and is repelling on the continuation of the same itinerary immediately below the lower boundary. The upper boundary is a grazing/contact endpoint; its inclusion in this claim is not asserted.

The thresholds have the sharp large-period laws
\[
\boxed{\lambda_M^*=1-4\nu^{M+1}+O(\nu^{2M})},
\qquad
\boxed{\frac{\mu_M(1)-\mu_M(\lambda_M^*)}{\mu_M(1)}
=\frac{4\gamma\nu}{1-\gamma}\nu^M+O(\nu^{2M})}.
\]
In addition, the multiplier crossing at the lower boundary is a **nondegenerate subcritical flip** for all sufficiently large \(M\): for each such fixed \(M\), immediately inside the attracting interval there is a nearby **repelling primitive period-\(2M\) orbit** whose two nonlinear visits alternate between two points of the same return branch. No uniform size for the smaller local period-\(2M\) coexistence interval is claimed.

## Assumptions and scope
All quantities above are real. The exponent is the rational number \(\gamma=q/p\) with \(0<q<p\), \(\gcd(p,q)=1\); the coefficient \(e>0\) is fixed; the slope is held at the excluded boundary \(\nu=p/(p+q)\). The map is considered on a real neighborhood containing the periodic cycles; the power is evaluated only for nonnegative \(\mu-x\). One cycle point satisfies \(\nu\mu<x_0<\mu\), while all other \(M-1\) points satisfy \(x_j>\mu\). The claim does not classify all other possible itineraries, invariant sets, or global basins.

The qualifier 'exactly' concerns the stability interval of this **unique one-nonlinear-step period-\(M\) word**, not global uniqueness of attracting cycles. Period-\(2M\) existence is local near the exact lower endpoint, not a claim over the entire attracting interval.

## Proof
**1. The exact return and its physical parameter.** Fix an integer \(M\geq2\), choose \(\lambda\in(\nu^{1/\gamma},1)\), and define \(\mu=\mu_M(\lambda)\). Write \(x_0=\mu z\) for \(z\in(\nu,1)\). The candidate itinerary uses the nonlinear map once and then its linear branch for \(M-1\) steps. The *exact* (not asymptotic) normalized return is
\[
P_{M,\lambda}(z)=\nu^M z+\nu^{M-1}e\mu^{\gamma-1}(1-z)^\gamma
=\varepsilon_M z+\nu(\lambda^{-\gamma}-\varepsilon_M)
\left(\frac{1-z}{1-\nu}\right)^\gamma.
\]
The last equality follows by substituting the defining formula for \(\mu_M(\lambda)\). At the two endpoints of the candidate section,
\[
P_{M,\lambda}(\nu)=\nu\lambda^{-\gamma}\in(\nu,1),
\qquad P_{M,\lambda}(1)=\varepsilon_M<1.
\]
Furthermore, \(P_{M,\lambda}'(z)<\varepsilon_M<1\), so \(P_{M,\lambda}(z)-z\) decreases strictly and has exactly one zero \(z(\lambda)\in(\nu,1)\). Let \(x_0=\mu z(\lambda)\). The candidate orbit satisfies \(x_M=x_0\). For \(1\leq j\leq M-1\), the proposed intermediate values are
\[
x_j=\mu z(\lambda)\nu^{j-M}.
\]
These are all strictly greater than \(\mu\), since \(z(\lambda)>\nu\) and \(j\leq M-1\). They therefore really do follow the linear branch. Exactly one step per \(M\) is nonlinear. This proves the itinerary is self-consistent, and it is primitive: a proper divisor of \(M\) would have a nonintegral number of nonlinear-branch visits per period.

**2. Exact multiplier and threshold.** At the fixed point, the return identity eliminates the power coefficient in the derivative:
\[
\rho_M(\lambda)
=P_{M,\lambda}'(z(\lambda))
=\varepsilon_M-\gamma(1-\varepsilon_M)
\frac{z(\lambda)}{1-z(\lambda)}.
\]
As \(\lambda\) decreases, the return map increases pointwise and its unique fixed point moves strictly upward. Consequently \(\rho_M\) decreases strictly. At \(\lambda\uparrow1\) the fixed point tends to \(\nu\), where
\(\rho_M=2\varepsilon_M-1\in(-1,1)\). Solving \(\rho_M=-1\) yields exactly \(z_M^*\) above, and substitution in the fixed-point equation yields \(\lambda_M^*\). Since \(\lambda_M^*\to1\) whereas \(\nu^{1/\gamma}<1\) is fixed, this threshold belongs to the admissible parameter interval for every sufficiently large \(M\). All multiplier inequalities now follow from strict monotonicity. The physical multiplier of the original primitive \(M\)-cycle equals that of \(P_{M,\lambda}\), because the rescaling \(x=\mu z\) is affine and all intermediate branches are differentiable on the orbit.

**3. Widths, accumulation, and separation.** Put \(\varepsilon=\varepsilon_M\) and \(z^*=z_M^*\). Direct Taylor expansion of the exact threshold equation at \(\varepsilon=0\) gives
\[
(\lambda_M^*)^{-\gamma}=1+4\gamma\nu\varepsilon+O(\varepsilon^2),
\quad \lambda_M^*=1-4\nu\varepsilon+O(\varepsilon^2).
\]
The parameter-to-width identity is
\[
\frac{\mu_M(\lambda_M^*)}{\mu_M(1)}
=\left(\frac{1-\varepsilon_M}{(\lambda_M^*)^{-\gamma}-\varepsilon_M}\right)^{1/(1-\gamma)}.
\]
Expanding this identity proves the relative-width formula. Also
\[
\mu_M(1)\sim
\left(e(1-\nu)^\gamma\nu^{-2}\right)^{1/(1-\gamma)}
\nu^{M/(1-\gamma)},
\]
so consecutive outer endpoints have asymptotic ratio \(\nu^{1/(1-\gamma)}<1\), whereas each interval has relative width tending to zero. All sufficiently late intervals are disjoint and converge to \(0\).

**4. Local flip and its criticality.** At \(\lambda_M^*\) the return fixed point is interior to \((\nu,1)\), its multiplier is exactly \(-1\), and the multiplier has nonzero parameter derivative. Indeed, differentiating the fixed-point equation gives \(z'(\lambda)=\partial_{\lambda}P/(1-\partial_zP)<0\), because \(\partial_{\lambda}P=-\gamma\nu\lambda^{-\gamma-1}((1-z)/(1-\nu))^\gamma<0\). Consequently \(\rho_M'(\lambda)=-\gamma(1-\varepsilon_M)z'(\lambda)/(1-z)^2>0\). The return map is smooth in a neighborhood of that point. When \(M\to\infty\), its derivatives through order three there converge to those of the root-power map \(G(z)=\nu((1-z)/(1-\nu))^\gamma\) at \(z=\nu\). Its Schwarzian derivative is
\[
S(G)(\nu)=\frac{1-\gamma^2}{2(1-\nu)^2}>0.
\]
In fact, direct differentiation gives its exact finite-return Schwarzian at the flip:
\[
S(P_{M,\lambda_M^*})(z_M^*)=\frac{(1-\gamma)(1+\varepsilon_M)\bigl(1+\gamma-3(1-\gamma)\varepsilon_M\bigr)}{2(1-z_M^*)^2}.
\]
It is strictly positive as soon as \(3(1-\gamma)\varepsilon_M<1+\gamma\), which holds for all sufficiently large \(M\). To see the direction without relying on a sign convention, write the centered return at a multiplier-\(-1\) point as \(P(u)=-u+a u^2+b u^3+O(u^4)\). Then
\[
P^2(u)-u=-2(a^2+b)u^3+O(u^4),
\qquad -6(a^2+b)=S(P)(0)>0.
\]
On the stable side the linear term of \(P^2(u)-u\) is negative and of first order in the parameter displacement, whereas the cubic coefficient is positive. The usual one-dimensional flip argument (or the implicit-function theorem after dividing by \(u\) and rescaling by the square root of parameter displacement) produces two additional nonzero roots of \(P^2(u)-u\) there; they have return-two multiplier greater than one. They form one repelling period-two orbit of \(P\). Because the point is interior for each fixed large \(M\), these small roots remain in its single itinerary branch for sufficiently small parameter displacement. They lift to one primitive repelling period-\(2M\) orbit of the original map.

## Verification
The accompanying standalone `verify.py` uses symbolic simplification for the multiplier and first-order boundary-layer coefficient and high-precision numerical verification for four rational exponents and four return times. It explicitly iterates the original map and checks the precise one-nonlinear-step itinerary, return equation, and stable/neutral/unstable multipliers. It also checks representative large-period width asymptotics. The program is supplementary evidence only; the formulas and sign arguments above prove the statements for all sufficiently large integers \(M\).

For illustration, when \(\gamma=1/2\), \(e=1\), and \(M=8\), the exact formulas yield \(\lambda_M^*\approx0.90529566016\) and the attracting physical-parameter interval is approximately \((0.002508615792,0.002781976969)\). This finite example is not a substitute for the all-period theorem.

## Relationship to prior work
Lima and Perdigão introduce the precise continuous power-law grazing map and give its exact finite-return expression (their equation (34)), but their bifurcation theorem treats the strict regimes on either side of \(\nu=p/(p+q)\). The limiting map \(G\) suppresses the order-\(\nu^M\) term. At the excluded equality, the suppressed term decides stability and generates the exponentially narrow attracting intervals proved here. In particular, the limiting flip parameter reaches the itinerary endpoint \(\lambda=1\), whereas the exact finite-return flip lies a positive distance of order \(\nu^M\) inside the admissible range. This is not an instance of the source's strict-inequality period-doubling theorem. The same authors' distinct grazing-return study concerns discontinuity mappings in hybrid flows, not this critical exact sequence of primitive-orbit windows. Earlier general border-collision and square-root-map references motivate the object but were not found to state the all-rational-power critical-slope threshold or its relative-width law.

## Limitations
The attracting result concerns a specific family of itineraries; neither an exhaustive global attractor classification nor uniqueness over other words is proved. The statement is asymptotic in period, with an unspecified finite \(M_0(\gamma)\). The endpoint \(\lambda=1\) is a grazing contact and is explicitly excluded. The repelling \(2M\)-cycle result is local near \(\lambda_M^*\), not uniform in \(M\). No inference about hybrid-flow impact dynamics beyond the stated return map is made. Publication-priority completeness cannot be established from indexed sources alone; the closest older book treatment was not independently available in complete mathematical text.

## References
1. M. F. S. Lima and T. R. Perdigão, *One-dimensional Piecewise Smooth Rational Degree Maps*, arXiv:2407.02782 (first posted July 3, 2024), https://arxiv.org/abs/2407.02782 . Especially equations (4), (34)–(41), Theorem 1 and the appendix.
2. M. F. S. Lima and T. R. Perdigão, *Zero Time Discontinuity Mapping (ZDM) and Poincaré Discontinuity Mapping (PDM) in a neighbourhood of a regular grazing point of order 4 in impacting hybrid systems*, arXiv:2407.02434 (first posted July 2, 2024), https://arxiv.org/abs/2407.02434 . Context only; its mathematical object is different.
3. M. di Bernardo, C. J. Budd, A. R. Champneys and P. Kowalczyk, *Piecewise-smooth Dynamical Systems: Theory and Applications*, Springer, 2008. Historical square-root grazing-map background, as cited by reference 1; complete text not independently examined.
