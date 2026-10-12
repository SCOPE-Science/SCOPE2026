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
# Exact reproducibility

Run the included `verification/verify.py` with Python 3 and SymPy. Expected final output is `VERIFY_OK`.

The checker builds the original six ODE right-hand sides, evaluates the true carcinoma-free equilibrium and the purported second equilibrium, and factors the exact Jacobian characteristic polynomial. It independently checks the signed constant coefficient in the infected-cell/virus quadratic, the exact apoptosis-dominance counterexample, and a stable comparison setting with \(\beta=5\).

The key general sign argument is analytic: with \(q,k,h,c>0\), the four scalar eigenvalues are negative; the remaining real quadratic has positive linear coefficient and constant coefficient \(kd_6(1-\mathcal R_{\mathrm{EBV}})\), which is positive below and negative above the exact boundary. A zero coefficient at equality creates a zero eigenvalue. The absence of a dysplasia-free steady state follows from incompatible equilibrium conditions \(\alpha N=0\) and \(\dot N=a_1>0\). The conditional dysplasia floor follows from an explicit linear normal-cell solution and asymptotically constant forcing in its stable scalar equation. No finite search is used as a proof of a universal inequality.
