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

The reproducible checker is the companion `CHECKER.py`, executable as `python3 CHECKER.py` using only the standard library. Its successful output contains `VERIFY_OK`.

The script uses exact fractions throughout. On each of the two parameter intervals it enumerates all affine endpoint-order transitions, finds the resulting parameter cells, and uses two distinct rational interpolation points per cell to certify the affine Perron--Frobenius equality and the exact interval integrals. It independently verifies the Markov transition probabilities and stationary weights at \(\beta=4\), the vector equation \(P^2v=-v/2\), and the zero lag-one covariance. Exact matrix powers match the claimed covariance through lag 30; direct subdivided initial-condition cylinder integrals match through lag 12. These finite checks are not substituted for the infinite-lag proof, which is the explicit vector equation.

The separate endpoint argument at \(\beta=3\) uses the published endpoint density and at \(\beta=4\) uses the four-state Markov partition. The claimed parameter range is \(3\le\beta<9/2\); no source-independent proof of uniqueness of arbitrary invariant probabilities is asserted. Independently conducted scientific and historical-priority audits have not been performed.
