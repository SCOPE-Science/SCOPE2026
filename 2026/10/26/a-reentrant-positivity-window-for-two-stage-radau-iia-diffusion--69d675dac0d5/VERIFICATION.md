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
# Verification details

Execute `python verify.py` from the extracted package with the versions in `requirements.txt`. The exact SymPy verification completes with:

`VERIFY_OK: 7 polynomial identities; exact R(L) entry replay 5879 entries; q=4 witness -4/323; 27 exact q-witnesses`

The verifier checks the three rational entry-orbit identities, fixed-degree sign identities, the small-root limit, and direct evaluations of a rational matrix expression constructed from the adjacency matrix for factor orders 2 through 6. The direct matrix calculations encompass 5,879 exact entries, with row sums checked. It also checks the exact witness \(-4/323\) and negative test values \(D_q(q)<0\) for integer \(q\) from 4 through 30. These finite tests **do not** establish the theorem for every graph order. The analytical projector/sign proof in `RESULT.md` establishes the uniform result; the limiting cutoff claims use rigorous polynomial scaling, not numerical extrapolation.

Verification is internal to the supplied mathematical package. No independent audit or external verification has occurred.
