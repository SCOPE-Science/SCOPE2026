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

Execute `python3 verify_hamming_swap.py` in the same folder. Standard Python 3 is sufficient; there are no downloaded datasets or external dependencies. Successful output is `VERIFY_OK {2: 1, 3: 14, 4: 63}`.

The program independently enumerates orbits in the original Hamming cube, tests all metric distances used by the orbit-complex adjacency rule, enumerates the complete flag complexes, independently reconstructs the core and checks its degree-one homology and all bridge triangles, and computes reduced homology by full binary-field boundary matrices for alphabets of sizes two, three, and four. It also verifies component counts at lower scales and the complete radius-three orbit graph. The unrestricted homotopy proof relies on explicit covering simplices, a good-cover nerve collapse, and the attaching-circle presentation; finite checks alone cannot establish its all-parameter conclusion. Integral homology and the sphere-wedge claim are established by the mathematical proof, not extrapolated from mod-two ranks. Independent review has not been performed.
