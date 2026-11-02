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

# Verification record

The mathematical evidence is the series/parallel harmonic-equilibrium derivation, the finite sum identity, the fixed-length strict monotonicity, the unique cubic stationary root and asymptotic expansion stated in `RESULT.md`.

The standalone Python 3 file `verify.py` performs an independent grounded-Laplacian solve over exact rational numbers for every chord in paths of lengths 3 through 11, compares the entire equilibrium potential vector, recomputes the total gain, checks global endpoint optimality and tests cubic-root bracketing for lengths 3 through 159. It reports `PASS 989 exact/comparison assertions` when executed as provided. The exact system solver does not use the analytic voltage formula, but the checker also evaluates the formula and thus can detect disagreements. Its finite scope does not establish the infinite theorem, which is proved algebraically.

Public source comparisons include the full relevant results and methods of Zhao, Liu and Wang (2014) and the full mathematical Problem 1, algorithms, and proof in Zhou and Zhang (2021). The latter's allowed edge class is restricted by hypothesis and does not directly establish the global path result. A historical duplicate might remain undetected. Independent audit has not been performed.
