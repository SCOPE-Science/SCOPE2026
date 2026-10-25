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
# Verification of the finite-recruitment accountability theorem

The proof's nonstandard step is the continuation valuation of a vacancy. Conditional on vacancy at the beginning of an epoch, the deterministic marginal per-round cost is \(D(m)=\kappa/[m(m-1)]\). Its epoch sum is \(A D(m)\), and only joint survival and unsuccessful recruitment, of factor \(t(1-\rho_m)\), preserves the vacant state. Iterating gives the **exact infinite** geometric expression \(A D(m)/[1-t(1-\rho_m)]\) because \(t<1\); the algebraic argument covers all allowed real parameters, not a finite simulation.

The included exact-rational program checks the Bellman fixed-point and finite-sum-plus-exact-tail identity for 15,840 parameter combinations across \(2\le n\le11\), and checks the sharp last-two-size inequality across \(3\le n\le12\), producing 260 strict-reversal points on its rational grid. The witness at \(n=3\) has normalized value differences \(-1/40\) for size two and \(+1/10\) for size three. Program requirements: Python 3 standard library. Execute `python3 check_recruitment.py` in the directory containing the extracted program.

Limits: parameter grids are not proofs beyond their tested points; the universal claim is proved analytically in `RESULT.md`. No independent auditor has examined the work. This check does not support equilibrium selection, strategic entry or a rule letting the exploited individual rejoin.
