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

Run `python verify.py` after installing the version-compatible dependency from `requirements.txt`. The script uses SymPy's exact integers, rationals and algebraic complex expressions; it invokes no remote service.

Actual replay output:

```
VERIFY_OK: scalar Padé/derivative identities; exact four-site crossover; 87 exact weighted-star matrices; 846 exact off-diagonal entries evaluated; 324 exact hub-entry sign tests
```

The program independently constructs the weighted star Laplacian and evaluates the completed matrix rational function, checks symmetry and unit row/column sums, tests exact center-entry signs against the declared scalar factor, verifies relevant leaf-entry positivity, checks strictly positive diagonal entries, and tests explicit four-site rational and complex-resolvent identities. The program does not enumerate all weights or all star sizes. Generality is established by the five-step mathematical proof in `RESULT.md`, including Schur complementation, sector geometry, and monotonicity. No external or independent audit was performed.
