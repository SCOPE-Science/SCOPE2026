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
# Reproduction and limitations

Run `python3 check.py` using only the Python standard library. The checker performs 1,841 exact rational tests of the first and factorial-second generator identities for finite configurations with 2, 3, and 4 sites; checks the rational two-site witness, exact stationary means and moment-gap inequalities; its literal output is `CHECK_OUTPUT.txt`.

The universal statements are not inferred from finite sampling. Their proofs use the displayed generator identities, irreducible Metzler Perron eigenvectors, positive inverse-resolvent Lyapunov weights, and stochastic coupling to a one-site regenerative process. The test cannot certify independent publication priority, the infinite-network limit, or behavior of stationary distributions with infinite mean.
