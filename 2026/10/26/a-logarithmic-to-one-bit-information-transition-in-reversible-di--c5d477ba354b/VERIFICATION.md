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

# Verification record
The included independent script \(\texttt{check.py}\) builds transition-rate generators by enumerating all physical microstates in the relevant class. It compares a numerical stationary solution of the complete generator with the equilibrium detailed-balance distribution, checks generator residuals, and computes two-block mutual information from the joint microstate table. It tests 30 combinations of \(N\in\{4,5,6,7,8\}\), \(p\in\{0.18,0.5,0.76\}\), and absent/present diffusion; the odd sizes are auxiliary controls for the parity formula, while the theorem itself concerns even sizes. All comparisons pass with absolute discrepancy below \(2\times 10^{-10}\).

The script additionally evaluates \(H(K)-\tfrac12\log(\pi e m p(1-p))\) for \(p\in\{0.2,0.5,0.8\}\), \(m\in\{100,1000,10000\}\), tests convergence to \(\log 2\) for positive diffusion at fixed \(p\), and checks Bessel entropy limits with \(\lambda\in\{0.2,1,2.5,5\}\), \(m\in\{300,3000\}\). These are numerical validations of finite projections and asymptotic formulas. Their observed agreement does not itself establish infinite asymptotics or literature priority.

Independent audit has not been performed. The main mathematical proof is self-contained in \(\texttt{RESULT.md}\), with irreducibility, conditional independence, local Gaussian asymptotics and dominated-convergence arguments stated explicitly. Requires Python 3 with NumPy and SciPy; run \(\texttt{python check.py}\).
