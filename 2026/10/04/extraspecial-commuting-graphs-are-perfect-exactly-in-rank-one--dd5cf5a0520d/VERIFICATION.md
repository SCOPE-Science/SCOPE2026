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
The proof is symbolic.

For rank one, the checker constructs the noncentral element-level blow-up of the symplectic orthogonality graph for
\[
p=2,3,5,7.
\]
It verifies that there are exactly
\[
p+1
\]
connected components and that every component is a clique of order
\[
p(p-1).
\]

For rank two, the checker uses coordinates
\[
(e_1,f_1,e_2,f_2)
\]
and evaluates all ten pairings among
\[
e_1,\quad e_2,\quad f_1,\quad f_1+f_2,\quad e_1-e_2+f_2.
\]
For every tested prime, the zero pairings are exactly
\[
12,\ 23,\ 34,\ 45,\ 51,
\]
so the induced graph is \(C_5\).

The script `artifacts/verify.py` returns `VERIFY_OK`.

Finite computation is not used to prove the result for arbitrary primes or ranks.
