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

Run `python3 verify.py` using Python 3 with its standard library. The script constructs all matrix entries from the weighted graph definition, computes the fourth-order rational update by exact Gaussian elimination over rational numbers, and checks spectral formulas, symmetry, unit row sums, positive diagonal entries, and two quartic sign identities.

A successful replay prints `VERIFY_OK 26712 exact rational assertions`. The verified finite cases have \(3\le n\le6\), \(a\in\{1,3/2\}\), \(b\in\{0,1/8,1/2,1,5/4,3/2,3\}\), and \(h\in\{0,1/8,1/2,1,4,20\}\). Finite verification does not imply the general theorem: the exact projector decomposition and coefficient sign proof in RESULT.md supply the unbounded parameter argument.

No independent mathematical audit has been performed.
