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

The standalone script `verification/check.py` uses rational arithmetic to construct diagonal Kronecker sums of canonical nilpotent Jordan blocks. It compares their exact kernel dimensions against the Laurent-coefficient formula for seven block families, for all feasible exponents \(1\le r\le3\) with dimension at most 64. It checks the normalized character and squared-weight moment, then compares the exact coefficient ratio at \(r=100\) to the predicted Gaussian leading term in five nontrivial families. Successful execution prints `VERIFY_OK`.

The algebraic and asymptotic proofs in `RESULT.md` establish the unrestricted statement. Finite tests cannot prove the infinite-power result. The local central limit proof depends on the finite-support symmetric character distribution and its lattice span; no floating-point numerical observation is used to justify this step.
