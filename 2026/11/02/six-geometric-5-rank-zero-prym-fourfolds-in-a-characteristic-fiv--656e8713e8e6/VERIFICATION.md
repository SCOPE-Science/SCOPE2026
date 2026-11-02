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

# Verification record

The direct proof is given in RESULT.md. Run `python3 verify_cartier.py` (Python standard library only) to reconstruct the seven-by-seven fifth-root semilinear Cartier matrix from polynomial coefficients over \(\mathbb F_{25}=\mathbb F_5[t]/(t^2-2)\). All 25 coefficient pairs in the field are enumerated: 23 give smooth curves, 6 of these have Prym geometric \(5\)-rank zero and 17 have Prym rank two, while two parameters are singular. The quotient has stable rank two, the curve has rank two or four, and the \(a\)-numbers are 1, 2, and 3 for quotient, Prym, and curve, respectively.

Successful exact execution reports `GENUS7_TRIGONAL_CHAR5_CARTIER_EXHAUSTIVE_GF25_OK`. These finite-field checks are corroboration. The all-parameter result depends on the proved coefficient identities, smoothness criterion, isogeny comparison, and semilinear stable-rank calculation. A separate independent mathematical audit has not been performed.
