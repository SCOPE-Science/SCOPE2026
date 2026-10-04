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

Run `python3 artifacts/verify.py`. The program uses only the Python standard library.

It reconstructs the entire complex from the definition “domination number at least \(3\)” on the \(15\) possible edges of a labeled six-vertex graph. It then rebuilds the explicit staged matching, checks all matching pairs and all Hasse cover relations, and topologically sorts the modified Hasse diagram to prove acyclicity.

The program performs exact integer algebraic Morse cancellation and verifies that the complete Morse boundary \(C_5^M\to C_4^M\) is the zero \(115\times24\) matrix. It separately computes the full ordinary simplicial boundary ranks over both \(\mathbb F_2\) and \(\mathbb F_3\), checks the Euler characteristic, and verifies the stated critical-cell counts.

A successful run ends with `D63_MIXED_WEDGE_VERIFY_OK`. The computation is exhaustive for this finite complex. It does not test or certify any statement for other parameters.
