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

# Reproducibility checks

Run `python3 verify.py` using Python 3 standard library only. The program enumerates all edge orientations for complete graphs with \(2\le n\le6\), cycles with \(3\le n\le11\), and friendship graphs with \(1\le r\le4\), then checks exact integer/rational identities. The complete-graph score-majorization inequality is checked for every subset-size prefix for every orientation, along with the \(q\)-moment domination for integer \(1\le q\le5\). Cycle support bounds and attaining orientations are checked. The friendship center/leaves pointwise bounds and explicit probability-\(2/3\) witness distribution are verified for the same integer moments.

Observed output:

```
PASS: exact orientation inequalities and explicit norming moments
{'complete_majorization': 168146, 'complete_power_bounds': 169330, 'cycle_support_bounds': 4088, 'friendship_pointwise': 23400, 'friendship_moment_witness': 20}
```

Every tested identity follows from exact arithmetic. These are finite tests of needed ingredients, not an exhaustive argument over all graph orders or all real \(p\); the universal result is supplied by the analytic proof in RESULT.md. No outside human or independent certification was performed.
