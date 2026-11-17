---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

Renewal analysis for the ENTIRE N-particle system gives M_N(r)=h_N(r)/(1-rh_N(r)) and derivative μ_N²−E[T_N²]/2. The fully labeled or count-lumped killed process has states positive occupations c_1..c_4 with Σc_i=N, diagonals −N and exact neighbor jump rates c_i/deg(i); u=A^-1 1, v=A^-1u yield first two moments. Independent exact rational Python/SymPy linear solves reproduced all four source pairs: N1 (12,-10), N2 (1555/272,-169263/73984), N3 (629176456/168587283,-4963736468372212/9473890663107363), N4 (98335794451053/35264790234112,+52393068681552240430947689/1243605430255921087768428544). Strict signs imply local r>0 reversal; continuity under rate changes follows nonsingular finite-state generator.

## originality

PASS

Biroli–Majumdar–Schehr establishes synchronized resetting renewal but on continuum Brownian half-line and different N threshold, not this finite path killed generator or exact 3↔4 reversal. Another related Resultary record studies INDEPENDENT reset clocks, different process, with onset at N=5. No broader earlier finite-graph exact 3-versus-4 moment result located after targeted searches.

## value

PASS

A small transparent 5-vertex graph shows the usefulness of synchronized resetting reverses between 3 and 4 searchers, contrasting Brownian and independent reset thresholds. Exact rational certificate and stability under small conductance perturbations make the narrow finite witness mathematically motivated and independently useful as a reproducible benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
