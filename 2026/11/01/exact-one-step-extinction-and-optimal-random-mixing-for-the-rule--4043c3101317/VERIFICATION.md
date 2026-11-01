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
# Reproducibility and limits

The accompanying `verify_extinction.py` is a standalone Python 3 program requiring only the standard library. Execute `python3 verify_extinction.py` from this directory.

The program checks 295 parameter/size combinations. On rings of size \(3\) through \(9\), direct enumeration iterates over every initial configuration and every sitewise rule-choice vector, rather than using the transfer-matrix expression under test. Separately, a Gaussian elimination procedure counts the nullity of each selected-neighbor XOR matrix over \(\mathbb F_2\). Exact fractions are used for rule-selection probabilities. On rings of size \(10\) through \(49\), the polynomial formula is tested against an independent second-order recurrence. Monotonicity is additionally probed on a rational grid for rings of size \(4\) through \(49\).

The actual bundled program was executed successfully and printed a PASS result. Its computations are finite checks only, not a substitute for the functional-graph and transfer-matrix proof covering all ring sizes and all real mixing parameters. The event is one-step extinction from a uniform initial input, not almost-sure eventual extinction. No external scientific audit has been performed.
