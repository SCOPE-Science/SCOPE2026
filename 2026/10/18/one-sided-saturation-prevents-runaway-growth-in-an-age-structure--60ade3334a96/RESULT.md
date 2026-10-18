# One-sided saturation prevents runaway growth in an age-structured role-reversal population model

## Finding

For a predator population governed by an age-structured renewal equation and a prey population that benefits from consuming juvenile predators but is consumed by adults, **saturation of the prey benefit alone implies a uniform absorbing bound**, even when the predator birth rate retains its original unbounded linear dependence on prey abundance. No condition comparing food-conversion efficiencies to predation rates is needed.

More precisely, for every solution in the assumptions below, write \(P(t)=\int_0^\infty u(t,z)\,dz\) and define
\[
 C=r+sh,\quad L=\frac{2C}{a},\quad K=k+\zeta\|\widetilde B\|_\infty,
 \quad m=\mu_M e^{-\rho L},\quad M=gL+\|\mu_B\|_\infty+\mu_M,
\]
\[
 c=\exp\bigl(-(M+KL)T\bigr),\qquad q=\frac{bc}{2K}.
\]
Assuming \(K>0\), all these relevant constants are positive and
\[
 \boxed{\limsup_{t\to\infty}P(t)\le\frac{(C+m)L}{mq}
 =\frac{2K(C+m)L}{mb}\,e^{(M+KL)T}.}
\]
Moreover \(\limsup_{t\to\infty}x(t)\le C/a\). Both ultimate bounds depend on the model parameters but not the initial masses. Every nonnegative finite-mass solution therefore exists globally and is ultimately bounded in \(\mathbb R_+\times L^1(0,\infty)\).

## Assumptions and scope

Let \(t\ge0\) denote time, \(z\ge0\) predator age, and \(T>0\) the age separating juveniles from adults. Let \(x(t)\) denote prey abundance and \(u(t,z)\ge0\) the predator age density. Set
\[
 y_1(t)=\int_0^T u(t,z)\,dz,\quad
 y_2(t)=\int_T^\infty u(t,z)\,dz,\quad P=y_1+y_2.
\]
The prey evolves by a **single-sided saturated** equation:
\[
 \dot x=x\Bigl(r-ax+sh\tanh\bigl(y_1/h\bigr)-by_2\Bigr).
\]
The predator equation retains **unsaturated fecundity**:
\[
 (\partial_t+\partial_z)u=-\mu(x,z)u,\qquad
 u(t,0)=\int_0^\infty B(x(t),z)u(t,z)\,dz,
\]
\[
 B(x,z)=kxA_\nu(z)+\widetilde B(z)(1-e^{-\zeta x}),
 \quad A_\nu(z)=\frac{1}{1+e^{-\nu(z-T)}},
\]
\[
 \mu(x,z)=gx(1-A_\nu(z))+\mu_B(z)+\mu_M e^{-\rho x}.
\]
Parameters \(r,a,s,h,b,T,\nu,\zeta,\rho,\mu_M\) are strictly positive; \(k,g\ge0\); \(\widetilde B:[0,\infty)\to[0,\infty)\) is bounded and continuous (and may be integrable); and \(\mu_B:[0,\infty)\to[0,\infty)\) is continuous and **uniformly bounded over all ages**. At least one of \(k\) and \(\widetilde B\) is nonzero, hence \(K>0\). Initial conditions are \(x(0)>0\) and a nonnegative bounded piecewise-smooth predator density with compact age support and finite total mass. The argument applies to classical/characteristic solutions and their nonnegative integral-solution continuations.

Uniform boundedness of age-specific baseline mortality is a substantive scope condition, stronger than mere boundedness on compact age intervals; it ensures a positive lower bound on the fraction of each cohort surviving a complete maturation interval. The claim imposes no numerical restriction on maturation time, recruitment slope, juvenile-prey benefit strength, or conversion ratios.

## Proof

**Step 1: uniform prey ceiling.** Since \(0\le\tanh(y_1/h)\le1\) and \(y_2\ge0\),
\[
 \dot x\le x(C-ax),\qquad C=r+sh.
\]
Logistic comparison, including arbitrarily large finite initial \(x(0)\), yields
\[
 x(t)\le\frac{C}{a(1-e^{-Ct})},\qquad t>0.
\]
In particular \(0<x(t)\le L=2C/a\) for all \(t\ge t_0=(\log 2)/C\), and \(\limsup x\le C/a\).

**Step 2: birth/death bounds.** The inequalities \(0\le A_\nu\le1\) and \(1-e^{-\zeta x}\le\zeta x\) give \(0\le B(x,z)\le Kx\). For \(t\ge t_0\), the characteristic mortality satisfies \(m\le\mu(x,z)\le M\), with the explicit \(m,M\) from the finding. Integrating the age-transport equation, including the renewal boundary term, gives for almost every \(t\ge t_0\)
\[
 P'=u(t,0)-\int_0^\infty\mu(x(t),z)u(t,z)\,dz
 \le(Kx-m)P\le KL P.
\]
Thus for \(t\ge t_0+T\),
\[
 P(t)\le e^{KLT}P(t-T).
\]

**Step 3: unavoidable adult fraction.** Every predator alive at time \(t-T\) is at least \(T\) old at time \(t\) if it survives. The characteristic survival factor over this interval is no smaller than \(e^{-MT}\). Births in the intervening interval only increase the adult mass, so
\[
 y_2(t)\ge e^{-MT}P(t-T)
 \ge e^{-(M+KL)T}P(t)=cP(t),\qquad t\ge t_0+T.
\]
This is the decisive cohort estimate. It does not require maturation to be instantaneous, a fixed adult-to-juvenile ratio at earlier times, or an upper bound on the numerical birth coefficient \(k\).

**Step 4: dissipativity from adult feedback.** Define \(q=bc/(2K)>0\) and \(V=x+qP\). For \(t\ge t_0+T\), combine the inequalities above:
\[
 \begin{aligned}
 V'&\le Cx-ax^2-bxy_2+q(Kx-m)P\\
 &\le Cx-ax^2-(bc-qK)xP-qmP\\
 &=Cx-ax^2-\frac{bc}{2}xP-qmP\\
 &\le (C+m)L-mV.
 \end{aligned}
\]
The final inequality follows from \(0\le x\le L\), since \((C+m)x-ax^2\le(C+m)L\). Scalar comparison yields
\[
 V(t)\le e^{-m(t-t_1)}V(t_1)
 +\frac{(C+m)L}{m}\bigl(1-e^{-m(t-t_1)}\bigr),
 \quad t\ge t_1=t_0+T.
\]
Consequently \(\limsup V\le(C+m)L/m\), and \(P\le V/q\) gives the boxed upper bound.

**Step 5: global extension.** On \([0,t_1]\), the logistic comparison keeps prey finite and \(P'\le KxP\) supplies a finite Gronwall bound for the predator mass. The same bounds and the renewal characteristic formula control the birth flux \(u(t,0)\le KxP\) on each finite interval. Standard local continuation for this semilinear renewal/ODE problem therefore cannot terminate at finite time. This proves global nonnegative solvability and the asserted absorbing estimate, including initial data with \(P(0)=0\), for which \(P\equiv0\).

## Verification

The standalone `verify.py` checks \(2499\) exact rational instances of the mixed-term cancellation and Lyapunov inequality and \(2400\) additional parameterized bounds on prey growth, predator recruitment, mortality, and the aggregate dissipation estimate. It requires only Python 3 and runs as `python verify.py`. These checks are supporting finite diagnostics; the proof above supplies the global all-parameter conclusion. The checks do not establish a sharp optimal absorbing radius.

## Relationship to prior work

Suarez, Cameron, Fagan, and Levy introduce the full age-structured role-reversal model, prove its local solvability, investigate large-growth numerical trajectories, and propose saturating **both** the juvenile benefit in the prey equation and the prey-dependent predator recruitment. Their published model (42) motivates the prey-side term considered here, while their proposed modification (43) saturates the predator fecundity. The present theorem instead leaves the original \(kxA_\nu(z)\) fecundity term unbounded as \(x\to\infty\), and supplies a quantitative parameter-uniform-in-initial-mass bound from the delayed adult-coercivity estimate. The source's general existence results and numerical phase diagrams do not themselves imply this one-sided-cap result.

Cai, Li, Song, and Yu study boundedness and stability in a different age-structured prey–predator model with delays; their mechanisms include different density regulation and stage placement. Their result is relevant background for dissipativity, but does not directly establish the above surviving-cohort inequality for the present predator-age renewal system. General dissipativity principles remain relevant and unindexed specialized coverage cannot be excluded solely by search.

## Limitations

The new bound assumes globally bounded age-specific background mortality, positive baseline starvation mortality, bounded age-dependent recruitment shape, and positive adult predation coupling. It covers the continuous untruncated age domain, not an artificial finite-age numerical cutoff. It does not prove persistence of both species, uniqueness of equilibria, stability of periodic orbits, or mathematical blowup of the fully unsaturated original model. The explicit constants can be extremely conservative when maturation is slow, mortality high, or fecundity large. Finite computational checks are not replacements for the characteristic and comparison inequalities.

## References

1. L. C. Suarez, M. K. Cameron, W. F. Fagan, D. Levy, *A predator-prey model with age-structured role reversal*, arXiv:2502.19748v1 (first public 2025-02-27); *Journal of Mathematical Biology* 92, 73 (2026), DOI: 10.1007/s00285-026-02402-5. Original model and discussion of saturation in Sections 2 and 7.
2. L. Cai, X. Li, X. Song, J. Yu, *Permanence and Stability of an Age-Structured Prey-Predator System with Delays*, *Discrete Dynamics in Nature and Society* 2007, Article 54861, DOI: 10.1155/2007/54861.
