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

# Verification and limits

Run `python3 artifacts/verify.py` from the project root. The program uses only the Python 3 standard library. It enumerates the full scale-two graph-distance clique complex independently of the proof for every integer parameter from seven through twenty-four. It verifies the four-cross-polytope slab complexes and every intersection, the complete face vectors, the uniqueness of the distance-two endpoint pair for every outside face, and the freeness of all 16n elementary collapse pairs against all currently remaining faces. For parameters seven through ten it additionally computes boundary-matrix ranks over the prime fields of two, three, and five elements and verifies reduced Betti ranks 1 in degree one and n in degree three. Expected terminal line: `VERIFY_OK 18 complete simplicial collapses; 12 exact homology checks`.

These exact finite experiments do not prove the all-n theorem. The all-n proof is the distance classification, free-face argument, and cyclic homotopy gluing in RESULT.md. Integral homology and the fundamental-group statement follow from that proof, not from finite-field calculations.
