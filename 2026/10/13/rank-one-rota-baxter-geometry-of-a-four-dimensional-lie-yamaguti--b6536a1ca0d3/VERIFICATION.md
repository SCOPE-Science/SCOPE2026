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

The cited examples match the displayed operations and the weight-zero identities. For rank one R=u⊗ℓ, both left-hand sides vanish by alternation in the first two slots. With ω(x,y)=x₁y₂−x₂y₁ and h=ω(u,−), the binary right-hand side is 2ℓ(e₄)(ℓ(x)h(y)−ℓ(y)h(x))u; the ternary one is the same expression with 2 replaced by u₁ℓ(z), so the binary condition implies both when char K≠2. If ℓ(e₄)≠0, taking x=e₄ forces h=0, exactly u₁=u₂=0. Otherwise R kills e₄. The zero operator belongs to both branches. Over an algebraic closure these are reduced determinantal cones of sizes 4×3 and 2×4, meeting in a 2×3 cone; they are irreducible of dimensions 6 and 5 with intersection dimension 4, and neither contains the other (e.g. E₂₁ versus E₃₄). These are reduced-variety conclusions, not claims that the coefficient equations define a reduced scheme. The source matrix families have zero second row, so E₂₁ is omitted but is not a counterexample to anything they assert. Counting normalized image-functional pairs gives 1+(qʳ−1)(qˢ−1)/(q−1) for an r×s rank-at-most-one cone. Inclusion–exclusion gives the stated polynomial; over F_{q^m}, substitute q^m, and exp(sum N_m T^m/m) gives the claimed zeta function with its stated signs. Independent bounded replay normalized the first nonzero coordinate of u to 1, enumerated all nonzero ℓ, and checked the original identities on ordered basis pairs and triples. It found 1257 of 3201 operators over F₃ and 22345 of 97345 over F₅, with no criterion mismatches and with E₂₁ included. The frozen artifacts/verify.py and artifacts/verify_output.txt were inspected, not executed; these finite replays do not substitute for the all-field proof.

## originality

PASS

The algebra, weight-zero identities, and a displayed sufficient family all occur in the literature. The supported distinct claim is the full rank-at-most-one locus on that exact example, including its reduced component geometry and arithmetic, not a correction to a previously asserted complete family. Both a neighboring two-dimensional Lie–Yamaguti classification and stronger operator results for different underlying Lie algebras were checked as possible overlaps.

## value

PASS

This is the natural minimal nonzero rank slice of a specific published Lie–Yamaguti example used in deformation theory. The complete classification reveals an unequal-dimensional reduced union, with the two solution mechanisms distinguished by annihilation of the derived line versus central image. It supplies an exact finite-field benchmark for the defining identities. The value is the complete slice and structure, not merely that one extra operator happens to be missing or that standard determinantal counts can be substituted after classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
