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

Execute `python verify.py` in the extracted package directory. The standalone checker builds independent finite forbidden-word matrices, compares their leading eigenvalues with the single-word autocorrelation equation for every word at bases and lengths \((b,n)=(2,5),(2,6),(3,4)\), and enumerates least word periods to cross-check the primitive-count Möbius formula. It also computes the scaled escape-rate variance for \((b,n)=(2,12),(2,14),(3,7),(3,8)\). The actual checker execution returned `VERIFY_OK`.

The analytic argument for arbitrary length requires the dominant-root bound uniform over words, Fine–Wilf decomposition, and absolute convergence of the primitive orbit series. The code verifies finite identities and examples, not the infinite asymptotic or originality. Independent audit is not performed.
