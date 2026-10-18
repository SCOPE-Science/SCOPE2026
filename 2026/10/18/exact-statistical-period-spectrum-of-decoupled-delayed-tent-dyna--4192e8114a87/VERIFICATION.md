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

The text `RESULT.md` proves the finite affine permutation formula for all integers \(d\ge2\) and \(p=2^n\), given the published exact one-dimensional tent-map band decomposition. The product exactness deduction is written out; it is not inferred from numerical data.

Run the included `verify_cycles.py` with Python 3 (standard library only). Its stdout is preserved verbatim in `verification_output.txt`. The independent finite enumerator checks 18 choices of \((d,p)\), 230 iterate fixed-count comparisons, the Burnside orbit sum and every Möbius-inverted period count. Exact rational arithmetic separately checks a four-band interval cycle for slope \(11/10\) and verifies pairwise disjointness and forward interval images.

The finite tests do not constitute proof of every dimension or slope. The critical published premise is the one-dimensional exact \(2^n\)-band return theorem; the new all-dimension extension follows analytically from tensor-product exactness and the permutation-count argument. Exceptional singular initial distributions and off-core initial points are outside the claim. Independent external validation has not been performed.
