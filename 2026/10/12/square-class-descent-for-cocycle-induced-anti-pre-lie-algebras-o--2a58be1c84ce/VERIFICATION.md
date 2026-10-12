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
The included `artifacts/verify.py` takes a generic symmetric matrix
\[
B=\begin{pmatrix}a&b\\b&c\end{pmatrix},\qquad ac-b^2\ne0,
\]
solves the defining relation
\[
B(x\circ y,z)=B(y,[x,z]),
\]
and independently verifies the exact four structure columns and all basis components of **both** anti-pre-Lie identities.

For \(q=3,5,7,11\), the checker exhaustively enumerates all nondegenerate symmetric forms over \(\mathbf F_q\). It projects forms modulo nonzero scalar, constructs the induced products, tests all structure identities, and checks every affine Lie algebra automorphism for each product and for each original form. The two orbit computations are separate: no finite-field orbit size is assumed in enumeration.

The reported outputs are:

- \(q=3\): \(18\) nonsingular forms, \(9\) products, \(5\) form orbits, product-orbit sizes \(3,3,3\).
- \(q=5\): \(100\) nonsingular forms, \(25\) products, \(9\) form orbits, product-orbit sizes \(5,10,10\).
- \(q=7\): \(294\) nonsingular forms, \(49\) products, \(13\) form orbits, product-orbit sizes \(7,21,21\).
- \(q=11\): \(1210\) nonsingular forms, \(121\) products, \(21\) form orbits, product-orbit sizes \(11,55,55\).

The checker finishes with `VERIFY_OK`. The run output is included as `artifacts/verify_output.txt`. The characteristic-free portion of the proof rests on explicit symbolic identities and orbit arguments, not finite enumeration. Characteristic two and all non-cocycle-induced products are outside the claim.
