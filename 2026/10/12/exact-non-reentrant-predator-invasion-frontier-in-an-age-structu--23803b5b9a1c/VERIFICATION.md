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

The proof is analytic. The numerical verifier only checks representative parameter choices.

For finite smooth maturation it evaluates
\[
\mathcal R_P(g,k)=
\int_0^\infty
\left[k\bar x\phi_A(\tau)+\tilde B(\tau)(1-e^{-\zeta\bar x})\right]
S_g(\tau)\,d\tau
\]
by trapezoidal quadrature and confirms strict decrease in \(g\), affine increase in \(k\), and increase of the derived \(k_c(g)\).

For the sharp model it independently evaluates the direct age integral and the transformed formula
\[
\mathcal R_P^\sharp=e^{-g\bar x\tau^*}Q(\tau^*,k)
\]
and checks agreement within the quadrature tolerance. It also checks that the resulting \(g_c(\tau^*;k)\) decreases on a representative interval where \(Q>1\).

The computation does not establish the infinite-dimensional stability theorem; that follows from the renewal characteristic equation and standard linearized-stability theory. No global extinction or persistence result is claimed.
