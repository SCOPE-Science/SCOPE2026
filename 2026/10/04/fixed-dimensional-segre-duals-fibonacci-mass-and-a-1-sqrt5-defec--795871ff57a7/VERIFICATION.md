---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Tangent space to Segre [u⊗v] is U⊗v+u⊗V; a bilinear form tangent there requires nonzero left and right kernels, equivalent to matrix rank <=a for (a+1)×(b+1). Determinantal codimension b-a+1 and Porteous class c_{b-a+1}[-(a+1)O(-1)]=binom(b+1,a)H^{b-a+1}. At fixed n=a+b, d_n(a)=binom(n-a+1,a); the adjacent ratio is (n-2a+1)(n-2a)/((a+1)(n-a+1)), crossing 1 precisely at q_n(a)=5a²-(5n+2)a+n²-1. Strict ratio decrease makes the ceil-root maximizer, with two adjacent ties if the small root is integral. Stirling gives defect ratio ->1/sqrt5. Pascal's identity gives sum_{a=1}^{floor(n/2)}d_n(a)=F_{n+2}-1-[n odd], and squeeze M_n^{1/n}->golden ratio. Independent exact-integer checks n=2..180 checked ratios, maximizers, and Fibonacci sum; all-n result is symbolic.

## originality

PASS

The rank-drop determinantal dual, Porteous degree, and Fibonacci coefficient identity are classical ingredients and explicitly not novel separately. Full Ottaviani--Sodomaco--Ventura arXiv text analyzes hypercubical multi-Segre hyperdeterminants, ED degree and stabilization for quadric factors, not optimizing rectangular two-factor dual degree at a fixed total intrinsic n or deriving the 1/sqrt5 defect ratio. Kaji's dual-defect theorem and Fulton's degeneracy loci likewise do not state the fixed-n mode. Resultary lookup found only this exact family theorem, plus adjacent but different projective-duality invariants. PASS is constrained to fixed-n extremal synthesis; elementary and potentially prior folklore remains risk.

## value

PASS

Dual degree and dual defect are intrinsic standard invariants of Segre varieties. The fixed-total-dimension family has a motivated tradeoff between complexity and defectivity, a nonbalanced exact optimizer, a geometric limit defect fraction 1/sqrt5, and a global Fibonacci degree census. These are natural exact family invariants and may be independently useful despite elementary binomial algebra.

The dated certificate retains the supplied scientific assessment, sources and limitations.
