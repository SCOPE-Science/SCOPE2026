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

# Verification and scope

The supplied `verify.py` requires only Python 3.10+ standard library. Execute `python3 verify.py`. It checks 32 independently time-integrated two-state matrix-propagation instances against the exact closed form, 16 spectral identities and derivative identities, eight small-asymmetry local minimum coefficients, and seven complete concave-lobe counts (each mirrored under sign reversal). For the representative parameters \(a=1\), \(v=2\), the counts for \(\varepsilon=0.1,0.05,0.02,0.01,0.005,0.002,0.001\) are respectively \(3,6,15,31,62,157,314\); the predicted limit for \(|\varepsilon|N\) is \(0.314400538709237\ldots\).

The proof in `RESULT.md` independently establishes the infinite-time zero exclusion, the finite number of intervals for every nonzero asymmetry, and the small-asymmetry limit by concavity and scaled-envelope bounds. Finite computation cannot establish a universal or asymptotic theorem. The script uses an analytic late-time envelope bound to terminate each concrete lobe census; it does not use numerical timeouts as impossibility evidence. The comparisons do not establish literature uniqueness or independent mathematical certification.
