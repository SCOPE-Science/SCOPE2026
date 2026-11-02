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

The unrestricted mathematical argument is given in RESULT.md. The independent derivations used for a computational cross-check are the composition recurrence and the exact formal-power-series factorization. Execute `python verify.py` using Python 3, with no third-party packages.

The verifier checks all coefficients through index \(2047\) modulo \(2^9\) by two different methods: recurrence, and a truncated geometric series formed from \(S(z)/z\) and \(T(z)/z\). It checks the vanishing criterion for every index in \(0\) through \(2^{19}-1\) at each precision \(1\) through \(9\), including nonvacuous high-weight cases.

The standalone verifier must complete with `VERIFY_OK`; exact observed output is reproducible by rerunning the code. The tests are finite and cannot certify the theorem for all indices or rule out overlapping research. The proof, source comparison, and known limitations determine the review outcome. No independent audit has been performed.
