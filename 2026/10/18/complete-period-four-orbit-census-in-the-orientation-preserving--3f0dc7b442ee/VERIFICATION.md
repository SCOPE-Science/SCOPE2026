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

# Verification of the period-four orbit census

The companion Python/SymPy checker explicitly tests all four periodicity identities for the three proposed primitive sign itineraries and the alternating two-cycle. It also verifies the expansions of \(P,U,V,R\) in the positive parameter \(t=a-b-1\), calculates exact fourfold Jacobian traces and determinants, and checks rational parameters in both count regimes. Execute `python lozi_period4_checker.py` with Python 3 and SymPy.

The proof, not finite sampling, excludes further orbits by binary necklace exhaustion, establishes positivity of all auxiliary polynomials on \(0<b<1\), \(t>0\), and establishes uniqueness of the collision curve from the derivative of \(P\) in \(t\). At \(P=0\) the orbit meets the nondifferentiable switching line; only off-boundary saddles are claimed. The dated original source is indexed August 1, 1978 by SciSpace; the original publisher confirms only the month. Historical novelty has residual access qualifications recorded in the scientific review.
