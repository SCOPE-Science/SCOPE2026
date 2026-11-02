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

The standalone `verify.py` forms the radical-square-zero algebra multiplication for every basis coordinate in each listed finite case. For each element it constructs the full linear map given by its commutator with each algebra basis element and computes its rank using finite-field row reduction. The result is compared with an independently implemented graph-support prediction. The number of commuting ordered pairs is cross-checked against a separate edge-subset sum. Both the binary field and a nonprime field of four elements are implemented with explicit arithmetic; tests also cover the three-element field.

Eight exhaustive configurations: one arrow over order two; both forward and fork orientations of a three-vertex path over order two; the fork over order four; a three-cycle over order three; two parallel arrows over order three; and complete graphs on four and five vertices over order two. The last case checks all 32,768 elements and its rank histogram for ranks 0 through 9 is (2,20,110,460,1616,960,4320,11200,8960,5120). Executing `python verify.py` prints `VERIFY_OK 8 direct exhaustive configurations`. The code needs no third-party dependency.

The mathematical proof covers all finite loopless quivers and prime powers, whereas the program checks only these finite inputs. No independent mathematical audit or general-purpose formal certification has been performed. The external publication overlap checks and historical-coverage limitations appear in REVIEW.md and AUDIT.json.
