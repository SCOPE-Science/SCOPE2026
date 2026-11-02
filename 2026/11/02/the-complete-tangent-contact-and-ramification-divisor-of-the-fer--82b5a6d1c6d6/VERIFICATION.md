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

The theorem has been checked by reconstruction of the Frobenius factorization, polar tangent criterion, norm-fibre counting, and exact local Hasse–Wronskian orders. The independent `verify_contacts.py` script exhaustively checks the points and all Taylor coefficients over \(\mathbb F_8\), \(\mathbb F_{27}\), \(\mathbb F_{64}\), and \(\mathbb F_{125}\). In the separate \(q=2\) test over \(\mathbb F_{64}\), nonflexes occur and all have exactly order-two tangency, providing a check beyond the rational support.

To reproduce: run `python verify_contacts.py` with Python 3. A successful run ends with `FERMAT_NORM_FLEX_EXHAUSTIVE_CONTACTS_OK`. The proof is algebraic for every prime power and does not depend on extrapolation from these tests. No independent external review, formal proof certificate, or exhaustive search of all historical literature is claimed.
