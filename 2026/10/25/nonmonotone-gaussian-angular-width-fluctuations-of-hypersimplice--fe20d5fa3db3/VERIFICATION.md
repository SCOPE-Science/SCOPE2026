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

# Reproduction and verification

Run `python3 CHECK.py` from the directory containing the standalone checker. It uses only Python standard-library `fractions`, `math`, and `itertools` modules. The test constructs certified rational enclosures for \(\pi\), \((2\pi)^{-1/2}\), \(e^{-z^2/2}\), and the Gaussian integral for \(z\in\{0,1/2,1,3/2,2\}\), then verifies the strict nonmonotonicity relations and the balanced endpoint bracket. It separately tests that support extrema over all incidence vectors agree with Gaussian-order-statistic top-minus-bottom extrema for small rational vectors. Reproduction is deterministic.

The proof of the all-dimensional triangular-array CLT is mathematical, not computational. The checker does not establish uniqueness or completeness of local extrema, finite-n variance convergence, or any sparse-rank law. No independent mathematical audit is represented or implied.
