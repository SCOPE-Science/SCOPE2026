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

# Verification record

Reproduce the finite checks by running `python check_whitening.py` with NumPy. The observed output was `PASS: 8472 reproducible exact/rational and seeded numerical checks`. The test covers exact diagonal arithmetic, repeated eigenvalues, random orthogonal changes of basis, attainment of the target condition number, and violation immediately beyond the predicted threshold.

The proof in RESULT.md supplies the actual all-dimensional argument: positive definiteness inside the radius, duality of a Frobenius unit ball, extremal compression to a two-dimensional plane, a sharp rank-two perturbation, and monotonic enlargement of the admissible perturbation set. Numerical sampling does not verify a universal quantifier or historical novelty.

Historical coverage comparisons included the complete relevant sections and conclusions of arXiv:2610.28808v1, arXiv:2603.28969v1, and the author-posted Giraud–Gratton 2006 manuscript. The author-hosted Rump 2003 PDF was inspected for matrix-sensitivity definitions and the distance-to-singularity theorem; a broader historical priority claim is not certified.
