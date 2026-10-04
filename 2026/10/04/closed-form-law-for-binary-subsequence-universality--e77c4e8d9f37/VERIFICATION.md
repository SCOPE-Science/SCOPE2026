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

Run `python3 verify.py` with the standard Python library.

The verifier performs four checks:

1. For every binary word through length \(10\), it compares greedy arch counting with an independent definition-based test that explicitly enumerates all candidate subsequences of the next length.
2. For every binary word through length \(18\), it constructs the complete universality-index histogram and compares it with the coefficient formula.
3. On the same exhaustive range it checks the cumulative \(k\)-universal counts and exact rational mean and variance.
4. Independently of word enumeration, it checks through length \(80\) the coefficient recurrence forced by \((1-z-2uz^2)F=1+z\).

A successful run prints:

`VERIFY_OK definition_n<=10 exhaustive_n<=18 recurrence_n<=80`

The exhaustive checks are finite corroboration. The universal quantifiers over all lengths are justified by the arch-factorization generating-function proof in `RESULT.md`, not by the finite search.
