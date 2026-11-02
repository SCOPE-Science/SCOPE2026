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

The self-contained `verify_johnson_convexity.py` program uses Python 3's standard library, enumerates small Johnson graphs, and independently tests shortest-path convexity and all Boolean traces. Run `python3 verify_johnson_convexity.py`. The finite tests verify exact convex-set representation for \(J(3,1)\), \(J(4,2)\), and \(J(5,2)\), all \(21{,}700\) supports of sizes at most five for \(J(6,3)\), exact maximum-support counts for all \(n\le7\), and mixed-case canonical constructions for four larger parameter pairs.

The universal support criterion, VC formula, and extremal-count theorem follow from the written combinatorial proof, not from the computation. No independent audit or external proof certification was performed. Priority comparisons are limited to accessible primary texts and described abstracts; inaccessible full text remains a residual risk.
