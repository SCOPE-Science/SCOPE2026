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
# Reproducible verification

The standalone files `verify.py` and `collapse_8.json` are sufficient. Run `python3 verify.py` in their directory using the Python 3 standard library. The recorded output is `verification_output.txt` and ends in `VERIFY_OK`.

The program constructs the fourteen exact integer-coordinate vertices, all 91 pairwise squared distances and complete clique complexes at squared thresholds \(0,3,4,8,11,12,16\). It checks the expected face vectors and connectedness; checks every edge has two triangles and every vertex link is a cycle at squared scale four; checks every one of the eighty claimed elementary collapse pairs is present, has codimension one and a unique immediate coface at the moment of removal; verifies exactly the eight-corner four-crosspolytope boundary remains; checks the seven opposite pairs at squared scale eleven; and checks universal cone vertices at squared scale twelve. It also checks the full simplex at squared scale sixteen.

The collapsing sequence is explicit finite evidence, not a stochastic experiment or a homology-rank heuristic. The proof of the integral barcode additionally uses standard geometric identifications of spheres, basic connected-graph homotopy and closed-surface classification. Full source-by-source originality and mathematical value comparisons are recorded in `AUDIT.json` and `REVIEW.md`; the checker alone makes no such judgments.

**Limits.** Only the stated finite Euclidean configuration is verified. No independent audit, equivariant reduction, wider family theorem, or publication-priority certificate is claimed.
