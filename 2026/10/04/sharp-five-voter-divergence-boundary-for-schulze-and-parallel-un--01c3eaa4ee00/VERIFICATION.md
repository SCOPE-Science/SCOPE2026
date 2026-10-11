---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

For three candidates, both rules expose exactly the alternatives obtained by omitting a weakest edge of a majority 3-cycle, with all tied weakest edges retained. For four candidates the frozen C verifier exhausts all labeled one-, three- and five-voter profiles; the independently coded frozen Python verifier exhausts all \(98280\) anonymous five-voter profiles using simple-path Schulze scores and Tideman-style ranking elimination for Ranked Pairs. A fresh independent anonymous replay in this audit reproduced the weighted histogram \(6858144,275760,591120,185760,51840\), strict containment on every divergence, and canonical margin types \((-3,-3,1,-1,-1,-1)\) with weight \(11520\) and \((-3,-1,1,1,-1,-1)\) with weight \(40320\).

## originality

PASS

Parkes and Xia directly define and compare Schulze and Ranked Pairs, exhibit different winners under the standard weighted-majority formalism, and discuss parallel-universe tie-breaking as a known Ranked-Pairs variant. Their paper is about strategic-complexity results and does not state a four-candidate minimal electorate, exact disagreement frequency, universal first-layer containment direction or the two-margin-type classification. Exact Resultary searches for \(51840\) and \(5/768\) returned no matching record.

## value

PASS

The first disagreement layer between two major Condorcet methods is a natural structural boundary. The result does more than count examples: it gives exact prevalence, the one-sided winner-set relation and a complete two-type weighted-majority geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
