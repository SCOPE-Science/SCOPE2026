---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

The complete 15-bit coefficient space is partitioned into 279 orbits under explicit GL3(F2) generators of order 168. The exact four-equation singularity ideal F=Fx=Fy=Fz is tested on all projective affine charts over an algebraic closure via Buchberger; this avoids the invalid rational-point-only smoothness proxy. Seven-point/seven-line incidence yields the exact ten weighted bins and 10920 smooth, 3888 blocking. Independent SymPy Gröbner evaluation of all 279 orbit representatives reproduced 10920 smooth and 78 orbits and the joint bins, rather than trusting a prior VERIFY_OK. Domain F2 degree 4 only.

## originality

PASS

Best-of-knowledge novel complete joint smooth-quartic blocking-incidence distribution. Asgarli–Ghioca–Yip establish unconditional binary-field half probability and smooth-conditioned high-degree asymptotics, neither fixes exact degree-four conditional joint bins. Nart–Ritzenthaler classify 78 isomorphism classes; that gives an alternative enumeration framework, not a displayed incidence-probability census. Their 78-class classification is substantial prior art and may implicitly permit reconstruction; residual priority risk retained.

## value

PASS

The question whether smooth plane quartics over F2 block every rational line is geometrically natural; conditioning on geometric smoothness changes unconditional half-probability to 162/455. The full 10-bin incidence/orbit refinement is a usable exact benchmark for genus-three classification and blocking-set constructions; a complete finite count has intrinsic interest.

The dated certificate retains the supplied scientific assessment, sources and limitations.
