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

# Mathematical verification

The included exact checker can be run with:

```bash
python checks/verify_conjugacy.py
```

It requires Python 3 and SymPy. It tests by symbolic identity: the original vector field at \(a=0\), the vanishing Lie derivatives of both polynomial integrals, the polynomial inverse and its constant determinant, equality of the reduced scalar vector field, the discriminant \(432\Delta\), both fold factorizations, the polynomial potential derivative, and the exact cusp trajectory. The check was executed against the embedded file's content before packaging and completed without assertion failure.

The actual mathematical justification of forward boundedness is the negative leading cubic sign; the convergence proof is scalar order preservation; the global invariant-measure conclusion follows by integrating \(\dot G=4y^2\) against any compactly supported invariant probability measure. Neither finite numerical sampling nor the symbolic checker alone establishes these global claims. The result is not a proof of behavior for \(a\ne0\).
