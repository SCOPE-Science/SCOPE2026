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
# Reproducibility

Run `python3 verify_rook_h1.py` from the directory containing `base_certificates.json`. The standard-library script builds all relevant triangles directly from rook adjacency, checks every listed certificate entry is a true face, and recomputes three integer determinants with fraction-free Gaussian elimination: \(-1\) of order \(26\) for \(3\times3\), \(+1\) of order \(54\) for \(3\times4\), and \(+2\) of order \(105\) for \(4\times4\). All matrix rows refer to the explicit spanning-tree integral cycle basis; every selected column is an actual triangle boundary. It verifies the row/column integer cocycles and global mod-two obstruction on the relevant base complexes.

The script also checks the connected-link condition in 21 small induction instances, including all \(4\)-through-\(7\)-row/column combinations and \(3\)-by-\(4\) through \(3\)-by-\(8\). These finite link checks do not prove the theorem for arbitrary sizes. The written link-witness construction and Mayer–Vietoris argument carry the infinite-family proof. Independent external audit was not performed.
