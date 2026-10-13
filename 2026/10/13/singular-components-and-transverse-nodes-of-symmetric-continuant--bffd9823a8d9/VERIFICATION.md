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

The included `verify_continuant.py` uses only the Python standard library and exact integer/rational arithmetic; run it with `python3 verify_continuant.py`. Its output is recorded in `checker_output.txt`. It checks 660 deterministic seeded integer specializations of the bridge-cut determinant formula over sizes \(2\le n\le11\), exhaustively compares a derivative-based Jacobian singularity test with the union of the proposed components on all 199,260 integer coordinate assignments over \(3\le n\le6\) in the cube with entries \(\{-1,0,1\}\), verifies 65 rational generic-component witnesses in sizes \(3\le n\le12\), and checks the summed degree identity for \(3\le n\le19\). The precise number of Jacobian-singular grid points is 27,728. The checker was executed and its output matched.

None of these finite experiments proves the infinite theorem. The general proof is the continuum irreducibility/rank-block/coordinate-change argument in `RESULT.md`; all crucial identities and rank conditions are derived there. No independent audit has been performed. The component-intersection formal germs and global singular-scheme primary decomposition are not determined.
