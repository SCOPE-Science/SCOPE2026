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

The claim is verified analytically from the printed autonomous equations. The vaccinated component has the exact limit \(V_\infty=\alpha\Pi/(\eta+\mu)\). Positivity of the standard-incidence contribution gives \(I'+hI\ge(1-p)\eta V\), where \(h=\omega+\mu+\xi>0\). Variation of constants therefore yields the claimed long-time lower bound.

At an equilibrium, \(V^*=V_\infty\) and the infected balance implies \(I^*\ge(1-p)\eta V_\infty/h>0\). Thus the published point with \(I^*=0\) cannot be a steady state in the nondegenerate regime.

`verify.py` uses exact rational arithmetic for the admissible witness \(\Pi=2\), \(\alpha=1/2\), \(\eta=1\), \(\mu=1\), \(p=1/2\), \(\omega=1\), and \(\xi=0\). It checks \(V_\infty=1/2\), the infectious residual at the proposed disease-free state is \(1/4\), and the general equilibrium floor specializes to \(I^*\ge1/8\). The script is a reproducibility check, not the proof of the quantified statement.

The source model and the methodological assumptions of the standard next-generation construction were independently re-read from the cited full texts. No claim is made about a corrected model, a positive equilibrium's stability, or the controlled equations.
