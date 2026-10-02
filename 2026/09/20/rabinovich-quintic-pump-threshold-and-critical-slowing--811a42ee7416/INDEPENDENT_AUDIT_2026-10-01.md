# Independent audit — 2026-10-01

## Final claim

At the first pump threshold \(h=\sqrt{\nu_1\nu_2}\) of the dissipative Rabinovich three-wave system, the origin remains globally asymptotically stable, the center dynamics have a nonzero quintic leading term, generic critical trajectories decay like \(t^{-1/4}\), and the post-threshold equilibrium amplitude turns on with quartic-root scaling.

## Correctness — PASS

At \(h=\sqrt{\nu_1\nu_2}\), the exact energy derivative factors as \(-2(\sqrt{\nu_1}x-\sqrt{\nu_2}y)^2\). Boundedness plus LaSalle leaves only the decaying \(z\)-axis inside the zero-dissipation set, establishing global attraction at equality. In the critical coordinates, independent symbolic reconstruction gives \(\dot s=vz\), \(\dot v=-Dv-sz\), and the stated \(z\) equation. Solving the leading invariance equations yields \(v=-pq(\nu_3D)^{-1}s^3+O(s^5)\), \(z=pq\nu_3^{-1}s^2+O(s^4)\), hence the nonzero quintic coefficient \(-p^2q^2/(\nu_3^2D)\). Integrating the reduced scalar equation gives the \(t^{-1/4}\) law and substitution gives the stated \(t^{-1/2}\) law for \(z\). The post-threshold quartic-root branch agrees with the exact equilibrium formula.

Checked sources:
- A. S. Pikovskii, M. I. Rabinovich, V. Yu. Trakhtengerts, Onset of stochasticity in decay confinement of parametric instability, Sov. Phys. JETP 47 (1978), primary source indexed and relevant model/bifurcation material inspected.
- N. V. Kuznetsov et al., Finite-time Lyapunov dimension and hidden attractor of the Rabinovich system, Nonlinear Dynamics 92 (2018), complete open full text inspected.
- Resultary semantic search for Rabinovich quintic pitchfork, critical slowing, quartic-root onset, and center-manifold threshold.
- Independent symbolic reconstruction of the critical coordinate equations, energy identity, center-manifold coefficients, and quintic coefficient.

Residual risks:
- Standard center-manifold and stable-foliation tracking theorems are used for the generic asymptotic transfer.

## Originality — PASS

Best-of-knowledge originality passes for the equality-case closure, explicit quintic normal form, and critical decay law. The 2018 open full text states global asymptotic stability only for the normalized parameter \(r<1\), and treats the post-threshold equilibria and later chaotic dynamics. Searches did not locate a prior statement of the equality theorem or the fifth-order coefficient and \(t^{-1/4}\) relaxation. The classical equilibrium formulas and the existence of a pitchfork are prior art and are not claimed as new.

### Equivalent formulations

Searches:
- Resultary semantic search: Rabinovich quintic pump threshold critical slowing center manifold
- Web search: Rabinovich system t^{-1/4} quintic pitchfork

Evidence:
- The assigned record is the only exact published-record hit.
- No earlier source containing the fifth-order normal form or critical decay exponent was located.

Reasoning: Equivalent formulations include a degenerate \(\mathbb Z_2\)-pitchfork with first saturation at fifth order and algebraic critical relaxation with exponent one quarter.

### Broader coverage

Searches:
- Kuznetsov et al. 2018 full text
- Pikovskii--Rabinovich--Trakhtengerts 1978 primary source

Evidence:
- The 2018 paper states the origin is globally asymptotically stable for \(r<1\), while for \(r>1\) nonzero equilibria exist.
- The original work supplies the physical model, threshold, and post-threshold states.

Reasoning: These broader dynamical studies do not cover the boundary \(r=1\) center dynamics or decay rate.

### Exact database or table

Searches:
- Resultary exact-topic search
- Targeted searches for critical exponent and quartic-root onset

Evidence:
- No independent prior exact coefficient or decay formula was located.

Reasoning: The exact equilibrium quartic-root scaling is known implicitly, but a branch exponent alone is not a table that determines the critical-time normal-form coefficient.

### Claim versus prior implication

Searches:
- Known exact equilibrium branch versus audited center dynamics
- 2018 strict-subthreshold theorem versus equality case

Evidence:
- The quartic-root branch suggests degeneracy but does not by itself determine the critical flow coefficient or generic temporal asymptotic.
- Strict stability for \(r<1\) does not imply global stability at the nonhyperbolic boundary.

Reasoning: The final claim needs an additional Lyapunov/LaSalle argument and explicit center-manifold calculation, so it is not mechanically implied by the prior statements.

### Source inspections

- **Finite-time Lyapunov dimension and hidden attractor of the Rabinovich system** — Covers strict subthreshold global stability and post-threshold equilibria, but not equality or the quintic critical law. Material read: Complete open article text, including the equilibrium/stability section around the \(r=1\) threshold. Method: Primary full-text inspection. Evidence: The paper explicitly states global asymptotic stability for \(r<1\) and then treats \(r>1\); the boundary is not supplied with the audited critical normal form.
- **Onset of stochasticity in decay confinement of parametric instability** — Prior source for the system and classical threshold scenario; not used for a whole-document noncoverage claim. Material read: Indexed primary-paper text and relevant threshold/bifurcation passages; direct full-PDF fetch timed out. Method: Primary indexed-text inspection. Evidence: Accessible passages discuss the onset threshold, nonzero states, and later stochastic regimes.

Checked sources:
- A. S. Pikovskii, M. I. Rabinovich, V. Yu. Trakhtengerts, Onset of stochasticity in decay confinement of parametric instability, Sov. Phys. JETP 47 (1978), primary source indexed and relevant model/bifurcation material inspected.
- N. V. Kuznetsov et al., Finite-time Lyapunov dimension and hidden attractor of the Rabinovich system, Nonlinear Dynamics 92 (2018), complete open full text inspected.
- Resultary semantic search for Rabinovich quintic pitchfork, critical slowing, quartic-root onset, and center-manifold threshold.
- Independent symbolic reconstruction of the critical coordinate equations, energy identity, center-manifold coefficients, and quintic coefficient.

Residual risks:
- A broad 1981 review by the original authors and older Russian-language analyses were not available in complete text during this run and remain explicit residual coverage risks.
- The \(t^{-1/4}\) asymptotic is stated only off the two-dimensional strong-stable manifold.

## Scientific value — PASS

The theorem identifies the exact nonhyperbolic stability boundary and explains a non-generic critical exponent in a classical nonlinear-wave model. The quintic coefficient, \(t^{-1/4}\) relaxation, and quartic-root onset form a coherent structural bifurcation picture, not a routine parameter substitution.

Checked sources:
- A. S. Pikovskii, M. I. Rabinovich, V. Yu. Trakhtengerts, Onset of stochasticity in decay confinement of parametric instability, Sov. Phys. JETP 47 (1978), primary source indexed and relevant model/bifurcation material inspected.
- N. V. Kuznetsov et al., Finite-time Lyapunov dimension and hidden attractor of the Rabinovich system, Nonlinear Dynamics 92 (2018), complete open full text inspected.
- Resultary semantic search for Rabinovich quintic pitchfork, critical slowing, quartic-root onset, and center-manifold threshold.
- Independent symbolic reconstruction of the critical coordinate equations, energy identity, center-manifold coefficients, and quintic coefficient.

Residual risks:
- A broad 1981 review by the original authors and older Russian-language analyses were not available in complete text during this run and remain explicit residual coverage risks.
- The \(t^{-1/4}\) asymptotic is stated only off the two-dimensional strong-stable manifold.

## Conclusion

The unchanged final claim passes correctness, best-of-knowledge originality, and scientific value.
