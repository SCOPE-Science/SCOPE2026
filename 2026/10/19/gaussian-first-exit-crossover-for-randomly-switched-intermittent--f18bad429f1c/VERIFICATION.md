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

# Verification and reproducibility

Run `python3 check_escape.py` from a directory containing the standalone script. Successful finite checks print `VERIFY_OK`.

The checker uses standard-library rational arithmetic to test the conjugacy at integer exponents, compares both neutral-branch updates to the exact original map for a grid of admissible real parameters, reconstructs the finite stopping identity from each simulated trajectory, and runs seeded finite ensembles in each of the three regimes. It checks neither infinite limits exhaustively nor historical novelty.

The mathematical proof uses the coordinate \(z=(2x)^{-\alpha}\), the exact branch updates, the elementary uniform Taylor bounds, an optional-stopping occupation estimate based on a nonnegative potential, the Bernoulli uniform law of large numbers and functional CLT, and a truncated Riemann-sum limit for the slower-branch occupation. The rates are for fixed \(\alpha\), \(\beta\), and \(p\) as the deterministic initial-coordinate parameter \(Z\to\infty\).

The original papers cited in the result concern the known map family and first-order return-interval behavior. This package contains no independent audit, no claim about stationary return-time laws, and no external publication or priority certification.
