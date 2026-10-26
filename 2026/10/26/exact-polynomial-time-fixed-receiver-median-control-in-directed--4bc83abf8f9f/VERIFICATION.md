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

# Verification and reproducibility

Run `python3 verify.py` using the Python standard library.

The verified execution output was:

```text
PASS: fixed-receiver budget classifications 764 exact subset replays 2155 independent matrix inversions 2155
PASS: four-node exposure-ranking reversal, exact rational
```

The test constructs the full matrix for every proposed perturbed network, inverts it independently, and checks equality with the response formula before exhaustively comparing all subsets against the crossing-point optimization algorithm. Every arithmetic operation is a rational fraction; a deterministic generator initializes graphs and parameters. These are finite verification tests, not substitutes for the mathematical proof for all finite networks. Historical priority remains subject to independent scrutiny; no such audit is asserted.
