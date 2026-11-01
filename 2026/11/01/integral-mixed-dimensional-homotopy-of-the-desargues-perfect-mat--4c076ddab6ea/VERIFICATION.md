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

# Verification scope

Run `python3 verify_desargues_perfect.py` next to this file. This fully self-contained Python 3 program performs exact integer and Boolean calculations without any third-party packages. `VERIFY_OUTPUT.txt` holds its recorded output.

The program computes two independent perfect-matching counts (both sixty), enumerates all \(113{,}192\) ordinary matchings and tests extendibility by residual-vertex dynamic programming, and obtains \(44{,}282\) faces including the empty face. It constructs \(22{,}124\) valid matched covers, checks all \(244{,}830\) nonempty-face Hasse incidences and visits each of the \(44{,}281\) nonempty faces in a complete topological sort. The remaining critical cells have dimensions zero (one), three (thirty-one), and four (one). Its signed integral projection gives thirty-one zero coefficients in the only possible Morse boundary, and direct mod-two boundary-rank calculations independently give ranks thirty-one and one in dimensions three and four.

The integral homotopy inference also uses the standard discrete-Morse CW theorem and the identification \(\pi_3(\bigvee^{31}S^3)\cong\mathbb Z^{31}\); these are mathematical arguments, not properties tested by a finite-field computation. The proof does not establish anything about other generalized Petersen graphs. Independent external audit has not been performed.
