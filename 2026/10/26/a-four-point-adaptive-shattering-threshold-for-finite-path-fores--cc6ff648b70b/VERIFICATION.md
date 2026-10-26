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

# Reproducibility and scientific limits

The accompanying JSON certificate contains the local paths, static VC query witnesses, and a complete adaptive decision-tree witness for each component size from one to five. Execute:

```
python3 generate_certificate.py
python3 verify_betweenness.py finite_betweenness_certificate.json
```

A separate executable verifier enumerates every unoriented labeled path and every nonredundant strict ternary-betweenness query. It verifies all explicit static and adaptive witnesses, checks all sets of one more than the asserted VC dimension, and checks the hypothesis-count upper bound on the adaptive dimension. The actual verified output is stored as `verification_output.txt`. Expected final line: `BETWEENNESS_CERTIFICATES_ALL_PASS`.

The unrestricted component-count claim uses the mathematical additivity argument in `RESULT.md`, not extrapolation from tests. No computation covers individual connected path components larger than five, unknown component partitions, or full historical priority. Independent external review has not been performed.
