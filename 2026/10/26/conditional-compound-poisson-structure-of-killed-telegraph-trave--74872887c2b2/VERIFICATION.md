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

## Reproduction
Run `python telegraph_posterior_check.py` with Python 3, NumPy and SciPy installed (for example, `pip install scipy`). The checker numerically integrates equation (48) of Orsingher--Marchione, including the boundary atom, and independently evaluates the two positive Lévy integrals.

The executed source file was checked in the deliverable directory. It passed 72 numerical comparisons: conditional Laplace ratios for four positive parameter triples at three endpoint distances and three positive Laplace variables, Lévy-mass and moment integrals, endpoint-density normalizations, and the ballistic-atom formula. Default numerical tolerances are on the order of \(2\times10^{-8}\).

## Analytical verification and limitations
The unconditional endpoint density is already known to be Laplace; the proof derives its joint weighted density from the two-state telegraph generator independently and factors the conditional transform. The key nonstandard check is the Laplace transform of the positive modified Bessel \(I_1\), derived using the standard transform of \(I_0\) and integration by parts. Finite Lévy masses then identify ordinary compound-Poisson processes without invoking an infinite-activity limit.

The numerical integration covers finitely many parameters and does not establish the general theorem or originality. The continuous regular-conditional version is specified; exact conditioning at a null event otherwise has no unique pointwise meaning. No independent scientific audit has been performed.
