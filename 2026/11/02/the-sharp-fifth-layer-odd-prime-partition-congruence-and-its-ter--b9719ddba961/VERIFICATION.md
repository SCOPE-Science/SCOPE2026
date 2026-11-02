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

The formal power-series proof is in RESULT.md. The bundled `verify.py` uses only the Python standard library, reconstructs the degree-ten rational-polynomial extraction coefficients exactly, and checks the specialized ternary numerator. Additional separate numerical comparisons use the defining recurrence for partition counts with four odd prime bases and eight progression values per base. The verifier does not replace the all-index proof, and no external independent validation has been performed.
