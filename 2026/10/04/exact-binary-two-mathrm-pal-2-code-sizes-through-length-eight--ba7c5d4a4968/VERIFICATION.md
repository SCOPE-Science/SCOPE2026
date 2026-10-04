---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
The verifier reads `artifacts/certificate.json` and regenerates the exact-two length-\(2\) palindromic-duplication descendant set of every relevant binary source word.

For every \(2\le n\le8\), it checks two independent finite certificates. The `witness` words have pairwise-disjoint exact-two descendant sets, giving the claimed lower bound. The `conflict_clique_cover` groups partition all \(2^n\) source words exactly once, and every pair within each group has intersecting exact-two descendant sets; hence each group is a confusability clique and any correcting code has at most one word per group.

No optimization package, floating-point arithmetic, or stored graph edge is used by the replay. The certificate proves only the displayed finite values. The equality between exact-two and at-most-two correction and the transfer to reverse-complement duplication are published channel theorems cited in `RESULT.md`.
