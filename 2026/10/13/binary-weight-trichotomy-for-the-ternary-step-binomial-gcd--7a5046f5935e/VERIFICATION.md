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
# Verification

The standalone `artifacts/verify.py` runs using Python standard-library integer arithmetic. It independently computes exact binomial GCDs and extracts their \(2\)-adic valuations for \(2\le n\le200\), evaluates the binary digit-sum expression directly over all \(1\le k<n\) for \(2\le n\le1000\), and verifies the symbolic proof's explicit admissible witnesses for each of those \(999\) rows.

The replay output is bundled as `artifacts/replay.txt`. Direct finite checks do not establish the theorem for unbounded \(n\); the exhaustive parity-subset argument and symbolic carry witnesses in `RESULT.md` supply the infinite proof. No formal or independent certification is asserted.
