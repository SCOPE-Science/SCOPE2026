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
# Verification and scope

## Analytical checks
The scalar threshold derivative \(1/[s(1-s)]-\beta\) establishes precisely when the scalar fixed-point count changes. The order interval in the proof compares full-network trajectories to scalar ones and does not assume symmetric or irreducible coupling. The critical scalar vector field is exactly \(-u+\tfrac12\tanh(2u)\); expansion to fifth order gives the first logarithmic term. Perron–Frobenius simplicity supplies precisely one center direction for irreducible coupling, so standard stable-foliation tracking transfers the scalar asymptotic to each coordinate. This is a paper proof, not an automated certification.

## Reproducible finite calculations
Execute `python verify.py` from the directory containing this file. It checks the exact rational cubic/quintic coefficients, the fold identities at three gains, and integrates two irreducible three-node examples from two initial configurations. The reported program output was: `PASS: exact fold identities and critical coefficients; finite irreducible-network illustrations`.

## Limits
Finite numerical integrations support but do not establish universal convergence. The proof does not cover signed or non-row-stochastic coupling, heterogeneous response functions, delays, or arbitrary dynamics inside the bistable interval. There has been no independent external review.
