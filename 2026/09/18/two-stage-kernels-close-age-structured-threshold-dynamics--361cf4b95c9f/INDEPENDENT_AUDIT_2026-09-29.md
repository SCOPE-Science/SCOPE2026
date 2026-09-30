# Independent Audit — 2026-09-29

**Record:** `2026/09/18/two-stage-kernels-close-age-structured-threshold-dynamics--361cf4b95c9f`  
**Title:** Two-stage reproductive kernels force complete threshold convergence in a bistable age-structured population model  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `a48dc8697038a4b8e7c3b6ecc833116af4d385d1`  
**Disposition:** **PASSED**

## Independent checks

- Re-derived the X and Y moment equations from the transport PDE and the two exponential stages.
- Differentiated the proposed energy and checked coercivity from limsup f(x)/x<1.
- Checked the planar Jacobian at each equilibrium and the strong-cooperativity/unordered-stable-manifold threshold mechanism.
- Checked the characteristic lift from Y(t)→κ to u(t,·)→κe^{-M(·)} in L1.

## Three-axis assessment

- **Correctness — PASS**: For β(a)=e^{M(a)}K(a), with K the two-stage hypoexponential density and β1(a)=r1 e^{M(a)-r1a}, direct integration by parts gives X′=r1(f(Y)−X), Y′=r2(X−Y). Eliminating X yields the damped scalar equation Y″+(r1+r2)Y′=r1r2(f(Y)−Y). The stated energy has derivative −(r1+r2)(Y′)^2; sublinear-at-infinity f makes the energy coercive, ruling out recurrent dynamics and forcing convergence to one of 0, κ1, κ2. The Jacobian signs give sinks at 0 and κ2 and a saddle at κ1. Because both kernels are strictly positive, the source paper’s strictly ordered initial-data family maps to a strictly ordered moment curve, which can cross the unordered saddle stable manifold at most once. The characteristic formula then lifts moment convergence to L1 convergence of the age density.
- **Originality — PASS**: The 2026 Griette–Herrera source proves sharp threshold dynamics for compactly supported fertility and a different special noncompact case with eventually constant birth and death rates. Its introduction explicitly says the general noncompact case is more intricate. No searched source supplied this phase-type two-stage kernel, exact planar closure, or complete convergence/threshold argument. The classical 1979 Gurtin–MacCamy paper was sought after open-access searching; authorized institutional retrieval reached a publisher human-verification gate, so its full text was not read and is retained as a residual originality risk rather than silently assumed away.
- **Scientific Value — PASS**: The result isolates a noncompact fertility family for which the infinite-dimensional threshold dynamics closes exactly to a two-dimensional cooperative damped system. This supplies a transparent global convergence mechanism and a complete threshold theorem in a regime the motivating source identifies as difficult, so it is a meaningful structural extension rather than a parameter-only refinement.

## Findings

- The assigned tree exactly matches the current tree at the dispatcher’s checked commit.
- Independent integration-by-parts reconstruction reproduces both moment equations and the scalar damped second-order equation.
- The Lyapunov derivative is strictly nonpositive and vanishes only when Y′=0; invariance then forces an equilibrium root of f(Y)=Y.
- Assumption 1.2 of Griette–Herrera requires strict increase of initial data on a positive-measure reproductive-age set; here the phase-type kernels are positive on every positive age, so the induced (X,Y) initial curve is strictly ordered.
- The Oxford retrieval job for Gurtin–MacCamy (1979) was revisited and ended at a human-verification requirement; no claim of reading that inaccessible full text is made.

## Sources compared

- Griette and Herrera, Sharp threshold dynamics for a bistable age-structured population model: https://arxiv.org/abs/2602.06809 — Primary 2026 source; it proves the compact-support theorem and a distinct eventually-constant noncompact case, and flags the general noncompact setting as more difficult.
- Gurtin and MacCamy, Some simple models for nonlinear age-dependent population dynamics: https://doi.org/10.1016/0025-5564(79)90049-X — Classical comparison source. Open-access search did not yield inspectable full text; authorized retrieval stopped at publisher human verification, so this paper is not claimed read.
- Andersson et al., Density-dependent feedback in age-structured populations: https://arxiv.org/abs/1903.02226 — Later Gurtin–MacCamy analysis confirms the breadth of classical density-feedback work but does not expose the audited two-stage phase-type closure in the accessible material.

## Limitations

- The theorem is for the specially engineered two-stage phase-type fertility kernel, not arbitrary noncompact fertility.
- The threshold statement uses the monotone one-parameter initial-data hypothesis; it is not a classification of all initial data.
- The full 1979 Gurtin–MacCamy article remained inaccessible behind publisher verification and was not read; originality is therefore to the best of the inspected evidence.

This audit is independent of the repository’s pre-existing same-model review. No GitHub writes were performed during the audit.
