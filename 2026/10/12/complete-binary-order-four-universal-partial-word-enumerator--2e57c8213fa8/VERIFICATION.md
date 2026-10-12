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

# Exact finite verification

The alphabet in the two provided programs is `0`, `1`, `*`, where `*` is the wildcard. Each wildcard matches both base letters; overlapping matches of the same four-bit factor are forbidden.

Run:

```sh
g++ -O2 -std=c++17 enum.cpp -o enum
./enum
python3 verify.py --check all_words.txt --check-reps orbit_representatives.txt
```

The C++ implementation expands each of \(81\) four-symbol patterns into its exact \(16\)-bit coverage mask and runs an exhaustive nonoverlap extension search. All \(27\) length-three prefixes are entered. The Python implementation independently uses direct character comparisons and sets, checks all \(385\) listed witnesses factor-by-factor, confirms disjoint coverage at every recursion step, and calculates symmetry orbits. Both visit \(15{,}840\) recursion nodes and obtain exactly the coefficient profile printed in RESULT.md. The Python output ends `VERIFY_OK`.

The fundamental completeness step is a mathematical invariant, not a program log: every valid extension must add a nonempty coverage set disjoint from the accumulated set; all and only valid prefixes survive. Thus no possible string lies beyond the finite recursion. The files `all_words.txt` and `orbit_representatives.txt` are fully embedded and checked against regenerated output. No computations for factor lengths other than four are included, and no independent external validation is claimed.
