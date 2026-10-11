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

The accepted theorem is analytic and does not rely on a finite experiment.

1. **Mean check.** For \(C(x)=\int_0^1\gamma(y)\gamma(y-x)\,dy\), periodic Fubini gives \(\int_0^1C(x)\,dx=(\int_0^1\gamma)^2\). Integrating the equation therefore yields \(\int_0^1\gamma^3=3\int_0^1\gamma\).
2. **Fourier check.** For real \(\gamma\), \(\widehat C(k)=\widehat\gamma(k)\widehat\gamma(-k)=\lvert\widehat\gamma(k)\rvert^2\). For \(k\ne0\), subtracting the squared mean changes no coefficient, so the nonlinear side has coefficient \(4\tau\lvert\widehat\gamma(k)\rvert^2\ge0\).
3. **Finite-support check.** If a nonconstant trigonometric-polynomial solution has maximal positive mode \(m\), then the covariance side and the linear term have zero coefficient at \(3m\). The cubic term has coefficient exactly \(\widehat\gamma(m)^3\), because the only three allowed frequencies summing to \(3m\) are \(m,m,m\). This contradicts the equation.
4. **Constant boundary.** The normalization \(\gamma(0)=1\) makes a constant candidate equal to \(1\), whose covariance defect is zero but whose nonlinear value is \(1\), so it is not a solution.

Limits: this verifies only the stated conditional theorem for exact continuous solutions of the displayed equation. It does not verify existence of such a solution, convergence of discrete dihedral systems, or accuracy of finite Fourier approximations.
