---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

For reflexive row-or-column incidence on W=[m]×[n], m,n>=2, the Galois closure of S is intersection of all row-column crosses C_(i,j) containing S (empty intersection=W). Pairwise distinct-cross intersections are entire rows, columns or diagonal two-point sets. Intersecting further yields only singleton or empty, giving exactly ∅,W,mn points,m+n full rows/columns,mn crosses and 2*C(m,2)*C(n,2) diagonal pairs; count 2+2mn+m+n+2*C(m,2)*C(n,2), including degeneracies for m=n=2. At m,n>=3 the join incidence among singleton atoms recovers rook adjacency; automorphisms therefore are independent coordinate permutations and a coordinate swap only for square boards. If one side has 2 rows, closure factorizes into product of two height-2 M_b lattices, allowing S_b wr S2; at 2×2 the product is Boolean on four atoms with group S4. For direct Horn width, every S admits subset T of <=4 points with c(T)=c(S); four corners of a 2×2 subboard need four premises to infer a cell outside their two rows and columns when m,n>=3. Iteratively, pair rules complete any occupied row/column and triple matching forces all W; saturated proper sets are exactly listed closed extents. A three-point transversal with closed pair subsets shows width >=3. Thus direct/iterative widths are (4,3) thick, (2,2) thin non-2×2, (0,0) 2×2. Independent enumeration computed 16,25,44,69 closed sets at 2×2,2×3,3×3,3×4 and matches formula. The finite tests are not used as universal proof.

## originality

PASS

Compared mathematical implications against primary literature, Resultary semantic findings, aliases and broader formulations. Best-of-knowledge priority only. The (3,4) width separation requires explicit constructive closure saturation and 4-corner/3-matching lower-bound witnesses. The thin product decomposition and S_b wr S2 jump also require the concrete incidence and are not mechanically supplied by the general papers.

## value

PASS

The canonical formal-context closure of rook incidence is a natural object joining FCA and graph symmetry. The theorem provides a complete all-parameter lattice classification, exceptional symmetry enlargement at thin boards, and a sharp quantitative distinction between one-shot and iterated Horn inference at thick boards. These structural invariants go beyond the generic observation that concept lattices are intersection closures.

The dated certificate retains the supplied scientific assessment, sources and limitations.
