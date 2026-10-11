---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

For each coordinate difference \(s=d_i\), common output symbols are partitioned exactly by whether they consume support in the first error, the second error, both, or neither. For \(s=0\), the factor is \(1+KXY\); for \(0<|s|\le K\), the one-sided counts are the two endpoint indicators and the remaining overlap count is \(K+1-|s|-\alpha_s-\beta_s\); for \(|s|>K\), no common symbol exists. Multiplication therefore records the two total support costs independently, and truncating to exponents at most \(t\) gives exactly the intersection. Fresh direct enumeration reproduced the formula on 4,454 independent small cases. The support-one formula and global maximum agree with the published theorem.

## originality

PASS

The primary source studies the same error balls and proves the exact global maximum over distinct centers, together with upper and lower bounds for arbitrary center pairs at prescribed distance. It does not give the exact intersection cardinality for an arbitrary signed displacement vector. The audited coordinate generating function retains all signed per-coordinate overlap information and specializes to the published global maximum on unit support, so it is additional exact structure rather than a restatement of Theorem 6 or Lemma 14.

## value

PASS

Exact ambiguity between arbitrary received-center pairs is a natural invariant in sequence reconstruction, and the source previously had only an extremal value and bounds. The exact formula simultaneously resolves every center displacement and yields a polynomial-time evaluator, giving reusable information for list reconstruction and finite-parameter code design rather than an isolated number.

The dated certificate retains the supplied scientific assessment, sources and limitations.
