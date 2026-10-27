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

The analytical proof provides every all-parameter and asymptotic statement. The accompanying standalone `checker.py` independently evaluates the exact angular integral at several noise levels, checks the elliptic small-noise coefficient, tests the first two terms of both asymptotic expansions, and checks numerical strict monotonicity.

For the independent root-count experiment, it eliminates the conjugate variable from \(z^2-u\overline z=c\), solves the resulting quartic, rejects spurious roots against the original harmonic equation, and compares the resulting count with the winding number of the sampled caustic boundary. In the preparation run, all 350 seeded trials matched. Finite numerical tests do not establish the global dichotomy, the sign of every derivative, or the asymptotic error estimates.

To reproduce: install Python with `mpmath` and `numpy`, then run `python checker.py` from the same directory as this document. The code has no data-file dependencies and performs no network access.

No independent audit or external validation has been performed.
