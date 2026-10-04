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

The universal proof is analytic. Its critical checks are:

1. With \(g_k=c+(1-c)q^k\), direct expansion gives \(g_{a+b}-g_ag_b=c(1-c)(1-q^a)(1-q^b)\ge0\). Therefore replacing product blocks by one correlated block can only increase target overlap.
2. Under \([\rho,\omega]=0\), the target ray is an eigenvector of every free state. This is the needed nonstandard boundary condition for reducing Umegaki and max-relative entropy to the target eigenvalue.
3. The testing converse uses the actual free state \(\zeta_n=g_n\rho^{\otimes n}+(1-g_n)\nu_n\), while the matching test is \((1-\varepsilon)\rho^{\otimes n}\).
4. The smoothing converse uses the trace-zero effect bound \(\operatorname{Tr}(\rho^{\otimes n}L)\ge1-\delta/2\). The matching state \(L_s=(1-s)\rho^{\otimes n}+s\zeta_n\) lies at exact trace distance \(2s(1-g_n)\) and has domination factor \(\max\{1,(1-\delta/2)/g_n\}\) below the free threshold, or factor \(1\) once the threshold is crossed.

The accompanying checker enumerates block-size compositions and assignments only as a finite corroboration. It does not certify the all-\(n\) theorem; the displayed algebra does. No statement is made for \([\rho,\omega]\ne0\).
