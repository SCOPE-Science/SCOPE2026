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
The derivation was checked directly against the source equations for the prey dynamics, renewal boundary, predator birth and death functions, and smooth maturation indicators. At \(u=0\), the prey equilibrium is \(\bar x=r/a\); derivatives of predator coefficients with respect to prey multiply the zero equilibrium predator density, so the predator linear block is autonomous at first order. Its exponential modes give the stated Euler--Lotka equation.

For \(\mathcal R_P(g)<1\), any characteristic root with \(\operatorname{Re}\lambda\ge0\) would imply
\[
1\le\int_0^\infty K(\tau)e^{-g\bar xA(\tau)}e^{-\operatorname{Re}(\lambda)\tau}\,d\tau\le\mathcal R_P(g)<1,
\]
which is impossible. For the source's smooth juvenile indicator, \(A(\tau)>0\) for \(\tau>0\), so differentiation under the integral gives strict decrease of \(\mathcal R_P\), and dominated convergence gives \(\mathcal R_P(g)\to0\).

`verify.py` stress-tests the formulas on an admissible finite-lifespan instance of the same functional forms. It checks the prey linear derivative, strict decrease of the renewal reproduction integral, the derivative formula, and a unique numerical crossing of \(\mathcal R_P(g)=1\). The script is finite evidence only; the quantified proof is analytic. No independent audit has been performed.
