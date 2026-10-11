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

# Computational verification and mathematical limits

Run `python3 verify.py` with a standard Python 3 interpreter. The script has no third-party dependencies, reads no external files, and constructs each graph from rim and antipodal edges.

The verifier exhaustively enumerates all bounded-independence faces of size up to five at each integer parameter \(5\le n\le14\). It tests the exact expected face counts, absence of five-vertex simplices, and all mod-two simplicial boundary ranks (reduced homology only in degree three, with multiplicities \(16,22,29,37,46,56,67,79,92,106\)). For each parameter it independently builds the path spanning tree and verifies the relative three-chain telescopes for every two-simplex not belonging to its bounded-independence subcomplex. Finally, it constructs the full Alexander-dual total three-cut complexes at \(n=5,6\) from independent triples and verifies all their mod-two boundary ranks; the only reduced ranks are \(16\) in degree four and \(22\) in degree six.

Expected final output: `VERIFY_OK`. These finite checks cannot prove the asserted theorem for arbitrary \(n\). The written proof establishes two-connectivity integrally, exact symbolic face counts and the integral homotopy type for every \(n\ge5\). No independent audit has been performed.
