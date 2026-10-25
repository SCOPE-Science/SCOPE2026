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

# Reproduction and limits

The proof is in `RESULT.md`; the supplemental exact-arithmetic program is `verify.py`. Run `python3 verify.py` with Python 3 and no external dependencies. The program implements each directional neighborhood gate from the fixed three-node adjacency list; it does not replace the directed gate by a symmetric ordinary confidence condition.

The program passed the following exact rational tests: 36,828 edge-word trajectories (all words of lengths zero through nine for a collection of exact rational compromise strengths, confidence thresholds and starting centers), 224 bilateral mean-square energy identities, 27 finite-time affine-recursion expectation and variance identities, and ten dyadic-mesh checks of the \(\rho=1/2\) uniform-law limit. It also checks blocked-leaf gate values on illustrative larger stars. All checks completed successfully with `ALL EXACT CHECKS PASS`.

The infinite-time statements are not consequences of these finite experiments. The mathematical argument uses a deterministic leaf-gate identity; a contracting coupling to prove uniqueness and convergence of the affine invariant law; independence and the strong law to prove nonconvergence and empirical means; and exact energy contraction, Markov's inequality and Borel–Cantelli for almost-sure consensus on the other side of the threshold. No independent audit, external validation or global novelty certification has occurred.
