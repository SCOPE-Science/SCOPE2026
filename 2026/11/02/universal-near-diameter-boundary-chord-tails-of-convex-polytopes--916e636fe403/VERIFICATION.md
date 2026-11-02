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

# Verification scope

The mathematical proof is given in `RESULT.md`. The supplementary source `verify.py` requires Python 3 and NumPy and performs exact rational cone-weight evaluations in 20 dimensions, plus geometric importance-sampling diagnostics for tetrahedral, four-simplex and cubic boundary samples. Use:

```
python verify.py
```

Expected successful output begins `VERIFY_OK exact_dimensions=2..21 cube_dimensions=2..21 tetrahedron=8 cube3=3/4 octahedron3=1/4` and then prints finite-\(\varepsilon\) diagnostic values. Sampled diagnostics are reproducible with the fixed seed used in the source. Exact rational checks do not rely on the random generator. The code was run successfully with the included source prior to packaging. The verifier is not a theorem prover for arbitrary polytopes; its computations are corroboration for the explicit benchmark formulas. The uniform-in-\(\varepsilon\) error bound and positive cone truncation are verified analytically in the written proof.

Independent audit was not performed.
