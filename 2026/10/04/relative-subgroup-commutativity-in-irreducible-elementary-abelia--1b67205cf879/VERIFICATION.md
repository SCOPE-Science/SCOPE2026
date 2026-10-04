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
The universal proof has two exact components.

First, irreducibility classifies the subgroup lattice. Any subgroup outside \(V\) projects onto \(C_q\), and its intersection with \(V\) is invariant under the complement. Therefore it is either a complement or all of \(G\). Fixed-point-freeness makes the \(p^r\) conjugate complements distinct.

Second, the permuting-partner counts are exhaustive:
- \(1\), \(V\), and \(G\) have all \(L\) subgroups as partners;
- every nonzero proper subspace has exactly \(s+1\) partners;
- every complement has exactly four partners.

The relative-degree formulas are the normalized sums of these exact counts over the subgroup lattice of \(H\).

The packaged checker `artifacts/verify.py` independently constructs the semidirect products for
\[
(p,r,q)=(2,2,3),\quad(2,3,7),\quad(5,2,3),
\]
enumerates every subspace and complement, checks irreducibility, tests set-product permutability for every listed subgroup pair, and compares every directly computed \(sd(H,G)\) with the theorem.

It returns `VERIFY_OK`.

Finite enumeration is not used to prove the universal subgroup-classification theorem.
