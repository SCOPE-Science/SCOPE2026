---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

In the declared normalized Bergman bases, the kernel expansion gives (n+1)/(n+k+1) times the square root of the target/source monomial weight ratio. The calculation on polynomials extends to the integral operator: evaluation at t is bounded by (1−t²)^(−(α+2)/2) times the input norm, which is integrable on (0,1) here, and at fixed disk z the other kernel is bounded. Set x=n+1,y=k+1. The uniform gamma-ratio and shift errors, and the cell interpolation error by log differentiation, are relative O(x⁻¹+y⁻¹) for Kδ=cδ x^(−δ/2)(y/x)^s/(x+y). Squared weighted error sums on y≥x and x≥y are bounded respectively by constants times Σx⁻³ and Σy⁻³, using 0<s<1/2. This proves the uniform Hilbert–Schmidt comparison after the unit-cell embedding. The logarithmic unitary gives the half-line convolution h_s(t)=exp(st)/(2 cosh(t/2)) with output damping exp(−δu/2). Young's inequality and direct integration give uniform operator norms and Hilbert–Schmidt norms O(δ⁻¹/²). For q≥1 the positive cyclic trace integral can first be taken on bounded boxes and then passed to the limit by monotone integration and Hilbert–Schmidt convergence. Anchor u₁, scale it by δ, and express the remaining coordinates as differences from u₁. The product of kernels is dominated by an exponential of the negative sum of edge differences from any spanning tree of the connected cycle; each anchored displacement is bounded by the sum along its tree path. Thus for small δ the damping in relative coordinates is absorbed with a fixed integrable exponential envelope, and the remaining exp(−qδu₁) yields the factor 1/q after scaling. The unconstrained difference integral is the zero-value convolution power of the autocorrelation, hence (2π)⁻¹∫|ĥ_s|^(2q); substitution r=e^t yields ĥ_s=π/cos(π(s−iξ)). Trace-norm telescoping with the Hilbert–Schmidt error changes each scaled moment by O_q(√δ). Polynomial approximation for the weighted measures on a common compact interval then proves the asserted weak limit. The phase-space pushforward has no positive-threshold atom, including at the maximum, because each ξ gives at most one u at any positive level. Division by the spectral coordinate above t² is thus justified; F(x)=x^(p/2−1) gives every fixed real p≥2 including p=2. At s=1/4, ∫sech(2πξ)dξ=1/2 and ∫sech²(2πξ)dξ=1/π yield the two stated benchmarks. Replay: RESULT.md lines 52–153 with the summability/domination arguments above. The supplied verify.py was inspected, not executed: it checks quadrature and a finite entrywise gamma-ratio comparison, not a discretized spectrum despite the loose wording at RESULT.md line 153. No finite experiment is needed for the limit.

## originality

PASS

Best-of-knowledge pass for the weighted singular spectral law and its fixed-threshold and p>2 consequences for the exact differential operator. The p=2 residue, including 15π/8 at α=−1/2, is existing coverage and receives no originality credit. Neither exact entrywise energy knowledge nor critical boundedness and above-critical membership gives the other spectral moments or the full counting law.

## value

PASS

The number of singular modes surviving at any fixed nonzero level measures how compactness fails when the exact Bergman-weight gap tends to zero. The result resolves that distribution quantitatively, not merely its Hilbert–Schmidt mass or the already-known class membership, and gives usable constants for all fixed powers p≥2. Uniform control of the discretization error and the half-line boundary in all trace moments make the spectral law substantive. There is no claimed uniform shrinking-threshold result, p<2 asymptotic, or individual singular-value estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
