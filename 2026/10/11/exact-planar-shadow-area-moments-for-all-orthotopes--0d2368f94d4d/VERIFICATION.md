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
# Verification and limits

The analytic proof covers all integer dimensions \(d\ge3\) and strictly positive orthotope side lengths. Its four critical identities are the zonotope area expansion, the Cauchy–Binet unit-bivector norm, the circular shared-index absolute product integral, and the \(SO(4)\)-invariant self-dual/anti-self-dual calculation for disjoint indices. The last step requires \(d\ge4\); the disjoint-index term is absent for \(d=3\).

Replay `python verify.py` in an environment with NumPy and SciPy. It uses a documented fixed numerical pseudorandom seed, constructs Haar two-frames by Gaussian Gram–Schmidt, checks convex-hull area independently against the zonotope determinant sum for 120 samples in dimensions \(3\)–\(7\), and checks scalar moments for 120,000 samples per dimension. The recorded run returned `CONVEX_HULL_CHECK_OK` with maximum difference \(2.665\times10^{-15}\), then `VERIFY_OK`, including cube dimensions \(3,4,5,7,12\) and unequal orthotopes of dimensions \(3,4,6,9\).

Monte Carlo agreement is not a rigorous finite-error enclosure and cannot prove the all-dimensional identities. Analytic group invariance, beta/Gamma integration and exact pair indexing establish the theorem. Numerical thresholds in the script are diagnostic tolerances, not mathematical hypotheses or certification.
