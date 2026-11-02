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

Run `python3 checker.py` from this package. The executable independently generates every set partition and every nested sequence of coarsening partitions up to the documented finite sizes, all exhaustive \(q\)-colour assignments, and all carrier permutations. It computes the automorphism-group order directly from the defining relations; it independently canonicalizes unlabelled isomorphism types and compares both counts to polynomial recurrences and the orbit-stabilizer identity. Checked \((q,K,n_{\max})=(1,1,5),(1,2,5),(2,1,5),(2,2,4),(3,1,4)\), plus displayed polynomial recurrences for further parameters. Successful execution prints `ALL_CHECKS_OK`.

The general theorem is proved symbolically in `RESULT.md`, including the top-degree coefficient, no-gap size spectra, and exact \(C_2\) automorphism characterization. The checker exhausts only those small finite search spaces; larger parameters are not exhaustively computed. No external or independent mathematical audit has been performed.
