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

For all integers \(n\ge7\), the paper provides a direct homotopy proof, using the published shellability result for the four-row chessboard complex. The attached program is a separate, exhaustive finite consistency check only.

Execute `python3 verify_bidirected_multipath.py` from the extracted artifact directory. Compare its standard output to `verify_output.txt`. The program lists all possible arc subsets of sizes one through four without using the paper's bent-edge decomposition; it checks in/out degree limits and directed-cycle absence, constructs mod-two boundary matrices, and compares face numbers to explicit formulas.

Widths four through nine are exhaustively checked; for widths seven, eight and nine the reduced mod-two homology is concentrated in degree three of ranks 491, 1105 and 2143. These checks do not assert integral torsion freedom or homotopy equivalence for arbitrary widths: those follow from the noncomputational proof.

Independent audit: not performed.
