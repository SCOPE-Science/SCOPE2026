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

# Verification notes

Running `python3 verify.py` returns `VERIFY_OK` after checking the exact odd/even partition factorization by independent exhaustive enumeration for \(0\le n\le16\), exact normalization against \(p(n)\) at several larger cutoffs through \(n=2000\), and finite numerical consistency with the local Gaussian expression at admissible lattice values. The checker uses only the Python standard library.

The analytical argument is not predicated on enumeration. Its noncomputational inputs are the classical asymptotics for ordinary and odd/distinct partitions. The proof's Taylor remainder is uniform for each fixed scaled compact window. No all-support relative estimate, rate of convergence, or independently validated proof is asserted.
