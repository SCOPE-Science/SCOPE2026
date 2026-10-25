---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

The bitangency criterion is an iff: a binary quartic on a rational line has all even geometric zero multiplicities iff it is a nonzero F_7 scalar times a quadratic square. Exactly 57 rational lines and 32 published model equations define a finite exhaustive census. Inspected both source implementations: five-value degree-four interpolation/square signatures and independent polynomial factor exponent plus infinity parity with Gröbner smoothness on all affine charts. Independently evaluated both D4 witness curves: b(C4)=4 and b(C8)=8 with precisely the asserted normalized line normals and no F_7 points. Full 32-vector histogram matches stored dual-code outputs, but was not independently executed in this run; source algebra and finite exhaustive algorithm support the complete claim, conditional on Faber–Grantham–Howe input classification. The shared Weil comparison uses F7, F49, F343 point counts/Newton identities; numerical Weil pair was not recomputed independently here.

## originality

PASS

The original classification provides 32 model equations but not the computed arithmetic bitangent frequency; exact equivalences and the broader theta/Weil work were compared. This is a qualified best-of-knowledge pass, not an absence-of-prior guarantee.

## value

PASS

Exact finite-field bitangent stratification of 32 canonical pointless genus-three quartics is a natural arithmetic moduli invariant not determined by Weil or rational-automorphism labels; the b=4/b=8 equal-coarse-invariant witness makes the refinement mathematically informative rather than arbitrary recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
