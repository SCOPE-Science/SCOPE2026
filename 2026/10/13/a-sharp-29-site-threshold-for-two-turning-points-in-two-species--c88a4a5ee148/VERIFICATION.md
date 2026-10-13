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

From the directory containing this file and `verify_zeta.py`, run `python3 verify_zeta.py` with Python 3. The verifier prints:

`VERIFY_OK lower_pairs=3654 boundary_pairs=406 unique_pair=(22, 26) direct_subsets=146595 weighted_curvature_identities=56`

The enumeration examines every unordered unequal occupancy pair among two positive-incidence species, at each site size from two through 29. To determine whether a ratio increased or decreased, all positive denominator factors are cleared and the sign is decided with exact integers. Equal occupancies are handled by the elementary monotone ratio formula. No floating-point tolerance or random sampling enters the proof. A separate direct subset enumeration reconstructs zeta values from the concrete 29-site presence–absence matrix for depths one through five. An exact rational implementation checks the variance identity across other occupancy profiles. The general identity is additionally proved algebraically in `RESULT.md`; its finite tests are consistency checks, not a proof over all input sizes.

Scientific limits: exactly two species for the sharp minimality and uniqueness result; all-combinations uniform without-replacement design; no guarantees for estimation errors, other sampling schemes, or a universal upper bound on turning points at larger site counts. This package contains a self-review; independent audit has not been performed.
