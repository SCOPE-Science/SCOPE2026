---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For metric f(r)=1−2M/r−Λr²/3 and timelike equatorial circular geodesics, exact effective potential differentiation gives Ω²=M/r³−Λ/3 and κ²=M/r³(1−6M/r)−(Λ/3)(4−15M/r). Put x=M/r, y=Λr²/3, a=Ω²r²=x−y, b=κ²r²=9x²−(15a+3)x+4a. Stable positive b implies 0<a<x<1/6, and 0<ρ=b/a<1. Solving yields a=3x(1−3x)/(4−ρ−15x), y=x(1−ρ−6x)/(4−ρ−15x), for exactly x∈(0,(1−ρ)/6), with Λ=Ω²(1−ρ−6x)/(1−3x). Explicit positive derivatives establish strictly increasing radius/mass, decreasing cosmological constant, and sharp open bounds; fixed-radius inverse is the unique lower quadratic root. Independently checked four exact symbolic identities and 2500 feasible numerical parameter samples. All-datum sufficiency follows analytically, not by these samples.

## originality

PASS

Earlier Stuchlík–Hledík treat circular potential/stability; Kunst–Perlick–Lämmerzahl study isofrequency degeneracy of orbital configurations in a fixed Kottler background; Boshkayev–Luongo–Muccino present forward coordinate frequencies. Their results provide inputs but are not an explicit complete inverse-parameter image with one-dimensional monotone fiber, all simultaneous sharp bounds and each single-physical-parameter recovery. The assessed finite-parameter inversion may be directly derivable from standard forward formulas, so specialized unindexed inverse analyses remain a material risk.

## value

PASS

A complete identifiability and sharp feasibility boundary for a natural relativistic inverse problem clarifies exactly what is recoverable from two coordinate-time frequencies, and which single additional measurement restores uniqueness. The coordinate-time/observer normalization limit is essential: this is not observational inference without clock calibration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
