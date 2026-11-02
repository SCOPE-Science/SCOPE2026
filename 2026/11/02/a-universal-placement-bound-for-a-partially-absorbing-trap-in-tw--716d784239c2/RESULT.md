# A universal placement bound for a partially absorbing trap in two-layer diffusion

## Finding

Let \(L,d,\kappa>0\), let \(r>1\), and set \(D(s)=d\) for \(0<s<L/2\) and \(D(s)=rd\) for \(L/2<s<L\). Under reflecting boundary conditions, maximize the lowest eigenvalue \(\lambda_1(x;\kappa)\) of the positive form
\[
\mathfrak q_x[u]=\int_0^L D(s)|u'(s)|^2\,ds+\kappa|u(x)|^2,
\qquad u\in H^1(0,L),\quad 0<x<L.
\]
This eigenvalue is the leading exponential decay rate of a Fickian diffusing particle killed by a partially absorbing point trap of strength \(\kappa\).

For \(0<z<z_\infty(r)\), define
\[
\alpha_r(z)=\arctan\!\left(\sqrt r\tan\frac z{\sqrt r}\right),
\quad z_\infty+\alpha_r(z_\infty)=\pi,
\quad \frac\pi2<z_\infty<\min\{\pi,\frac{\pi\sqrt r}{2}\}.
\]
The equation specifying \(z_\infty\) has exactly one solution in that indicated interval. Every \(\kappa>0\) uniquely specifies \(z\in(0,z_\infty)\) by
\[
\kappa=\frac{4dz}{L}\tan\!\left(\frac{z+\alpha_r(z)}2\right).
\]
**Exact all-strength optimum:** the unique trap location maximizing the lowest eigenvalue is
\[
\boxed{x_*(\kappa)=\frac L4\left(1+\frac{\alpha_r(z)}z\right)},
\qquad \boxed{\max_{0<x<L}\lambda_1(x;\kappa)=\frac{4dz^2}{L^2}}.
\]
The optimum lies strictly in the slower layer, \(x_*(\kappa)<L/2\). As \(\kappa\) increases it decreases strictly from \(L/2\) to \(x_\infty(r)=\pi L/(4z_\infty(r))\). More sharply, if \(t_0\) is the unique root of \(\tan t_0=-t_0\) in \((\pi/2,\pi)\), then
\[
\boxed{\frac{\pi}{4t_0}<\frac{x_*(\kappa)}L<\frac12},
\qquad \frac{\pi}{4t_0}=0.387132534324\ldots .
\]
The lower constant is sharp as both diffusivity ratio and trap strength diverge. Thus the strongest possible displacement away from the midpoint is less than \(0.112867465676\ldots L\), despite arbitrarily large diffusivity contrast.

## Assumptions and scope

The diffusion law is exactly \(\partial_t p=\partial_s(D(s)\partial_s p)-\kappa\delta_x p\), with no-flux endpoints and continuous density and flux across the material interface. The absorber imposes \((Du')(x+)-(Du')(x-)=\kappa u(x)\). At a trap located at the material interface the corresponding flux jump is imposed there. The operator is defined by the closed quadratic form above; its compact resolvent ensures a simple, strictly positive ground eigenfunction. The diffusion convention is Fickian, not the Itô forward equation \(\partial_s^2(Dp)\) or the Stratonovich equation \(\partial_s(\sqrt D\,\partial_s(\sqrt D\,p))\). All statements are for finite \(L\), positive \(d\), arbitrary finite \(r>1\), and positive finite \(\kappa\); limiting parameter statements concern these explicit domains.

## Proof

**1. One-sided impedance comparison.** Fix a positive spectral parameter \(\lambda\) below the first mixed Neumann–Dirichlet eigenvalue on each side of a proposed trap \(x\). Let \(u_L\) solve \(-(Du_L')'=\lambda u_L\) on \((0,x)\) with \(u_L'(0)=0\), and let \(u_R\) solve it on \((x,L)\) with \(u_R'(L)=0\). Normalize both by their positive values at \(x\). Their positive inward impedance contributions are
\[
\ell(x,\lambda)=-\frac{D(x-)u_L'(x-)}{u_L(x)},\qquad
m(x,\lambda)=\frac{D(x+)u_R'(x+)}{u_R(x)}.
\]
The absorber eigencondition is \(\ell+m=\kappa\). On each constant-diffusivity layer these quantities obey
\[
\partial_x\ell=\lambda+\ell^2/D,
\quad\partial_x m=-\lambda-m^2/D,
\quad\partial_x(\ell+m)=(\ell^2-m^2)/D.
\]
The same impedance values are continuous when \(x\) crosses the material interface. Since \(\ell\) increases strictly and \(m\) decreases strictly with \(x\), the sum decreases strictly while \(\ell<m\), and increases strictly while \(\ell>m\). Therefore, whenever balance \(\ell=m\) occurs, it is the unique global minimum of the required trap strength \(\ell+m\) at fixed \(\lambda\) on the positive-impedance interval. The variational principle shows that for \(x\) outside this interval the ground eigenvalue is already strictly below \(\lambda\): a test function supported on the side whose first mixed eigenvalue is below \(\lambda\) suffices. Strict monotonicity in \(\lambda\) of each impedance (from the positive squared solution integral, or Sturm comparison) converts minimizing the required strength at fixed \(\lambda\) into uniquely maximizing \(\lambda_1(x;\kappa)\) at fixed \(\kappa\).

**2. Explicit balanced solution.** Put \(k=\sqrt{\lambda/d}=2z/L\). For a trap in the slow layer, the left impedance equals \(dk\tan(kx)\). The fast right half has input impedance \(dk\sqrt r\tan(z/\sqrt r)\) at the interface, so its slow-layer phase shift is \(\alpha_r(z)\). The right impedance evaluated at \(x\) is \(dk\tan(k(L/2-x)+\alpha_r(z))\). Matching the two positive impedances forces
\[
kx=k(L/2-x)+\alpha_r(z),\qquad
x=\frac L4(1+\alpha_r(z)/z).
\]
At that point both equal \(dk\tan((z+\alpha_r(z))/2)\), giving the stated strength law. The logarithmic-slope phases are positive and less than \(\pi/2\) for \(0<z<z_\infty\), so the assembled eigenfunction remains positive on the whole interval and is the ground eigenfunction. Further, \(\alpha_r(z)<z\) for \(r>1\), so the point lies strictly to the left of the interface. The map \(z\mapsto(4dz/L)\tan((z+\alpha_r(z))/2)\) increases continuously from zero to infinity; hence there is exactly one \(z\) for every positive \(\kappa\). Step 1 then makes this the unique global optimum, not merely a stationary configuration.

**3. Monotone location and sharp contrast-independent bound.** Differentiation gives
\[
\alpha_r'(z)=\frac1{1+(r-1)\sin^2(z/\sqrt r)}.
\]
It decreases strictly with \(z\) on \((0,z_\infty)\) for \(r>1\), because \(z_\infty/\sqrt r<\pi/2\). Thus \(\alpha_r(z)/z\) decreases strictly, so increasing \(\kappa\) moves \(x_*\) strictly left. At \(z=z_\infty\), the phase identity gives \(x_\infty/L=\pi/(4z_\infty)\). For fixed \(z\), \(\sqrt r\tan(z/\sqrt r)=z\,[\tan(z/\sqrt r)/(z/\sqrt r)]\) decreases strictly with \(r\) wherever defined. Hence \(z_\infty(r)\) increases strictly with \(r\) and has limit \(t_0\), the unique solution of \(t_0+\arctan t_0=\pi\). This is equivalent to \(\tan t_0=-t_0\). For finite \(r\), \(\pi/2<z_\infty(r)<t_0\); using \(z<z_\infty\) proves the strict universal bounds. Taking first large \(\kappa\), then large \(r\), reaches the lower constant in the limit and proves sharpness.

**4. Weak-reactivity limit.** Near zero,
\[
\alpha_r(z)=z-\frac{r-1}{3r}z^3+O(z^5),
\quad z^2=\frac{\kappa L}{4d}+O(\kappa^2).
\]
Substitution yields, with \(r,d,L\) fixed,
\[
x_*=\frac L2-\frac{\kappa L^2}{48}\left(\frac1d-\frac1{rd}\right)+O(\kappa^2),
\quad \lambda_{\max}=\frac\kappa L-\frac{\kappa^2}{24}\left(\frac1d+\frac1{rd}\right)+O(\kappa^3).
\]
The implicit constants depend on the fixed positive dimensional parameters.

## Verification

The standalone program `check.py` independently computes the lowest eigenvalue by multiplying flux-state transfer matrices across both material layers and the absorber jump, then uses root bracketing to locate the first positive eigenvalue. It compares the analytic optimum against sampled competing positions on both sides of the interface, multiple contrasts, strength regimes, dimensional scalings, and the weak-strength coefficients. It passes 2578 deterministic assertions on Python 3 with NumPy and SciPy. These finite diagnostics are not used as proof of the all-parameter statement.

## Relationship to prior work

Heterogeneous diffusion and its sensitivity to stochastic interpretation are documented by Kazakevičius and Ruseckas (2016) and Tung and Lawley (2026), but the inspected works do not establish the exact placement law for a movable interior point sink in a two-layer *Fickian* interval. The latter work principally derives weak-reactivity/small-target escape asymptotics in broad geometries. Grebenkov and Kolokolnikov (2026) study trap configurations in heterogeneous media for mean capture times and many small or perfect traps, a different objective and parameter regime. Classical narrow-capture studies optimize eigenvalues in higher-dimensional domains with small interior absorbing sets; they do not imply the explicit one-dimensional heterogeneous all-reactivity optimization and contrast-independent migration bound. The coincidence of a balanced impedance mechanism with other point-interaction eigenvalue problems does not supply this statement without its diffusion-interface analysis.

## Limitations

This is an exact model theorem, not an experimental transport prediction. It concerns a single point absorber, two *equal-length* material layers, piecewise-constant Fickian diffusivity, and reflecting endpoints. The optimum need not have this form for unequal layer lengths, several movable traps, non-Fickian stochastic conventions, finite-time capture objectives, or arbitrary variable diffusion profiles. A complete historical-priority guarantee is not claimed, particularly because some relevant older interior-trap eigenvalue papers were inaccessible in full text; independent literature verification has not been performed.

## References

1. R. Kazakevičius and J. Ruseckas, "Influence of external potentials on heterogeneous diffusion processes," arXiv:1608.07335v1 (posted 2016-08-25), https://arxiv.org/abs/1608.07335.
2. H.-R. Tung and S. D. Lawley, "Stochastic search with space-dependent diffusivity," arXiv:2601.08740v1 (posted 2026-01-13), https://arxiv.org/abs/2601.08740.
3. D. S. Grebenkov and T. Kolokolnikov, "Minimizing capture time with many small traps in heterogeneous media," arXiv:2609.39990v1 (posted 2026-09-30), https://arxiv.org/abs/2609.39990.
4. T. Kolokolnikov, M. S. Titcombe and M. J. Ward, "Optimizing the fundamental Neumann eigenvalue for the Laplacian in a domain with small traps," European Journal of Applied Mathematics 16 (2005), 161–200, https://doi.org/10.1017/S0956792505006145.
5. A. F. Cheviakov and M. J. Ward, "Optimizing the principal eigenvalue of the Laplacian in a sphere with interior traps," Mathematical and Computer Modelling 53 (2011), 1394–1409.
