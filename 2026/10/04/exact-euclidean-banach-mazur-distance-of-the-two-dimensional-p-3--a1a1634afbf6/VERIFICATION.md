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
The exact proof reduces the Euclidean pullback optimization to diagonal forms by averaging over coordinate sign symmetries. For
\[
F_r(t)=\frac{\left((8+(1+t)^3)/8\right)^{2/3}}{1+r t^2},
\]
the critical-point map is
\[
R(t)=\frac{(1+t)^2}{t((1+t)^2+8)}.
\]
Its derivative is strictly negative for \(t>0\) because
\[
t^3+3t^2-5t+9=t(t-1)^2+5\left(t-\frac35\right)^2+\frac{36}{5}>0.
\]
Thus every \(F_r\) has one interior maximum. Equalizing the two endpoint values gives \(r_0=3^{-4/3}\), and the two monotonic lower-bound arguments on \(r\le r_0\) and \(r\ge r_0\) prove global optimality.

The bundled `verify.py` is a numerical replay only. It bisects the equation
\[
3^{4/3}(1+\tau)^2=\tau((1+\tau)^2+8)
\]
on a certified sign-changing interval, checks the endpoint equalization, and evaluates the final formula. The numerical replay is not used to justify uniqueness or global optimality; those are established analytically above.
