# Sharp peak-growth tomography for two equal-depth Rayleigh–Taylor layers

## Finding
Consider the fastest growing mode of a capillary Rayleigh–Taylor interface between two equally deep, inviscid fluid layers. With the densities and gravity known, the wavenumber and growth rate of that one mode determine the unknown common depth and interfacial tension **uniquely**. This inverse problem has the exact and strict realizability criterion
\[
k_*>0,\qquad 0<\frac{\Gamma_*^2}{Ak_*}<\frac23,\qquad A=\frac{(\rho_h-\rho_l)g}{\rho_h+\rho_l}.
\]
Every observational pair inside this region comes from exactly one pair of strictly positive finite physical parameters. The endpoints are unattainable for these parameters.

## Assumptions and scope
Let \(g>0\) and \(\rho_h>\rho_l>0\) be known. Two homogeneous, incompressible, inviscid, immiscible fluids fill equal finite depths \(H>0\) above and below a flat interface, with the heavy fluid above the light. The top and bottom walls are fixed and impermeable. The domain is horizontally unbounded, both base velocities vanish, and interfacial tension \(T>0\) is constant. Perturbations are infinitesimal normal modes with arbitrary continuous horizontal wavenumber \(k>0\). Linearization, not nonlinear pattern selection, determines the growth rates. The unknowns are precisely \(H,T\).

Define \(\Delta\rho=\rho_h-\rho_l\), \(A=\Delta\rho g/(\rho_h+\rho_l)\) and \(B=T/(\rho_h+\rho_l)\). For \(0<k<k_c=\sqrt{A/B}\), the positive growth rate is
\[
\Gamma(k)^2=(Ak-Bk^3)\tanh(kH).
\]
Outside this interval there is no exponentially growing normal mode. Define \((k_*,\Gamma_*)\) as the wavenumber and positive growth rate at the **global** maximum of the growing branch.

For \(x>0\), set
\[
q(x)=\frac{2x}{\sinh(2x)},\qquad
E(x)=\frac{2\tanh x}{3+q(x)},\qquad
b(x)=\frac{1+q(x)}{3+q(x)}.
\]
Then \(E\) is a strictly increasing bijection from \((0,\infty)\) onto \((0,2/3)\). For any proposed observations \(k_*,\Gamma_*>0\), set \(y=\Gamma_*^2/(Ak_*)\). A physical parameter pair exists **if and only if** \(0<y<2/3\); when it exists it is uniquely recovered as
\[
x=E^{-1}(y),\qquad H=\frac{x}{k_*},\qquad
T=\frac{\Delta\rho g}{k_*^2}\,b(x).
\]
In particular, the capillary ratio at the fastest-growing mode satisfies the sharp bound
\[
\frac13<\frac{Tk_*^2}{\Delta\rho g}<\frac12.
\]

## Proof
**Dispersion relation.** Solve Laplace's equation for the velocity potentials in the two layers with vanishing normal velocity at their rigid walls. The potentials are multiples of the relevant \(\cosh\) profiles. The interface kinematic condition and linearized Bernoulli pressure jump, including the capillary restoring pressure, give the standard finite-depth relation
\[
\Gamma(k)^2=\frac{\Delta\rho g\,k-Tk^3}{(\rho_h+\rho_l)\coth(kH)}
=(Ak-Bk^3)\tanh(kH).
\]
Both signs and the unstable band follow from \(\Delta\rho>0\) and \(T>0\).

**Exactly one growth peak.** Let \(s=B/A>0\), \(b=sk^2\), and \(x=kH\). On \(0<k<1/\sqrt{s}\), differentiating the squared growth rate and dividing by the positive quantity \(A\tanh(kH)\) gives
\[
F(k)=1-3sk^2+(1-sk^2)q(kH).
\]
For every \(x>0\), \(q(x)>0\) and \(q'(x)<0\), since \(\sinh(2x)<2x\cosh(2x)\). Hence
\[
F'(k)=-6sk-2skq(kH)+(1-sk^2)Hq'(kH)<0.
\]
Also \(\lim_{k\downarrow0}F(k)=2\) and \(F(1/\sqrt{s})=-2\). Consequently \(F\) has exactly one zero in the unstable band; this zero is the unique strict global growth maximum because \(\Gamma^2\) vanishes at both band endpoints and is positive between them.

**Direct-to-inverse reduction.** At the maximum \(F(k_*)=0\). Rearrangement gives
\[
\frac{Tk_*^2}{\Delta\rho g}=sk_*^2=\frac{1+q(x)}{3+q(x)}=b(x),\qquad x=k_*H.
\]
Substituting into the dispersion relation yields
\[
\frac{\Gamma_*^2}{Ak_*}=(1-b(x))\tanh x=E(x).
\]
Now \(q'(x)<0\) implies \(3+q(x)\) strictly decreases, whereas \(\tanh x\) strictly increases. Both are strictly positive; therefore \(E(x)\) is strictly increasing. Its limiting values are \(E(0+)=0\) and \(E(+\infty)=2/3\). Hence it has the claimed global inverse. The reconstruction formulas give \(H,T>0\) for every admissible observation pair, and the already-proved peak uniqueness ensures the recovered pair realizes exactly those observations. The strict tension-ratio bounds follow from \(0<q(x)<1\).

**Sharp edges and identifiability sensitivity.** The elementary expansions give
\[
E(x)=\frac{x}{2}-\frac{x^3}{12}+O(x^5)\quad(x\downarrow0),
\]
\[
\frac23-E(x)=\frac49(3+2x)e^{-2x}+O(x^2e^{-4x})\quad(x\to\infty).
\]
Thus neither endpoint can occur at finite depth. The inverse becomes exponentially ill-conditioned for large \(k_*H\); uniqueness is exact but numerical stability in the deep-water limit is not uniform.

## Verification
A standalone `CHECK.py` independently maximizes the forward dispersion relation numerically and applies the inverse equations, with 76 forward-to-inverse cases and 63 constructed inverse-to-forward cases. Its finite tests verify signs, normalization and representative reconstructions; the global uniqueness claim is proved above and is not inferred from numerical sampling.

## Relationship to prior work
Mikaelian (1990) derived the finite-thickness two-fluid surface-tension dispersion relation within a broader multilayer Rayleigh–Taylor/Richtmyer–Meshkov analysis. Mikaelian (1996), especially the inviscid limit of equation (2) and equal-layer discussion around equation (26), treats finite-thickness growth rates and their dependence on thickness, viscosity and tension. Those **forward** dispersion relations are assumed as established, not claimed as discoveries here. The present claim is the **complete inverse classification from just the global peak's location and height**, including a necessary-and-sufficient dimensionless feasibility wedge and uniqueness for the two unknown parameters. A literature search did not identify an exact equivalent theorem. The complete 1990 article could not be inspected, so historical priority for the inverse result remains a material uncertainty.

## Limitations
The strict feasibility wedge holds for common finite depths, known densities and gravity, inviscid incompressible fluids, positive surface tension, no mean shear, perfectly rigid horizontal boundaries, and continuous wavenumbers. It does not cover unequal depths, viscosity, compressibility, bounded horizontal geometry, finite-amplitude breakup, noisy estimates, or simultaneous uncertainty in densities or gravity. Exact identifiability does not establish robust statistical recovery. Priority against inaccessible historical sources is unresolved.

## References
- K. O. Mikaelian, "Rayleigh–Taylor and Richtmyer–Meshkov instabilities in multilayer fluids with surface tension," *Physical Review A* **42** (1990), 7211–7225. DOI: 10.1103/PhysRevA.42.7211. First public date verified as 1990-12-01.
- K. O. Mikaelian, "Rayleigh–Taylor instability in finite-thickness fluids with viscosity and surface tension," *Physical Review E* **54** (1996), 3676–3680. DOI: 10.1103/PhysRevE.54.3676.
