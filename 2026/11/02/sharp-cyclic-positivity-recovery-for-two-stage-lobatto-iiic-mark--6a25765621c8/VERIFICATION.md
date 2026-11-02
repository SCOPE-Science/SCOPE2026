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

# Reproducibility checks and limits

Run `python3 verify.py` with a standard Python 3 interpreter; the script uses only the standard library. The actual run passed **25,420 assertions**, including rational Gauss–Jordan inversions of the original cyclic generator polynomial, all cyclic coefficient and mass checks for sizes two through seventeen and twelve rational step sizes, independent checks of the Butcher tableau and stability rational function, boundary sine tests through two hundred states, and large-phase sign estimates. A zero-step matrix is exactly the identity by definition.

The analytic proof in `RESULT.md` establishes the infinite-dimensional family of finite cycle sizes: no finite test set is claimed exhaustive. Exact rational comparisons and floating trigonometric consistency probes play distinct roles. The proof requires no downloaded data or inaccessible executable dependency.

No independent mathematical audit has been carried out. Literature-overlap risks and restrictions on rates, graph topology, stages and accuracy are described in the result and review.
