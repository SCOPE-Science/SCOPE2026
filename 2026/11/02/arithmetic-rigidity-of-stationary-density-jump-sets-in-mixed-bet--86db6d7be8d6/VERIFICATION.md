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

The attached `check.py` uses only the Python standard library and performs exact rational arithmetic. Run `python check.py`. It enumerates three rational beta/integer-slope/probability triples through eight word lengths each; applies independent inverse-branch transfer formulas to the finite endpoint series; checks the finite-depth residual bound on a 96-point rational grid; and verifies the nonzero jump weights along the rational-beta denominator-growth orbits. The run passed all 24 depth/case combinations.

The transfer action on a step function is established algebraically in `RESULT.md`; it is not inferred from numerical tests. The infinite endpoint expansion is uniformly summable because its length-n total weight is the n-th power of a number strictly below one. The density's one-sided jump is therefore exactly the sum of its positive endpoint weights. Infinitely many distinct rational and irrational witness endpoints are proved separately. Generic density of the irrational witness orbit uses ergodicity of multiplication by an integer on the circle.

**Limits:** The checker cannot prove infinitely many distinct endpoints, generic orbit density, absence of earlier publication, or independent validation. It tests rational parameters only; the golden-ratio example is established symbolically by the proof, not floating-point evidence.
