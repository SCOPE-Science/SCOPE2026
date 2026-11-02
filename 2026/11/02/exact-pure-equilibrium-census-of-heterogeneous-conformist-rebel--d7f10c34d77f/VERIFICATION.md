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

# Computational and analytical verification

Run `python3 verify.py` with standard Python 3. The verifier implements two checks of the theorem's input model: a direct best-response test trying all alternative actions and a separate local-condition test. It derives the closed formula from the run lengths using exact integer binomial arithmetic and compares each count with enumeration of all labeled action assignments in each tested instance.

Actual run completed:

```
VERIFY_OK direct_cases=667 direct_profiles=2406873 local_cases=1252 local_profiles=14438529 periodic_r=1..8 arrangement_pairs=2
```

The direct comparisons include \(m=3\) and \(3\le n\le8\), \(m=4\) and \(3\le n\le6\), and \(m=5\) and \(3\le n\le5\), all type words containing a rebel. The local comparisons include \(m=3\) up to \(n=9\) and \(m=4\) up to \(n=7\). Cases with run length one are checked and must return zero.

The proof is independent of the tests: the decisive steps are the three-action local best-response equivalence, the exact path-edge-cover classification, and the cycle-block coloring formula. The verifier is a finite cross-check, not an automated universal proof. No external files, solvers or network downloads are required.
