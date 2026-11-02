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

# Verification and boundaries

The proof is symbolic for every prime power \(q\ge2\). Its crucial steps are the Frobenius-square rationality of all geometric lines, the isotropic-line identity for the second Fermat polynomial, the exact equality between complete-intersection degree and total generator degree, Cohen--Macaulay generic reducedness, and the two-row Jacobian criterion.

Run `python3 verify.py` with the Python standard library. The executable enumerates every \(\mathbb F_{q^2}\)-rational two-plane in \(\mathbb F_{q^2}^4\) for \(q=2,3\), filters precisely by Hermitian isotropy, confirms that the second equation vanishes, computes every rational point and its line-incidence multiplicity, and checks arithmetic genera. Its successful output is:

```
q=2 FIELD=4 RATIONAL_POINTS=45 GENERATOR_LINES=27 GENERATORS_PER_POINT=3 DEGREE=27 ARITHMETIC_GENUS=109
q=3 FIELD=9 RATIONAL_POINTS=280 GENERATOR_LINES=112 GENERATORS_PER_POINT=4 DEGREE=112 ARITHMETIC_GENUS=1569
VERIFY_OK
```

These two finite cases corroborate, but do not by themselves prove, the uniform theorem. The claim of an exact ideal is supported by the degree, purity, and reducedness argument, not a finite set of point tests. Literature-priority uncertainty remains, and no independent scientific audit has been performed.
