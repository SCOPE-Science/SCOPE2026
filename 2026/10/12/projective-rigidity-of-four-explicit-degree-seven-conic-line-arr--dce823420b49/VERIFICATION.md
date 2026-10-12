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

The exact checker `verify.py` uses only Python's standard library. It verifies the factorization giving the four intersection parameters, constructs the unique projectivity associated to each of the \(24\) frame permutations, and checks quadratic forms by the matrix identity \(Q(Mv)=v^T(M^TAM)v\).

Expected successful summary:

- pair stabilizer order: \(4\);
- pair-swap coset size: \(0\);
- triple stabilizer order: \(1\);
- four distinct bitangent lines;
- terminal marker `VERIFY_OK`.

The finite enumeration is exhaustive because four points in general position determine a unique projectivity. It proves only the stated stabilizer and projective-equivalence claims for the four explicit representatives.
