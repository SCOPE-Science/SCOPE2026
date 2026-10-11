---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Solving the equilibrium equation separately on \(x>0\) and \(x<0\) gives the always-present negative root and the positive pair exactly for \(c\le1/100\), with coalescence at \(x=1/10\). At nonzero equilibria, direct differentiation and elimination of \(c\operatorname{sgn}(x)\) gives the stated cubic. The smaller positive branch has negative constant term and is unstable; the larger branch satisfies the Routh inequality throughout. On the negative branch, the Routh quantity is monotone and vanishes only at \(x_H=(10-3\sqrt{230})/197\); independent exact arithmetic reproduced \(c_H\approx0.06850593165728569\) and the factorization with imaginary pair \(\pm i/\sqrt{10}\). At the origin, the left smooth extension has a positive real eigenvalue for every \(c>0\); its local unstable branch lies in \(x<0\), where it coincides with the original vector field, proving Lyapunov instability without differentiating \(|x|\) at zero.

## originality

PASS

The accepted manuscript of the defining paper was inspected around the absolute-value jerk equation, equilibrium derivation, Jacobian, and claimed Hopf conditions. It treats the origin with a one-sided smooth derivative and reports a classical Hopf condition at \(c=0.1\), despite the \(|x|\) nonsmoothness. The audited result instead proves actual Lyapunov instability of the origin for every \(c>0\), gives the exact nonzero-equilibrium existence range, and locates the unique genuine spectral crossing on the negative smooth branch. Fresh Resultary and exact-threshold searches found no prior correction.

## value

PASS

The correction changes the local bifurcation interpretation of the model: the reported origin Hopf cannot be a classical smooth Hopf because the actual origin is already unstable on one side for every positive parameter. The exact equilibrium existence diagram and the genuine negative-branch spectral crossing provide a mathematically appropriate replacement, making this a substantive source correction rather than a cosmetic recalculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
