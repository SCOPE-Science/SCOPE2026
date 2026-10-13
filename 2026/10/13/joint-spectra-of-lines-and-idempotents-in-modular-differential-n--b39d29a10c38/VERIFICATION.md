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

# Reproducibility

The standalone `checker.py` is executable with Python 3 and standard-library modules only. Running `python checker.py` prints a series of `BRUTE_OK` and `UNIFORM_OK` lines and finishes with `VERIFY_OK`.

`BRUTE_OK` means that direct enumeration of algebra products over the listed finite field agrees with independently calculated canonical-obstruction counts of embedded projective lines and nonzero idempotents. All parameter vectors were checked for \((p,q)=(2,2),(2,4),(3,3)\); for \((5,5)\), 32 parameter vectors including varied low/high coefficients were tested. `UNIFORM_OK` checks every parameter vector for those four finite-field instances, including \(5^5\) choices in the final case, against the asserted exact fiber cardinality \(q^{p-2}\).

The proof of the theorem for all primes and prime powers is in `RESULT.md`: existence/uniqueness of the two recurrence solutions, the valuation split of all lines, identification of idempotents, and triangular parameter-fiber counting. Exhaustive finite computations are confirmatory and do not certify generality. No independent audit was performed.
