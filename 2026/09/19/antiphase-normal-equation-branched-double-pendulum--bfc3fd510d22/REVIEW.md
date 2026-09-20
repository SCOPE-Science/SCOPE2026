# Scientific review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS. The normal equation follows directly from the second variation of the source Lagrangian about the exact child-symmetric invariant manifold. The mixed `x xdot` term can be removed by a total derivative, leaving a scalar oscillator with coefficient
\(\kappa=G_2\cos\theta_m+\mu\cos(\theta_m-\theta_1)\dot\theta_1^2-\mu\sin(\theta_m-\theta_1)\ddot\theta_1\). A standalone symbolic calculation independently reconstructs this coefficient.

The release-point formula is obtained by solving the two in-phase acceleration equations with zero initial velocities. Substitution of the source's measured geometry, masses, and fitted inertias gives the first stiffness zero at 84.4335888 degrees and a strictly positive stiffness at 47.8 degrees. The small-amplitude combination spectrum is obtained by inserting the linear two-mode in-phase solution into the exact coefficient; symbolic/numerical checks reproduce the source's three linear frequencies and verify a nonzero sum-frequency coefficient.

No claim is made that the quadratic expansion predicts the finite-amplitude critical angle. This avoids an uncontrolled Mathieu extrapolation: the mean quadratic shift, nonlinear base-frequency shifts, damping, and higher-order terms are relevant at the observed amplitude.

## Originality

PASS, narrowly scoped. General autoparametric resonance, Hill equations, and transverse variational analysis are prior art and excluded from novelty. The claim is limited to the specific branched-double-pendulum model of arXiv:2609.20688v1: its exact finite-amplitude antiphase normal equation, the source-parameter release-stiffness obstruction, and the complete leading quadratic combination spectrum of that normal coefficient.

Searches for the source identifier and exact title together with `Floquet`, `Hill`, `Mathieu`, `parametric`, `variational`, and `stability`, as well as searches for `branched double pendulum` with those terms, found no public source-specific derivation. The v1 full text does not contain the terms `stability`, `parametric`, `variational`, or `Floquet`. Current SCOPE searches by source identifier, model name, and antiphase/variational terminology found no overlap.

The most important residual originality risk is the same authors' 2025 Physical Society of Japan meeting contribution, *Energy transfer processes between oscillation modes of a branched double pendulum observed with image analysis* (Meeting Abstracts 80.2, 18pPS-113). Bibliographic metadata and a short partial display were inspected, but the full contribution was not. The accessible 2024 meeting abstract reports that antiphase growth begins above a parent-angle threshold, without exposing the normal-stability analysis given here. Generic autoparametric-pendulum papers by Cartmell--Kovacic--Zukovic (2012) and Warminski (2006) concern different mechanical systems and establish background mechanisms rather than this source-specific coefficient.

## Value

PASS. The source experimentally identifies a sharp onset and derives an energy-transfer diagnostic, while leaving the onset mechanism unresolved. The exact scalar normal equation turns that question into a direct stability problem on the invariant in-phase manifold. It also proves that the observed transition cannot be explained by a stiffness sign loss at the instant of release and identifies, with a nonzero coefficient, the leading quadratic combination channel closest to principal antiphase parametric resonance. This supplies a concrete analytical object for future threshold calculations or direct use with measured/simulated in-phase trajectories.

## Limitations

The model is the ideal conservative symmetric Lagrangian used in the source. Friction, air drag, small construction asymmetry, and finite-antiphase saturation are not included. Positive release stiffness is only a negative result about instantaneous static loss; it does not prove later-time stability. The combination-frequency expansion is valid locally near the hanging equilibrium on fixed time intervals and is not a quantitative theory of the finite-amplitude 47.8-degree threshold.
