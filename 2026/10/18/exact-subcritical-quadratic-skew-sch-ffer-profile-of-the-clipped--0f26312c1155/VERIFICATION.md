---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For the real Banaś–Frączek norm N(a,b)=max(sqrt2|a|,sqrt(a²+b²)), the unit input set splits into flat and circular strata. Pure flat-flat and arc-arc inputs obey F>=q=1+r²; the explicit mixed-stratum witness has F<q below r_c=sqrt(2-sqrt3), so minima are mixed. The displayed U=(1-r*sqrt(1-r²+r⁴))/(1+r⁴) solves (1+r⁴)U²-2U+1-r²=0 and yields unit x=(1/sqrt2,(2U-1)/sqrt2), y=(-v,sqrt(1-v²)), with v=[1-(1+r²)U]/(sqrt2*r). Both transformed outputs lie on corner rays, attaining F_*=(1+r²)²[1+(1-r²)U²]/2. The two-variable inequality (1) is bounded by a linear combination of its two max branches with weights ell in (-1,0), mu>0, |ell|+mu<1; the resulting quadratic minimization completes squares, proves its unique lower certificate globally, and matches the witness. At r_c the value agrees with published exact saturation 3(1+r²)/4, and r=0 value is 1. Independently minimized over two unit-sphere angular parameters using SciPy global differential evolution at r=.02,.1,.22,.4,.51: discrepancies from claimed F_* under 1.1e-9, and inspected 2,000-sample verifier for witness/weights. These samples corroborate but the algebraic dual certificate supplies the all-r bound.

## originality

PASS

Xu–Liu Example 3.5 proves a late-r equality branch; Resultary saturation-threshold result proves precisely *where* that branch starts but expressly leaves r below it uncomputed; a separate Resultary paper obtains the first derivative at zero, not the full nonlinear interior curve. Radical U and global mixed-stratum certificate fill that natural gap.

## value

PASS

This computes a naturally previously missing entire interval of a standard geometric Banach-space invariant between two established analytic regimes. The exact radical and certified minimizer produce a complete λ=sqrt2 profile and a nontrivial global minimax lower certificate, not a reparametrization of saturation or of endpoint slope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
