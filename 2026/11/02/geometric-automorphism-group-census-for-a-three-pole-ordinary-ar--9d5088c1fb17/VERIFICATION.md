---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

Geometric descent uses uniqueness of the Artin--Schreier p-deck subgroup for three distinct simple poles in characteristic p>=5. An isomorphism descends to S3 and scalar Fp*, since h^p-h cannot have a simple pole unless h is constant. Normalizing b/a=u,c/a=v gives s(u,v)=(v,u),t(u,v)=(u^-1,-v/u). Three transposition fixed lines u=v,u=-1,v=-1 share exactly (-1,-1); three-cycle points solve u^3=-1,v=u^-1. Counting orbit sizes 1,2,3,6 gives the four formulas. Scalar action on deck translations determines the stated semidirect groups. Independent direct S3 orbit census for p=5..31 agrees. Applies only to Fp-coefficient representatives, not all k-valued triples.

## originality

PASS

Best-of-knowledge: related primary work gives this S3 × Fp* equivalence action and weighted masses, but inspection did not locate the four full-group-specific orbit frequencies on the nonzero prime-field coefficient torus. Hence the finite stabilizer-spectrum classification is not merely genus/p-rank existence. Historical invariant-theory and orbit-table equivalence remains possible.

## value

PASS

The complete stabilizer- and group-resolved finite-field moduli slice is a natural invariant of ordinary three-pole Artin--Schreier curves. It distinguishes generic, involutory, threefold and full branch symmetries, information absent from a generic-existence or weighted-mass statement. Exact group distribution is independently usable for automorphism and geometric moduli enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
