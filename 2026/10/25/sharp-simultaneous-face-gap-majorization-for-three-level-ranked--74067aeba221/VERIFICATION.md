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

# Verification checks and limits

The source package contains `verify.py`, a standalone Python 3 standard-library program. Run `python3 verify.py` in the extracted directory. A successful execution reports `EXACT_OK gap_pairs=169 balancing_steps=68 independent_facets=8`.

Checks recompute polynomial counts for 169 pairs, verify 68 exact Jacobi–Trudi comparisons, and enumerate facets/vertices to recover eight small face vectors independently of the stated formulas. All computations use integer arithmetic, including modular row reduction at prime 1000003 for small 0–1 vertex configurations. In the tested dimensions the determinant bounds are below the modulus, so those ranks agree with rational affine ranks.

Finite checks do not establish the theorem in all dimensions. The generating-function and Schur-tableau arguments in `RESULT.md` provide the universal proof. The historical-priority assessment is self-review only; no independent external validation was performed.
