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

## Reproduction
Execute `python3 verify.py` in a directory containing that file. No optional packages or network requests are needed. For the odd prime fields \(q=3,5\), the checker enumerates all nonzero traceless matrices; independently computes Lie brackets and ranks for every unordered pair; classifies invariant projective eigenlines; checks the complete adjacency matrix against the proposed quotient labels; verifies component-size multisets and degree distributions; and recomputes the middle-graph integer Laplacian characteristic polynomial with Faddeev–LeVerrier elimination. Its final line is `VERIFY_OK`.

## Observed output
```
EXACT_CHECK_OK q=3 vertices=26 components=4 middle_order=10
EXACT_CHECK_OK q=5 vertices=124 components=11 middle_order=21
VERIFY_OK
```

## Unproved computational limits
This executable tests two prime fields, not arbitrary prime powers or unbounded field sizes. The all-odd-prime-power claim is proved symbolically by the invariant-line and incidence-matrix arguments in RESULT.md. No independent external review was performed.
