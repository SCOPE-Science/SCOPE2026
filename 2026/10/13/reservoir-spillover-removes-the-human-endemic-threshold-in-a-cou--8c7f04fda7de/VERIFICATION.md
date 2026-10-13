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

Let
\[
A_h=(\sigma_h+\mu_h)(\gamma_h+\mu_h+\alpha_h),
\qquad
\kappa=\beta_{bh}I_b^*>0.
\]
The source's human quadratic has coefficients
\[
a=\beta_hA_h,
\]
\[
b=(\kappa+\mu_h)A_h-\Pi_h\sigma_h\beta_h,
\]
and
\[
c=-\Pi_h\sigma_h\kappa.
\]
Using
\[
\mathcal R_0^h=
\frac{\beta_h\Pi_h\sigma_h}{\mu_hA_h}
\]
gives
\[
\frac{b}{A_h}=\kappa+\mu_h(1-\mathcal R_0^h),
\qquad
\frac{c}{A_h}=
-\frac{\mu_h\mathcal R_0^h}{\beta_h}\kappa.
\]
Since
\[
a>0,\qquad c<0,
\]
the root product is negative and exactly one root is positive.

The bundled checker evaluates this algebra at rational parameter choices in subcritical, critical, and supercritical human regimes. It confirms the positive root, positivity of the reconstructed human compartments, and the limits
\[
\frac{I_h^*(\kappa)}{\kappa}
\to
\frac{\mathcal R_0^h}{\beta_h(1-\mathcal R_0^h)}
\]
below threshold,
\[
\frac{I_h^*(\kappa)}{\sqrt{\kappa}}
\to
\frac{\sqrt{\mu_h}}{\beta_h}
\]
at threshold, and
\[
I_h^*(\kappa)
\to
\frac{\mu_h(\mathcal R_0^h-1)}{\beta_h}
\]
above threshold.

The existence proof itself is exact and does not depend on the finite numerical replay.
