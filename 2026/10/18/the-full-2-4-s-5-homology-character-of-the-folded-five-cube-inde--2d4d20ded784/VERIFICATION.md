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

The 5-regular folded-five-cube is Cay(F2^4,{1,2,4,8,15}), not the 10-regular Clebsch complement. Its automorphism group has exactly 16*120=1920 affine transformations since the neighbor stabilizer injects into S5. Independent enumeration of all 2^16 subsets yields 393 independent faces with cardinalities (1,16,80,160,120,16); independently checked F2 boundary ranks 15,65,95,16. Each rank is a rational lower bound via nonzero minors, and chain-complex upper bounds force equality over Q, giving sole reduced H3 dimension 9. Independent exhaustive signed-fixed-face checks for all 1920 automorphisms matched the formula sign(p)*(fixed(p)-1+sum_fixed (-1)^alpha_i(t)); the seven-value histogram is {-5:20,-3:60,-1:884,1:865,3:80,5:10,9:1}. Character decomposition as sign*(standard_4 plus the 5-line monomial W) follows from character equality over Q; S5 transitivity on five distinct translation eigenspaces proves W irreducible. Translation invariants 4, whole-group invariants 0. Nothing is inferred from a sample.

## originality

PASS

The known 5-folded-cube independent-set face table and sphere-wedge homotopy rank nine do not contain the 1920-element character; the previously published odd-folded-cube translation decomposition applies to the open-neighborhood complex, not this independence complex. Barmak star-cluster suspension does not supply this full character. Cioabă–Mim arXiv:2606.27328 full paper, especially Proposition 7.7 and Theorem 7.8, actually discusses H1 of the clique complex of the *degree-ten* Clebsch graph; it does not imply degree-three homology of the degree-five graph independence complex with full automorphisms. The difference in the degree-ten versus degree-five naming convention was explicitly checked. No stronger character source found, with residual unindexed-table risk.

## value

PASS

This graph is the canonical 16-vertex exceptional symmetric folded cube/degree-five Clebsch graph. Its rank-nine reduced H3 has a natural 1920-member affine action whose 4+5 absolutely irreducible decomposition gives the translation-fixed dimensions and loss of global invariants, information not contained in an ordinary Betti table. The module is a meaningful exact equivariant invariant for a natural graph, not merely a recomputation of its independence polynomial.

The dated certificate retains the supplied scientific assessment, sources and limitations.
