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
# Reproducibility and limits

Run `python3 verify.py` with Python 3. The script has no third-party dependencies. It enumerates every residue/tangent assignment for four small parameter sets, computes the tangent-matrix ranks over prime fields, extracts the exact exponential-generating-function coefficients with rational arithmetic, and compares the two type-count dictionaries. It also checks that the total number of tuples is \(q^{2\ell r}\).

The finite checks are not a proof for arbitrary parameters. The all-parameter proof is in `RESULT.md`: residue interpolation and idempotent lifting give the product decomposition; rank counts give each block weight; the exponential generating function then counts labeled coordinate assignments. Independent audit has not been performed.

The trusted importer initializes absent external channels as unperformed; research never assesses/authors them or resets old evidence.
