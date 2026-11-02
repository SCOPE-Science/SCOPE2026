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

# Reproducibility

Execute `python3 verify.py` using standard Python 3, without third-party packages. The script builds fragment-composition histograms directly from each indexed binary word, then independently builds the predicted fibers by capped gaps and stars-and-bars multiplicities. It compares the entire fibers (signature keys *and* multiplicities) for \(3\le n\le18\), \(0\le w\le\min(n,6)\), yielding 106 checked parameter pairs. It also checks the all-length three-marker finite table through length \(30\), the sharp threshold for weights \(1\) through \(8\), and all \(65\) nontrivial four-gap states partitioned into \(29\) signature classes. The reported terminal marker is `VERIFY_OK`.

The infinite theorem is established by locality of length-at-most-three windows, a disjoint gap partition, stars and bars, and the all-two-gap sharpness witness; finite testing alone is not used to infer any universal result. The enumeration of 65 capped patterns is exhaustive because every one of four coordinates lies in \(\{0,1,2\}\) and exactly the \(2^4\) all-short patterns are omitted. All math and tests refer to the attached version of `verify.py`.
