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

For arbitrary \(k>0\), \(A>2k\), the four exact elementary solutions in `RESULT.md` satisfy the two piecewise-linear second-order equations in their respective quadrants. The crossing times \(\theta_\pm\) satisfy \(\cos\theta_-=-k/(A-k)\), \(\cos\theta_+=k/(A+k)\), and their nonzero velocities equal \(\sqrt{A(A-2k)}\) and \(\sqrt{A(A+2k)}\) in magnitude. The endpoint and return-state formulas follow by substituting these trigonometric identities; no approximation is required.

The energy obstruction for \(A\le 2k\) and the strict sign of the exact period derivative establish the global-in-amplitude conclusions. `verify.py` independently evaluates the four junction residuals, acceleration crossing signs, energy threshold and derivative formula at a deterministic set of positive parameters, printing `CHECK_OK` on success. Such finite checks do not imply universal validity or certify external literature comparisons; the universal statements rest on the displayed proof.

Independent audit status: not performed. There is no external validation claim.
