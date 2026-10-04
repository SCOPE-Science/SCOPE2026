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
The universal argument rests on four exact checks.

First, every subgroup is either above the normal kernel \(A=C_r\) or disjoint from it. The first kind is the inverse image of a subgroup of \(C_{pq}\); the second kind injects into \(C_{pq}\) and is cyclic of order \(1\), \(p\), \(q\), or \(pq\).

Second, fixed-point-freeness implies
\[
N_G(P)=N_G(Q)=N_G(B)=B,
\]
so the order-\(p\), order-\(q\), and order-\(pq\) cyclic subgroups each form a conjugacy class of size \(r\).

Third, the cyclic-subgroup permuting-partner counts are exactly
\[
3r+2
\]
for \(1\) and \(C_r\), and exactly \(5\) for every other cyclic subgroup. The latter five partners are \(1\), \(C_r\), and the three cyclic subgroups inside the unique complement containing the subgroup.

Fourth, substituting these counts into the definition of \(\operatorname{csd}(H,G)\) gives the five formulas. Their successive differences factor as
\[
\frac{3(r-1)}{2L},\quad
\frac{3(r-1)}{4L},\quad
\frac{3(r-1)(r-6)}{4(r+2)L},\quad
\frac{12r(r-1)}{(r+2)L^2},
\]
where \(L=3r+2\). All are positive because \(r\ge7\).

The packaged checker `artifacts/verify.py` constructs the semidirect products for
\[
(p,q,r)=(2,3,7),\quad(2,5,11),\quad(2,3,13),
\]
enumerates all cyclic subgroups, tests every ordered pair for permutability, and recomputes every relative degree directly from the definition.

It returns `VERIFY_OK`.

Finite enumeration is not used to prove the universal theorem.
