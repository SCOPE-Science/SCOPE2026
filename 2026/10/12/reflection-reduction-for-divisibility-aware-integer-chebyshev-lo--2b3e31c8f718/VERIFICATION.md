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
The theorem is proved symbolically in `RESULT.md`. The accompanying `verify.py` is a corroborative regression check, not a finite substitute for the proof.

The script checks four independent algebraic/numerical consequences:

1. normalized polynomial reflection \(Q^\rho(x)=(-1)^{\deg Q}Q(1-x)\) is an involution and preserves degree and positive leading coefficient on a sample of integer polynomials;
2. \((x-t)(1-x-t)=x(1-x)-t(1-t)\) holds exactly over a rational grid;
3. on a reflection-closed three-polynomial test library and a nonsingular symmetric atomic measure, the computed continuum term satisfies \(A^\rho(x)=A(1-x)\) and the computed divisibility penalties pair as \(G_{i^\rho}^\rho=G_i\);
4. for the same symmetric measure, direct potentials agree with the pushed-forward \(w=x(1-x)\) potential to floating-point tolerance.

A successful replay prints a single `VERIFY_OK` line with the number of cases. The universal no-loss statement depends on exact covariance plus concavity, as given in the proof, not on the sampled cases.
