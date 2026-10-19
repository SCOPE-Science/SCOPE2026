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
# Verification

The quantitative periodic-orbit theorem is proved for all finite complete prefix codes and every positive code length by a constructive de Bruijn/decoder-cycle argument. The checker below is an additional finite consistency test, not a replacement for the infinite proof.

Run with a standard Python 3 interpreter:

```text
python artifacts/verify_prefix_orbits.py
```

The actual checker run completed with `VERIFY_OK pair_checks 5091068`. It verified the de Bruijn factor property, completeness of six finite codes, existence and primitivity of parsed cycles, the lower bound on their codeword periods, and the required strict inequality for all pairwise common-codeword-prefix lengths. It covered four binary codes through span 9 or 10 and two ternary codes through span 7. The planar realization is established separately by exact forward-invariant rectangles and first-level distances, without reliance on floating-point approximation.

The finite diagnostic does not exhaust all finite codes, all spans or infinite sequences. The proof and cited established self-similar measure theorem carry the generality. No external independent audit has been performed.
