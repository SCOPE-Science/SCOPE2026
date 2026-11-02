---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Without equality, the truth of any first-order formula under assignments depends only on assigned unary colors and on which colors occur globally: this follows inductively through quantifiers. Thus sentences are support-set Boolean functions. Nonempty disjoint union takes set union of supports; all arbitrary unions of finitely many colors reduce to a finite subfamily, so binary union-closure is necessary and sufficient. Every member of a finite union-closed support family is the union of its uniquely necessary join-irreducibles, yielding Theta_F=forall x OR_{J irreducible}(B_J(x) AND all color-presence existentials E_J). Direct semantic reasoning proves both directions, including F empty and k=0. The quantifier-rank-two bound is explicitly only for the restricted outer-universal syntax, since unrestricted rank-one existential sentences may already express a given example. Independently enumerated all union-closed support families for 1,2,3,4 colors (2,7,61,2480) and 37650 canonical semantics tests; all matched.

## originality

PASS

Carreiro et al. (2021/2022), full article Section 3.1, already gives realized-type normal forms for equality-free monadic first-order logic. Van Benthem, ten Cate and Yang (2026), full HTML Section 3.4, discuss an outer-universal conjecture for disjoint-union preservation and an equality-based counterexample, leaving general equality-free languages distinct. The submitted claim resolves only the unary fragment, using a canonical join-irreducible support basis and small obstruction theorem. The underlying support reduction and finite semilattice theory are prior art; no inspected result states or immediately implies the exact union-preservation normal form in these constraints, but priority could be subsumed by older unary-preservation folklore.

## value

PASS

This is a complete characterization with effective canonical synthesis and fixed quantifier-rank bound for a natural decidable fragment of a live preservation question. It identifies the smallest finite witness models and clarifies exactly why equality matters. The 2480 number itself is known finite-set enumeration and not presented as new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
