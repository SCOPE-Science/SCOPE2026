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

# Reproducible checks

The supplied `verify.py` is standalone Python 3 with no nonstandard dependencies. Run `python3 verify.py` in the extracted file directory. It was actually executed and produced:

```
PASS: membership recurrences and constructive witnesses for n < 100000
PASS: direct Boolean sumset enumeration for A+A, 0 <= n < 8192
PASS: direct Boolean sumset enumeration for A+B, 0 <= n < 8192
PASS: direct Boolean sumset enumeration for B+B, 0 <= n < 8192
PASS: initial exceptional set and dyadic family
```

These finite tests independently test the indexing convention, witness construction and the claimed excluded values. They do **not** prove universal completeness. The theorem for every \(n\ge0\) follows from the full residue-class proof in `RESULT.md`, especially the reduction \(4m+2\in B+B\iff 2m\in B+B\). The only classification established is for the regular paperfolding sequence indexed from zero; no external independent scientific audit has been performed.
