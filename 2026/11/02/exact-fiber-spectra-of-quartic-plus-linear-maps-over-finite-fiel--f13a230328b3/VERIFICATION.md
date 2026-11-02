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

# Reproducibility and limits

The complete theorem has an algebraic proof in `RESULT.md`; this independent script checks instances rather than serving as an infinite proof. Execute `python verify.py` using standard Python 3. No third-party packages or data are required.

Checks actually executed: all \(a\ne0\) in fifteen prime fields \(5,11,17,23,29,41,47,53,59,71,83,89,101,113,137\); all \(124\) nonzero coefficients in the cubic extension field of size \(125\); four coefficients in the cubic extension field of size \(1331\). Each checker directly enumerates the image values and their preimage multiplicities, then compares the full five-entry histogram against the table. Extension field arithmetic uses degree-three irreducible polynomials independently found by checking their lack of roots, and is independent of the proof's quadratic-form moment method.

Observed output:

```
VERIFY_OK primes= 15 cubic_extensions= [(5, 125, 1, 1, 124), (11, 1331, 1, 4, 4)] histogram=PASS
```

Not tested by finite enumeration: infinitely many other field orders, every coefficient over size \(1331\), or any outside-theorem field congruence classes. No independent mathematical audit has been performed.
