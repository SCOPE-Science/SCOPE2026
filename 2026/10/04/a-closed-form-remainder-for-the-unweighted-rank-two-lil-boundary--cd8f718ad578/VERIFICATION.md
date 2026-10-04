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
The analytic check is finite and explicit. For \(0<\varepsilon<1\), differentiate
\[
H_\varepsilon(t)=2\sqrt t-\frac{2}{1+\varepsilon}t^{(1+\varepsilon)/2}.
\]
Then
\[
H_\varepsilon''(t)=\frac12t^{-3/2}\left((1-\varepsilon)t^{\varepsilon/2}-1\right)<0,
\]
so the symmetric row sum is maximized at \(1/2\). Evaluating there gives the claimed \(\delta(\varepsilon)\). Schur's test and the variational principle then give the operator and eigenvalue bounds.

The bundled `verify.py` re-evaluates the \(\varepsilon=0.02\) numerical interval using the source-certified endpoints and checks the displayed derivative signs on a diagnostic grid. The grid is not an exhaustive proof and is not used to establish concavity; the displayed symbolic derivative does that.

Unproved limit: the enclosure is not asserted to be sharp, and no second-order coefficient is certified.
