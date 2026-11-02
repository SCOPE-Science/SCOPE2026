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

# Reproduction and limits

Run `python3 verify_circular_four_run.py` from the directory containing that file. The script requires only Python 3's standard library and checks two implementations of the circular-palindrome language: a direct enumeration of starts and lengths, and expansion about possible palindrome centers in the doubled word.

Observed output: `VERIFY_OK direct_definition_instances=3836 symbolic_compositions=1502486 six_run_cases=20`.

The direct finite tests include all positive four-run lengths through \(18\), all two-run lengths through \(29\), deterministic random four-run lengths, and six-run witnesses through \(t=21\). The symbolic census checks parameter formulas, optimality, equality conditions and all optimizing-quadruple counts through length \(79\). All formula cases and proofs are contained in `RESULT.md`. Finitely many tests cannot certify all integer parameters and are not presented as independent validation.

External scientific priority comparison remains incomplete because the full text of the closest 2014 paper could not be obtained. Publication-level independent audit has not been performed.
