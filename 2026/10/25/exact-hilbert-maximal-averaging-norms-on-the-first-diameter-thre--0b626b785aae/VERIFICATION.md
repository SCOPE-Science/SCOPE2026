---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

The exact finite selector identity reduces the centered graph-ball maximal-operator squared l2 norm to max_lambda(A_sigma^T A_sigma) over every 4^n radius mask for n=6,7. I independently reconstructed the 30- and 105-scaled averaging matrices. Exact integer Bareiss/Sylvester checks enumerated all 4096 C6 masks and all 16384 C7 masks: respectively exactly 12 and 7 dihedral winners, with 4084 and 16377 strict losing inequalities at 1.517 and 1.531. Exact integer Rayleigh witnesses exceed 1.520400 and 1.532672; positive-definite upper isolations at 1.520401 and 1.532673, Gram characteristic coefficients and announced quintic/cubic are verified. Uniform-ball rows make the winning Grams entrywise positive, so Perron simplicity fixes the modulus; arbitrary coordinate signs/phases are permitted because M uses |f|. This proves precisely two cycles, real and complex, not a larger-cycle family.

## originality

PASS

Best-of-knowledge PASS for the exact two finite-cycle maximizations and full equality classes. Prior general and small-graph results do not mathematically imply the two algebraic maxima or winning-mask classification; the linear-selector reduction is standard and not presented as novel.

## value

PASS

The six- and seven-cycles are the first natural diameter-three cycle pair, with distinct parity and different equality orbits. Exact algebraic Hilbert maximal norms and ALL extremizers supply a nontrivial finite extremal benchmark; the result is not a mere recomputation of the norm of a fixed linear averaging operator because it optimizes all 20,480 nonlinear row selections. Its bounded scope is explicit, and no claim of a universal cycle theorem is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
