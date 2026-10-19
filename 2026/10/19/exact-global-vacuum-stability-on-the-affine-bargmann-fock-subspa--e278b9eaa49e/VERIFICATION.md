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

# Verification of the affine vacuum stability bound

## Analytic checks

The scalar Gaussian case uses \(Z\) of density \(\pi^{-1}e^{-|z|^2}\) and the exact Rayleigh moments \(\mathbb E|Z|=\sqrt\pi/2\), \(\mathbb E|Z|^2=1\). For \(s>0\), the variance derivative of \(|a+sZ|\) is twice \(\operatorname{Cov}(R,\cos\Theta)\), and the conditional angular von Mises law makes the covariance nonnegative (strict when \(a>0\)). This proves the global mean bound including boundary cases. Orthogonality and the exact phase minimization give the desired remainder. The normalized pure linear function \(F(z)=z_1\) attains the claimed Lipschitz ratio. No estimate is inferred from a finite experimental sweep.

## Executed numerical checks

With SciPy exponentially scaled modified Bessel functions, the executable `verify_affine.py` completed all 64 parameter cases in its documented grid. The checked inequalities are the displaced-Gaussian mean bound, its squared-algebraic refinement, and the claimed radial remainder; both axes of equality were exercised. Its final exact Rayleigh arithmetic reproduces \((1-\sqrt\pi/2)^{-1/2}\). All tests completed successfully.

## Reproduction

Run `python verify_affine.py` with Python 3 and SciPy available. This is a supplementary numerical check of the displayed analytic proof. It is neither an exhaustive parameter test nor external validation.

## Scientific limits

The result concerns Gaussian observation of the entire affine holomorphic subspace, relative to the constant reference function. It makes no claim about arbitrary Fock signals, arbitrary reference functions, finite sample sets, or the full generalized phase-retrieval problem. No independent mathematical audit has been performed.
