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

# Reproducibility and verification

The accompanying `verify.py` uses only the Python 3 standard library and may be run as `python3 verify.py`.

The verifier exhaustively enumerates all binary operation tables on \(n=1,2,3\) points and compares regularity tests with the exact Stirling-occupancy count. A separate direct test over all potential inner inverses for \(n=2\) confirms that the criterion agrees with monoid regularity. Direct enumeration returns respectively \(1\) of \(1\), \(14\) of \(16\), and \(14619\) of \(19683\) regular operations. Its recurrence independently computes exact diagonal-occupancy weights and weighted regularity probabilities for \(n=10,20,40,80,160,320,640\). At \(n=640\) it obtains ratio approximately \(0.999963\) for \(\Pr(R_n)/(Ce^{-In})\). The conditional variance divided by \(n\) at \(n=640\) is about \(0.093976\), close to the predicted Gaussian variance \(0.093950\). It evaluates the constants from their defining scalar equations and reports `VERIFY_OK` on success.

The finite tests support the conditioning algebra and constant calculations but do not prove the asymptotic. The proof additionally requires the documented uniform local limit estimate and a global tail bound for the occupancy sum. No independent audit has been performed.
