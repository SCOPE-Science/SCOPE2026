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

# Verification and reproducibility

The proof in `RESULT.md` covers every symmetric \(2\)-\((v,k,\lambda)\) design with odd block size and even pair intersection over every finite characteristic-two field. Finite computation checks illustrative designs, not the universal quantifier.

Run the following independent checkers from the directory containing these files:

```
python3 check_matrix.py
g++ -O2 -std=c++17 -Wall -Wextra -o check_independent check_independent.cpp
./check_independent
```

Each checker builds the \(2\)-\((4,3,2)\) complement-of-singletons design and the cyclic \(2\)-\((11,5,2)\) biplane, toggles each of 16 and 121 point–block entries, and checks matrix fixed-space dimensions, ranks, and iterate identities over \(\mathbb F_2\). Each also independently enumerates every binary initial state for a representative insertion and deletion in the four-point design. The checked exact-period populations are \((4,12,12,228)\) at periods \((1,2,3,6)\) for insertion, and \((4,12,48)\) at periods \((1,2,4)\) for deletion. For deletion, 64 states are initially periodic and 192 first enter after one update. The command output is captured in `verification_output.txt`.

No probabilistic numerical estimate is needed. Computational verification cannot exclude historical redundancy, mistakes in an untested symbolic lemma, or failures outside the theorem's precise hypotheses.
