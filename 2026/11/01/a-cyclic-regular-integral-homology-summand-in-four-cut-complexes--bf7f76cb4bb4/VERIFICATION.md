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

# Reproducibility and limits

Run `python3 verify.py` using Python 3.9 or later and only the Python standard library. The verifier constructs every connected four-subset and every five-subset whose four-subsets are connected, using the circular-distance rule. It checks the oriented cross-polytope chain is a cycle; verifies two integer cocycles at the wrapped cases \(n=12,13\), including signed unit pairings; and independently calculates mod-two boundary ranks, yielding \(\dim H^3(K_{12};\mathbb F_2)=2\) and \(\dim H^3(K_{13};\mathbb F_2)=14\). For \(13\le n\le28\) it checks the full cyclic identity pairing; for \(14\le n\le28\) it also enumerates all potential cofaces of the distinguished tetrahedron.

The universal conclusions are proved in RESULT.md by the explicit no-coface case distinction, uniqueness of the eight-vertex support block, and integral Alexander duality. Finite checks are corroboration, not an infinite enumeration or independent certification. The exact rest of the integral homology and other degrees are not determined.
