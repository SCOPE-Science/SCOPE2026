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

The supplied `verify_paired.py` was executed with SymPy and returned `PASS`. Its exact checks rebuild the interval lengths and transition probabilities from the affine map, verify stationarity and primitivity, calculate the odd spectral polynomial, verify the correlation law through lag \(10\), and verify the rational generating function and its first derivative at unity. Independent numerical time-series experiments are not used as proofs.

The infinitely many correlation identities follow analytically from Cayley–Hamilton and checked initial conditions. The Gaussian limit invokes the classical finite-state primitive Markov-chain central limit theorem, with strictly positive calculated variance. Finite symbolic checks do not by themselves validate that limit theorem. Endpoint conventions are irrelevant under the absolutely continuous stationary law. The earlier six-cell Markov partition and its spectral framework belong to the cited source, not to this computation.

Independent audit: not performed.
