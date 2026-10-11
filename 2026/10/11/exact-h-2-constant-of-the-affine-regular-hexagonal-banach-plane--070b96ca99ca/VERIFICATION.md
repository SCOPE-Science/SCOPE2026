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
The verification has an exact finite part and an analytic continuum part.

`verify.py` fixes one unit-ball edge using the dihedral symmetry of
\[
N(s,t)=\max\{|s|,|t|,|s-t|\}.
\]
For every edge containing \(y\) and every ordered pair of active signed facets for \(N(x+y)\) and \(N(x-y)\), it solves the equality and intersects it with all dominance inequalities. The output is exactly eight nonempty line segments. The checker then generates the full twelve-element linear isometry group and verifies that every segment, after an isometry and optional interchange of \(x,y\), is one of the two canonical families used in the proof.

For those families, the checker symbolically confirms the crossing parameters and verifies the exact target inequality
\[
\frac{N(x+\lambda y)^2}{1+\lambda^2}\ge\frac{32}{45}.
\]
It checks the factorization
\[
45(u^2-u+2)^2-32(u^2-2u+5)
=(3u-1)(15u^3-25u^2+56u-20)
\]
and the derivative/discriminant facts used to establish its sign on \([0,1/3]\). It also verifies the explicit equality configuration.

No finite experiment is used as a substitute for the continuum proof. No independent audit or independent validation has been performed.
