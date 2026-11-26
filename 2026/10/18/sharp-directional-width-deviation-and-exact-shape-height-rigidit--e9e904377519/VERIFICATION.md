---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For a uniform direction on S^2, its absolute vertical component T is uniform on [0,1] and independent of planar azimuth. The product support function gives width sqrt(1−T^2)w_K(V)+hT. Integrating the five required scalar moments gives EW=μ(π/4+λ/2) and EW²=μ²(2q+2λ+λ²)/3. For q>=1 the sign of the height derivative is the sign of (π−2)λ+π−4q, which switches at a single positive height. Substitution gives R_*(q)=16(2q−1)/[3(π²−4π+8q)] for the minimized second-moment ratio. Its derivative is strictly positive, so q=1 is necessary and sufficient for the global shape optimum; continuity of width turns equality almost everywhere into constant width everywhere. Completing the square in the height numerator and taking the difference R_*(q)−R_*(1) give exactly the two displayed positive-denominator deficit terms. Direct evaluation reproduces Δ_*=0.0753372200107355 and h/w=0.7519383938841089. The polygonal specialization uses the cited planar result legitimately: Akiyama–Kamae eqs. (1), (3) define the same coefficient of variation and give q_n=1+ν_n²; Theorems 6–7 identify all minimizers with Reinhardt n-gons for n not a power of two. Monotonicity and the Cauchy mean-width formula then give exactly the stated bound and equality height. Inspected frozen RESULT.md, VERIFICATION.md and verify.py without executing the checker; the proof covers nonsmooth bases and all positive heights, unlike the recorded finite tests. The frozen related-record URL text in references 2–3 does not give functional URLs; the material comparator has the exact catalogue locator in the originality evidence. The mathematical proof uses the arXiv planar theorem, not those related-record links.

## originality

PASS

The supported distinction is the arbitrary-planar-convex-base, free-height right-prism optimum with the exact two-term deficit and equality at all constant-width bases. The closest identified earlier prism record has regular polygonal bases and fixed height, while the planar theorem is explicitly imported. A later catalogue result covers this exact three-dimensional theorem as part of a higher-dimensional extension; it is not an earlier source against the frozen record.

## value

PASS

The question compares width anisotropy in a natural product class with free aspect ratio, not a prescribed regular base or a single numeric example. The exact deficit separates height mistuning from planar width variation; the sharp extremizer family includes nonsymmetric constant-width bases and the theorem transfers existing planar optima to exact spatial prism bounds. It does not claim more general shape-distance stability or an unrestricted convex-body optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
