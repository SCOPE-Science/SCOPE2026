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

# Reproducible verification

Run `python3 verify.py` with Python 3.10 or later. This self-contained standard-library program uses exact rational harmonic numbers and enumerates every allocation on a size-\(K\) simplex for \(1\le K\le6\), \(1\le m\le3\), and every choice of including zero or one voter for each nonempty approval type. It directly checks the original PAV score and all valid one-seat swaps, without invoking the three-party decomposition formula. The observed output was:

```
VERIFY_OK three_party_cases=10852 known_four_party_local=7/2 global=4
```

The program separately checks the already-published four-party Example B.3 at house size two, including all feasible allocations to verify the global benchmark. Enumeration establishes only these finite cases; the unrestricted guarantee follows from the decreasing-marginal proof in RESULT.md. No independent validation has been performed.
