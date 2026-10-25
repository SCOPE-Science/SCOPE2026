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

# Reproducibility of the three-grain classification

Run `python3 verify.py` with standard Python 3. The verification has no third-party dependencies. Compare its stdout byte-for-byte with `verification_output.txt`.

The program independently simulates parallel sandpile firing from each binary triple. It enumerates translated maximal firing sets, rebuilds all simplicial edges and triangles, repeatedly removes an actual free edge with its unique incident triangle, inspects leftover tetrahedral boundaries, and compares connected components and integral graph-cycle ranks against the five-case formula. Every initial three-subset was checked for \(3\le n\le30\): 31,465 instances. Simplicial boundary ranks over \(\mathbb F_2\) were independently calculated for every instance with \(3\le n\le15\).

These tests check concrete finite instances and executable certificates of the collapse mechanism. They do not establish the result for untested \(n\); the general theorem is instead proved by the translation-orbit, free-face and edge-count arguments in `RESULT.md`. Integer homotopy types follow from explicit elementary collapses and tetrahedral boundary identifications; no inference from mod-two ranks to integral homotopy is made.

This package does not include an independent scientific audit or any external certification.
