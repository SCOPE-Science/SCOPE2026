---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

Normalize a complex quadratic at its maximizing point so a+b+c=1. Parseval of its square gives exactly |a|^4+4|ab|^2+|b^2+2ac|^2+4|bc|^2+|c|^4. Strict convexity in complex coefficients gives unique minimizer; reflection plus conjugation force a=c=rho real, b=1-2rho. Direct expansion Q=70x^4-80x^3+36x^2-8x+1 and Q=840(x-2/7)^2+24/7>0 yield unique cubic stationary root rho. Independent high-precision root evaluation and symbolic derivative checks reproduce C=1/Q(rho)=4.38567264283198 and strict contraction (5Q(rho))^-1/4. Equality rotations and normalized Bergman moment ∫|u|^8=1/5 follow. Full proof, not eight finite rational checks, proves all complex polynomials.

## originality

PASS

Instanes analyzes the identical point-evaluation constant and uniqueness and reports degree-two bounds but does not in the relevant full accessible article compute the exact algebraic d=2,p=4 optimum. Brevig et al. gives universal C<=5 via Rudin diagonal restriction, not the smaller restricted constant or optimizers.

## value

PASS

Exact natural finite-degree nonlinear Nikolskii/point-evaluation invariant, complete equality family and quantitative strict gap for a canonical homogeneous Hardy-to-Bergman restriction; narrow but not a merely arbitrary coefficient slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
