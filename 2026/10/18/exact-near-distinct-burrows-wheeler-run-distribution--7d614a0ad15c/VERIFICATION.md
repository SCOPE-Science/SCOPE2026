---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Singleton multiplicities force primitivity and free rotation orbits, giving q!/2 necklaces. In the last column there is only one possible equal adjacent pair, so the linear run count is q or q+1. Its two occurrences of c are in rows beginning at the two successors of c. When they are distinct from c, the two singleton rows are adjacent exactly when the successors are neighboring alphabet values. When the occurrences of c are adjacent in the input, the c-prefixed rows begin cc and cx. Comparing c and x puts the c-preceded row cx on the side of the c block facing x, so the same neighboring-value criterion applies. For each unordered successor pair not containing c, designate one successor first, permute the other q−3 letters and cut the permutation into two tails. This gives (q−2)! necklaces per pair. For a pair containing c, use the unique representative ccx followed by the remaining q−2 letters in any order, giving the same count. There are q−1 neighboring pairs; count their complement or subtract from q!/2. At q=2 only the cc case arises and no q+1-run necklace exists. Aggregation and probabilities follow by disjoint choices of c and division. Independent last-column enumeration used stable inverse LF rather than sorting input rotations; all c at q=2..7 yielded the exact histogram, and reconstructing 20,159 necklaces also checked the successor rule. Replay: python -B /workspace/branches/frozen_recheck.py 4.

## originality

PASS

Credit the fixed-content total and one-cycle criterion to prior theory. The exact two-bin run refinement and successor criterion are not covered by the available earlier fixed-content or existence results. A later-dated Resultary record does cover the entire theorem in equivalent notation; this is exact overlap, not proof of an earlier antecedent or of any priority relationship beyond the indexed dates.

## value

PASS

This is the first content family in which BWT clustering can occur without any periodicity: the all-distinct family has no repeated symbols to cluster. The exact unclustering fraction 1−2/q, its rank independence and the local successor test give a baseline for fixed-content unclustering and run-enumeration work. The fixed-content total alone cannot answer that question, and the scope is natural rather than a chosen finite range.

The dated certificate retains the supplied scientific assessment, sources and limitations.
