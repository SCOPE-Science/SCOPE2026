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

The finite-field checker `verify.py` is standalone and requires only Python 3. It uses ordinary integer bit operations for binary matrix multiplication and Gaussian elimination, and explicit irreducible-polynomial arithmetic for finite fields of orders \(2\), \(4\), and \(8\).

Direct exhaustive enumeration was performed for every one of the 530 structure matrices in dimensions one, two, and three and for each extension degree \(f\in\{1,2,3\}\). It also enumerated the full vector spaces for the five-cycle over fields of sizes \(2\), \(4\), and \(8\), and the Petersen graph over fields of sizes \(2\) and \(4\). All counts matched binary kernel ranks. The standalone script reported `VERIFY_OK`.

The general theorem depends on the normal basis theorem and the Fitting decomposition, proved in `RESULT.md`; exhaustive small-field checks are supporting evidence and do not establish the infinite quantifiers. The polynomial greatest-common-divisor specialization follows from the elementary ideal structure of \(\mathbb F_2[t]\). The displayed zeta factors follow from the same exact rank identities; no floating-point arithmetic was used.
