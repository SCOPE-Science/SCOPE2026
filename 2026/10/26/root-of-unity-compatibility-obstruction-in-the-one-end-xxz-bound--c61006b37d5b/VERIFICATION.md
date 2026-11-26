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

The source's Eq. (14), normalization and factors of 1/2 match the claim, and its Eqs. (3) and (12) specialize to Δ=0 and γ=i cot(πs/2) on the stated branch. At j=0, a0=g u1. At j=1 the forward coefficient vanishes, and eliminating u1 yields (g²−1/2)sin(πs)=0. Conversely at g²=1/2 the computed u1 solves both rows with any u2, so sufficiency is exactly for these two rows. At s=i log(3)/π the displayed relation has γ=coth(log(3)/2)=2 and sin(πs)=i sinh(log 3) is nonzero, so g=1 does give an admissible obstruction. Checked the repaired statement for scope: it does not conclude existence at resonance for the whole sequence, or nonexistence of the physical steady state away from resonance. No numerical or formal verification is required for the calculation.

## originality

PASS

Pass only for the specific compatibility test and counterexample to unrestricted forward well-posedness. The repaired relationship to prior work explicitly credits the x-field recurrence background to Yao et al. Supplemental Eq. (S.14), which Popkov–Prosen describe as the same recurrence for this special field. Neither the recurrence itself nor generic root-of-unity truncation is a contribution here. The inspected primary equation and its prose actually assert forward well-posedness except at zero or z-directed field, rather than asserting the compatibility locus. No inspected result establishes that locus; access to the older supplement remains unresolved.

## value

PASS

The calculation diagnoses a consequential exception to a printed assertion for a standard physical anisotropy, rather than merely noting a zero denominator. It both excludes generic x-fields from the normalized construction at that point and identifies the exact fields at which the first obstruction disappears, while still not allowing forward determination there. An explicit admissible dissipation strength makes the exception usable when checking the boundary construction. The claim remains a narrow mathematical correction, not a statement about which physical steady states exist.

The dated certificate retains the supplied scientific assessment, sources and limitations.
