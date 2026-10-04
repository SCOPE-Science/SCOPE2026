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

The proof has two exact ingredients.

First, for \(\Phi_D=\{x_i\}\cup\{Dx_i\}\), orthonormality of the normalized Hadamard rows gives \(S=I+D^2\). The canonical-dual criterion reduces scalability to existence of nonnegative squared coefficients whose weighted original-frame operator equals \(S^2\).

Second, Hadamard flatness gives the necessary diagonal equations
\[
A+Bt=n(1+t)^2
\]
for every distinct squared diagonal value \(t\). This immediately limits the spectrum to at most two points. For two values \(u,v\), exact elimination gives
\[
A=n(1-uv),\qquad B=n(2+u+v),
\]
so nonnegativity is equivalent to \(uv\le1\). The converse follows from the identity
\[
1-uv+(2+u+v)t=(1+t)^2
\]
for \(t\in\{u,v\}\).

The bundled `verify.py` checks these identities with exact rational arithmetic for representative interior and boundary pairs, and checks that the published three-level pattern \(\{1,4,9\}\) fails the affine interpolation test. These finite checks are supplementary and do not replace the arbitrary-parameter proof.

Limit: no computational check establishes originality, Hadamard existence, or any statement outside the real positive-diagonal family.
