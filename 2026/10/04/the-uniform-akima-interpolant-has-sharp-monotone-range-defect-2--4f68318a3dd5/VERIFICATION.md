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
The verification artifact uses exact rational arithmetic only.

It implements the original four-secant Akima derivative with the standard zero-weight average convention. Over an exhaustive integer test box it corroborates
\[
0\le m(a,b,c,d)\le\frac{a+b+c+d}{2}.
\]
The proof for all nonnegative real inputs is analytic in RESULT.md.

The script reconstructs the five active secants of the sharpness family, derives both interior derivatives exactly, and checks
\[
(A_1y)(2+2/3)=\frac{104\varepsilon-2}{27}
\]
for several rational \(\varepsilon\). It then verifies the exact strictly positive affine-transformed witness and the value \(-2/75\).

Finally, it checks the Hermite basis identities and the exact scalar extrema used in the proof. No floating-point log is used as a mathematical certificate.
