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

# Verification of the cube-center theorem

Run `python3 verify_cube_extension.py` in the same directory. The standard-library verifier was run from its real packaged source before inclusion, and returned:

```
VERIFY_OK distance_witness_pairs=86360 scalar_checks=73
thresholds_d2_d3_d4=0.611516173 0.352841879 0.191981864
scaled_d16_d18=3.038001796 3.018384721 limit=2.885390082
```

The 86,360 ordered-pair comparisons cover every distinct pair of vertices in dimensions one through seven at four test exponents. They check the metric distance-to-vertex extremizer and exact binomial sum. The other tests bracket the threshold in dimensions two through eighteen and check explicit low-dimensional identities. The proof in `RESULT.md` separately establishes the global operator minimum, unique threshold for all integers \(d\ge2\), and the asymptotic estimate, which no finite computation can certify. Calculations use floating-point tolerances stated in the script; no machine-checkable formal proof is claimed. No independent audit has been performed.
