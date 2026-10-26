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

# Verification notes

Run `python check_ladder.py` in this directory after installing `requirements.txt`. The program constructs actual normalized joint density matrices and blockwise energy-conserving unitaries. It verifies unitary and commutator identities, direct partial traces, exact endpoint maxima against all sector-swaps and identities, randomly sampled interior controls, threshold root monotonicity, minimal dimensions and the near-half-temperature expansion. It yielded `PASS 1484 standalone assertions` when executed from the package path.

The exact proof is the decomposition into one-dimensional extremal energy sectors and independent two-dimensional mixed sectors, followed by a Rayleigh-quotient bound and geometric-sum algebra. The program samples finite parameter sets only; it is neither an exhaustive search nor an independent scientific audit. Experimental implementation, arbitrary finite reservoirs, and full originality certification are outside scope.
