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

Execute `python verify.py` alongside this document with Python 3.9 or later. The program needs only the Python standard library. It computes periodically stationary initial occupancy via affine-map composition, then exact rational integrated turnover excess and exact exchange identities.

At preparation the program printed:

```text
PASS: 1080 exact rational test sets for reversal, nonnegative excess, three/four-block formulas
PASS: all 24 four-block arrangements and exact example
Exact excess extinction levels: 3/25 46/375 49/375
```

The numerical example's full expected events are those excess values plus the common equilibrium baseline \((4/5)\log 2\). The proof for arbitrary strictly positive real rates, positive durations and all finite season counts is analytic; rational sampling is not an exhaustive proof or a substitute for the derivation. For exact symbolic polynomial-identity verification, install the optional dependency with `python -m pip install -r requirements.txt` and run `python symbolic_check.py`; it separately expands both four-block exchange identities into zero rational functions. The symbolic script was run successfully. Neither biological field data nor an independent mathematical audit is supplied.
