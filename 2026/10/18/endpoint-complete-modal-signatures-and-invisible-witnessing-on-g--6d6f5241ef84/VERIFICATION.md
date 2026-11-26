---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Under the declared fixed valuations, all leaves share the same strict order 0<s<1. At a terminal leaf Box always returns 1 and Diamond 0, and the three Gödel connectives act on that ordered triple uniformly. This proves by induction that the leaf-coordinate function of each formula is 0, s, or 1, with one common role. At the root a modal operation on these roles returns respectively 0, a or b as appropriate, and 1; the zero-weight root edge contributes only the neutral value. The propositional operations preserve the scalar root chain {0,a,b,1}. Box p and Diamond p recover a and b. At their extrema the neutral self-edge cannot supply a missing witness, since a<1 and b>0 even if a=0 or b=1. If both endpoints are present they witness the identity role, and constants or terminal evaluation cause no other witnessing obstruction. For 0<a<b<1 the signatures are distinct and the displayed table realizes each of the 12: Box bottom and Diamond p allow the needed root values independently of the leaf role, and Box bottom implies p gives the identity role with root 1. The pair with and without endpoint leaves has the same root theory and the same role-1 theory at every leaf, so universal local truth-one consequence agrees even for arbitrary premise sets. In fact the order of all formula degrees at a leaf also depends only on role. The conclusion distinguishes fixed-valued models, not class logics or frame validity. A fresh exact closure on vectors of actual world values gave 12 states on each of two finite stars with equal distinct interior endpoints and 9 on a singleton leaf set, outside the twelve-state hypothesis.

## originality

PASS

The distinct contribution supported by the comparison is the exact whole-model twelve-signature classification and the explicit endpoint-completion pair with equal exact root degrees and all local consequence despite different witnessing status. The unary leaf normal form and finite extremal reduction have materially overlapping indexed evidence and receive no independent originality credit. None of the inspected claims establishes the whole-model classification or the preservation across the witnessed/unwitnessed pair. This is bounded evidence, not a certification of historical priority.

## value

PASS

The explicit pair answers a natural expressibility question raised by witnessed semantics. Even a full collection of local consequences of a fixed-valued model cannot decide attainment, although the logic of the witnessed class can have a completeness theorem. The exact all-depth signature algebra makes the observational limit concrete, rather than producing only a bounded countermodel or one formula that fails.

The dated certificate retains the supplied scientific assessment, sources and limitations.
