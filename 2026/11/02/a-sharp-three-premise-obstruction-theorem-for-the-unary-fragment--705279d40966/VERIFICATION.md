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

The decomposition into outer-negation parity and syntactic core is unique. For each core B, independent truth/falsity bits are permitted; the sole restriction is t_circle=1 implies (t_parent,f_parent)=(1,0) or (0,1). A simultaneous positive and negative requirement on the parent contradicts a positive circle requirement. Conversely absent that triple, choosing (1,1) only when both parent signs are demanded, (1,0) when positive alone, and (0,1) otherwise satisfies every circle requirement. The induction extending signed unary bits to all binary connectives enforces De Morgan, involution and the one-way circle implication, including nested circles and all infinite premises. Every proper subset of a prohibited triple is satisfiable, so the exact 3-Helly statement follows. An independent enumeration of 6,564 core-forest premise subsets for sizes <=4 matched the criterion; this is only a finite sanity check. Linear scanning assumes unshared input tree or linear-time syntax interning.

## originality

PASS

Grandinetti–Rodrigues 2026 Definition 3.2 gives the exact six clauses and Sections 3–4 provide full-signature sequent decision procedures and known explosive circle triples. Neither inspected part gives converse classification of arbitrary nested unary inconsistent sets. Older LET_F tableau work gives a general decision method, not this exact obstruction family. Search of Resultary returned no obvious equivalent statement; this absence alone is not a novelty proof. Best-of-knowledge originality is qualified by potentially older LFI terminology.

## value

PASS

A finite forbidden-obstruction basis for a nonclassical syntactic fragment is a meaningful structural/algorithmic invariant; sharp Helly number 3 plus arbitrary nesting and infinite compactness is stronger than noting the familiar explosive triple or restating a tableau.

The dated certificate retains the supplied scientific assessment, sources and limitations.
