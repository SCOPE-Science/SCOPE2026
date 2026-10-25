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

# Verification record

The scientific argument is a finite-case **proof schema** valid for all factor sizes \(p,q\ge3\): any nonclique triple shares a row or column, and the three explicitly listed canonical induced paths cover all possible equality patterns. Every adjacency and non-chord statement is checked directly from coordinate inequality. Clique classification then gives both finite-sum polynomials for the whole infinite family.

The supplied standalone executable `verify.py` builds the adjacency matrix, generates every induced path, detects each forbidden triple, tests all \(2^{pq}\) subsets and tests inclusion maximality. Running `python3 verify.py` from the extracted artifact directory produced the following exact lines:

```
PASS p=3,q=3: all={0: 1, 1: 9, 2: 36, 3: 6}; maximal={2: 18, 3: 6}; induced-path-forbidden-triples=78
PASS p=3,q=4: all={0: 1, 1: 12, 2: 66, 3: 24}; maximal={2: 30, 3: 24}; induced-path-forbidden-triples=196
PASS p=3,q=5: all={0: 1, 1: 15, 2: 105, 3: 60}; maximal={2: 45, 3: 60}; induced-path-forbidden-triples=395
PASS p=4,q=4: all={0: 1, 1: 16, 2: 120, 3: 96, 4: 24}; maximal={2: 48, 4: 24}; induced-path-forbidden-triples=464
VERIFY_OK
```

These finite computations provide implementation regressions and independently confirm boundary examples. They do not claim exhaustive verification for arbitrary size or any independent third-party validation. Inaccessible/unindexed prior literature could affect priority, not the correctness of the displayed combinatorial proof.
