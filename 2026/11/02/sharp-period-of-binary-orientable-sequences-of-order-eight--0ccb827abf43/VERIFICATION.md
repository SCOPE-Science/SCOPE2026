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

# Exact certificate verification

Run `python3 verify.py` next to `certificate.json`. No third-party libraries, network or optimization engines are needed. The verifier reconstructs the 240 admissible eight-bit arcs and 120 reversal pairs, checks the palindromic-vertex identity exhaustively in its local four-arc universe, checks 240 integer inequalities from the explicitly supplied potentials, and confirms that their reversal-pair multipliers total 92. It also checks all 92 cyclic windows of the witness and the balance of the corresponding de Bruijn circuit.

The arithmetic proof is valid for any candidate binary cyclic word of order eight; the witness verifies attainability. The finite certificate is not an asymptotic theorem, and it makes no claim about periods at other window lengths or about the enumeration of optimal cycles.
