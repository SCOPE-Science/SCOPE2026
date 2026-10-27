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

The identity \(\widehat g_m(\xi)=(\sin(\pi\xi)/(\pi\xi))^m\), the Poisson alias representation and the explicit differentiation formulas provide independent analytic routes to check the normalizations. The complete argument bounds all aliases outside the two nearest half-integer modes and confines the entire sublevel set to the frequency scale \(1/m\).

Execute `python CHECKER.py` in this directory with Python 3. The checker uses only the standard library; its recorded output is in `CHECKER_OUTPUT.txt`. It evaluates spline values via the truncated-power formula and also via a Fourier series, checks compact-scale profile convergence, tests exact positive derivative sums, and approximates scaled sublevel areas. The finite quadratures are not exhaustive proofs and no independent mathematical audit was performed.
