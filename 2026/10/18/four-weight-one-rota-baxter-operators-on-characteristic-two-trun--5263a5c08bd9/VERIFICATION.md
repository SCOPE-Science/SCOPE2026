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

With u=P(1), the (1,1) equation in characteristic two gives u^2=u. The only idempotents of the local ring are 0 and 1. The (1,b) equation then gives P^2=P in both cases. Such a projection satisfies the identity exactly when both summands are subalgebras: equal-summand inputs force closure, while mixed products cancel in the identity and there is one copy of each of the two pure products in its argument. A subalgebra with an element v of nonzero residue c contains 1 by expanding (v-c)^n=0, whose constant term (-c)^n is invertible. A single element of (t) with nonzero t coefficient generates (t) linearly by its positive powers, by triangularity. In any complementary pair one summand contains 1 and the other lies inside (t). If the former has an element with nonzero t coefficient it is the whole algebra (subtract the residue); otherwise the latter must supply the t coefficient and hence is all of (t). Thus the only decompositions up to swapping are A_n plus zero and K plus (t). Their projections give precisely four distinct maps and the stated ranks for n>=2, and automorphisms fix constants and preserve the maximal ideal. For n=1 only zero and identity remain. The reviewed finite-field checker covers all maps in its listed cases by bilinearity, not the universal quantifiers; it was not executed.

## originality

PASS

The supported distinct result is completeness of the four maps at arbitrary chain length over any characteristic-two field. Neither constructing the two complementary projections nor the splitting criterion in isolation is a novelty claim. The inspected closest square-zero classification and neighboring indexed results do not give the stated exhaustiveness.

## value

PASS

This is a natural complete classification for an entire family of one-generator local algebras, including arbitrarily long nilpotent filtrations and infinite fields. It shows why counting solutions to growing matrix systems gives a field- and length-independent answer by reducing the problem to the presence of one first-order generator in a subalgebra. The exact list, ranks, and trivial conjugation action are useful to work on classifications in positive characteristic; the finite checks alone would not have this value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
