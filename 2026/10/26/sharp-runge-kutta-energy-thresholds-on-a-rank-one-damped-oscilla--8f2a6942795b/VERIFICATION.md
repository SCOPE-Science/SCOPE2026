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

The executable `verify.py` checks the exact symbolic identities, polynomial shifts, rational boundary comparisons, and finite rational samples directly from the defining \(2\times2\) generator. It uses Python and SymPy and does not require numerical eigensolvers or external inputs. Execute `python verify.py` after extracting the file.

The universal conclusions use the explicit sign proofs and monotonicity identities given in `RESULT.md`; finite rational checks cannot prove global inequalities. Publication priority and behavior for other matrices are unverified beyond the stated comparisons.
