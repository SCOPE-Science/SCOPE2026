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

# Verification instructions and boundaries

Run `python3 verify.py` with a standard Python 3 interpreter. The script uses only the standard library and constructs all periodic factors of bounded length directly. It independently enumerates minimal absent words and bispecial factors, checks every ordered zero-gap triple with all three gap lengths from zero through nine, and checks fixed-length extrema for lengths three through thirty-three.

Successful execution prints exactly these two lines:

```
PASS: ordered triples: 1000 max gap: 9 max word length: 30
PASS: extremal ranges and maximizer classification at lengths 3..33
```

The mathematical proof is in `RESULT.md`. The checker is finite, does not assert exhaustive verification over all nonnegative gap triples, and cannot establish novelty or independent certification.
