---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Appending an e-digit integer acts on (v,k,1) by the upper-triangular matrix with rows (10^e,1,0), (0,1,1), (0,0,1). Over F₇ its sixth power is unipotent of index at most three, hence the 42nd power is the identity; lifting I+7K to its seventh power gives identity modulo 49. The order of 10 modulo 49 is 42 (powers 21,14,6 are 48,30,8). For e≥2, increasing e by 42 leaves the matrix and starting integer unchanged modulo 49, the iteration count unchanged modulo 294 by the Chinese remainder theorem, and e times that count unchanged modulo 42. Independent modular matrix powering and composition of widths 2 through 43 gave (a,b,length)=(1,0,0) modulo (49,49,42). This cycle can start after width four by cyclic conjugation of invertible maps. The computed state through 9999 was (28,39), then appending the first nine width-five integers gave (14,0), independently confirmed by a direct decimal stream through 10008. The nine-integer tail is identical in these residues at every specified width. A rotation moving h digits gives C′≡10^h C modulo 49 because 42 divides the length, so v₇(C′)=1 for every block rotation. This proves the exclusion for every integer power exponent at least two.

## originality

PASS

The theorem concerns a specific infinite family with m≡0 mod 9 starting at 10008. The strongest inspected perfect-power results address other residue classes or finite cutoffs below this family. A later study with an advanced extension of Kashihara's problem in its title concerns trailing-digit frequencies, not valuation or perfect powers.

## value

PASS

This supplies a uniform perfect-power exclusion for infinitely many block indices not decided by the known residue criterion or finite scan. The exact 7-adic valuation across all rotations is the useful invariant and covers all exponents at once; the result is not simply a large finite case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
