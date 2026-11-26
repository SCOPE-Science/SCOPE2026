---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

In Gaussian-normal coordinates the plane is g·x=r; r divided by ||g|| is the unit-normal offset. Thus |r|=UW_d with U independent uniform, while the orientation is tilted by W_d/||g|| divided by its expectation. The tilt is uniformly bounded by the aspect bounds. Generic section vertices correspond bijectively to crossing box edges. The high-side cube subset has size from 1 through 2^(d−1); the boundary lies between its size and d times its size, which preserves its log exponent. Conditional log-mgf and derivative converge by bounded lengths, Gaussian second moments and empirical convergence. For the lower bound at an interior threshold s m M1, tilt to the mean at a slightly larger s′ m M1 and use a small interval wholly above the threshold; the conditional tilted variance is at most d^−2 times the sum of squared coordinate weights, O_P(1/d). Shrink s′ to s after taking the log limit; the Chernoff upper bound and continuity give the same exponent. This one-sided interval is the precise interpretation of the proof's brief tilting step. Strict versus weak inequalities and the replacement by U W_d/d follow by bracketing and integrating over U. Strict increase and continuity of the rate follow from its positive interior optimizer and the endpoint expansions. Jensen at the heterogeneous optimizer gives the strict comparison at the same M1. At zero the cumulant begins with M2 λ²/2; at infinity its correction to m M1 λ−log 2 is m π² M_{−1}/(24λ). Minimizing m M1(1−s)λ plus this correction gives the lower-end square-root relation for log 2−I(s) and hence the specified quadratic probability; the small-λ expansion gives the other coefficient. The mean follows exactly from summing each edge's crossing interval at fixed normal. The frozen verify.py was inspected, not run; its boundary examples, finite quadrature comparison and coefficient evaluations do not prove the limiting distribution.

## originality

PASS

The cubical cumulant/rate and uniform-translation cube mean are prior. The supported distinct result is the bounded deterministic side-profile limit for the logarithmic vertex count under motion-invariant affine sampling, its strict heterogeneous-versus-cube stochastic comparison, and its two sharp endpoint laws. The related Crofton cube variance and simplex log-count records do not determine that result, and the central orthotope comparison uses a different observable and sampling. Swan's cited statement is for cubes; the unequal-side-length mean identity is proved in the record but its earlier attribution is not settled by that citation alone. The mean is not used as the novelty claim.

## value

PASS

The logarithmic observable gives typical information that the exactly shape-blind arithmetic mean misses. Under the invariant sampling, different side profiles yield a strict stochastic order and two ends governed by distinct moments. The relation between random affine cuts, edge expansion and a deterministic-profile quenched rate explains the phenomenon rather than merely recomputing finite section counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
