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

# Verification of the mathematical claim

The stationary densities are checked by direct substitution into the forward transport equations. The periodic corrector \(F_s(x)=x+h(x)+sg\) has zero generator because \(h'(x)=(\gamma(x)-G)/(\alpha+G)\). Its bounded jumps yield exact bracket rate \(2v^2/[(\alpha+G)(1+R)]\) after stationary averaging. The usual bounded-jump martingale invariance principle gives the displacement CLT; martingale isometry and bounded error give the asymptotic second moment. An elementary two-pair exchange proves the rearrangement ordering before bounded approximation.

The standalone `check_transport.py` was executed successfully with 217 exact-rational and finite numerical assertions. A discretized periodic velocity-jump Markov chain, independent of the displayed continuum corrector, yielded progressively smaller absolute errors on three test environments as cell mesh was refined from 12 to 24 to 48 points per zone. The paired two-zone calculation independently reproduced the exact \(4/3\) diffusion ratio. Finite tests are corroborative and not a proof of the unbounded-time theorem. The source literature comparison is a qualified self-review originality assessment, not independent publication-priority certification.
