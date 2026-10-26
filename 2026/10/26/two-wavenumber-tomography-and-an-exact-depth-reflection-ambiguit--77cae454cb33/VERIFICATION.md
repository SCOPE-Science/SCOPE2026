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

# Verification and limits

The proof verifies the complete physical domain using exact hyperbolic identities, a positive quadratic discriminant and the strict derivative sign of a scalar ratio. The executable `checker.py` constructs both measured branches directly from the previously published forward quadratic, computes the proposed inverse, and tests 600 seeded valid parameter points and symmetric/reflection cases. Execute with `python checker.py` using Python 3's standard library; the observed success line is `CHECK_OK: 600 independent forward/inverse cases, strict-ratio samples, symmetric cases, reflection`.

The finite numerical tests cannot establish global monotonicity or novelty. Global monotonicity follows analytically from the strict increase of the auxiliary hyperbolic function; parameter completeness follows from Vieta's formulas and the ratio endpoints. The stated reconstruction is noiseless and does not establish conditioning or experimental accuracy. The full text of Avital and Miloh's closely themed ship-wave inverse paper was inaccessible, leaving a literature-priority qualification. No independent assessment has been performed.
