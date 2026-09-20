# Scientific review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness — PASS

For the dissipative Rabinovich three-wave system, differentiating
\(E=x^2+y^2\) gives
\[
\dot E=4hxy-2\nu_1x^2-2\nu_2y^2.
\]
At \(h=\sqrt{\nu_1\nu_2}\) this factors exactly as
\[
\dot E=-2(\sqrt{\nu_1}x-\sqrt{\nu_2}y)^2.
\]
This supplies global boundedness of \(x,y\); the stable scalar equation for \(z\)
then supplies global boundedness of the full orbit. LaSalle reduction was checked
carefully: the largest invariant subset of the zero-dissipation plane is the
\(z\)-axis, not merely the origin. LaSalle therefore yields \(x,y\to0\), after
which variation of constants yields \(z\to0\). A direct small-data bound gives
Lyapunov stability. For \(h>\sqrt{\nu_1\nu_2}\), the \(x,y\) Jacobian block has
negative determinant and hence a positive eigenvalue, establishing the converse.

The critical coordinate change was independently recomputed. It gives one zero
eigenvalue and two stable eigenvalues, and the center-manifold invariance equations
force
\[
z=(pq/\nu_3)s^2+O(s^4),\qquad
v=-(pq/(\nu_3D))s^3+O(s^5).
\]
Their product gives the nonzero fifth-order coefficient
\(-p^2q^2/(\nu_3^2D)\). The symbolic artifact returns zero residual for the
critical transformed equations, energy identity, leading invariance equations,
and quintic coefficient. The \(t^{-1/4}\) law follows from the scalar reduced
equation, while the original-variable constants follow by substitution.

The post-threshold quartic-root branch was checked both from the reduced unfolding
and from the exact equilibrium equations. The two calculations agree.

## Originality — PASS, narrowly scoped

The 1978 paper of Pikovskii, Rabinovich and Trakhtengerts already proves global
attraction to the origin for the strict subthreshold regime and gives the exact
nonzero equilibria above threshold. Those facts, and the existence of a
pitchfork, are prior work and are not claimed as new.

Kuznetsov et al. (2018) state global asymptotic stability for the normalized
parameter \(r<1\) and treat hidden attractors for larger forcing. Pusuluri,
Pikovsky and Shilnikov describe the same first transition as a pitchfork and
focus on later homoclinic, heteroclinic and chaotic organization. The inspected
sources did not state the equality-case global theorem, a vanishing cubic
center coefficient, a fifth-order reduced equation, or the explicit
\(t^{-1/4}\) critical relaxation law.

Searches using exact and synonymous language—Rabinovich critical pump, center
manifold, normal form, degenerate/quintic pitchfork, quartic-root onset, critical
exponent, and algebraic relaxation—did not locate a prior statement of this
combination. The exact equilibrium formulas make the quartic-root branch
recoverable by expansion, so the bare branch scaling is not treated as an
independent originality claim; the claimed contribution is the structural
quintic mechanism and its critical dynamics.

The main residual risk is A. S. Pikovskii and M. I. Rabinovich, *Stochastic
behavior of dissipative systems*, Soc. Sci. Rev. C: Math. Phys. Rev. 2 (1981),
165--208. The full text was not inspected. It is especially relevant because it
is a broad review by the original authors and may contain a more detailed
threshold analysis. Older Russian-language work on the same three-wave
instability is another residual coverage risk. Llibre--Messias--da Silva (2008)
was inspected at abstract level for its scope; it treats global phase portraits
for selected parameter sets and special invariant/integrable cases, but the
accessible material does not establish the present threshold normal form.

## Value — PASS

The result changes the interpretation of the first pump threshold. A generic
supercritical pitchfork has cubic saturation and \(t^{-1/2}\) critical decay.
Here the cubic coefficient vanishes identically throughout the positive damping
family, the first saturation is fifth order, and generic critical decay is
\(t^{-1/4}\). This gives a concrete mechanism for unusually slow relaxation at
the parametric-instability threshold and explains the quartic-root onset already
hidden in the classical equilibrium formulas.

The exact equality-case global stability result also closes the strict
subthreshold statement at the physically distinguished pump threshold.

## Scientific limitations

All damping parameters and the pump are assumed positive. The algebraic asymptotic
holds off the two-dimensional strong-stable manifold; trajectories on that
manifold decay exponentially. No claim is made about the later Hopf, homoclinic,
or chaotic transitions. Originality is asserted only to the best of our knowledge,
with the 1981 review and older language-specific literature as the principal
unresolved coverage risks.
