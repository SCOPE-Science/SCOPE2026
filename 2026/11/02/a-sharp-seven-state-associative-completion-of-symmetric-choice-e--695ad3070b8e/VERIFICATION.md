---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

The specified exact five-element operation is preserved on the original subalgebra. A new r with coarse (k,1) signature has r∨1=1 and 1∨r error-projected; associativity forces (e∨r)∨1=e and 1∨(e∨r)=1∨r. No old element or r can satisfy both, proving necessity of a second new value x. The displayed complete seven-element table has 0 as identity and k as absorber, all 343 associativity triples and all 49 Nmatrix projection cases hold. Independent exact finite reconstruction agrees, and the four required ordered masking profiles occur. This establishes only the stated *error-only extension* minimum, not complete determinization of the Nmatrix.

## originality

PASS

The 2026 Aldini–Graziani–Mezzina–Vergottini paper proves properties of the symmetric three-valued Nmatrix and its five-valued deterministic disjunction. The minimal seven-state fixed-subalgebra completion with reverse error mask and forced composite state was not found as a prior theorem. Qualified because older McCarthy/semigroup algebraic constructions may be equivalent.

## value

PASS

The source deterministic refinement misses one of the four natural ordered success/error masking signatures. Demanding all four while retaining associativity and the existing operation is a motivated algebraic minimal-completion problem. The extra forced composite error is a structural obstruction, not merely a tabulated tiny example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
