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
The proof is independent of finite enumeration.

For the faithful semidirect product
\[
G=C_r\rtimes C_m,
\]
choose a complement action by \(u\in\mathbf F_r^\times\) of exact order \(m\). If the complement coordinate of an element is \(b\ne0\), then
\[
u^b\ne1,
\]
so the equation placing that element in a conjugate complement has a unique solution because
\[
1-u^b
\]
is invertible modulo \(r\).

This gives the critical structural facts:
\[
H_s\cap H_t=1
\quad(s\ne t),
\]
every non-kernel cyclic subgroup lies in exactly one \(H_t\), and the kernel \(C_r\) is a leaf. The graph decomposition and all counting formulas follow.

The packaged checker `artifacts/verify.py` directly constructs the groups
\[
(r,m)=(5,4),(7,6),(13,4),(13,6),(17,8),(31,10),
\]
enumerates every cyclic subgroup from multiplication, constructs all cover relations, and verifies the displayed vertex and edge formulas and the strict cyclic comparison.

It returns `VERIFY_OK`.

Finite computation is not used to prove the universal theorem.
