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
# Verification and limits

The exact conditional distribution was proved analytically using Prüfer sequences; no approximation is required. The order relations were proved using a shared occupancy-prefix coupling. Every omitted comparison was excluded using positive-probability extreme support events. The degree-three mean transition was proved by logarithmic derivative monotonicity and exact endpoint rational evaluations; higher degrees were handled by an explicit lower bound plus exact finite cases.

Run the included `verification.py` with Python's standard library. Actual execution returned `PASS 129 exact checks`. The code enumerates every Prüfer word for sizes 5–7, independently counts its conditional leaves, matches those counts to occupancy probabilities, tests the strict stochastic orders and incomparabilities, and checks all conditional mean inequalities through size 40. Finite tests are not a replacement for the analytic universal proof.

The historical literature search was limited to the cited, accessible scientific material. Full text for the 1999 joint degree-count article was not accessible; no independent audit of novelty or correctness was performed.
