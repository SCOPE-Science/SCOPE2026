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

# Reproducibility and limitations

Run `python3 verify_projective_cech.py` in a folder containing the supplied standalone verifier. The program requires Python 3 standard library only. It independently reconstructs \(\mathrm{PG}(2,2)\) and \(\mathrm{PG}(2,3)\), checks plane axioms, graph distances and distance-two Čech generators, verifies each free-face pair in the two auxiliary line complexes, and checks their cycle ranks. It completely enumerates the order-two scale-four Čech complex, checks the exact join intersection, and uses binary boundary-matrix elimination to check all mod-two homology groups.

Observed output is in `verification_output.txt`, ending `VERIFY_OK`. At order two, 7,919 nonempty faces yield reduced Betti vector \((0,0,0,0,64,0,0,0,0,0)\). At order three, the script checks 26 maximal Čech facets and auxiliary cycle rank \(27\) in each factor. The predicted order-three rank \(729\) follows from the general proof, **not** from a full order-three homology computation. The code uses only prime-field coordinate planes, whereas the theorem covers all finite projective planes by the axiomatic collapse and homotopy-pushout proof in `RESULT.md`.

No third-party review or independent mathematical validation has been performed. Verification is not an infinite-order computational certificate and makes no assertion about unexamined bibliographic sources.
