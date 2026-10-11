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

The verification package contains `verify.py`. It checks the following algebraic components of the stated claim:

1. the positive-equilibrium equation \(P_*(1+fP_*)=(1-m)(m-\theta)\);
2. the exact rearrangement \(e^{J_P}=1+h(\bar N-m)\Longleftrightarrow \bar N-m=(e^{J_P}-1)/h\);
3. the prey-factor rearrangement leading to the exact predator-mean identity;
4. the completed-square identity \((1-N)(N-\theta)=(1-\theta)^2/4-(N-(1+\theta)/2)^2\);
5. the numerical ceilings \(0.2025\) for \(\theta=0.1\) and \(0.038025\) for \(\theta=0.61\).

The checker does not attempt to certify existence of an invariant measure or convergence of a numerical trajectory. The strict Jensen step and its equality case are proved analytically in `RESULT.md`; finite computation is not used as a substitute for those arguments.
