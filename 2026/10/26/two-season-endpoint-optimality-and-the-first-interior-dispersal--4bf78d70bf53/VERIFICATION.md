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

# Computational verification and boundaries

The complete `checker.py` and its `verification_certificate.json` accompany this result. `python checker.py` computes symbolic matrix equalities with exact rational inputs, checking the identity
\[
D_1^{1/2}M(d)D_2M(d)D_1^{1/2}
=\bigl(D_2^{1/2}M(d)D_1^{1/2}\bigr)^\mathsf{T}
 \bigl(D_2^{1/2}M(d)D_1^{1/2}\bigr)
\]
for 28 finite combinations and checks the explicit eigenvalues of the three-season counterexample. The certificate contains input-independent exact rational outputs; its contents are reproducible by executing the bundled script.

The proof for all dimensions is mathematical, not a conclusion from those examples. A matrix need not be irreducible, and no spectral-gap hypothesis is invoked. Equality can occur throughout an interval in homogeneous environments; the result only guarantees existence of an optimal endpoint. For the stated two-site cost switch, a separate strict norm-triangle argument excludes interior ties. The three-season witness guarantees only that a maximizer is interior, not where every maximizer lies.

No independent audit or external certification has been performed.
