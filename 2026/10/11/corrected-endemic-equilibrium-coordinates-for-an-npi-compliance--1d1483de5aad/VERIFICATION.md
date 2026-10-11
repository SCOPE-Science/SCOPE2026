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

The exact symbolic checker `verify.py` uses the compartment equations as printed in the source. It first substitutes the published endemic susceptible coordinate and verifies
\[
(1-\rho)\pi-(\lambda^*+\theta+\mu)S_n^{\mathrm{pub}}
=-\frac{(1-\rho)\pi\theta}{\lambda^*+\mu}.
\]
It then constructs the corrected coordinates conditional on a symbolic positive \(\lambda^*\) and verifies that all seven compartment residuals simplify identically to zero. Running `python3 verify.py` returns `VERIFY_OK`; the captured output is included as `verification_output.txt`.

This check does not impose or solve \(\lambda^*=\beta(I_n^*+\alpha I_y^*)/N^*\). Consequently it verifies the corrected stationary coordinate family conditional on \(\lambda^*\), not existence or uniqueness of an endemic equilibrium. It also does not verify any local/global stability theorem, center-manifold coefficient, or empirical fit.
