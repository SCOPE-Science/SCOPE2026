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

# Reproduction and checks

Execute `python3 verify.py` from the extracted directory. The script needs Python 3 standard library only. It constructs explicit Frobenius frames independently of the displayed transfer matrix, checks orthogonality, verifies exact rational characteristic identities for 3 and 4 points per loop, compares direct powers to the closed formula on 13 mesh sizes, checks the computed singular values and determinants, and compares the asymptotic coefficient with large-mesh numerical values.

The mathematical validity for every integer \(N\ge3\) and the infinite-grid error limit rests on the algebraic discriminant, orthogonal-projection norm argument, and Taylor expansion supplied in `RESULT.md`, **not** on floating-point outcomes. The values at large \(N\) are not certified intervals. The specified benchmark uses exact state projectors and a zero covariant forcing term; numerical state errors and nonzero forcing are outside its scope. No independent audit or external validation has been performed.
