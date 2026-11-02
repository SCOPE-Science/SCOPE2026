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

# Verification

The independent scientific audit is not performed. The result is reproducible from its proof and `verify.py`.

Run `python verify.py` with `sympy` installed. Its exact symbolic checks confirm all parameter expansions, the signed \(3\)-by-\(3\) determinant formula, and the common characteristic polynomial. Rational checks test 500 different admissible parameter triples and every chronological permutation, plus 42 exact nonlinear trajectory identities with boundary initial states. The displayed survival reversal is exact rational, not a floating-point classification. The global asymptotic conclusion is proved with the positivity of the three-step matrix, Perron–Frobenius theory, and the stated exact solution formula; a finite checker does not prove it. Actual source access: full Mertens 2006 PDF and open Caswell 2019 chapter were inspected; the full Cushing–Ackleh 2011 article remained unavailable. The substantive unresolved issue is historical priority over any unlocated stronger general rational population-map theorem.
