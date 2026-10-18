---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The reproducible finite test is `python artifacts/verify.py` with NetworkX 3.5+ (tested under 3.6.1). It enumerates all 272 connected chordal seven-vertex atlas graphs, tests every nonempty clique neighbourhood, deduplicates 7268 candidates to 1614 eight-vertex isomorphism types, and computes the global refinement partition using collision-free tuple interning. The program asserts that the partition is stable, finds precisely two ambiguous classes of size two, and verifies nonisomorphism and the equitable quotients for their members. Its success line is `VERIFICATION_PASS: 1-WL ambiguities are precisely two unordered pairs on eight vertices.`

The structural completeness lemma is deletion of a simplicial vertex preserving connectedness, with its converse by clique attachment. The test uses NetworkX's graph-atlas completeness and exact isomorphism implementation; McKay's public 1614 count is an external count check, not a second end-to-end refinement-class enumeration. It does not prove uniqueness beyond eight vertices or rule out nonchordal countergraphs to global \(C^2\) identification. No independent external audit has been performed.
