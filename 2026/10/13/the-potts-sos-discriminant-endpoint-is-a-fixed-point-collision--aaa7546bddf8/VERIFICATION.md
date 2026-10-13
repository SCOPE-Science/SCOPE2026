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

The bundled `verify.py` performs exact symbolic checks of the following identities:

- \(\operatorname{num}(f_\theta^2(z)-z)=N_\theta(z)H_\theta(z)\), with \(N_\theta\) the fixed-point numerator.
- \(\operatorname{disc}_z H_\theta=-16(\theta-1)^2(\theta+1)^2P(\theta)\).
- \(\operatorname{Res}_z(N_\theta,H_\theta)=256(\theta-1)^6(\theta+1)^6P(\theta)\).
- The repeated root of \(H_\theta\) at \(P(\theta)=0\) also satisfies \(N_\theta=0\).
- At that root, \(f'_\theta(z)+1\) is divisible by \(P(\theta)\), so the critical multiplier is \(-1\).
- \(P'(\theta)=6\theta(2\theta+1)(\theta+2)>0\) for \(\theta>0\), giving a unique positive critical root.

A rational point below threshold is also checked numerically at high precision to confirm that the two positive roots of \(H_\theta\) are exchanged by \(f_\theta\). A rational point above threshold is checked to have negative discriminant. These numerical checks are corroborative; the classification in the stated sector rests on the exact symbolic identities and elementary sign arguments.

The verification does not inspect or certify solution branches outside \(z_0=t_0=1\), does not establish a global phase diagram, and does not replace the explicitly unperformed independent audit.
