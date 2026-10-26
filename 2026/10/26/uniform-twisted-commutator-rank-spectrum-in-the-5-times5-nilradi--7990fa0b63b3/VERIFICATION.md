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

# Reproducibility and verification

Run the self-contained `verify.py` with standard Python 3. The checker constructs the twisted commutator coefficient matrix, enumerates every normalized first-superdiagonal support and all five remaining coordinates, and checks the complete rank histogram, polynomial totals, and fixed-flag pair count. It uses explicit tables for the four-element field and ordinary modular arithmetic for the prime fields, without external dependencies.

Completed exhaustively on fields of sizes 2, 3, 4, 5 and each nonzero twist parameter: `TWISTED_FLAG_RANKS_OK`.

The general theorem is supported by the separately stated field-independent row reductions and weighted mask sum. Finite enumerations alone do not establish its infinitely many field cases. No independent audit has been performed. The bibliographic coverage is bounded, and a relevant 2005 canonical-form source was not available in full text.
