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

The packaged `verify.py` was executed directly from its packaged path with the system Python interpreter.

It checks the monotone-function recurrence against the exact totals \(3,6,20,168,7581\) for one through five variables. After imposing the simple-game boundary conditions, it verifies \(1,4,18,166,7579\) games, respectively. For every such game it computes normalized Banzhaf and Shapley–Shubik indices with exact rational arithmetic and checks equality of all pairwise weak-order signs.

It then constructs the six-player game from the four stated minimal winning coalitions and verifies the exact vectors
\[
\left(\frac{1}{24},\frac{1}{6},\frac{1}{6},\frac{1}{24},\frac{1}{12},\frac{1}{2}\right)
\]
and
\[
\left(\frac{1}{30},\frac{1}{6},\frac{1}{6},\frac{1}{20},\frac{1}{12},\frac{1}{2}\right).
\]
The replay terminates with `VERIFY_OK`. No floating-point comparisons are used.
