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

For side directions separated by an angle \(\phi\), the smallest enclosing parallelogram with those directions has area
\[
\frac{w_1w_2}{\sin\phi}.
\]

The published edge-contact lemma reduces a global minimum for a convex polygon to pairs of polygon-side directions.

For a regular \(n\)-gon of circumradius \(R\), the side-normal width is
\[
2R\cos(\pi/n)
\]
when \(n\) is even, and
\[
R(1+\cos(\pi/n))
=
2R\cos^2(\pi/(2n))
\]
when \(n\) is odd.

The maximum sine of an angle between two side directions is
\[
1,\qquad
\cos(\pi/n),\qquad
\cos(\pi/(2n))
\]
in the three cases
\[
n\equiv0\pmod4,\qquad
n\equiv2\pmod4,\qquad
n\ \text{odd},
\]
respectively. Substitution gives the theorem.

`verify.py` reconstructs the regular polygon from vertices, computes side-normal widths by support maxima and minima, enumerates all edge-direction pairs through \(n=300\), and checks the formula to floating-point tolerance.

The finite sweep is diagnostic only. The quantified proof is the exact edge-contact reduction plus the trigonometric calculation.
