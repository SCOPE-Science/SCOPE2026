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

Run \(`python3 verify.py`\) with a standard Python 3.9+ interpreter; no packages, auxiliary datasets, or network access are required. The script builds the graph from its cycle and pendant edges; constructs all-pairs distances independently of the coefficient formulas; and rejects a vertex subset if any one of the three possible betweenness equalities holds for any triple.

For \(3\le n\le9\), all \(2^{2n}\) subsets are tested (a combined 349,504 subsets) and the resulting polynomial compared against two separate formulas: direct supporting-site cyclic-gap enumeration, and the finite binomial sums. For \(10\le n\le16\), the two formulas are compared by exhaustive supporting-site subsets. For \(17\le n\le32\), integer and degree checks run against the explicit formula. The text file \(`verification_output.txt`\) is a complete captured output from the included program.

Finite tests are not an infinite proof. For the infinite family, the crucial mathematical justifications are the root–leaf exclusion for sets of size at least three, the strict cyclic-gap geodesic criterion (including ties), the impossibility of nonadjacent eligible roots for at least four sites, and the bijective root/pair/triple markings that give all coefficients. These appear in \(`RESULT.md`\). This document records ordinary reproducibility checks only; no external audit has been performed.
