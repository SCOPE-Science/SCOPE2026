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

The density in Lemma 4.1 has the form
\[
\pi(z)=Qz^q(\sigma_{11}+\sigma_{12}z)^h\exp\!\left(\frac{C}{\sigma_{11}+\sigma_{12}z}\right),
\]
with \(q=-2+2r/\sigma_{11}^2\) and \(h=-2-2r/\sigma_{11}^2\). The proof checks the two endpoints separately.

At zero, all factors except \(z^q\) approach finite positive limits, so normalization requires and is locally equivalent to \(q>-1\), namely \(r>\sigma_{11}^2/2\). At equality, \(q=-1\), which gives logarithmic divergence.

At infinity, \(q+h=-4\) exactly and the exponential approaches one, so the density has an integrable \(z^{-4}\) tail. No further endpoint restriction is needed.

The packaged `verify.py` uses exact rational arithmetic to replay these exponent identities, the critical equality witness, and the paper's reported extinction-example values. It is a finite algebraic check supporting the analytic proof, not a substitute for the endpoint-integrability argument.

The verification does not classify the stochastic dynamics outside the corrected theorem domain and does not assess any independent validation channel.
