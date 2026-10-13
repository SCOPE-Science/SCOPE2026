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
# Reproducibility and verification

Run `python3 verify.py` from the directory containing this file and `verify.py` (Python 3 standard library only). The exact program and actual standard output are both included; no external package, data file, network connection, or theorem prover is needed. Reproduced checks:

1. Enumerate every maximal independent set of each labeled cycle \(C_n\) for \(3\le n\le18\): 637 sets in total. Use two mathematically distinct methods to compute every rational probability: first-arrival recursion on vertex masks, and the theorem's kernel moment/trace recurrences. Check exact equality and per-graph total probability equal to one.
2. Count all vertex permutations of \(C_n\) for \(3\le n\le8\) (46,230 permutations altogether). Compare exact observed probabilities to the theorem for all outputs.
3. Independently assert values \(\phi_0=1/3\), \(\phi_1=1/5\), \(\phi_2=1/7\), \(\phi_3=8/81\), \(\phi_4=34/495\), \(T_3=1/3\), \(T_4=7/30\), \(T_5=17/105\), and \(\phi_0\phi_2-\phi_1^2=4/525\).
4. Check the uniformity classification on all 16 tested graph orders, but **do not** confuse these finite tests with the infinite proof in `RESULT.md`.

No exhaustive validation for all graph orders is possible by finite enumeration. The infinitary uniformity proof uses exact algebraic positivity; the all-2 trace identity uses a classical trace-class Fredholm determinant and is derived explicitly in `RESULT.md`. Source-access and potential unindexed equivalence risks persist. No independent external validation was performed.
