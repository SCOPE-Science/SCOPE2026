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

# Reproduction and mathematical limits

Run `python3 verify.py` with Python 3 and no non-standard packages. The script confirms the characteristic-five formal polynomial expansion of the Cartier coefficient matrix; enumerates the marked smooth coefficient pairs over \(\mathbb F_5\); checks direct Cartier rank and stable rank of its fourth power over \(\mathbb F_5\); constructs extension fields of degrees \(1,2,3,4\) using explicit polynomial moduli and verifies their irreducibility; counts all affine solutions and both rational points at infinity; and reconstructs the degree-eight zeta numerator using Newton identities and the Weil functional equation.

Expected prints include `F5_PARAMETER_CENSUS {(0, 0): 12, (0, 1): 2, (1, 0): 2, (1, 1): 1}`, `POINT_COUNTS_F5_TO_F625 [6, 36, 126, 576]`, `ZETA_NUMERATOR_COEFFICIENTS [1, 0, 5, 0, 0, 0, 125, 0, 625]` and `VERIFY_OK`.

These computations do not enumerate infinitely many algebraic-closure parameters. The proof in `RESULT.md` independently covers every smooth geometric parameter using Cartier semilinearity and the factorization on \(U=0\). The finite-field enumeration exactly determines the zeta polynomial at the one special \(\mathbb F_5\) curve, because four extension counts and functional reciprocity suffice for genus four. No independent audit or independent validation has been performed.
