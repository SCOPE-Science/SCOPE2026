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

# Reproduction and limits

Execute `python3 verify.py` with a standard Python 3 installation. The script uses only standard-library exact fractions, dense elimination, and elementary floating-point functions. It checks rational instances of the Dirichlet inverse, positivity and symmetry of the uniform averaged block update, exact energy decrease for direct block solves, the constant-mode obstruction for explicitly nonuniform sampling, three closed small-block formulas, and near-critical and fixed-coupling asymptotic trends. It outputs a `PASS` line with the number of individual finite checks. A finite check or floating-point limit comparison cannot establish a universal equality or limit: the full proof is in `RESULT.md`.

The result has not undergone an independent audit. Verification is limited to mathematical reconstruction and the executable checks supplied with the finding. The claim applies only to exact real arithmetic, fixed-length cyclic blocks, and the specified periodic nearest-neighbor operator.
