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

Execute `python3 verify.py` with Python 3 and `sympy` installed. The program uses only symbolic algebra, exact finite summation, reproducibly seeded finite diagnostics, and a binary Gaussian-elimination check. The run on the embedded, byte-verified file returned `VERIFY_OK`.

The program checks the two normalized fourth-moment identities and the exact quadratic deficit symbolically with an indeterminate positive integer \(k\). It evaluates the proposed extremal arrays in dimensions \(n=2,3,4\) and directly enumerates \(2^{2n}\) possible sign vectors for \(n=2,3\) using exact algebraic arithmetic. For dimensions \(n=2,3,4\), it also checks several seeded integer-coefficient instances of the bound. Finally, it computes binary ranks of the four-cycle span for \(2\le n\le6\) and compares them with the graph's full cycle-space dimension.

The code verifies formal arithmetic and illustrative small cases. For **all** \(n\ge2\), the fourth-moment expansion, Cauchy--Schwarz equalization inequalities, interior maximizer, and graph chord argument are established in `RESULT.md`; finite experiments are not used to establish those infinite statements. No computational-accuracy uncertainty is attached to exact rational and symbolic checks, but exact arithmetic alone does not establish originality or independent validation.
