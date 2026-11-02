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

`python verification/check.py` was executed on the bundled checker before publication packaging. It printed `PASS: 218 exact rational assertions; full tuple/BSC identities verified for n=3,k=2`.

The code uses exact rational probabilities and enumerates the clause sign patterns directly, rather than assuming the claimed monotonicities. Independent finite checks include single-clause equality, strict ordinary moments for two or three clauses, weak factorial moments, and the noise-convolution identity on every pair of assignments of three variables.

Finite enumeration is not a proof at arbitrary `n,k,m,r`; the mathematical proof in RESULT.md covers the infinite parameter families. No independent audit has been performed.
