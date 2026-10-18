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

The mathematical proof is self-contained in RESULT.md. The nonstandard ingredient is an elementary \(\ell_p\)-splitting fact for bounded weakly null sequences, proved by finite-head approximation. No finite computation is used to infer a universal infinite-dimensional statement.

The included executable `CHECK.py` uses fixed seed `314159`, five exponents for \(p\), six values for \(q\) (including both endpoint types), and 3,500 positive-coordinate tuples per exponent pair. It verifies the two-sided mixed-norm bounds, the tame-inequality upper estimate, and 30 explicit equality witness comparisons. Running `python3 CHECK.py` should print `PASS: 105000 finite parameter tests; 30 exact-construction comparisons.` Numerical floating-point tolerances are deliberately modest; these calculations are diagnostics only.

For hand replay, normalize \(f_0\in F\) to norm one and calculate the norms of \((f_0,e_{n+1})\) and \((0,e_1+e_{n+1})\) in \(F\oplus_q\ell_p\). They are exactly \(2^{1/q}\) and \(2^{1/p}\), independently of \(n\), which directly verifies sharpness. To verify the infinite-dimensional upper bound, check the two applications of Minkowski in the mixed-norm comparison (5), then maximize the scalar function in Step 4.

Limitations: the tests are neither exhaustive nor an independent mathematical audit. Bibliographic comparisons are described in REVIEW.md and AUDIT.json. Independent audit: not yet performed.
