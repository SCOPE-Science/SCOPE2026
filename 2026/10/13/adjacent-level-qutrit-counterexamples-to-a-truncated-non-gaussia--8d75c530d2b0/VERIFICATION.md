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

For pure dephasing, the source coefficient law reduces exactly to
\[
(\Phi_{1,t}(\rho))_{mn}=e^{-(m-n)^2t}\rho_{mn}.
\]
With \(q=e^{-t}\), the adjacent-level witness therefore has exact output eigenvalues \(0,(1-q)/2,(1+q)/2\).

The proof compares each conjectured candidate to the threshold
\[
T(q)=\left(\frac{1+q}{2}\right)^2+\frac12\left(\frac{1-q}{2}\right)^2.
\]
Any three-level state whose largest eigenvalue is at least \((1+q)/2\) must have purity at least \(T(q)\). The two exact differences used in the proof factor as
\[
T(q)-P_B(q)=\frac{(1-q)(9q^7+9q^6+9q^5+9q^4+9q^3+9q^2+21q-11)}{128},
\]
\[
T(q)-P_\kappa(q)=\frac{(1-q)(3q^7+3q^6+3q^5+3q^4+3q^3+3q^2-2)}{8}.
\]
Both are positive for \(3/4\le q<1\). The bundled checker verifies these polynomial identities and the endpoint rational inequalities with exact integer arithmetic.

No numerical optimization, finite enumeration, or asymptotic extrapolation is needed for the accepted claim. The proof does not establish the actual global minimizer and makes no assertion outside the stated parameter interval.
