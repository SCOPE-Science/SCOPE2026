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

The claim was checked symbolically from its stated hypotheses.

For a class-two group, centrality of commutators gives \([x^q,y]=[x,y]^q\). Taking \(q\) to be the exponent of the finite subgroup \([H,H]\) therefore makes every \(T_i^q\) commute with every generator. No stronger group-theoretic claim is used.

For \(p\in\mathbb Z[n]\) and a residue \(r\), expansion of each monomial shows that \(p(qm+r)-p(r)\) is divisible by \(q\), so the reduced iterate is again an integer polynomial. Polynomial independence survives affine substitution and subtraction of constants. Total ergodicity survives passage from \(T_i\) to \(T_i^q\).

The published commuting independent-polynomial joint-ergodicity theorem is then applied separately on each residue class. All residue-class limits are the same because measure preservation fixes the integrals of the translated functions. The incomplete final block contains only finitely many bounded summands and vanishes after normalization.

No numerical computation, finite enumeration, or unproved infinite extrapolation is used. The argument does not verify the infinite-commutator case and does not establish a non-totally-ergodic seminorm estimate.
