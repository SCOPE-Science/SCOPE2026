---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

Read fixed tree RESULT.md and artifacts/verify_action.py. For every 2<=m<=n each Hom(K_m,K_n) cell is an m-tuple of disjoint nonempty color blocks; a cell fixed under g uses q whole color cycles, with signed Lefschetz weight (-1)^(q-m). Inclusion-exclusion over onto assignments gives L(g)=sum_{j=0}^m (-1)^j binom(m,j)(1-j)^{c(g)}. Combining the known Babson-Kozlov homology wedge in degree n-m, subtracting the trivial H0 Lefschetz contribution and sign(g)=(-1)^{n-c} yields the claimed class function (all n=m boundaries included). F_{n,q} colorings with q<m<=n stabilize a repeated pair transposition, hence have zero sign-isotypic part, proving the quotient has vanishing reduced rational homology via equivariant simplicial subdivision and rational averaging. For m=3 decompose the 2^{c(g)} all-subsets module by Young rule; coefficients n-2 and n-2j+1 are nonnegative. Independently enumerated complete fixed-cell signs for (2,4),(3,4),(3,5),(4,5), 24/24/120/120 target permutations respectively; all match. Infinite claim is the counting proof plus prior nonequivariant topology.

## originality

PASS

Babson/Kozlov full primary PDF contains nonequivariant wedge of spheres/Betti numbers, not the target-color S_n character computed here. Source permutation of source positions differs mathematically from target-color permutations. Resultary searched exact target character, sign function modules and rational quotient, no identified covering equivalent. Prior wedge is credited, priority of equivariant refinement remains best knowledge.

## value

PASS

A uniform exact character for the natural target-color action of complete-graph Hom complexes, with a rationally acyclic symmetry quotient and explicit Specht multiplicities, is a meaningful equivariant refinement of standard nonequivariant topology and useful in graph-homomorphism representation theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
