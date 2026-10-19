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

# Verification instructions and limits

Run `python3 verify.py` from the extracted file set using Python 3 and no third-party packages. The program enumerates all 65,536 local pairing assignments of the order-five binary de Bruijn graph and, independently, every direct Euler tour starting with edge `00000`. Both constructions yield the identical set of 2048 rotation classes. Each generated cycle is checked for its 32 distinct length-five circular windows.

The two independent border algorithms directly compare all proper prefix/suffix pairs and count squares centered at each circular cut of root length one through four. The mathematical proof establishes that no border of a de Bruijn rotation of order five can be longer than four, so the latter algorithm is complete. All 65,536 cut comparisons agree, with 16 shortest one-symbol borders and four shortest two-symbol borders in each cycle. All seven remaining profile frequencies and all orbit-cell checks pass.

The search is exhaustive over the stated finite domain. It supplies no proof of analogous distributions at higher orders. The previous literature search cannot rule out an inaccessible historical equivalent. No independent external audit has been performed.
