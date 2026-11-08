---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

The self-inclusive sequential XOR sweep is a product of involutory local updates, hence invertible with scan matrix F=(I+L)^(-1)(I+U). Cyclic rotation and relabeling reduce the single deleted edge to oriented gap k. Unimodular elimination over F_2[x] leaves a 2x2 block H whose determinant is (x^k+1)(x^(n-k)+1); its entry gcd gives d1=gcd(x^k+1,(x^n+1)/(x+1)) and d2=product/d1. Gcd with x^t+1 gives fixed dimensions g+h-epsilon, while invariant-factor order and Moebius inversion yield the full cycle census and sharp order. The boundary k=1 is explicitly handled. Separately enumerated actual binary scan state maps for canonical gaps n=4..8 and times 1..16 and reproduced all fixed counts. The sparse cycle comparison uses the known cyclic-ascent classification, with an explicit caution that the submitted proof quotes rather than rederives that all-scan cycle lemma. This is set-conjugacy, not linear similarity.

## originality

PASS

General linear SDS representations by Chen–Reidys and fixed-graph source-to-sink cycle equivalence by Macauley–Mortveit are prior methods. Defant studies cycle Rule 150, not the one-edge-deleted dense clique all-scan Smith decomposition. The distinct contribution is the dense all-gap exact invariant factors with uniform scan frequencies and their comparison to Eulerian cycle scan frequencies. Equivalent Coxeter/transvection factorizations are an unresolved historical-priority risk.

## value

PASS

Deleting one edge from K_n creates a canonical near-complete graph where scan order remains visible in an exact two-factor Smith normal form. The fact that its orbit populations match a sparse cycle model despite radically different scan-frequency distributions is a structural equivalence with complete orbit counts, not a routine renaming of a known cycle result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
