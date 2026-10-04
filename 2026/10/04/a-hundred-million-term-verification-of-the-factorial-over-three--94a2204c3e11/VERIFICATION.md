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

The finite claim is checked by `artifacts/verify.cpp` using exact integer arithmetic. For \(X_n=n!/3\), the program maintains \(E_q=v_q(X_n)\) and \(T_q=v_q(	au(X_n))\), with
\[
T_q=\sum_p v_q(E_p+1).
\]
It updates the complete state for every successive \(n\) and fails immediately if any \(T_q>E_q\). Thus a successful traversal is exactly equivalent to \(	au(X_n)\mid X_n\) at every checked \(n\).

The recorded full-range run is:

`VERIFY_OK limit=100000000 checks=99999998 direct_samples=1002`

The 1002 direct samples reconstruct factorial prime exponents from Legendre's formula rather than trusting the incremental state. They are corroborative cross-checks; exhaustive coverage of the interval comes from the main loop.

Limits: this verifies only \(3\le n\le10^8\). It is not a proof for larger \(n\), and independent audit has not been performed.
