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

# Reproducibility

Run `python3 verify.py` in a directory containing the accompanying standalone script. Successful output is:

```
PASS: normalized noncoprime-seed indices: 2640
PASS: state and witness checks: 68094
PASS: independently recomputed modular inverses: 68094
PASS: parity-period comparisons: 58782
PASS: exhaustive small Diophantine searches: 9269
```

The checker iterates \(2\le k\le14\), selected coprime seeds \(1\le a<b\le31\), and 18 recurrence indices per seed; direct Diophantine enumeration is restricted to small target values. It also tests normalized noncoprime seeds for \(2\le k\le12\). Computations check the recurrence transport and boundary cases but are not infinite proofs. The proof in `RESULT.md` supplies the universal argument. No independent mathematical audit has been performed.
