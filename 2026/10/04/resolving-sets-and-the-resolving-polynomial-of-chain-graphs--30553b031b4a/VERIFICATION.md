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
The proof is symbolic. The accompanying `verify_resolving_chain.py` independently constructs each tested chain graph, computes graph distances, and compares the literal resolving-set definition with the structural criterion and with the four-state recurrence.

Replay command: `python3 verify_resolving_chain.py`

Expected terminal line: `VERIFY_OK graph_types=298 subset_checks=191508 polynomial_checks=2932 max_order=10`

The finite exhaustive replay covers class-size vectors with \(p\le4\), each twin-class size in \(\{1,2,3\}\), and total graph order at most \(10\). It is not a proof of the unrestricted theorem; the proof in `RESULT.md` is. Independent audit has not been performed.
