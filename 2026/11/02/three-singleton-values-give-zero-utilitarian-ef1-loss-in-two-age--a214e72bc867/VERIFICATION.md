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

# Verification of the mixed-manna three-level theorem

The accompanying `verify.py` can be run using `python3 verify.py` without external packages. The test uses exact integer arithmetic and a direct, bundle-wise EF1 definition, including both permitted ways to eliminate mixed-manna envy: removing a positively valued item from the other bundle or a negatively valued item from one's own bundle.

The executable enumerates 488,275 small signed item sequences across five three-level alphabets at lengths one to seven, of which 117,995 meet the equal-total condition. In every eligible case, it checks the explicit algorithm's EF1 property and exact itemwise-optimal welfare. Independently, it enumerates all two-way allocations for 3,186 selected eligible profiles and compares maximum EF1 welfare to the unrestricted maximum. A further 50,000 seeded random profiles are generated; 13,555 meet the equal-total condition and are checked. As a boundary check, it exhaustively searches all allocations for six published four-level counterexample instances indexed by integers two through seven, verifying unrestricted and EF1-constrained welfare exactly.

These finite tests are not a proof for all item counts or arbitrary real values. The universally quantified proof is contained in RESULT.md: it uses equal directed-pair counts, the signed common-item witness invariant and explicit envy-gap equations. Computations do not verify that all equivalent prior formulations have been indexed. This document reports no independent audit or external certification.
