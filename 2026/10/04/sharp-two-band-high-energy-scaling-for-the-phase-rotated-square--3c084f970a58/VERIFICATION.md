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

The proof uses the exact Bloch secular coefficients published in arXiv:2108.04708v1. The standalone `verify.py` reconstructs the exact quotient \(Q(k)\), then solves \(Q(k)=\pm2\) near each predicted local edge by bisection. No external packages are required.

The replay checks three representative interior phase values and three increasing band indices for each. For every case it verifies that all four exact edge equations are bracketed and solved, that the energy-edge errors decrease at the expected second-order rate, and that the central point \(k=N_n\) is nonspectral because the exact secular polynomial equals \(4\sin(2\mu)N_n^2\ne0\).

The numerical checks are finite and do not establish the asymptotic theorem by themselves. The infinite-index conclusion comes from the uniform expansion of the exact quotient on compact sets away from \(x=0\), strict monotonicity of the limiting function on both half-lines, and simplicity of all four boundary roots. Endpoint regimes \(\mu=0\) and \(\mu=\pi/2\) are not tested or claimed.
