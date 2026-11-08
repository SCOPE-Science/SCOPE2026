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

Coefficient-normalization by unique cube roots is valid since gcd(3,q-1)=1. Collision pairs uniquely fix a; three distinct roots require Q=x²+y²+z²+xy+xz+yz=0, and its q² zeros follow from nondegenerate ternary quadratic theory (char>=5); equality-plane intersection counts use 6≠0. Four distinct roots use six pair-equality hyperplanes. Subtracting the a=0 monomial moments and applying binomial inversion yields the q mod 24 table. Independent direct polynomial enumeration checked all a≠0 for eleven prime fields; extensions are handled by proof, not inferred from finite tests.

## originality

PASS

Zhi-Hong Sun 2006 Equation (1.7) already gives prime-field image cardinality for x^4+bx, explicitly excluded. The published family-averaged polynomial value-set work of Matera–Pérez–Privitelli covers other statistics; no examined theorem provides this exact individual quartic fiber histogram for all allowed finite fields.

## value

PASS

A complete output-fiber histogram, including 3- and 4-preimage strata and extension-field uniformity in a, is a natural value-distribution invariant strictly finer than the previously known image cardinality, with explicit arithmetic residue-class transitions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
