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

Run `python3 verify.py` from the directory containing this document. The program depends only on the Python standard library. It evaluates the unique fold equation by bisection, checks fixed-point and derivative-one identities, verifies monotonicity over a finite parameter grid, and independently counts sign changes on both open branches away from neutrality. It was run successfully with output `PASS 591 checks`.

The four-root demonstration at \((a,b,c)=(1/100,1/2,99/100)\) is independently certified by the exact integer inequality \(3\cdot297^2>500^2\). This exact finite witness and the computational sampling do **not** establish the all-parameter theorem; the uniform proof uses the strict positivity of the derivative of the critical numerator, elementary monotonicity and the implicit-function expansion given in `RESULT.md`.

The primary cosine map equation, domain and switching-point value were checked from the full 2023 published text. The separate 2024 follow-up paper's institutional accepted-manuscript PDF could not be opened, so its abstract rather than full mathematical argument was compared. No independent external audit has been performed.
