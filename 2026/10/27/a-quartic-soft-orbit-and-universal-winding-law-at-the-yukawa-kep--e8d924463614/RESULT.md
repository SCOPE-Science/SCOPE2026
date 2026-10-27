# A quartic soft orbit and universal winding law at the Yukawa–Kepler cusp

## Finding

For a particle of unit mass moving in the central potential
\[
\Phi(r)=-\frac{\mu}{r}\left(1+\alpha e^{-r/\lambda}\right),\qquad \mu,\lambda>0,\quad\alpha\ge 0,
\]
there is one sharp attractive-Yukawa strength
\[
\alpha_c=\frac{e^3}{5}
\]
at which the circular-orbit angular-momentum curve develops a stationary cubic point. This is also the unique coupling at which a circular orbit has a strictly confining quartic, rather than quadratic, radial effective-potential minimum. Its radius and squared *specific* angular momentum are
\[
r_c=3\lambda,\qquad \ell_c^2=\frac{27}{5}\mu\lambda.
\]
For radial oscillations about this orbit with fixed angular momentum and outer turning point \(r_c+A\), \(A\downarrow0\), the full radial period \(T(A)\) and the azimuth swept in one radial period \(\Delta\theta(A)\) satisfy the sharp laws
\[
\boxed{\lim_{A\downarrow0}A T(A)=\sqrt{\frac{540\lambda^5}{\mu}}\,\mathrm B\!\left(\frac14,\frac12\right)},\qquad
\boxed{\lim_{A\downarrow0}\frac A\lambda\Delta\theta(A)=6\,\mathrm B\!\left(\frac14,\frac12\right)}.
\]
Here \(\mathrm B\) is Euler's beta function. The second coefficient is independent of either dimensional parameter. In particular, the radial oscillations soften to zero frequency while a radial cycle involves unboundedly many revolutions.

The same critical coupling marks a *global* transition in circular-orbit multiplicity. Put
\[
x=\frac r\lambda,\quad p=\frac{\ell^2}{\mu\lambda},\qquad
H_\alpha(x)=x\left[1+\alpha(1+x)e^{-x}\right].
\]
All circular orbits correspond exactly to positive roots of \(H_\alpha(x)=p\). For \(0\le\alpha<\alpha_c\), every \(p>0\) gives one strictly radially stable circle. At \(\alpha=\alpha_c\), the same is true apart from the quartic orbit at \(p=27/5\). For \(\alpha>\alpha_c\), there are unique numbers \(x_-\in((1+\sqrt5)/2,3)\) and \(x_+\in(3,\infty)\) satisfying
\[
\alpha e^{-x_\pm}(x_\pm^2-x_\pm-1)=1.
\]
Define \(p_-=H_\alpha(x_+)\) and \(p_+=H_\alpha(x_-)\). Then \(0<p_-<p_+\). Precisely when \(p_-<p<p_+\), there are three circles, with the inner and outer radially stable and the middle radially unstable. At the endpoints there are two distinct circles, one an ordinary stable circle and one degenerate fold circle; outside the closed interval there is exactly one stable circle.

The triple-orbit interval opens with a quantified cusp. As \(\alpha=\alpha_c(1+\eta)\), \(\eta\downarrow0\),
\[
x_\pm=3\pm\sqrt{\frac{10}{3}}\,\eta^{1/2}+O(\eta),
\]
\[
p_\pm=\frac{27}{5}+\frac{12}{5}\eta\pm\frac23\sqrt{\frac{10}{3}}\,\eta^{3/2}+O(\eta^2),
\]
so its exact leading width is
\[
\boxed{p_+-p_-\sim\frac43\sqrt{\frac{10}{3}}\,\eta^{3/2}}.
\]
These statements form one description of the sharp soft-orbit cusp and its global unfolding.

## Assumptions and scope

The motion is classical and Newtonian, in a plane, under a smooth central force for \(r>0\). The potential is taken as an exact mathematical model for arbitrary nonnegative coupling \(\alpha\); no small-coupling approximation is used. The parameter \(\mu\) is the gravitational parameter per unit test mass, \(\lambda\) is the Yukawa length, and \(\ell\ne0\) is *specific* angular momentum. Linear radial stability refers to the reduced dynamics at fixed \(\ell\), not to dissipative attraction or nonlinear stability with externally varying angular momentum. At zero epicyclic frequency the classification is made from the full radial potential, rather than from linear eigenvalues alone. The radial period and winding limits use fixed \(\ell=\ell_c\), fixed \(\alpha=\alpha_c\), and a turning-point amplitude \(A\) measured in units of length.

## Proof

The radial effective potential per unit mass is
\[
\Phi_{\rm eff}(r)=\frac{\ell^2}{2r^2}-\frac\mu r(1+\alpha e^{-r/\lambda}).
\]
Direct differentiation, without expansion in \(r/\lambda\), yields
\[
\Phi_{\rm eff}'(r)=\frac{\mu\lambda}{r^3}[H_\alpha(r/\lambda)-p],
\]
which proves the circular-orbit equation. Its radial second derivative at such an orbit is
\[
\kappa_r^2=\Phi_{\rm eff}''(r)=\frac\mu{r^3}H_\alpha'(x),\qquad
H_\alpha'(x)=1+\alpha e^{-x}(1+x-x^2).
\]
In particular \(\kappa_r^2\) is positive or negative precisely according to the strict radial minimum or maximum of the effective potential.

Write \(g(x)=e^{-x}(x^2-x-1)\). This function is nonpositive on \((0,(1+\sqrt5)/2]\), strictly increases until \(x=3\), and strictly decreases thereafter to zero, because
\[
g'(x)=x(3-x)e^{-x},\qquad g(3)=5e^{-3}.
\]
Consequently, \(H_\alpha'=1-\alpha g\) is everywhere positive when \(\alpha<e^3/5\). At equality its only zero is \(x=3\) and the function remains strictly increasing. Above equality it has exactly the two simple zeros \(x_-\) and \(x_+\) specified in the finding and has derivative signs \(+,-,+\) across the three resulting intervals. Since \(H_\alpha(0+)=0\), \(H_\alpha(\infty)=\infty\), and \(H_\alpha(x)>0\), the full orbit counts and stability signs follow. At a fold the force vanishes to second order in radial displacement, which is why no claim of ordinary stability is made there.

At the critical point, direct differentiation gives
\[
H_{\alpha_c}(3)=27/5,\quad H_{\alpha_c}'(3)=H_{\alpha_c}''(3)=0,\quad H_{\alpha_c}'''(3)=3/5.
\]
Therefore \(H_{\alpha_c}(3+\delta)-27/5=\delta^3/10+O(\delta^4)\). Integrating the exact effective-potential derivative gives, for \(z=r-3\lambda\),
\[
\Phi_{\rm eff}(3\lambda+z)-\Phi_{\rm eff}(3\lambda)
=\frac\mu{1080\lambda^5}z^4+O\!\left(\frac{\mu|z|^5}{\lambda^6}\right).
\]
Thus the critical circle is a strict *quartic* radial minimum at its fixed angular momentum. The leading radial equation is
\[
\ddot z+\frac\mu{270\lambda^5}z^3=0.
\]
The full equation has higher-order analytic terms, but standard turning-point rescaling in the energy integral gives the same leading period. Indeed, writing \(c=\mu/(270\lambda^5)\), energy conservation for an excursion with outer turning displacement \(A\) implies, uniformly on compact subsets of the rescaled interval,
\[
\dot z^{\,2}=\frac c2(A^4-z^4)+o(A^4).
\]
The inner turning point is \(-A+O(A^2/\lambda)\). Factoring the two simple turning-point zeros for each \(A>0\), or equivalently using a sine-angle substitution, gives dominated convergence also at the endpoints. Hence
\[
T(A)\sim4\sqrt{\frac2c}\,\frac1A\int_0^1\frac{du}{\sqrt{1-u^4}}
=\frac1A\sqrt{\frac2c}\,\mathrm B\!\left(\frac14,\frac12\right).
\]
At the circle the azimuthal rate is \(\Omega_c=\ell_c/(3\lambda)^2=\sqrt{\mu/(15\lambda^3)}\). Throughout the shrinking radial oscillation \(\dot\theta=\ell_c/r^2=\Omega_c[1+O(A/\lambda)]\), so
\[
\Delta\theta(A)=\Omega_c T(A)[1+O(A/\lambda)].
\]
The two stated constants follow, including \(\Omega_c\sqrt{540\lambda^5/\mu}=6\lambda\).

Finally, set \(\alpha=\alpha_c(1+\eta)\). Taylor expansion of the *exact* derivative near \(x=3\) gives
\[
H_\alpha'(3+\delta)=-\eta+\frac3{10}\delta^2+O(|\delta|^3+\eta\delta^2).
\]
The two zeros therefore satisfy \(\delta=\pm\sqrt{10\eta/3}+O(\eta)\). The center value is exactly \(H_\alpha(3)=27/5+12\eta/5\). Integrating this derivative between the center and each turning point gives the two expansions for \(p_\pm\), and subtraction gives the \(\eta^{3/2}\) width law. No finite computation is used to infer any of the quantifiers in these arguments.

## Verification

The included standalone `VERIFY.py` checks the exact differentiation and critical Taylor coefficients symbolically, tests the fold inequalities and circular-root counts on independently generated finite parameter families, and independently integrates the radial energy equation and angular advance near the quartic orbit. It reports numerical convergence to the beta-function coefficients. Run `python VERIFY.py` with Python 3 and the freely available `sympy` and `mpmath` packages; its outputs are diagnostics, not a substitute for the proof. Parameter examples for \(\alpha=1.1\alpha_c\): \(x_-\approx2.5056068264\), \(x_+\approx3.6353688966\), \(p_-\approx5.5992638971\), and \(p_+\approx5.6737955036\). Thus \(p\approx5.6365297003\) yields three circles at approximately \(2.1523775145\), \(3.0347486184\), and \(4.1354379185\) in units of \(\lambda\).

## Relationship to prior work

The Yukawa correction to Newtonian gravity and its exact central acceleration are classical. Iorio (arXiv:1109.6249, first public 28 September 2011), equation (10)–(11), gives the same potential and force and analyzes perturbative orbital observables, not the strong-coupling quartic orbit or its nonlinear apsidal winding. Pricopi (2016, DOI below) studies stable and unstable motion for the Yukawa-corrected two-body model with energy and angular-momentum foliations; its abstract directly overlaps the broad stability theme. The original complete text could not be accessed during the comparison, so any equivalence of its phase-space classification is a priority risk; **mere existence of stable and unstable regions is not claimed as new**. Abo Hasan–Joudieh–Chamoun (arXiv:2301.02498, published in 2023) analyze the same potential but replace the exponential by its small-radius first-order expansion in their stability calculation (their equations (18)–(26)), a regime that removes the strong-coupling radial cusp. The quantitatively assessed contribution here is the sharp quartic singularity, its universal winding coefficient, and the exact cusp-opening law within the unexpanded model, not the potential, central-force equation, or generic central-orbit stability criterion.

## Limitations

The coupling \(\alpha_c\approx4.0171073846\) is substantially larger than the weak-coupling values typically investigated for Solar-System fifth-force phenomenology; no observational relevance is asserted. The model neglects general relativity, extended-body structure, radiation, drag, dissipation, and changes to the source gravitational parameter. At the critical circle the linear radial frequency vanishes, so statements about oscillations rely on the nonlinear energy integral. The inaccessible full 2016 source and any earlier unlocated equivalent asymptotic analyses leave a real historical-priority risk. No independent audit or experimental confirmation is claimed.

## References

1. L. Iorio, “Constraints from orbital motions around the Earth of the environmental fifth-force hypothesis for the OPERA superluminal neutrino phenomenology,” arXiv:1109.6249, originally submitted 2011-09-28; https://arxiv.org/abs/1109.6249 . Relevant model equations (9)–(11), and methods/claims in Sections 2–4.
2. D. Pricopi, “Stability of the celestial body orbits under the influence of Yukawa potential,” *Astrophysics and Space Science* **361** (2016), 277; DOI:10.1007/s10509-016-2864-3; public online 2016-07-29. Abstract and bibliographic metadata inspected; full text inaccessible in this comparison.
3. N. Abo Hasan, N. Joudieh and N. Chamoun, “Dynamics and stability of the two-body problem with Yukawa correction to Newton's gravity, revisited and applied numerically to the solar system,” arXiv:2301.02498, 2023; https://arxiv.org/abs/2301.02498 . Relevant Hamiltonian equations (3), (14)–(26) and their small-\(r/\lambda\) assumption.
4. G. S. Adkins and J. McDonnell, “Orbital precession due to central-force perturbations,” *Physical Review D* **75** (2007), 082001; DOI:10.1103/PhysRevD.75.082001. General perturbative precession framework (bibliographic and abstract comparison).
