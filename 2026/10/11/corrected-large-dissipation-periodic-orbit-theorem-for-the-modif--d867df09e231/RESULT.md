# Corrected large-dissipation periodic-orbit theorem for the modified Nosé–Hoover oscillator

## Finding
Consider
\[
\dot x=y,\qquad \dot y=-x-yz,\qquad \dot z=\alpha(y^2-1-\varepsilon z),
\]
with fixed \(\alpha>0\) and \(\varepsilon>0\). The published large-dissipation proof introduces the surface
\[
M_{1/\varepsilon}=\left\{z=\frac{y^2-1}{\varepsilon}\right\}
\]
and treats the planar vector field obtained by substitution as though it were the flow induced by the full system. It is not. Define
\[
Q=z-\frac{y^2-1}{\varepsilon}.
\]
Then the exact normal equation is
\[
\dot Q=-\alpha\varepsilon Q+\frac{2}{\varepsilon}y(x+yz).
\]
Consequently,
\[
\dot Q\big|_{Q=0}=\frac{2y}{\varepsilon^2}\bigl(\varepsilon x+y^3-y\bigr),
\]
which is generically nonzero. In fact, the only complete trajectory contained in \(M_{1/\varepsilon}\) is \((0,0,-1/\varepsilon)\). Thus the nonconstant planar periodic orbit constructed on that nullcline cannot itself be a periodic orbit of the full three-dimensional system, and a closed orbit of the substituted planar vector field is not automatically a section of an invariant torus.

The intended large-dissipation conclusion nevertheless has a rigorous repair that is stronger. For every fixed \(\alpha>0\), there exists \(\varepsilon_0(\alpha)\) such that every \(\varepsilon>\varepsilon_0(\alpha)\) admits an asymptotically stable nonconstant periodic orbit of the full system. As \(\varepsilon\to\infty\), its \((x,y)\)-projection converges to
\[
x^2+y^2=\frac43.
\]
On a compact annulus containing this branch, the attracting slow manifold has expansion
\[
z=\frac{y^2-1}{\varepsilon}+\frac{2xy}{\alpha\varepsilon^2}+O(\varepsilon^{-3}).
\]

## Assumptions and scope
The claim is local to the large-\(\varepsilon\) regime and assumes fixed \(\alpha>0\). It proves existence and asymptotic stability of one perturbative periodic branch near radius \(2/\sqrt3\). It does not classify all periodic orbits, invariant tori, chaotic sets, or global basins for finite \(\varepsilon\), and it makes no claim that the numerical recurrent sets reported at small \(\varepsilon\) disappear.

## Proof
First, differentiating \(Q=z-(y^2-1)/\varepsilon\) along the exact vector field gives
\[
\dot Q=\alpha(y^2-1-\varepsilon z)-\frac{2y}{\varepsilon}(-x-yz)
=-\alpha\varepsilon Q+\frac{2}{\varepsilon}y(x+yz).
\]
This proves the stated normal defect. If a complete trajectory were contained in \(Q=0\), then \(\dot z=0\), so \(z\) and hence \(y^2\) would be constant. If \(y=0\), then \(\dot y=-x\) forces \(x=0\), giving the equilibrium. If \(y^2>0\), continuity makes \(y\) a nonzero constant; then \(\dot x=y\) makes \(x\) nonconstant, while \(\dot y=0\) requires \(x=-yz\) to be constant, a contradiction.

For the repair, set \(\iota=1/\varepsilon\). The system becomes
\[
\dot x=y,\qquad \dot y=-x-yz,\qquad
\iota\dot z=\alpha\bigl(\iota(y^2-1)-z\bigr).
\]
At \(\iota=0\), the critical manifold \(z=0\) is normally hyperbolic and attracting because the fast normal derivative is \(-\alpha<0\). Restrict attention to a compact annulus containing \(x^2+y^2=4/3\). Fenichel persistence therefore supplies a locally invariant attracting slow manifold \(z=h_\iota(x,y)\) for all sufficiently small positive \(\iota\).

Insert
\[
h_\iota=\iota h_1+\iota^2h_2+O(\iota^3)
\]
into the invariance equation. At leading order, \(h_1=y^2-1\). At the next order, the derivative of \(h_1\) along the unperturbed harmonic oscillator is \(-2xy\), while the fast relaxation contributes \(-\alpha h_2\); hence
\[
h_2=\frac{2xy}{\alpha}.
\]
Thus
\[
h_\iota=\iota(y^2-1)+\frac{2\iota^2}{\alpha}xy+O(\iota^3),
\]
and the reduced slow flow is
\[
\dot x=y,\qquad
\dot y=-x-\iota y(y^2-1)-\frac{2\iota^2}{\alpha}xy^2+O(\iota^3).
\]

Let \(E=(x^2+y^2)/2\) and \(r=\sqrt{x^2+y^2}\). To first order,
\[
\dot E=-\iota y^2(y^2-1)+O(\iota^2).
\]
Averaging on the unperturbed circle \(x=r\cos t\), \(y=-r\sin t\) gives
\[
\langle y^2\rangle=\frac{r^2}{2},\qquad
\langle y^4\rangle=\frac{3r^4}{8},
\]
so the averaged radial equation is
\[
\dot r=\iota\frac{r(4-3r^2)}8+O(\iota^2).
\]
Its positive zero \(r_*=2/\sqrt3\) is simple, with derivative \(-1\) for the leading averaged vector field. The standard first-order averaging theorem therefore gives a nearby attracting periodic orbit of the reduced flow for all sufficiently small positive \(\iota\). Normal attraction of the Fenichel manifold adds a stable transverse direction, so the corresponding periodic orbit of the full three-dimensional system is asymptotically stable. Replacing \(\iota\) by \(1/\varepsilon\) yields the stated theorem and expansion.

## Verification
The standalone verifier `verify_modified_nose_hoover.py` symbolically reconstructs the exact \(Q\)-equation, its restriction to the nullcline, the first two slow-manifold coefficients, the averaged radial polynomial, its positive zero, and the negative derivative at that zero. These computations are algebraic checks only; existence and stability use the stated Fenichel and averaging theorems on a compact annulus.

## Relationship to prior work
Han, Deng, and Yang prove global return/\(\omega\)-limit results for small \(\varepsilon\) and state that for sufficiently large \(\varepsilon\) there is either an invariant torus or a stable periodic orbit. Their large-\(\varepsilon\) argument, on pp. 7294–7295, substitutes the \(z\)-nullcline into the vector field and applies a planar continuation calculation that selects radius \(2/\sqrt3\). The exact normal-defect calculation above shows why that substitution is not an invariant reduction. The corrected fast-slow argument preserves the same first-order radius selection but places it on the true attracting slow manifold and gives a definite stable periodic orbit rather than an either/or alternative.

A later analytical study of a different dissipative Nosé–Hoover-derived oscillator uses averaging to prove periodic-orbit and torus results, but its vector field and perturbation regime differ from the model here; it does not supply this nullcline correction or this large-\(\varepsilon\) theorem. Searches for the source title, the nullcline reduction, and equivalent large-dissipation formulations did not locate a published correction that implies the result stated here.

## Limitations
The proof is asymptotic and does not provide an explicit numerical value of \(\varepsilon_0(\alpha)\). The displayed slow-manifold expansion is local and uniform only on a fixed compact annulus around the selected cycle. Standard geometric singular perturbation and averaging hypotheses are invoked rather than reproved. Unindexed corrections or later work could reduce the originality claim; no such source was found in the checked literature.

## References
1. Q. Han, B. Deng, and X.-S. Yang, “The existence of \(\omega\)-limit set for a modified Nosé–Hoover oscillator,” *Discrete and Continuous Dynamical Systems - B* 27 (2022), 7275–7300. DOI: 10.3934/dcdsb.2022043.
2. C. Kuehn, *Multiple Time Scale Dynamics*, Springer, 2015. See the persistence theory for normally hyperbolic slow manifolds.
3. J. A. Sanders, F. Verhulst, and J. Murdock, *Averaging Methods in Nonlinear Dynamical Systems*, 2nd ed., Springer, 2007. See first-order averaging near a family of periodic orbits.
4. M. Messias and M. R. Cândido, “Analytical results on the existence of periodic orbits and canard-type invariant torus in a simple dissipative oscillator,” *Chaos, Solitons & Fractals* 183 (2024), 114845. DOI: 10.1016/j.chaos.2024.114845.
