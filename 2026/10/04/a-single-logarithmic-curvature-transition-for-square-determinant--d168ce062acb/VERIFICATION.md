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
The proof was replayed from the published product formula using exact integer and rational arithmetic.

`verify_determinantal_curvature.py` performs three checks. First, for every \(2\le n\le40\), it computes every \(D_{n,r}\) directly from the factorial product and verifies the closed formula for \(D_{n,r+1}/D_{n,r}\) and for \(D_{n,r-1}D_{n,r+1}/D_{n,r}^2\). Second, it checks through \(n=1000\) that the sign of the curvature quotient agrees exactly with the comparison \(17(n-r)^2\gtreqless n^2+4\) and that the sign changes at most once. Third, it searches the exact Pell equality in the finite window \(n-r<10000\), finding \((8,2,6)\), \((536,130,406)\), and \((35368,8578,26790)\).

The checker output was `VERIFY_OK`, with 1521 direct degree/ratio checks. These finite checks do not establish the infinite theorem; they verify the implementation and sample the symbolic identities. The infinite result follows from the displayed cancellation proof in `RESULT.md`.

Limits: no complete parametrization of the negative Pell solutions is certified here, and no claim is made for rectangular, symmetric, or skew-symmetric determinantal degree sequences.
