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

# Verification of exact three-orbit projection formulas

`CHECKER.py` computes each graph \(K_n\square P_3\) directly, with \(n=2,3,4,5,6,7,8\), constructs its signed incidence matrix, deletes one dependent Laplacian row and column, inverts the resulting matrix with `fractions.Fraction`, and reconstructs every entry of the canonical cut projector from first principles. The complementary cycle projector is obtained by subtraction from the identity. It checks the six stated rational edge-orbit column sums, and then the two maximum-norm branches, for **all \(322\) columns** in those seven examples.

Observed cut/cycle norm pairs are \((9/5,8/5)\), \((2,19/9)\), \((11/5,33/14)\), \((7/3,5/2)\), \((17/7,170/63)\), \((5/2,57/20)\), and \((23/9,98/33)\) in increasing graph order. Tests are exact rational computations but **finite**; no claim of exhaustive verification beyond that set is made. All-integer correctness rests on the complete algebraic proof. Independent mathematical audit has not been performed.
