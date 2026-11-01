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

## Reproducible exact checks
Execute in a single directory:

```
python3 verify_exact.py > exact_certificate.json
python3 verify_independent.py > independent_output.json
```

The first program enumerates canonical restricted-growth ternary words satisfying the weak exact integer inequality \(20\operatorname{LCS}(X,Y)\le9(|X|+|Y|)\). It returns a list of all ten length-\(32\) survivors and all thirty rejected extensions at length \(33\), with a distinct strict-violation witness for each extension. Its level sizes are included for every length \(1\) through \(33\). It directly checks the explicit strict length-\(32\) witness and reports smallest integer margin \(1\).

The second program independently calculates LCS via bit-parallel masks instead of the ordinary dynamic program. Its level cardinalities must match the first program exactly, and it independently verifies the strict witness.

The mathematical proof reduces all words to the finite canonical recurrence; without this completeness argument, numerical enumeration alone would not imply a universal theorem. There has been no independent mathematical audit beyond these reproducible implementations. The exact \(9/10\) cutoff does not identify the optimal possible \(\varepsilon\) above it.
