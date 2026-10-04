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
The included `verify.py` independently constructs the transition table and performs exact forward power-automaton breadth-first search for every coprime pair \(2\le p<q\le13\). It verifies the minimum reset length, the reset target, and the total number of shortest reset words.

The same program separately checks the symbolic rotating-preimage schedule for every coprime pair with \(q\le100\). It confirms the forced copy times \(1+(m-1)p\), the \(q-1\) forced \(a\)-positions, the \(p-1\) forced \(b\)-positions, and the \((p-1)(q-3)\) free positions.

Recorded output: `VERIFY_OK exhaustive_power_cases=45 symbolic_q_max=100`.

The exhaustive power-automaton computation is finite verification, not the infinite proof. The general statement is proved by the scheduled-copy argument in `RESULT.md`.
