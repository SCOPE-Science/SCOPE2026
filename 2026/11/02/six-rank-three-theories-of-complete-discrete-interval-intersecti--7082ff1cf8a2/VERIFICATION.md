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

# Reproduction and mathematical checks

Run `sh reproduce.sh` from the directory containing the companion files. The script uses only a C++17 compiler, Python 3 standard library, and `diff`. Each recorded output is checked byte-for-byte against the newly executed program's standard output.

`interval_types.cpp` enumerates every interval and every ordered triple of its interval-graph vertices for \(1\le n\le26\). The six-bit triple atomic code consists of the three equality predicates and the three unordered adjacency predicates. Set-valued recursion computes the complete graph rank-three type; repeated selections are included.

`independent_types.py` implements the nested-set recursive definition of logical types without the C++ bitmask optimization, on \(1\le n\le12\). Its canonical digests and class labels are in `independent_types_output.txt`.

`witness.py` independently checks that \(G_5\) has eight rank-two singleton profiles and \(G_6\) nine; the new one is represented by \([3,4]\). Its output is in `witness_output.txt`.

The finite recursion does **not** prove the conclusion for \(n>26\); the separate mathematical two-endpoint order game, with gap thresholds \(t_r=3^r-1\), proves that all indices at least \(26\) are equivalent at rank three. Combining this with the fully covered interval \(1\le n\le26\) completes the classification.

The programs are finite exhaustive checkers, not proofs of unbounded enumeration, and no external mathematical validation is asserted.
