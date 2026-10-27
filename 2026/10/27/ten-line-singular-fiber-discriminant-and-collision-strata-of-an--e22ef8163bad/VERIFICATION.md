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

# Verification and reproducibility

Run `python3 verify_fano_fibers.py` using a Python 3 standard-library interpreter. The checker computes exactly, with integer vectors, the ten equality lines of the five eigenvalue forms, all projective pairwise line intersections, their eigenvalue-multiplicity partitions, the line-incidence profile, and the independent degree-four Chern-class and topological-stratification Euler computations.

Expected verification output:

```
VERIFY_OK lines=10 triple_points=10 double_pair_points=15 singular_base_points=25
VERIFY_OK generic_line_fibers=10 each_two_A1 total_nodes=20
VERIFY_OK c4=5g4+4hg3+4h2g2 euler_from_Chern=24 euler_from_fibers=24
```

The exact enumeration checks the finite ten-line intersection arrangement only. The proof of the singularity type \(A_1\), smooth quadrics and conic intersection uses the symbolic projective Jacobian and the analytic quadratic normal form in `RESULT.md`. The Euler computation presupposes these geometric fiber types, and agreement with Chern classes is a consistency test, not a substitute for the proof. No independent audit or external theorem certification has been performed.
