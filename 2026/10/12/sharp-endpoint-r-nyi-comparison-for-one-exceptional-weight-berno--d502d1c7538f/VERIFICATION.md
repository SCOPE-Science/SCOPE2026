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

# Verification details

Run `python3 verify_one_outlier.py` with Python 3 from the extracted package directory. Its only dependency is the Python standard library (`math` and `fractions`). The checker reconstructs every integer coefficient \(A_{n,k}(j)\), verifies positivity and normalization, and checks the exact strict inequality for \(190\) pairs \((n,k)\) and \(3990\) atom positions. It also independently tests sample central-binomial inequalities, but those finite samples are not treated as proofs for all dimensions.

The analytical argument supplies the missing infinite steps: two binomial-coefficient ratio inductions, the exact symmetric binomial pmf, a pointwise exponential decay inequality based on mode distances, and the \(n\ge20\) tail comparison. The finite computation only certifies the explicitly bounded cases \(n\le19\). The special limiting calculation uses the standard central-binomial asymptotic. No independent audit or third-party certification has been performed.
