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

On zero-bit points, term-defined disjunction computes index join, and negation transfers same-bit identifications to the one-bit points. The unary term x·0_bottom sends both points at index i to 0_i, so identifying opposite bits first forces equality of index classes. If 0_i and 1_i are identified, right-multiplying by 1_j and then projecting to the zero bits forces i∨j to be in the class of i for every j. This proves that the only possible opposite-bit collapse is at the greatest quotient class, and same-bit identifications propagate it throughout that class. Conversely the natural map to the algebra over I/α preserves all operations; in that quotient merging the top fiber preserves negation and multiplication in either operand, since a left zero ignores the second operand and joining any index with the top gives the top. Restriction to zero bits and a mixed-bit witness prove the forward inclusion test; a surjective join map preserves any greatest element, proving the reverse. The argument does not use finiteness. For example equality on (N,max,0) has no optional bit, while a quotient formed by collapsing an upper tail has one. A finite index semilattice and every quotient have a greatest element; chain congruences are precisely interval partitions, giving the Boolean rank n. A fresh finite direct partition census recovered 8 and 14 for the 3-index chain and 4-index diamond, respectively. Replay: python3 review_evidence/frozen_math_spot_checks.py. The frozen exhaustive script was inspected but not executed; no finite enumeration proves the infinite case.

## originality

PASS

Credit the completeness and order of the congruence classification, including the quotient-dependent permission for a mixed-bit collapse, not the construction, the known top-fiber merger, or the number sequence 2^n. The closest primary comparison proves the construction and a merger but does not classify arbitrary congruences across indices. The accessible general ideal-congruence comparison does not supply that classification either.

## value

PASS

The construction is a natural family in the structure theory of McCarthy algebras. The theorem turns a whole congruence lattice into data from a join semilattice and specifies how an infinite index quotient can lose or acquire the extra collapse. It yields an exact finite lattice product, not merely a few congruence counts, and can be used to identify quotient algebras directly.

The dated certificate retains the supplied scientific assessment, sources and limitations.
