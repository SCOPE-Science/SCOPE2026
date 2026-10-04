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

The proof was checked at three levels.

First, the scalar memory equation \(\dot v+v=y^2\) was solved on a bounded complete trajectory, yielding \(v(t)=\int_{-\infty}^{t}e^{-(t-s)}y(s)^2\,ds\). This establishes \(v\ge0\) without numerical approximation. The contradiction at \(v=0\) uses only \(d>0\) and \(k\ne0\).

Second, the stationary identities were reconstructed from the generator. The symbolic checker verifies
\[
L(y^2/2)+L(z^2/2)-k y=c y^2\tanh v-dz^2
\]
and
\[
L(v^2/2)=vy^2-v^2.
\]
Together with \(L u=gy\), these identities imply the stated moment law for every compactly supported invariant measure.

Third, the checker substitutes the source parameters \(c=7\), \(d=31\), \(g=1/20\), and \(k=7\) and confirms the specialized coefficients exactly.

The verification does not certify existence of a compact attractor, does not infer chaos from the identities, and does not replace the analytic bounded-complete-trajectory argument with finite-time computation.
