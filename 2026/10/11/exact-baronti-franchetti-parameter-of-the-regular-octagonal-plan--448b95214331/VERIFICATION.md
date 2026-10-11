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

Put
\[
a=\sqrt2-1,\qquad s=\sqrt{1+a^2}=\sqrt{4-2\sqrt2}.
\]
For an isosceles pair with coordinate ratio \(r\in[0,1]\),
\[
h(r)=
\begin{cases}
\displaystyle\frac{1+r^2}{\sqrt2(1+ar)},&0\le r\le a,\\[3mm]
\displaystyle\frac{1+r^2}{(1+r)(1+ar)},&a\le r\le1.
\end{cases}
\]
The first derivative vanishes at \(r_0=a/(1+s)\), the second at \(r_1=s-a\), and both branch minima equal
\[
L=\frac{\sqrt2}{1+s}.
\]
The explicit dual unit functionals displayed in the proof attain \(h(r)\) on both members of each isosceles pair.

For arbitrary unit \(w,z\), write
\[
z=\alpha\,\epsilon k+\beta\,\sigma w,\qquad \alpha,\beta\ge0,
\]
in one of the four cones determined by \(w\) and its quarter-turn \(k\). The triangle inequality gives \(\alpha+\beta\ge1\), so an isosceles-pair functional gives \(|f(w)|\ge L\) and \(|f(z)|\ge L\). The pair at \(r=r_0\) attains \(L\).

The included `algebra_check.py` was executed successfully and verifies all critical radical and derivative identities by exact symbolic arithmetic. No numerical optimization is used as proof.
