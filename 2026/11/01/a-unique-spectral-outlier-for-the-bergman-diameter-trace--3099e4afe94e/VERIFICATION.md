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

# Verification and scope

The formula for the positive matrix was derived by direct integration of weighted monomials on the full symmetric diameter. Weighted Schur estimates use convexity of \(F_n(x)\) and its exact logarithmic integral. The two-by-two compression and the explicit off-diagonal norm are exact. The spectral uniqueness uses the codimension-one min–max argument; the essential norm lower bound uses a weakly null logarithmic-window sequence, with sum asymptotics proved by integral comparison.

The standalone Python 3 checker `CHECK.py` completed with **8,705 deterministic assertions** and reported finite leading eigenvalues \(1.162941479656\), \(1.182950248683\), and \(1.197017016769\) at truncation sizes \(12\), \(24\), and \(60\), respectively. These data neither determine the exact infinite-dimensional eigenvalue nor replace the analytic proof. The computed Weyl-sequence Rayleigh quotients approach, but do not attain, the essential spectral edge in the tested finite windows. The result has not undergone independent mathematical audit.
