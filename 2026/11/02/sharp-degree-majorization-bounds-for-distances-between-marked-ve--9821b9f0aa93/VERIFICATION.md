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

# Verification of exact path-distance and majorization identities

Run `python3 verify.py` with Python 3 and only its standard library. The program enumerates all Prüfer words for labeled trees of sizes \(2\le n\le8\), grouping them by the complete assigned degree vector, then compares exact rational upper tails of marked pair distance to the closed formula. It also checks every integer Robin-Hood balancing transfer on all nonnegative unmarked excess vectors of length \(2\le N\le8\) and total at most \(N\); finally it checks all sharp profile extremal tail and mean inequalities on nonnegative excess vectors of length \(1\le N\le9\) and total at most \(N\).

The executed code reported:

```
Prüfer exact group tail assertions: 15591
All Robin-Hood e_k identity assertions: 1272258
All sharp-extrema and mean assertions: 704114
TOTAL EXACT ASSERTIONS: 1991963
```

All assertions passed using exact integers or `fractions.Fraction`; none uses floating point, random sampling, or an external database. Direct Prüfer enumeration is independent of the weighted-forest derivation. These tests do not replace the infinite proof, do not verify literature priority, and are not independent scientific audit. The uniform model, fixed assigned degrees, and both marked endpoints must be preserved for the checks to apply.
