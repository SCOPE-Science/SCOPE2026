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

The standalone script `verify.py` was run from the included package with Python 3 and printed `VERIFY_OK monoid_pairs= 36 word_membership_cases= 4599` and `samples: [(1, 1, 5), (2, 2, 19), (3, 3, 69), (4, 4, 251), (6, 6, 3431)]`.

Checks: breadth-first closure of the two transformation generators; independent enumeration from each weakly monotone signature; equality of the two transformation sets for \(1\leq r,s\leq6\); a further brute-force word enumeration for \(1\leq r,s\leq4\); and direct subsequence membership versus the greedily matched-prefix DFA for 4,599 word/pattern cases. These checks concern finite parameters. The all-parameter proof is in `RESULT.md`. No independent audit has been performed.
