---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the divisor-sum power collision theorem

The symbolic argument establishes that any powered collision with unequal exponents would need an integer common-power exponent simultaneously larger than \(\sqrt{n+1}/5-1\) and smaller than \(\log_2(n(1+\log n))\), impossible for all \(n\ge10000\). The endpoint is checked using the explicit derivative inequalities in `RESULT.md`.

The finite verification covers every consecutive pair \((n,n+1)\) for \(1\le n<10000\); it is exhaustive in this range only. Run `python3 verify.py` to check exact integer values and an exact perfect-power prefilter. Run `python3 verify_valuations.py` for an independent prime-valuation equality test of the same interval. Both use only the Python 3 standard library and include boundary \(n=1\) for clarity. The only equality in the finite interval is \(n=1\). The Pell candidate count is derived symbolically and is not a finite enumeration result.

These checks do not settle the existence of a nontrivial global collision, nor claim external or independent human validation.
