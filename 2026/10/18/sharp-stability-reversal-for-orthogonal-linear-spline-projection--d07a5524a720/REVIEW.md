# Scientific review: sharp stability reversal for alternating linear-spline meshes

## Correctness — PASS
The direct tridiagonal inverse-Gram construction verifies the parity-split geometric Green row for every positive parameter pair. Exact cellwise integration, a summable four-tail decomposition, and symmetry plus an extremizing sign input prove the full-line sharp norm, not merely a finite-section estimate. The rational simplification is independently checkable by symbolic polynomial division modulo the root equation; the package checker passed 144 assertions. Critical limits include equal cell lengths and extreme contrast. No infinite-dimensional conclusion is inferred solely from numerical tests.

## Originality — PASS (same-model, with identified priority uncertainty)
Passenbrunner's 2016 periodic-spline full-text work and Passenbrunner–Shadrin's 2013 arbitrary-knot full-text results provide global bounds and inverse-Gram localization. Their inspected theorems do not assert this exact alternating full-line norm or its strict contrast law. The isolated single-cell perturbation belongs to a different knot geometry and does not imply the new rational identity. Direct searches for alternative aliases, explicit rational formulas, and exact mesh tables found no matching coverage. A 2013 sharp-bounds chapter by Oswald and older geometric-mesh work by Jia could not be read in full, leaving a real priority risk; no absent-source noncoverage is asserted. This does not constitute independent bibliographic validation.

## Value — PASS
The result provides a natural complete family with a surprising mathematical direction: alternating periodic mesh deformation decreases the sharp projection norm from 2, whereas an isolated mesh defect increases it. Exact dependence on the normalized cell contrast, a unique uniform-mesh equality case, and the sharp unattained limit 5/3 quantify a meaningful stability mechanism not captured by generic knot-independent estimates.

## Boundaries
The theorem concerns continuous degree-one splines on the full real line. Finite endpoints, higher spline orders and nonperiodic meshes are outside scope. Potential exact historical specializations remain an explicit risk. The reported checks are reproducibility evidence, not an independent audit.

Self-review: passed. Independent audit: not yet performed.
