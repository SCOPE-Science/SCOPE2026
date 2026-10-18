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

# Reproducibility and scope

Run `python verify.py` using Python 3 and SymPy. The program checks the three-depth instance at five rational disturbance frequencies and seven rational allocation vectors. The matrix characteristic determinant and the analytic rank-one secular condition agree exactly. It additionally checks all sharp-family winner intervals, ties, parameter restrictions, and pairwise affine difference identities for each integer class count from 2 through 16. Its expected terminal message is `PASS: three-depth exact determinant tests and sharp families n=2..16`.

The algebraic proof in `RESULT.md` independently handles every integer class count and every real admissible parameter; finite tests are not an exhaustive proof. The computed spectral radius concerns the deterministic matrix of mean contributions; stochastic survival distributions and empirical seed-depth responses have not been evaluated. Source comparisons included full accessible matrix-theory and seed-dormancy materials; the central 2013 seed-depth article was not accessible in full. Independent audit has not been performed.
