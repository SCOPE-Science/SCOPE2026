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

# Verification of the totient capture law

The theorem is proved in `RESULT.md`. The standalone `verification/verify.py` uses only Python's standard library to construct adjacency lists for perfect rooted trees and compute the spans of vertex-generated Krylov sequences modulo each of two independent primes. It checks the leaf sum of totients and the root depth-plus-one rank for 17 branching-depth cases. These are reproducible finite consistency tests, not proof for arbitrary integers or evidence that the finite-rank computation exhausts the parameter space.

For four separately tested small trees, direct symbolic characteristic-polynomial calculation agreed exactly with the recursive factorization in the proof: \((b,h)=(2,2),(2,3),(3,2),(3,3)\). These symbolic spot checks are auxiliary evidence. The proof explicitly verifies spectral visibility at every leaf and asymptotic decay on the bright subspace, which are necessary to translate adjacency rank into eventual absorption.

Run `python3 verification/verify.py` using Python 3.9 or newer. No numerical package, downloaded paper, machine-specific path or external service is required.

**Limits.** The script proves no result outside its finite tested parameters; in particular it does not establish the general characteristic polynomial, no-jump semigroup convergence or literature priority. The stated result is limited to a single site loss, fixed nonzero homogeneous coupling, and perfect rooted trees.
