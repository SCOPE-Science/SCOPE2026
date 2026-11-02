---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

Run `python verify.py` with Python 3 standard-library support. The checker builds the full adjacency matrix independently of the formula, enumerates every labeled seed set for ordered community sizes \(3\le a,b\le6\), and replays synchronous irreversible adoption at every rational fraction in the finite test grid. It compares the exact successful-seed count at each cardinality with the polynomial identity, checks the minimum required seeds and the three-way difference classification, and tests explicit six-vertex examples.

At package preparation, the checker returned `PASS 2211 finite exact assertions; rates 46 graph pairs 16`. All arithmetic for threshold comparisons, binomial coefficients, counting and equality testing is exact integer or `fractions.Fraction` arithmetic. The finite test grid is not exhaustive over all graph sizes or real thresholds; the universal claim rests on the closed-form proof in `RESULT.md`. Historical novelty remains provisional, and independent mathematical validation has not been performed.
