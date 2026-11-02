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

# Verification and limits

Run `python3 verify.py` with Python 3; no third-party packages are needed. The checker constructs \(\mathbb F_2\), \(\mathbb F_3\), and the nonprime field \(\mathbb F_4\) using the relation \(t^2+t+1=0\). For the three-dimensional Heisenberg algebra, it exhaustively enumerates every linear operator, tests both its square and the defining weight-one Rota–Baxter identity directly, and computes the rank by finite-field Gaussian elimination. The resulting coefficient arrays (from constant term upward) are \([1,9,0]\), \([1,32,0]\), and \([1,75,0]\), respectively. For the five-dimensional algebra over \(\mathbb F_2\), all \(65536\) horizontal matrices and associated central functionals are enumerated, and the rank coefficient array is \([1,225,990,0]\). Every assertion must pass for `VERIFY_OK` to print.

These finite checks confirm sample coefficients but are not an exhaustive proof of the infinite family. That proof uses the center-preserving normal form, isotropic-space counting, quotient-map enumeration, and degree comparison in the companion mathematical text. Independent mathematical validation and global publication-priority verification have not been performed.
