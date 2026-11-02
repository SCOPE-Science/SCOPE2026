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

The full geometric tube asymptotic follows from upper and lower geometric inequalities in `RESULT.md`, not from a finite computational experiment. The code `verify.py` uses only the Python standard library. Running `python3 verify.py` checks 1,276 exact-rational inverse-branch and cylinder assertions for four fixed rational values of \(q\). It also probes six finite-scale horizontal union-width approximations; these are not exact two-dimensional Euclidean neighborhood areas and are used only for scale intuition.

For fixed \(q\in(0,1)\), the upper cutoff is the least \(N\) with \(q^N\le\varepsilon\). The tail graph is inside a strip of width at most \(\varepsilon\). The lower cutoff requires both the innermost opposite-branch gap and the narrowest within-side branch gap to exceed \(4\varepsilon\). Both cutoffs equal \(\log(1/\varepsilon)/\log(1/q)+O_q(1)\); their matching leading coefficients prove the formula. Boundary-point extensions do not affect the closed open-branch graph or Lebesgue-theoretic conclusion. No independent audit or formal proof assistant validation has been performed.
