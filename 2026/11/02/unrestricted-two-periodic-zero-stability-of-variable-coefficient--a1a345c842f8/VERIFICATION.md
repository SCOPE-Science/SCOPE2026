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

Running `python verify_bdf4.py` derives both BDF4 matrices directly from rational Lagrange cardinal derivatives and proves their displayed characteristic polynomial identity symbolically. All five strict Schur polynomial identities are checked by exact expansion and every nonzero coefficient of each positive certificate is positive. Exact reciprocal symmetry, endpoint polynomial limits and the first-order asymptotic coefficient \(16/3\) are verified.

The order-five obstruction is not a sampled near-unit eigenvalue: the code constructs BDF5 weights from scratch with exact rational arithmetic at \(r=10\) and proves the rational negative value of \(\det(I_4+G_1G_{10})\). A supplementary NumPy loop checks 301 finite ratios and is expressly not used as a universal proof.

Boundaries: this is homogeneous zero stability for fixed alternating ratio, not stability for arbitrary time sequences or nonzero differential equations. Complete independent mathematical validation is not performed.
