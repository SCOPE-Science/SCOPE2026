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

# Finite verification

The executable certificate uses only Python 3's standard library. Place `verify_bp4.py` and `matching_certificate.json` in the same directory, then run `python3 verify_bp4.py`. `verification_output.txt` contains the output of the check actually executed on the packaged files.

The two independent full face enumerations agree on all 1,023 nonempty ten-bit subsets. They find 80 nonempty faces with face vector \((10,30,30,10)\) in dimensions zero through three. The explicit certificate contains 38 valid covering pairs and the four critical faces of dimensions \((0,2,3,3)\). The Hasse-directed gradient digraph contains 80 nodes and 190 arrows; exhaustive topological sorting visits all 80, establishing acyclicity. The top-facet partition and the two signed integral top-cycle boundaries are also checked exactly.

The topological deduction uses the standard acyclic-matching CW theorem and \(\pi_2(S^2)\cong\mathbb Z\). The computations certify one finite complex, not an infinite result. No formal proof-assistant certification, external expert validation or independent audit is implied.
