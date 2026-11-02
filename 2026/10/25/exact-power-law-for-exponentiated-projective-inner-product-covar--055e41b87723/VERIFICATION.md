---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For α=2m, the real Hilbert–Schmidt pairing of rank-one Hermitian projectors P_u=uu* equals |<u,v>_F|^2, for F=R,C,H. Tensor power X_u=P_u^{⊗m} is injective on distinct projective lines, so exp(κ<X_u,X_v>) is the Euclidean Gaussian kernel times e^κ and is strictly positive definite on distinct finite sites. For every α>0 not even, restrict to embedded real projective line parameter t∈R/πZ, where kernel is e^{κ|cos(t-s)|^α}. Unique cusp at t=π/2 has local expansion 1+κ|t-π/2|^α+O_symbol(|t-π/2|^{α+min(α,2)}); Fourier asymptotic is (-1)^{n+1} κΓ(α+1)sin(πα/2)/(π2^α)n^{-α-1}+o(n^{-α-1}). Nonzero alternating leading sign forces infinitely many negative Fourier coefficients and rules out PSD by the compact abelian group positivity criterion. Independent finite Fourier integration found negative modes at α=1,3 and nonnegative α=2; this corroborates rather than proves all α,κ.

## originality

PASS

Matzke (2021) explicitly computes Fourier signs of pure projective powers and is credited for the structural obstruction, but unexponentiated coefficient signs cannot logically rule out a positive infinite exponential series at all κ. The local cusp dominant term prevents cancellation for any κ and yields the exact exponent dichotomy simultaneously for R,C,H; no equivalent full exponentiated classification identified. Best-of-knowledge with general negative-type harmonic theorem priority risk.

## value

PASS

Exponentiated absolute projective inner-product affinity is a natural orientation-invariant covariance kernel. Exact concentration-independent all-dimensional PSD classification distinguishes legal Gaussian feature constructions from kernels with infinitely many negative Fourier modes. This answers a structural kernel-design question, not an isolated numerical parameter check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
