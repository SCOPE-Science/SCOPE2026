---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Buzaglo-Rogalski Lemma 6.4 identifies Delta_n as the sum-congruence subgroup of (Z/(3n))^3 rtimes C3 with coordinate rotation. Direct fixed-translation analysis gives center C_{3n}; two independent commutator translation vectors have Smith normal form diag(1,3), producing derived subgroup C_{3n} x C_n; presentation abelianization has Smith normal form diag(1,3,3n). Every nontrivial rotational element cubes to a diagonal translation; a has order 9n. The group is a 3-group iff n has no prime divisor besides 3; otherwise a Sylow 3-element rotates a nontrivial p-primary translation subgroup, excluding nilpotency. Independent SymPy Smith computations verified n=1,2,3,5,7,9,12. The proof works for every n>=1.

## originality

PASS

Material reading of the source embedding/order lemma and exact-presentation searches found no prior theorem giving the combined center, derived group, abelianization, exponent, metabelianity and nilpotency cutoff. The source supplies an embedding, not these invariant computations. A possible hidden isomorphic presentation remains a stated priority risk.

## value

PASS

The invariants classify key intrinsic features of a newly introduced infinite group family, including an exact nilpotency transition. This is motivated structural group theory across all n, not a one-off small-order table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
