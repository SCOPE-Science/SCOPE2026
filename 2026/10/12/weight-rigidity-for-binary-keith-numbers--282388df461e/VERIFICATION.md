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

The proof does not depend on computation.

The packaged checker performs an independent finite comparison through all binary integers below
\[
2^{18}.
\]
For every bit length \(2\le n\le18\), it directly tests the Keith recurrence for every \(n\)-bit integer. Independently, for every weight \(2\le w\le n\), it computes
\[
c=\lceil\log_2w\rceil,\qquad L=2^c,
\]
divides
\[
2^{n-c}w
\]
by \(L+1\), and keeps the unique quotient-remainder candidate exactly when the remainder is smaller than \(L\) and the two Hamming weights sum to \(w\). It then adds the power \(2^{n-1}\).

At every tested bit length, the direct set and predicted set are required to agree exactly. The checker also verifies the known initial non-power values appearing in the public binary sequence.

These computations are corroborative only. The infinite theorem is established by the recurrence and quotient-remainder proof in `RESULT.md`.
