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

The exact proof is contained in RESULT.md. To reproduce finite checks, run `python3 verify.py` using the Python standard library; the observed output in this run was `VERIFY_OK 1215`. The tests evaluate 400 seeded nondegenerate parallelograms by independent angular midpoint quadrature (8192 points each), compare the closed second-moment formula, check derivative bounds and bisection inversion, and verify the optimal limiting slope numerically at 15 endpoint configurations. The script verifies finite examples only. Positivity of the derivative, its strict decrease in the side product, endpoint sharpness, and universal identification are established analytically in RESULT.md.
