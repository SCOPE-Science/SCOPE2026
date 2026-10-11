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

The proof was checked symbolically from the exact Hilbert-valued identity
\[
\int_{\mathbb T}\|x+zy\|^{2h}\,dm(z)
=
\sum_{k=0}^{\lfloor h/2\rfloor}
\frac{h!}{(h-2k)!(k!)^2}
(\|x\|^2+\|y\|^2)^{h-2k}|\langle x,y\rangle|^{2k}.
\]
The bound \(|\langle x,y\rangle|\le(\|x\|^2+\|y\|^2)/2\), positivity of every coefficient, and the scalar identity \(\int_{\mathbb T}|1+z|^{2h}dm=\binom{2h}{h}\) give the exact one-coordinate factor. Hilbert direct-sum induction supplies all dimensions. Equality was separately checked from the strict positivity of the \(k=1\) coefficient for every \(h\ge2\).

The standalone `verify.py` performs exact integer checks of the central-binomial identity for \(2\le h\le10\), exact convolution-moment equality for product coefficients, and deterministic integer-coefficient inequality checks for \(1\le d\le4\), \(2\le h\le5\). A replay returned:

`VERIFY_OK local_identities=9 exact_cases=335 d=1..4 h=2..5`

The finite computations are only corroborative. They do not establish the theorem for arbitrary \(d\) or \(h\); that scope is supplied by the analytic proof. Independent audit and independent validation have not been performed.
