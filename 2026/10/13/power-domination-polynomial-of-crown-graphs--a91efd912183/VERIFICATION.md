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

The proof was stress-tested by the standalone `verify.py`. For each \(n\) from \(3\) through \(8\), the checker constructs \(\operatorname{Cr}_n\), enumerates every vertex subset, runs the standard domination step and forcing rule to closure, and compares the result with the claimed classification. It also compares every coefficient against the closed formula, evaluates the total count, and checks the minimum layer.

Observed output:

`VERIFY_OK n_range=3..8 subset_checks=87360 coefficient_checks=66 total_checks=6 minimum_checks=6 max_order=16`

The exhaustive computation is finite and does not certify the theorem for arbitrary \(n\). The general proof is the symbolic neighborhood-count argument in `RESULT.md`; the computation checks boundary cases and guards against algebraic/counting errors through order sixteen.
