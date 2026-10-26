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

# Reproduction

The finite proof covers every equality partition of the twelve symbol positions in a triple of length-four center words. Its canonical recursion generates all \(4213597\) patterns. The complete histogram's integer cells are checked against literal expected values, including zero cells. After removing pairwise-equal centers there are \(4201207\) valid ordered patterns and none has a three-shadow intersection above four.

Run in a fresh extraction of this package:

```sh
g++ -std=c++17 -O2 -Wall -Wextra -pedantic verification/enumerate.cpp -o enumerator
./enumerator
python3 verification/direct_check.py
```

The direct checker independently creates each actual deletion shadow over \(q=2,3,4,5\), examines every unordered triple, checks against the symbolic falling-factorial formula, and validates the two complementary counting identities for \(2\le q\le14\). The two programs report `VERIFY_OK`, with exact outputs supplied as `verification/check_output.txt`.

# Proof boundaries

Finite-word brute force for four alphabet sizes is not a proof for arbitrary \(q\). The all-alphabet proof rests on exhaustive classification of restricted-growth equality patterns, which is finite because twelve indexed symbol occurrences generate at most twelve distinct symbol classes. The verifier is a reproducible proof-support computation, not an independent external certificate. Code review or a separate implementation would add assurance. No source outside this package is needed to reproduce the computational part.
