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

# Finite verification and analytical boundary

Execute `python verify.py` with Python 3. The program enumerates each \(n^n\) preference vector for \(1\le n\le7\), retains only successful parking runs, and checks the resulting final-car deficit probabilities against the exact formula attributed to Pinsky. It also checks by rational arithmetic the strict coordinatewise mass loss, normalizations, transition conservation and successive likelihood-ratio order for \(n\le100\). Floating calculations only illustrate the Borel ratio and asymptotic tail. Observed result: `VERIFY_OK 735 assertions, exhaustive n<=7; rational transitions n<=100`.

The infinite-index claims are proved separately by analytic inequalities, monotone convergence, and Stirling/Euler--Maclaurin expansions in `RESULT.md`. Enumeration through seven cars cannot establish the infinite-index theorem. The source formulas are independently checked in finite small sizes and credited rather than rederived as new. No external or independent audit has been performed.
