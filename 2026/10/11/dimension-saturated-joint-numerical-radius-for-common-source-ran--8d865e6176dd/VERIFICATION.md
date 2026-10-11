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

The analytic argument proves the sharp bound, the rank/phase equality classification for every \(m\ge2\), \(k\ge1\), and both scalar fields, and the exact spectral defect for perpendicular outputs. Its critical finite-dimensional ingredients are an averaging identity for two unit test vectors, singular-value trace domination, and an explicit \(t>1/2\) perturbation when \(q=1\) and a source-parallel output is present. All are proved in `RESULT.md`.

The attached `verify.py` is a standalone Python 3 / NumPy program and checks 70 coordinate-witness shapes, 70 strictness examples, and 1680 deterministic random Gram inequalities. It prints:

`VERIFY_OK exact_witness_assertions=210 rank_equalizers=70 nonorthogonality_tests=70 random_gram_tests=1680 analytic_global_proof_required=True`

The finite checks do not establish infinite quantifiers, literature priority, or any unrestricted index formula. No external independent validation is reported.
