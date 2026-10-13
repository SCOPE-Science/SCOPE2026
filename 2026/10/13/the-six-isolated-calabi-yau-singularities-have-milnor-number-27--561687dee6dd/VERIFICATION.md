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

The bundled checker uses only the Python standard library.

It reconstructs
\[
q(x,y)=xy(x+25y)(x+9y)
=x^3y+34x^2y^2+225xy^3
\]
and its cubic partial derivatives. It verifies that \(q_x\) and \(q_y\) have no common projective root by an exact Euclidean/resultant-style calculation on the affine chart together with the two coordinate points. Therefore they form a homogeneous complete intersection of degrees \(3\) and \(3\), whose quotient length is \(9\).

For the weighted initial form
\[
f_4=\lambda z^2+\mu s^4-q(x,y)
\]
with \(\lambda\mu\ne0\), the Jacobian quotient factors as the length-\(1\) \(z\)-factor, the length-\(3\) \(s\)-factor, and the length-\(9\) binary-quartic factor. The resulting Milnor-algebra dimension is \(27\).

The checker also expands the exact local equation printed by Burek over \(v=0\),
\[
(z-1-s^4)(z^2-4s^4)-q(x,y),
\]
and verifies that its weighted-degree-\(4\) part is
\[
-z^2+4s^4-q(x,y),
\]
while every remaining monomial has weighted degree greater than \(4\) for weights \((1,1,1,2)\).

The semiquasihomogeneous invariance of Milnor number and Milnor's bouquet theorem are mathematical inputs from the cited literature and are not replaced by finite computation. The result is local; no global smoothing is claimed.
