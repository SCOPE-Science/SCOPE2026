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

# Exact reproducibility checks

Run `python3 verify.py` in the same directory (Python standard library only). The code explicitly constructs the nine cyclotomic factors of \(X^{4q^2}-1\), enumerates all 512 monic divisors for each of \(q=3,5,7,11,13\), evaluates coefficient heights, and enumerates all 64 monic low-level divisors and their residue-slice \(\ell^1\) norms. It verifies the exact factorization and coefficient of the sharpness witness and returns `VERIFY_OK` on success.

The finite runs are exact integer operations rather than floating-point estimates. They do not constitute exhaustive proof over infinitely many primes. The universal claim rests on the residue-slice proof in RESULT.md. No independent audit has been performed.
