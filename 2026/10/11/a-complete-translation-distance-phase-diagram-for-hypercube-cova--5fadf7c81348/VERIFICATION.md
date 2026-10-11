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

The result is proved analytically in `RESULT.md`. The critical equal-coordinate lemma is checked from the derived second derivative identity \(f''(u^2)+f''((1-u)^2)=(1-2u)^2/[4u^3(1-u)^3]>0\), and the support-transition theorem follows from an exact sign analysis of the derivative of \(\log(F_k/F_{k+1})\). These analytic arguments apply to every integer dimension \(d\ge2\) and every \(0<s<\sqrt d\).

Run `python3 verify.py` to perform deterministic finite numerical checks. The code uses only the standard Python library and seeds its pseudorandom generator. It reconstructs overlap volumes from coordinate intervals, compares 263,200 randomized fixed-norm competitors against the branch maximum (the exact printed count is definitive), and computes the critical universal root and adjacent thresholds. The finite checks do not certify global optimality or mathematical originality, and no independent audit is reported.
