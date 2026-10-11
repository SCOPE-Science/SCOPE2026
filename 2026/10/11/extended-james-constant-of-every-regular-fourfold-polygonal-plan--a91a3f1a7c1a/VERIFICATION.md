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
Put
\[
\alpha=\frac{\pi}{4n}.
\]
The upper proof uses only
\[
N_n(z)\le |z|_2\le \sec\alpha\,N_n(z)
\]
and
\[
|x+y|_2^2+|x-y|_2^2=2|x|_2^2+2|y|_2^2.
\]
These yield
\[
\min\{N_n(x+y),N_n(x-y)\}
\le \sqrt2\,\sec\alpha
\]
whenever
\[
N_n(x)^2+N_n(y)^2=2.
\]

For the sharp pair, take
\[
u=\sec\alpha\,e_\alpha,
\qquad
v=\sec\alpha\,e_{\alpha+\pi/2},
\qquad
t=\tan\alpha,
\]
and
\[
c=\sqrt{\frac{2}{1+t^2}},
\qquad
x=cu,
\qquad
y=ctv.
\]
Then
\[
N_n(x)^2+N_n(y)^2=2,
\]
while
\[
u+tv=\sec^2\alpha\,e_{2\alpha},
\qquad
u-tv=\sec^2\alpha\,e_0.
\]
Both directions are facet normals, so both chord norms equal
\[
\sqrt2\,\sec\alpha.
\]

`verify.py` reconstructs the finite-facet norm for the first forty values of \(n\), verifies the sharp construction, and checks deterministic admissible samples against the analytic bound. These computations are supplementary; the displayed inequalities prove the infinite theorem.

No independent audit or independent validation has been performed.
