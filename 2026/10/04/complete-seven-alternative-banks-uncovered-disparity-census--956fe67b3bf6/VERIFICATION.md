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

An independent C implementation exhaustively enumerated all 2^21 labeled seven-vertex tournaments using the standard Banks maximal-transitive-subtournament definition and uncovered-set covering relation. It reproduced the full joint size histogram, exactly 13,440 strict BA subset UC cases, and fraction 105/16384. Canonicalizing every strict case under all 7! relabelings produced exactly four canonical representatives, with orbit sizes 5040,5040,1680,1680 and one class in each size cell (4,5),(5,6),(3,4),(6,7), agreeing with the frozen claim.

## originality

PASS

The first-disparity threshold and BA subset UC inclusion are prior. Best-of-knowledge originality survives for the complete minimal-order layer: exact labeled count/probability, four strict size-pair counts, and four-isomorphism-class census. No checked source or exact search supplied those enumerative data.

## value

PASS

The classification targets the first order at which two classical tournament solutions diverge and completely resolves that minimal layer, including exact probability and unlabeled types. This is a natural complete finite classification, not an arbitrary order slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
