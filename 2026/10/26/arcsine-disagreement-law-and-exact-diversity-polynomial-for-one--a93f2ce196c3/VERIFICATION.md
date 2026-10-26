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

The supplied `checker.py` depends only on the Python standard library. Run `python checker.py` in the directory containing that extracted file. It exhaustively constructs stable subsets for all one-attacker frameworks, allowing zero attackers, on \(1\) through \(5\) vertices, and checks the entire disagreement polynomial against a separate cycle-component calculation. It additionally sums over all labelled functional maps and verifies the EGF coefficient formula by exact rational arithmetic.

Recorded self-review run: `CHECKS 8496 ALL_CHECKS_OK`. This is finite corroboration, not a substitute for the general combinatorial proof or complex-analytic asymptotics. The latter are derived in `RESULT.md`. The limiting arcsine law applies to uniform triples \((f,E,H)\); it is not a claim about the distribution produced by uniform maps conditional on admitting stable extensions.
