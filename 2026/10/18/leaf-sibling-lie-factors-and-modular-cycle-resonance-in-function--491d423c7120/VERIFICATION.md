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

In the natural basis, Leibniz on e_v² gives D(e_f(v))=2a_vv e_f(v), forcing every image-indexed column to be diagonal. On e_v e_w=0, independence of distinct target basis vectors forces both cross coefficients to vanish unless v,w have the same target; for equal targets they are negatives of one another. Thus both vertices must be leaves for a nonzero off-diagonal entry. In characteristic different from two the diagonal recurrence has exactly one free parameter per cycle with 2^L=1, determines all incoming values uniquely, and makes each sibling leaf block scalar on its diagonal. Hence the diagonal subalgebra centralizes the skew blocks and different supports commute. In characteristic two the image diagonals vanish and leaf diagonals are free; transpose of a commutator of symmetric matrices is its negative, equal to itself here. These conditions are also sufficient by bilinearity. Dimensions and finite-field cardinalities follow, including the cases of empty leaf sets, singleton blocks and fixed points. In the star/chain comparison, eliminating noncycle coordinates in leaf-to-root order gives k[T]/(T²−T) in both cases, whereas sibling block sizes four and one give the stated distinct derivation dimensions.

## originality

PASS

Credit the simultaneous explicit Lie classification on nonbijective unweighted endofunctions over arbitrary fields. Earlier work covers the general Leibniz equations, characteristic-zero sibling mechanisms (including acyclic functional-square formulas), some rank-one cases in odd characteristic, and the perfect/bijective cycle result. None of the inspected statements covers the combined nonperfect cyclic case and characteristic-two symmetric blocks. The strongest apparent all-field rank-one comparison has a characteristic-two error as printed and does not cover image ranks greater than one even aside from that error.

## value

PASS

The derivation Lie algebra is a natural structural invariant. The decomposition reads it directly from the functional graph, distinguishes the actual Lie bracket from a mere rank of Leibniz equations, and identifies a substantive characteristic-two change, not only a parameter substitution. It also explains why the star and chain can have the same idempotent scheme but different derivation dimensions. No priority is claimed for that example in isolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
