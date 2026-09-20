# Review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

**PASS.** Expanding the source's exact transformed Lagrangian to quadratic order in the antisymmetric coordinate and applying the Euler--Lagrange equation gives
\[
M_2\ddot d+[G_2\cos y+\mu\cos(y-x)\dot x^2-\mu\sin(y-x)\ddot x]d=0.
\]
The mixed \(d\dot d\) term cancels all apparent first-derivative terms after differentiation. Symbolic verification reproduces this identity exactly. Substituting the exact equations on the symmetric manifold yields the stated acceleration-free stiffness, also checked symbolically.

The small-amplitude expansion is checked independently by comparing its five Fourier components (mean, two double-frequency terms, difference frequency, and sum frequency) against direct evaluation of the quadratic stiffness at 101 sample times. The maximum residual for the printed source parameters is \(1.85\times10^{-13}\). The source-parameter eigenfrequencies computed from the printed masses, lengths, and fitted inertias agree with its reported frequencies to the expected rounding accuracy.

No critical-angle value is inferred from the leading resonant coefficient. This is important because the mean stiffness correction and nonlinear shifts occur at the same asymptotic order as the sum-frequency modulation.

## Originality

**PASS, with a narrow source-specific claim.** The target preprint derives an antiphase energy-transfer function, reports the observed onset near \(47.8^\circ\), discusses the near relation \(f_++f_-\approx2f_d\), and explicitly states that systematic theoretical study of the critical value is planned. It does not state the scalar transverse variational equation, the acceleration-free transverse stiffness, or the displayed sum-frequency coefficient.

Searches by the source identifier and title, branched-double-pendulum terminology, antiphase stability, variational-equation terminology, and parametric-resonance terminology did not locate a matching published formula. The authors' 2024 meeting abstract reports the experimental generation condition; the 2025 meeting record concerns image-based energy transfer. Related literature on ordinary or driven double pendula establishes that parametric and combination resonances are standard mechanisms, so those general ideas are excluded from the novelty claim.

The main unresolved priority risk is gray literature cited by the source itself: T. Miura's 2024 master's thesis and K. Kato's 2026 graduation thesis are cited for preliminary numerical simulations, but their full contents were not inspected. Either could contain a related transverse-stability calculation. The claim is therefore explicitly limited to the source-specific formulas and to the best of our knowledge.

## Value

**PASS.** The result converts the source's experimentally observed spontaneous antiphase growth into an exact stability problem on the invariant child-synchronous manifold. The acceleration-free form is directly suited to angle-and-velocity trajectory data, avoiding numerical second differentiation. The small-amplitude decomposition also clarifies that the two in-phase modes generate a direct sum-frequency parametric modulation near \(2\omega_d\); nonlinear low-frequency sidebands are therefore not the only possible route by which the frequency mismatch can be bridged. At the same time, the large mean correction explains why a one-harmonic threshold estimate is not controlled.

## Scientific limitations

The result is linear in the transverse antiphase perturbation and does not describe nonlinear saturation. The explicit Fourier decomposition is a small-amplitude expansion and is not used to claim the experimentally observed large-angle threshold. Real-apparatus damping, asymmetry, release imperfections, and noise are absent from the conservative model. Standard single-period Floquet criteria apply only when the symmetric base trajectory is periodic; generic two-mode small-amplitude motion is quasiperiodic.
