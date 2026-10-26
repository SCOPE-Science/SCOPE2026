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

# Reproducibility and scope

Run `python verify.py` with Python 3.10+ (standard library only). The program directly enumerates \(r\)-element vertex witnesses, obtains their edge-incidence masks, and compares exact shattering with a separately coded structural predicate.

The checker exhausted all subsets of \(E(K_n)\) for \(2\le n\le6\), for every \(1\le r\le n\); exhausted all edge subsets of cardinality at most four for \(n=7,8\), for all these \(r\); and directly enumerated all shattered edge-subset counts through cardinality four for closed neighborhoods of \(J(n,2)\), \(3\le n\le8\). It ended with:

```
VERIFY_OK uniform_starforest=PASS exact_vc=PASS triangular_enumeration=PASS
```

The independent direct-coverage enumeration is finite evidence. The theorems for unbounded \(n,r\) follow from the component-cost proof in `RESULT.md`, not from the checker. No external formal proof certification has been conducted.
