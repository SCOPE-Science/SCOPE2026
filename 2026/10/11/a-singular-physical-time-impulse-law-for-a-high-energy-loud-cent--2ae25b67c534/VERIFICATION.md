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

# Verification and scope

The derivation uses exact physical-time conjugacy, conserved Hamiltonian, positive and negative passage-time estimates, bounded convergence, and an explicit total-variation bound. In particular, the direct inequality for the positive-branch integrand proves uniform control all the way to its turning point. The signed limiting observable is tested against arbitrary continuous phase test functions; finite-grid evaluation is not treated as evidence of weak-* convergence.

The standalone `check.py` uses the Python standard library and checks the defining coordinate identities and the energy derivative at representative values, computes the two turning roots, evaluates both physical-time quadratures after endpoint-regularizing substitutions, and checks a decreasing sequence of period ratios and negative excursion fractions. In the actual package location it prints `CHECK_OK` with period ratios `1.159338, 1.050719, 1.015438` and negative-phase fractions `0.110024, 0.040806, 0.013278` at energies 16, 64 and 256. These are finite sanity checks, not an infinite-energy proof.

The limit is valid in the invariant region \(x<1\) for the displayed undamped system, with phase anchored at the positive turning point. The delta impulse is a signed-measure phenomenon; no ordinary density convergence at the impulse or independent assessment is claimed.
