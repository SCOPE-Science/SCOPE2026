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

# Reproducibility and scope

The attached `verify.py` directly builds the \(S_n\) Cayley-graph Hamiltonian for small sizes, checks the quantum amplitude and its standard-character expectation against the independently computed branching formula, and verifies the leading quadratic moment. It evaluates fifteen finite approximations to the Bessel-square profile; this is numerical corroboration, not an infinite-size certificate. Reproduce with `python verify.py` after installing `requirements.txt` dependencies.

The analytic proof relies on established Young branching, Jucys–Murphy content eigenvalues, and Kerov's transition-measure continuity together with Plancherel limit shape concentration. The limiting assertion is for each fixed scaled time, not uniform across all times or all modes. Self-review found the stated critical identities consistent with the finite computations; no external or independent audit has been performed.
