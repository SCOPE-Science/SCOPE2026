---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The review reproduction starts with the ordinary binary zero-run criterion, b_0=1. At each of the 50 endpoints it scans starts in increasing order and resolves candidate equalities by exact byte comparison, so fingerprint collisions cannot alter the first match. Every (R,P) pair in the frozen table is reproduced, including the largest R=24576 at n=8192, whose last needed bit is at index 32767. A length-b witness is also a witness at every length <=b, and no length-a collision before the certified R can become a collision at any length >=a. Hence each interval [a,b] has its stated first repeat, and P agrees throughout because at the first collision two earlier matches are impossible. The intervals are consecutive, cover exactly 1..8192, and each adjacent pair of rows differs, giving maximality within that domain.

## originality

PASS

No equivalent finite table, explicit covering formula or sequence-specific implication was found in the inspected sources. Same-word work concerns Parikh vectors or scattered subsequences, and same-invariant work gives formulas for other words. The standard word definition and generic finite search do not supply the 25 exact intervals or their witnesses without an additional mathematical computation. The pass is restricted to the demonstrated finite classification.

## value

PASS

Baum–Sweet is a canonical automatic word, and the initial repeat threshold measures a different aspect of its prefixes than ordinary or Abelian factor complexity. The complete finite profile through 2^13 crosses many binary scales and resolves exact transition positions, alternating earlier-index patterns and the short exceptions. For example, the upper endpoint of a plateau can shift by one past three halves of the preceding power of two (1537 versus the unshifted 3072 at the next scale). Those exact boundaries and predecessors form a benchmark for any proposed structural or all-length formula; selected sample lengths or the leading scale alone could miss them.

The dated certificate retains the supplied scientific assessment, sources and limitations.
