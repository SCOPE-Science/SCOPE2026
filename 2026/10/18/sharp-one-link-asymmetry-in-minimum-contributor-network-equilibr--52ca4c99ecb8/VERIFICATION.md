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
# Verification notes

The mathematical proof is self-contained in `RESULT.md`. The separately embedded `verify.py` can be run by `python3 verify.py` and requires only Python 3 standard-library modules.

The program checks graph connectivity by exact bit-mask reachability, independently computes the minimum size of an independent dominating set by exhaustive search through every subset, and then tests each nonedge of every labelled connected graph on orders \(3\), \(4\), \(5\), and \(6\). Recorded graph–edge counts are \(3\), \(84\), \(3140\), and \(186360\). Observed changes at order six: \(-1:29895\), \(0:155655\), \(+1:810\). The program asserts each case obeys the claimed universal bounds. For orders \(4\) through \(14\), it checks the improvement family, and for \(6\) through \(14\), the sharp deterioration family.

The enumeration is complete for the declared vertex bound because it loops over all \(2^{\binom n2}\) labelled edge subsets, filters for connected graphs, and then over all missing edges. No enumeration beyond six vertices is claimed; no finite check is used in place of the analytic all-order proof. No independent external audit has occurred.
