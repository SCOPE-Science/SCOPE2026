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

# Reproducible verification

The self-contained script `verify_crown.py` uses exact rational numbers, not floating-point eigensolvers, optimization solvers, network access, or outside data. Run `python3 verify_crown.py` with Python 3.

The script constructs heat-kernel matrices for every \(n\in\{3,4,5,6,7,8\}\) at rational values \(e^{-t}\in\{1,1/2,2/3,3/4\}\), verifies 24 rational heat matrices and all 72 representative pair transports by explicit primal-dual witnesses, and exhaustively compares 2359 anchored integer graph-Lipschitz potentials for the three smaller sizes. The anchored feasible polytope has integral vertices by total unimodularity of the edge-incidence constraint matrix. The successful reproduced result is:

`CERTIFICATE_OK rational_matrices=24 transport_witnesses=72 exhaustive_integer_potentials=2359`

Finite tests are not a proof for infinitely many graph sizes or continuous times. The proof in `RESULT.md` uses the exact Laplacian spectral projectors, symmetry-reduced Lipschitz dual optimization, and explicit attaining potentials to establish the unrestricted statements. No independent scientific audit has been performed.
