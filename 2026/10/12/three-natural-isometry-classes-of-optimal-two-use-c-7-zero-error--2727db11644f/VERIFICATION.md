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
# Verification

The standalone `verify.py` reconstructs the 49-vertex compatibility graph for two uses of the seven-cycle channel. It exhaustively counts target-size cliques, proving that size eleven is impossible and that exactly 980 size-ten codes exist. It then constructs the 392-element natural group \((D_{14}\times D_{14})\rtimes S_2\), computes canonical images of every maximum code, and obtains exactly three orbits of sizes \(392,196,392\) with stabilizers \(1,2,1\).

The verifier also recalculates all pairwise compatibility conditions, all orbit-stabilizer products, three pairwise-distinct cyclic-distance signatures, and a deterministic SHA-256 digest of the complete sorted maximum-code census.

Actual packaged replay:

`VERIFY_OK vertices=49 target11=0 maximum=10 labeled_maxima=980 group=392 orbits=3 orbit_sizes=392,196,392 stabilizers=1,2,1 nodes11=266991 nodes10=432900 census_sha256=7bedb501045012255db706cd7e32facf1e07891edeac480c48a721885fb0e3ab`

This is an exhaustive proof of the finite statement, not an inference from random sampling or from the published total 980. The independent external literature count is used only as a consistency check. The verification does not claim any result for higher strong powers or for Shannon capacity itself.
