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

The included `verify.py` is standalone Python 3 with no external dependencies. It constructs all states \((t,s)\) reachable by a positive base-\(b\) numeral, where \(t\) is its remainder modulo \(b^r+1\) and \(s\le2b+7\) is its digit sum. It terminates after exploring a finite graph and therefore checks **all numeral lengths** for each bounded digit sum, not just numerals below a chosen integer bound. It independently constructs the divisibility witnesses and checks no-carry concatenations.

Command: `python3 verify.py`.

Observed result: `VERIFY_OK: exact finite automata for 35 (base, exponent) settings; constructive witnesses for 325 settings/sums, all checked exactly`.

The exhaustive finite-state tests are only for finitely many base/exponent parameters and finitely many digit sums. The general assertion, including the exclusion for **every** positive multiple, is established by the explicit signed-relation proof in `RESULT.md`, not by experiments. No computer-algebra certification or independent audit is claimed.
