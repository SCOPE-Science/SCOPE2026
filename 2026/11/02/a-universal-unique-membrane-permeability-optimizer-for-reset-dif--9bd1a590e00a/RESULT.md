# A universal unique membrane-permeability optimizer for reset diffusion on a circle

## Finding

For Brownian diffusion with independent Poisson resetting on a circle interrupted by one symmetric semipermeable membrane, **the stationary interfacial entropy-production rate has exactly one maximizer as a function of membrane permeability**, for every reset law producing nonzero membrane current. The optimizer depends on the reset law only through one dimensionless asymmetry parameter, and its rescaled value lies in the sharp source-independent interval

\[
0.385933275998194\ldots < \kappa_*g < \frac12.
\]

This is a statement about the *interfacial contribution* to entropy production, not the total entropy production or a physical maximum-entropy-production principle.

**Exact theorem.** Fix \(D,L,r>0\) and an arbitrary Borel probability measure \(\mu\) on \((0,L)\). Write

\[
\lambda=\sqrt{r/D},\quad
 a=\frac{\lambda}{\sinh(\lambda L)}\int_{(0,L)}\cosh(\lambda(L-y))\,\mu(dy),\quad
 b=\frac{\lambda}{\sinh(\lambda L)}\int_{(0,L)}\cosh(\lambda y)\,\mu(dy),
\]
\[
 g=\frac{\tanh(\lambda L/2)}{D\lambda},\qquad
 s=a+b,\qquad h=\frac{|a-b|}{a+b}.
\]

Then \(g>0\), \(s>0\), and \(0\le h<1\). If \(h=0\), interfacial entropy production vanishes for every permeability. If \(h>0\), define \(u_h\in(0,1)\) as the unique root of

\[
\operatorname{artanh}(hu_h)
=\frac{h(1-u_h)}{1-h^2u_h^2}.
\]

The unique maximizing permeability is

\[
\boxed{\kappa_* = \frac{1-u_h}{2g u_h}}.
\]

Moreover \(u_h\) increases strictly with \(h\), so the scaled optimum \(\kappa_*g\) decreases strictly with \(h\), from the limiting value \(1/2\) as \(h\downarrow0\) to

\[
\frac{1-u_\infty}{2u_\infty}=0.385933275998194\ldots
\]

as \(h\uparrow1\), where \(u_\infty\in(0,1)\) is the unique solution of \(\operatorname{artanh}(u_\infty)=1/(1+u_\infty)\), numerically \(u_\infty=0.564376588560399\ldots\). Both bounds are sharp across admissible physical parameters and source laws. For weak source asymmetry,

\[
\kappa_*g=\frac12-\frac{h^2}{12}+O(h^4).
\]

## Assumptions and scope

Map the ring to the open interval \((0,L)\) with the membrane joining \(0^+\) and \(L^-\). The diffusion coefficient is spatially constant \(D>0\), resets occur independently at rate \(r>0\), and every reset selects a new position with the fixed, permeability-independent Borel law \(\mu\). The membrane permeability \(\kappa>0\) is symmetric, with the precise convention

\[
D p_\kappa''-r p_\kappa=-r\mu,\qquad
-Dp_\kappa'(0^+)=-Dp_\kappa'(L^-)=J_\kappa
=\kappa[p_\kappa(L^-)-p_\kappa(0^+)].
\]

The differential equation holds distributionally if \(\mu\) has atoms. The stationary density is normalized to one, and the membrane's average stationary entropy-production rate is

\[
\mathcal I_\mu(\kappa)=J_\kappa\log\frac{p_\kappa(L^-)}{p_\kappa(0^+)}.
\]

This is the symmetric-interface convention of Bressloff, *Physical Review Research* **6**, 023283 (2024), equations (4.1), (4.5), (4.13) and (4.20). It includes atomic, mixed and continuous reset distributions.

## Proof

**1. Exact source reduction.** The Neumann (perfectly reflecting) stationary resolvent has density

\[
p_N(x)=\frac{\lambda}{\sinh(\lambda L)}
\int\cosh(\lambda\min\{x,y\})\,
\cosh(\lambda[L-\max\{x,y\}])\,\mu(dy).
\]

It satisfies \(Dp_N''-rp_N=-r\mu\), \(p_N'(0)=p_N'(L)=0\), and \(\int_0^L p_N(x)\,dx=1\). Its boundary densities are exactly \(a=p_N(0)\) and \(b=p_N(L)\). Every stationary solution with a prescribed common boundary flux \(J\) is

\[
p_J(x)=p_N(x)+\frac{J}{D\lambda}\,
\frac{\sinh[\lambda(L/2-x)]}{\cosh(\lambda L/2)}.
\]

The additive term has zero integral, satisfies the homogeneous ODE, and gives derivatives \(-Dp_J'(0)=-Dp_J'(L)=J\). In particular, \(p_J(0)=a+gJ\) and \(p_J(L)=b-gJ\). The membrane law therefore imposes

\[
J_\kappa=\frac{\kappa(b-a)}{1+2\kappa g},\quad
p_\kappa(0)=\frac{a+\kappa g(a+b)}{1+2\kappa g},\quad
p_\kappa(L)=\frac{b+\kappa g(a+b)}{1+2\kappa g}.
\]

The denominator is positive; these formulas give the unique normalized stationary resolvent. Since \(a,b>0\), its boundary densities are positive.

**2. Exact entropy curve.** Put \(q=2\kappa g\) and \(u=(1+q)^{-1}\). Then

\[
\left|J_\kappa\right|=\frac{sh}{2g}(1-u),\qquad
\left|\log\frac{p_\kappa(L)}{p_\kappa(0)}\right|
=2\operatorname{artanh}(hu).
\]

The signs of the flux and logarithm agree, giving the complete nonnegative entropy curve

\[
\boxed{\mathcal I_\mu(\kappa)=\frac{sh}{g}
(1-u)\operatorname{artanh}(hu),\qquad
u=(1+2\kappa g)^{-1}.}
\]

If \(h=0\), this expression is zero. For \(h>0\), it is positive at every finite \(\kappa>0\) and tends to zero at both \(\kappa\downarrow0\) and \(\kappa\to\infty\).

**3. Unique global optimum.** Differentiating with respect to \(u\) gives a positive factor \(sh/g\) times

\[
F_h(u)=\frac{h(1-u)}{1-h^2u^2}-\operatorname{artanh}(hu).
\]

Now \(F_h(0)=h>0\), \(F_h(1)=-\operatorname{artanh}(h)<0\), and

\[
\frac{dF_h}{du}=-\frac{2h(1-h^2u)}{(1-h^2u^2)^2}<0
\quad(0<u<1,\ 0<h<1).
\]

Thus it has exactly one root \(u_h\), where the entropy curve has its sole strict global maximum. The map \(u=(1+2\kappa g)^{-1}\) is a bijection from positive permeabilities to \((0,1)\), proving the formula for \(\kappa_*\).

**4. Universal sharp band and strict source-asymmetry order.** A direct derivative gives

\[
\frac{\partial F_h}{\partial h}
=\frac{1-2u+h^2u^2}{(1-h^2u^2)^2}.
\]

At its root \(u=u_h\), the strict inequality \(\operatorname{artanh}(hu)>hu\) implies \(1-2u+h^2u^3>0\), hence \(\partial_hF_h(u_h)>0\). Since \(\partial_uF_h(u_h)<0\), implicit differentiation yields \(du_h/dh>0\). Dividing the root equation by \(h\) and taking \(h\downarrow0\) gives \(u_h\to1/2\); taking \(h\uparrow1\) gives the unique solution of \(\operatorname{artanh}(u)=1/(1+u)\). These limits yield the strict bound for \(\kappa_*g\). Expanding the root equation at small \(h\) gives \(u_h=1/2+h^2/24+O(h^4)\), and thus \(\kappa_*g=1/2-h^2/12+O(h^4)\).

Sharpness at \(h\downarrow0\) follows from noncentral point sources approaching the ring midpoint. For point resets at \(y\in(0,L/2)\),

\[
h=\tanh(\lambda L/2)\,\tanh[\lambda(L/2-y)].
\]

Taking \(\lambda L\to\infty\) with \(\lambda y\to0\) makes \(h\uparrow1\) and attains the lower bound as a limit. No finite admissible parameters attain either endpoint when \(h>0\).

## Verification

The standalone Python 3 file `verify.py` reconstructs the Neumann Green solution and the independent flux boundary conditions, integrates the stationary density to check normalization, checks the PDE away from atoms, numerically optimizes permeability against the analytic root over multiple atomic source distributions, and checks the universal constants and symmetric-source zero case. It uses only the Python standard library and reports **302 passed diagnostic assertions** on execution. The argument above supplies the global proof; numerical scans are not used to establish uniqueness or sharpness.

A reproducible numerical instance is \(D=L=1\), \(r=25\), and \(\mu=\delta_{1/4}\). It yields

\[
g=0.197322859630286\ldots,\quad h=0.836928768070022\ldots,\quad
\kappa_*=2.176222715530913\ldots,
\]

with maximal interfacial production \(\mathcal I_\mu(\kappa_*)=1.483291329181599\ldots\) in the source's normalization.

## Relationship to prior work

Bressloff (2024) derives the stationary boundary-value problem, the interfacial entropy formula, and demonstrates numerically that this entropy contribution is nonmonotone in permeability (his Fig. 8). The current result *does not* claim discovery of this qualitative nonmonotonicity or of the membrane Green function. It establishes the exact number of positive permeability optimizers, the complete arbitrary-reset-law classification, strict monotonic dependence on the source asymmetry, and source-independent sharp bounds on the scaled maximizer. Bressloff (2022/2023) treats diffusion and resetting screened by a semipermeable interface, with emphasis on first passage rather than this stationary entropy optimizer.

Existing results on inverse recovery of source asymmetry from membrane flux do not imply the unique nonlinear entropy optimizer or the sharp universal band without an additional global analysis of the logarithmic boundary ratio.

## Limitations

Only one symmetric membrane on a homogeneous one-dimensional circle is covered, with Poisson resetting to a fixed rate- and permeability-independent law. The result maximizes the interfacial term only; other sources of entropy production may be present. For an exactly balanced reset law at the selected rate, all permeabilities yield zero interfacial entropy, so there is **no unique optimum**. The conclusion does not cover biased membranes, nonlinear membrane laws, reset laws changing with permeability, or spatially varying diffusivity. Publication-priority assessment may be affected by broader scalar conductance/entropy-optimization results not located in the accessible literature; no independent scientific audit has been performed.

## References

1. P. C. Bressloff, "Entropy production for diffusion processes across a semipermeable interface," *Physical Review Research* **6**, 023283 (2024), DOI: 10.1103/PhysRevResearch.6.023283; arXiv:2402.16403 (first public version 2024-02-26), https://arxiv.org/abs/2402.16403 . Equations (4.1), (4.5), (4.13), (4.20) and Fig. 8.
2. P. C. Bressloff, "Diffusion with stochastic resetting screened by a semipermeable interface," *Journal of Physics A* **56**, 105001 (2023), arXiv:2211.12468, https://arxiv.org/abs/2211.12468 .
3. P. C. Bressloff, "Renewal equations for single-particle diffusion through a semipermeable interface," *Physical Review E* **107**, 014110 (2023), arXiv:2211.12460, https://arxiv.org/abs/2211.12460 .
