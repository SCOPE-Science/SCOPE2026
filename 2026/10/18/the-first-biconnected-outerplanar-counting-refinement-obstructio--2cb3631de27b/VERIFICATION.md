---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For connected simple outerplanar graphs under uniform-start 1-WL, the complete unlabeled population counts at n=1..8 are 1,1,2,5,13,46,172,777. Every connected outerplanar n=8 graph has a removable non-cut vertex of degree 1 or 2 (terminal outerplanar block ear), and alternatively any n=8 connected graph is an arbitrary-neighborhood one-vertex extension of some connected 7-vertex parent; exhaustive atlas cases justify global coverage. Independently implemented fresh generator from 172 outerplanar n=7 atlas parents enumerated and deduplicated all 777 n=8 classes, 75 biconnected, exactly four failures of stable WL versus full automorphism orbit, exactly two biconnected. Fresh independent automorphism/refinement checks on all four explicitly listed labeled 8-vertex witnesses verified their exact partitions, edge counts and automorphism orders 8,8,4,2. Thus the sharp cutoff at n=8 is mathematically exhaustive, not extrapolated from samples.

## originality

PASS

Best-of-knowledge statement-level comparison of the exact final conclusion against the closest primary theorems, relevant Resultary corpus, mathematical aliases and broader potential implications. Existing prerequisites are credited; absent search hits are not priority proof.

## value

PASS

Biconnected outerplanar graphs are a natural structured subclass for finite-variable counting expressiveness. Showing the first exact order of vertex-orbit blindness, identifying all four first failures and the two without articulation points gives a meaningful complete cutoff and explicit obstructions; finite size is intrinsic to a first-example problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
