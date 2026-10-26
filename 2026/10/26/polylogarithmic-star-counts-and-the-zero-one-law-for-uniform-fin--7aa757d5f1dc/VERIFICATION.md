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

# Reproducibility

Run `python3 verify_idempotent.py`. The program loops independently over every function on a labelled set of size from \(1\) through \(6\), tests \(f\circ f=f\) by direct function evaluation, counts components by root and nonfixed leaf multiplicity, and checks the exact first and second factorial-moment formulas against separately computed coefficient sums. Expected counts are \(1,3,10,41,196,1057\), and the last line is `IDEMPOTENT_STAR_MOMENTS_OK`.

The finite checker does not prove tail concentration for the root number, probabilistic variance estimates at arbitrary order, the asymptotic fixed-star frequencies, or EF-theory completeness; those are the symbolic steps of the manuscript. No independent mathematical audit was performed.
