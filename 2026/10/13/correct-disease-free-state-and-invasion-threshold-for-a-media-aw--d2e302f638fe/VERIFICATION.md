---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The publisher PDF confirms the balances in model (2.1), the p̃S̃ influx in (2.2), and the non-equilibrium point and negative first row attributed to Section 3.1. At disease absence, summing the S,Q balances gives S+Q=Λ/μ and Q=pS/(λ+μ); substituting the printed zero-Q point into (2.2) gives Q̃′=p̃. The incidence derivative at the true equilibrium is βs* times the I+θA derivative; derivatives of the media and susceptible factors multiply a zero infectious term. In infected coordinates E,I,A the single new-infection row yields the stated spectral radius by triangular inversion. For the threshold signs, write a,b,c for the three positive removal rates and P,Q for βs*σρ, βs*θσ(1−ρ). On Re z≥0 the characteristic equation is z+a=P/(z+b)+Q/(z+c). If R₀<1, the right-hand modulus is at most aR₀<a; if R₀>1, the real equation has a positive root by continuity and monotonicity. Equality gives a zero eigenvalue. The uninfected linear block is stable. Independently recomputed from the now-confirmed Table 2 literals: s*=10251/10351, R₀=0.2281211174466805 and 1.6475414037815814, and βc=0.394527262567158. The frozen verify.py was inspected, not executed. This is a local threshold check, not a validation of downstream nonlinear claims or code.

## originality

PASS

The original paper prints a different point and numbers. The general next-generation construction and the prior same-paper adjoint correction do not provide this corrected equilibrium and threshold of the printed uncontrolled model. No equivalent correction was established in the checked material.

## value

PASS

The correction replaces a non-equilibrium and an invalid new-infection split with a quantitative local threshold for the actual equations. Both published sample parameters remain on their respective sides of one, but the quantitative values and interpretation around the corrected boundary change. This is a source-specific structural correction, not a new general next-generation theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
