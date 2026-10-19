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

# Reproducible finite-field checks

Use `cc -O2 -std=c11 -Wall -Wextra verify.c -o verify && ./verify` in a directory containing the companion source file `verify.c`. The program constructs the full eight-by-eight linear commutator matrix for the four-cycle directly from the multiplication of paths of length one and two and computes its exact rank using modular row reduction.

Every possible \((a,b)\in\mathbb F_q^8\) is checked for \(q=2,3,5\). The rank-frequency vectors at ranks \(0,2,4,6\) are \((1,9,102,144)\), \((1,32,1344,5184)\), and \((1,144,30480,360000)\), respectively. The respective conjugacy-class totals are \(190\), \(2289\), and \(49105\). The program also checks the vanishing of the other ranks and the formula for the total number of conjugacy classes. The successful output ends in `VERIFY_OK`.

The test checks prime fields only; arbitrary prime-power fields are covered by the symbolic algebraic proof. It does not replace the proof and does not independently verify every instance of the higher-cycle witness theorem. Independent external mathematical audit has not been performed.
