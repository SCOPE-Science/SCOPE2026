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

The two decisive signs are certified with rational intervals.

For the sectional derivative,
\[
J'\!\left(\frac{23}{35}\right)
=
-\log 6+
\frac1{\sqrt2}
\log\!\left(
\frac{121+84\sqrt2}{23}
\right).
\]
The checker encloses \(\sqrt2\) by integer-square-root bounds, then encloses both logarithms through the exact identity
\[
\log x=
2\sum_{k\ge0}
\frac{z^{2k+1}}{2k+1},
\qquad
z=\frac{x-1}{x+1},
\]
after powers-of-two range reduction. The geometric tail bound is included explicitly. The resulting upper endpoint is negative.

For the full three-dimensional derivative,
\[
K'\!\left(\frac{33}{50}\right)
=
\frac\pi4+
\frac12\arctan\!\left(\frac{17}{50}\right)
+
\frac14
\log\!\left(
\frac{17^4}{33^2\cdot2789}
\right).
\]
The checker encloses the arctangent by its alternating series and \(\pi\) using Machin's formula
\[
\pi=
16\arctan\!\left(\frac15\right)
-
4\arctan\!\left(\frac1{239}\right).
\]
The resulting lower endpoint is positive.

The exact Pythagorean and rational simplifications at the two witness heights are also checked.

These certificates establish only the two local derivative signs. The passage from those signs to the two-point inequalities uses the strict-concavity theorem for the radial integral, as reconstructed in the proof.
