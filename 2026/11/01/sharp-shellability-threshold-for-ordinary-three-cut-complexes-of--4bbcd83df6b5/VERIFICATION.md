---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

The ordinary three-cut complex has complements of all disconnected triples of C_n^4 as facets. For n≤9 C_n^4 is complete; at n=10 the unique nonneighbor per vertex prevents an isolated vertex of any triple, so the complex is void. Independently implemented exact full mod-two chain complexes for n=11,…,16 (all faces; all boundary ranks) and reproduced reduced homology {11:H3=1,12:H6=6,13:H7=40,14:H8=15,15:H9=1,16:H11=3}; all lie below the pure top dimension n−4 and obstruct shellability. For n=17,18,19,20 retrieved four actual certificate blobs, independently enumerated all disconnected triples and verified each certificate lists each once and satisfies the shelling ridge-witness condition against every earlier facet. Verified counts (facets,spanning): (408,1),(528,10),(665,20),(820,31); hence homotopy wedge counts at boundary. Chauhan–Shukla Theorem 1.4 proves shelling for all n≥6p−3, so p=4 begins n≥21; published top-sphere count binom(n−8,2)−35=(n²−17n+2)/2 matches the four finite boundaries. This uses genuinely exhaustive finite certification plus a distinct published infinite theorem, not finite extrapolation.

## originality

PASS

The exact new structural step is the four n=17..20 facet shellings; lower Betti ranks and the n≥21 tail are not claimed new. The published Chauhan–Shukla 2026 paper Theorem 1.4 covers n≥21 at p=4 and explicitly describes a prior conjecture of sharp n≥4p+1 in its conclusion, without providing shellings of n17..20. The browsable 2024 arXiv version of earlier Chauhan–Shukla–Vinayak does not display the later published Conjecture 4.2/Table 2, a bibliographic-version limitation transparently noted; 2026 source confirms its published citation. No indexed earlier boundary shellings found; unindexed finite orders remain an originality risk.

## value

PASS

Proves a complete natural p=4 instance of a published sharp shellability threshold conjecture, providing explicit shelling certificates rather than merely homology coincidences. Shellability is a structural condition stronger than vanishing of lower homology, and the result joins exact boundary cases to a published infinite family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
