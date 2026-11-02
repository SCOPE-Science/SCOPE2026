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
# Verification and reproducibility

Use Python 3 and execute `python verify.py` in the directory containing the standalone program. Only the standard library is required.

The independent definition-based checker exhaustively enumerated all \(\binom{2n}{n}\) candidate extremal-cardinality subsets for each \(n=2,\ldots,10\), and found precisely the four or six word-coded sets. It additionally tested **every** vertex subset for \(n=1,\ldots,9\), totaling 349524 tested masks, and recovered the scalar minimal-domination counts (2, 6, 7, 18, 39, 75, 155, 310, 638) independently of the upper-set classification, matching OEIS A290379. The six/four constructive word families were also individually tested at every length from 11 to 100. The actual run emitted:

`VERIFY_OK extremal_lengths=2..10 distinct_sets=46 direct_all_subset_lengths=1..9 examined=349524 constructions=11..100`

Finite enumeration does not establish the infinite theorem. The structural proof in RESULT.md establishes both the universal upper bound and exhaustive classification; the code is a direct, independent boundary and arithmetic cross-check. The independent-audit status is unperformed.
