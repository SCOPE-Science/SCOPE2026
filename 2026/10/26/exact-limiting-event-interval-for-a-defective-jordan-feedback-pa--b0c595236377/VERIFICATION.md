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

Analytic checks: \(J\) is invertible, has characteristic polynomial \((\lambda+a)^2\), and has eigenspace \(\operatorname{span}\{(1,0)^\top\}\). The trigger ratio is strictly increasing on \([0,\delta]\) because \(\|x\|_2^2+s x^\top Jx\ge(1-sL)\|x\|_2^2>0\). The uniform root bounds guarantee existence and a positive lower bound for every nonzero sample. The projective recurrence handles the vertical direction, the negative-ratio crossing, and the positive-ratio limit; the exact limiting root is obtained by solving \(as=\sigma(1-as)\).

The analytic proof, rather than a finite trajectory, establishes the limit. The smallness conditions are sufficient and are not asserted to be necessary. No independent audit or external validation is represented here.
