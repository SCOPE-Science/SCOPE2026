---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

PASS. Reconstructed the generalized eigenvalue equation (L u)_m=lambda m_m u_m, where L=2I-shift-shift*, m=1 outside the three defects and 1-delta on them. For lambda>4, write lambda=2+q+1/q, 0<q<1. Free resolvent kernel is (-q)^{|i-j|}/(q^-1-q); the symmetric Birman–Schwinger/Green matrix on the three defects is diagonal-conjugate to ((1+q)/(1-q)) times the positive 3x3 Toeplitz matrix with t=q^d and entries [1,t,t^2;t,1,t;t^2,t,1]. Its channels are exactly mu_+=(2+t^2+t sqrt(8+t^2))/2, mu_odd=1-t^2 and mu_-=(2+t^2-t sqrt(8+t^2))/2. Monotonicity of lambda(lambda-L)^-1 and limits at lambda down to 4 give inverse-deficit thresholds 0,4d,4d/3, hence three strict mode regions with equality non-normalizable at the band edge. Independent symbolic second-order expansions of delta=1/[((1+q)/(1-q))mu_j] around q=1 produce derivatives 1/4 and 1/12 for the two emerging channels, and lambda-4=(1-q)^2/q; therefore coefficients 16,144. Computed for d=1,2,5 without relying on package verify.py. Finite-chain Sturm calculations from package are supplementary; finite intervals or eigenvalue approximations are not infinite completeness proofs. Scope excludes stiffness changes, damping, nonlinear contacts and arbitrary defect arrangements.

## originality

PASS

PASS, qualified best-of-knowledge with significant historical risk. Montroll and Potts (1955) invented the defect Green-function method and analyzed localized modes and two-defect interactions; their article is broad, directly relevant and inaccessible in full after authorized OA/institutional routes. Boechler et al. (2011) analyze one or two defects in Hertzian granular crystals, including changes to contact properties. The inspected materials do not state an all-d three-identical-mass-defect two-threshold mode count with both separation-independent quadratic edge coefficients. The 1955 method could imply the finite determinant, but no direct prior statement or derivation of these particular sharp thresholds was established. Risk is explicitly retained rather than falsely declaring historical absence.

## value

PASS

PASS. A symmetric three-defect cluster is the first arrangement capable of two additional independent above-band localized channels. The exact thresholds 1/(4d) and 3/(4d), strict edge-eigenvalue loss, and striking d-independent 16 and 144 quadratic detachment laws are natural structural spectral information useful even in this ideal linear model. It is a complete classification of a motivated infinite discrete operator, not only a finite numerical example or a textbook restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
