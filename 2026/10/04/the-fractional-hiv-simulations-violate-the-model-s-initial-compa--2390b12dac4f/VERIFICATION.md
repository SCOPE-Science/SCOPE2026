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
The core checks are analytic.

For the source initial state and parameters, the bundled checker evaluates
\[
F(100,0,1)=
\left(
\frac{109}{1000},
\frac{27}{1000},
-2
\right),
\]
which is nonzero in every coordinate.

For the exponential history
\[
Q(t)=\int_0^t \Xi(s)e^{-k(t-s)}\,ds,
\]
the exact update is
\[
Q(t+h)-Q(t)
=
(e^{-kh}-1)Q(t)
+
\int_t^{t+h}e^{-k(t+h-s)}\Xi(s)\,ds.
\]
For the constant test input \(\Xi\equiv1\), this becomes
\[
\frac{e^{-kt}(1-e^{-kh})}{k},
\]
not \(h\).

The checker evaluates this identity at a representative fractional order only to replay the algebra numerically. The nonexistence and history-update conclusions do not depend on numerical experiments.
