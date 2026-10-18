# Exact straight-line isochrons by unique shear tuning in polygonal affine oscillators

## Finding
For every origin-star-shaped simple polygon whose successive vertex rays turn counterclockwise through angles strictly between zero and \(\pi\), a prescribed piecewise-affine hybrid oscillator has **one and only one choice of tangential shear on each edge** for which all sufficiently close perturbations along that edge's *incoming vertex ray* require exactly the on-cycle time to reach the next ray. The cancellation holds at finite perturbation amplitude, not only to first order. It creates an explicit local foliation by straight-line **asymptotic isochrons**, while preserving the polygonal limit cycle, its period and its transverse multiplier.

Fix the geometric and dynamical data in the next section. Define
\[
 E_i=\exp(-\kappa_i/\omega_i),\qquad
 A_i=\frac{p_i\cdot e_i}{\ell_i^2},\qquad B_i=A_i+1.
\]
The unique shear is
\[
 \boxed{\mu_i^*=\frac{\kappa_i}{C_i}\frac{A_i-B_iE_i}{1-E_i}.}
\]
For every sufficiently small real \(\delta\), the trajectory started at \((1+\delta)p_i\) reaches the next ray **at exactly** \(t_i=1/\omega_i\) in the point \((1+E_i\delta)p_{i+1}\). Thus at a fixed vertex ray the one-turn return map and physical period are exactly
\[
 \boxed{\delta\longmapsto R\delta,\quad R=\prod_{i=1}^N E_i\in(0,1),\qquad P=\sum_{i=1}^N\omega_i^{-1}.}
\]
For a centered regular polygon with common \(\omega_i=\omega>0\), \(\lambda_i=\lambda>0\) and one common shear, the unique choice reduces to
\[
 \boxed{\mu^*=-\frac{\kappa}{2C}\coth\!\left(\frac{\kappa}{2\omega}\right),\qquad \kappa=\lambda\ell^2,\quad C=\det(p_i,p_{i+1}).}
\]

## Assumptions and scope
Take an integer \(N\ge3\) and nonzero ordered planar points \(p_1,\ldots,p_N\), indexed cyclically. Their connecting edges form a simple closed polygon with the origin strictly inside, the polygon is star-shaped about the origin, and the successive radial angular increments lie in \((0,\pi)\). In particular, \(C_i=\det(p_i,p_{i+1})>0\). Put
\[
 e_i=p_{i+1}-p_i,\quad n_i=(e_{i,2},-e_{i,1}),\quad
 \ell_i^2=e_i\cdot e_i,\quad V_i(x)=n_i\cdot x-C_i,
 \quad \kappa_i=\lambda_i\ell_i^2.
\]
Choose arbitrary real tangential shears \(\mu_i\), positive transverse coefficients \(\lambda_i>0\) and positive on-cycle speeds \(\omega_i>0\). In the sector between the successive vertex rays, use the piecewise affine flow
\[
 \boxed{\dot x=\omega_i e_i-(\lambda_i n_i+\mu_i e_i)V_i(x).}
\]
The trajectory switches to the next affine mode at each **transverse** crossing of a vertex ray. This is the standard continuous-trajectory hybrid concatenation convention for this model; the vector field need not be continuous across a ray. All conclusions concern a sufficiently small annular neighborhood of the polygon, not a global basin or arbitrary disturbances.

An isochron through a point of the stable periodic orbit means the set of nearby points whose trajectories converge in phase to the trajectory based at that point with no asymptotic time shift. We use this phase-convergence definition, and do not assume global differentiability at switching rays.

## Proof
**1. Normal/tangential coordinates and exact flow.** On edge \(i\), write
\[
 x=p_i+s e_i+(v/\ell_i^2)n_i,\qquad v=V_i(x).
\]
Since \(n_i\cdot e_i=0\), \(n_i\cdot p_i=C_i\), and \(\|n_i\|^2=\ell_i^2\), the equations reduce *exactly* to
\[
 \dot v=-\kappa_i v,\qquad \dot s=\omega_i-\mu_i v.
\]
For \(x(0)=(1+\delta)p_i\), one has \(v(0)=C_i\delta\) and \(s(0)=A_i\delta\). Therefore
\[
 v(t)=C_i\delta e^{-\kappa_i t},\quad
 s(t)=\omega_i t+A_i\delta-\frac{\mu_iC_i}{\kappa_i}\delta(1-e^{-\kappa_i t}).
\]
The point \((1+\delta')p_{i+1}\) on the outgoing ray has coordinates \(v=C_i\delta'\) and \(s=1+B_i\delta'\). Consequently the exact first-crossing equation, in the local transverse crossing regime, is
\[
 \omega_i t=1+\delta\left[B_i e^{-\kappa_i t}-A_i+
 \frac{\mu_i C_i}{\kappa_i}(1-e^{-\kappa_i t})\right],
 \qquad \delta'=\delta e^{-\kappa_i t}.
\]

**2. Unique cancellation and exact return.** At \(\delta=0\), the flight time equals \(1/\omega_i\). For this same time to solve the crossing equation for every small nonzero \(\delta\), its bracket must vanish at \(t_i=1/\omega_i\). Since \(1-E_i>0\), this condition has the *unique* solution \(\mu_i=\mu_i^*\) displayed in the finding. Conversely this solution makes the outgoing point exactly \((1+E_i\delta)p_{i+1}\) at the fixed time. The unperturbed polygon crosses each radial switching section transversely, because its angular velocity there has the sign of \(\omega_i C_i>0\). Continuity of each affine flight implies that, after restricting \(|\delta|\) sufficiently, this is indeed the first next-ray crossing with no intervening ray or grazing event. Choosing a common small radius for the finitely many edges and composing yields the exact period \(P\) and multiplier \(R\) in the statement; on successive revolutions the amplitude is multiplied by \(R\).

**3. The explicit isochron foliation.** Let \(0\le t\le\omega_i^{-1}\), let \(\gamma_i(t)=p_i+\omega_i t e_i\) be the orbit point, and define the nonzero direction vector
\[
 w_i(t)=\left[A_i-\frac{\mu_i^*C_i}{\kappa_i}(1-e^{-\kappa_i t})\right]e_i
 +\frac{C_i}{\ell_i^2}e^{-\kappa_i t}n_i.
\]
The exact flow satisfies
\[
 \boxed{\Phi_t((1+\delta)p_i)=\gamma_i(t)+\delta w_i(t).}
\]
At the gluing endpoints \(w_i(0)=p_i\) and \(w_i(\omega_i^{-1})=E_i p_{i+1}\), so these line segments match at every ray (up to nonzero scalar reparameterization). For every fixed \(t\), the later trajectory of \(\gamma_i(t)+\delta w_i(t)\) is synchronized to that of \(\gamma_i(t)\): at all subsequent full-period times its signed amplitude decreases as \(R^m\delta\), and the intervening bounded affine flows preserve convergence. Therefore the line segment at fixed \(t\) lies in the exact asymptotic isochron, not merely in its tangent line. Its normal component relative to the edge is \(C_i e^{-\kappa_i t}/\ell_i^2\ne0\). Hence \((t,\delta)\mapsto\gamma_i(t)+\delta w_i(t)\) has nonzero Jacobian at \(\delta=0\), yielding a local coordinate strip. Together over the edges, these strips cover a neighborhood of the cycle; their fixed-phase straight segments give the **complete local isochron foliation** (with one-sided gluing at the switching rays). Distinct time phases have distinct asymptotic phase, proving local completeness and no double counting.

**4. Regular-polygon reduction.** For vertices of a centered regular polygon, \(A_i=-1/2\), \(B_i=1/2\), and \(C_i,\ell_i,\kappa_i\) are independent of \(i\). Thus
\[
 \mu_i^*=-\frac{\kappa}{2C}\frac{1+e^{-\kappa/\omega}}{1-e^{-\kappa/\omega}}
 =-\frac{\kappa}{2C}\coth(\kappa/(2\omega)),
\]
with all shears equal. The uniqueness established in Step 2 proves uniqueness also within the common-shear subfamily. This completes the proof.

## Verification
The included standalone `verify.py` uses no third-party dependencies. Run `python3 verify.py` to check randomly sampled and regular polygons of several sizes, both signs of small vertex-ray offsets, exact section equations, phase-independent flight times, multi-edge radial contraction, perturbations away from the unique shear, and the regular-polygon hyperbolic-cotangent formula. Finite numerical diagnostics corroborate only the enumerated test cases; the universal statement and first-crossing/isochron assertions follow from the preceding exact argument and local transversality.

## Relationship to prior work
T. Kai (2026) introduced the three-parameter affine polygonal oscillator and proved construction and local stability of the prescribed polygon, edgewise transverse decay, on-cycle periods and numerical tangential-shear effects. Those ingredients are used, not claimed as new. Its full sections on dynamics and simulations do **not** give an exact unique shear making perturbed radial flight times constant or an explicit nonlinear straight-line isochron foliation.

Y. Park, K. Shaw, H. Chiel and P. Thomas (2018, first preprint 2016) developed a general saltation/adjoint method to compute infinitesimal phase response curves of piecewise-smooth and piecewise-linear oscillators. The present exact **finite-amplitude** isochron construction and unique parameter formula for Kai's polygonal family are more specific than, and not an explicit statement of, that general linear theory. The general phase-response mechanism is established prior work. An unlocated equivalent construction elsewhere in hybrid-control or isochron literature is a residual bibliographic risk.

## Limitations
Results require simple origin-star-shaped polygons with all radial gaps below \(\pi\), positive \(\omega_i,\lambda_i\), free unrestricted real \(\mu_i\), and the specified transverse hybrid switching convention. The straight-line isochrons are **local**, not guaranteed globally. No general robustness against noise, perturbations of the switching law, trajectories far from the cycle, or arbitrary smooth oscillators is asserted. The uniqueness is for the *edgewise fixed-flight-time requirement*, not a classification of all conceivable shear configurations having other phase properties. Numerical tests alone do not establish uniqueness or the universal theorem. Historical priority is not independently certified.

## References
1. T. Kai, “Piecewise affine oscillators with polygonal limit cycles,” *International Journal of Dynamics and Control* 14, article 392 (2026). First public publication 2026-10-08. DOI: 10.1007/s40435-026-02340-6. Open access: https://link.springer.com/article/10.1007/s40435-026-02340-6.
2. Y. Park, K. M. Shaw, H. J. Chiel and P. J. Thomas, “The Infinitesimal Phase Response Curves of Oscillators in Piecewise Smooth Dynamical Systems,” *European Journal of Applied Mathematics* (2018); arXiv:1603.03503, first posted 2016-03-11. Open manuscript: https://arxiv.org/html/1603.03503v3.
