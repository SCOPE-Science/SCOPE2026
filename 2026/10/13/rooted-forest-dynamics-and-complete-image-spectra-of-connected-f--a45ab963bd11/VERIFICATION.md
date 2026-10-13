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

# Verification record

The fresh standalone verifier `verify_kd45.py` was executed locally with Python 3. It uses independent function-table enumeration rather than constructing maps from the closed-form characterizations. It tests all finite connected KD45 frames of total size at most six: 296,675 candidate function tables, of which 15,403 were bounded endomorphisms by direct successor-set testing. It compared ordinary image, idempotent image and eventual-image distributions against the three formulas and checked total counts.

The hom-set experiment enumerated 100 ordered source-target pairs whose component sizes sum to at most four on each side. The direct modal-algebra experiment checked 550 cases by evaluating the diamond operation on every subset of the finite target set. The completed replay printed:

```text
VERIFY_OK function_tables 296675 bounded_maps 15403 hom_pairs 100 modal_algebra_checks 550 exact_comparisons 205
example_c2_s3 ([16, 114, 108, 12], [8, 27, 12, 1], [100, 90, 48, 12])
```

The coefficients correspond to the number of endomorphisms at algebra-image sizes \(2^{c+j}\); the second line gives \(j=0,1,2,3\) for \(c=2,s=3\). Both finite-enumeration limits and general mathematical proof are explicitly distinguished. Reproduce using `python3 verify_kd45.py` beside this file. No external certification has been sought.
