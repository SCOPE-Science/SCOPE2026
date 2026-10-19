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

# Reproducibility of the repeated-symbol deletion theorem

The mathematical proof is in `RESULT.md` and applies to every length and deletion order; the following finite checks are corroborating tests, not an infinite certificate.

From a directory containing the two stand-alone checkers, run:

```sh
python3 verify.py
python3 majorization_check.py
```

The executed outputs from the packaged Python 3 scripts were:

```text
VERIFY_OK words=18030 alphabet_cases=2,3 max_n=12,8 triple_n<=250
MAJORIZATION_OK compositions= 262143 total_a<=18
```

`verify.py` builds actual distinct output sets for every binary source word through length 12 and every ternary source word through length 8, checks the exact run-product enumeration, and compares all allowable fixed-deletion maxima against the closed coefficient formula. It also evaluates the explicitly proved three-deletion piecewise expression for each integer length from 3 through 250.

`majorization_check.py` independently enumerates every positive composition of each integer through 18, expands its entire bounded-sum polynomial, and verifies coefficientwise domination by the corresponding balanced composition.

Only standard-library Python is needed. These checks do not establish originality or supply an independent scientific audit; correctness of the unbounded theorem rests on the bijection, the separator budget, the balancing polynomial identity, and the exhaustive algebraic case division in the written proof.
