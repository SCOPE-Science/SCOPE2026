---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Rebuilt first-step equations for transient states 11,10,01 with 00 absorbing, solved their three-by-three linear system and checked all positive denominators including c=0 or B. With D=ab(a+b+B), the means are [a²+ab+b²+(a+b)B+c(B-c)]/D, [(b+c)(a+b+B-c)]/D, [(a+B-c)(a+b+c)]/D. Weighted derivative T'(c)=[B+a w10-b w01-2c]/D, second derivative −2/D<0. Projection of (B+a w10−b w01)/2 to [0,B] uniquely optimizes, including equality at endpoints. Independently evaluated 756 exact-rational generator/inequality assertions; this finite grid does not prove the general theorem.

## originality

PASS

Best-of-knowledge distinct result: continuous-time two-patch *mean hitting time*, arbitrary initial-law-dependent fixed directional split, quadratic curvature; compared with discrete-time patch processes, symmetric spectral resilience, many-patch asymmetric connectivity and general intervention heuristics. Full text of key Etienne–Heesterbeek source inaccessible; substantial historical risk remains but no positive evidence it already states this exact law.

## value

PASS

Expected regional extinction time under constrained directional recolonization is a motivated finite-state conservation objective. The exact initial-distribution control and endpoint-switching rule separate extinction time from quasi-stationary eigenvalue or all-patches-initially-occupied criteria. Although three-state CTMC algebra is elementary, the sharply interpreted allocation response to initial uncertainty is a natural exact invariant that could be needed in intervention design; not a claim about realistic demographics or arbitrary networks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
