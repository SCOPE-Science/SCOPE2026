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

# Reproducibility and verification

Run `python3 verify.py` using the Python 3 standard library; no external dependencies are required. The checker uses exact rational arithmetic with a fixed seed for generated examples. It reconstructs terminal population from both direct iteration and the closed reciprocal formula at each eligible pulse date. It checks strict convexity at interior dates, all endpoint comparisons, direct threshold ties for rational-square growth factors, and the exact dose necessary to reach a terminal target.

Actual execution produced:

```text
PASS: 1332 exact rational parameter cases; 7992 placement identities; endpoint comparisons, convexity, exact target dose and ties.
R=3, n=4, s=1 threshold x=1/5; x=1/10: first; x=1/5: tied endpoints; x=3/10: last.
```

These are finite checks. They cannot certify the full theorem for all real inputs. The universal correctness argument is the direct algebra, the strictly convex timing weight, the exact endpoint difference, and the positive discrete difference for subcritical growth, all included in `RESULT.md`. The source-comparison limits and no-independent-audit status are recorded in the other accompanying research documents.
