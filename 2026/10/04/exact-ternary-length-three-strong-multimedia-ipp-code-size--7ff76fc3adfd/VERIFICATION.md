---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The parent-set definition reduces exactly to the local uniqueness criterion inside each pair-descendant box: a word is forced into every parent set iff one coordinate-symbol it carries occurs uniquely in that box. A fresh reconstruction generated 459 minimal violating subsets, all of sizes 4 or 5, directly verified the displayed 11-word witness, and exhaustively ruled out size 12 in the three symmetry-normalized second-word cases 100,110,111. The published general upper bound already gives 12, so the finite exclusion establishes exact maximum 11.

## originality

PASS

PASS. The original SMIPPC paper's full accessible text gives the general length-three strength-two upper bound q^2+q(q-1)/2, which is 12 at q=3, and constructs optimal codes only in congruence classes excluding 3 and 4 mod 6. The 2024 follow-up still advertises/ concludes optimal constructions outside those same omitted classes. Fresh Resultary search returned the distinct exact 2-traceability theorem, not a SMIPPC result. Thus no inspected source states or implies the exact ternary value 11.

## value

PASS

The ternary alphabet is the smallest member of a congruence class explicitly omitted by both the foundational and later optimal-construction program. Showing that the broad upper bound 12 drops to 11 is therefore a natural first boundary case for a fingerprinting/tracing invariant rather than a gratuitous tiny instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
