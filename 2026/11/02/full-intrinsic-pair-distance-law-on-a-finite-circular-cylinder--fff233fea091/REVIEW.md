# Scientific review: intrinsic random distances on finite circular cylinders

## Correctness

PASS. The lateral cylinder is isometric to a flat product strip with one periodic coordinate. The closest-lift angular gap is exactly uniform on the half-circumference interval, independent of the triangular vertical gap. Their squared sum is precisely the intrinsic squared distance, since every candidate shortest straight lift stays inside the strip. The integrated conditional triangular law gives the CDF and its derivative. Local cutoff integrals give nonzero fractional singularity coefficients of orders \(3/2\) and \(5/2\), and corner scaling gives the cubic upper tail. The explicit even moments and diameter form a nonsingular inverse system for the two dimensions. No sampled computation is used as proof of a universal assertion.

## Originality

PASS under a best-knowledge comparison, not an independent historical-priority certification. The full one-periodic covering-space treatment of Chen and Chen (arXiv:1011.5320, 2010) concerns shortest-path algorithms, without a random-pair distribution. The exact planar Euclidean distance frameworks of Sheng (1985) and Marsaglia, Narasimhan, and Zaman (1990) involve unwrapped planar regions rather than shortest paths on an angular quotient. Hammersley's 1951 circular-cylinder integral concerns Euclidean distance between pairs of interior volume points, not the intrinsic lateral-surface metric. An accessible related prior calculation for flat Klein bottles concerns a different closed quotient and its second moment, not the present finite-cylinder full distribution, contact thresholds, or inverse law. Targeted mathematical research searches did not return an equivalent statement. Full text was unavailable for some older geometrical-probability papers; their possible unexpected extensions are recorded as a residual priority risk. These limitations do not supply affirmative evidence of an implication covering the exact theorem.

## Mathematical value

PASS. Random pair-distance distributions are natural invariants of compact metric-measure surfaces. Here a geometrically canonical surface with a genuine boundary and a nontrivial fundamental group has an exact full CDF across arbitrary radius and height, distinct universal singularity exponents distinguishing periodic cut-locus and axial boundary effects, and an explicit inverse reconstruction from distributional observables. This is a complete two-parameter classification of a natural invariant, not a singled-out numerical slice. The result is specific to the lateral intrinsic geometry and does not assert applications to extrinsic distances or cylinder solids.

## Verification and risk

The included independent numerical implementation passed 336 midpoint-quadrature comparisons, 350,000 directly sampled surface-point pairs, checks of moment identities and inverse formulas, and tests of both threshold powers and the endpoint tail. The maximum CDF quadrature discrepancy was less than \(2.31\times10^{-6}\). Reproducibility requires only Python 3. The relevant research sources and material-read limits are stated in `AUDIT.json`; independent priority and mathematical review have not been performed.

Self-review: passed. Independent audit: not yet performed.
