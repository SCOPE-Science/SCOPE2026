---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

The ordinary matching complex uses 15 edges of Petersen graph KG(5,2) as vertices and disjoint edges as simplices; its natural group is S5 on five underlying labels. Exhaustive matching counts by cardinality k=0..5 are (1,15,75,145,90,6). Exact rational invariant-chain elimination as implemented in the inspected verify_invariants.py finds reduced boundary ranks (1,14,61,79,6), giving H2 and H3 both rank5. Seven cyclic-invariant subcomplex computations recover class traces chi2=(5,-3,1,2,0,-1,0), chi3=(5,1,1,-1,1,-1,0) on (1^5),(2,1^3),(2^2,1),(3,1^2),(3,2),(4,1),(5). My independent standard-field oriented chain and image-trace computation reproduces every rank/trace; it is corroboration, not a claim that mod-p always equals Q. In characteristic zero averaging is exact and fixed dimensions determine class characters. chi2(g)=sgn(g)f(g) identifies sgn⊗Q^5, chi3(g)=((f-1)^2+f(g²)-1)/2-f gives the Specht S^(3,2) by Sym² of the standard module. Rational semisimplicity and characters prove the isomorphisms, with H_q=0 elsewhere. No integral module or homotopy equivariance follows.

## originality

PASS

Prior exact nonequivariant Petersen matching homotopy yields five S2 and five S3 but supplies only Betti numbers, not the distinct rational S5 characters. General complete-graph matching Specht results do not automatically descend to the Petersen subgraph matching complex. This exact two-module decomposition is original at best knowledge; standard representation-theory character identities are not presented as new.

## value

PASS

Petersen is the canonical S5-automorphism cubic Kneser graph, and the full rational automorphism action on the same-rank homology groups is a natural invariant. The finding distinguishes a reducible signed five-point module in degree two from irreducible S^(3,2) in degree three, information the homotopy wedge statement omits and future equivariant matching-complex work could require. This is a substantive classification, not a relabeling of Betti ranks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
