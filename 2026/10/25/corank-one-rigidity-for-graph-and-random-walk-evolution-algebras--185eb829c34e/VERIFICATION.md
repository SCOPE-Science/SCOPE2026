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

# Reproducibility

The standalone `verify.py` uses only the Python standard library. Execute `python3 verify.py` in the directory containing the research files. The checked run returned:

```
VERIFY_OK {'with_twins': 4129, 'twin_free': 2700, 'regular_or_biregular': 3, 'neither': 6826}
```

It enumerates connected labeled graphs of orders three through six with adjacency nullity one and checks the unique-false-twin and degree-pattern dichotomies. It also inspects the diamond, a twin-free path, and the nullity-two star. This does not constitute an exhaustive test of graphs of arbitrary order, nor a computer proof of the theorem. The universal proof is in RESULT.md.
