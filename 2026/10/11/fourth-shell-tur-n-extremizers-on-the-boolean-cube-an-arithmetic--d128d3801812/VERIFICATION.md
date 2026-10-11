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

# Verification record

The proof uses Walsh positivity, full symmetry averaging, the published harmonic-slice basis theorem, and exact restricted-Walsh multipliers. The standalone `checker.py` is executable with the Python standard library and returns `CHECK_PASS` after exact checks. It verifies 5,115 Krawtchouk identities, 988 minimizing-weight/dimension cases, 16,438 nonzero contrast evaluations, and 72 rational Fourier inequalities for the explicit nonradial dimension-19 extremizer. The indicated computations do not establish an infinite theorem by themselves; the proof gives the infinite-dimension reduction and the square-resonance characterization. No independent audit was performed. The case \(d<13\) is not claimed.
