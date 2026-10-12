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

Run `python3 verify.py` with a standard Python 3 interpreter; no third-party packages are required.

The verifier builds all \(64\) words in \(\{0,1,2,3\}^3\). It evaluates the literal \(2\)-traceability condition for every three-codeword subset, obtaining \(14{,}016\) compatible triples out of \(41{,}664\). Because every violation is witnessed by two parents and one outside codeword, a larger code is valid exactly when each of its three-subsets is compatible.

All \(635{,}376\) four-subsets are then tested, producing exactly \(27{,}696\) maxima. The literal parent/descendant/nearest-codeword definition is replayed again on every enumerated maximum. A complete recursive size-five search rejects every possible extension, so the maximum is exactly \(4\).

For equivalence, adjacent symbol transpositions in each coordinate and adjacent coordinate transpositions generate the order-\(82{,}944\) Hamming-isometry group. Orbit closure partitions the full maximum list into sizes \(48,288,576,2592,3456,10368,10368\); no maximum lies outside those seven orbits.

The canonical newline-terminated census digest is `b22fb6b34d0cca55a2b161541233bcf81435a8d81d55122fc7c8e0c8263c9779`.

Expected first output line:

`VERIFY_OK vertices=64 good_triples=14016 maximum=4 labeled_maxima=27696 natural_group=82944 orbits=7 orbit_sizes=48,288,576,2592,3456,10368,10368 stabilizers=1728,288,144,32,24,8,8 maxima_sha256=b22fb6b34d0cca55a2b161541233bcf81435a8d81d55122fc7c8e0c8263c9779`
