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

# Reproducibility

Execute `python3 verify.py` with a standard Python 3 installation. The program uses only standard-library rational arithmetic, binomial coefficients and square roots. Expected output is `VERIFY_OK exact=1116 numerical=114`.

The exact tests enumerate batch counts and joint trajectory probabilities up to three iterations on three explicit nonorthogonal systems, and compare each coordinate's direct expected square with powers of the derived two-by-two moment matrix. Additional floating-point identities check both formulas for the Perron eigenvalue and the endpoint crossing. All-iterate mean-square convergence, divergence, limiting rates, convexity and optimization are established in `RESULT.md` by algebra and Perron eigenvalue theory; no finite test is represented as an infinite proof. This is a self-review only, not independent certification.
