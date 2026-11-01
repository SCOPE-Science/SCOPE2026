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

# Reproduce the finite certificate
Run `python3 verify.py` in a directory containing this file and `verify.py`. Only the Python 3 standard library is required; the program constructs the graph and complex itself without downloading any data.

The verifier independently checks the graph's sorted 24-edge list; all 11,393 nonempty faces, their disjoint-endpoint property and eight face counts; the 5,690 deterministic critical-pair removals and thirteen exact critical masks; the entire directed Hasse diagram with 55,256 incidences; the signed integral Morse boundary between the five four-cells and seven five-cells; all four-by-four minors and one unit three-by-three minor; and the original mod-two reduced simplicial homology. An acyclic matching plus the integral unit cancellation and the Hurewicz theorem establish the displayed **integral homotopy type**. A successful run prints four `VERIFY_OK` lines and exits normally.

This is a finite exhaustive certificate for the specifically defined 16-vertex ladder, not a finite-experiment extrapolation to larger ladders. It does not prove a uniform family theorem, an equivariant classification, or independent validation.
