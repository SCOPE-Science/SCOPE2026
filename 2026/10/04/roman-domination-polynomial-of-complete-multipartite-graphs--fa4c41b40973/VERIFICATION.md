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
The proof is symbolic. The accompanying `verify.py` provides a finite independent replay against the definition. It generates every complete multipartite isomorphism type on at most \(10\) vertices, enumerates every labeling in \(\{0,1,2\}^N\), and checks: (1) the structural classification, (2) every coefficient of the displayed polynomial, and (3) the minimum-weight coefficient formulas.

Replay command: `python3 verify.py`

Expected terminal line: `VERIFY_OK graph_types=128 labelings=3169350 coefficient_checks=2230 max_order=10`

Finite exhaustive replay does not certify the unrestricted theorem; the proof in `RESULT.md` does. Independent audit has not been performed.
