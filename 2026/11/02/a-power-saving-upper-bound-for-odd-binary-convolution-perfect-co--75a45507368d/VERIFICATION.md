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

# Verification details

Execute `python3 verify.py` with Python 3. The verifier computes the explicit graph matching for each \(2\leq B<70\) and each \(1\leq t\leq B/2\), checking \(2m\geq B+1-t\). It also enumerates odd composite \(n<10^4\) and \(n<10^5\), using integer factorization by trial division and independently checking every ordered bit-support sum for each nontrivial factor pair. Output:

```
VERIFY_OK matching_pairs=1190 theta=0.930827083454 pi_odd_10000=130 pi_odd_100000=522
```

These counts agree with the source's Table 3. The proof is valid without these computations: the matching inequality follows from a disjoint union of paths, and the balanced-case bound uses the finite support interval and the elementary binomial count. No infinite computational certification or external audit was performed.
