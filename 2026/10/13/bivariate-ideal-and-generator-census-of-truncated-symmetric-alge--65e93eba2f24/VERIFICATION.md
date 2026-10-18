---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For A=F_q[x_1,...,x_d]/m³, d≥1 any prime-power q, split radical m=V⊕W with W=Sym²V, h=dim W. Every proper ideal projects to U≤V, dim U=r, intersects W in C containing VU; conversely every such pair and linear graph map U→W/C determines a unique ideal. W/VU≅Sym²(V/U) of dimension b_r=binom(d-r+1,2) in all characteristics including 2. Gaussian choices [d r]_q[b_r j]_q q^{r(b_r-j)} give dimension r+h-b_r+j. Nakayama μ(I)=dim I/mI=r+j, and A contributes unique X^{1+d+h}Y. Principal count follows from r+j=1. Independent exhaustive RREF enumeration of 374 subspaces of five-dimensional F2 radical for d=2 checked ideal closure under x,y and μ via product-span rank; got exactly 27 ideals with the asserted eight bivariate coefficients. General argument is exact, not inferred from finite experiment.

## originality

PASS

The standard local-submodule argument and Gaussian counting/Nakayama are classical tools, which are credited, but inspected Ringel and Ringel–Zhang manuscripts ask existence of reflexive or Gorenstein-projective modules over short local algebras, not a joint polynomial counting every embedded ideal of this free truncation by vector-space dimension and minimal generator number over all finite fields. Search for finite-ring ideal zeta polynomials and truncated multivariate rings did not demonstrate a previously stated bivariate formula. A known general ideal-zeta specialization is a live residual risk, not a proof of coverage.

## value

PASS

The free commutative length-three local algebra is a canonical finite-field test family for radical-cube-zero rings; the number and sizes of embedded ideals, refined by minimal generators, are natural enumeration invariants. The formula includes nonhomogeneous ideals, all prime powers and arbitrary embedding dimension and distinguishes ideals invisible to dimension-only counts, making the exact result independently useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
