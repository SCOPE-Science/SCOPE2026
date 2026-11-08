---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

Edge-open-packing means two selected edges cannot be joined by a third distinct graph edge between endpoints; an induced star may contribute three compatible edges. Q5 has 80 graph edges, hence the compatibility graph on those edges has 1120 conflicting pairs. Independent C++ reconstruction from Hamming adjacency searched all 12-cliques and all 13-cliques via branch with proper-coloring upper bounds: exactly 80 of size 12 and none of size 13. Independent Python generated all center constructions C={x,x xor a,x xor b,x xor a xor b} with wt(a)=2, wt(b)=4, wt(a&b)=1, yielding 80 distinct valid 12-edge sets. In each, four centers have distance pattern {2,2,4,4,4,4}, each with precisely three private leaves; independent enumeration matched all optimizer edge sets. Counting 32 choices of x, 10 a masks, 2 b masks / 8 representations yields 80 and a 40+40 parity split. Affine hypercube translations and coordinate permutations act transitively on the mask pattern. The finite exhaustive upper bound and structural census are complete for dimension five only.

## originality

PASS

Brešar et al 2024 Section 5.1 Table 1 lists Q5 lower bound 10 and proves exact results for power-of-two dimensions; an upper bound 12 and complete 80-optimum census/orbit for Q5 are not contained in those inspected results.

## value

PASS

Q5 is a natural unresolved finite dimension singled out by hypercube edge-open packing tables. Giving the exact maximum, all 80 optimizer sets, a geometric four-star normal form and a single automorphism orbit is a self-contained complete combinatorial classification of that natural object, not arbitrary one-off parameter fitting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
