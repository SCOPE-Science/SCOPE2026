---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Translation reduces each candidate of span<=L_k to a unique increasing (k-1)-tuple in [1,L_k], where L_k=1,3,6,11,17,25,34 respectively. An independently written iterative C++ enumerator with a direct Boolean sumset marker—not the archived recursive bitset implementation—exhausted 5,563,258 normalized sets across k=2..8, including 5,379,616 for k=8, and reproduced every advertised minimum-diameter vector. Every sumset cardinality in the admissible interval had a witness within L_k; any smaller-diameter counterexample would be in the enumerated search. d_8(32)=20 and d_8(33)=19, while all earlier profiles are nondecreasing. The endpoint L_8=34 includes a previously known length-34 Golomb ruler. Convention caution: for [0,N] the endpoint is 34, but a source defining N by [0,N-1] would write N=35.

## originality

PASS

The classical 8-mark optimal Golomb ruler gives only d_8(36)=34. Published general attainability and compression results do not in inspected sections list every k<=8 inverse diameter or the 32-to-33 strict descent. The most on-point July 2026 inverse-sumset source was not accessible in full, retained as genuine residual priority risk rather than presumed negative coverage.

## value

PASS

A complete inverse profile on the first finite cardinality with a nonmonotone t->minimum-diameter phenomenon is a natural additive-combinatorial classification. The exact first reversal is a motivated structural counterexample to an attractive monotonicity heuristic; the finite scope is explicit and exhaustively certified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
