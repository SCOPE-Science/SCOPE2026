# Exact period and the saddle-node threshold for periodic Liénard blow-up profiles

## Finding
Let \(n\ge2\) be even and \(\kappa\in\mathbb R\) satisfy \(|\kappa|<2\sqrt{n+1}\). Consider the polynomial balance system
\[
\dot u=-\frac un-v,\qquad
\dot v=-\frac{n+1}{n}v+u^{2n+1}+\kappa u^n v.
\]
If \(0<\kappa<2\sqrt{n+1}\), the nonzero plane contains **exactly one periodic orbit**, understood as a geometric orbit rather than as a parametrized solution. Its minimal time period is the explicit absolutely convergent integral
\[
T_{n,\kappa}=\frac{4n\kappa}{(n+1)^{3/2}}
\int_0^1\frac{\sqrt{1-t^2}}{1-\frac{\kappa^2}{n+1}t^2(1-t^2)}\,dt.
\]
Its nontrivial Floquet multiplier is \(e^{T_{n,\kappa}}>1\). The Floquet identity was already noted for the motivating system in the source and is recalled here, not claimed as a new discovery. For \(-2\sqrt{n+1}<\kappa\le0\), there are **no nonconstant periodic orbits**. As \(\kappa\downarrow0\),
\[
T_{n,\kappa}=\frac{n\pi}{(n+1)^{3/2}}\kappa
\left(1+\frac{\kappa^2}{8(n+1)}+O(\kappa^4)\right).
\]
As \(\kappa\uparrow\kappa_c:=2\sqrt{n+1}\) from below,
\[
T_{n,\kappa}\sim\frac{2\pi n}{n+1}
\left(1-\frac{\kappa^2}{4(n+1)}\right)^{-1/2}.
\]
The critical value is the first positive coefficient for which the balance system develops nonzero equilibria. All claims about cycles and the integral apply only to the open coefficient range above; no classification of cycles at or beyond the critical point is asserted.

## Assumptions and scope
A dot denotes derivative with respect to the balance-law time \(\eta\). The parameter \(n\) is an arbitrary even integer \(\ge2\); the coefficient of \(u^{2n+1}\) is normalized to one and the coefficient of \(u^nv\) is the independently variable \(\kappa\). At \(\kappa=1\) these are exactly the two-dimensional balance equations (5.5) of Matsue, arXiv:2610.05354v1. The theorem concerns the planar balance system and does not by itself prove any additional blow-up solutions for other, lower-order perturbed original equations.

## Proof
**1. Canonical nonlinear angular coordinate.** Define \(C(s),S(s)\) by
\[
C'=-S,\quad S'=C^{2n+1},\quad C(0)=1,\quad S(0)=0.
\]
Their conserved energy gives \(C^{2n+2}+(n+1)S^2=1\). They traverse the entire smooth weighted unit oval once in their minimal positive period
\[
P_n=\frac2{\sqrt{n+1}}B\!\left(\frac1{2n+2},\frac12\right),
\]
where \(B\) is Euler's beta function. The uniqueness and regularity of ODE solutions and nonvanishing tangent vector prove this parametrizes the oval without repetition. Every \((u,v)\ne(0,0)\) therefore has a unique weighted radius \(R>0\) and phase \(s\) modulo \(P_n\) such that \(u=RC(s)\) and \(v=R^{n+1}S(s)\).

**2. Exact radial and angular equations.** Directly substitute these expressions and solve the resulting two-by-two linear system for the radial and angular derivatives. Using the oval identity yields
\[
\frac{\dot R}{R}=-\frac1n+\kappa R^n C^nS^2,\qquad
\dot s=R^n b_\kappa(s),\quad b_\kappa(s)=1+\kappa C^{n+1}(s)S(s).
\]
The sharp inequality \(|C^{n+1}S|\le1/(2\sqrt{n+1})\) follows by completing the square in \(C^{2n+2}+(n+1)S^2=1\). Hence \(b_\kappa>0\) throughout \(|\kappa|<\kappa_c\). In particular, every nonzero orbit crosses each angular phase in positive order and has a periodic trajectory precisely when its radius returns after one traversal (or multiple traversals).

**3. An affine scalar phase equation.** Put \(z=R^n>0\). Division by \(\dot s\) gives the *linear* differential equation
\[
\frac{dz}{ds}=a_\kappa(s)z-d_\kappa(s),\qquad
 a_\kappa(s)=\frac{n\kappa C^nS^2}{b_\kappa(s)},\quad
 d_\kappa(s)=\frac1{b_\kappa(s)}>0.
\]
Write \(\Lambda_\kappa=\int_0^{P_n}a_\kappa(s)\,ds\). Since \(n\) is even, \(C^nS^2\ge0\), not identically zero, so \(\operatorname{sgn}\Lambda_\kappa=\operatorname{sgn}\kappa\). For \(\kappa\ne0\) the affine return map on \(z\) has slope \(e^{\Lambda_\kappa}\) and precisely one fixed point. It is characterized for every phase \(s\) by
\[
z_\kappa(s)=\frac{\displaystyle\int_s^{s+P_n}
\exp\!\left(-\int_s^v a_\kappa(w)\,dw\right)d_\kappa(v)\,dv}
{1-e^{-\Lambda_\kappa}}.
\]
The numerator is positive. Thus the fixed radius is positive exactly for \(\kappa>0\); for \(\kappa<0\) it is negative and inadmissible, while for \(\kappa=0\) the return is a strict translation \(z\mapsto z-P_n\). The affine return map has no additional periodic points, so even traversals of multiple ovals cannot generate distinct cycles. The one positive cycle for \(\kappa>0\) has one angular revolution and is radially repelling. Its transverse multiplier equals \(e^{\Lambda_\kappa}\).

**4. Exact period, and normalization.** The balance-law time period is \(T=\int_0^{P_n}[z_\kappa(s)b_\kappa(s)]^{-1}ds\). On the positive periodic solution integrate \(d\log z_\kappa/ds=a_\kappa-d_\kappa/z_\kappa\) through one period to obtain the *exact identity* \(T=\Lambda_\kappa\). Pair the four conservative-oscillator quadrants. The sign of \(C^{n+1}S\) changes across paired quadrants, while \(C^nS^2\) does not. With \(t=|C|^{n+1}\), this gives
\[
\Lambda_\kappa=\frac{4n\kappa}{(n+1)^{3/2}}
\int_0^1\frac{\sqrt{1-t^2}}{1-\frac{\kappa^2}{n+1}t^2(1-t^2)}dt.
\]
It is positive and finite throughout the stated open interval. The cited source's numerical value \(T_{2,1}=1.262967766799167\) agrees with the quadrature's \(1.2629677667993\ldots\), but only the latter formula and its consequences are asserted as new here.

**5. Sharp limiting regimes and equilibrium boundary.** Uniformly expand the denominator at \(\kappa=0\). Elementary beta integrals give \(\int_0^1\sqrt{1-t^2}\,dt=\pi/4\) and \(\int_0^1t^2(1-t^2)^{3/2}\,dt=\pi/32\), yielding the small-coefficient expansion. At the critical endpoint put \(\delta=1-\kappa^2/[4(n+1)]\) and \(t_0=1/\sqrt2\). The denominator equals \(\delta+[\kappa^2/(n+1)](t^2-1/2)^2\); locally it is \(\delta+8(t-t_0)^2+o(\delta+(t-t_0)^2)\). The numerator tends to \(1/\sqrt2\). Rescaling \(t-t_0=\sqrt\delta\,q\) and dominating the far region gives the stated \(\delta^{-1/2}\) singularity and coefficient. Finally, at nonzero equilibria \(v=-u/n\), the equation reduces to \(n^2(u^n)^2-n\kappa u^n+(n+1)=0\). Since \(n\) is even, positive solutions for \(u^n\) are first possible at \(\kappa=2\sqrt{n+1}\). This proves the asserted collision threshold without extrapolating the cycle theorem outside its valid interval.

## Verification
The attached standalone standard-library program `verify.py` checks two separately transformed numerical quadratures, the quasi-polar vector-field identities at multiple radii and phases, the sign condition, the leading small-coefficient limit, and agreement with the previously published special-case period. Run `python3 verify.py`; successful output begins `VERIFY_OK:`. Its finite floating-point checks are consistency evidence; the statements for all even orders and continuous parameters depend on the exact proof above.

## Relationship to prior work
Matsue, arXiv:2610.05354v1, Sec. 5.2, especially equations (5.3)–(5.5), Observation 5.4, and Table 3, provides the \(\kappa=1\) equation, reports a numerically obtained period for \(n=2\), and already observes the identity between the nontrivial Floquet multiplier and \(e^T\). The same paper cites Dumortier and Herssens (1999) for quasi-polar geometry and a periodic orbit at infinity. Consequently neither the basic oscillator, the conservative oval, nor generic horizon existence or the Floquet identity is presented here as a novelty. The additional claim is the parameter-resolved **closed period integral**, sharp signed-coefficient existence classification, unique positive affine return profile, and precise singular behavior at the first nonzero-equilibrium threshold. Qualitative prior uniqueness and infinity results alone do not state those quantities. Earlier equivalent quantitative formulae in the 1999 paper or related Liénard literature remain a genuine priority risk because its full text was not available for examination.

## Limitations
All formulas are for the explicitly normalized balance equation, even \(n\), and \(|\kappa|<2\sqrt{n+1}\). The singularity at the positive threshold is a one-sided asymptotic, not a claim about an orbit at the endpoint. Nothing is asserted about limit cycles when \(|\kappa|\ge2\sqrt{n+1}\), the dynamics of associated full Liénard equations with lower-order terms, or independently certified publication priority. Finite numerical checks are not a substitute for the analytic proof, and independent scientific auditing has not been performed.

## References
1. K. Matsue, *On Algebraic-Dynamical Correspondence of Oscillatory Blow-Up Solutions for ODEs*, arXiv:2610.05354v1 (first submitted 2026-10-04), especially §5.2 and Table 3. https://arxiv.org/abs/2610.05354
2. F. Dumortier and C. Herssens, *Polynomial Liénard equations near infinity*, Journal of Differential Equations 153 (1999), 1–29. DOI:10.1006/jdeq.1998.3543. Full text not examined; possible quantitative priority overlap remains unresolved.
