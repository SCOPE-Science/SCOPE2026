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

# Reproduction and limits

Run `python verify.py` with Python 3, using only its standard library. The checker tests 78 sizes from 3 through 80 and heights 0.1, 1, and 3. For each size/height it constructs all candidate supporting facets, checks they support the full vertex configuration and have the expected incidence sizes, constructs every maximal consecutive illumination block for both layers, checks full ordinary covering by partition blocks, and verifies cyclic fractional multiplicities. It also tests sampled generic directions against the one-layer and capacity restrictions. The execution produced:

`VERIFY_OK antiprism n=3..80, h=0.1,1,3; regression_checks= 143208`

This is a numerical regression check with explicit tolerances, not a formal exact-arithmetic certificate or evidence for every integer size and every positive real height. The quantified result follows instead from the exact facet-normal formulas, strict trigonometric cap bound, nonempty vertical-parameter interval, and combinatorial partitions proved in `RESULT.md`.

The only unperformed checks are independent scientific review and comprehensive historical priority determination. In particular, a finite geometry test is not a substitute for either.
