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

# Verification details

The proof is entirely analytic and relies on two explicit, correctly normalized positive-kernel identities from Li–Luo–Xu (2026), namely the hypergeometric expression for the Schur test function and the dual beta-integral bound, both stated with the precise parameter range. The additional strict interior gap follows from monotonicity of \({}_2F_1\); its conversion into the cap stability coefficient uses the estimates \(|r\eta-\xi|\le3/2\), \(1-r^2\ge3/4\) for \(|r|\le1/2\), and \(1-\langle\xi,\eta\rangle^2\ge\delta^2(1-\delta^2/4)\) outside the caps.

The accompanying executable numerical consistency checker evaluates \(F(1/4)<F(1)\), \(\mathscr A\mathscr B=\mathcal C_{n,\alpha}\), and \(\kappa_{n,\alpha}(1/2)>0\) in six representative admissible dimension/parameter pairs. These finite evaluations are checks of transcribed formulas, not certification of universal inequalities. The universal claim is established by the displayed analytic proof. An independent audit has not been performed.
