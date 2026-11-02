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
# Computational verification and limits

Run `python verify_weddle16.py` with Python 3 (standard library only). It reconstructs \(\mathbb F_{16}\) exactly as \(\mathbb F_2[\theta]/(\theta^4+\theta+1)\), checks fifteen general-position determinants for each six-point configuration, expands the Weddle determinant, checks every one of the 4369 projective points by two independent polynomial/matrix evaluations, and extracts the tangent-square and cubic factorization at the rational \(D_4\) point. It reports the two numbers of rational exceptional arms and computes the corresponding resolution totals.

The proof of the exceptional-fiber point correction uses the local blow-up analysis of a \(D_4\) singularity with square tangent cone and squarefree restricted cubic, and the published classification of characteristic-two Weddle singularities. The verifier counts finite-field points, but is not a substitute for the local resolution argument. No claim about the full zeta function of the nonmaximal example or exhaustive parameter classification is made.
