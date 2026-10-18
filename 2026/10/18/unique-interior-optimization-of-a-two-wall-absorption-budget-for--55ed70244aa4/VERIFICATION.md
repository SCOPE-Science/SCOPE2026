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
The standalone `verify.py` executes with Python 3 and SymPy, with no online or private data dependencies. The program reconstructed the backward interior equations, both sticky-wall equations, the unbiased MFPT against the published generic-boundary formula, all key derivative and monotonicity expressions, an exact radical optimum, and a finite grid of rational-rate/initial-state endpoint signs. Its run reported `PASS 994 including all-direction boundary witnesses`.

The exact finite assertions are corroboration and are not substituted for the analytic proof over all positive parameters. The strict inequalities needed for the global theorem are given symbolically in `RESULT.md`: positivity of \(C'(u)\), monotonicity of \(t/(1+\eta t^2)\) for \(0<\eta<1\), and the boundary-range comparison for \(|\delta|\le p+1\). Independent auditing has not been performed.
