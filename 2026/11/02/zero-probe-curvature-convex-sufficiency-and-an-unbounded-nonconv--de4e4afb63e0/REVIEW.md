# Scientific review — zero-probe SQP–SQCQP gap

## Correctness (PASS)
For positive-semidefinite inequality corrections, quadratic feasibility implies affine feasibility, and the zero-correction SQP minimizer is also quadratic-feasible. The strict convex objective makes it the unique minimizer of both. The independent nonconvex family has base constraint gradient \((0,1)\), Hessian eigenvalues \(\pm1\), SQP point \((r,0)\), and SQCQP point \((r,m)\). The source-style correction is exactly zero at the probe; direct evaluation gives objective gap \(m^2/2\) and direction gap \(m\). The SQCQP multiplier required at the SQP point is \(m/(1-r)<0\), so no KKT stationarity holds. The included checker passes 16,269 exact-rational witness instances and nine convex controls; proof is analytical.

## Originality (PASS, with explicit historical uncertainty)
The arXiv source's equation-level indicator inspects quadratic correction at an SQP probe and uses it to choose between the two model classes. Its local stability theorem assumes a shrinking probe and shared regular active set; it does not imply global objective-gap control from the scalar indicator. Solodov's 2004 paper instead uses positive-semidefinite constraint surrogates; the 2003 convex SQCQP paper is also outside the indefinite witness. Dedicated literature and published-finding corpus equivalence/coverage queries did not find the source-specific zero-indicator, arbitrarily separated-model-minima family. A general geometric observation may be implicit in older nonconvex QCQP literature; this is a residual historical-priority risk, not evidence of a duplicate. The convex inclusion lemma is elementary context, not asserted as independently novel.

## Value (PASS)
The finding answers a natural question for a newly proposed model-selection diagnostic: does an exactly vanishing probe-based curvature estimate imply the second-order model will not materially improve the local quadratic objective? The structural convex/nonconvex boundary isolates when the implication is valid and gives an unlimited failure when curvature is indefinite, despite exact derivatives, identity objective curvature, norm-one constraint Hessian and a regular base constraint. It explains that testing the scalar \(d^{\mathsf T}Hd\) may miss the vector correction \(Hd\), which can flip the active constraint normal. The result is a diagnostic design limitation, not a negative theorem about full-iteration convergence.

## Closest sources and limits
- Tiwari–Ansary, arXiv:2610.18428v1 (2026), §§2.1, 3.1, 4.2: exact model definitions, normalized probe indicator, and local small-step comparison.
- Solodov, doi:10.1287/moor.1030.0069 (2004), introductory formulation: positive-semidefinite surrogate constraints and slack strategy.
- Fukushima–Luo–Tseng, doi:10.1137/S1052623401398120 (2003), accessible abstract: convex SQCQP models.

The negative construction is nonconvex and nonlocal, with gap growing in an objective target parameter. More comprehensive historical-priority checking and independent mathematical review remain warranted.

Self-review: passed. Independent audit: not yet performed.
