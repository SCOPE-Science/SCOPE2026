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

# Reproducible verification

Run `python3 verify.py` with Python 3 and the standard library. The script contains full tables for \(a\leftrightarrow b\) and \(a\widetilde\wedge b\); it imports no external results or data files.

The replay exhaustively screens **15,024** top-preserving scalar mappings for all \(2\le m,n\le6\), identifies exactly the predicted morphisms, and checks their count. It independently screens **72,380** mappings from five Cartesian-product sources to chain targets, including all functions for sources \((A_2,A_2)\), \((A_2,A_3)\), and \((A_3,A_3)\) after the necessary preservation-of-top filter. It checks all \(4^4\) maps on the Boolean square for endomorphisms, idempotents and units; the counts are **9, 6 and 2**, respectively.

The code generates **811** endomorphism tables from the asserted normal form, evaluates both operations on **457,673** ordered argument pairs, and checks pointwise idempotence against the symbolic rooted-star criterion. It confirms the finite-sum idempotent formula in feasible ranks through four and verifies the EGF's coefficients independently by exact rational formal-power-series arithmetic through rank six and chain size six. The final deterministic replay line is:

`VERIFY_OK_CERTIFIED 934995 exact assertions; 15024 scalar maps screened; 72380 product-to-chain maps screened; 811 product endomorphism tables checked on 457673 ordered pairs, each with both operations; EGF checked m<=6, r<=6`

**Scope of certification:** these are finite computational stress tests. They do not prove the theorem for unbounded rank or size and are not external or independently conducted mathematical review. The general theorem follows from the proof in `RESULT.md`.
