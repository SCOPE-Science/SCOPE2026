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

# Exact verification

Run `python3 verify_sextactic.py` using Python 3's standard library from the directory containing this file and `verify_sextactic.py`. The script checks the characteristic-three identity in the polynomial ring over \(\mathbb F_3\), the characteristic-two Frobenius identities, all 91 points of \(\mathbb P^2(\mathbb F_9)\), the decomposition into 28 rational Hermitian points, 16 non-coordinate points and 12 coordinate points, and all three characteristic-two support points. Observed output:

```
FERMAT_48_SEXTactic_FLAT_SPECIALIZATION_IDENTITY_AND_F9_COUNTS_PASS
char3 Hermitian rational points: 28 triple-support: 16 axis-complement: 12
char2 support: 3 local algebra Hilbert function: [1, 2, 3, 4, 3, 2, 1]
```

The local-algebra assertions follow from the proved transversality and exact special-fiber equations; they are not inferred from finite-point counting. The universal exclusion of other exceptional primes and the finite-flat rank-48 assertion follow from the complete-intersection proof in `RESULT.md`. The standard-library verifier alone does not certify research priority, an intrinsic osculation interpretation in positive characteristic, or independent validation.
