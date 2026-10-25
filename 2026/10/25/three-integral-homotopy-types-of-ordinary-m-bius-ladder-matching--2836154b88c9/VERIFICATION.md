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

# Verification protocol and limits

The computational proof is completely finite and reproducible with Python 3.8+ standard library by executing `python3 check_mobius_matching.py`. The output must match `CHECK_OUTPUT.txt` byte-for-byte. The program checks both independent face-enumeration procedures, covers every graph-edge incidence, builds all matching faces, and verifies the complete codimension-one Hasse directed acyclic graph under its stated matching.

The signed Morse boundary matrices are built from orientation-aware gradient-path eliminations. Their \(\partial^2=0\) identities are checked directly. Integer row and column operations use only unit pivots and confirm every remaining entry is zero, which certifies the absence of non-unit invariant factors. The expected matrix dimensions, integral ranks, critical-cell counts and independent full-chain mod-two Betti ranks are asserted in the program; failure causes a nonzero exit. The matrix hashes in stdout pin the exact signed matrices constructed by the package.

The program establishes claims for precisely \(n\in\{6,7,8\}\); it does not compute arbitrary larger cases or certify novelty. The conversion from these finite Morse CW complexes to wedge-of-spheres types uses the explicit homotopy-theoretic argument in RESULT.md, not just program output. External independent audit has not been performed.
