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

Install the dependency from `requirements.txt` and invoke `python verify.py` in the extracted finding directory. The checker constructs the full subdivision Laplacian independently for 24 connected regular source graphs, checks 9,338 exact off-diagonal RK4 polynomial coefficient vectors, tests rational steps on and around the claimed sharp horizon, verifies row sums and an extremal Laplacian eigenvector, and reconstructs the symbolic positivity certificates.

Observed output:

`VERIFY_OK 24 different regular base graphs; 9338 exact off-diagonal RK4 coefficient comparisons; rational steps and spectral eigenvector verified; all symbolic certificates verified`

The checker uses exact arithmetic; it does not establish universal correctness by graph enumeration. Universal quantifiers follow from the incidence-block formulas and inequalities in `RESULT.md`. Spectral contractivity is not the same as entrywise positivity; no stagewise positivity is asserted. Independent validation has not been performed.
