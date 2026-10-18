# Scientific review

## Correctness — PASS
For the exact published nIRK4 tableau, the stage matrix has positive determinant \((13a^2+224a+1080)/1080\) on every \(a\geq0\). The fourth stage equals the output, and symbolic inversion gives the rational multiplier displayed in RESULT.md. Factoring the differences with \(\pm1\) and analyzing the cubic derivative yields the unique sharp threshold and all boundary cases. An independent exact construction of the Gaussian collocation tableau verifies the classical algebraic-stability identities, which prove uniqueness and contractivity for every sampled nonnegative damping profile. The included symbolic verifier replay passed; finite tests are ancillary, not an infinite proof.

## Originality — PASS, with residual risk
The primary full text [1] gives the nIRK4 coefficients, autonomous stability function and accuracy experiments, but not the sharp affine-time damping multiplier and its contractivity frontier. Classical algebraic-stability theory explains the Gaussian comparison but does not supply this concrete nIRK4 parameter classification. Relevant public mathematical-record searches using the method name, profile aliases, nonautonomous contractivity, and the exact polynomial yielded no equivalent claim; closest records concern Fehlberg estimator resonance and Markov positivity of a different Padé integrator. Search incompleteness and potential earlier treatment under different stability nomenclature remain explicit risks.

## Value — PASS
The concrete A-stable method can amplify by arbitrarily large factors on a smooth scalar flow that contracts exactly. The sharp parameter frontier, globally solvable stages, and exactly matched Gauss Padé comparator isolate a consequential failure of frozen-coefficient stability as a proxy for nonautonomous contractivity. This is more informative than a routine negative-sign example and can guide numerical method selection for time-varying stiffness. It does not establish broad nonlinear instability or a general-purpose stepsize prescription.

## Status
Self-review: passed. Independent audit: not yet performed.
