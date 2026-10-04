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

The source gives the characteristic factorization at \(P_4\) as a one-dimensional factor with eigenvalue \(r_1>0\) and a quadratic factor \(\lambda^2-B_1\lambda+B_2\), together with \(B_1<0\) and \(B_2>0\).

For the quadratic roots \(\lambda_2,\lambda_3\), Vieta gives \(\lambda_2+\lambda_3=B_1<0\) and \(\lambda_2\lambda_3=B_2>0\). If the roots are real, both are negative; if they are nonreal, both have real part \(B_1/2<0\). Thus the full Jacobian has one eigenvalue with positive real part and two with negative real parts, with no zero eigenvalue.

The standard saddle-node condition was checked against Kuznetsov's definition: a critical saddle-node equilibrium in an autonomous ODE has a zero eigenvalue. Hence the source spectrum is incompatible with the label “saddle-node” under the same displayed assumptions. No numerical approximation is used in this verification.
