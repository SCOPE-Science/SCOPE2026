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
# Reproducibility

Run `python verify.py` with Python \(3\) and the standard library. The script directly builds \(J(n,2)\) adjacency, recursively explores all legal additions (without using the incidence-potential proof), and checks that maximum lengths for \(3\le n\le8\) are \(2,2,4,4,6,6\). It also computes finite ordered maximum-sequence counts as data rather than as an asserted infinite enumeration formula.

Independently, the script checks the critical undominated-edge identity on every nonempty selected-edge subset of the complete graph for each \(3\le n\le7\): a total of \(2,131,011\) subsets. It then constructs the claimed extremal legal sequences for every \(3\le n\le50\) and verifies every step from the original open-neighborhood definition, including terminal total domination.

`verification_output.json` records the actual script output. The infinite upper bound and equality classification are established by the proof in `RESULT.md`; neither a finite census nor a computational timeout is treated as an infinite certificate. No external validation has been performed.
