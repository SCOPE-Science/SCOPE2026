---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For critical binary Kesten tree, side-branch leaf-count PGFs obey f0(z)=(1+z)/2, f_h(z)=(z+f_{h-1}(z)^2)/2. The zero coefficients a_h=2^{-(2^{h+1}-1)} give the exact probability via coefficients ≤m of product f0...f_(r-1). The support set S*= {r-m,...,r-1} has uniquely maximal removed zero-leaf cost and contributes B_{r,m}=2^{-2^{r-m+1}+r-2m+2}; every other support loses ≥2^{r-m} in the binary exponent. With at most (m+1)r^m supports and b_h≤1/2+a_(h-1), this yields the explicit relative upper bound and the comb-like conditional concentration. m0 equality agrees with prior. The finite tree claim only takes N→infinity at fixed r,m, then r→infinity. Independent exact rational PGF bounds passed for r≤10,m≤3; general proof is symbolic.

## originality

PASS

The critical binary first-leaf tail m=0 is explicitly known in Maciá–Stufler 2026. The new higher order m≥1 exact fixed-order staircase, relative error and conditional dominant side-subtree configuration require multi-leaf PGF coefficients and a support weight gap absent from the checked original first-distance proofs. No simultaneous (m,r) or (N,r) limit is claimed.

## value

PASS

Higher nearest-leaf order statistics (m≥1) in a canonical critical branching local limit exhibit a sharp successive doubling of protection costs plus a unique rare-event geometry, addressing a meaningful refinement beyond already known nearest-leaf tail.

The dated certificate retains the supplied scientific assessment, sources and limitations.
