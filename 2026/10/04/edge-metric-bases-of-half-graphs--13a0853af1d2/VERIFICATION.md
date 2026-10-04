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
The general proof was checked from the defining distances, including the boundary case \(p=2\), the marker-threshold lower bound, the exclusion of \(b_1\) and \(a_p\) from every minimum basis, and the prefix/suffix inequalities forcing \(z_r=1\).

`verify.py` independently constructs every half graph \(H_p\) for \(2\le p\le9\), computes graph distances by breadth-first search, and checks all subsets of sizes \(p-2\) and \(p-1\). It verifies that no smaller generator exists and that a size-\(p-1\) set resolves the edges exactly when it chooses one vertex from each \(\{a_r,b_{r+1}\}\).

Replay output:

`VERIFY_OK p_range=2..9 subset_checks=101762 basis_checks=59278 transversal_checks=510 max_order=18`

The exhaustive range is finite and does not certify larger values of \(p\); the infinite claim is supported by the symbolic proof in `RESULT.md`.
