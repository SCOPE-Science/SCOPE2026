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

Partition away from null ties by the least absolute coordinate. Fixing the other k=n-1 coordinates y in the unit k-ball gives an interval of length 2 min|y_j|, because the strongest cylinder constraint omits the least coordinate. The homogeneous function m=min|y_j| has ball radial integral 1/n and Gaussian radial integral Γ(n/2)/2. Hence 2n times its ball integral equals 4/Γ(n/2) times its integral with weight exp(-|y|²) on R^k. Product integration and the layer-cake formula give the latter as π^(k/2) times the integral of erfc(t)^k. Dividing by κ_n gives the exact stated factor 2n/√π. With u=erf(t) this is E[f(U_n)] for f=exp((erf^{-1}u)^2) and U_n=1-W^(1/n) for uniform W. This coupling makes U_n strictly decrease and f strictly increases. Also 1<f(u)≤1/(1-u) for 0<u<1 by the shifted Gaussian tail, giving finite expectations and convergence to 1. At n=2 the body is the square and R_2=4/π. Writing x=√π u/2 gives erf^{-1}(u)=x+x³/3+O(x⁵), so f=1+x²+(7/6)x⁴+O(x⁶). The exact beta moments j!/[(n+1)…(n+j)] give both coefficients; restricting first to a fixed small interval gives an O(n^-6) local remainder and the tail bound gives exponentially small error on its complement. Finally min_i v_i²≤1/n, with equality for equal magnitudes, gives the claimed maximal radius and its distinct defect scale.

## originality

PASS

Prior coverage includes the coordinate-cylinder family, the exact low-dimensional volumes and a polar description in dimension three. The inspected statements do not give the strict order of the normalized all-dimensional sequence or the two-term defect with the stated remainder. No inspected source gave the integral representations either; full-text priority for those reductions, as well as the conclusions, remains open because the closest reports could not be read. The verdict credits the known cases and assesses the supported comparative and asymptotic result, not discovery of these bodies.

## value

PASS

Normalization by the inscribed unit ball separates the effect of increasing dimension from trivial unit-ball scaling for a natural Steinmetz family. Strict ordering and an exact leading and next contribution to volume quantify a phenomenon not visible from the maximal radius: the radius defect is of order n^-1 but the relative volume defect is of order n^-2. The beta representation explains this distinction and controls the error rather than fitting finite values.

The dated certificate retains the supplied scientific assessment, sources and limitations.
