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

# Finite verification

The source `verify_strategy.py` and `STRATEGY.json` together form a standalone, exact-integer, reproducible certificate. Execute `python verify_strategy.py` in the directory containing both files. The script does not import third-party libraries or retrieve network data.

It reads and checks the three valuation vectors and verifies all \(42\) certified reachable adversary-policy states. All \(126\) recipient responses are checked; \(74\) immediately fail an EF1 inequality, and each remaining response enters a certified next state. Every branch terminates in an EF1 failure no later than arrival seven. It separately solves the full turn-based minimax recursion at horizons six and seven, obtaining \(W_6(0)=\mathrm{false}\) and \(W_7(0)=\mathrm{true}\). Last, an independent exhaustive dynamic program finds a temporally EF1 assignment on each of the \(3279\) fixed arrival sequences of length at most seven.

The proof is a finite theorem for one fixed valuation system. This program is not evidence about arbitrarily many goods, other item values, adaptive randomized rules, or historical novelty. The six-/seven-turn contrast is specific to the displayed three item types.
