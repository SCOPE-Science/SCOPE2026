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

The proof applies to four independent Bernoulli variables with identical parameter and arbitrary fixed strictly positive real weights. Run both attached standalone Python programs in the same directory using Python 3.13.5 (or compatible) and mpmath 1.3.0. `classify4.py` performs exact rational arrangement enumeration, checks the total of 23 realizable coefficient patterns, and compares them with the complete list represented by sorted integer weights at most eight. `curvature4.py` constructs those 23 coefficient lists independently, checks the exact derivative polynomials, and proves interval upper bounds strictly below zero on the full real interval from 0.0001 to 0.5 by outward-rounded enclosures and adaptive subdivision. The separate analytical endpoint estimate proves strict negativity below 0.0001; reflection covers above 0.5. The two programs passed from their embedded file paths before packaging.

Bounds and limits: The interval library performs outward-rounded real arithmetic; it is not a symbolic proof assistant, and this is not an external or independent scientific audit. The statement does not include heterogeneous Bernoulli parameters or five or more summands. The strongest priority uncertainty is that the full lead preprint was inaccessible; the originating public author discussion was materially examined.
