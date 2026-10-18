# Scientific review

## Correctness — PASS
The theorem covers every nonnegative integrable position-dependent reversal rate with fixed spatial integral. Its proof obtains the backward equations from the continuous-time velocity-jump generator, uses the outgoing absorbing conditions to fix the unique solution, and reduces optimization to two sharp first-moment inequalities over positive measures. Both strictness assertions follow because integrable profiles have no atoms. Explicit approximating rectangular profiles prove both bound sharpness, and an interpolation argument proves all interior values are attained. Finite-grid generator checks in `verification.py` corroborate the normalization and formulas; no finite computation is used to establish the infinite-class result.

## Originality — PASS, with residual risks
Leydolt (1993) treats telegraph first-passage laws with two boundaries at uniform switching; Angelani et al. (2014) permit spatially varying tumble rates but solve a reflecting-to-absorbing first-passage setup, not the present function-space optimization. Newby and Keener (2011) use spatially inhomogeneous velocity jumps for turning-point escape; only a publisher abstract was accessible, so direct full-text exclusion is unavailable. Angelani (2023, 2024) analyzes flexible boundary configurations or rate optimization for spatially uniform bulk rates. Guéneau et al. optimize a uniform rate under confining potentials. None of the inspected full texts states an unrestricted fixed-integral spatial-rate design problem, its sharp mean interval, or its symmetry obstruction. Equivalence under other terminology remains a residual bibliographic risk; database nonmatches alone do not prove novelty.

## Mathematical value — PASS
An integrated spatial switching budget is a natural control resource in velocity-jump transport, bacterial motility and persistent search. The complete sharp attainable range resolves both extremes without artificial finite-dimensional parameterization, demonstrates a nonintuitive strict advantage of asymmetric reorientation over ballistic motion, and proves a contrasting global obstruction for every symmetric profile. The geometric concentration limit is mathematically essential rather than a small numerical improvement.

## Limits of verification
The extremal values are only approached by increasingly concentrated integrable profiles. Other budget choices and bounded-rate constraints are outside scope. External independent validation was not performed.

Self-review: passed. Independent audit: not yet performed.
