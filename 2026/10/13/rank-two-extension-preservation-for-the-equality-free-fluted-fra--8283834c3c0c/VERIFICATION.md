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

The suffix convention is essential. At level two and rank zero, all atom truth is determined by the target unary type and ordered binary type. One step back, the source unary type and the set of outgoing types determine every rank-one formula at level one, including arbitrary Boolean combinations and both quantifiers. At level zero the set of these row descriptors then determines the rank-two theory. B satisfies the existential χ_A exactly when each row of A is contained, in signed support and with matching source unary type, in a row of B. To check the crucial amalgamation independently, choose one witness f(a) in B for each old row (one choice per descriptor suffices). Form C on A plus a disjoint copy of B; retain all old–old relations, and assign each other binary pair by pulling back B along f on A and the copy identification on the new elements. Unary types agree with this map. Old rows realize their chosen complete B support through the new copy and add only allowed types on A. New rows already realize the full B support in the copy and mixed targets add no new types. This verifies D(C)=D(B) and inducedness, even on a single copy, with any higher arities freely filled off A and the copy. There is no forced conflict between ordered pairs or diagonal values. The proof works for infinite domains and for finite domains stays finite. Upward transfer to C and descriptor invariance transfer φ to B. The finitely many descriptor sets yield the stated finite disjunction, with ⊥ for no models. Existential formulae with signed atoms preserve truth in induced extensions by retaining witnesses. Empty unary/binary vocabularies produce a singleton empty atomic type, not a missing type. The replay independently checked the one-copy construction on 664 exhaustive compatible small pairs and 808 fixed-seed compatible pairs of size three, not a proof for all signatures. The rank-three obstruction was verified as an attributed result in Ding, §4, for both semantics.

## originality

PASS

The positive, equirank result for induced extensions in the unrestricted equality-free suffix syntax is distinct in the inspected sources. Ding supplies the negative rank-three bound, which is credited as prior, and the stronger preservation hypothesis of a different positive theorem. The possible ordered-fragment overlap does not give evidence of a result in the mixed unary/binary suffix syntax, although the exact comparison with the inaccessible original has a residual limit.

## value

PASS

This supplies the positive side immediately below an established failure threshold, and it simultaneously shows the finite and arbitrary cases with the original rank bound. The row amalgamation is a structural statement explaining why induced-substructure behavior is captured by signed witnesses at depth two; an unranked first-order preservation theorem would not give it. The positive threshold and constructive witnesses are useful beyond checking isolated formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
