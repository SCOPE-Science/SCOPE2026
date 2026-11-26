# Gas-current shape controls stationary coexistence but not optimal droplet width

## Finding

For symmetric stationary branches of a one-dimensional locally reset two-velocity transport law, let \(M\) be the total mass, \(r>0\) the reset rate, \(\alpha>0\) the direction-reselection rate, \(u>0\) the constant dense-phase speed and \(\rho_m>0\) the dense-phase threshold. Write \(\Lambda=\sqrt{r(r+\alpha)}\), \(J=u\rho_m\) and \(F_{\max}=f(\rho_p)\) for the maximum dilute-phase current. Assume \(F_{\max}>J\).

Within the stationary class specified below, the continuous gas branch exists exactly for \(M\Lambda/2\le F_{\max}\), and the nondegenerate dense droplet branch exists exactly for \(M\Lambda/2>J\); each is unique in its class. Thus the two branches coexist exactly for \(J<M\Lambda/2\le F_{\max}\). The droplet half-width and gas and dense masses are
\[
b=\frac{u}{\Lambda}\log\!\frac{M\Lambda}{2J},\qquad M_{\rm gas}=\frac{2J}{\Lambda},\qquad M_{\rm dense}=M-\frac{2J}{\Lambda}.
\]
The half-width is maximized uniquely at \(\Lambda_*=2eJ/M\), with \(b_*=M/(2e\rho_m)\) and gas mass fraction \(1/e\). This maximum is strictly inside the coexistence interval if \(F_{\max}/J>e\), at the upper endpoint if \(F_{\max}/J=e\), and above that endpoint if \(F_{\max}/J<e\). For the pure gas branch, the right-hand origin density \(\rho_0\) approaches the upper endpoint according to
\[
\rho_p-\rho_0\sim\sqrt{\frac{2(F_{\max}-M\Lambda/2)}{|f''(\rho_p)|}}.
\]
These are statements about existence, not dynamical stability or phase selection.

## Model and assumptions

Take \(M>0\) and \(f\in C^2([0,\rho_m))\), interpreting derivatives at zero one-sided. Require \(f(0)=0\), \(f'(0)>0\), \(f(\rho)>0\) for \(0<\rho<\rho_m\), and \(f''(\rho)<0\) for **\(0<\rho<\rho_m\)**; no strict inequality is required for \(f''(0)\). Assume an interior maximum at \(\rho_p\in(0,\rho_m)\), so \(f'(\rho_p)=0\) and \(f''(\rho_p)<0\). The dilute speed is \(v(\rho)=f(\rho)/\rho\), extended continuously to zero; for \(\rho\ge\rho_m\) the speed is \(u\).

For right- and left-mover densities \(q_+,q_-\), with \(\rho=q_++q_-\), the stationary equations off the resetting origin are
\[
0=-(vq_+)'-\left(r+\frac\alpha2\right)q_++\frac\alpha2 q_-,\qquad
0=(vq_-)'-\left(r+\frac\alpha2\right)q_-+\frac\alpha2 q_+.
\]
The origin injects \(rM/2\) into each directional equation as a point source. Assume \(q_+(x)=q_-(-x)\), total mass \(M\), decay at infinity, and no atoms or additional shocks. The continuous gas branch takes values in \((0,\rho_p]\). The droplet branch has a single dense interval \([-b,b]\), with \(b>0\), \(\rho(b^-)=\rho_m\), and a continuous monotone dilute tail on \(x>b\). A density jump at the interface is allowed, but the two directional transport fluxes are continuous there. The gas endpoint cusp is admitted as a weak solution.

## Proof

Set \(\sigma=q_+-q_-\), \(R=v\rho\), \(S=v\sigma\) and \(c=\sqrt{r/(r+\alpha)}\). Adding and subtracting the equations on smooth phases gives \(S'=-r\rho\) and \(R'=-(r+\alpha)\sigma\). For \(D=S-cR\) this gives \(D'=(\Lambda/v)D\). On the right gas tail both fluxes vanish at infinity, and a nonzero solution for \(D\) would have nondecreasing absolute value there since \(v>0\). Thus \(D=0\); continuity propagates this identity across the interface and uniqueness of the linear equation makes it hold in the dense interval as well. Consequently
\[
S=cR,\qquad \sigma=c\rho,\qquad R'=-\Lambda\rho,
\qquad R(x)=\Lambda\int_x^\infty\rho(s)\,ds \quad(x>0).
\]
In particular \(R(0^+)=M\Lambda/2\). Conversely, construct any right-hand density profile with these identities, and use \(q_\pm=(1\pm c)\rho/2\) on the right and reflection with direction exchange on the left. The transport fluxes are \((R\pm S)/2\), continuous at the phase transitions, and their jumps at the origin are \(rM/2\) and \(-rM/2\), respectively, since \(c\Lambda=r\). With the displayed signed derivatives these jumps cancel the point sources in both stationary equations.

On a continuous decreasing gas tail the strict decrease of \(R\) forces the density to use the increasing branch of \(f\). For a starting location \(a\) with density \(d\in(0,\rho_p]\), the unique gas continuation is the inverse of
\[
\Lambda(x-a)=\int_{\rho(x)}^d\frac{f'(z)}{z}\,dz.
\]
The right side increases strictly from zero to infinity as \(\rho(x)\) decreases to zero, the divergence following from \(f'(0)>0\). For gas alone take \(a=0\); normalization fixes \(f(\rho_0)=M\Lambda/2\), which is possible uniquely exactly up to \(F_{\max}\). At equality the inverse is continuous and the flux has a finite derivative at the origin from the right; it yields the weak solution despite the density cusp. The asymptotic law for \(\rho_0\) follows from Taylor expansion at the strict interior maximum with nonzero second derivative.

For a droplet, matching the flux gives \(R(b)=J\), so its gas interface density is the unique lower-branch solution of \(f(d)=J\). Its right tail mass is \(J/\Lambda\). In the dense region \(R=u\rho\), so \(R(x)=J\exp(\Lambda(b-x)/u)\) for \(0\le x\le b\). Imposing \(R(0)=M\Lambda/2\) now gives the stated half-width, strictly positive exactly for \(M\Lambda/2>J\). These profiles satisfy all phase and normalization conditions and are uniquely determined within their respective classes. For \(t=M\Lambda/(2J)>1\), maximizing \(b\) is equivalent to maximizing \((\log t)/t\), whose derivative has the sign of \(1-\log t\). Since \(r\mapsto\Lambda\) is strictly increasing and onto \((0,\infty)\), the unique maximum is at \(t=e\). Substitution gives the half-width and mass fractions and comparing to \(M\Lambda/2=F_{\max}\) gives the three cases.

## Two laws with different coexistence behavior

Take \(\rho_m=8\), \(u=1/8\), \(M=4\), \(\alpha=1\), so \(J=1\). The currents \(f_1(\rho)=\rho(1-\rho/8)\) and \(f_2(\rho)=\rho[1-(\rho/8)^2]\) share the same slope at zero and satisfy strict curvature on the open density interval (\(f_2''(0)=0\)). Their maxima are \(2\) and \(16/(3\sqrt{3})\), respectively, strictly on opposite sides of \(e\). The optimal half-width is \(1/(4e)\) for both. There is a gas-only stationary solution at the second law's optimum but not at the first law's optimum, despite identical droplet geometry and mass partition at optimality.

## Verification, prior work and limits

The accompanying `verify.py` gives finite numerical illustrations for \(f_p(\rho)=\rho[1-(\rho/8)^p]\) with \(p=1,2,3,4,7\), checking quadrature of the phase masses and the implicit gas equation. The analytic argument, not these spot checks, proves the theorem. Its strict curvature condition is on positive densities, so all five laws satisfy it.

Grange, *Motility-Induced Phase Separation of Run-and-Tumble Particles under Local Stochastic Resetting*, [arXiv:2610.26149v2](https://arxiv.org/html/2610.26149v2), §§2–4, derives the flux first integral, the width and optimum, and gas cutoff, origin-density square root and coexistence inequalities for a linear gas speed. With \(u=v_0/\rho_m\), that law has \(J=v_0\), \(F_{\max}/J=\rho_m/4\); even the comparison to the width optimum is implicit in those special-case formulas. The contribution here is the joint stationary branch comparison over the stated concave-current class, with the peak current free to change independently of the dense flux. A separate result on [gas-independent droplet geometry and power-law optimal resetting](https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-gas-independent-droplet-geometry-and-power-law-optimal-resetting--c82a3ef3fe29/RESULT.md) gives broader matched-flux droplet formulas and includes the constant-dense-speed optimum, but does not treat the competing gas-only branch or the origin-density fold.

No general characterization of nonmonotone or multishock stationary states, hydrodynamic stability, microscopic invariant measures, or finite-speed return dynamics is implied.
