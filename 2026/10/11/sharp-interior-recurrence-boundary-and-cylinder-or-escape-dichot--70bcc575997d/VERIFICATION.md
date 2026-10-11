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

The included `check_es9.py` verified exact SymPy polynomial identities for the cylinder factor and Lyapunov functions, together with rational-parameter exact equilibrium and endpoint substitutions. Run `python check_es9.py` with SymPy installed. The program's successful assertions do not independently certify the mathematical argument or settle originality.

The non-crossing property, global existence, compact-invariance exclusion, sharpness and bounded-orbit dichotomy were checked analytically in `RESULT.md`. In particular, completeness uses \(|z'|\le1+|b|\) inside the cylinder; the limiting alternative uses integrability and uniform continuity of the cylinder factor. The proof concerns only the open interior, not its exterior. No external audit or independent validation was performed.
