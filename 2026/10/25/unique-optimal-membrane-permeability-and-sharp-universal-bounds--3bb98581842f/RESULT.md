# Unique optimal membrane permeability and sharp universal bounds for resetting diffusion on a ring

## Finding
Fix a ring of circumference \(L>0\), diffusion coefficient \(D>0\), reset rate \(r>0\), and an arbitrary reset-position probability measure \(\mu\) on \((0,L)\). Cut the ring at a symmetric permeable interface and write its transmission condition as \(J=\kappa[p(L)-p(0)]\), with \(\kappa>0\). Define
\[
a=\sqrt{r/D},\qquad b=\frac{2\tanh(aL/2)}{Da},\qquad
U=\frac{a}{\sinh(aL)}\int\cosh(a(L-y))\,\mu(dy),\quad
V=\frac{a}{\sinh(aL)}\int\cosh(ay)\,\mu(dy),
\]
and set \(S=U+V\), \(\delta=U-V\), and \(t=|\delta|/S\). Thus \(0\le t<1\).

The stationary **interfacial** entropy-production contribution (not the whole entropy production of the resetting mechanism) is exactly
\[
\mathcal I(\kappa)=\frac{2|\delta|}{b}(1-z)\operatorname{artanh}(tz),
\qquad z=(1+b\kappa)^{-1}.
\]
If \(\delta=0\), this contribution vanishes identically for all permeabilities. If \(\delta\ne0\), there is exactly **one** globally maximizing finite positive permeability \(\kappa_*\), given by
\[
\operatorname{artanh}(tz_*)=\frac{t(1-z_*)}{1-t^2z_*^2},\quad
\tfrac12<z_*<s,\quad
\kappa_* =\frac{1-z_*}{bz_*},
\]
where \(s=0.564376588560399\ldots\) is the unique solution in \((1/2,1)\) of \(\operatorname{artanh}s=(1+s)^{-1}\). Consequently the following universal, sharp, strict bounds hold:
\[
0.771866551996389\ldots=\frac{1-s}{s}
<b\kappa_*<1.
\]
The optimizer's reciprocal-transmission coordinate \(z_*\) grows strictly with contrast \(t\); equivalently, \(b\kappa_*\) strictly decreases with contrast. As \(t\downarrow0\) through nonzero contrasts,
\[
z_*=\tfrac12+\tfrac1{24}t^2+O(t^4).
\]
Neither strict bound can be improved uniformly over the stated physical family.

For a single reset site \(y\in(0,L)\setminus\{L/2\}\),
\[
t=\tanh(aL/2)\bigl|\tanh(a(L/2-y))\bigr|,
\]
so the dimensionless optimum \(b\kappa_*\) decreases strictly as the reset site moves away from the midpoint. Keeping \(D,L,y\) fixed, the optimal physical permeability satisfies the two sharp resetting-rate laws
\[
\kappa_*(r)=\frac DL+\frac{rL}{12}+O(r^2)\quad(r\downarrow0),
\qquad
\frac{\kappa_*(r)}{\sqrt{Dr}}\longrightarrow\frac{1-s}{2s}=0.385933275998194\ldots\quad(r\to\infty).
\]
For every fixed permeability, the interfacial entropy is no greater for any reset-position distribution than its limiting value for deterministic resets arbitrarily close to either side of the interface. More precisely, for \(\mu\) supported on the open interval the upper envelope is a supremum, not necessarily attained.

## Assumptions and scope
The particle follows drift-free Brownian diffusion in the interior \((0,L)\), with instantaneous Poisson resetting at rate \(r\) to independent samples from the *fixed* law \(\mu\), irrespective of the side of the permeable interface. The stationary density solves, distributionally,
\[
Dp''-rp=-r\mu,
\qquad -Dp'(0)=-Dp'(L)=J=\kappa[p(L)-p(0)].
\]
The membrane law \(J=\kappa[p(L)-p(0)]\) fixes our permeability convention; in formulations placing a factor of one-half in front of an intrinsic permeability, \(\kappa\) denotes that factor-adjusted coefficient. Every optimization and limit concerns the **interfacial** entropy term \(J\log[p(L)/p(0)]\). Resetting may contribute separate terms to total entropy production, and point-reset laws need not have a finite resetting-entropy term.

The optimizing contrast is nontrivial precisely when \(U\ne V\). The case of any symmetric or otherwise boundary-balanced reset distribution giving \(U=V\) is excluded from uniqueness claims. For point resets, the limiting rate statements exclude the midpoint, where the interfacial contribution is identically zero.

## Proof
**1. Baseline and boundary flux.** The Neumann Green kernel for \(r-D\partial_x^2\), multiplied by reset rate \(r\), is
\[
G_N(x,y)=\frac{a}{\sinh(aL)}
\cosh(a\min(x,y))\cosh\bigl(a[L-\max(x,y)]\bigr).
\]
Thus \(p_N(x)=\int G_N(x,y)\mu(dy)\) satisfies the stationary interior equation, has zero endpoint derivatives, integrates to one, and has strictly positive endpoint values \(U,V\). Set
\[
h(x)=-\frac{\sinh(a(x-L/2))}{Da\cosh(aL/2)}.
\]
It solves \(h''=a^2h\), \(h'(0)=h'(L)=-1/D\), \(h(0)=b/2\), \(h(L)=-b/2\), and \(\int_0^Lh(x)dx=0\). Hence \(p=p_N+Jh\) is the uniquely normalized stationary solution with prescribed boundary current \(J\). The interface law gives
\[
J=-\frac{\kappa\delta}{1+b\kappa},\qquad
p(0)=\frac{S+z\delta}{2},\qquad
p(L)=\frac{S-z\delta}{2},\qquad z=(1+b\kappa)^{-1}.
\]
These formulas give strictly positive endpoint densities and the displayed entropy-production identity by using \(\log[(1+u)/(1-u)]=2\operatorname{artanh}u\). Standard positivity and the positive reset rate ensure uniqueness of the stationary solution; the explicitly constructed solution has unit mass.

**2. Sharp optimizer.** For nonzero contrast, maximizing \(\mathcal I\) reduces to maximizing \(F_t(z)=(1-z)\operatorname{artanh}(tz)\) on \([0,1]\). Its second derivative is
\[
F_t''(z)=-\frac{2t(1-t^2z)}{(1-t^2z^2)^2}<0\quad(0<z<1),
\]
and \(F_t(0)=F_t(1)=0\), while \(F_t(z)>0\) in between. Strict concavity gives a unique interior optimum. Setting its derivative to zero gives the stated equation. At \(z=1/2\), positivity follows from the strict inequality \(\operatorname{artanh}u<u/(1-u^2)\) for \(0<u<1\). At fixed \(z\in(0,1)\) define
\[
g(z,t)=\operatorname{artanh}(tz)-\frac{t(1-z)}{1-t^2z^2}.
\]
At the optimizer, \(g=0\) and
\[
g_z=\frac{2t(1-t^2z)}{(1-t^2z^2)^2}>0,\qquad
g_t=\frac{2z-1-t^2z^2}{(1-t^2z^2)^2}<0.
\]
For the last inequality use the root equation and \(\operatorname{artanh}(tz)>tz\), which imply \(1-z>z(1-t^2z^2)\), so \(2z-1<t^2z^3<t^2z^2\). Implicit differentiation now yields \(dz_*/dt=-g_t/g_z>0\). The optimizer therefore increases from \(1/2\) as \(t\downarrow0\) to the unique root \(s\) of \(\operatorname{artanh}s=(1+s)^{-1}\) as \(t\uparrow1\). Its expansions follow from the implicit equation; in particular \(z_*=1/2+t^2/24+O(t^4)\). Substitution into \(b\kappa_*=(1-z_*)/z_*\) proves the sharp bounds.

**3. Dependence on reset locations and reset frequency.** For a point source \(\mu=\delta_y\), hyperbolic addition identities give
\[
S=\frac{a\cosh(a(L/2-y))}{\sinh(aL/2)},\qquad
\delta=\frac{a\sinh(a(L/2-y))}{\cosh(aL/2)}.
\]
Consequently \(t\) has the displayed form. It increases strictly with \(|y-L/2|\), and the optimizer conclusion follows from step 2. For fixed off-center \(y\), as \(r\downarrow0\) one has \(t=O(r)\) and
\[
b=\frac LD-\frac{rL^3}{12D^2}+O(r^2),\qquad
\frac{1-z_*}{z_*}=1+O(r^2).
\]
Multiplication yields \(\kappa_*=D/L+rL/12+O(r^2)\). As \(r\to\infty\), \(t\to1\) and \(b\sqrt{Dr}\to2\), yielding the claimed large-rate limit. Source families with \(t\downarrow0\) and fixed off-center sources with \(r\to\infty\), respectively, approach both universal bounds, establishing sharpness.

**4. Extremal reset-position bound.** For fixed \(\kappa\), the boundary values \(p(0),p(L)\) depend linearly on \(\mu\). The functional \((u-v)\log(u/v)\) is jointly convex for \(u,v>0\): it is the sum of the two jointly convex relative-entropy perspectives \(u\log(u/v)\) and \(v\log(v/u)\). Jensen's inequality therefore gives \(\mathcal I_\mu(\kappa)\le\int\mathcal I_{\delta_y}(\kappa)\,\mu(dy)\). The point-source formulas show both \(|\delta_y|\) and \(t_y\) increase strictly with \(|y-L/2|\), and \(\mathcal I_{\delta_y}(\kappa)=2|\delta_y|(1-z)\operatorname{artanh}(t_yz)/b\). This increases toward either endpoint; their limiting values agree by reflection. Taking the supremum gives the stated distribution-independent envelope.

## Verification
Run `python verify_membrane.py` with Python 3, NumPy and SciPy. The script independently reconstructs the piecewise stationary boundary-value problem (110 deterministic parameter cases), verifies 70 three-point mixtures by superposition, compares the analytical and directly optimized permeability for ten contrasts, checks monotonicity and two asymptotic regimes, and tests the extremal-source inequality. The script passed these tests. Finite numerical checks are supplementary and do not certify all real parameter values; the preceding analytic steps carry the theorem.

## Relationship to prior work
Bressloff (2024) introduced the interfacial entropy expression and analyzed diffusion with resetting across a permeable cut of a circle, supplying stationary formulas and numerical nonmonotonicity plots, including arbitrary-reset-distribution superposition. These formulas and the qualitative existence of a nonmonotone permeability dependence are prior work, not claimed as discoveries here. The present result is the strict **global uniqueness** classification (including the exact zero-contrast exception), an all-distributions scalar optimizer, sharp universal normalized permeability bounds and their sharpness, monotone source-contrast dependence, small- and large-reset-rate laws, and a location-independent extremal-source entropy envelope. The result is a mathematically explicit implication of the existing stationary equations, not a new stochastic dynamics model.

Related treatments of semipermeable crossings and resetting were consulted for alternative interface and first-passage formulations. In particular, optimization of *resetting rate* for absorption times behind a membrane is a different objective from optimizing *membrane permeability* for stationary interfacial entropy on a ring. The relationship to general convex divergence arguments is explicit in the proof, not represented as a new convexity principle.

## Limitations
Only the stationary **interfacial** contribution to entropy production is optimized, not total entropy including reservoir/reset costs. The symmetric, constant-permeability interface and drift-free, spatially constant diffusivity are essential to the scalar reduction. Existence of a unique optimum is false for a boundary-balanced reset law, since its interfacial entropy vanishes identically. No conclusions about higher-dimensional interfaces, spatially varying permeability, drift, or optimal resetting rates for total entropy are asserted. Some results may be obtainable by further reduction of published stationary formulas; that derivational relationship is an originality risk. Independent validation has not been performed.

## References
- P. C. Bressloff, *Entropy production for diffusion processes across a semipermeable interface*, arXiv:2402.16403v1 (public 2024-02-26); *Physical Review Research* 6, 023283 (2024), DOI:10.1103/PhysRevResearch.6.023283. Relevant parts: sections II-III, especially stationary equations (3.11)-(3.20), interfacial entropy (3.18), and Fig. 7.
- P. C. Bressloff, *Diffusion with stochastic resetting screened by a semipermeable interface*, arXiv:2211.12468v1 (2022). Distinct absorption/first-passage objective.
- Kay and Giuggioli, *Local Time Statistics and Permeable Barrier Crossing: from Poisson to Birth-Death Diffusion Equations*, arXiv:2406.07142 (2024). Relevant permeable-crossing models.
