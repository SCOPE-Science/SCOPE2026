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

For a cell centered at c, the unordered abscissas are c±T with T uniform on [0,h/2]. If ℓ and u are the endpoint interior slope bounds, φ(T)=(f(c+T)+f(c−T))/2 is nondecreasing and (u−ℓ)/2-Lipschitz. The independent-copy identity Var φ(T)=E[(φ(T)−φ(T′))²]/2 gives h² Var φ(T)≤h⁴(u−ℓ)²/192. The nonnegative cell slope increments sum to at most 2L, even for singular curvature; summing independent variances proves the claimed bound. Equality forces all 2L of the slope increment into one longest cell. Within it, equality in the independent-copy bound makes φ affine with slope L; almost-everywhere differentiation then forces slopes −L and L on the two halves. Convexity extends those slopes to the whole interval, giving exactly the stated midpoint V's, which attain the bound. For the auxiliary hinge kernel, integration over Z in [0,u] gives E[(u−Z)₊(v−Z)₊]=u²v−u³/3 for density 2 on [0,1/2]; subtraction gives (5). Each cell pair is unbiased by uniform marginals. Independent query noise adds precisely ν²∑h_i²/2, with no effect on extremizers; the maximum width alone already forces uniqueness of the equal mesh, which also minimizes the noise term.

## originality

PASS

The reflected estimator and unbiasedness are established prior art. The supported distinct claim is the exact worst-case law on arbitrary meshes with the complete extremizer classification; mesh and independent-noise conclusions follow from it. This is a bounded best-of-knowledge comparison, not a priority guarantee.

## value

PASS

The result gives a tight, shift-invariant error budget and a complete failure-mode classification for a standard implementable rule on a natural nonsmooth shape class. In particular arbitrary meshes depend on the longest cell rather than the sum of fourth powers; this changes mesh design and explains why a single cusp is worst. The noise extension makes the exact risk directly usable without claiming optimality over all quadrature algorithms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
