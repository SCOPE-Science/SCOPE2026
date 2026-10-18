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

# Finite verification and its scope

Execute `python3 verify.py` with Python 3.9 or newer. The program independently constructs complements of paths and cycles and tests the ordinary color-change rule on **every** initially blue subset for both graph types at each order from \(5\) through \(14\), a total of 65,472 subsets on 20 graph instances. It independently enumerates eligible three-white sets using the original-graph degree-two-neighborhood criterion, and checks that this classification exactly agrees with the actually successful minimum sets. It also compares every polynomial coefficient with the closed formulas.

The output of the test is included in `verification_output.txt`. The checker makes no use of previously saved checks, off-package files, or mathematical software. Finite tests do not establish the claims for arbitrarily large \(n\); the corresponding proof appears in `RESULT.md`. Independent audit has not been performed.
