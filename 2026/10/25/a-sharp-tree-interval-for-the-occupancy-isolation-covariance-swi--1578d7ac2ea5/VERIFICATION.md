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

## Reproduction

Install dependencies with `python -m pip install -r requirements.txt` and run `python verify.py` from the directory containing the source and certificate. The script emits sorted-key JSON with a final newline, and its exact output matches `certificate.json`. It checks 47 nonisomorphic tree classes of orders two through eight at three rational survival probabilities, evaluating every retention subset in rational arithmetic. It also verifies signs at the analytical endpoint probabilities and the four strict rational signs for the 17-vertex connected cyclic witness.

## Limits

Finite enumerations do not prove statements at larger tree orders. The complete proof for all tree sizes appears in `RESULT.md`. The connected non-tree witness only demonstrates the possible failure of the one-switch law, and does not assert a smallest order. Independent audit has not been performed.
