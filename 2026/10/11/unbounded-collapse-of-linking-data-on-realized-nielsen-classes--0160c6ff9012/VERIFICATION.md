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

The proof was checked directly against Proposition 5.1 and Theorem 4.6 of arXiv:2610.04382v1. Proposition 5.1 is quantified over an arbitrary finite list \(u_1,\ldots,u_m\in F_n\), so using \(u_j=[x_1,x_2]^j\) is legitimate for every finite \(m\). The same proposition constructs one homeomorphism realizing the entire list and permits the prescribed loop braid \(\beta=1\).

For \(\beta=1\), the induced automorphism is the identity, so the source's twisted-conjugacy criterion is ordinary conjugacy. The commutator \(c=[x_1,x_2]\) is cyclically reduced and adjacent copies in \(c^j\) do not cancel. Hence the cyclically reduced length is exactly \(4j\). Conjugate elements of a free group have the same cyclically reduced length, so the coordinates are pairwise nonconjugate.

Every \(c^j\) lies in the commutator subgroup and therefore has zero abelianization. Section 5.1 of the source identifies the abelianization coordinates with linking numbers, giving the common zero linking vector.

No computation or finite census is used as proof. The result is limited to realized classes; essentiality, fixed-point indices, the Nielsen number, and the existence of one map with infinitely many classes remain unproved here.
