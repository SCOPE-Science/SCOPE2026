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

The source gives
\[
\phi_1(t)
=
\frac{1+4\cos(2t)}{48\pi}
\]
and
\[
\rho_{\lambda,N}(t)
=
\sec(t-h_{\lambda,N}(t)).
\]
Writing \(\delta=\lambda-\lambda_0\),
\[
t-h_{\lambda,N}(t)
=
\frac{\pi}{3}-\delta\phi_1(t)+O_N(\delta^2).
\]
Since
\[
(\sec x)'|_{x=\pi/3}=2\sqrt3,
\]
the exact first variation is
\[
-\frac{\sqrt3}{24\pi}\bigl(1+4\cos(2t)\bigr).
\]

The bundled checker symbolically differentiates the radial expression, verifies this identity, evaluates its maximum and minimum, and checks that their difference is exactly
\[
\frac{\sqrt3}{3\pi}.
\]
It also checks the displayed decimal value.

The computational replay is not the proof of the passage from pointwise variation to \(R\) and \(r\). That step uses the uniform \(O_N(\delta^2)\) remainder on the compact angular domain. For a family
\[
f_\delta(t)=c+\delta g(t)+O(\delta^2)
\]
uniformly in \(t\), the global maximum and minimum equal
\[
c+\delta\max g+O(\delta^2),
\qquad
c+\delta\min g+O(\delta^2)
\]
for \(\delta>0\), with the roles exchanged for \(\delta<0\).

Limits: no infinite-\(N\) convergence, actual counterexample, or second-order asymptotic is verified or claimed.
