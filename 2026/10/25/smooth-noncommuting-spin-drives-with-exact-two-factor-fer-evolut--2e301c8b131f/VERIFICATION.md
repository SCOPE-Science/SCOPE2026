---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

PASS — Checked the full final formula and all quantifiers n>=1, Theta>0, any finite-dimensional nontrivial su(2) spin representation. The piecewise radial then constant-radius rotating f is C-infinity by the flat switch; it integrates H=dot(f). Rodrigues conjugation of the Fer recursion produces the two cross-product terms alpha(r)(f×h)+beta(r)((f×h)×f). At tan(2r)=2r, beta=0, and on the circular arc f×h=r² theta-prime e_z, so H2=A_n theta-prime Tz with A_n!=0. On the radial arc H2=0. F2=-i A_n theta Tz commutes pointwise with H2, forcing H3=0 exactly (not merely convergence); Pauli norm integral equals r(1+Theta) and nonparallel drive vectors prove noncommutation. Critical algebra, continuity at t=1, and n-root locations were independently checked; the actual numerical verifier was inspected, not counted as an infinite proof. Spin j norms differ from the Pauli area by 2j as stated in VERIFICATION.md.

## originality

PASS

PASS, qualified. The published 2026-10-20 spin-rigidity paper proves a no-go ONLY for real-analytic drives; its Theorem 1 and proof use analyticity at the start to propagate fixed axis. A nonzero compactly supported pulse is necessarily nonanalytic, so the theorem is inapplicable without contradicting it. The 2026-09-23 universal bound 2.6058 is sufficient for convergence and does not rule out exact special trajectories outside it. No matching smooth two-factor noncommuting family appeared in the semantic indexed-result search. The closed su(2) map itself is known; only special resonant smooth trajectory is put forward as new. Residual risk of an earlier smooth counterexample remains.

## value

PASS

PASS — This is a nontrivial boundary witness distinguishing strong real-analytic rigidity from C-infinity flexibility for the same exact Fer recursion. It yields a genuinely noncommuting all-time finite product with nonzero second correction and arbitrarily large operator-norm pulse area; a clear, motivated exception to a recent theorem, not a generic convergence-radius claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
