---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

The exact displayed 12x25 matrix has rank 12 and GG^T=0 mod3. Independently generated all 3^12=531441 primal codewords via vectorized GF(3) multiplication and reproduced coefficients 1,2158,39522,202272,236692,49992,804 at weights 0,9,12,15,18,21,24. Independently enumerated every normalized nonzero dual dependence on supports of size <=4, finding exactly one projective weight-4 relation on zero-indexed (0,18,19,20) with coefficients (1,2,2,2), and no smaller relation. Source MacWilliams transform produces the displayed dual enumerator summing 3^13. The unique weight-4 support is monomial-automorphism invariant; this does not determine the full automorphism group.

## originality

PASS

The Araya–Harada paper and original database present the classified extremal generator matrix and some dual-distance properties but do not print the second representative’s unique four-coordinate projective circuit or full pair of weight enumerators. The contribution is the explicit invariant of one natural code, not the database code’s existence or MacWilliams identity.

## value

PASS

For a classified extremal self-orthogonal ternary code, the dual minimum support size, low-weight multiplicity, complete spectrum, and unique four-column matroid circuit are natural code invariants used to distinguish classes and constrain automorphism searches. The intrinsic unique support stabilizes under every monomial automorphism, giving structural content beyond an arbitrary weight histogram. One exact representative can be useful independently of a full 26-class census; no broader classification is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
