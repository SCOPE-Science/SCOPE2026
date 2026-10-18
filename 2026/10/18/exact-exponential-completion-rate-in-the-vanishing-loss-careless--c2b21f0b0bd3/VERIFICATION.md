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

# Reproducible checks

Run `python3 check.py` with Python 3 and no external dependencies. The script constructs the original post-draw loss process on all subsets for \(n=2,3,4\), solves six finite stationary distribution systems exactly using rational Gaussian elimination, verifies every set-inclusion identity independently of the scalar recurrence, and checks stationary entrance flux. The computed full-state masses for \(n=2,3,4\), with losses \(1/3\) and \(2/5\), match the stated product formula. Approximate finite-exponent calculations at three larger sizes converge numerically to the integral in the theorem.

These checks verify specific finite identities, not the infinite-sequence limit or claimed originality. The uniform convergence, monotone coupling, total variation mixing estimate, and block-hitting bounds are mathematical proof arguments in `RESULT.md`. The published literature comparisons are described in `REVIEW.md` and `AUDIT.json`. No independent audit has been performed.
