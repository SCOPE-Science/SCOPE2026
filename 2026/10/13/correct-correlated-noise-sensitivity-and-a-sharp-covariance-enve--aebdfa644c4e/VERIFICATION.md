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

For the stable baseline SIRS model, independently recomputed S*=3.50361582597,I*=1.01641189180,R*=0.225869309288 and Hurwitz F. Solving F^TP+PF+I=0 gives trW(R)=17.274750562409+5.395303120131*r12+0.537604148434*r13+0.152951296895*r23 (rounded values). Gram vectors give max all +1 and min (-1,-1,+1) because a>bc/(b-c), proving the sharp interval [11.494794590740,23.360609127869]. Finiteness and uniqueness follow from Hurwitz stability; trace bounds refer only to the linearized weak-noise model.

## originality

PASS

The originally submitted Brownian covariance correction fails originality: it is published in a same-model 2026-10-04 Resultary paper. The REPAIRED final finding excludes it and claims only the precise sharp three-correlation baseline envelope; after full earlier-paper comparison this narrower numerical theorem is a distinct motivated calculation.

## value

PASS

Sharp attainable total-variance range for the original epidemiological model at its actual data baseline is a motivated, model-specific uncertainty invariant: keeping all marginal noise intensities fixed, correlations change trace by a factor of 2.032. The separate published covariance typo alone is not the value/novelty credited here.

The dated certificate retains the supplied scientific assessment, sources and limitations.
