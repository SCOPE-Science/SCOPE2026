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

# Verification and reproducibility

The unrestricted theorem is proved analytically by cyclic averaging, the equilateral Lipschitz-free total-variation identity, and two explicit positive kernel constructions. There is no external formal certification.

Run `python cyclic_extension_checker.py` using the standard library. It enumerates 384 feasible rational cyclic six-point metrics in both coefficient-support phases, all six scalar extreme points of the source Lipschitz unit ball, and all 15 unordered pairs in each extended metric. The observed result was:

`CYCLIC_TRIANGLE_EXACT_OK metrics=384 full_pairs=5760 extreme_pair_checks=34560 phases={'three': 382, 'two': 2}`

Optionally install `requirements-optional.txt` and run `python independent_lp_spotcheck.py`. It solves an unrestricted nine-coefficient linear program for five rational cases, allowing asymmetric signed kernels. All five solutions matched the formula to numerical tolerance \(10^{-8}\). This LP is corroboration rather than a proof of unrestricted optimality; the analytic averaging and lower bound supply that proof.

The Euclidean application is derived from the classical Pompeiu triangle inequality and does not extrapolate from finite samples. The theorem does not certify mathematical originality independently, classify all optimizers, or provide a single globally optimal extension to the whole Euclidean plane.
