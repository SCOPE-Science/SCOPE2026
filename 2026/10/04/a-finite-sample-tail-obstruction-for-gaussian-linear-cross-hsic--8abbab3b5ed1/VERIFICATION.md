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

The proof was checked at four levels.

First, direct algebra from the published linear-kernel definition gives
\[
T_n=\operatorname{sgn}(f_2)\frac{(n-2)C}{\sqrt{n(n-1)Q}}.
\]
The accompanying checker compares the source-form jackknife calculation with this reduction on exact rational inputs.

Second, for \(n=3\), the centered Gaussian directions live on a circle. Expansion in the displayed orthonormal basis gives \(u\cdot v=\cos(A-B)\) and \(\|P(u\circ v)\|^2=1/6\), yielding the arcsine law.

Third, the \(n=4\) denominator zero is regular. The checker performs exact rational elimination and verifies a \(3\times3\) derivative minor equal to \(-15/16\) before nonzero normalization factors.

Fourth, for \(n\ge5\), the proof of regularity is symbolic: an annihilator would force at least five distinct coordinates to be roots of a quartic, hence the annihilator is zero. The submersion theorem then gives a local \((n-1)\)-dimensional transverse ball, which proves the polynomial lower-tail bound and moment divergence.

Finite numerical checks do not certify the infinite statements; those follow from the analytic submersion argument. No matching upper tail, exact constant, or below-threshold moment finiteness is claimed.
