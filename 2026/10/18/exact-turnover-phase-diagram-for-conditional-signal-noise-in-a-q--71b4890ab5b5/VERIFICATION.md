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
# Reproducibility and verification

The `verify.py` program is embedded alongside the result; the only external Python dependencies are specified in `requirements.txt`. Run `python verify.py` in the extracted directory. The following checks have been performed on the actual program: symbolic substitution into the \(2\times2\) continuous Lyapunov equation; symbolic Gaussian conditioning identity; exact derivative and peak substitutions; five exactly rational examples representing each turnover regime; rational polynomial endpoint signs isolating the stable positive reference equilibrium; and independent high-precision covariance residuals at \(r=0.5,1,256\) and at the calculated peak.

Observed output:

```
PASS: exact 2-by-2 Lyapunov solution and Schur complement
PASS: derivative factorization and exact peak formula
PASS: five exactly rational phase-regime examples
PASS: exact rational bracket for the large positive equilibrium
PASS: reference model, published variance samples, and unique optimum
r_star = 1.1228372734920565530552209718808556
V_max  = 2.0146489521771415415814346754183994
```

The analytic proof supplies the quantifiers over all admissible equilibrium parameters and \(r>0\). The program verifies algebraic identities and example evaluations; finite numerical checks alone would not prove the theorem. The theorem is about a stationary Gaussian approximation and does not certify rare-event exit asymptotics or exact stationary behavior of the finite-population process.
