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

The analytic classification and enumeration in `RESULT.md` are the principal proof.

Run `python3 artifacts/verify.py` with Python 3 and the standard library. The script builds actual strong-product graph edges, computes distances from independent breadth-first searches, and tests the general-position predicate for every subset of cardinality \(2m\) in the documented finite range. It checks the structural iff statement, not merely its minimum-set count.

It then performs a separate enumeration by selecting two path positions for each labeled leaf and compares the support-size distribution with the four-term formula. The latter route uses no graph distances.

The direct census covers \(m=3\), \(2\le s\le8\); \(m=4\), \(2\le s\le4\); and \(m=5\), \(2\le s\le3\). Positional-pair enumeration reaches \(s=14\) for \(m=3\), \(s=7\) for \(m=4\), and \(s=5\) for \(m=5\). A total of \(1,641,522\) candidate vertex subsets are checked by graph distances.

Exact replay output is embedded at `artifacts/verification_output.txt`.

Finite enumeration is not an infinite certificate. Arbitrary \(s,m\) follow from the self-contained proof of center exclusion, support classification, and the four exhaustive counting cases.
