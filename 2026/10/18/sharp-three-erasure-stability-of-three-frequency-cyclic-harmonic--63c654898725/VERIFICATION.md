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
The analytical derivation in RESULT.md supplies the all-order proof. The standalone `checker.py` is standard-library-only. Running `python3 checker.py` enumerates all unordered three-erasure subsets in all orders from \(6\) to \(48\). It independently computes Gram eigenvalues with a Jacobi method, compares the derived formula, checks that every maximizing mask is cyclically consecutive and that exactly \(N\) such masks exist for each tested order, and confirms that retained lower bounds are positive. Recorded output is provided in `checker_output.txt`.

The numerical tests are intentionally finite and use floating-point trigonometry and eigenvalue calculations; they provide corroboration only, not an infinite certificate. The all-order argument is purely analytical and includes exact elementary treatment of the two exceptional small cyclic orders. The first-public-date provenance for the motivating frame-erasure paper is arXiv:1801.04548v1 (2018-01-14). Independent scientific audit has not been performed.
