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

Run the standalone program with a Python 3 interpreter:

```sh
python check_frobenius_quadric.py
```

Expected terminal marker: `FROBENIUS_QUADRIC_EXACT_OK`.

The exact finite tests cover primes \(5,7,11,13,17,19\), checking all rational points on the split quadric, their inclusion in the cyclic surface, the number of rational singular points, the derivative gcd of the infinity restriction, and two rational tangent-cone directions at every rational node. Algebraic proof over the algebraic closure uses the polynomial identities and Frobenius diagonalization in RESULT.md; enumeration by itself cannot certify the geometric \(4p\)-node count, all-prime smoothness, or geometrical irreducibility. No independent external mathematical audit is claimed.
