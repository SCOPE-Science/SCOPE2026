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

The proof is symbolic and applies to every prime power \(q\). The finite checker is supplementary.

`verify.py` enumerates all \(2\times2\) matrices and all idempotents for \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_5\), and \(\mathbb F_7\). It also contains an independent polynomial-basis implementation of \(\mathbb F_4\) with \(\alpha^2+\alpha+1=0\). For each matrix it directly counts idempotents \(E\) for which \(A-E\) is nilpotent and compares that count with
\[
\mathbf 1_{A\text{ nilpotent}}+\mathbf 1_{A-I\text{ nilpotent}}+\mathbf 1_{\operatorname{tr}A=1}\bigl(q+1-e(A)+q\,\mathbf 1_{\det A=0}\bigr).
\]
It then checks the total nil-clean locus and the predicted trace-one class profile.

Finite enumeration does not prove the theorem for all prime powers; the all-\(q\) proof is the rank-one projection count in `RESULT.md`. No independent audit or external validation has been performed.
