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

The proof is self-contained: it uses Walsh orthogonality, elementary homogeneous harmonic polynomials, and direct sign projection. In particular, it establishes the infinite family of rank statements analytically for all integers \(d\ge3\), while `check_cube_ranks.py` supplies optional finite exact-rational corroboration.

Reproduction: run `python check_cube_ranks.py` using Python 3. The observed output was `CUBE_EXACT_DEGREE_RANK_OK 975 exact Krawtchouk spectral checks; 10 dimensions`. The checker verifies all degrees \(0\le k\le d+2\) in dimensions \(3\le d\le12\), and the elementary witness coefficients. It does not independently certify the infinite-dimensional theorem or the literature comparison. Neither an independent scientific audit nor independent validation has been performed.
