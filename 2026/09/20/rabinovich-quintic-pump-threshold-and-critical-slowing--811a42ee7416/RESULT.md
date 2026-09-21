# Quintic pump threshold and critical slowing in the Rabinovich wave system

## Result

Consider the Rabinovich three-wave system
\[
\dot x=h y-\nu_1x-yz,\qquad
\dot y=h x-\nu_2y+xz,\qquad
\dot z=xy-\nu_3 z,
\]
with \(h,\nu_1,\nu_2,\nu_3>0\). Put
\[
h_c=\sqrt{\nu_1\nu_2}.
\]

**Theorem.**

1. The origin is globally asymptotically stable exactly for
\[
\boxed{h\le h_c}.
\]
For \(h<h_c\) convergence is exponential. For \(h>h_c\) the origin is linearly unstable.

2. At the critical pump \(h=h_c\), the loss of hyperbolicity is structurally degenerate. Writing
\[
p=\sqrt{\nu_1},\qquad q=\sqrt{\nu_2},\qquad D=p^2+q^2
\]
and introducing
\[
s=\frac{qx+py}{D},\qquad v=\frac{px-qy}{D},
\]
the critical equations become
\[
\dot s=vz,\qquad
\dot v=-Dv-sz,
\]
\[
\dot z=pq\,s^2+(p^2-q^2)sv-pq\,v^2-\nu_3 z.
\]
A local center manifold has
\[
v=-\frac{pq}{\nu_3D}s^3+O(s^5),\qquad
z=\frac{pq}{\nu_3}s^2+O(s^4),
\]
and the reduced equation is
\[
\boxed{
\dot s=-\frac{p^2q^2}{\nu_3^2D}s^5+O(s^7).
}
\]
Thus the cubic pitchfork coefficient vanishes identically: the pump threshold is a
quintic, rather than generic cubic, \(\mathbb Z_2\)-symmetric pitchfork.

3. Consequently, every critical trajectory outside the two-dimensional strong-stable
manifold of the origin has the algebraic asymptotics
\[
s(t)\sim \pm(4\kappa t)^{-1/4},
\qquad
\kappa=\frac{\nu_1\nu_2}{\nu_3^2(\nu_1+\nu_2)}.
\]
In the original variables,
\[
t^{1/4}x(t)\to
\pm\sqrt{\nu_2}
\left(\frac{\nu_3^2(\nu_1+\nu_2)}{4\nu_1\nu_2}\right)^{1/4},
\]
\[
t^{1/4}y(t)\to
\pm\sqrt{\nu_1}
\left(\frac{\nu_3^2(\nu_1+\nu_2)}{4\nu_1\nu_2}\right)^{1/4},
\]
while the third wave has the parameter-reduced law
\[
\boxed{
t^{1/2}z(t)\to\frac{\sqrt{\nu_1+\nu_2}}2.
}
\]
Trajectories on the strong-stable manifold decay exponentially.

4. If \(h=h_c+\varepsilon\) with \(\varepsilon>0\) small, the two nonzero equilibria
satisfy
\[
s_\pm=
\pm \nu_3^{1/2}
\left(\frac{2\varepsilon}{pq}\right)^{1/4}(1+o(1)).
\]
Hence the physical order parameter turns on with a quartic-root law. This agrees
with the exact equilibrium formulas but identifies their local mechanism: the first
nonzero saturation term in the center dynamics is fifth order.

## Proof

For
\[
E=x^2+y^2
\]
one has the exact identity
\[
\dot E
=4hxy-2\nu_1x^2-2\nu_2y^2.
\]
At \(h=h_c=pq\),
\[
\boxed{\dot E=-2(px-qy)^2\le0.} \tag{1}
\]
For \(h<h_c\), the quadratic form on the right-hand side of the general energy
identity is negative definite, so \(x\) and \(y\) decay exponentially. The equation
for \(z\) is a stable scalar equation forced by \(xy\), hence \(z\) also decays
exponentially.

At \(h=h_c\), (1) bounds \(x,y\) globally. Since
\[
|xy|\le \frac12E(0),
\]
variation of constants gives
\[
|z(t)|
\le e^{-\nu_3t}|z(0)|
+\frac{E(0)}{2\nu_3}\bigl(1-e^{-\nu_3t}\bigr),
\]
so every forward orbit is bounded and global.

The linear change of variables displayed above has inverse
\[
x=qs+pv,\qquad y=ps-qv.
\]
Direct substitution at \(h=pq\) gives the critical system in item 2 and
\[
E=D(s^2+v^2),\qquad \dot E=-2D^2v^2.
\]
The largest invariant subset of \(\{v=0\}\) is the \(z\)-axis: if \(v=0\), then
\(\dot v=-sz\); a nonzero constant \(s\) would require \(z=0\), but then
\(\dot z=pq\,s^2>0\). Thus LaSalle's invariance principle gives
\(s(t),v(t)\to0\). The stable scalar equation
\[
\dot z+\nu_3z=xy
\]
then gives \(z(t)\to0\). Small initial \(E\) and the displayed bound on \(z\)
also give Lyapunov stability. Hence the origin is globally asymptotically stable
at equality.

For \(h>h_c\), the \(x,y\) block of the Jacobian at the origin has determinant
\(\nu_1\nu_2-h^2<0\), so it has a positive real eigenvalue. The origin is therefore
unstable. This proves the exact global threshold in item 1.

At criticality the linear eigenvalues in \((s,v,z)\) are
\[
0,\qquad -D,\qquad -\nu_3.
\]
The system is invariant under \((s,v,z)\mapsto(-s,-v,z)\). Write a center
manifold as \(v=V(s)\), \(z=Z(s)\). The invariance equations, through the first
nonzero orders, give
\[
Z(s)=\frac{pq}{\nu_3}s^2+O(s^4),\qquad
V(s)=-\frac{pq}{\nu_3D}s^3+O(s^5).
\]
Since \(\dot s=V(s)Z(s)\),
\[
\dot s=-\frac{p^2q^2}{\nu_3^2D}s^5+O(s^7),
\]
which proves item 2.

The scalar asymptotic follows by integrating
\[
\frac{d}{dt}s^{-4}=4\kappa+o(1)
\]
on either side of the origin. Standard stable-foliation tracking transfers this
leading behavior to every trajectory not on the strong-stable manifold. Substitution
of the center-manifold expansions gives item 3.

Finally set \(h=pq+\varepsilon\). In the fixed critical coordinates,
\[
\dot s=\frac{2\varepsilon pq}{D}\,s+
\left(z+\frac{\varepsilon(p^2-q^2)}D\right)v.
\]
The reduced equation therefore has the unfolding
\[
\dot s=
\frac{2pq}{D}\,\varepsilon s
-\frac{p^2q^2}{\nu_3^2D}s^5
+O(\varepsilon^2|s|+\varepsilon|s|^3+|s|^7).
\]
Balancing the leading terms yields
\[
s_\pm^4\sim \frac{2\nu_3^2}{pq}\varepsilon,
\]
which is item 4. Equivalently, the exact nonzero equilibria have
\[
z_0=\sqrt{h^2-\nu_1\nu_2},
\]
\[
x_\pm^2=\frac{\nu_3z_0(h-z_0)}{\nu_1},\qquad
y_\pm^2=\frac{\nu_3z_0(h+z_0)}{\nu_2},\qquad
x_\pm y_\pm=\nu_3z_0,
\]
with \(x_\pm,y_\pm\) of the same sign. Expanding these formulas gives the same
quartic-root onset.

## Context and originality

Pikovskii, Rabinovich and Trakhtengerts introduced the dissipative three-wave
system and proved that below the pump threshold \(h<\sqrt{\nu_1\nu_2}\) all
trajectories approach the origin, while above it two nonzero equilibria appear and
the origin is unstable. Their exact equilibrium formulas already contain the
quartic-root branch geometry implicitly. Later literature routinely describes this
event as a pitchfork bifurcation.

Kuznetsov et al. restate the normalized system as a generalized Lorenz system with
\(r=h^2/(\nu_1\nu_2)\) and likewise state global asymptotic stability for \(r<1\),
not the equality case. Pusuluri, Pikovsky and Shilnikov describe the same threshold
as a pitchfork while focusing on the later global bifurcations that organize chaos.

The contribution claimed here is narrower: the exact equality case, the structural
vanishing of the cubic center coefficient, the resulting fifth-order saturation,
and the explicit \(t^{-1/4}\) critical relaxation law. Searches for Rabinovich
center-manifold reductions, degenerate or quintic pitchforks, quartic-root onset,
critical exponents, and algebraic relaxation did not locate these statements in
the inspected literature. To the best of our knowledge, this critical-threshold
normal form and its decay law have not been stated previously.

Llibre, Messias and da Silva give global phase portraits for selected parameter
sets and special invariant/integrable cases of a sign-equivalent Rabinovich
system, but the accessible abstract does not indicate the pump-threshold normal
form treated here. Chiş and Puta explicitly separate the original dissipative
pump system from the conservative nonlinear core they analyze geometrically, so
their equilibrium-stability results do not cover this threshold theorem.

## Limitations

The theorem assumes positive damping parameters and positive pump amplitude. The
critical asymptotic formulas in item 3 apply off the strong-stable manifold; that
exceptional two-dimensional manifold has exponential decay instead. The result
does not classify the later Hopf, homoclinic, or chaotic regimes above threshold.

The exact nonzero-equilibrium formulas and the existence of a pitchfork are prior
knowledge and are not claimed as new. The novelty claim concerns the degenerate
quintic local mechanism, the critical algebraic decay, and closure of the global
stability statement at equality.

The most important residual prior-coverage risk is A. S. Pikovskii and
M. I. Rabinovich, *Stochastic behavior of dissipative systems*, Soc. Sci. Rev. C:
Math. Phys. Rev. 2 (1981), 165--208. Its full text was not inspected; because
it is a broad review by the original authors, it could contain a more detailed
threshold asymptotic analysis than the 1978 paper. Older Russian-language analyses
of the same three-wave instability present a similar residual risk.

## Verification

The compact symbolic verifier in `artifacts/verify_critical_threshold.py` checks
the transformed critical equations, the exact energy identity, the leading
center-manifold invariance equations, and the quintic coefficient. Its recorded
output is in `artifacts/verification.txt`.

## References

1. A. S. Pikovskii, M. I. Rabinovich and V. Yu. Trakhtengerts,
   *Onset of stochasticity in decay confinement of parametric instability*,
   Sov. Phys. JETP 47 (1978), 715--719.
   https://www.jetp.ras.ru/cgi-bin/dn/e_047_04_0715.pdf

2. N. V. Kuznetsov, G. A. Leonov, T. N. Mokaev, A. Prasad and M. D. Shrimali,
   *Finite-time Lyapunov dimension and hidden attractor of the Rabinovich system*,
   Nonlinear Dynamics 92 (2018), 267--285.
   https://doi.org/10.1007/s11071-018-4054-z

3. K. Pusuluri, A. Pikovsky and A. Shilnikov,
   *Unraveling the Chaos-Land and Its Organization in the Rabinovich System*,
   in Advances in Dynamics, Patterns, Cognition (2017), 41--60.
   https://doi.org/10.1007/978-3-319-53673-6_4
   Preprint: https://arxiv.org/abs/1806.01306

4. J. Llibre, M. Messias and P. R. da Silva,
   *On the global dynamics of the Rabinovich system*,
   Journal of Physics A 41 (2008), 275210.
   https://doi.org/10.1088/1751-8113/41/27/275210

5. O. Chiş and M. Puta,
   *The Dynamics of Rabinovich system*, arXiv:0710.4583.
   https://arxiv.org/abs/0710.4583
