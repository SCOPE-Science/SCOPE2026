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

# Reproducibility and limits
Run `python3 verify.py` using the Python standard library. The observed output is recorded in `CHECKS.txt` and includes 917 passing assertions. The checker enumerates direct walk paths independently of the compact covariance formula, checks 200 additional five-step deterministic environments, uses exact Fraction arithmetic for the finite moment and dyadic residue tests, verifies algebraic smoothing-level multiplicities, and evaluates a finite mesh of the Fourier decay estimate.

The source-code contents embedded alongside this document constitute the complete dependencies for these tests. The almost-sure convergence, all-order residue uniformity, analyticity, exact limiting cumulants and uniqueness of the centered square-integrable smoothing fixed point follow from the explicit proofs in `RESULT.md`. Finite enumerations or numerical checks do not establish the corresponding infinite theorems. No independent audit or independent validation has been performed.
