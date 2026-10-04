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

For
\[
D=\{d_1,\ldots,d_m\}\ne\varnothing,
\]
the decisive test is
\[
f_m^N(\{d_1\},\ldots,\{d_m\};D).
\]
Any witnessing neighbourhood lies inside \(D\) and meets every singleton \(\{d_i\}\), so it equals \(D\). The empty neighbourhood is tested separately by
\[
f_0^N(;\varnothing).
\]

The lower-bound frames differ only by whether the full carrier \(X\) belongs to one local neighbourhood family. A test with at most \(n-1\) instance sets can replace \(X\) by a proper transversal containing one selected point from each nonempty instance set. At arity \(n\), the \(n\) singleton instance sets have only the full carrier as a witness.

The bundled `verify.py` exhaustively checks the reconstruction identity for every local neighbourhood family through \(n=4\), and checks every lower-arity argument tuple for the sharpness pair through \(n=4\). It prints `VERIFY_OK`.

## Limits

The computation is corroborative. The proof establishes the theorem for every finite \(n\). No smaller-cutoff claim is made for restricted frame classes.
