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

# Reproducible checks and boundaries

Run `python3 verify.py` using Python 3.9 or later. The program uses only Python's standard library, exact `Fraction` arithmetic, exhaustive Prüfer codes, and uniform fixed-size site subsets. A completed execution printed:

```text
n 4 W classes and labeled counts {2: 12, 3: 4}
n 5 W classes and labeled counts {3: 60, 4: 60, 6: 5}
n 6 W classes and labeled counts {4: 360, 5: 720, 6: 90, 7: 120, 10: 6}
n 7 W classes and labeled counts {5: 2520, 6: 8400, 7: 3150, 8: 2100, 9: 420, 11: 210, 15: 7}
A [(2, 5), (3, 5), (4, 5)] B [(2, 4), (3, 8), (4, 2), (5, 1)]
VERIFY_OK trees 18244 tree-sample-size_cases 144358 site-subsets 2238496
```

The source in the same package is the verified executable. It checks every labeled tree on four through seven vertices for every fixed site-sample size, all site subsets, both first and second moments, boundary sample sizes, and equality cases. It separately checks the six-site two-community example including the centered third-moment difference \(2/5\), and the infinite-family construction at orders six through fifteen. The mathematical proof independently establishes every integer order \(n\ge4\); finite checks are not a proof beyond the enumerated range. Source comparisons are bibliographic and mathematical, not claims of independent validation.
