---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducible numerical checks and limits

Run `python3 verify.py` using Python 3 and its standard library only. The script evaluates the one-dimensional elementary integral by composite Simpson quadrature, separately on either side of its absolute-value kink; no external library is required.

For each of five positive shape triples, it directly samples uniformly oriented normals and uses offsets uniformly drawn from a common sphere-bounding interval, rejecting all planes that miss the pyramid. The retained-plane distribution is proportional to the Euclidean-motion-invariant measure and contains the required directional width bias. Section vertices are counted independently as crossing edges of the five-vertex pyramid graph, rather than obtained from the formulas under test.

The completed deterministic test proposed 450,000 random orientations and retained 241,034 hit sections. It verified each of the three predicted probabilities to absolute tolerance 0.015, each mean count to tolerance 0.025, the derivative identity for the exact mean-width normalizer to numerical tolerance, all probability signs, triangle dominance, and both sharp expectation limits. Output ended with `RECTANGULAR_PYRAMID_CROFTON_LAW_OK accepted=241034`.

These tests provide reproducibility diagnostics, not a finite exhaustive classification or independent mathematical proof. The universal claims require the exact edge/offset integrations and monotonicity argument in `RESULT.md`. No independent audit has been performed.
