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
# Reproduction and limitations

Run `python3 verify_delta_affine.py` with the Python 3 standard library; no data downloads or third-party packages are required. The checker computes the semantic truth-set operation directly on all events for every labelled frame with \(1\le n\le4\) and at most two distinct outgoing successors, computes the corresponding bit-matrix dynamics independently, compares every tested iterate with \(\boldsymbol1+B^k x\), compares the first repeated matrix-power index with the rank stabilization index, and tests all admissible one- and two-world frames for period one.

Successful replay prints `all_frames_n=1 passed` through `all_frames_n=4 passed`, then `frame_count=15002 valuation_count=237068`, odd-cycle exact periods at sizes 3, 5, 7 and 9, and finally `VERIFY_OK`.

The checker also computes algebraic normal-form degrees on local rows of successor size 0 through 6 by a truth-table Möbius transform. The unrestricted formula for those degrees, the matrix-iteration identity, the exact Fitting classification, and the unbounded-period conclusion are proved symbolically in RESULT.md. In particular, 15,002 frame tests are not exhaustive over arbitrarily many worlds, and the four odd-cycle instances are not proofs of the lower bound for every odd size.

Independent scientific auditing or formal verification has not been performed. Historical coincidence with an inaccessible full text has not been excluded.
