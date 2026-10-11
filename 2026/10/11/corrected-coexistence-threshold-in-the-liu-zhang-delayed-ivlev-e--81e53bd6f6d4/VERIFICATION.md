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

The equilibrium calculation was replayed from the printed Section 4.1 parameters.

The positive-equilibrium criterion is
\[
\tau<\frac1s\log\!\left(\frac{\alpha Y(1-e^{-\beta K})}{s}\right),
\]
which evaluates to
\[
132.923341652608\ldots.
\]
The value agrees with the source's reported transcritical value \(132.9233\) to four decimal places.

The weaker real-logarithm condition is
\[
\tau<\frac1s\log\!\left(\frac{\alpha Y}{s}\right)
=250.531764704813\ldots.
\]
It does not ensure \(y^*>0\). At \(\tau=250\), the equilibrium formulas give \(x^*=45.4889011125\ldots\) and \(y^*=-409.077854460\ldots\).

The standalone checker reproduces these values and sign conditions. It is a reproducibility aid; the proof of the positivity threshold is the symbolic argument in `RESULT.md`.

Limit: no Hopf coefficient, periodic orbit, or chaotic trajectory was recomputed.
