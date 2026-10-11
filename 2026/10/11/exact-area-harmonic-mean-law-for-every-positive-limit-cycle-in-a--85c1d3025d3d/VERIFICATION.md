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

The finding is proved directly from the printed two-dimensional vector field. No finite simulation is used as evidence for an infinite statement.

## Exact algebraic check
With
\[
B(x,y)=\frac{1}{xy},
\]
the first weighted component has \(x\)-derivative \(-b/y\), while the second weighted component is
\[
BF_2=-\frac{n}{x}+\varepsilon(c+ey)
\]
and therefore has \(y\)-derivative \(\varepsilon e\). Thus
\[
\nabla\!\cdot(BF)=\varepsilon e-\frac{b}{y}.
\]

## Global step
For a positive periodic orbit, ODE uniqueness makes the orbit a simple closed curve. Its interior is contained in the positive quadrant, where \(B\) is smooth. Since \(BF\) is tangent on the orbit, its normal flux is zero. Green's theorem therefore gives
\[
0=\iint_D\left(\varepsilon e-\frac{b}{y}\right)dx\,dy,
\]
which is equivalent to the claimed harmonic-mean identity.

Because the integrand has exactly one zero, at \(y=b/(\varepsilon e)\), a zero area integral is impossible if the entire Jordan domain lies on only one side of that line. Hence every cycle strictly straddles it.

## Source cross-check
The publisher full text independently prints the equilibrium trace
\[
\operatorname{tr}J=\bar x(-b+e\varepsilon\bar y),
\]
so a positive equilibrium has zero trace exactly at the same level \(\bar y=b/(\varepsilon e)\).

## Example arithmetic
For the source values \(b=0.9\) and \(\varepsilon=0.4\), the threshold is \(2.25\) at \(e=1\) and \(0.45\) at \(e=5\). These numerical values are illustrative only.

## Limits
The verification does not establish that a periodic orbit exists, nor its uniqueness, stability, period, or shape. It does not classify nonperiodic recurrent sets. The proof applies only to nonconstant periodic orbits contained in the positive quadrant with \(e>0\).
