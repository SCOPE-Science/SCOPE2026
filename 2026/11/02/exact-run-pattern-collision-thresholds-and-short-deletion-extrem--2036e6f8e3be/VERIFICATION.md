---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

First unequal retained count in a pair of equal-output deletion patterns forces erasure of at least one current-run letter plus all letters between two equal-symbol runs; hence t>=delta. A pair of patterns deleting one opposite end-run letter and every intervening run collides at delta; same extra deletions extend to all t<length. Smoothing identity Q_(a-1)Q_(b+1)-Q_a Q_b=sum_(j=b+1)^(a-1) z^j is coefficientwise nonnegative, giving balanced upper bound. Cyclic q distinct successive run symbols ensure delta>=q>t, attaining it, and n=r=t+1 proves sharpness as a uniform sufficient q threshold. Independent exact enumeration checked iff onset for 3076 binary and 4923 ternary short-word/deletion cases. Full verifier read; finite checks are corroboration only.

## originality

PASS

The first-collision threshold and tight nondivisible-run extremum are not identical to prior general deletion-pattern upper bounds. The 2026 Li–Wang–Fu primary preprint explicitly gives only a larger equal-length upper bound for r not dividing n; 2008 Mercier–Khabbazian–Bhargava unavailable full text remains priority risk.

## value

PASS

Resolves a natural open short-deletion nondivisible-run maximum with sharp alphabet sufficiency, and characterizes exact injectivity breakdown in an arbitrary run profile. These are structural coding-channel invariants rather than an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
