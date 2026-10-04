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

The proof was checked by differentiating the stated antiderivatives back to the three published pieces of \(G\), substituting the endpoints \(0,1,3/2,2\), and using \(\operatorname{Li}_2(-1)=-\pi^2/12\). The numerical checker then evaluated \(\operatorname{Li}_2(-1/2)\) and \(\operatorname{Li}_2(-3/4)\) from their convergent series and compared the closed form with direct split quadrature of the published profile.

Recorded replay: `VERIFY_OK closed=0.05887977990512816 direct=0.058879779905129243 abs_diff=1.08e-15`.

The numerical replay is not the proof and does not establish originality. The theorem's density asymptotics and the open Erdős problem are outside this verification.
