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

# Verification details

The proof gives a complete all-horizon argument with exact Fourier inversion and monotonicity of an elementary trigonometric quotient. The companion `verify.py` is standalone Python 3 with standard-library-only dependencies. Execute `python3 verify.py` beside this document.

The numerical checks run 60978 comparisons, including binomial-residue distributions versus the Fourier expression for \(h=1,\dots,18\), comparison with a \(1001\)-point probability grid for each \(h=2,\dots,60\), both predicted minimizers, the one-step boundary interval, and strict improvement over spectral tuning. Successful numerical checks provide consistency evidence only, not a proof of the infinite sequence of horizon claims. The formal analytic proof in `RESULT.md` supplies that coverage.

Independent auditing was not performed. Priority is conditional on the material actually inspected, including limitations on access to one related cycle-mixing paper.
