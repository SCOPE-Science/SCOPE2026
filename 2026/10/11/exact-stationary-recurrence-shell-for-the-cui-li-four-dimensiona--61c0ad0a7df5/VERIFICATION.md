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

The bundled `verify.py` reconstructs the four polynomial vector-field components and the observable
\[
Q=\frac12(u^2-ew^2)
\]
using an exact multivariate-polynomial implementation with rational coefficients from the Python standard library. It differentiates \(Q\) and checks exactly that
\[
LQ=-au^2+auv+bew^2.
\]
It also checks that eliminating \(\int uv\,d\mu\) with \(\int\dot w\,d\mu=0\) gives the polynomial balance equivalent to the displayed completed-square shell, and verifies the source-parameter fractions \(a/(2e)=3/2\), \((a/(2e))^2=9/4\), and \(a/(be)=3/43\).

The equality classification is analytic rather than experimental. Once the shell equality forces \(u=0\) in \(L^2(\mu)\), stationarity of \(w^2\), \(uv\), and \(vp\) successively forces \(w=v=p=0\). This uses only \(a,b,m>0\) and compactly supported invariance, which makes the generator identities integrable.

Limits: the checks do not establish the existence or boundedness of a non-equilibrium attractor, do not certify any numerical Lyapunov spectrum, and do not turn finite trajectories into invariant measures. Literature coverage retains the residual risks stated in `AUDIT.json`.
