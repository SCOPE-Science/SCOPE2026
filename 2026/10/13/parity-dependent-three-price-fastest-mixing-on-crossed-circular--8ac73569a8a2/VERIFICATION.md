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

# Reproducibility and verification limits

Run `python3 verify.py` in a directory containing the accompanying standalone checker. Python 3 and NumPy are required; no web access or external data are required.

The checker uses a fixed deterministic pseudorandom seed; independently enumerates intersections of bounding planes in the exact three-variable model; compares all analytic vertex candidates with that enumeration; constructs undirected Laplacian matrices directly from their edges; compares numerical full-matrix spectra with the Fourier eigenvalues; normalizes randomly generated nonuniform edge rates to the stated price budget; and checks the strict-regime predictions.

Observed result:

`VERIFY_OK vertices=45 independent_min_costs=850 full_spectra=130 nonsymmetric_budget_comparisons=430 phase_checks=640`

Finite floating-point tests alone neither prove optimality for all positive prices and every graph size nor constitute a mathematical originality certificate. The proof in RESULT.md gives an exact symbolic spectral reduction and an exhaustive polyhedral argument for every integer \(n\ge5\). The executable is supplementary and does not classify all possible nonsymmetric optimizers.
