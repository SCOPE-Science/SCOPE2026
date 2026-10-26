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

# Verification and limits

The accompanying `verify.py` was executed against the actual file contents before packaging. The independent finite checker directly evaluates Rule 250, detects the first repeated state, and compares actual preperiods with both the cyclic-gap formula and all coefficients of the proposed bounded-composition polynomials.

Expected recorded output from the supplied checker:

```
VERIFY_OK exhaustive_binary_configurations= 131064 random_larger_cases= 4800 cumulative_fixed_density_histogram=verified
```

The exhaustive check covers every labelled configuration for each ring size \(3\le n\le16\), totaling 131,064 configurations. A deterministic pseudorandom check covers 4,800 configurations on twelve larger ring sizes (17, 18, 19, 20, 24, 31, 32, 41, 48, 63, 64, and 101). It also verifies absence of periods above two among tested orbits, exact maximal-preperiod counts, and the counts of initially periodic states.

Finite tests cannot prove the formula for arbitrarily large rings. The infinite-size argument is the reachability identity, the gap-covering criterion, the periodic-state characterization, and exact rooted cyclic-gap enumeration in `RESULT.md`. No independent audit was conducted.
