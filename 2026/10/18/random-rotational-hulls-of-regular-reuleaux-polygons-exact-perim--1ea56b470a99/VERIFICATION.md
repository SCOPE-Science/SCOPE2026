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

# Reproducible checks and limits

Execute `python verify.py` (Python 3.9+; standard library only). The recorded run completed `VERIFY_OK 9060 support/parameter/numeric checks`, `HAUSDORFF_OK 45 exact mid-gap identities`, and `GUMBEL_OK 2200 normalized maximal-spacing replicates`. The first battery includes 9,000 comparisons between two independently coded angular support computations (one over actual vertices and boundary arcs), an independent numerical integral evaluation and finite-copy tests, and 130,000 Monte Carlo samples for the four-copy expected perimeter at order seven. The measured sample estimate was approximately 3.201569; the exact integral predicts approximately 3.201486 at width one.

The second battery builds independent random rotation phase sets and directly checks the claimed support deficit at each largest-gap midpoint in the regime where the exact identity applies. The third battery checks three Gumbel CDF values using 2,200 normalized exponential-spacing samples. All randomized trials use fixed seeds. Symbolic proofs, including the support CDF, the Gumbel limit, and the asymptotic constants, are supplied in `RESULT.md`; finite sampling cannot establish universal identities or weak convergence. No independent scientific validation or audit is represented by these checks.
