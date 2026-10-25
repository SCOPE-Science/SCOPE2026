# Uniqueness, strict crossing stability and an energy-invariant multiplier for the discontinuous generalized Chazy cylinder

## Finding
For the discontinuous generalized Chazy equation at \(q=1\) and \(k=2\), **every negative first-integral level has exactly one geometrically distinct primitive periodic orbit**. This orbit is exponentially orbitally attracting *within its two-dimensional level*, and every other bounded positive semiorbit on that level converges to it. The three Floquet multipliers, counted algebraically, are
\[
 1,\qquad 1,\qquad \mu_* = \exp\!\left(-\int_0^{T_h}|x_h(t)|\,dt\right)\in(0,1),
\]
where the strict multiplier \(\mu_*\) is identical for every negative energy \(-h\). The original-time minimal periods obey
\[
 T_h = h^{-1/4} T_1,\qquad h>0.
\]
The period scaling is already implied by the symmetry in the originating literature; the new conclusions are uniqueness, strict stability through the discontinuity, and the global leafwise bounded-orbit basin. The single nontrivial multiplier is not claimed to have a closed numerical value.

## Assumptions and scope
The phase state is \((x,y,z)\in\mathbb R^3\), with the Filippov crossing interpretation of
\[
 \dot x=y,\qquad \dot y=z,\qquad
 \dot z=-|x|z-2\operatorname{sgn}(x)y^2
 \quad(x\ne0).
\]
The vector field's value at \(x=0\) is interpreted by the unique transverse crossing trajectories; it is not a sliding system on the negative levels. The first integral is
\[
 H(x,y,z)=xz-\frac12y^2+x|x|y.
\]
For each real \(h>0\), put \(S_h=\{H=-h\}\). A bounded forward orbit means a positive semiorbit contained in a compact subset of \(S_h\), not merely one with a bounded projection. The result does not assert global boundedness of all trajectories.

The existence of at least one primitive cycle on every \(S_h\) is a published theorem (Llibre–Novaes–Valls, 2023, Theorem 1, discontinuous \(q=1\) case). The assertion here includes no new existence certificate and makes no claim for zero or positive integral levels or for parameters other than \(q=1,k=2\).

## Proof
**1. Invariant smooth cylinder and transverse crossings.** On the two open half-spaces define \(s=\operatorname{sgn}(x)\). In either sector the vector field is
\[
 X_s=(y,z,-sxz-2sy^2),\qquad
 H_s=xz-\tfrac12y^2+sx^2y.
\]
Direct differentiation gives \(X_s(H_s)=0\). The function \(H\) is globally \(C^1\) and continuous across \(x=0\). Its gradient cannot vanish on \(S_h\): since \(H_z=x\), a critical point would satisfy \(x=0\), then \(H_y=-y\) gives \(y=0\), contradicting \(H=-h\). In fact \(H=-h\) and \(x=0\) force \(y=\pm\sqrt{2h}\ne0\). Hence every meeting with the switching plane is strictly transverse, with equal incoming and outgoing normal velocity \(X_x=y\). Such crossings are locally unique and have continuous, piecewise-smooth dependence on initial data. There is no sliding or grazing on \(S_h\).

The continuous, locally bi-Lipschitz coordinate change \(w=z+|x|y\) makes \(H=xw-y^2/2\). With \(U=x+w\) and \(V=x-w\), the equation for \(S_h\) is \(V^2+2y^2-U^2=4h\). Parametrizing the ellipse for each \(U\in\mathbb R\) shows that \(S_h\) is a regular cylinder \(\mathbb R\times S^1\), with no equilibria. The two switching curves are embedded lines on this cylinder.

**2. Exact crossing Jacobian and coarea-area decay.** On either half-space the three-dimensional divergence is \(\nabla\!\cdot X_s=-|x|\). Let \(\Omega=dx\wedge dy\wedge dz\) and equip the regular leaf with its positive coarea area form \(\omega_h\), obtained from \(dH\wedge\omega_h=\Omega\). In a smooth sector, first-integral conservation and the Liouville identity imply \(\mathcal L_X\omega_h=-|x|\omega_h\).

The possible distributional contribution at \(x=0\) must be checked, because ordinary smooth-flow Liouville theory does not directly apply. The one-sided fields there are
\[
 X_-=(y,z,2y^2),\qquad X_+=(y,z,-2y^2).
\]
For a crossing from \(x<0\) to \(x>0\), the saltation matrix is
\[
 S_{-+}=I+\frac{(X_+-X_-)e_x^{\mathsf T}}{y}
       =I-4y\,e_z e_x^{\mathsf T}.
\]
For the reverse crossing, \(S_{+-}=I+4y\,e_z e_x^{\mathsf T}\). Both are rank-one shears with determinant \(1\); here \(y\ne0\). They also preserve the covector \(dH=(z,-y,0)\) at the switch and map the incoming vector to the outgoing vector. Thus the induced coarea area has **no multiplicative jump**. Equivalently, the jump \(X_+-X_-\) is tangent to the switching curve in \(S_h\) and has zero discontinuity of normal flux. As a distribution on \(S_h\), therefore,
\[
 \mathcal L_X\omega_h=-|x|\omega_h,
\]
with no interface delta term. The area Jacobian along any finite collection of transverse crossings and smooth arcs is exactly \(\exp(-\int |x(t)|dt)\).

**3. Uniqueness.** A periodic trajectory is an embedded circle because the piecewise-smooth crossing flow has uniqueness, and it cannot lie wholly in \(x=0\). Suppose a periodic circle were contractible in \(S_h\). It would bound a compact disk \(D\) in the cylinder. If two distinct essential periodic circles existed, they would bound a compact annulus \(D\). Cut \(D\) along its finitely many switching arcs and apply the surface divergence theorem on each piece. The internal interface fluxes cancel by the one-sided normal-flux identity in step 2, and the external boundary flux vanishes because all boundary components are trajectories. Consequently
\[
 0=\int_{\partial D}\iota_X\omega_h
   =-\int_D |x|\omega_h<0,
\]
a contradiction: the interior of a two-dimensional disk or annulus cannot be contained in \(x=0\). Thus no contractible periodic circle exists and there is **at most one** essential circle. The previously established existence gives exactly one primitive orbit on every \(S_h\).

**4. Stability, exact spectrum and time scaling.** For the Poincaré map on a one-dimensional transverse section within \(S_h\), the derivative at the cycle is the area contraction from step 2:
\[
 \mu_h=\exp\!\left(-\int_0^{T_h}|x_h(t)|dt\right),\qquad0<\mu_h<1.
\]
The integral is strictly positive because the cycle cannot be contained in \(x=0\). This makes the cycle exponentially orbitally attracting inside its leaf. For the full three-dimensional crossing return, the autonomous flow direction and the invariant-energy quotient each contribute a unit multiplier; the remaining one is \(\mu_h\). A size-two Jordan block at eigenvalue \(1\) is not excluded.

For every \(a>0\), if \((x(t),y(t),z(t))\) is a solution, then
\[
 \big(a x(at),\ a^2y(at),\ a^3z(at)\big)
\]
is another solution. The first integral scales by \(a^4\), and the time integral of \(|x|\) is unchanged. Uniqueness identifies the rescaled cycle with the sole cycle on the new energy level. Setting \(a=h^{1/4}\) proves both the period formula and \(\mu_h=\mu_*\).

**5. Bounded forward orbits.** The transverse switch gives local flow boxes on \(S_h\) exactly as for an ordinary planar flow, and compact orbit segments cross only finitely many times. Therefore the usual planar Poincaré–Bendixson argument applies to this continuous crossing flow on the cylinder. A bounded positive semiorbit has a nonempty compact omega limit set; there are no equilibria on \(S_h\), so its omega limit is periodic. By step 3 that periodic orbit must be the unique cycle. The distance to that cycle tends to zero. This conclusion does not assert convergence to a distinguished phase point or attraction across energy levels.

## Verification
The standalone `check_chazy_discontinuous.py` uses exact symbolic polynomial operations to verify the two sector conservation identities, both divergence identities, the weighted scaling covariance, and both saltation matrices' determinant, vector-field matching, and first-integral-covector preservation. The recorded replay printed `PASS: 18 exact algebraic identity checks`. These calculations check the nonstandard algebra at the switch, but are not substitutes for the global area argument, topology, or the published existence theorem. Run with `python check_chazy_discontinuous.py` after installing SymPy (see `requirements.txt`).

## Relationship to prior work
Llibre, Novaes and Valls (2023, arXiv:2307.00087, Theorem 1 and Section 3.1) prove existence of a crossing periodic cylinder specifically at \(q=1\). Their argument uses a trapping region and a return-map zero and does not state uniqueness or compute the crossing Floquet spectrum. The 2024 Zhuang–Liu–Luo article supplies an all-positive-integer existence result, according to its abstract and available publisher preview; its unavailable complete text leaves a historical-priority uncertainty.

A separately published uniqueness-and-attraction result for the same generalized Chazy family treats **only integers \(q\ge2\)** and applies ordinary \(C^1\) Liouville theory. It excludes the \(q=1\) discontinuity by hypothesis, and therefore does not establish the saltation identity, its lack of an interface contraction defect, or the resulting uniqueness and basin at the discontinuous parameter. The method here necessarily verifies that interface condition rather than extending the smoother theorem by notation alone.

## Limitations
No finite-time bounds on convergence, closed form for \(\mu_*\), or proof that all forward trajectories in a noncompact energy cylinder remain bounded is claimed. The two unit Floquet multipliers do not make the cylinder asymptotically stable in the full phase space; the first integral prevents transport across leaves. The analysis is for Filippov transverse crossing and not for alternative switching rules or perturbed systems with sliding. The 2024 sequel's full text was inaccessible, so complete historical priority is not established. Independent audit has not been performed.

## References
1. J. Llibre, D. D. Novaes, C. Valls, *Existence of a cylinder foliated by periodic orbits in the generalized Chazy differential equation*, **Chaos** 33 (2023), 073104, arXiv:2307.00087v1 (posted 2023-06-30), doi:10.1063/5.0138309. Theorem 1 and Section 3.1.
2. Z. Zhuang, C. Liu, J. Luo, *On the periodic behavior of the generalized Chazy differential equation*, **Chaos** 34 (2024), 113106, doi:10.1063/5.0209050. Only abstract and publisher preview inspected.
3. *Uniqueness and leafwise attraction of the generalized Chazy periodic cylinder*, published scientific report, 2026, available at https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-uniqueness-and-leafwise-attraction-of-the-generalized-chazy-peri--027cb0928569 . Covers \(q\ge2\) and expressly excludes \(q=1\).
