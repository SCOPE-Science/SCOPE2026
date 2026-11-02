---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Spectral rational f(x)=(x²-6x+12)/(x²+6x+12) gives SPD endpoint and row sum 1. Independent symbolic inversion verifies each C5/C6 distance-class numerator and denominator. For C6 the sole potentially negative class is adjacency with -2h q(h)/D(h); Descartes gives unique positive quartic root in (6,7). For n>=6, f(hL)=I-12 L⁺/h+O(h^-2), and cycle resistance double-centering gives (L⁺)_{01}=(n-1)(n-5)/(12n)>0, proving eventual negative adjacent entries for all n>=6. C3/C4 complete multipartite spectral cases give unconditional positivity. Green identity sampled n=6..12 only as corroboration, not infinite proof.

## originality

PASS

Best-of-knowledge originality limited to the narrow final claim: Existing 8-state small-step obstruction does not imply a six-vertex symmetric large-step failure; C6 sharp four orbit rational functions are specific.

## value

PASS

Unconditional positivity is a central property of numerical heat diffusion; exact minimal failing symmetric cycle and sharp C6 timestep threshold constitute a motivated boundary, with effective-resistance mechanism explaining the onset on every larger cycle.

The dated certificate retains the supplied scientific assessment, sources and limitations.
