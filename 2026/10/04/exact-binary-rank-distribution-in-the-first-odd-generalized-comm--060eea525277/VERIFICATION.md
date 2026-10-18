---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-11.md",
      "INDEPENDENT_AUDIT_2026-10-11.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For each three-space U in M_3(F_2), L_U(X)=s_4(A,B,C,X) is basis-independent because s_4 is alternating in its first three slots and every GL_3(F_2) basis change has determinant one. The identity and U lie in its kernel; the alternating trace form forces even rank, so only 0, 2, 4 are possible. Independently compiled C++ enumeration of EVERY unique RREF three-space in F_2^9, with s_4 evaluated by all 24 word permutations and exact GF(2) elimination, reproduced exactly 788035 spaces with rank histogram (0:11635,2:122320,4:654080) and 10795 rank-zero spaces containing I_3; hence 840 zero spaces avoid I_3. This is a complete finite census, not an infinite-field theorem.

## originality

PASS

The 2026 odd-generalized-commutator result is a Zariski-generic theorem in characteristic zero, and the older conjecture is posed for real matrices. Neither gives a characteristic-two Grassmannian rank histogram. The exact rank-zero exception 840 is not a consequence of genericity. Originality is best-of-knowledge from statement-level comparison, not a claim that the temporarily unavailable index was searched successfully.

## value

PASS

The smallest odd generalized-commutator instance over the smallest finite field is a natural boundary left untouched by characteristic-zero genericity. Exact rank-stratum sizes, maximal-rank proportion 1792/2159, and the unexpected 840 extra rank-zero subspaces form a complete, reproducible finite structural census with clear use as a benchmark for positive-characteristic conjectures.

The dated certificate retains the supplied scientific assessment, sources and limitations.
