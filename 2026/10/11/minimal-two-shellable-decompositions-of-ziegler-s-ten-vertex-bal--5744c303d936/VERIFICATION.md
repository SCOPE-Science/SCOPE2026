---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Independently rebuilt all faces from the exact 21 named tetrahedra, giving f-vector (10,38,50,21), and verified 21 distinct facets. An exact dynamic program evaluates recursive facet deletion/shellability for all 2^21-1 nonempty tetrahedron facet subsets, including non-shellability of the full complex; every one of 2^20-1 unordered nontrivial complementary partitions is then checked for two shellable sides, intersection maximal faces all triangles and recursively shellable 2-dimensional intersection. Fresh independent implementation reported exactly 247 valid partitions, six block-size counts 3/10/23/40/74/97, three size-five blocks and four-triangle interfaces matching RESULT.md. The source checker was independently read and its recurrence verified. This is a complete finite classification, not a sample or timeout inference.

## originality

PASS

Canonical fixed strongly nonshellable but constructible ball, with a meaningful complete minimal-size shellable assembly classification. Published qualitative constructibility does not imply a count or minimum under this defined partition interface; direct exact enumeration supplies extra information.

## value

PASS

Ziegler’s 10-vertex ball is a canonical minimal strongly nonshellable combinatorial object central to the distinction between shellability and constructibility. The finite invariant is structurally motivated: classify the smallest and all one-step assemblies into shellable pieces with shellable interface. Complete exact count, block distribution and three sharp minimum witnesses can be reused in comparisons of constructibility decompositions, without needing a general theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
