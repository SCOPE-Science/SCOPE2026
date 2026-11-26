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

Here U₀=0, U₁=1, and reduction mod 2 gives Uₘ even exactly at even m. The cited Murru–Sanna valuation theorem applies with apparition index 2 and 2 dividing a²+4b. Independently, set Vₘ=αᵐ+βᵐ for the characteristic roots. All Vₘ are even; the recurrence gives V₂ⱼ₊₁/a odd by induction, and V₂ⱼ=Vⱼ²−2(−b)ʲ≡2 mod 4 for j≥1. Repeated use of U₂ₘ=UₘVₘ thus gives ν₂(Uₘ)=ν₂(m)+t−1 on even m, with zero valuation on odd m. Taking the floor after division by 2 gives ν₄. At depth e≥1 of the 4-kernel all offsets except the final one give constant sequences; the final offset gives h+e with h(n)=floor((ν₂(n+1)+t−1)/2). Consecutive final offsets yield the unit constant, and then h itself is in the module. For t=1,2, h=s and s is unbounded; if t≥3, evaluating a relation first at n=4ʲ−1 and then at even n shows s,h,1 independent because h−s=floor((t−1)/2)>0 on the even indices. This establishes exact rank over ℤ, not just regularity.

## originality

PASS

The termwise valuation formula and regularity are established prior work. The supported additional claim is the exact rank split for the floor-transformed valuation and its 4-kernel across the specified parity family. The closest catalogued base-4 rank concerns Fibonacci, and the inspected general valuation paper's exact-rank theorem is for prime base.

## value

PASS

Exact rank distinguishes actual module complexity from finite generation in the first composite prime-power base. Even a and odd b are a natural parity regime with 2-apparition index 2, not a sample of isolated parameters. The threshold at t=3 identifies precisely when taking the floor requires an extra independent generator. This is a concrete family-level answer to part of a published composite-base rank question, rather than recomputation of the valuation formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
