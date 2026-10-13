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
# Verification

Run `python3 verify.py` beside `verify.cpp` and `certificate.json`.

For each split \(Q=Q^+\cup Q^-\), the compiled verifier constructs all \(625\) possible input-letter transition maps. State symmetry fixes the initial entrance state in \(Q^+\) to state \(0\), and the accepting singleton has only the start-state type or a distinct-\(Q^+\)-state type.

The end-marker enumeration deliberately enlarges the model: later left-endmarker behavior is allowed independently of the normalized initial entrance. Therefore any upper bound obtained is valid for the actual automata. The exact split maxima in this superset are \(0,3,4,3\), so no binary four-state direction-determinate automaton can have shortest accepted length \(5\).

The verifier separately simulates the explicit binary witness on every word shorter than \(\mathtt{abba}\), and the explicit ternary witness on every ternary word shorter than \(\mathtt{abbac}\). It then replays both accepted words.

The only external premise used for ternary optimality is the published theorem that the unrestricted four-state direction-determinate maximum is \(5\). Independent audit has not been performed.
