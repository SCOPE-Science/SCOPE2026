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

# Reproducible verification

Run `python3 affine_frobenius_verifier.py` with Python 3 and no third-party packages. The program constructs extension fields using independently checked irreducible polynomial moduli, enumerates all affine coefficient pairs, extracts complete functional graphs, and compares the observed cycle multiplicities, type totals, and type distinctness against the formulas.

The observed output ends with:

```
VERIFY_OK all_cases= 15 all_affine_maps= 28076
```

The cases cover primes \(2,3,5,7\), degrees up to six, coprime and noncoprime Frobenius exponents, and fixed fields of orders \(2,3,4,5,7,8,9\). The computational check is exhaustive only for these finite parameter cases. The proof for every prime and arbitrary positive \(m,r\) uses relative norms, multiplicative and additive Hilbert 90, and Möbius inversion as described in RESULT.md. The implementation contains no external certificate and provides no claim of independent mathematical audit.
