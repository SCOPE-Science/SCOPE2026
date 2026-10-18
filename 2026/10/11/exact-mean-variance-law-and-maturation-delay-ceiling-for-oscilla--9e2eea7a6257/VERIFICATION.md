---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-14.md",
      "INDEPENDENT_AUDIT_2026-10-14.json"
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

For any positive T-periodic solution, integrate delayed predator recruitment over one period; time-shift invariance gives E(Gp)=e^{beta tau} pbar. Integrate the logistic prey equation to get pbar=sigma e^{-beta tau}[nbar(1−nbar/kappa)−Var(n)/kappa]. Nonconstant prey follows from strict monotonicity of fixed-n predation in p; then Var(n)>0 yields 0<nbar<kappa and strict pbar<sigma*kappa*exp(−beta*tau)/4. Saturation 0<G<1/h gives h exp(beta tau)<1 as a necessary condition. Checked algebra and saturation independently, and directly checked actual 2024 source delayed equations; the shift does not require tau/T rational.

## originality

PASS

PASS for the **surviving central exact period-mean–variance law and strict amplitude-sensitive mean-predator ceiling**, not for novelty of the handling-time no-cycle threshold. The published same-model global-extinction theorem definitively covers the latter by a stronger all-history result; this is explicitly acknowledged and the no-cycle corollary is not counted as original. The 2024 primary provides equilibria/Hopf statements, not the exact finite-amplitude mean law in inspected material. Different Bai–Zhang delay model has another period-mean law that does not imply this exact formula. This is a best-of-knowledge originality judgment with clear partial coverage.

## value

PASS

The exact mean–variance law quantifies a real finite-amplitude predator-density deficit for positive delayed cooperation cycles, including an explicit maturation survival factor and uniform ceiling independent of cooperation strength. It is a natural ecological recurrence statistic beyond local Hopf/equilibrium arguments and remains mathematically meaningful even though the no-cycle parameter obstruction is already covered by stronger global extinction work.

The dated certificate retains the supplied scientific assessment, sources and limitations.
