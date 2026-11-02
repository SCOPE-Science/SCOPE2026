---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Identified (a,b) with (a+b)+b√2 in Z_2[√2]/(√2)^(2k). The noncancelling norm valuations are v(a+b√2)=min(2ν_2(a+b),1+2ν_2(b)), giving the source Delta. For λ=1+√2, verified v(λ-1)=1, v(λ²-1)=2, v(λ⁴-1)=5, and for s≥2 v(λ^(2^s)-1)=2s+1; odd multiples retain the same valuation. Return requires that unit-power valuation be ≥h=2k-truncated v(state). The shell of height h has 2^(h-1) states and yields exactly the stated cycles by division; k=1,2 and h=0,1,2,3,4,5 checked. Independent direct orbit enumeration k=1..6 gives 3,6,14,30,62,126 cycles, all states covered. Exhaustion for all k is symbolic, not inferred from finite checks.

## originality

PASS

Primary published Pell-sequence literature establishes standard-seed sequence period and matrix order, not the complete state-by-state distribution on the full dyadic state module. Exact shell census is a natural refinement; historical 2-adic quadratic-unit module results could imply it.

## value

PASS

For a canonical Pell recurrence, a complete all-seed orbit decomposition is an intrinsically natural finite-ring dynamical invariant, more informative than matrix order. The stabilization and first-appearance disparity of 2^t cycles are precise features future 2-adic dynamical studies can use.

The dated certificate retains the supplied scientific assessment, sources and limitations.
