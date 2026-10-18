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

# Reproducible mathematical checks

Run `python3 verify_steiner_currents.py` using Python 3; the script imports only Python's standard library. It builds the following Steiner \(2\)-designs directly from finite arithmetic: all pairs on five points, the projective planes of orders two and three, and the affine planes of orders three and five.

For each graph it constructs an unweighted point-to-block signed incidence, forms a grounded graph Laplacian, inverts that Laplacian in exact rational arithmetic, and constructs all entries of the orthogonal cut projector. It checks the incidence axioms, uniform diagonal \(\rho\), exact absolute column sums \(5-4\rho\) and \(6(1-\rho)\), matrix symmetry, and projector idempotence for all examples of at most \(52\) edges. It also independently enumerates **every** length-five edge-avoiding bypass for each root incidence edge and verifies equality of the complete electrical-flow column with the asserted direct-edge-plus-bypasses combination.

Expected final output: `VERIFIED 5 designs; 279 edge columns; 14064 length-five bypass paths`. This output was reproduced from the packaged script during the self-review. The five finite examples are not an exhaustive list of Steiner designs. The all-parameter statements follow from the explicit incidence-matrix proof in `RESULT.md`, not computational extrapolation.

A separate analytic consistency check verifies \(\rho+(k-1)(v-k)/(kv)=1\) and the identities \(\rho+5(1-\rho)=5-4\rho\) and \((1-\rho)+5(1-\rho)=6(1-\rho)\). No external independent audit has been conducted.
