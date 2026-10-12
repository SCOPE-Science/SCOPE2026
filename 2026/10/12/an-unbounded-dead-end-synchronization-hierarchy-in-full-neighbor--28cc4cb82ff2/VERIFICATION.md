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

# Verification evidence and limits

The exact finite checker is `verify.py`; execute `python3 verify.py` from its directory with Python 3 and no third-party dependencies. It enumerates every pointwise filter core on the listed factor sizes, thereby testing all finite filters on those sets, including the improper filter. The product check covers \(8{,}784\) pairs in dimensions \((1,1)\), \((1,2)\), \((2,2)\), \((3,2)\), and \(300\) reproducible seeded pairs in dimension \((3,3)\), through rank \(7\).

For every integer \(1\leq n\leq16\), it constructs the \(n+1\)-world transitive three-relation witness, checks both mixed relation-composition inclusions, checks every lower-depth closed formula at all worlds and verifies failure of the depth-\(n\) formula at the designated root. Its recorded terminal output is:

```
VERIFY_OK: 8784 finite filter-product pairs, ranks 0..7; 16 transitive counterframes, ranks 0..n+2; last witness edges R/R1=(122, 121)
```

The universal statements are established by the symbolic rectangular-union and reachability proofs, not by finite enumeration. The checker neither attempts to prove arbitrary infinite-filter behavior nor asserts an independent review.
