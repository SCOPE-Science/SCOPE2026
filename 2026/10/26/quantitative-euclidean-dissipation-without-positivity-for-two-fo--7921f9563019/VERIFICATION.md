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
# Verification

The executable \(\texttt{verify.py}\) uses Python 3 standard-library exact rational arithmetic. Run \(\texttt{python3 verify.py}\) next to the other included files. It performs \(1096\) checks on rank-two boundary reconstruction and quadratic-form identities for both stencils, dimensions \(5\le n\le35\), and local sum-of-squares identities. The observed output was:

```text
PASS 1096 exact local/matrix/energy checks; n=5..35.
Scope: finite replay confirms formulas; arbitrary-n coercivity follows from the analytic completion-of-squares argument.
```

The analytic calculation in RESULT.md, not finite replay, proves the arbitrary-size inequality. In particular the least eigenvalues of the two explicit boundary forms give the constants \(10-\sqrt{14}\) and \(9-\sqrt{62}\). The exact rational subcertificate \(\operatorname{Re}(u^*Mu)\ge u^*Du+\|Du\|_2^2\) supplies an independent algebraic cross-check. No external audit or formal proof certification has been performed. The numerical check does not establish historical originality, sharpness of either constant, or claims for other stencils.
