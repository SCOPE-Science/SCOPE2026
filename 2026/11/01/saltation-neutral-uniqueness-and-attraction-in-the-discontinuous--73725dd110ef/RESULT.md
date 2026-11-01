# Saltation-neutral uniqueness and attraction in the discontinuous generalized Chazy cylinder

## Finding
At the discontinuous member \(q=1\), \(k=2\) of the generalized Chazy equation, **each negative-energy surface carries exactly one nonconstant periodic orbit**. Its within-surface transverse Poincaré multiplier is
\[
\rho=\exp\left(-\int_0^{T_h}|x_h(t)|\,dt\right)\in(0,1),
\]
independent of the energy \(-h\), where \(h>0\). Every bounded forward trajectory on that surface approaches this orbit, and its period is \(T_h=h^{-1/4}T_1\). The full, saltation-corrected linearized return has Floquet multipliers \(1,1,\rho\) (with algebraic multiplicity). Its unique periodic orbit also obeys the exact central half-period symmetry \(\gamma_h(t+T_h/2)=-\gamma_h(t)\). Existence is imported from Llibre–Novaes–Valls; the uniqueness, attraction, saltation and multiplier conclusions are proved here.

## Assumptions and scope
The autonomous equation is the piecewise-smooth three-dimensional system
\[
\dot x=y,\quad \dot y=z,\quad
\dot z=-|x|z-2\operatorname{sgn}(x)y^2\quad(x\ne0),
\]
interpreted by **crossing (Filippov) solutions** at \(x=0\). Write
\[
H(x,y,z)=xz-\tfrac12y^2+x|x|y,\qquad S_h=\{H=-h\},\quad h>0.
\]
Every point on \(S_h\cap\{x=0\}\) satisfies \(y=\pm\sqrt{2h}\), so the one-sided normal speeds coincide and are nonzero. Thus these are genuine crossings, never sliding or grazing, and the forward and backward flows are unique on each negative-energy surface. A *bounded forward orbit* is one whose positive semiorbit remains in a compact subset of its energy surface. Distances and periods are measured in the original physical time. No claim is made for \(H\ge0\), the crossing-free differential inclusion elsewhere, or arbitrary unbounded orbits.

## Proof
**1. Exact polynomial leaf coordinates and crossing geometry.** Introduce the continuous, invertible triangular coordinate change \(w=z+|x|y\). On the two half-spaces the transformed vector field is
\[
\dot x=y,\quad\dot y=w-|x|y,\quad\dot w=-\operatorname{sgn}(x)y^2.
\]
Its globally defined first integral becomes the smooth polynomial \(H=xw-y^2/2\); on each side \(dH/dt=0\), and continuity preserves \(H\) through a crossing. The change is locally bi-Lipschitz (not claimed to be globally differentiable across the seam). On \(S_h\), \(dH\ne0\), and there are no equilibria. Setting \(U=x+w\), \(V=x-w\) gives
\[
V^2+2y^2-U^2=4h.
\]
Hence each \(S_h\) is a smooth cylinder \(\mathbb R\times S^1\). Its intersection with \(x=0\) consists of two smooth transverse crossing curves, where \(y=\pm\sqrt{2h}\). The jump \(F^+-F^-=(0,0,-2y^2)\) has zero normal component. In particular the seam carries no surface-flux defect.

**2. Strict contraction excludes extra cycles.** Let \(\Omega=dx\wedge dy\wedge dw\). Since \(dH\ne0\), fix the smooth positive leaf area form \(\omega_h\) uniquely up to choice of transverse volume normalization by \(dH\wedge\omega_h=\Omega\). On either side the ambient divergence is \(-|x|\), so conservation of \(H\) and the coarea identity imply the leafwise divergence identity
\[
\mathcal L_F\omega_h=-|x|\omega_h\qquad (x\ne0).
\]
The one-sided vector fields have identical normal components along the crossing set, so piecewise Stokes' theorem has **no extra seam term**. A contractible periodic Jordan curve on the cylinder would bound a compact disc; two distinct essential periodic curves would bound a compact annulus. For either hypothetical invariant region \(R\), the boundary is tangent to \(F\); consequently
\[
0=\int_{\partial R}\iota_F\omega_h
=\int_R(-|x|)\omega_h<0.
\]
The strict inequality holds since every nonempty open region on \(S_h\) contains points with \(x\ne0\). Hence there are no contractible cycles and at most one essential cycle. Llibre–Novaes–Valls, Theorem 1 for \(q=1\), establishes a periodic orbit on **every** negative-energy level. Therefore each \(S_h\) has exactly one periodic orbit \(\gamma_h\).

**3. Return-map multiplier with saltation.** At a transverse crossing the conventional saltation matrix is
\[
\mathcal S=I+\frac{(F^+-F^-)n^{\mathsf T}}{n^{\mathsf T}F^-},
\qquad n=(1,0,0)^{\mathsf T}.
\]
Because \(n^{\mathsf T}(F^+-F^-)=0\), \(\det\mathcal S=1\). The reverse crossing has the same determinant. Thus there is no impulsive determinant factor: the determinant of the full three-dimensional monodromy is precisely
\[
\det M_h=\exp\left(-\int_0^{T_h}|x_h(t)|\,dt\right)=\rho.
\]
The positive integral is nonzero because no nonconstant orbit can lie entirely in \(x=0\). Autonomous time translation gives one unit multiplier; the smooth noncritical first integral \(H\) gives a second unit multiplier on the energy-normal quotient. The last multiplier is \(\rho\), hence the within-leaf transverse return is strictly attracting. This does not assert semisimplicity of the two unit multipliers.

**4. Energy scaling and central symmetry.** The flow is covariant under the physical-time dilation
\[
(x(t),y(t),w(t))\longmapsto
(\lambda x(\lambda t),\lambda^2 y(\lambda t),\lambda^3 w(\lambda t)),\quad\lambda>0.
\]
It scales \(H\) by \(\lambda^4\), and scales the period by \(\lambda^{-1}\). The orbit on each level is unique, so \(T_h=h^{-1/4}T_1\). Moreover the integral \(\int |x|dt\) is invariant under this scaling, proving that \(\rho\) does not depend on \(h\). The transformed field is odd and \(H\) is even under \((x,y,w)\mapsto(-x,-y,-w)\). Thus central inversion maps the unique cycle to itself. It commutes with time evolution, has order two, and has no fixed point on \(S_h\). Its induced time shift on the cycle must equal half of the least period, proving \(\gamma_h(t+T_h/2)=-\gamma_h(t)\); the same identity transfers to \((x,y,z)\) because \(z=w-|x|y\) is odd under inversion.

**5. Bounded forward basin.** Any bounded forward orbit has a compact nonempty omega-limit on \(S_h\). There are no equilibria on this surface, including at the seam. Since all seam crossings are transverse and have continuous matched normal speeds, local crossing flowboxes allow the usual planar-cylinder Poincaré–Bendixson argument. Its omega-limit is therefore a periodic orbit. By uniqueness this is \(\gamma_h\), and the distance from the forward trajectory to \(\gamma_h\) tends to zero. No assertion is made that every forward orbit on this noncompact cylinder is bounded.

## Verification
Run `python check_chazy_q1.py` with SymPy installed. The exact symbolic checker verifies both half-space first-integral identities, the divergence, weighted energy and vector-field scaling, transverse matching of the seam-normal velocities, determinant-one saltation matrices in both crossing directions, the negative-energy seam condition, and central-inversion invariance. These local symbolic identities support but do not replace the global topological argument, the cited external periodic-orbit existence theorem, or the Poincaré–Bendixson theorem.

## Relationship to prior work
Llibre–Novaes–Valls (2023), Theorem 1, construct an invariant cylinder of periodic orbits for \(q=1,2,3\), including this discontinuous case, but do not establish that the periodic orbit is the **unique** cycle per negative-energy leaf, determine its saltation-corrected multiplier, or prove the bounded-basin conclusion. A related separately published result, *Uniqueness and leafwise attraction of the generalized Chazy periodic cylinder* (2026), proves analogous uniqueness and Floquet statements for **\(q\ge2\)**, explicitly excluding the discontinuous \(q=1\) regime. That previous theorem alone does not imply the present claim: it requires treating discontinuous Filippov crossings and checking a missing saltation determinant. Zhuang–Liu–Luo (2024) establish existence for arbitrary positive integer \(q\) at \(k=q+1\), according to their abstract; their complete text could not be inspected, and equivalence of a possible stronger claim there is an unresolved priority risk.

## Limitations
Existence is not independently reproved and relies on the 2023 theorem. There is no proof that all orbits on a noncompact energy cylinder are bounded, and no closed-form numerical value for the multiplier. The two unit Floquet multipliers need not be semisimple; convergence is leafwise only. The proof concerns the \(q=1,k=2\) crossing flow at negative energy, not sliding solutions on other levels. The 2024 paper's accessible abstract does not settle full-text priority; this claim has not undergone independent scientific audit.

## References
1. J. Llibre, D. D. Novaes and C. Valls, *Existence of a cylinder foliated by periodic orbits in the generalized Chazy differential equation*, Chaos 33 (2023), 073104. First public arXiv version 2023-06-30, https://arxiv.org/abs/2307.00087; DOI:10.1063/5.0138309. Theorem 1 and its proof in Section 3 were read.
2. *Uniqueness and leafwise attraction of the generalized Chazy periodic cylinder* (2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-uniqueness-and-leafwise-attraction-of-the-generalized-chazy-peri--027cb0928569. Its statement and proof expressly assume integer \(q\ge2\).
3. Z. Zhuang, C. Liu and J. Luo, *On the periodic behavior of the generalized Chazy differential equation*, Chaos 34 (2024), 113106; DOI:10.1063/5.0209050. Only the abstract was accessible for the comparison.
