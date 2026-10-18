---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

PASS. Direct exact rational solution of printed (5.1), keeping -0.48Q as printed rather than replacing by Table 1 0.38, gives positive equilibrium (320/197,1371240/665663,399945/665663,1313079/665663). Table 1 parameters imply eta+d+alpha2=0.38, directly inconsistent with the numerical equation. The linearized delayed infection Jacobian has rank one, so det(lambda I-J0-z Jdelay) is affine in z=e^{-lambda tau1}, contradicting published z². Independent SymPy symbolic differentiation/determinant derivation exactly reproduced the two integer polynomials P(lambda), Q(lambda), modulus quartic F(u), whose derivative is positive for u>0 and F(0)<0; thus exactly one imaginary frequency exists. Independent numerical evaluation gives omega=0.1447950754167241, earliest tau1=13.87960223606146 and positive real derivative 0.0017462878979220143. The original omega=0.0786 gives strictly negative nonzero F(omega²), impossible at any tau1. Zero-delay Hurwitz positivity, nonzero determinant at lambda=0 and continuity of roots confirm first loss of linear stability. These computations do NOT establish nonlinear Hopf branch direction or general two-delay behavior.

## originality

PASS

PASS best of knowledge. The complete original Yang–Zhang paper reports the inconsistent Table 1/system (5.1) coefficients and different equilibrium and crossing numbers, not these corrected values or rank-one cancellation. A related SEIQRS later analysis repeats the general quarantine coefficient but does not give the exact correction. Targeted numerical/DOI, characteristic-alias and Resultary searches surfaced no published corrigendum for the same printed benchmark; absence from search is not independent priority proof.

## value

PASS

PASS. The corrected equilibrium and first linear stability threshold address a materially wrong published numerical verification of a delay-induced Hopf theorem, including an algebraic structural cancellation; this is a substantive model-consistency and stability correction, not a rounding or cosmetic typo.

The dated certificate retains the supplied scientific assessment, sources and limitations.
