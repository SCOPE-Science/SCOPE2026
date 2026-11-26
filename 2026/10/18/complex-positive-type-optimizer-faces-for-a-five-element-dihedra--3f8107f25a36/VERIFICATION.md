---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Fourier decomposition of the kernel f(g⁻¹h) gives the stated 2×2 Hermitian blocks: the rotation diagonal terms are 1+2u cosθ ∓2v sinθ and the reflection terms are b+c exp(∓iθ). Frequencies 0 and π (when present) split into the required one-dimensional representations. The support-preserving automorphism averages to real equal reflection values without altering the mass. The exact symmetric constraint uses 2|t|z; the missing absolute-value qualification in (2) is harmless for maximizing, since multiplying by the sign character (r↦1, s↦−1) preserves feasibility and strictly improves mass if t<0. Thus (2) can be used with t≥0. For 3∤n, α and β exist, β is in (1/2,1), and the two-root witness is feasible. The two displayed positive multipliers satisfy λα+μβ=1 and λ(4α²−2)+μ(4β²−2)=−2, giving the mass gap; the two distinct contacts determine the unique u,t. For 3|n, contact at 1/2 fixes t=1−u, and sign changes of the factorized polynomial give exactly the nearest-sample endpoints. For n=3 only 1/2 and 1 occur; the sample at 1 imposes u≥1/4 and t≥0 imposes u≤1, including the feasible t=0 endpoint. At β or 1/2, respectively, the unaveraged square-root inequality at an interior angle is already saturated by its (b+c)²z² term, so (b−c)²(1−z²) and 4v²sin²θ vanish separately; this works even when b+c=0. The frozen numerical LP checker was inspected, not executed; the exact Fourier and dual certificates were checked algebraically.

## originality

PASS

The scalar mass is existing theta-value coverage, not a novelty. The supported distinct claim is the complete optimizer set for complex positive-type functions on the dihedral group with the specified support. The closest primary text supplies an invariant optimum and a scalar dual bound but does not resolve all equality directions for the allowable dihedral-invariant Hermitian kernels. The frozen argument uses an active interior block to exclude complex or asymmetric equality cases, including the n=3 endpoint.

## value

PASS

For a natural two-reflection, two-rotation support, the equality classification distinguishes recovery of one function from a genuine interval of solutions. It settles whether symmetrization loses extremizers and gives the arithmetic transition and endpoints. These are concrete stability and reconstruction benchmarks for this group problem beyond the prior scalar value; no claim about the whole graph SDP is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
