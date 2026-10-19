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

# Verification record

The companion standalone `verify.py` uses exact rational integration of the map \(x\mapsto\sigma_\pi(f_\varepsilon(x))\), partitioned by full-branch inverse images of output-cell boundaries. All sign configurations and all permutations are checked for the six finite parameter pairs \((m,N)=(2,2),(2,3),(3,3),(3,4),(4,4),(4,5)\), totaling 2,576 cases; it also enumerates the exact permutation mean/variance against formulas for each orientation. The program prints `VERIFY_OK` on success and raises an assertion on failure.

The verification calculation uses direct branch integration, not the conditional-expectation or rank-reduction identities from the proof. Consequently it checks the formulas at the specified finite sizes without proving the claims for arbitrary sizes or the Gaussian weak limit. The universal claims follow from the printed analytical steps in `RESULT.md`; the latter invokes a published quantitative combinatorial central limit theorem.

The entire result relies on uniform stationary initialization and ordinary Lebesgue integration; endpoint conventions have no statistical effect. No independent audit or external certification has been performed.
