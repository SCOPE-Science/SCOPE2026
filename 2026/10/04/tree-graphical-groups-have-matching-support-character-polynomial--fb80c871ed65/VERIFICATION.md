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

The packaged checker `artifacts/verify.py` verifies four distinct tree shapes over
\[
\mathbf F_3
\quad\text{and}\quad
\mathbf F_5.
\]
For every edge assignment it forms the alternating weighted adjacency matrix and checks
\[
\operatorname{rank}B=2\nu(\operatorname{supp}B).
\]

It separately enumerates all edge supports and evaluates
\[
\sum_S(q-1)^{|S|}z^{\nu(S)},
\]
then compares that polynomial with the two-state rooted recursion.

Finally it verifies
\[
\sum_i
q^{n-2i}[z^i]\mathcal R_T(q,z)\,q^{2i}
=
q^{n+|E(T)|},
\]
the degree-squared identity for the graphical group.

The checker returns `VERIFY_OK`.

Finite computation is not used to prove the infinite family.
