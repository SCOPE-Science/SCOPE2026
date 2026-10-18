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

# Reproduction and limits

Run `python verify.py` with Python 3 and no third-party packages. The program terminates with `VERIFICATION_OK` after **754 exact assertions**, using `fractions.Fraction` throughout. Its first check independently enumerates the full leaf-splitting history space from one through nine leaves (\((n-1)!\) equally likely sequences at size \(n\)) and calculates the cherry count and the Sackin edge-depth sum for every resulting rooted ordered binary tree with integer history multiplicity. It verifies expected values, cross-covariance, variances and the finite regression coefficient.

A separately implemented root-decomposition moment recurrence verifies the same formulas for every \(3\le n\le120\), and checks the established Sackin variance for every \(2\le n\le120\). The checker validates the statement's finite algebra but makes no claim that tests at finitely many sizes prove its infinite extension. The complete induction is in `RESULT.md`.

The numerical coefficient in the limiting Pearson correlation comes from the established Yule Sackin-variance formula and the exact cherry variance; it does not represent a Monte Carlo estimate. All fractions are exact in the verifier, whereas the displayed decimal is rounded. No independent examination has yet been carried out.
