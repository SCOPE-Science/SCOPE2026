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

# Exact arithmetic reproducibility

Run `python3 verify.py` with Python 3 and no extra packages. The checker enumerates each subgroup of the unit group for every modulus \(2^a\) with \(2\le a\le10\), generates all multiplicative cosets, calculates the centered sum by integer addition, and independently checks both spectral types and half-interval counts. The completed execution reported:

```
PASS: 126 subgroups and 4043 cosets, moduli 2^2 through 2^10.
```

The mathematical proof in `RESULT.md` is unbounded in \(a\) and establishes exhaustion and exact multiplicity. The program is finite evidence only; it does not independently certify the theorem at all exponents. No other computational data are required by the proof. Publication priority remains subject to independent review, particularly for older general-modulus distribution-vector literature.
