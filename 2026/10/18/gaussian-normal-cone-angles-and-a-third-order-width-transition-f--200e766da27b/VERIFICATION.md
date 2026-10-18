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

# Reproducibility and limits

Execute `python3 verify.py` using Python 3 and its standard library. The complete script accompanies this result and uses no external data, third-party packages, remote services or hidden files.

The script enumerates all 30 parameter combinations with \(1\le m\le5\) and \(1\le n\le6\) to check **every vertex's** exact rational normal-cone angle from all \(2^m m!\) sign/absolute-rank configurations. It also verifies 1,360 support-maximization tests for all \(1\le m,n\le4\), segment and right-triangle mean widths against exact formulas, and three normalized-width asymptotic profiles at dimension \(240\). All assertions passed and the script printed `CHECKS_PASSED normal_angle_profiles 30 direct_support_tests 1360 exact_planar_benchmarks 2 scaling_profiles 3`.

The exact formulas and the limit theorems require the analytical steps in RESULT.md. Neither numerical integration nor finite enumeration proves their universal claims. In particular, there is no independent audit or formally certified proof.
