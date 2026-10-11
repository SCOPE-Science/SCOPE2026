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

# Reproducible verification

The theorem follows from the exact Gram identities and convex geometry developed in `RESULT.md`. The direct arithmetic checker was run from the embedded source artifact with Python's standard library:

```text
python3 check_weighted.py
p=3 triangles_each_parity=1 optimal_masks=1 Gram_checks=9
p=5 triangles_each_parity=5 optimal_masks=25 Gram_checks=225
p=7 triangles_each_parity=14 optimal_masks=196 Gram_checks=1764
p=11 triangles_each_parity=55 optimal_masks=3025 Gram_checks=27225
```

The determinant-derived barycentric weights were independently evaluated on each regular polygon, all candidate triangle triples were enumerated at the checked primes, and every diagonal/off-diagonal Gram entry was calculated directly for every classified six-frequency support. The 29,223 Gram checks and gap tests corroborate the theorem only in the tested instances; the symbolic proof is required for all odd primes. Ordinary floating-point comparisons use tolerance 2e-10; no numerical output is asserted as an infinite-domain certificate. The independent audit has not been performed.
