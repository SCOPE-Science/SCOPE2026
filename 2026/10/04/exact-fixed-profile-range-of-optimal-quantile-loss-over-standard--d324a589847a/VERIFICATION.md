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
# Verification

The proof is analytic. The accompanying checker uses exact rational arithmetic whenever a comparison can be squared without changing sign.

For generated rational mass profiles, rational quantile levels, and strictly increasing rational supports it verifies:

- direct minimization of the pinball loss over all atom locations;
- the adjacent-gap coefficient formula;
- the exact covariance representation with the cell-averaged quantile score;
- the lower bound and strictness for three or more atoms;
- the upper Cauchy--Schwarz bound;
- the conditional-variance formula for the upper constant;
- exact two-point equality;
- the three-point central-cell upper equality construction;
- convergence toward both nonattained endpoints.

The computations are finite stress tests. They do not establish the universal theorem or exhaust all probability profiles.

Independent audit has not been performed.

Exact-rational replay result: `VERIFY_OK direct_checks=2500 covariance_checks=2500 lower_checks=2167 upper_checks=2500 formula_checks=2500 two_point_checks=333 three_attain_checks=1000 boundary_checks=4667`.
