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

# Verification of the finite classification

Two standalone executables are embedded with the six scientific documents.

1. `pg3_resolving.cpp` (C++17): compile with `g++ -std=c++17 -O3 pg3_resolving.cpp -o pg3_resolving`, then run `./pg3_resolving`. It exhaustively checks \(\binom{26}{7}=657800\) unsuccessful seven-landmark sets and \(\binom{26}{8}=1562275\) eight-landmark sets; 9,828 latter are resolving and all have four selected points. Five graph automorphism generators produce a 11,232-element group, whose exhaustive action partitions these bases into four orbits \(936,1404,1872,5616\). Its successful final marker is `VERIFY_OK`.
2. `pg3_independent.py` (Python 3 standard library): run `python3 pg3_independent.py`. It computes distinguishing incidence signatures on 13 point and 13 line labels, tests every \(\binom{13}{4}^2=511225\) balanced candidate, and reproduces the total 9,828 with geometric class sizes \(936,1404,1872,5616\). It separately checks the one-sided semi-resolving minimum six. Its successful marker begins with `VERIFY_OK independently`.

The two algorithms do not share an implementation of the resolving predicate. Both use the same finite-field definition from the finding, as required to study the same graph. The orbit calculation uses explicit projective linear maps and the displayed polarity. A zero result for size seven is sufficient to exclude smaller sizes by monotonicity of the resolving property. The proof is exact only for this finite graph; external independent validation has not been performed.
