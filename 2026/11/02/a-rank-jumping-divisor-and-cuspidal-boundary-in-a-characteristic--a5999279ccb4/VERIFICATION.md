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

# Algebraic verification

Execute `python verify_net.py` with Python 3 and SymPy. It computes in characteristic three and checks the transposed Hasse–Witt coefficient matrix obtained from all sixteen coefficients of \((PQ)^2\), the identity \(\det B=s\), the permanently invertible minor, the quintic-discriminant resultant, and the two specializations. The observed completion token is `CHAR3_BIELLIPTIC_NET_RESULTANT_HASSE_RANK_CUSP_EXACT_PASS`.

The certificate is a finite exact polynomial-identity check, not an exhaustive enumeration of arbitrary algebraically closed fields. Geometric connectedness, genus, local cusp type, normalization genus, Newton slopes, moduli dimension, and the exclusion of singular fibers outside \(V(\Delta)\) are justified by the independent symbolic-and-geometric arguments in `RESULT.md`. Earlier priority cannot be certified by a finite literature search. Independent audit: not performed.
