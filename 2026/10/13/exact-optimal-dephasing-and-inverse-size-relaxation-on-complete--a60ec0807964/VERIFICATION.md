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

The independent finite test in `verify.py` builds the superoperator by applying the Lindblad expression directly to each elementary matrix, rather than assuming the three-by-three reduction. It diagonalizes the entire superoperator for site counts \(n=3,4,5,6,7\), two hopping strengths, and five dephasing choices per pair, comparing every eigenvalue with the proposed characteristic polynomial and checking the slowest decay rate. For selected models it tests the analytic population-contrast Laplace transform against an independent matrix resolvent and compares the full matrix exponential's diagonal with the reduced three-dimensional propagation. It also brackets the claimed noise optimum on both sides. The required packages are declared in `requirements.txt`; execute `python3 verify.py` from this directory.

Observed execution: `VERIFY_OK spectra=50 localized_profiles=12 optimum_brackets=40`.

The substantive proof is the invariant-space decomposition, cubic root monotonicity, separation from the residual pair, exact optimization, and nonzero slow-mode observable residue given in `RESULT.md`. No finite number of numerical instances proves the all-\(n\) statements. In particular, these checks do not establish novelty or independent validity, and the results do not extend to site-dependent noise or finite-time mixing-time optimality.
