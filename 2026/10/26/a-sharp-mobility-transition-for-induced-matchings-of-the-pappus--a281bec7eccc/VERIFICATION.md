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

# Reproducible finite checks

Run `python3 check_lcf.py` and `python3 check_incidence.py` from a directory containing only the supplied scripts (no data dependencies). Compare their JSON printed outputs to `lcf_results.json` and `incidence_results.json` respectively. Both programs have executable assertions that abort on a discrepancy. Python standard library suffices; neither requires package installation, randomized sampling, or access to a web service.

The LCF checker constructs the 18-vertex graph from its 18-cycle and chord jumps, computes the unordered 27-edge list, and directly tests every \(4\)-, \(5\)- and \(6\)-edge subset. The independent checker constructs the 9-point/9-line incidence graph and uses recursive intersections of bitmask compatibility lists. Both construct the size-four one-edge-exchange graph and calculate its metric from complete breadth-first searches. The finite-search universe is bounded explicitly by \(\binom{27}{6}=296010\) six-edge candidates. The bound excludes all larger induced matchings by downward closure.

The fixed 27-entry quotient isomorphism permutation in `check_lcf.py` is verified pairwise, and the separate 18-entry line-graph root certificate in `check_incidence.py` is checked against every edge/nonedge. All recorded 9045 pairwise distances are exhaustive. This is a finite enumeration, not an assertion about general graph families.

Literature comparisons and unindexed-priority risk are recorded separately in `AUDIT.json`. Independent external scientific audit remains unperformed.
