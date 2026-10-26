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

- The analytic proof derives the logarithmic recurrence for \(u_n=-\log x_n\), treats the two cycle-duration assumptions separately, and obtains the outside-time asymptotics by summation.
- The example's exact return map is reconstructed from the slow and fast branches:
  \(r(x)=\sqrt{1+x^2}-1\) and \(F(x)=r(x)/(1+r(x)-r(x)^2)\).
- `verify.py` was run from the packaged path. It checks the quadratic coefficient, quartic coefficient, and leading cycle-duration coefficient symbolically.
- The symbolic checks do not prove the infinite-time theorem; the proof in `RESULT.md` does that.
- Scope limits: no claim is made for \(p=1\), unbounded outside-time contributions, or trajectories without infinitely many returns.
- Independent audit and independent validation have not been performed.
