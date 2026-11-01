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

The verifier and finite certificate apply exclusively to the explicit six-vertex bidirected complete bipartite digraph. Run `python3 verify.py --check-certificate certificate.json` with Python 3.10+ and the standard library. It enumerates all 262,144 potential arc subsets with two independent membership criteria; confirms the nonempty face vector (18, 108, 264, 252, 72); checks 336 disjoint matching pairs and all 2,376 directed Hasse incidences by a complete acyclicity topological sort; performs all 336 integer cell-pair cancellations; checks the remaining 5-by-24 degree-three boundary, its determinant-one minor, and the zero 24-by-12 degree-four boundary. The included `verification_output.txt` is a recorded successful execution.

An independent direct simplicial boundary calculation over the field of two elements yields ranks (17,91,173,60), consistent with unreduced Betti ranks (1,0,0,19,12). These field calculations corroborate the integral result but do not themselves prove integral torsion-freeness or the homotopy splitting. The homotopy claim instead follows from the acyclic matching, signed unit-cancellation certificate, and the low-dimensional CW attaching-map argument in RESULT.md. The computation does not imply a formula for other bipartition sizes and is not an independently performed external audit.
