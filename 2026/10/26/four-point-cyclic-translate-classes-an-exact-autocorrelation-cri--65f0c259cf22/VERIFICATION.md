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

The mathematical proof in `RESULT.md` establishes the result for every integer \(n\ge8\). This document reports checks of the submitted code and does not claim external scientific validation.

Execute `python3 verify_four_shifts.py` in the same directory as this document. The script computes all distinct cyclic translates, then tests shattered-tree depths directly from the Boolean incidence table using a recursive version-space predicate, not the stated autocorrelation formula. The stated formula is computed separately from the stabilizer and nonzero pair overlaps. Every four-element set in \(\mathbb Z/n\mathbb Z\), for every \(8\le n\le20\), is checked: 20,293 input sets in total. Explicit trees are constructed and each of their paths verified against an actual hypothesis for seven representative cases.

The bundled `verification_output.txt` contains the successful `EXHAUSTIVE_OK 20293 input sets` and `ALL_CHECKS_OK` markers. The verifier is finite: it does not establish the universal theorem, nor does it prove bibliographic originality. Independent audit status remains not performed.
