---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

All pure states of an ensemble of the rank-two density lie in its GHZ/W range. The HJW co-isometry has weights p_j=lambda|v_1j|²+(1-lambda)|v_2j|² and r_j=|v_1j|²/p_j with sum p_jr_j=1. The given pure objective is g(r)=(5lambda²r²-4lambda r+8)/9 with g''=10lambda²/9>0; strict Jensen equality forces all r_j=1, then |v_1j|²=|v_2j|²=p_j. Orthogonal co-isometry rows are precisely the phase zero-barycenter condition. Conversely it yields a valid row isometry and equality. Minimum rank-two ensemble size >=2, and a two-vector zero barycenter forces 1/2 weights and antipodal phases. Direct independent complex-amplitude density-matrix calculations evaluated 4det rho_A at six lambda values and four phases each; phase-independence and polynomial matched. The strict Jensen argument proves all lambda, not finite samples.

## originality

PASS

The August 2026 anchor obtains the convex-roof value and gives an attaining four-column co-isometry; the submitted result identifies the complete strict-Jensen equality family and minimal support. The previous HJW classification supplies all ensembles of a density operator but does not isolate this measure’s optimizers. Other GHZ/W entanglement papers address distinct measures or bounds. There is a meaningful access risk because the full anchor article could not be obtained this run, but no inspected stronger statement decisively covers the all-optimizer equality classification.

## value

PASS

A full description of every finite convex-roof attaining ensemble is a natural variational equality classification with operationally relevant ensemble cardinality. The exact two-state minimum and continuum of zero-barycenter higher support ensembles distinguish optimizer geometry from one example and can be used when analyzing ensemble choice for this entanglement measure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
