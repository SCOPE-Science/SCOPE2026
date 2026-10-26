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

## Analytical verification
The proof reconstructs the conditional transition rule and exact martingale bracket. Its three decisive ingredients are (i) an asymptotic for the normalizing product with a convergent multiplicative constant, (ii) almost-sure finiteness of the entire bracket correction by a summable second-moment bound, and (iii) uniform logarithmic-clock bracket convergence plus bounded-jump martingale functional CLT. The covariance-clock inversion is an ordinary derivative identity. Scalar phase variation follows from a periodic first-order ODE and nonzero mean-zero forcing.

## Reproducible finite checks
Execute `python verify.py` with Python 3, NumPy and SciPy. It tests 378 exact rational transition/martingale identities on all binary histories through six steps; 244 numerical derivative, inverse, and first-order expansion identities; the nonconstant profile at \(h(\theta)=0.1\sin\theta\); and finite product sums for three terminal indices. The finite checks are supplementary, not an infinite proof.

## Known limitations
The theorem applies to the specified smooth periodic perturbations of critical repetition probabilities. Originality cannot be certified from limited literature coverage; related urn martingale invariance principles remain a plausible source of equivalent reformulations. Independent audit has not been performed.
