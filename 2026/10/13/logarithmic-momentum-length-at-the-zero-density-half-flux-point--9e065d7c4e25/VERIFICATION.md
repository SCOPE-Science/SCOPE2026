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

Equation (33) at half-integer flux, after removing the isolated half-integer momenta, gives |sin(πk)|≤r_ℓ(k)=2kℓ/(k²ℓ²+1). For fixed ℓ the right side is O(1/n) throughout the cell about n, so the band must be within O(1/n) of n. On both sides of n the edge function sin(πδ)−r_ℓ(n±δ) has positive derivative near zero and changes sign, yielding exactly one interval. Substitution gives r_ℓ(n±δ)=2/(ℓn)+O(n^{-3}), and the cubic arcsine remainder gives the claimed two edges. Width errors in momentum are O(n^{-3}), hence summable, leaving 4 log K/(πℓ)+O(1). In energy the width is 2n(δ⁺+δ⁻)+(δ⁺)²−(δ⁻)²=8/(πℓ)+O(n^{-2}); there are √E+O(1) full bands and a bounded partial band. The omitted flat points have measure zero in either coordinate.

## originality

PASS

The cited same-model source establishes integer localization and zero limiting momentum density at half flux, but its inspected statements do not quantify the surviving bands or the total occupied length on the zero-density scale. No same or stronger measure law for the target geometry was identified. No novelty is assigned to the dispersion equation, localization or vanishing density.

## value

PASS

The half-flux point is selected by the known vanishing momentum density, not by an arbitrary parameter slice. The sharpened result proves that the remaining occupied momentum length is unbounded, fixes its logarithmic rate, and distinguishes shrinking momentum widths from asymptotically nonzero energy widths. Those statements resolve a natural ambiguity left by a zero-density limit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
