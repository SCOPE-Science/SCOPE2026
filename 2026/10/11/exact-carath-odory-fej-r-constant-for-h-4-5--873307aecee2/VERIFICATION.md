---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

Let τ=cos(π/9), σ=cos(2π/9), θ0=7π/9. At θ=π the (cosθ,cos4θ,cos5θ) signs are (−1,1,−1), while at θ0 they are (−σ,−τ,τ). Thus for any globally nonnegative candidate, τT(π)+T(θ0)=1+τ−a(τ+σ)≥0, implying a≤(1+τ)/(τ+σ)=2 cos(π/18)/√3. The proposed a,b,c at r=cos(7π/9) satisfy 8r³−6r−1=0 and factor T(arccos x)=(x+1)(x−r)²R_r(x)/[(9/2)(8r²−6r−1)]. I independently reduced the identity modulo the cubic in exact symbolic arithmetic, verified the residual quadratic has positive leading coefficient and negative discriminant, and the denominator is positive for r∈(−1,−3/4). Thus T≥0 for every x∈[−1,1], not only on sampled θ. Both positive-weight contact points must vanish for equality; interior zero derivative forces a third independent linear equation and fixes b,c uniquely. Independent symbolic check gives 3a³−3a−1=0. Numerically sampled positivity is merely supplementary.

## originality

PASS

The primary sparse Carathéodory–Fejér works organize positive definite support and derive singleton/complement/parity/tail exact families, none algebraically yields H={4,5}. An actual published neighboring SCOPE record at 2026/10/04/exact-carath-odory-fej-r-constant-for-h-3-4--917b17d3814a/RESULT.md has M({3,4})=2cos(2π/7), different support and cubic; it does not imply {4,5}, since distinguished first harmonic is fixed and no support inclusion or dilation carries {3,4} to {4,5}. The present exact two-contact upper certificate and separate factorization are for a genuinely different sparse support.

## value

PASS

M(H) for a natural two-element sparse harmonic support is an explicitly posed invariant in classical Carathéodory–Fejér support problems. The exact cutoff includes a unique extremal polynomial and an algebraic dual certificate, useful as a benchmark for sparse positive trigonometric polynomials and potential two-frequency classifications. The calculation is not a known-table recomputation, a pure substitution of H={3,4}, or an arbitrary angle slice: the contact frequencies determine new algebraic constraints and positivity factorization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
