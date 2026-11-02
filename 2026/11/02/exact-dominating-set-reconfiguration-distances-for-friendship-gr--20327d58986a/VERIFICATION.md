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

# Reproducibility and evidence

The theorem is a symbolic statement for every integer \(r\ge2\). The proof in `RESULT.md` gives the complete classification and sharp inequalities, including the all-parameter quantifiers. The following computations are **finite checks**, not an independent proof of the unrestricted theorem.

Run `python3 verify_direct.py`. It independently constructs \(F_r\) from its adjacencies and identifies every dominating set by the definition, rather than accepting the three-type classification as input. It builds one-toggle adjacency directly; checks states, edges, connectivity and every state's eccentricity for \(2\le r\le5\), then each symmetry-class representative for \(6\le r\le8\). Its final required message is `ALL_DIRECT_CHECKS_PASS`.

Run `python3 verify_metric.py`. It constructs the abstract state model without a domination predicate and compares all six proposed distance formulas with shortest paths between all ordered pairs for \(2\le r\le5\), then representative-source distances at \(r=6\). Its final required message is `ALL_ABSTRACT_METRIC_CHECKS_PASS`.

Expected examples include \(r=2\): 19 states, 28 edges, radius four, diameter five, three central and sixteen peripheral states; \(r=5\): 750 states, 2752 edges, radius seven, diameter eleven, six central and 224 peripheral states. The programs use Python 3 standard library only. Neither code file downloads sources or relies on external input.

The historical novelty comparison is limited by possible older unindexed equivalents and incomplete access to some prior records. The scientific claims and proofs are offered for examination; independent audit has not been performed.
