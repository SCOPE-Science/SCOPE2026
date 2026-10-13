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

The universal theorem is proved analytically in `RESULT.md`.

For \(p_\pm=(1\pm x)/2\), direct diagonal calculation gives
\[
D(\rho_{p_-}^{\otimes2},\rho_{p_+}^{\otimes2})=x
\]
and
\[
D(\mathcal P_2(\rho_{p_-}),\mathcal P_2(\rho_{p_+}))
=\frac{2x}{1+x^2}.
\]
CPTP contraction and the triangle inequality are the only channel-level ingredients in the lower bound.

The scalar lower-bound function is
\[
d(x)=\frac{x(1-x^2)}{2(1+x^2)}.
\]
Its derivative is
\[
d'(x)=\frac{1-4x^2-x^4}{2(1+x^2)^2},
\]
so the unique interior maximizer has \(x^2=\sqrt5-2\). The discard-one-copy channel has exact error \(d(|2p-1|)\), establishing matching achievability.

The bundled checker verifies these scalar identities and the displayed decimal value. It is not used to infer the universal CPTP statement.

Limit: no claim is made for postselected transformations, higher powers, noncommuting families, or higher dimensions.
