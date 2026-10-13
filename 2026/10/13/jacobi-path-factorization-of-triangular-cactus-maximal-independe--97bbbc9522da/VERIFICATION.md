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

# Reproduction and logical limits

Use Python 3.10 or later with no third-party modules:

```bash
python3 verify.py
```

The captured execution output is `verification_output.txt`. The verifier builds each triangular-chain graph by adding triangles sharing one cut vertex, enumerates every subset up to nine triangles, and tests the independent and dominating predicates directly. It separately constructs the published rational-generating-function coefficient recurrence, a monomer–dimer endpoint-weighted tiling recurrence, and the exact rational Jacobi characteristic recurrence through eighty triangles. The final line should be `VERIFY_OK exhaustive_instances=9 candidate_vertex_subsets=699048 determinant_checks_n=2..80`.

These tests are finite checks only. Infinite validity relies on the proof's exactly-one-per-triangle correspondence, the polynomial recurrence and tridiagonal determinant induction; real, simple roots and the strict spectral bound follow from elementary spectral theory. The separate originality determination requires human literature review for differently named or unindexed antecedents. This package does not provide an independent mathematical audit.
