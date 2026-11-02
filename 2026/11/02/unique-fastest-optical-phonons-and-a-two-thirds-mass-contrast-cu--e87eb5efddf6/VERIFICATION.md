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

The mass-weighted two-by-two Hermitian Bloch matrix yields \(\omega_+^2=\Omega^2(1+u)\) with \(u=\sqrt{1-(1-c^2)\sin^2(q/2)}\). Differentiation and elimination of \(q\) produce the exact scalar maximization function \(F_c(u)=(1-u)(1-c^2/u^2)\) on \(c\leq u\leq1\). A strictly decreasing numerator of \(F_c'(u)\) has opposite endpoint signs, so its root and the maximum are unique. The sound speed is derived independently as the \(q\downarrow0\) acoustic slope, and the normalized strict bound follows by comparison with the equal-mass limit. Substitution \(u_c=c^{2/3}y_c\) in the cubic proves the fractional-power asymptotics. The supplied `check.py` uses Python 3, NumPy and SciPy and provides 523 numerical diagnostics. This diagnostic code does not independently prove global uniqueness or novelty; no independent audit is claimed.
