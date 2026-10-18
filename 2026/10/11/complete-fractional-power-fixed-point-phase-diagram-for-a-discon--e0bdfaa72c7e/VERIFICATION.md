---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-11.md",
      "INDEPENDENT_AUDIT_2026-10-11.json"
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

Read RESULT.md at frozen commit and reconstructed separate fixed-point equations. With \(u=(b-x)/b\), \(H_L(u)=1-b+bu-(1-a)u^d\) is strictly convex with positive endpoints; with \(v=(x-b)/(1-b)\), \(H_R(v)=cv^d-b-(1-b)v\) is strictly concave with negative endpoints. Weighted concavity gives exclusion when \(b\le d\) or \(b\ge1-d\); solving \(H=H' =0\) yields exact \(L(b,d)\), \(R(b,d)\) and interior x coordinates. Endpoint signs force precisely 0, 1, or 2 roots per permitted branch; derivative monotonicity gives the local types and generic one-parameter folds. Joint strict branch conditions give sharp four-root regime \(d<1/2,d<b<1-d\). Independently checked the exact \(a=1/20,b=1/2,c=19/20,d=1/4\) witness via the quartic signs at \(0,3/4,1\). Source verify.py also presents exact witness fractions, but witness alone is not a universal proof.

## originality

PASS

This particular final statement and its implications were checked against the named primary sources; the returned primary literature supports the stated best-of-knowledge comparison, while incomplete/full-text risks are expressly recorded. The Resultary semantic query returned temporarily_unavailable (search_completed=false), not a negative hit; no absence or external certification is inferred.

## value

PASS

A full natural analytic solution of the fractional regime explicitly left example-based in the original paper. It identifies exact saddle-node hypersurfaces, the sharp otherwise unobvious four-fixed-point phase, and local attracting/repelling order throughout the continuous parameter box. These are reusable structural facts about the motivating map, not isolated numerical witnesses.

The dated certificate retains the supplied scientific assessment, sources and limitations.
