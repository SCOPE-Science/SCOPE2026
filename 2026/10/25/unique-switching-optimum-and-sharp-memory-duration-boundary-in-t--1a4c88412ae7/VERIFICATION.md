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

# Verification of the OU switching optimum

The analytic proof is in `RESULT.md`. Direct differential identity: \(M_0-(\gamma+c)M_1=\int_0^\infty t[h_\tau(t)-c]e^{-\gamma t}G_\tau(t)\,dt\). Its sign is governed by early and late time contributions separated at \(t_0=-\tau\log(1-c/D)\), whose ratio decreases strictly with the Laplace parameter. The strictly increasing likelihood ratio \(G_{\tau_2}/G_{\tau_1}\) for \(\tau_2>\tau_1\) proves the moment boundary's strict monotonicity. The limiting short-memory scaled derivative yields the unique positive zero in the theorem.

Reproduce finite numerical tests after installing `verification/requirements.txt` with `python verification/check_response.py` from the document root. Direct Gaussian OU correlation quadratures, integration-by-parts derivative comparisons, root brackets for \(D\in\{0.7,1,1.8\}\), and memory phase boundaries yielded **908 passing assertions** on the extracted candidate program. In the illustrative case \(D=1\), \(c=0.5\), the numerically bracketed critical memory is \(4.221462440171303\).

Numerical quadrature and sampled sign evaluations do not establish the universal quantifiers; they supplement the analytic arguments. The proof does not cover non-OU kernels, nonlinear solutions, or resource constraints different from an unrestricted nonnegative spin-switching rate. No independent mathematical audit was performed.
