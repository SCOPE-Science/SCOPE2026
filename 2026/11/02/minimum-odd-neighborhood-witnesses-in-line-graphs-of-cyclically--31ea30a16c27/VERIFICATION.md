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

Run `python3 check_flip_linegraphs.py` and `python3 check_cubic_cut_certificates.py` using Python 3. Both programs are complete, require only the standard library, and independently construct the named graphs.

The direct line-graph checker evaluates every selected-edge subset of cardinality 1–5, enough to rule out any smaller support because support necessarily includes the selected set. It reports Petersen 33, Heawood 21 and dodecahedral 42 minimum supports, all of size five. The independent graph-cut checker evaluates all cut shores in these graphs, verifies the three/four-edge cut structure and gives five-cycle counts 12, 0 and 12. It also distinguishes nontrivial cyclic cuts from trivial forest shores.

The theorem for every graph in the stated infinite family follows from the self-contained parity and small-cut argument, not from extrapolating these finite verifications. A graph-state stabilizer weight is not, by itself, the distance of an encoded quantum error-correcting code. An independent scholarly audit has not been performed.
