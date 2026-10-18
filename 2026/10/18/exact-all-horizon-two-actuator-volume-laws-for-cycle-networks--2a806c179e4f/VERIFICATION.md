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

Run `python3 verify.py` with Python 3 and no additional packages. The verifier reconstructs the cycle Laplacian, both independent input columns, every finite-horizon Gramian, and exact integer determinants using fraction-free elimination; it does not ingest numerical eigensolver approximations. It tests 440 exact Gramian determinants over cycle orders 3 through 15 and two affine shifts, checks equality within the gcd/parity classes and the even-order optimality ordering, and checks exact spectral formulas on cycles of orders 3, 4, and 6, whose distinct Laplacian eigenvalues are integers.

The universal Fourier factorization, sine-product identities, and Schur-complement ordering are analytical; these finite checks are corroboration rather than a proof of infinitely many orders. In particular the checker does not establish historical novelty, cover more general graph topologies, prove strict cross-parity inequality, or validate any independent audit channel.
