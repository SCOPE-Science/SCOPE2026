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

The key exact identity is
\[
\operatorname{area}(P_iP_{i+1}P_{i+2})
=
\frac12\ell_i\ell_{i+1}\sin\frac{2\pi}{n}.
\]
Thus equality of all vertex-triangle areas gives
\[
\ell_{i+2}=\ell_i.
\]

For even \(n\), the classified family has alternating side lengths \(a,b\). The analytic area certificate is
\[
A(P)
=
\frac{n}{16}
\left[
\cot\!\left(\frac{\pi}{n}\right)(a+b)^2
-
\tan\!\left(\frac{\pi}{n}\right)(a-b)^2
\right].
\]

`verify.py` directly constructs the polygons from their edge vectors, checks closure, checks equality of all consecutive triangle areas, computes area by the shoelace formula, and compares it to the closed form. It also checks the opposite-edge criterion underlying the central-symmetry parity statement.

The finite sweep is diagnostic only. The universal theorem is the exact recurrence, root-of-unity closure, and Fourier area computation in `RESULT.md`.
