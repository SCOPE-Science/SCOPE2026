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

The analytical proof reduces the geometric definition to one variable. For
\[
x(t)=(a+\cos t,\sin t)
\]
and
\[
z=\frac{\cos t+a}{1+a\cos t},
\]
the exact squared outer-asymmetry function is
\[
|f_{\mathrm{out}}(x(t))|^2
=
\frac{64a^2(1-a^2)^3}{\pi^2}
\frac{
(1-z^2)\bigl((1+a^2)^2-4a^2z^2\bigr)
}{
(1-a^2z^2)^4
}.
\]
With \(y=z^2\), differentiation produces the quadratic numerator
\[
N_a(y)
=
8a^4y^2
+
(-3a^6-18a^4+5a^2)y
+
4a^6+7a^4-2a^2-1.
\]
Its endpoint values determine the threshold, and its unique zero in \((0,1)\) above threshold is the stated \(y_*(a)\).

The family maximum uses two separate checks. On the lower branch,
\[
\frac{d}{da}\left[a(1+a^2)(1-a^2)^{3/2}\right]
=
-\sqrt{1-a^2}(2a^2+1)(3a^2-1),
\]
so the branch maximum is \(a=1/\sqrt3\). On the upper branch, the envelope derivative is strictly negative after reduction by \(N_a(y_*)=0\), so no later parameter can improve the value.

The embedded `verify.py` was replayed from its actual package path before packaging. It reconstructs \(b(x)\) and \(b(p(x))\) from line-circle intersections rather than from the reduced formula, scans the boundary densely for nine parameter values, checks the high-branch witness, and verifies the family maximum. It returned:

`VERIFY_OK translated-disk outer asymmetry phase diagram`

The dense scans are finite consistency checks. They are not used to justify the continuum maximization.
