---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For integers d,t>=2, the Apéry residue thresholds h_{dj}=j and h_{dj+s}=(t+1)(d-s)+1+j follow from the unique reduced b-coefficient modulo a=dt+1. Rows m<t have the exact long suffix lengths d(t-m), while later interior gaps of length l<d last t+1 rows per interval, including the d-1 boundary case. Thus missing blocks occur t(t+1) times at each length 1..d-1 and once at each dj, j=1..t. Symmetry of the coprime two-generator semigroup and (1-x)1_S coefficient switches double each count for polynomial consecutive-nonzero-exponent spacings. Independent direct semigroup enumeration agrees for 25 pairs d=2..6,t=2..6. The proof handles d=2 and the initial/end rows; no finite extrapolation is needed.

## originality

PASS

Bachman 2026 Theorem 2 gives the SET of allowed lengths using the Euclidean algorithm, not multiplicities. Cafure–Cesaratto 2025/2026 Theorem 1.2 gives frequencies for b congruent ±1 modulo the smaller generator, whereas 2<=d=b mod a<=a-2 here; Theorem 1.1 gives partial second-largest information. Moree supplies the general semigroup-polynomial identity. The all-parameter multiset formula for the non±1 congruence family was not found as a logical implication of those inspected statements. An older detailed word decomposition may conceal an equivalent evaluated distribution.

## value

PASS

A complete symbolic run-length multiplicity distribution for a two-parameter family of numerical semigroups and binary inclusion-exclusion polynomials is a natural nontrivial refinement of the already researched set of attainable gap lengths; it is reusable for coefficient-word and spacing statistics, not a random isolated numerical instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
