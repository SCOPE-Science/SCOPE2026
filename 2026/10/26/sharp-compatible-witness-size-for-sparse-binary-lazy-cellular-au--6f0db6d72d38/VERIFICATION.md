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

# Verification of the compatibility-witness theorem

Run `python3 verify.py` using Python 3.10 or later; standard library only. The script uses literal integer neighborhoods, directly checks both defining compatibility conditions, independently constructs a local two-step non-idempotence witness, and compares the directed-graph closure criterion with direct compatibility checks.

Observed output:

```
PASS family-subsets: 2035
PASS small-ambient patterns: 577
PASS graph-closure equivalences: 1646
PASS total assertions tested: 4258
```

The family-subsets test checks every one of the \(2^k-1\) nonempty subsets for each \(2\le k\le10\). The small-ambient check enumerates all binary patterns with \(p(0)=0\) on supports of size at most four inside \([-4,4]\), and excludes a compatible set without a compatible singleton. The graph test varies supports, patterns, and subsets in a separate finite universe. The universal bounds and all-parameter construction are established by the mathematical proof in `RESULT.md`, not by extrapolating from computation. No independent audit has been performed.
