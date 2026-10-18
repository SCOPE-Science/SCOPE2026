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

# Finite exact verification

Run `python verify.py` and `python independent.py` using Python 3.9 or later with no third-party dependencies. Their expected text output is in `verification_output.txt`.

The canonical search checks every permitted append operation from the unique restricted-growth starting word, clearing denominators in each strict LCS test. The complete survivor vector through length \(28\) is asserted in code. The exact gap \(3/23\), its two minimizing triples, and all six relabelings are asserted using rational arithmetic.

The second search generates all square-free words with initial symbol \(0\) and checks every adjacent interval pair by a separate two-dimensional LCS routine. Its candidate counts are \(5162\) at length \(27\) and \(6740\) at length \(28\), with exactly two and zero valid words, respectively, at fixed initial symbol. It does not use the first search's dynamic-programming implementation or pruning rule.

Every finite search in this package has a clearly bounded universe, and the mathematical proof explains why the considered universe is exhaustive. These computational checks do not supply an independent human audit and do not solve an infinite-word optimal-gap problem. A successful execution of the code is evidence for the finite theorem, not independent validation.
