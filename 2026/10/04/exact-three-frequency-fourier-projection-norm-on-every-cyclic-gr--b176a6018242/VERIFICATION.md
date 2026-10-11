---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Convolution with the centered three-frequency kernel gives the normalized absolute kernel sum as the exact ℓ∞ operator norm by the sign extremizer; finite-dimensional duality gives the same ℓ1 norm. The kernel is negative exactly for integer samples N/3<k<2N/3. Summing the cosine over that consecutive interval yields the three displayed formulas according to N mod 3. Fresh direct evaluation for every N from 3 through 500 agrees with the closed form to at most 6.7×10⁻16; this numerical replay is corroborative, while the finite cosine-sum derivation proves all N.

## originality

PASS

The closest inspected literature concerns continuous-torus idempotent Dirichlet kernels or the norm of the full finite Fourier transform, which are different operators. No source located states the sampled endpoint norm of the three-character finite cyclic projection or its exact residue-class formula. The formula is elementary once the sign interval is recognized, but it is a natural all-N discrete Lebesgue constant and not mechanically supplied by the broader cited theorems.

## value

PASS

This is the first nontrivial consecutive-frequency projection and a standard discrete Lebesgue/stability invariant. The exact arithmetic dependence on N mod 3 explains how sampling the kernel's sign changes perturbs the continuous norm, providing a complete and reusable finite-to-continuous benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
