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
# Reproducibility and verification

Install the declared package dependency with `python -m pip install -r requirements.txt`, then run `python verify.py` in this package directory. The verifier uses exact SymPy identities to rederive the two MSEs, the factored difference, the strict threshold derivative, the special budget inequalities, and three independent rational two-step Lanczos equalities. It checks four spectral pairs for each of two angular integrals using \(16384\) midpoint angles, brackets the unique crossover for six even budgets, and runs \(320000\) seeded Gaussian diagnostic draws. Successful replay prints `VERIFY_OK`.

These checks do not turn a finite experiment into a proof: the general assertion follows from the analytical radial/angular integrals and positive-denominator sign argument in RESULT.md. Source papers are cited by identifiers and URLs but are not included or redistributed. No finite-precision or higher-dimensional claims are certified by these diagnostics.

The two-node equality assumes a nonbreakdown Krylov pair, which occurs with probability one for independent standard Gaussian probes and two distinct eigenvalues; the strict comparison does not include the repeated-eigenvalue endpoint. The model does not compare all black-box algorithms or assert novelty merely from unsuccessful searching.
