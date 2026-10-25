---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

The Fernandes--Paulista dihedral extension theorem, checked in the primary preprint, says every partial cycle isometry restricts a dihedral symmetry, uniquely for domain rank at least 3; nonunique rank-two antipodal restrictions require correction. If alpha=g|D self-inverse at rank>=3, D invariant under g and g^2 fixes >=3 points, forcing g^2=id since a nontrivial dihedral permutation fixes at most two. Each group involution contributes (1+z)^f(1+z^2)^t for invariant domains, according to fixed points and transpositions. Odd n: identity + n reflections each (f,t)=(1,(n-1)/2); even n: n/2 vertex-axis reflections (2,(n-2)/2), n/2 edge-axis reflections plus halfturn (0,n/2). The group sum overcounts rank0 by n (odd) or n+1 (even), rank1 by n, and rank2 by 0 (odd) or n (even); subtract precisely those terms. Independently enumerated all self-inverse metric partial bijections from scratch for n=4..8, giving complete predicted vectors (1,4,12,8,6), (1,5,20,20,10,6), (1,6,30,32,36,12,8), (1,7,42,56,56,42,14,8), (1,8,56,80,124,80,64,16,10). Finite counts corroborate the universal group-theoretic argument.

## originality

PASS

The full monoid dihedral-restriction/uniqueness theorem and all-partial-isometry enumerator are acknowledged from Fernandes--Paulista. They do not equal the self-inverse rank polynomial: the self-inverse restriction criterion and low-rank collision correction must be imposed. Related Dimitrova et al works concern three proper submonoids and presentations rather than this entire inverse monoid self-inverse distribution. Standard cycle-index multiplication is prior known; only the natural complete rank distribution is claimed as new.

## value

PASS

The all-rank involution locus is a natural order-theoretic invariant of the inverse monoid of metric partial symmetries; precise small-domain overlaps make it differ from the raw group involution cycle index. The parity-sensitive complete distribution, not merely a tiny instance or arbitrary slice, can be reused in semigroup classifications and combinatorial enumeration. Its method is elementary but the complete natural classification is independently useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
