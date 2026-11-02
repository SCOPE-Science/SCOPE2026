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

# Mathematical verification and scope

The complete proof is given in `RESULT.md`. Reproduce independent finite calculations with `python3 coalescence_check.py` (standard-library Python 3 only). The checker solves rational-valued first-step equations on the full particle-occupancy subset Markov chain, with no use of the stage-based Laplace formula in the generator construction. It checks transforms at three positive rational arguments and means for \(1\le n\le6\), and second moments for \(1\le n\le5\), as well as supplemental positivity and numerical asymptotic checks. Observed output: `PASS 467 exact-state and numerical assertions`.

The general statements are analytic: geometric excursions and the strong Markov property prove finite exactness; the coupled independent-stage series and its summable variances prove the centered distributional limit; a convergent infinite product and explicit cumulants distinguish the limit from Gumbel. Finite-state computations do not imply infinite asymptotic statements. Historical originality is assessed only against the named inspected sources and is not certified complete. No independent audit has been performed.
