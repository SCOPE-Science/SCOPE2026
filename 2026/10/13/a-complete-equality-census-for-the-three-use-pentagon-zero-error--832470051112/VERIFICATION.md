---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

The 125 word alphabet is (Z/5)^3 and pair compatibility requires cyclic coordinate difference of 2 in at least one position. Fixing 000 by translation leaves exactly 98 compatible candidates. An independently written bitset exact branch-and-bound C++17 clique search (greedy proper graph-color pruning and unique branching) exhaustively finds 31,328 size-9 cliques on these candidates and no size-10 clique, proving alpha(C5 strong-power 3)=10. Translation double counting gives total 125*31328/10=391600 maximum labeled codes. Independent anchor/reflection/coordinate-permutation normalization finds exactly 85 natural isometry orbits, and orbit-size/stabilizer calculation yields histogram 1:53,2:19,3:2,4:7,8:1,10:2,40:1 with sum 391600. The fixed finite census is justified exhaustive enumeration, not random sampling; the generated C++ program was independently run and matched the source package ORBITS.csv.

## originality

PASS

The classical theorem alpha(C5 strong-power 3)=10 and a finite nonexistence search belong to Baumert et al 1971. The present original claim is the exact complete 391600/31328 maximum-code census and 85 natural symmetry orbit decomposition. The complete scanned founding primary and related odd-cycle-power results do not report these multiplicities, while exact-count and alias queries including Resultary returned no implication-equivalent source. A potentially relevant Sonnemann-Krafft 1974 paper remained inaccessible in full even after lawful preprint/OA and authorized Oxford retrieval; no snippet used to assert its noncoverage.

## value

PASS

The pentagon strong cube is a foundational test case for Shannon zero-error coding. A complete, independently exhaustive equality census and symmetry decomposition of its 391600 optimum codes supplies natural finite extremal invariants, distinct from the previously settled maximum cardinality and useful as a reusable classification benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
