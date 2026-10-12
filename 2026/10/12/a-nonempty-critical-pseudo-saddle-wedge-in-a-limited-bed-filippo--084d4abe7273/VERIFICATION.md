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
The classification is proved analytically from the printed vector fields and sliding equation.

At \(\mathcal R_0=1\), the checker verifies
\[
I_{c0}=0
\]
and
\[
S_{c2}=\frac{r_0}{\Delta}I_c+\frac{br_1}{\Delta}.
\]
It then verifies symbolically that
\[
S_s\ge S_{c2}
\]
is equivalent to
\[
\Lambda\Delta-\mu b r_1\ge I_c\bigl((\mu+\nu)\Delta+\mu r_0\bigr).
\]

For the exact witness, the replay confirms
\[
I_c^{\dagger}=\frac{1597}{150},\qquad
S_{c2}=\frac{53}{20},\qquad
S_s=45,
\]
with \(I_c=5<I_c^{\dagger}\), opposite normal-field signs, zero sliding velocity, and \(S_s+I_c<\Lambda/\mu\).

The witness is only a concrete certificate. The full parameter classification follows from the preceding symbolic identities and inequalities.
