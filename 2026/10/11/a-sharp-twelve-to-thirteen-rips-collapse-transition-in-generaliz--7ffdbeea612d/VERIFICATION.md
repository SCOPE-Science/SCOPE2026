---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

The inclusive radius-two Vietoris–Rips complex is Cl(GP(n,2)^2). Its square graph has U–U offsets ±1,±2; V–V offsets ±2,±4; U–V offsets 0,±1,±2. For n>=13, offsets in each v_i link lie between -4 and 4 and no modular alias can create an extra adjacency: the largest relative difference is 8, whereas n-4>=9. The five exact link-vertex cases therefore support a uniform symbolic closed-neighborhood fold certificate (8,7,6,5,4 folds respectively), leaving a single vertex in every link. A collapsible vertex link permits simplicial deletion of v_i; all n inner vertices can be removed sequentially. The remaining Cl(C_n^2) collapses to the outer C_n by pairing each triangle with its unique distance-two edge. At n=12, direct enumeration from original GP edges gives 24,108,160,84,12 simplices in degrees 0..4; exact F2 boundary ranks 1,23,85,72,12 yield reduced Betti vector 0,0,3,0,0. An independent NetworkX BFS/clique enumeration and bit-vector boundary-reduction implementation verified 13 sample parameters (13..101), 402 links, 2,412 fold pairs and n=12 boundary ranks. The five symbolic offset regimes, not the finite samples, establish the all-n collapse.

## originality

PASS

The exact GP(n,2) family and universal inner-link folding transition are not covered by the full-text graph-square sufficient criteria, Rips circle/cyclic graph theorem, metric gluing results, or product-cylinder/lower-order published results. Girth-five and a square five-clique exclude Adamaszek’s principal sufficient conditions, and a new five-case elimination is needed even when the cycle-square conclusion is known. This is a best-of-knowledge priority assessment, not an absolute novelty certification.

## value

PASS

Generalized Petersen GP(n,2) is a canonical infinite cubic two-ring graph family with persistent five-cycles, exactly where standard girth>=7 collapse criteria stop applying. Establishing an explicit simplicial collapse despite the short cycles fills a natural stability gap, and the exact n=12 mod-two H2 obstruction gives a sharp lower boundary. The all-n structural mechanism and finite threshold are mathematically motivated; no classification of unrelated graph parameters or scales is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
