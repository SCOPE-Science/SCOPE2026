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

# Reproducibility
Run the two accompanying standalone programs in a Python 3 environment:

```sh
python3 verify_canonical.py
python3 verify_quotient.py
```

Expected terminal markers: `CANONICAL_HW_OK` and `QUOTIENT_AND_FIELD_OK`.

The canonical check multiplies the five-variable sparse polynomial \((QG)^4\) exactly modulo five and compares all 16 Hasse–Witt matrix coefficients as polynomials in \(\lambda\). The independent quotient check expands the hyperelliptic sextic square, extracts its 2-by-2 Hasse–Witt matrix, verifies determinant \(D\), proves degree-six irreducibility with exact gcd computations, and checks the semilinear rank over all Frobenius-conjugate exceptional roots represented in the quotient field. These algorithms check finite polynomial identities that support universal algebraic proofs; extension-field enumeration alone is not an infinite proof.

Geometric smoothness, unramified covering, genus and Prym isogeny are argued in the proof and are not replaced by numerical tests. No independent external audit or certification is claimed.
