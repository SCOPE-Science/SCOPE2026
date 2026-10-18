---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

For f(n)=floor(μ−rn), integer adjacent differences are −1 or 0; composing yields g(n+1)−g(n)∈{0,1} and h(n)=g(n)−n nonincreasing by steps 0 or −1. The exact rounding defects ε_n=μ−rn−f(n)∈[0,1) give g(n)=r²n+(1−r)μ+r ε_n−ε_{f(n)}; hence h changes sign at infinity and, with unit steps, has a nonempty consecutive finite zero interval [L,U]. Monotonicity rules out overshoot; exterior g-orbits strictly approach and attain their nearer endpoint. f permutes finite fixed core and reverses its order, giving f(j)=L+U−j. The half-open real first-step cells ((μ−j−1)/r,(μ−j)/r] yield exact disjoint basins incl all boundary ties. Uniform additive error |g^k(n)−r^{2k}n|≤C gives τ(n)=log|n|/(−2log r)+O_{r,μ}(1) from lower exclusion and finite-state upper capture. The bundled rational checker was read, not executed; no finite result is infinite proof.

## originality

PASS

PASS best of knowledge after direct primary reading: Hoseana 2024 preprint Theorem2 enumerates all cycles and Theorem3(vi/vii), Proposition13 prove qualitative eventual cycle-or-fixed alternatives for λ=−r, not which cycle attracts exterior initial states when several coexist, nor exact half-open cells/finite basin measures, nor a logarithmic settling coefficient. Rozikov–Sattarov–Usmonov 2015 covers μ=0 only. These are not necessarily minor restatements of a periodic-point census. The 2025 published Hoseana version was identified but not read in full, leaving version-drift risk; search failure not claimed as proof.

## value

PASS

For a discontinuous quantized contraction with many coexisting cycles, exact initial-condition basin selection is a natural dynamical gap left open by listing periodic points and coarse eventual behavior. The basin partition and parameter-dependent exact cell measures distinguish an outer-cycle infinite-tail attractor from finite interior basins; the logarithmic transient coefficient addresses a meaningful independent asymptotic observable across all μ∈R and 0<r<1.

The dated certificate retains the supplied scientific assessment, sources and limitations.
