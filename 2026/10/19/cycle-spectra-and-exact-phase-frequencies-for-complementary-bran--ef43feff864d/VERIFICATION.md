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

Run `python verify.py` with Python 3 (standard library only). The program exhaustively enumerates all shuffles at partition sizes four through seven, tests the exact complementary-branch matrix identity, and compares root-order incidence counts against rational products. It uses Newton identities to compute the four-state witness's characteristic coefficients. Expected terminal marker: `VERIFY_OK`.

An explicit analytical proof for all integer partition sizes appears in RESULT.md. Finite enumeration cannot prove the unbounded-size statements or absolute historical priority. The spectral statement is restricted to Markov eigenvalues realized on a finite-dimensional invariant subspace; the remaining essential spectrum is not examined. No independent audit has been performed.
