---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Nodal sampling determinant is 2sinκ(cosκa−cosκ), so singular samples cannot reproduce nonzero endpoint derivative of g(x)=cosκx−cosκ. Invert unisolvent sample matrix; interior cardinal derivative D_11=κsinκa/(cosκ−cosκa). Positive P_11 and SBP central diagonal force sinκa=0, hence a=0 or ±π/κ exclusively. Endpoint SBP equations uniquely fix q0=sinκ/[κ(1+2cosκ)], P0 middle 2(1+cosκ)q0; off-centre q1=sinκ/[κ(2cosκ−1)], P1 middle 2(1−cosκ)q1. Entrywise cross-identity yields complete SBP. As sinκ<0, central positive only κ<4π/3, off only κ<5π/3. For mass=2, mass residual functions H0,H1 decrease strictly (derivatives 2sinκ(κ∓sinκ)) and have opposite endpoint signs, giving unique κ0≈4.028701 and κ1≈5.066777. Hand-checked positivity, derivatives, 3/2π boundary and alias equality; full parametric proof not inferred from 149 sampled frequencies.

## originality

PASS

Best-knowledge PASS for explicit minimal-node high-frequency phase diagram and exact mass root count, not generic positive FSBP or generalized quadrature existence. The Tchebyshev sufficient hypothesis used by optimal-node theorems fails for the product derivative space because sin(2κx) has five zeros; general results do not imply exact second-band geometry.

## value

PASS

The minimal three-node trigonometric FSBP element has a sharp and counterintuitive reentrant nodal geometry beyond first resonance: two aliased off-center positive diagonal norms exist after midpoint failure; exactly three norm-mass-calibrated choices survive across whole band. This supplies exact feasibility boundaries and physically meaningful mass consistency for numerical discretizations; not arbitrary frequency sampling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
