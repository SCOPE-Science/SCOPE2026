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

The standalone `verify.py` uses exact integer arithmetic and two distinct constructions of the forced-presence coefficient series. Run `python3 verify.py` in the directory containing this document and `verify.py`; no third-party packages or external data are required.

Recorded execution: `VERIFY_OK exact_coefficients=2394 n_max=170 m_max=13 base_overpartitions=verified identity=verified monotone=verified`. The program also reports three finite-size comparisons with the asymptotic survival; these are exploratory checks, not a convergence certificate.

The unrestricted theorem is proved analytically through the Boltzmann conditioning identity and a Gaussian local-limit Fourier bound, including a uniform global tail bound. Code can check the exact combinatorial identity but not the infinite limit or all positive moments. All mathematical verification in this package is self-review only; no independent audit was performed.
