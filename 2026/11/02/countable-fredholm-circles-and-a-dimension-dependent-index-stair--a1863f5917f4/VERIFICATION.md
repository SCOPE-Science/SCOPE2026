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

The monomial-slice reduction uses the exact Drury–Arveson moments \(n!\beta!/(n+r)!\). Dividing by a constant on each slice identifies the normalized Hardy or weighted-Bergman monomial moments; the resulting operator has generalized Cesàro parameter \(r+1\).

The one-variable Fredholm-circle and subnormality results were checked in Len Miller's March 18, 2011 presentation (the theorem on page 9). The Hardy endpoint is the classical Cesàro case. The local index is also recovered independently from the recurrence for the adjoint eigenvectors, together with injectivity and known Fredholmness off the circle. The index sum is \(\sum_{r=0}^{k-1}\binom{r+d-2}{d-2}=\binom{k+d-2}{d-1}\), **not** the adjacent shifted binomial.

Running `python3 verification.py` returned `PASS: 17796 finite exact-arithmetic checks`. These are consistency checks of the weighted moments, counting identities, and sample circle regions; they cannot replace analytic Fredholm theorems or exhaustive mathematical proof. A separate mathematical audit has not been performed.
