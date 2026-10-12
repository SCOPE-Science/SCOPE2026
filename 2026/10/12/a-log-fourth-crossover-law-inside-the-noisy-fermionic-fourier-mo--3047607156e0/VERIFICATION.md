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
From \(p(N-B)T(N)^2=A\) and \(T(N)=\kappa(\log N)^2(1+o(1))\), any small-\(p\) solution diverges and satisfies \(pN(\log N)^4\to A/\kappa^2\). Taking logarithms gives \(\log N/\log(1/p)\to1\), proving the log-fourth normalization.

`artifacts/verify.py` solves the simplified exact model \(N(\log N)^4=C/p\) by bisection for decreasing \(p\). It is corroborative only; the proof is analytic.

Limit: no universality is claimed for the phenomenological model, its constants, or the interpretation of \(T(N)\).
