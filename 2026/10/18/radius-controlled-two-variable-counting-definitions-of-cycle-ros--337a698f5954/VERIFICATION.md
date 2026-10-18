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

The attached proof applies to arbitrary finite roses with at least two petals; the listed finite checks corroborate it without certifying all infinite parameters. Run `python rose_check.py` from the extracted file directory: four petal-length samples reproduce their input multiplicities and 30 explicit lower-bound pairs have equal common-palette refinement histograms through the claimed round. Run `python global_small_check.py`: among all \(2^{10}=1024\) labelled graphs at five vertices and \(2^{15}=32768\) labelled graphs at six vertices, the target rose patterns agree only with their isomorphic copies under the claimed rank bound (15 and 180 labelled copies respectively). Code uses integer colour interning, not probabilistic hashes. The all-size proof is in RESULT.md. Independent audit has not been performed.
